count = 0
sum = 0
while True:
   line = input("Enter a number: ")
   if line == "done" :
     break
   try:
     user_inp = float(line)
   except:
     print("Invalid input")
     continue   
   count = count + 1
   sum = sum + user_inp
print(sum, count, sum / count)