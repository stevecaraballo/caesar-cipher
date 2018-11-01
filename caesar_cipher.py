
word = input('Give me a word to rotate: ')

num = input('Give me a number to rotate the word by: ')

def if_num_greater_26(num):
    if num < 0:
        pos_num = num * -1
        change_num = pos_num % 26
        neg_again = change_num * -1
        return neg_again
    else:
        change_num = num % 26
        return change_num


def rotate_word(word,num):
    change_word = word.lower()
    number = num
    new_word = []
    if number == 0:
        return word
    if num > 26 or num < 0:
        number = if_num_greater_26(num)       
    for i in change_word:
        if i.isalpha():
            change = ord(i) + number
            if change > 122:
                new_letter = change - 26
                new_word.append(chr(new_letter))
            elif change < 97:
                new_letter = change + 26
                new_word.append(chr(new_letter))
            else:
                new_word.append(chr(change))
        else:
            new_word.append(i)
    return ''.join(new_word)

print(rotate_word(word,int(num)))


