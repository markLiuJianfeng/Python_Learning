#Recursive 1
def fact(n): #Normal Recursive
    if n==1:
        return 1
    return n*fact(n-1);

#Recursive 2 Call the function itself
def fact_1(n): #Stack protection
    return fact_iter(n,1);
def fact_iter(num,product):
    if num==1:
        return product;
    return fact_iter(num-1,num*product);

#Recursive 3 Advanced


#Test About Tower of Hanoi
def move(n,a,b,c):
    if n==1:
        print(a+"-->"+c);
    else:
        move(n-1,a,c,b);
        move(1,a,b,c);
        move(n-1,b,a,c);
#Step1: take the n-1 pieces from A to B through C;
#Strp2: take the rest one piece form A to C directly;
#Step3: take the n-1 pieces from B to C through A.

print(fact(5));
print(fact_1(100));
move(3,'A','B','c');
