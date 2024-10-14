while True:
  a=int(input("Enter your age:"))


  if(a>=18):
    print("You are above the age of consent \n Good for you")
    # print(" Good for you")

  elif(a<=0):
    print("You are entering an invalid age")

  else:
    print("You are below the age of consent")

  print("End of program")