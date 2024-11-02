def findCommon(a1, a2, a3):
    set1 = set(a1)
    set2 = set(a2)
    set3 = set(a3)

    common_elements = set1.intersection(set2).intersection(set3)

    print("Common Elements are:", end=" ")
    for element in common_elements:
        print(element, end=" ")
    print()  

a1 = [1, 5, 10, 20, 40, 80]
a2 = [2, 5, 6, 7, 8, 9, 20, 88]
a3 = [5, 20, 11, 22, 33, 44, 55, 66]

findCommon(a1, a2, a3)
