def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = list(map(int, input("Enter elements of list1: ").split()))
list2 = list(map(int, input("Enter elements of list2: ").split()))

if overlapping(list1, list2):
    print("The lists have common elements")
else:
    print("The lists have no common elements")