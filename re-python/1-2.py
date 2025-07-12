print(" *** Wind classification ***")

windSpeed = float(input('Enter wind speed (km/h) : '))

if 0 <= windSpeed <= 51.99 :
    print("Wind classification is Breeze.") 
elif 52.00 <= windSpeed <= 55.99 :
    print("Wind classification is Depression.")
elif 56.00 <= windSpeed <= 101.99 :
    print("Wind classification is Tropical Storm.")
elif 102.00 <= windSpeed <= 208.99 :
    print("Wind classification is Typhoon.")
elif windSpeed >= 209 :
    print("Wind classification is Super Typhoon.")
