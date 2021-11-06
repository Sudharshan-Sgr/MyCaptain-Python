num = int(input("Enter number of terms: "))
ls = []
ls1 = []
print("Input the list: ")
for i in range(0,num):
    list = int(input())
    ls.append(list)
print("The list entered: ",ls)

for j in ls:    
    if j >= 0:
        ls1.append(j)

print("The positive numbers in the list are: ",ls1)

