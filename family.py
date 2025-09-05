def father( option):
    if option == 'yes':
       print("if you had lived what I lived you would not dare talk to me like that")
    else:
       print("You show no respect")


def mother(option):
    if option == 'yes':
        print("did you clean your room?")
    else:
        print("Go looking for something to clean")


def sister(option):
    if option == 'yes':
        print("No you are wrong")
    else:
        print("Whatever you want to say you are wrong")


def brother(option):
    if option == 'yes':
        print("do you want to fight with me ")
    else:
        print("talk to me come on talk!!")


user_input = input("Good morning, tell me who do you want to talk to, father, mother, sister, brother\n")

if user_input == "father":
    ans=input("Are you sure please answer with yes or no ")
    if ans == "yes":
        father("yes")
    else:
        father("no")
elif user_input == "mother":
    ans=input("Are you sure please answer with yes or no ")
    if ans == "yes":
        mother("yes")
    else:
        mother("no")
elif user_input == "brother":
    ans=input("Are you sure please answer with yes or no ")
    if ans == "yes":
        brother("yes")
    else:
        brother("no")
elif user_input == "sister":
    ans=input("Are you sure please answer with yes or no ")
    if ans == "yes":
        sister("yes")
    else:
        sister("no")
else:
    print("I don't get it ")
   