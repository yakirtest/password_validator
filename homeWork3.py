import statistics

def split_male_female(data_set: dict)->(dict,dict):
    """
    A function that accepts data_set as a parameter and returns 2 dictionaries -
    one for organs where the value "sex" is equal to "male"
    and the other for organs where the value "sex" is equal to "female"
    :param data_set: Dictionary within a dictionary
    The main dictionary contains the ID number
    and values of the people in the secondary dictionary
    :return:tuple Of dictionaries (dict,dict)
    data_male = The value "sex" is equal to "male"
    data_female = The value "sex" is equal to "male"
    """
    data_male = dict()
    data_female = dict()
    for id in data_set:
        if data_set[id]["sex"] == "male":
            data_male[id] = data_set[id]
        else:
            data_female[id] = data_set[id]
    return data_male,data_female


def find_maedian_average (data_set:dict)->(float,float):
    """
    A function that receives a dictionary and finds
    the mean age and median age of the resulting dictionary
    :param data_set: Dictionary within a dictionary
    The main dictionary contains the ID number
    and values of the people in the secondary dictionary
    :return: tuple Of float (float,float) average age and median
    """
    ages = []
    for id in data_set:
        ages.append(data_set[id]["age"])
    return statistics.mean(ages),statistics.median(ages)

def print_values_above(data_set: dict, number: int = 0)->None:
    """
    A function will print values that their age value is greater than the number sent
    **If not sent number
    The function will print all the values of the dictionary
    :param data_set: Dictionary within a dictionary
    The main dictionary contains the ID number
    and values of the people in the secondary dictionary
    :param number: Positive number - **optional**
    :return:None
    But print output
    Example of output
    " ID: {ID number} / {Values of a person)}"
    """
    for id in data_set:
        if number >= 0:
            if data_set[id]["age"] > number:
                print(f" ID: {id} / {format_values(data_set[id])}")
        else:
            print(f" ID: {id} / {format_values(data_set[id])}")


def format_values(data:dict)->str:
    """
    format function,
    Of a dictionary with values person
    :param data:dictionary with values person
    :return:string format fo values person
    """
    val = str()
    for k, v in data.items():
        val += f"{k}: {v} "
    return val


if __name__ == '__main__':
    data_set = {3322117: {"name": "Tal", "sex": "male", "age": 22.6},
                176864301: {"sex": "female", "age": 54, "height": 1.65, "name": "Anat"},
                256468123: {"sex": "male", "age": 29, "height": 1.65, "name": "yakir"},
                3322117: {"name": "yosef", "sex": "male", "age": 40},
                37867617: {"name": "Yitzhak", "sex": "male", "age": 22, "email": "Yitzhak@gmail.com"},
                4567801: {"sex": "female", "age": 18.9, "height": 1.65, "name": "Katya"},
                78905123: {"sex": "male", "age": 30, "height": 1.65, "name": "Moshe"},
                343768797: {"name": "Yaffe", "sex": "male", "age": 25}
                }
    male, female = split_male_female(data_set)
    #testing the dictionary
    #print(male)
    #print(female)
    print("~" * 40)

    Average, Median = find_maedian_average(data_set)
    print("The average age is: " + f"{Average:.2f}")
    print("The median age is: " + f"{Median}")
    print("~" * 40)

    print_values_above(data_set,35)
    print(f"{'~'* 20}No number sent{'~'* 20}")

    print_values_above(data_set)




