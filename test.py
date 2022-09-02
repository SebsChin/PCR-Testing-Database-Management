
# Code tester file

import re


while True:
    
    name = input("Enter a name: ")

    check = bool(re.fullmatch('[A-Za-z]{1,10}( |-|)[A-Za-z]{1,10}', name))
    
    print(check)
    
    print(name.title())