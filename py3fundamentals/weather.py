condition = input("What is the condition (rainy, sunny, other)? ")
temp = int(input("What is the temperature? "))

if (condition == 'sunny' and temp >= 90):
    print("It's too hot!")
    print("Stay inside!")
elif condition == 'rainy':
    print("It's raining!")
    print("Stay inside!")
else:
    print("Go outdoors!")    

