def jogo_adivinhacao():
    numero_secreto = 7  # você pode trocar esse número
    tentativa = 0

    print("**Jogo de Adivinhação!**")
    print("\nTente adivinhar o número secreto de 1 a 10.")

    while tentativa != numero_secreto:
        tentativa = int(input("\nDigite sua tentativa: "))
        
        if tentativa != numero_secreto:
            print("Errado! Tente novamente.")
        else:
            print("Parabéns! Você acertou o número!")

# Chama a função para iniciar o jogo
jogo_adivinhacao()