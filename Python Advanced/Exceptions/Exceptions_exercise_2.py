def example1() -> None:
    for i in range(3):
        try:
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))
            print(x, '/', y, '=', x / y)
        except ZeroDivisionError:
            print("Can't divide by 0.")
        except ValueError:
            print("Invalid input. "
                  "Input can not be blank / expected type: class <int>.")


def example2(L: list) -> None:
    sumOfPairs = []

    if isinstance(L, str):
        raise AttributeError('\n\nExpected type class <list>. Got class <str> instead.')

    try:
        for i in range(len(L)-1):
            sumOfPairs.append(L[i] + L[i + 1])
    except IndexError:
        print("List must contain at least two integers")
    except TypeError:
        sumOfPairs = example2([num for num in L if isinstance(num, int)])
    else:
        print("\n\nExample 2")
        print("sumOfPairs = ", sumOfPairs)


def printUpperFile(fileName: str) -> None:
    try:
        file = open(fileName, "r")
    except FileNotFoundError:
        print(f"\n\nFile {fileName} not found at specified path.")
    except IOError:
        print(f"\n\nCould not read the {fileName} file.")
    else:
        for line in file:
            print(line.upper())
            file.close()


def main():
    L = [10, 3, 5, 6, 9, 3]

    example1()

    example2(L)
    example2([10, 3, 5, 6, "NA", 3])
    example2('asd')

    example3([10, 3, 5, 6])

    printUpperFile("doesNotExistYest.txt")
    printUpperFile("./Dessssktop/misspelled.txt")


if __name__ == "__main__":
    main()
