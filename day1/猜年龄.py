age_of_oldboy = 56
guess_age = int(input ("guess age"))

if age_of_oldboy == guess_age:
    print("yes,you got it ")
elif guess_age > age_of_oldboy:
    print("think smaller")
else:
    print("think bigger")
