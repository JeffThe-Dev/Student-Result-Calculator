name = str(input("Enter Your Name:"))

while True:
  try:
    marks_phy = float(input("Enter your Physics marks: "))
  except ValueError:
    print("Please enter numbers only")
    continue
  if marks_phy >=0 and marks_phy <=100:
     break
  elif marks_phy <0:
     print("Marks cannot be less than 0")
     continue
  else:
     print("Marks cannot be greater than 100")
     continue

while True:
   try:
      marks_maths = float(input("Enter your Mathematics marks:"))
   except ValueError:
      print("Please enter numbers only!")
      continue
   if marks_maths >=0 and marks_maths <=100:
      break
   elif marks_maths <0:
      print("Marks cannot be less than 0!")
      continue
   else:
      print("Marks cannot be greater than 100!")
      continue

while True:
   try:
      marks_comp = float(input("Enter your Computer marks:"))  
   except ValueError:
      print("Please enter numbers only")
      continue
   if marks_comp >=0 and marks_comp <=100:
      break
   elif marks_comp <0:
      print("Marks cannot be less than 0!")
      continue
   else:
      print("Marks cannot be greater than 100!")
      continue

while True:
   try:
      marks_chem = float (input("Enter your Chemistry marks:"))
   except ValueError:
      print("Please enter numbers only!")
      continue
   if marks_chem >=0 and marks_chem <=100:
      break
   elif marks_chem <0:
      print("Marks cannnot be less than 0!")
      continue
   else:
      print("Marks cannot be above than 100!")
      continue      

while True:
   try:
      marks_bio = float (input("Enter your Biology marks:"))
   except ValueError:
      print("Please enter numbers only!")
      continue
   if marks_bio >=0 and marks_bio <=100:
      break
   elif marks_bio <0:
      print("Marks cannnot be less than 0!")
      continue
   else:
      print("Marks cannot be above than 100!")
      continue      

while True:
   try:
      marks_eng = float (input("Enter your English marks:"))
   except ValueError:
      print("Please enter numbers only!")
      continue
   if marks_eng >=0 and marks_eng <=100:
      break
   elif marks_eng <0:
      print("Marks cannnot be less than 0!")
      continue
   else:
      print("Marks cannot be above than 100!")
      continue      

Total_marks = marks_phy + marks_maths + marks_comp + marks_bio + marks_chem + marks_eng

percentage = Total_marks/600*100

if percentage >=90:
   grade = "A+"
elif percentage >=80:
   grade = "A"
elif percentage >=70:
   grade = "B"
elif percentage >=60:
   grade = "C"
elif percentage >=50:
   grade = "D"
elif percentage >=40:
   grade = "E"
else:
   grade = "F"

if percentage >=40:
   status = "PASS!"
else:
   status = "FAILED!"   

print(f"Name:{name}")
print(f"\nTotal Marks:{Total_marks}")
print(f"\nPercentage:{percentage:.2f}%")
print(f"\nGrade:{grade}")
print(f"\nStatus:{status}")