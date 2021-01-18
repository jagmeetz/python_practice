def fact(n=5):
    if n==0:
        return 1
    return n*fact(n-1)

x=fact()
print(x)
