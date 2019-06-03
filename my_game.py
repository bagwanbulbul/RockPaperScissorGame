import random
my_list = ["rock", "paper", "scissor"]
computer =random.choice(my_list)
user_input = raw_input("enter the rock, sesior, paper")

if user_input not in my_list:
	print "invalid input"
