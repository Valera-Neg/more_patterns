# Write a programm which repeatedly reads numbers 
# until the user enters "done".
# Once "done" is entered, print out the total, count, and average
# of the numbers. If the user enters anithing other then a number,
# detect their mistake using <try> and <except> and print error message 
# and skip to the next number.


count = 0
sum = 0
while True:
  line = input("Enrer a number: ")
  if line == "done" :
    print(sum, count, sum / count)
    break
  try:
    line = int(line)
  except:
      print("Invalid input")
      continue 
  count = count + 1
  sum = sum + line
  print(line)
  
