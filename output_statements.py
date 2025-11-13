#print string statements
print("Hello, World!")
#we can use escape characters also
print("Hello,\nWorld!")
print("Hello,\tWorld!")

#we can use repatition operators (*) in the string
print(10*"Hello ")
print("Hello "*10)

#we can use + operator also
print("Hello " + "World!")
print("hello","World!")



a,b,c = 10,20,30
print(a,b,c,sep=",")
print(a,b,c,sep=":")

#we can use end parameter also
print("Hello",end=" ")
print("World")

#print() with end attribute
print("hello")
print("craw")
print("cyber")
print("security")


# if we want output inthe same line with space
print("hello",end=" ")
print("craw",end=" ")
print("cyber",end=" ")
print("security \n",end=" " )


#print (String , variable, list)

s = "name"
a = 25
s1 = "Python"
s2 = "AI/Ml/DS"
print("My",s,"is Sonu and my age is",a,"I love",s1,"and I am learning",s2)
print("My {} is Sonu and my age is {} I love {} and I am learning {}".format(s,a,s1,s2))
print(f"My {s} is Sonu and my age is {a} I love {s1} and I am learning {s2}")
print("My %s is Sonu and my age is %d I love %s and I am learning %s"%(s,a,s1,s2))