#my own stupid function - but not working -  see expo_func2.py
def raise_to_pow(base, expo):
    return(base ** expo)

base_ = float(input("Enter Base Number :"))
expo_ = float(input("Enter Exponential Number: "))
res=raise_to_pow(base_, expo_)
print("Exponential value is : " + str(res))
