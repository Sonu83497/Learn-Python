# Ex:1
import re
pattern = r"^abc"
myString = "abcdef"
print(re.match(pattern,myString))

# Ex:2
import re
pattern = r"^abc"
myString = "abdef"
print(re.match(pattern,myString))

import re
pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
email="abc@gmail.com"
rs = re.match(pattern,email)
print(rs)



import re
pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
email="abcgmail.com"
rs = re.match(pattern,email)
print(rs)

import re
pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
email="abcgmail.com"
rs = re.match(pattern,email)
if rs == None:
    print("Email invalid !")
else:
    print("Email is Valid !")

print(rs)

