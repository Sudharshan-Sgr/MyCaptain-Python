file_name = input("Input the Filename: ")
my_Dict = {".py":"Python",".cpp":"C++", ".C":"C", ".java":"Java"}
for i in range(0,len(file_name)):
    if file_name[i] == ".":
        temp = file_name[i::]
        break
if temp in my_Dict:
    print(my_Dict[temp])