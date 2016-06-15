# Several CTF challenges I have come across require manipulation of 
# character codes, i.e. subtract a list of character codes from 
# a word. Python manipulation comes easier than JS so this bit 
# of code was born to help out with those challenges. 

def get_ord(word):
    tmp = []
    for letters in word:
        tmp.append(ord(letters))
    return(tmp)

def get_char(word):
    tmp = []
    for letters in word:
        tmp.append(chr(letters))
    return(tmp)

def main():
    list_one = [176,214,205,246,264,255,227,237,242,244,265,270,283]
    word_one = get_char(list_one)
    print('{}'.format(''.join(word_one)))

    word_two = 'administrator'
    list_two = get_ord(word_two)
    print('{}'.format(list_two))

if __name__ == '__main__':
    main()

