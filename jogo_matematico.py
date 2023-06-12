import random
import time

def generate_equation(difficulty):
    if difficulty == "Fácil":
        number_range = range(-10, 11)
    elif difficulty == "Médio":
        number_range = range(-100, 101)
    elif difficulty == "Difícil":
        number_range = range(-1000, 1001)
    
    operation = random.choice(["+", "-", "*", "/"])
    num1 = random.choice(number_range)
    num2 = random.choice(number_range)
    
    if operation == "/":
        while num2 == 0:  # Evitar divisão por zero
            num2 = random.choice(number_range)
        equation = f"{num1} {operation} {num2}"
    else:
        equation = f"{num1} {operation} {num2}"
    
    return equation

def calculate_score(response_time):
    score = 10
    if response_time > 20:
        score = 0
    else:
        score -= response_time * 0.05 * score
    return int(score)

def play_individual(difficulty):
    print(f"Modo Individual - Dificuldade: {difficulty}")
    score = 0
    operations = ["+", "-", "*", "/"]
    
    for operation in operations:
        equation = generate_equation(difficulty)
        print(f"\nResolva a seguinte equação em até 20 segundos:")
        print(equation)
        
        start_time = time.time()
        user_answer = input("Resposta: ")
        end_time = time.time()
        
        response_time = end_time - start_time
        
        if response_time > 20:
            print("Tempo esgotado! Zero pontos.")
            score = 0
            break
        
        correct_answer = eval(equation)
        if float(user_answer) == correct_answer:
            operation_score = calculate_score(response_time)
            score += operation_score
            print(f"Resposta correta! Pontos ganhos: {operation_score}")
        else:
            print("Resposta incorreta! Zero pontos.")
            score = 0
            break
    
    print(f"\nPlacar final: {score} pontos")

def play_duo(difficulty):
    print(f"Modo Duas Pessoas - Dificuldade: {difficulty}")
    score_player1 = 0
    score_player2 = 0
    operations = ["+", "-", "*", "/"]
    
    for operation in operations:
        equation = generate_equation(difficulty)
        print(f"\nResolva a seguinte equação em até 20 segundos:")
        print(equation)
        
        start_time = time.time()
        user_answer_player1 = input("Jogador 1 - Resposta: ")
        end_time = time.time()
        
        response_time = end_time - start_time
        
        if response_time > 20:
            print("Tempo esgotado! Zero pontos para o Jogador 1.")
            score_player1 = 0
            score_player2 += 10  # Jogador 2 ganha 10 pontos por tempo esgotado do Jogador 1
            break
        
        correct_answer = eval(equation)
        if float(user_answer_player1) == correct_answer:
            operation_score = calculate_score(response_time)
            score_player1 += operation_score
            print(f"Resposta correta! Pontos ganhos pelo Jogador 1: {operation_score}")
        else:
            print("Resposta incorreta! Zero pontos para o Jogador 1.")
            score_player1 = 0

def main():
    print("Bem-vindo ao Jogo das Operações Matemáticas!")
    print("Escolha uma opção:")
    print("1. Jogar individualmente")
    print("2. Jogar em dupla")
    option = input("Opção: ")
    
    if option == "1":
        print("Escolha a dificuldade:")
        print("1. Fácil")
        print("2. Médio")
        print("3. Difícil")
        difficulty_option = input("Opção: ")
        
        if difficulty_option == "1":
            difficulty = "Fácil"
        elif difficulty_option == "2":
            difficulty = "Médio"
        elif difficulty_option == "3":
            difficulty = "Difícil"
        
        play_individual(difficulty)
        
    elif option == "2":
        print("Escolha a dificuldade:")
        print("1. Fácil")
        print("2. Médio")
        print("3. Difícil")
        difficulty_option = input("Opção: ")
        
        if difficulty_option == "1":
            difficulty = "Fácil"
        elif difficulty_option == "2":
            difficulty = "Médio"
        elif difficulty_option == "3":
            difficulty = "Difícil"
        
        play_duo(difficulty)
        
    else:
        print("Opção inválida. Por favor, escolha novamente.")
        main()

main()