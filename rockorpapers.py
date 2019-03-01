
import random

a = ["rock", "papers", "scissors"]
u = "you win"
l = "you lose"
k = 0
c = 0
count = 0

while True:
	while<count
	p = input("enter rock or papers or scissors")

	if p == "q":
		print("thanks for playing")
		quit()
	
	com = random.choice(a)
	print("you chose", p, "computer chose", com)
	
	if p == com:
		print("its a tie")
	elif p == "rock" and com == "scissors":
		print(u)
		k = k +1
	elif p == "papers" and com == "rock":
		print(u)
		k = k +1
	elif p == "scissors" and com == "papers":
		print(u)
		k = k +1

	elif p == "scissors" and com == "rock":
		print(l)
		c = c +1
	elif p == "rock" and com == "papers":
		print(l)
		c = c +1
	elif p == "papers" and com == "scissors":
		print(l)
		c = c +1
	print("your score is ", k, "computer score is ", c)