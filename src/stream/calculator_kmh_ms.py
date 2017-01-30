

def kmh_ms(kmh):
    ms = kmh * 0.277
    return ms


def ms_kmh(ms):
    kmh = ms * 3.6
    return kmh

temp = float(input('Type in the speed:'))

ms = kmh_ms(temp)
print(temp, 'km/h is', ms, 'm/s')


kmh = ms_kmh(temp)
print(temp,'m/s is', kmh,'km/h')