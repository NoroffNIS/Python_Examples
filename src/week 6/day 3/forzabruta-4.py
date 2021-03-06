import requests
from threading import Thread
import sys
import time
import getopt
import re
import hashlib
from sys import platform
from termcolor import colored




def banner():
    print("\n***************************************")
    print("* ForzaBruta 0.3*")
    print("***************************************")


def usage():
    print("Usage:")
    print("		-w: url (http://somesite.com/FUZZ)")
    print("		-t: threads")
    print("		-f: dictionary file\n")
    print("example: forzabruta.py -w http://www.targetsite.com/FUZZ -t 5 -f common.txt\n")


class request_performer(Thread):
    def __init__(self, word, url, hidecode):
        Thread.__init__(self)

        try:
            self.word = word.split("\n")[0]
            self.urly = url.replace('FUZZ', self.word)
            self.url = self.urly
            self.hidecode = hidecode
        except Exception as e:
            print('Thread error:',e)

    def run(self):
        try:
            start = time.time()
            r = requests.get(self.url)
            elaptime = time.time()
            totaltime = str(elaptime - start)
            lines = str(r.content.count(b'\n'))
            chars = str(len(r._content))
            words = str(len(re.findall(b"\S+", r.content)))
            code = str(r.status_code)
            hash = hashlib.md5(r.content).hexdigest()

            if r.history != []:
                first = r.history[0]
                code = str(first.status_code)
            else:
                pass

            if self.hidecode != code:
               if platform == "win32":
                   print('{:.8}'.format(totaltime), "  \t", code, "\t", chars, "\t", words, "\t", lines, "\t", hash,
                         "\t", '{:10}'.format(self.word), "\t", self.url)
               elif platform == "darwin" or platform == "linux" or platform == "linux2":
                   if '200' <= code < '300':
                       print('{:.8}'.format(totaltime), "  \t", colored(code, 'green'), "\t", chars, "\t", words, "\t", lines, "\t", hash,
                             "\t", '{:10}'.format(self.word), "\t", self.url)
                   elif '400' <= code < '500':
                       print('{:.8}'.format(totaltime), "  \t", colored(code, 'red'), "\t", chars, " \t", words, "\t", lines, "\t",
                             hash, "\t", '{:10}'.format(self.word), "\t", self.url)
                   elif '300' <= code < '400':
                       print('{:.8}'.format(totaltime), "  \t", colored(code, 'blue'), "\t", chars, "\t", words, "\t", lines, "\t", hash,
                             "\t", '{:10}'.format(self.word), "\t", self.url)

            else:
                pass
            i[0] = i[0] - 1  # Here we remove one thread from the counter

        except Exception as e:
            print('Run error', e)

def start(argv):
    banner()
    if len(sys.argv) < 5:
        usage()
        sys.exit()
    try:
        opts, args = getopt.getopt(argv, "w:f:t:c:")
    except getopt.GetoptError:
        print("Error en arguments")
        sys.exit()
    hidecode = 000
    for opt, arg in opts:
        print(opt,'=',arg)
        if opt == '-w':
                url = arg
        elif opt == '-f':
                dict = arg
        elif opt == '-t':
                threads = int(arg)
        elif opt == '-c':
                hidecode = arg
    try:
        f = open(dict, "r")
        words = f.readlines()
    except:
        print("Failed opening file: " + dict + "\n")
        sys.exit()

    launcher_thread(words, threads, url, hidecode)


def launcher_thread(names, th, url, hidecode):
    global i
    i = []
    resultlist = []
    i.append(0)
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("Time" + "\t\t" + "Code" + "\tChars \t Words \tLines \t",'{:32}'.format('MD5')," \t Site \t\t URL \t\t ")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    while len(names):
        try:
            if i[0] < th:
                n = names.pop(0)
                i[0] = i[0] + 1
                thread = request_performer(n, url, hidecode)
                thread.start()

        except KeyboardInterrupt:
            print("ForzaBruta interrupted  by user. Finishing attack..")
            sys.exit()
        thread.join()
    return


if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print("ForzaBruta interrupted by user, killing all threads..!!")
