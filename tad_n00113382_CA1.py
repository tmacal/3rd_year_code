import time

def voltCalc():
    while True:
        try:
            i = float(input('*Enter current in Amps: '))
            i = abs(i)
            r = float(input('*Enter resistance in Ohms: '))
            r = abs(r)
            wrapper1()
            print('Result: ')
            return i * r, ' Volts ', ((i ** 2) * r), ' Watts'
        except Exception as e:
            print("Input should be a number")
            continue

def currentCalc():
    while True:
        try:
            v = float(input('*Enter voltage in Volts: '))
            v = abs(v)
            r = float(input('*Enter resistance in Ohms: '))
            r = abs(r)
            wrapper1()
            print('Result: ')
            return v / r, ' Amps ', (v ** 2 / r), ' Watts'
        except Exception as e:
            print("Input should be a number")
            continue

def resCalc():
    while True:
        try:
            i = float(input('*Enter current in Amps: '))
            i = abs(i)
            v = float(input('*Enter voltage in Volts: '))
            v =  abs(v)
            wrapper1()
            print('Result: ')
            return v / i, ' Ohms ', (v * i), ' Watts'
        except Exception as e:
            print("Input should be a number")
            continue
##Planned separate function for power - included in ohmsLaw calculations instead
# def powerCalc(v, i, r):
#     return (v * i) or (v ** 2 / r) or ((i ** 2) * r) ##TODO: logic here - same as ohmslawtest?

baseOptions= [
    'resistorval',
    'ohmslaw'
]
nestedOptions= {
    'voltage': voltCalc,
    'current': currentCalc,
    'resistance': resCalc,
}
colours = {
    'black' : 0 ,
    'brown' : 1 ,
    'red' : 2 ,
    'orange' : 3 ,
    'yellow' : 4 ,
    'green' : 5 ,
    'blue' : 6 ,
    'violet' : 7 ,
    'purple' : 7,
    'grey' : 8 ,
    'gray' : 8 ,
    'white' : 9 , }

asciiArt = [
    ('#######  ##    #  #########  ##     #   ########   ##      ##'),
    ('##    #  ##    #      ##     ##     #   ##     #   ###     ##'),
    ('##    #  ##    #      ##     ##     #   ##     #   # ##    ##'),
    ('#######  #######      ##     ########   ##     #   #  ##   ##'),
    ('##            ##      ##     ##     #   ##     #   #   ##  ##'),
    ('##            ##      ##     ##     #   ##     #   #    ## ##'),
    ('##            ##      ##     ##     #   ##     #   #     ####'),
    ('##            ##      ##     ##     #   ########   #      ###'),
]
def wrapper(): print ('***************************************************************')
def wrapper1(): print ('===============================================================')

def ohmsLaw():
    nestedOptionsStr = (' || '.join(map(str, nestedOptions)))
    wrapper()
    print(nestedOptionsStr)
    wrapper()
    choice = input("Enter one of the above options: ")
    wrapper()

    if choice in nestedOptions:
        wrapper1()
        print('You have selected ' + choice)
        wrapper1()
        resultStr = (' '.join(map(str, (nestedOptions[choice]()))))
        print (resultStr)
        wrapper1()
    else:
        print("not in list")

def resistorCalculator():
    resArray = []
    while True:
        try:
            num1 = input ("Enter first colour: ") ##wait for input
            if num1 in colours:
                num1 = colours[(num1)]
                resArray.append(num1) ##append input val to array if in dictionary
            else:
                print("not in list")
                continue
        except ValueError:
            print("something went wrong")
        try:
            num2 = input ("Enter second colour: ")
            if num2 in colours:
                num2 = colours[(num2)]
                resArray.append(num2)
            else:
                print("not in list")
                continue
        except ValueError:
            print("something went wrong")
        try:
            num3 = input ("Enter third colour: ")
            if num3 in colours:
                num3 = colours[(num3)]
                resArray.append((num3)*str(0))
                resArrayStr = (''.join(map(str, resArray))) ##Clean up array - remove commas - whitespace
                wrapper1()
                print (('Value: ') + resArrayStr.lstrip('0')+' Ohms') ##Strip leading zeros from resArrayStr
                break
            else:
                print("not in list")
                continue
        except ValueError:
            print("something went wrong")

def Main():
    count = -1
    for i in range((len(asciiArt))):
        time.sleep(0.3)
        count += 1
        print (asciiArt[count])
    while True:
        try:
            baseOptionsStr = (' || '.join(map(str, baseOptions)))
            wrapper()
            print (baseOptionsStr)
            wrapper()
            option = input('Enter one of the above options: ')
            option = option.casefold() ##Make case insensitive
            if option in baseOptions:
                wrapper1()
                print('You have selected: ' + option)
                wrapper1()
            if option == 'resistorval':
                resistorCalculator()
            elif option == 'ohmslaw':
                ohmsLaw()
        except Exception as e:
            print("selection not in list")
            continue

##Main loop
try:
    Main() ##Call main function
except KeyboardInterrupt:
    print('__________Goodbye__________')
    pass
