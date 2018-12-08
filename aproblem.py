from math import factorial

#
# proof of the equality in equation 1 of the article titled "a problem"
#

def comb(a,b):
    return factorial(a) / (factorial(b) * factorial(a - b))


range_of_ns = range(5,10)

for n in range_of_ns:
    sum = 0.0
    for i in range(2,n):
        top = i-1
        bottom = i-1
        sumofterms = 0.0
        for term in range(1,n+1-i+1):
            ans = comb(top,bottom)
            sumofterms += ans
            top += 1
        lhs = sumofterms
        rhs = comb(n,i)
        print("For i={} and n={}: LHS={} and RHS={}".format(i, n, lhs, rhs))
