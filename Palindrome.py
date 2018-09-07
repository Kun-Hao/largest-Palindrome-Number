def Palindrome(num):
    number = str(num)
    # print(number)
    reverse = number[::-1]
    # print(reverse)
    if number == reverse:
        return True
    else:
        return False


for num_1 in range(999, 990, -1):
    for num_2 in range(999, 990, -1):
        if Palindrome(num_1 * num_2) == True:
            print(num_1 * num_2)
            print("True")
            break