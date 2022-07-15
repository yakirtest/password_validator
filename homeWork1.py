


if __name__ == '__main__':
    # Exercise 1
    lst = [3, 7, 2]
    histo = []

    for item in lst:
        histo.append("*" * item)
    print(histo)

    # Exercise 2
    list1 = ["a", "b", "c"]
    list2 = ["x", "y", "z"]
    list3 = []

    for x in range(len(list1)):
        list3.append(list1[x] + list2[-x - 1])
    print(list3)

    # Homework not submitted
    # Exercise 1

    l1 = [1, 2, 3, 4]
    l2 = [5, 6, 7, 8]
    l3 = []
    for x in range(len(l1)):
        l3.append(l1[x] + l2[x])
    print(l3)

    # Exercise 2
    li1 = [[1, 2, 3], [6, 4], [9, 8, 7, 6, 5], [0]]
    li2 = []
    for x in range(len(l1)):
        li2.extend(li1[x])
    print(li2)

    # Exercise 2

    s = input("Please enter a string:")
    while (True):
        n = input("Please enter a number:")
        if n.isdigit():
            n = int(n)
            break
        else:
            print("<*error*> Invalid number!")
            n = input("Please enter a number:")

    newlist = []
    for x in range(0, len(s), n):
        newlist.append(s[x:x + n])

    print(newlist)

