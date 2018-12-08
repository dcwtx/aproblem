from math import factorial

#
# proof of the equality in equation 1 of the article titled "a problem"
#

def comb(a,b):
    return factorial(a) / (factorial(b) * factorial(a - b))


n=500
tol = 1e-6

def main():
    sum = 0.0
    for i in range(2,n+1):
        top = i-1
        bottom = i-1
        sumofterms = 0.0
        for term in range(1,n+1-i+1):
            ans = comb(top,bottom)
            sumofterms += ans
            top += 1
        lhs = sumofterms
        rhs = comb(n,i)
        # print("For i={} and n={}: LHS={} and RHS={}".format(i, n, lhs, rhs))
        if (lhs-rhs)/lhs > tol:
            print("LHS not equal to RHS!!!")
            print("LHS={} and RHS={}".format(lhs,rhs))
            print("n={} and i={}".format(n,i))
            return

    print("Equality held.")
    return


if __name__ == "__main__":
    main()