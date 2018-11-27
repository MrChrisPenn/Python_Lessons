
#initialise list to store game players
Game_Players = []

#add a player
def Add_Player():
  Gamer_Tag = input("please type in gamer tag")
  Game_Players.append(Gamer_Tag)

#remove a player
def Remove_player():
  Player_to_remove = input("who do you want to remove? ")
  Game_Players.remove(Player_to_remove)

#Sort list
def Sort_List():
    Game_Players.sort()
    
#pop list / removes a player from the end of a list
def Pop_List():
    Game_Players.pop()
    
#print list
def Print_List():
    print(Game_Players)

# a menu to choose options
def Menu():
  print("Option 1: Add player")
  print("Option 2: Remove player")
  print("Otion 3: Remove from the end of the list")
  print("Option 4: Sort List")
  print("Option 5: Print list")
  Choice = int(input("Please type in your choice"))

  if Choice == 1:
    Add_Player()
    Print_List()
  elif Choice == 2:
    Remove_player()
    Print_List()
  elif Choice == 3:
    Pop_List()
    Print_List()
  elif Choice == 4:
    Sort_List()
    Print_List()
  elif Choice == 5:
    Print_List()
      

#turning on loop to manage players list
while True:
  Menu()
