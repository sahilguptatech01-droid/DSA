# Search Queries

def search (a,m,target):
        l=0
        r=n-1
        while(l<=r):
            mid=(l+r)//2
            if(a[mid]==target):
                print(mid+1)
                return
            elif(a[mid]>target):
                r=mid-1
            elif(a[mid]<target):
                l=mid+1
        print(-1)


n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(m):
    target=int(input())
    search(a,m,target)
 
#  Search Queries - II


# for sorted in descending order 
def search (a,m,target):
        l=0
        r=n-1
        while(l<=r):
            mid=(l+r)//2
            if(a[mid]==target):
                print(mid+1)
                return
            elif(a[mid]>target):
                l=mid+1
            elif(a[mid]<target):
                r=mid-1
        print(-1)

n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(m):
    target=int(input())
    search(a,m,target)


# First and Last Occurence

def search_first_index(a,m,target,ans):
    l=0
    r=n-1
    while(l<=r):
        mid=(l+r)//2
        if(a[mid]==target):
            ans=mid+1
            r=mid-1
        elif(a[mid]>target):
                r=mid-1
        elif(a[mid]<target):
            l=mid+1
    return ans

def search_last_index(a,m,target,ans):

    l=0
    r=n-1
    while(l<=r):
        mid=(l+r)//2
        if(a[mid]==target):
            ans=mid+1
            l=mid+1
            
        elif(a[mid]>target):
                r=mid-1
        elif(a[mid]<target):
            l=mid+1
    if(ans>-1):
        return ans
    return ""
    
  



n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(m):
    target=int(input())
    print(search_first_index(a,m,target,ans=-1),end=" ")
    
    print( search_last_index(a,m,target,ans=-1))
 

# Frequency of Element


def search_first_index(a,m,target,ans):
    l=0
    r=n-1
    while(l<=r):
        mid=(l+r)//2
        if(a[mid]==target):
            ans=mid
            r=mid-1
        elif(a[mid]>target):
                r=mid-1
        elif(a[mid]<target):
            l=mid+1
    first=ans
    return first

def search_last_index(a,m,target,ans):

    l=0
    r=n-1
    while(l<=r):
        mid=(l+r)//2
        if(a[mid]==target):
            ans=mid
            l=mid+1
            
        elif(a[mid]>target):
                r=mid-1
        elif(a[mid]<target):
            l=mid+1
    last=ans
    return last
    
  


n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
for i in range(m):
    target=int(input())
    first=search_first_index(a,m,target,ans=-1)
    last=search_last_index(a,m,target,ans=-1)
    if (last==-1):
        print(0)
    else:
        count=last-first+1
        print(count)
 