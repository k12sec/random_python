import itertools
from string import ascii_lowercase

def gen_userids(SET1, SET2, LENGTH1, LENGTH2):
    FIRST_SET = [''.join(i) for i in itertools.product(SET1, repeat = LENGTH1)]
    SECOND_SET = [''.join(i) for i in itertools.product(SET2, repeat = LENGTH2)]
    return ([''.join(i) for i in itertools.product(FIRST_SET, SECOND_SET)])
    

if __name__ == "__main__":
   
    ids = gen_userids(ascii_lowercase, "012", 2, 2)
    for users in ids:
        print('{}'.format(users))