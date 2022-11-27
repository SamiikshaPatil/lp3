
#iterative 

# nterm = int(input("how many terms 1"))

# n1, n2 = 0, 1
# count= 0

# if nterm<=0:
#     print("Enter valid no ")

# elif nterm ==1 :
#     print("Fibonacci sequence upto", nterm,":")
#     print(n1)

# else:
#     print("fibonacci series")

#     while count<nterm:
#         print(n1)
#         nth = n1+n2
#         n1 = n2
#         n2 = nth
#         count+=1


#RECURSIVE


def recur_fibo(n):
       if n <= 1:
        return n
       else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("enter no"))

# check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
print("Fibonacci sequence:")
for i in range(nterms):
       print(recur_fibo(i))



