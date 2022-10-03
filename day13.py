testname = input ("Enter name of the test: ")
score = int(input ("How many points You scored? "))
maxpoints = int(input ("How many points You could get? "))
percentage = (score*100/maxpoints)
#print(str(grade).split(".")[0])
if percentage > 90:
    grade = ("A+")
elif percentage >= 80 and percentage <= 89:
    grade = ("A")
elif percentage >= 70 and percentage <= 79:
    grade = ("B")
elif percentage >= 60 and percentage <= 69:
    grade = ("C")
elif percentage >= 50 and percentage <= 59:
    grade = ("D")
elif percentage < 50:
    grade = ("U")
else:
   print("Something went wrong... :( ")
print ("Your grade in",testname,"is",grade)
