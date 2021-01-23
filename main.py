"""
list2 = ["Asadbek","Bekzod","sanjar","charly"]

list2.sort(reverse = True)

print(list2)


list44 = [1,2,3,4]
list44 = list44 + ["asadbek"]

print(list44)



list3 = list2

list3.append(2)
print(list3)


list4 = [list2,list3]
print(list4)


tuple5 = [9,1,2,3,3]
print(tuple5[len(tuple5)-1])


print(tuple5.index(3)) #elementi indexichisini korsatisini




print("Motto: ",tuple5.count(3))

tuple5.remove(9)
print(tuple5)




"""
"""
tanlov = input("Please choose if yo buy (y/n)")

product = 0

while tanlov != "n":
    input()
    print("1. Olmaa  15 000")
    print("2. Nok  20 000")
    print("3. uzum  18 000")
    product =
    if option == "1":
        print("siz olma oldignziz ")
        total = total + 15000
        print("Hisob: {}".format(total))
    elif option == "2":
        print("Siz nok sotvoldigingiz ")
        total = total + 20000
    elif option == "n":
        break
option = input("Do you want to buy smth ? (y/n)")
"""




list2 = [1,2,3,4]
element=list2.pop(2)
print("Element: {}".format(element))
print(*list2,sep="\n")
print("Length",len(list2))
list2.insert(1,4)
print(list2)
list2.reverse()
print(list2)

