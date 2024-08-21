print("enter marks obtained in 4 subjects")
maths = int(input("enter your math marks here"))
english = int(input("enter your english marks here"))
science = int(input("enter your science marks here"))
urdu = int(input("enter your urdu marks here"))
sum = maths+english+science+urdu
print("sum of all is", sum)
perc = (sum/400)*100
print(end = "percentage mark = ")
print(perc)