print('   Tablas de Verdad')
print('Introduzca la operacion boolena que desea')
n = str(input())

if ((n=='and')or(n=='AND')or(n=='And')):
    print('F   F | F ')
    print('F   V | F ')
    print('V   F | F ')
    print('v   V | V ')
if ((n=='or')or(n=='OR')or(n=='Or')):
    print('F   F | F ')
    print('F   V | V ')
    print('V   F | V ')
    print('V   V | V ')
if ((n=='not')or(n=='NOT')or(n=='Not')):
    print('V  |  F')
    print('F  |  V')

