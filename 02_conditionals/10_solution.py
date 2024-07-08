age=3
animal1="dog"
animal2="cat"

animal_choice=input("dog \n")

if animal_choice=="dog":
    if age<2:
        print(" Puppy food")
if animal_choice=="cat":
    if age>5:
        print("senior cat food")