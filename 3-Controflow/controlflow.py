# Hogwarts House Sorting Quiz
# Initialize house scores
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("Welcome to the Hogwarts House Sorting Quiz!")
print("Answer the following questions to see which house you belong to.\n")

# Question 1
print("Q1) Do you like Dawn or Dusk?")
print("    1) Dawn")
print("    2) Dusk")
answer1 = int(input())

if answer1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")

# Question 2
print("\nQ2) When I'm dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
answer2 = int(input())

if answer2 == 1:
    hufflepuff += 2
elif answer2 == 2:
    slytherin += 2
elif answer2 == 3:
    ravenclaw += 2
elif answer2 == 4:
    gryffindor += 2
else:
    print("Wrong input.")

# Question 3
print("\nQ3) Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
answer3 = int(input())

if answer3 == 1:
    slytherin += 4
elif answer3 == 2:
    hufflepuff += 4
elif answer3 == 3:
    ravenclaw += 4
elif answer3 == 4:
    gryffindor += 4
else:
    print("Wrong input.")

# Display final scores
print("\n" + "="*30)
print("FINAL HOUSE SCORES:")
print("="*30)
print(f"Gryffindor: {gryffindor}")
print(f"Ravenclaw: {ravenclaw}")
print(f"Hufflepuff: {hufflepuff}")
print(f"Slytherin: {slytherin}")

# Determine the winning house
max_score = max(gryffindor, ravenclaw, hufflepuff, slytherin)
if gryffindor == max_score:
    winner = "Gryffindor"
elif ravenclaw == max_score:
    winner = "Ravenclaw"
elif hufflepuff == max_score:
    winner = "Hufflepuff"
else:
    winner = "Slytherin"

print(f"\nCongratulations! You belong in {winner}!")