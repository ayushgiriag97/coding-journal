#Sum of Digits of an Integer Using Recursion
def sum(x):
    if x==0:
        return 0
    else:
        return int(x%10)+sum(int(x/10))
print(sum(345))