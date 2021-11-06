str = input("Please enter a string: ")
lstr = str.lower()

def most_frequent(x):
    my_Dict = {}
    for i in x:
        if i not in my_Dict:
            my_Dict[i] = 1 
        elif i in my_Dict:
            my_Dict[i] = my_Dict[i] + 1

    list1 = list(my_Dict.keys())

    for i in range(0, len(list1)):
        for j in range(i+1,len(list1)):
            if my_Dict[list1[i]] < my_Dict[list1[j]]:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
    
    for k in list1:
        print(k," = ",my_Dict[k])

most_frequent(lstr)