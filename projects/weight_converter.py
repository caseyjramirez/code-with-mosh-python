import math

weight = input('Weight: ');
type = input('(L)bs or (K)g: ')


if type.lower() == 'l':
    converted_weight = float(weight) * 0.453592;
    print(f'You are {math.floor(converted_weight)} Kilos');
elif type.lower() == 'k':
    converted_weight = float(weight) * 2.20462;
    print(f'You are {math.floor(converted_weight)} Pounds');
else:
    print('Entry not processible');