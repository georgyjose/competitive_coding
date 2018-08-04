def palindrome(n):
    if n == int(str(n)[::-1]):
        return True
    return False
while True:
    print(palindrome(int(input()))