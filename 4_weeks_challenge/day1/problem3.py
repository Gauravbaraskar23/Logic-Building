# Count word frequency with a plain dict, then with Counter.
# from collections import Counter
# def count_word_freq(words):
#     lst = words.split(' ')
#     ctr = Counter(lst)
#     return ctr

def count_word_freq(words):
    freq = {}
    lst = words.split()
    for i in range(len(lst)):
        
        if lst[i] not in freq:
            freq[lst[i]]  = 1
        else:
            freq[lst[i]] +=1
    return freq
        
        
words = "the cat and the hat and the bat"
print(count_word_freq(words))