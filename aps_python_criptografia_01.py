import string  # Importa o módulo string que contém o alfabeto.

def preparar_texto(texto):
    """
    Remove caracteres não alfabéticos e transforma o texto para letras minúsculas.
    """
    texto = texto.lower()  # Transforma todo o texto para letras minúsculas.
    return ''.join(filter(str.isalpha, texto))  # Filtra apenas os caracteres alfabéticos e os une novamente em uma string.

def gerar_chave(texto, chave):
    """
    Gera uma chave repetida até o tamanho do texto e a converte para valores numéricos.
    """
    chave = preparar_texto(chave)  # Remove caracteres não alfabéticos e transforma a chave em minúscula.
    chave = list(chave)  # Converte a chave para uma lista de caracteres.
    
    if len(chave) == 0:  # Se a chave estiver vazia, gera um erro.
        raise ValueError("A chave não pode ser vazia.")

    # Repete a chave até que o seu tamanho seja igual ao do texto.
    for indice in range(len(texto) - len(chave)):
        chave.append(chave[indice % len(chave)])  # Adiciona letras da chave original ciclicamente até alcançar o tamanho do texto.

    return [ord(c) - ord('a') for c in chave]  # Converte cada letra da chave para sua posição no alfabeto ('a' = 0, 'b' = 1, etc.).

def criptografar(texto, chave, alfabeto):
    """
    Criptografa o texto usando a cifra de Vigenère.
    """
    texto_convertido = ""  # Inicializa uma string vazia para armazenar o texto criptografado.
    tamanho = len(alfabeto)  # Armazena o tamanho do alfabeto (por exemplo, 26 letras).
    chave_index = 0  # Inicializa o índice da chave.

    # Percorre cada letra do texto.
    for letra in texto:
        if letra in alfabeto:  # Verifica se a letra está no alfabeto.
            indice_original = alfabeto.index(letra)  # Obtém a posição original da letra no alfabeto.
            indice_novo = (indice_original + chave[chave_index]) % tamanho  # Calcula a nova posição da letra somando o valor da chave.
            texto_convertido += alfabeto[indice_novo]  # Adiciona a nova letra criptografada ao texto convertido.
            chave_index += 1  # Avança para a próxima letra da chave.
        else:
            texto_convertido += letra  # Se a letra não estiver no alfabeto, apenas a adiciona ao texto sem modificações.

    return texto_convertido  # Retorna o texto criptografado.

def descriptografar(texto, chave, alfabeto):
    """
    Descriptografa o texto usando a cifra de Vigenère.
    """
    texto_convertido = ""  # Inicializa uma string vazia para armazenar o texto descriptografado.
    tamanho = len(alfabeto)  # Armazena o tamanho do alfabeto.
    chave_index = 0  # Inicializa o índice da chave.

    # Percorre cada letra do texto.
    for letra in texto:
        if letra in alfabeto:  # Verifica se a letra está no alfabeto.
            indice_original = alfabeto.index(letra)  # Obtém a posição original da letra no alfabeto.
            indice_novo = (indice_original - chave[chave_index]) % tamanho  # Calcula a nova posição da letra subtraindo o valor da chave.
            texto_convertido += alfabeto[indice_novo]  # Adiciona a nova letra descriptografada ao texto convertido.
            chave_index += 1  # Avança para a próxima letra da chave.
        else:
            texto_convertido += letra  # Se a letra não estiver no alfabeto, apenas a adiciona ao texto sem modificações.

    return texto_convertido  # Retorna o texto descriptografado.

def menu():
    """
    Exibe o menu e permite ao usuário criptografar, descriptografar ou sair.
    """
    alfabeto = string.ascii_lowercase  # Define o alfabeto como as letras minúsculas.

    # Laço principal do menu.
    while True:
        # Exibe as opções do menu.
        print("\n*** Menu Cifra de Vigenère ***")
        print("1. Criptografar Texto")
        print("2. Descriptografar Texto")
        print("3. Sair")
        
        # Solicita a escolha do usuário e trata erros de entrada.
        try:
            opcao = int(input("Escolha uma opção (1-3): "))  # Solicita a opção escolhida pelo usuário.
        except ValueError:  # Se o usuário não inserir um número válido.
            print("Entrada inválida. Por favor, insira um número entre 1 e 3.")  # Exibe uma mensagem de erro.
            continue  # Retorna ao início do laço para tentar novamente.

        if opcao == 1:  # Se o usuário escolher a opção de criptografar.
            texto = input("Digite o texto para criptografar: ")  # Solicita o texto a ser criptografado.

            # Laço que garante que a chave seja válida.
            while True:
                chave = input("Digite a chave para criptografia (somente letras): ")  # Solicita a chave de criptografia.
                if chave.isalpha():  # Verifica se a chave contém apenas letras.
                    break  # Se a chave for válida, sai do laço.
                else:
                    print("Erro: a chave deve conter apenas letras, sem espaços ou símbolos. Tente novamente.")  # Mensagem de erro.

            texto_preparado = preparar_texto(texto)  # Remove caracteres não alfabéticos e transforma o texto para minúsculo.
            if not texto_preparado:  # Se o texto estiver vazio após a limpeza.
                print("Erro: o texto não pode ser vazio.")  # Mensagem de erro.
                continue  # Volta ao início do laço para uma nova entrada.

            try:
                chave_ajustada = gerar_chave(texto_preparado, chave)  # Gera a chave ajustada para o texto.
                texto_criptografado = criptografar(texto, chave_ajustada, alfabeto)  # Criptografa o texto.
                print("Texto criptografado: {}".format(texto_criptografado))  # Exibe o texto criptografado.
            except ValueError as ve:  # Se houver algum erro no processo.
                print(ve)  # Exibe a mensagem de erro.

        elif opcao == 2:  # Se o usuário escolher a opção de descriptografar.
            texto = input("Digite o texto para descriptografar: ")  # Solicita o texto a ser descriptografado.

            # Laço que garante que a chave seja válida.
            while True:
                chave = input("Digite a chave para descriptografia (somente letras): ")  # Solicita a chave de descriptografar.
                if chave.isalpha():  # Verifica se a chave contém apenas letras.
                    break  # Se a chave for válida, sai do laço.
                else:
                    print("Erro: a chave deve conter apenas letras, sem espaços ou símbolos. Tente novamente.")  # Mensagem de erro.

            texto_preparado = preparar_texto(texto)  # Remove caracteres não alfabéticos e transforma o texto para minúsculo.
            if not texto_preparado:  # Se o texto estiver vazio após a limpeza.
                print("Erro: o texto não pode ser vazio.")  # Mensagem de erro.
                continue  # Volta ao início do laço para uma nova entrada.

            try:
                chave_ajustada = gerar_chave(texto_preparado, chave)  # Gera a chave ajustada para o texto.
                texto_descriptografado = descriptografar(texto, chave_ajustada, alfabeto)  # Descriptografa o texto.
                print("Texto descriptografado: {}".format(texto_descriptografado))  # Exibe o texto descriptografado.
            except ValueError as ve:  # Se houver algum erro no processo.
                print(ve)  # Exibe a mensagem de erro.

        elif opcao == 3:  # Se o usuário escolher sair.
            print("Encerrando o programa...")  # Exibe uma mensagem de saída.
            break  # Encerra o laço e o programa.

        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 3.")  # Mensagem de erro para opção inválida.

# Chama o menu para iniciar o programa.
menu()
