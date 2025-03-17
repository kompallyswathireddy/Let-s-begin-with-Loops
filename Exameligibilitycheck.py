medicalcause=str(input("did you have medicalcause yes or no ?"))
attendance=int(input("enter your attendance"))
if medicalcause=="yes":
 print("you are allowed")
else:
 if attendance>=75:
  print("allowed")
 else :
  print("you are not allowed")