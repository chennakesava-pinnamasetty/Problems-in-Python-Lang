
num = 5
print(int(num*(num+1)))      # 30


num = 5
print(int(num*(num+1))//2)   # 15



# recursion

def search(n):
    if n == 1:
        return 1
    return n + search(n-1)
    
n = 5
print(search(n))       # 15