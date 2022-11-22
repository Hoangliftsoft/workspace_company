# def calculator(a):
def isLeafYear(a):
    if (a % 400 == 0):
        return True
    if (a % 100 == 0):
        return False
    if (a % 4 == 0):
        return True
    return False


if __name__ == "__main__":
    print(isLeafYear(2000))