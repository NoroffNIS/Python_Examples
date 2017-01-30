
def km_h_to_m_s():
    print('You choose to convert km/t -> m/s')
    km_h = float(input('Type in a km/h:'))
    m_s = km_h * 0.2778
    print(km_h, 'km/h = ', m_s,'m/s', sep='')

def m_s_to_km_h():
    print('You choose to convert m/s -> km/t')
    m_s = float(input('Type in a m/s:'))
    km_h = m_s * 3.6
    print(m_s, 'm/h = ', km_h, 'km/s', sep='')

def main():
    print('What do you wan to do?')
    user_choise = input('Type 1 for km/t -> m/s\n'
                        'Type 2 for m/s -> km/t\n>')
    print('Your choise is:', user_choise)

    if user_choise == '1':
        km_h_to_m_s()
    elif user_choise == '2':
        m_s_to_km_h()
    else:
        print('You typed in wrong!')

main()

