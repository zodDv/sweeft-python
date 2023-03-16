def word_counter():
    num_lines = int(input()) # number of lines
    count_dict = {}  # word count dictionary
    for n in range(0, num_lines): 
        word = str(input())
        count_dict[word] = dict.get(count_dict, word, 0) + 1   # get count of word from dictionary and increment  
    print(len(count_dict.keys()))  
    print(" ".join(str(x) for x in list(count_dict.values())))
