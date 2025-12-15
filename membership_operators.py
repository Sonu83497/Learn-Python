s = set("sunil")
print(s)
print('s'in s)

#write a program to print different vowels present in the given word ?
w = input("Enter word to search for vowels :")
s = set(w)
v = {'a','e','i','o','u'}
d = s.intersection(v)

print("The different vowel present in ",w,"are",d)