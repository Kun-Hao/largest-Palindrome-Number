# largest-Palindrome-Number
Why does the code still continue even though the condition is not fuilfied

'''largest palindromic number from the product of two three digit numbers'''

def Palindrome(num):
    number = str(num)
    print(number)  
    reverse = number[::-1]
    print(reverse)
    if number == reverse:
        return True
    else:
        return False
    
print(Palindrome(225))


for num_1 in range(999,990,-1):
    for num_2 in range(999,990,-1):
        product = Palindrome(num_1 * num_2)
        print (product)
        if product == True:
            print (num_1 * num_2)
            break
