Simpsons_Characters = ["homer","barney","moe","mr burns","nelson","willie" ]


#add character name
def Add_Character_Name():
    Character_Name = input("enter simpsons character name you would like to add ")
    Simpsons_Characters.append(Character_Name)
    print(Simpsons_Characters)


#Remove Character Name
def Remove_Character_Name():
 
    Character_Name = input("enter simpsons character name that you want to remove")
    Simpsons_Characters.remove(Character_Name)
    print(Simpsons_Characters)

#Sort Character Names
def Sort_Character_Names():
    Simpsons_Characters.sort()
    print(Simpsons_Characters)



#Options menu
def Menu():
    print("option 1 add character")
    print("option 2 remove character")
    print("option 3 sort character")
    
    Choice = int(input("please type in your option"))

    if Choice == 1:
       Add_Character_Name()
    elif Choice == 2:
       Remove_Character_Name()
    elif Choice == 3:
        Sort_Character_Names()  

        
while True:
    Menu()
    


