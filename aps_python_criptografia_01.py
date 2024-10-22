def preparar_texto(texto):
    """
    Remove espaços e transforma o texto para letras minúsculas.
    """
    return texto.lower()

def gerar_chave(texto, chave):
    """
    Gera uma chave repetida até o tamanho do texto.
    """
    chave = list(chave)
    if len(chave) == len(texto):
        return [ord(c) - ord('a') for c in chave]
    else:
        for i in range(len(texto) - len(chave)):
            chave.append(chave[i % len(chave)])
    return [ord(c) - ord('a') for c in chave]

def criptografar(texto, chave, alfabeto):
    """
    Realiza a criptografia usando a cifra de Vigenère, mantendo números e caracteres especiais inalterados.
    """
    texto_convertido = ""
    tamanho = len(alfabeto)
    
    for i, letra in enumerate(texto):
        if letra in alfabeto:
            # Obtém o índice da letra no alfabeto
            ind_o = alfabeto.index(letra)
            # Calcula o novo índice somando a chave (criptografia)
            ind_novo = (ind_o + chave[i % len(chave)]) % tamanho
            # Adiciona a letra correspondente ao novo índice
            texto_convertido += alfabeto[ind_novo]
        else:
            # Mantém o caractere original se não estiver no alfabeto (números, espaços, etc.)
            texto_convertido += letra
    
    return texto_convertido

def descriptografar(texto, chave, alfabeto):
    """
    Realiza a descriptografia usando a cifra de Vigenère, mantendo números e caracteres especiais inalterados.
    """
    texto_convertido = ""
    tamanho = len(alfabeto)
    
    for i, letra in enumerate(texto):
        if letra in alfabeto:
            # Obtém o índice da letra no alfabeto
            ind_o = alfabeto.index(letra)
            # Calcula o novo índice subtraindo a chave (descriptografia)
            ind_novo = (ind_o - chave[i % len(chave)]) % tamanho
            # Ajusta o índice se for negativo (rotação inversa)
            if ind_novo < 0:
                ind_novo = tamanho + ind_novo
            # Adiciona a letra correspondente ao novo índice
            texto_convertido += alfabeto[ind_novo]
        else:
            # Mantém o caractere original se não estiver no alfabeto (números, espaços, etc.)
            texto_convertido += letra
    
    return texto_convertido

def menu():
    """
    Exibe o menu de opções e permite ao usuário criptografar, descriptografar ou sair.
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    
    while True:
        print("\n*** Menu Cifra de Vigenère ***")
        print("1. Criptografar Texto")
        print("2. Descriptografar Texto")
        print("3. Sair")
        
        # Solicita a escolha do usuário e trata possíveis erros de entrada
        try:
            opcao = int(input("Escolha uma opção (1-3): "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número entre 1 e 3.")
            continue  # Volta ao início do laço, solicitando nova entrada

        if opcao == 1:
            texto = input("Digite o texto para criptografar: ")
            chave = input("Digite a chave para criptografia (somente letras): ")

            # Verifica se a chave contém apenas letras
            if not chave.isalpha():
                print("Erro: a chave deve conter apenas letras.")
                continue  # Volta ao início do laço

            texto = preparar_texto(texto)
            chave = preparar_texto(chave)
            chave_ajustada = gerar_chave(texto, chave)
            texto_criptografado = criptografar(texto, chave_ajustada, alfabeto)
            print(f"Texto criptografado: {texto_criptografado}")

        elif opcao == 2:
            texto = input("Digite o texto para descriptografar: ")
            chave = input("Digite a chave para descriptografia (somente letras): ")

            # Verifica se a chave contém apenas letras
            if not chave.isalpha():
                print("Erro: a chave deve conter apenas letras.")
                continue  # Volta ao início do laço

            texto = preparar_texto(texto)
            chave = preparar_texto(chave)
            chave_ajustada = gerar_chave(texto, chave)
            texto_descriptografado = descriptografar(texto, chave_ajustada, alfabeto)
            print(f"Texto descriptografado: {texto_descriptografado}")

        elif opcao == 3:
            print("Encerrando o programa...")
            break  # Encerra o laço e sai do programa

        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 3.")

# Chama o menu para iniciar o programa
menu()
