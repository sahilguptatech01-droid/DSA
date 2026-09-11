# Even Sum Query

n=int(input())
numbers=list(map(int,input().split()))
for i in range(n):
    if(i%2==0):
        numbers[i]=0



# Making prefix sum
    
p=[]
sum=0
for i in range(len(numbers)):
    sum+=numbers[i]
    p.append(sum)


query=int(input())
for i in range(query):
    l,r=map(int,input().split())
    l-=1
    r-=1
    if(l==0):
        print(p[r])
    else:
        print(p[r]-p[l-1])


#  Count Vowels

# checking the vowel
def isVowel(i):
    if i in "aeiou":
        return True

length=int(input())
string=input()
numbers=[]
for i in string:
    if isVowel(i):
        numbers.append(1)
    else:
        numbers.append(0)


# # Making prefix sum
    
p=[]
sum=0
for i in range(len(numbers)):
    sum+=numbers[i]
    p.append(sum)


query=int(input())
for i in range(query):
    l,r=map(int,input().split())
    l-=1
    r-=1
    if(l==0):
        print(p[r])
    else:
        print(p[r]-p[l-1])


# Range Sum of Squares

n,query=map(int,input().split())
numbers=list(map(int,input().split()))
for i in range(len(numbers)):
    square=numbers[i]**2
    numbers[i]=square

p=[]
sum=0
for i in range(len(numbers)):
    sum+=numbers[i]
    p.append(sum)


for i in range(query):
    l,r=map(int,input().split())
    l-=1
    r-=1
    if(l==0):
        print(p[r])
    else:
        print(p[r]-p[l-1])


#  Count Numbers with Digit Sum K

def check_sum(num,k):
    add=0
    while num>0:
        rem=num%10
        add+=rem
        num=num//10

    if(add==k):
        return True

n,query,k=map(int,input().split())

numbers=list(map(int,input().split()))
for i in range(len(numbers)):
    if(check_sum(numbers[i],k)):
        numbers[i]=1
    else:
        numbers[i]=0


p=[]
sum=0
for i in range(len(numbers)):
    sum+=numbers[i]
    p.append(sum)


for i in range(query):
    l,r=map(int,input().split())
    l-=1
    r-=1
    if(l==0):
        print(p[r])
    else:
        print(p[r]-p[l-1])



