'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#Yasss the not in came in handy here. 
def count_th(word):
    if 'th' not in word:
        return 0
    else:

        word = word.replace('th', 'z', 1)
        return 1 + count_th(word)

print(count_th('thhtththshfhthahfhth'))