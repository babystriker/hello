
import random

a = ["rock", "papers", "scissors"]
u = "you win"
l = "you lose"
while True:
	p = input("enter rock or papers or scissors")
	if p == "q":
		print("thanks for playing")

	com = random.choice(a)
	print("you chose", p, 
	if p == com:
		print("its a tie")
	elif p == "rock" and com == "scissors":
		print(u)
	elif p == "papers" and com == "rock":
		print(u)
	elif p == "scissors" and com == "papers":
		print(u)
	elif p == "scissors" and com == "rock":
		print(l)
	elif p == "rock" and com == "papers":
		print(l)
	elif p == "papers" and com == "scissors":
		print(l)