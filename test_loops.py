#using boolean
#is_male = input(" Enter True or False: Are you  male? :")
#is_tall = input(" Enter True or False: Are you  male? :")
is_male=False
is_tall=False

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are a not male but tall")
else:
    print("You are not a male and not tall")