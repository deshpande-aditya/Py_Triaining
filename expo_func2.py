##try code from video - using R loop
def raise_to_pow(base, pow):
    res=1
    for index in range(pow):
        res=res * pow
    return res
print(raise_to_pow(2, 2))