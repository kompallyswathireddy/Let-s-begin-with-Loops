print("select your ride")
print("1.bike")
print("2.car")
choice1=int(input("enter your choice"))
if choice1==1:
 print("what type of bike")
 print("1.hayabusa")
 print("2.ninja h2r")
 choice2=int(input("enter your choice "))
 if choice2==1:
  print("you have selected hayabusa")
 else:
  print("you have selected ninja h2r")
elif choice1==2:
 print("what type of car")
 print("1.lamborghini")
 print("2.bhugati")
 choice3=int(input("enter you choice"))
 if choice3==1:
  print("you have selected lamborghini")
 else:
  print("you have selected bughati ")
else:
 print("wrong input")