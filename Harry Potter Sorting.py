import random
import time

Students_List = ["Harry","Ron","Dave","Hermione"]

Slytherin_Students = [] # stores s students
Hufflepuff_Students = [] # stores hp students
Ravenclaw_Students = [] # stores rc students
Gryffindor_Students = [] # stores g students

House_Names = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"] # list of house names to randomly select.

#create a variable to store current position in student list
Current_Student = 0

while Current_Student < len(Students_List) :
 #randomly choose a house for the 1st student
  House = random.choice(House_Names)
  time.sleep(5)
  print("Your house is",House)
  
  #add student to correct house list
  if House == "Gryffindor":
    Gryffindor_Students.append(Students_List[Current_Student])
    print(Gryffindor_Students)#show house population

  elif House == "Ravenclaw":
    Ravenclaw_Students.append(Students_List[Current_Student])
    print(Ravenclaw_Students)#show house population

  elif House == "Hufflepuff":
    Hufflepuff_Students.append(Students_List[Current_Student])
    print(Hufflepuff_Students)#show house population
  
  elif House == "Slytherin":
    Slytherin_Students.append(Students_List[Current_Student])
    print(Slytherin_Students)

  else:
    print("You have chosen a house that doesn't currently exist")
  


  #add one to current position in student list
  Current_Student = Current_Student + 1

