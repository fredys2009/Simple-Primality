"""
Filename: simple_primality.py
Author: <NAME>
Created: <DATE>
Instructor: Holtslander
"""
n = 2
def prime():
    a = int(input("enter a non negative number"))
    if a == n:
        print("its prime")
    elif a != n:
        for i in range(2, a):
            if a % i == 0:
                print("its not prime")
                break
        else:
            print("its prime")


# You should not need to change any code below this point
def main():
    print("This program will determine the primality of a number.")
    running = "y"
    while running == "y":
        prime()
        running = input("Check another number? (y/N)\n").lower()
    print("Thank you for using this primality program!")

if __name__ == "__main__":

    main()




