
def get_fibonacci():
    x = 0
    y = 1

    n = input("Enter the number of the postion in the sequencce you want the value of: ")

    if int(n) < int(0):
        print("Please enter a number that is 0 or greater")

    elif n == 0:
        return 0

    elif n == 1:
        return y

    else:
        for i in range(1, int(n)):
                z = x + y
                x = y
                y = z
                print("Z is: " + str(z))
        return z

def main():
    get_fibonacci()

if __name__ == '__main__':
    main()
