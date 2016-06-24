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

#Recursive 3


#Test About Tower of Hanoi
def move(n,a,b,c):
    if n==1:
        print(a+"-->"+c);


        
print(fact(5));
print(fact_1(100));
move(1,'A','B','c');
