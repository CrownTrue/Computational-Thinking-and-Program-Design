high=input("身高:")
weigh=input("體重:")
high=int(high)
weigh=int(weigh)
BMI=weigh/(high**2)
if BMI>24:
    print("過重")
else:
    print("沒有過重")