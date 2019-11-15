

def task_1():
    start, end = int(input()), int(input())
    count = 0
    for num in range(start, end + 1):
        if num % 2 != 0:
            count += 1
    print(count)


def task_2():
    l_1 = float(input())
    l_2 = float(input())
    l_3 = float(input())
    l = [l_1, l_2, l_3]
    l.sort()
    if l[0]**2 + l[1]**2 == l[2]**2:
        print(l)


def task_3():
    sentence = input()
    list = sentence.split(" ")
    new_l = []
    for i in list:
        new_l.append(i[0].upper() + i[1:])
    print(" ".join(new_l))


def task_4():
    string = input()

    def count(str_, current_count=0):
        if not str_.strip():
            return current_count
        str_list = list(str_)
        next_word = str_list.pop(0)
        if next_word.isalpha():
            current_count += 1
        return count(''.join(str_list), current_count)

    print(count(string))


def task_5():
    # слова в множестве вводятся через ","
    first_set = set(input().split(','))
    second_set = set(input().split(','))
    unique_words = []
    intersection = first_set.intersection(second_set)
    for i in first_set:
        if i not in intersection:
            unique_words.append(i)
    for i in second_set:
        if i not in intersection:
            unique_words.append(i)
    print(unique_words)
    print(len(unique_words))


def task_6():
    n = int(input())

    def f(n):
        for i in range(n - 1):
            print(' '*(n-1) + "**" + ' '*(n-1))
        print("*"*n*2)
    f(n)


def task_7():
    db_dict = dict()
    temp = "если вы закончили введите 0"

    def insert_data(dict_):
        while True:
            category = input("Введите следующую категорию, " + temp)
            if category == "0":
                break
            dict_[category] = list()
            while True:
                product = input("Введите следующий продукт, " + temp)
                if product == "0":
                    break
                dict_[category].append(product)
    insert_data(db_dict)
    print(db_dict)


#task_1()
#task_2()
#task_3()
#task_4()
#task_5()
#task_6()
#task_7()

