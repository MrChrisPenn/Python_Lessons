


def Add_Two_Numbers():
    num1 = int(input("please type in one number"))
    num2 = int(input("please type in one number"))
    answer = num1 + num2
    return answer

def Subtract_Two_Numbers():
    num1 = int(input("please type in one number"))
    num2 = int(input("please type in one number"))
    answer = num1 - num2
    return answer

def Multiply_Two_Numbers():
    num1 = int(input("please type in one number"))
    num2 = int(input("please type in one number"))
    answer = num1 * num2
    return answer

def Divide_Two_Numbers():
    num1 = int(input("please type in one number"))
    num2 = int(input("please type in one number"))
    answer = num1 / num2
    return answer

def Binary_To_Denary8Bit():

    Number_Is_Acceptable = False

    while Number_Is_Acceptable == False:
        Binary_Number = input("please type in an 4 digit binary number")

        if len(Binary_Number) > 8 or len(Binary_Number)<8:
            print("Please type in your binary number again")
        else:
            Denary_Number = 0
            if Binary_Number[7] == "1":
                Denary_Number = Denary_Number+1

            if Binary_Number[6] == "1":
                Denary_Number = Denary_Number+2

            if Binary_Number[5] == "1":
                Denary_Number = Denary_Number+4

            if Binary_Number[4] == "1":
                Denary_Number = Denary_Number+8

            if Binary_Number[3] == "1":
                Denary_Number = Denary_Number+16

            if Binary_Number[2] == "1":
                Denary_Number = Denary_Number+32

            if Binary_Number[1] == "1":
                Denary_Number = Denary_Number+64

            if Binary_Number[0] == "1":
                Denary_Number = Denary_Number+128

            print("Your binary in denary is",str(Denary_Number))

            Number_Is_Acceptable == True

# a menu to choose options
def Menu():
  print("Option 1: Add two numbers")
  print("Option 2: Subtract two numbers")
  print("Option 3: Convert an 8 bit binary number to denary")
  print("Option 4: Multiply two numbers")
  print("Option 5: Divide two numbers")
  
  Choice = int(input("Please type in your choice"))

  if Choice == 1:#add two numbers
      Actual_Answer = Add_Two_Numbers()
      print(Actual_Answer)
  elif Choice == 2:#subtract two numbers
      Actual_Answer = Subtract_Two_Numbers()
      print(Actual_Answer)
  elif Choice == 3:#Turn 8 bit binary num into denary
      Binary_To_Denary8Bit()
  elif Choice == 4:#Multiply two numbers
      Actual_Answer = Multiply_Two_Numbers()
      print(Actual_Answer)
  elif Choice == 5:#Divide two numbers
      Actual_Answer = Divide_Two_Numbers()
      print(Actual_Answer)

      
while True:
    Menu()
