print("Welcome to Health Management system")
print("There are 3 clients in my Gym ")


def getdate():
    import datetime
    return datetime.datetime.now()


MYclient = ["Kartikey", "Vanya", "Special"]
print(MYclient)
while(1):
    n = int(input("What do you want to do ?\n"
              "1. Lock DATA\n"
              "2. Retrieve DATA\n"
              "3. Exit\n"))
    if n == 1:
        name = input("Enter the name of client\n")
        if name == "Kartikey":
            choice = int(input("For what you are looking forward\n"
                               "1. For Exercise\n"
                               "2. For Diet\n"))
            if choice == 1:
                with open("Kartikey_Ex.txt", "a") as f:
                    write = f.write(str([str(getdate())]) + " : " + input("Write the Exercise here  ") + " \n ")
            elif choice == 2:
                with open("Kartikey_diet.txt", "a") as f:
                    write = f.write( str([str(getdate())])+ " : " + input("Write the Diet Plan here  ") + " \n ")
            else:
                print("Invalid Choice\n")

        elif name == "Vanya":
            choice = int(input("For what you are looking forward\n"
                               "1. For Exercise\n"
                               "2. For Diet\n"))
            if choice == 1:
                with open("Vanya_Ex.txt", "a") as f:
                    write = f.write(str([str(getdate())]) + " : " + input("Write the Exercise here  ") + " \n ")
            elif choice == 2:
                with open("Vanya_diet.txt", "a") as f:
                    write = f.write(str([str(getdate())]) + " : " + input("Write the Diet Plan here  ") + " \n ")
            else:
                print("Invalid Choice\n")

        elif name == "Special":
            choice = int(input("For what you are looking forward\n"
                               "1. For Exercise\n"
                               "2. For Diet\n"))
            if choice == 1:
                with open("special_Ex.txt", "a") as f:
                    write = f.write(str([str(getdate())])+ " : " + input("Write the Exercise here   ") + " \n ")
            elif choice == 2:
                with open("special_diet.txt", "a") as f:
                    write = f.write(str([str(getdate())]) + " : " + input("Write the Diet Plan here   ") + " \n ")
            else:
                print("Invalid Choice\n")

        else:
            print("Client Does not exist\n")


    elif n == 2:
        name = input("Enter the name of client\n")
        if name == "Kartikey":
            choice = int(input("For what you are looking to see\n"
                               "1.  Exercise PLAN\n"
                               "2.  Diet PLAN\n"))
            if choice == 1:
                with open("Kartikey_Ex.txt", "r") as f:
                    print(f.read())
            elif choice == 2:
                with open("Kartikey_diet.txt", "r") as f:
                    print(f.read())
            else:
                print("Invalid Choice\n")

        elif name == "Vanya":
            choice = int(input("For what you are looking forward\n"
                               "1.  Exercise PLAN\n"
                               "2.  Diet PLAN\n"))
            if choice == 1:
                with open("Vanya_Ex.txt", "r") as f:
                    print(f.read())
            elif choice == 2:
                with open("Vanya_diet.txt", "r") as f:
                    print(f.read())
            else:
                print("Invalid Choice\n")

        elif name == "Special":
            choice = int(input("For what you are looking forward\n"
                               "1.  Exercise PLAN\n"
                               "2.  Diet PLAN\n"))
            if choice == 1:
                with open("special_Ex.txt", "r") as f:
                    print(f.read())
            elif choice == 2:
                with open("special_diet.txt", "r") as f:
                    print(f.read())
            else:
                print("Invalid Choice\n")

        else:
            print("Client Does not exist\n")

    elif n==3:
        exit(1)
    else:
        print("It seems that what you are looking for is not be available to my management system\n")


"""
OUTPUT:
Welcome to Health Management system
There are 3 clients in my Gym 
['Kartikey', 'Vanya', 'Special']
What do you want to do ?
1. Lock DATA
2. Retrieve DATA
3. Exit
1
Enter the name of client
Kartikey
For what you are looking forward
1. For Exercise
2. For Diet
3
Invalid Choice

What do you want to do ?
1. Lock DATA
2. Retrieve DATA
3. Exit
2
Enter the name of client
Kartikey
For what you are looking to see
1.  Exercise PLAN
2.  Diet PLAN
1
['2020-09-19 01:00:27.558187'] :  Tredmil 
 
What do you want to do ?
1. Lock DATA
2. Retrieve DATA
3. Exit
3

Process finished with exit code 1
"