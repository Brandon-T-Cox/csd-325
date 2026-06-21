# Brandon Cox 6/13/26 module 1 assignment 1.3

# the purpose of this program is to countdown the bottles of beer from user imput number until reaching 0

# Function to manage the countdown
def countdown(bottles):

    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, "
              f"{bottles} bottles of beer.")
        print("Take one down and pass it around.")
        bottles -= 1
        print(f"{bottles} bottles of beer on the wall.\n")

    # Special case for 1 bottle
    if bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take it down and pass it around.")
        print("No more bottles of beer on the wall.\n")


# Main program
def main():
    bottles = int(input("How many bottles of beer are on the wall? "))

    countdown(bottles)

    print("No more bottles of beer on the wall.")
    print("Time to buy more beer!")


# Call main function
main()
