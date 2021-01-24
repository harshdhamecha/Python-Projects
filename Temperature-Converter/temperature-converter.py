def to_fahrenheit(temperature):
    resultant_temp = round(((9 / 5) * temperature) + 32, 2)
    print(f'{temperature}°C = {resultant_temp}°F')

def to_celsius(temperature):
    resultant_temp = round((5 / 9) * (temperature - 32), 2)
    print(f'{temperature}°F = {resultant_temp}°C')

while True:
    conversion = input('Press 1: For Celsius to Fahrenheit conversion and\nPress 2: For Fahrenheit to Celsius conversion\n')
    if conversion == '1' or conversion == '2':
        print('WARNING: Enter only the numeric value below in the temperature')
        temperature = float(input('Enter the temperature: '))
        conversions = {'1': to_fahrenheit, '2': to_celsius}
        conversions[conversion](temperature)
    else:
        print('You\'ve wrongly pressed a key other than 1 or 2.')
    decision = input('Would you like to try again(y/n)? ').lower()
    if decision != 'y':
        break