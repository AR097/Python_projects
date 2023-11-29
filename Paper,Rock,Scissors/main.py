import random #retorna um numero aleatorio entre 0 e 1.

user_wins = 0 #player jogador real
computer_wins = 0 #player computador

options = ["rock", "paper", "scissors"]

while True: #inicia um loop usando palavra chave
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break  #permite que voce saia do loop

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #opções= rock: 0, paper: 1, scissors(tesoura): 2

    #na vez do computador
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    # na vez do jogador
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!") #won(ganhou)
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    #caso de empate
    elif user_input == "scissors" and computer_pick == "scissors":
        print("There was a tie between the players. Try again!")
        user_wins += 0

    elif user_input == "paper" and computer_pick == "paper":
        print("There was a tie between the players. Try again!")
        user_wins += 0

    elif user_input == "rock" and computer_pick == "rock":
        print("There was a tie between the players. Try again!")
        user_wins += 0

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")