arr = []

num = int(input("Enter the number of terms to be in fibonacci sequence: "))

for i in range(0,num):
    
    if i < 2:
        arr.append(i)      
    elif i >= 2:
        arr.append(arr[i-1] + arr[i-2])
print(arr)