def no_teen_sum(a, b, c):
    # CODE GOES HERE
    if (a == 15 or b == 15 or c == 15) or (a == 16 or b == 16 or c == 16):
        fix_teen(a or b or c)
        return ()
    elif (a>=13 and a<=19) and(b>=13 and b<=19) and (c>=13 and c<=19):
        return(0)
    elif(a >= 13 and a <= 19):
        return (b+c)
    elif (b >= 13 and b <= 19):
        return (a + c)
    elif (c >= 13 and c <= 19):
        return (a + b)
    else:
        return (a+b+c)



def fix_teen(n):
    return (n)
# CODE GOES HERE

x,y,z = int(input()),int(input()),int(input())
sum = no_teen_sum(x,y,z)
print(sum)
