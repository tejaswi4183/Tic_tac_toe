#!/usr/bin/python3
l="abcdefghi"
board={"a":"a","b":"b","c":"c","d":"d","e":"e","f":"f","g":"g","h":"h","i":"i"}
print(" a | b | c \n---+---+---\n d | e | f \n---+---+---\n g | h | i ")
print("\n")
def win(board):
	if(board["a"]==board["b"]==board["c"] or board["a"]==board["e"]==board["i"] or board["a"]==board["d"]==board["g"]):
		print("\n***Final board***")
		prin(board)
		print(player1 if board["a"]=="x" else player2,"won by",end =" ")
		print(player2 if board["a"]=="x" else player1)
		return 1
	elif(board["b"]==board["e"]==board["h"]):
		print("\n***Final board***")
		prin(board)
		print(player1 if board["b"]=="x" else player2,"won by",end=" ")
		print(player2 if board["a"]=="x" else player1)
		return 1
	elif(board["c"]==board["f"]==board["i"] or board["c"]==board["e"]==board["g"]):
		print("\n***Final board***")
		prin(board)
		print(player1 if board["c"]=="x" else player2,"won by",end=" ")
		print(player2 if board["a"]=="x" else player1)
		return 1
	elif(board["d"]==board["e"]==board["f"]):
		print("\n***Final board***")
		prin(board)
		print(player1 if board["d"]=="x" else player2,"won by",end=" ")
		print(player2 if board["a"]=="x" else player1)
		return 1
	elif(board["g"]==board["h"]==board["i"]):
		print("\n***Final board***")
		prin(board)
		print(player1 if board["g"]=="x" else player2,"won by",end=" ")
		print(player2 if board["a"]=="x" else player1)
		return 1
	else:
		return 0
def prin(board):

	print("\n",board["a"] if(board["a"]!="a") else " ",end="")
	print(" |",board["b"] if(board["b"]!="b") else " ",end="")
	print(" |",board["c"] if(board["c"]!="c") else " ",end="")
	print("\n---+---+---\n",end=" ")
	print(board["d"] if(board["d"]!="d") else " ",end="")
	print(" |",board["e"] if(board["e"]!="e") else " ",end="")
	print(" |",board["f"] if(board["f"]!="f") else " ",end="")
	print("\n---+---+---\n",end=" ")
	print(board["g"] if(board["g"]!="g") else " ",end=" ")
	print("|",board["h"] if(board["h"]!="h") else " ",end="")
	print(" |",board["i"] if(board["i"]!="i") else " ")
print("   |   |   \n---+---+---\n   |   |   \n---+---+---\n   |   |   ")

i=1
a="x"
player1=input("enter first player name:")
player2=input("enter second player name:")
print("\n\t\t*** GAME STARTS ***")

while(i<=9):
	print("select a place a-i to enter\"",a)
	b=input()
	
	if((board[b]!="x")  and (board[b]!="o")):
	
		board[b]=a
		i=i+1
		if(i>2):
			rc=win(board)
			if(rc==1):
				break
		
		prin(board)
		if(i==9 and rc==0):
			print("No one won the game")
			
		if(a=="x"):
			a="o"
					
		else:
			a="x"
				
