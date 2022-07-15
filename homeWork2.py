
def print_dictionary(dictionary: dict):
    """
     function Dictionary printing
    :param dictionary:
    :return: None
    """
    for i in sorted(dictionary.keys()):
        print(i, "-", dictionary[i], end="\n")
    print()

def Double_value(lst_dict, list1):
    """
    Lists that have at least one repeating organ
    :param lst_dict: List of dictionaries
    :param list1: List of dictionaries without duplicates
    :return: None
    """
    for k,v in lst_dict.items():
        this_set = set(v)
        if len(this_set) is not len(v):
            pass
            #test
            print(f'"There are duplications:{str(v)}')
        else:
            list1.append(v)# adding Lists without a double value
            #test
            print(f'No duplicates:{str(v)}')

def intersection(list1:list)->set:
    """
    function Finds equal organs In all dictionaries
    :param list1: List of dictionaries
    :return: set: Of equal organs In all dictionaries
    """
    if list1 != []:
        set1 = set(list1[0])
        for i in list1:
            set1 = set1.intersection(i)
        return set1
    return {}




if __name__ == '__main__':
    print("~"*10+"#Exercise 1"+"~"*10)
    # s=input("Please enter a string: ")
    s = "dabaxyddab"
    print(s)
    dictionary = {}
    for i in s:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    # Exercise 1
    print_dictionary(dictionary)
    print("~"*10+"#<<<Section B>>>"+"~"*10)
    #Section B
    reverse_dictionary = {}
    for k,v in dictionary.items():
       if v not in reverse_dictionary:
           reverse_dictionary[v] = [k]
       else:
           reverse_dictionary[v].append(k)
    print_dictionary(reverse_dictionary)

    print("~"*10+"#Exercise 2 <#test>"+"~"*10)
    #Exercise 2
    lst_dict = {"lst1": [11, 7, 5, 8, 5, 37, 11, 5], "lst2": [22, 8, 10, 1, 11], "lst3": [71, 3, 22, 8, 2, 14, 1]}
    list1 = []  # Save Lists without a double value
    Double_value(lst_dict, list1)
    # Section B
    print("~"*10+"##<<<Section B>>>"+"~"*10)
    this_set = intersection(list1)
    print(this_set)
    print()

    print("~"*10+"#Exercise 3"+"~"*10)
    # Exercise 3
    lst = [31, 99, 3, 1943]
    set2 = set()
    for num in lst:
        set2.update({int(digit) for digit in str(num)})
    print(set2)
    print(sorted(set2, reverse=True))







