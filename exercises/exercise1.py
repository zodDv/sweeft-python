def ex1():
    num_lines = int(input())
    count_dict = {}
    for n in range(0,num_lines):
        word = str(input())
        count_dict[word] = dict.get(count_dict, word, 0) + 1
    print(len(count_dict.keys()))
    print(" ".join(str(x) for x in list(count_dict.values())))
