# 12, -1000, 300, 19, 220
def main():
    print("This program sorts integers from lowest to highest when separated by a comma.")
    x = (input("Input a list of integers separated by a comma: "))

    ## ASCENDING ORDER
    print("Here are your numbers in ascending order:")
    print(ascending(x))

    ## DESCENDING ORDER
    print("Here are your numbers in descending order:")
    print(descending(x))

def ascending(c):
    c = c.split(", ")  # Isolates integer values to be converted

    numbers = [int(i) for i in c] # Creates a list set of integers
    numbers.sort() # Sorts in ascending order.

    return numbers
def descending(d):
    d = d.split(", ")
    numbers_reverse = [int(i) for i in d]
    numbers_reverse.sort(reverse=True) #Definitely found this online :D
    return numbers_reverse


if __name__ == "__main__":
    main()
