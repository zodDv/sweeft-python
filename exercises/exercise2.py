def lex_orderer(word):
    word = list(word)
    i = len(word)-1  # find the non-increasing part of the word
    while i > 0 and word[i-1] >= word[i]:
        i -= 1
    if i <= 0:
        return 'no answer'
    j = len(word) - 1  # find the rightmost successor
    while word[j] <= word[i - 1]:
        j -= 1   
    word[i-1], word[j] = word[j], word[i-1] # swap with the rightmost character
    word[i:] = word[len(word)-1:i-1:-1]  # reverse
    print(''.join(word))




