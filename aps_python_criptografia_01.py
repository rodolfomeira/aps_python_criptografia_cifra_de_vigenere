def preparar_texto(texto):
    """
    Remove espaços e transforma o texto para letras minúsculas.
    Isso padroniza o texto para evitar problemas com maiúsculas/minúsculas
    e facilita a aplicação da cifra de Vigenère, que opera em letras.
    """
    return texto.lower()  # Converte o texto para letras minúsculas.


def gerar_chave(texto, chave):
    """
    Gera uma chave repetida até o tamanho do texto.
    Se a chave fornecida for menor que o texto, ela será repetida ciclicamente
    até que seu comprimento seja igual ao do texto. Em seguida, converte cada letra
    da chave para sua posição no alfabeto (0 para 'a', 1 para 'b', etc.).
    
    Parâmetros:
    - texto: texto que será criptografado/descriptografado.
    - chave: chave usada para criptografia/descriptografia.

    Retorno:
    - Uma lista de inteiros representando o valor numérico de cada letra da chave.
    """
    chave = list(chave)  # Converte a chave em uma lista de caracteres.
    if len(chave) == len(texto):  # Verifica se o tamanho da chave é igual ao do texto.
        return [ord(c) - ord('a') for c in chave]  # Converte cada letra da chave em número (posição no alfabeto).
    else:
        # Se a chave for menor que o texto, repete a chave até alcançar o tamanho necessário.
        for i in range(len(texto) - len(chave)):
            chave.append(chave[i % len(chave)])  # Adiciona letras da chave repetidamente.
    return [ord(c) - ord('a') for c in chave]  # Retorna a chave ajustada em forma de números.


def criptografar(texto, chave, alfabeto):
    """
    Criptografa o texto usando a cifra de Vigenère, mantendo números e caracteres especiais inalterados.
    Para cada letra do texto, aplica um deslocamento no alfabeto de acordo com o valor da chave correspondente.
    
    Parâmetros:
    - texto: texto a ser criptografado.
    - chave: lista de inteiros gerada pela função 'gerar_chave', representando os deslocamentos para cada letra.
    - alfabeto: string contendo o alfabeto usado para criptografia (ex: 'abcdefghijklmnopqrstuvwxyz').

    Retorno:
    - Uma string contendo o texto criptografado.
    """
    texto_convertido = ""  # Armazena o resultado da criptografia.
    tamanho = len(alfabeto)  # Obtém o tamanho do alfabeto (ex: 26 letras).

    for i, letra in enumerate(texto):  # Itera sobre cada letra do texto com seu índice.
        if letra in alfabeto:  # Verifica se a letra está no alfabeto (ignora números e símbolos).
            ind_o = alfabeto.index(letra)  # Posição da letra no alfabeto.
            ind_novo = (ind_o + chave[i % len(chave)]) % tamanho  # Calcula o índice da nova letra somando o valor da chave.
            texto_convertido += alfabeto[ind_novo]  # Adiciona a nova letra criptografada ao texto convertido.
        else:
            texto_convertido += letra  # Se a letra não está no alfabeto, mantém a original.
    
    return texto_convertido  # Retorna o texto criptografado.


def descriptografar(texto, chave, alfabeto):
    """
    Descriptografa o texto usando a cifra de Vigenère, mantendo números e caracteres especiais inalterados.
    Para cada letra criptografada, aplica um deslocamento inverso usando o valor da chave correspondente.
    
    Parâmetros:
    - texto: texto a ser descriptografado.
    - chave: lista de inteiros gerada pela função 'gerar_chave', representando os deslocamentos para cada letra.
    - alfabeto: string contendo o alfabeto usado para criptografia.

    Retorno:
    - Uma string contendo o texto descriptografado.
    """
    texto_convertido = ""  # Armazena o resultado da descriptografia.
    tamanho = len(alfabeto)  # Obtém o tamanho do alfabeto (ex: 26 letras).

    for i, letra in enumerate(texto):  # Itera sobre cada letra do texto com seu índice.
        if letra in alfabeto:  # Verifica se a letra está no alfabeto (ignora números e símbolos).
            ind_o = alfabeto.index(letra)  # Posição original da letra criptografada no alfabeto.
            ind_novo = (ind_o - chave[i % len(chave)]) % tamanho  # Calcula o índice da nova letra subtraindo o valor da chave.
            texto_convertido += alfabeto[ind_novo]  # Adiciona a nova letra descriptografada ao texto convertido.
        else:
            texto_convertido += letra  # Se a letra não está no alfabeto, mantém a original.
    
    return texto_convertido  # Retorna o texto descriptografado.


def menu():
    """
    Exibe o menu de opções e permite ao usuário criptografar, descriptografar ou sair.
    Essa função faz o controle principal do fluxo do programa e permite interação
    com o usuário.
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"  # Define o alfabeto utilizado.

    while True:  # Laço infinito para manter o menu até o usuário decidir sair.
        # Exibe as opções do menu
        print("\n*** Menu Cifra de Vigenère ***")
        print("1. Criptografar Texto")
        print("2. Descriptografar Texto")
        print("3. Sair")
        
        # Solicita a escolha do usuário e trata possíveis erros de entrada
        try:
            opcao = int(input("Escolha uma opção (1-3): "))  # Captura a opção digitada pelo usuário.
        except ValueError:  # Captura erro caso o usuário não insira um número.
            print("Entrada inválida. Por favor, insira um número entre 1 e 3.")
            continue  # Volta ao início do laço, solicitando nova entrada.

        if opcao == 1:  # Caso a opção seja "Criptografar"
            texto = input("Digite o texto para criptografar: ")  # Solicita o texto a ser criptografado.
            chave = input("Digite a chave para criptografia (somente letras): ")  # Solicita a chave de criptografia.

            # Verifica se a chave contém apenas letras
            if not chave.isalpha():
                print("Erro: a chave deve conter apenas letras.")  # Exibe erro se a chave tiver outros caracteres.
                continue  # Volta ao início do laço.

            texto = preparar_texto(texto)  # Padroniza o texto (minúsculas).
            chave = preparar_texto(chave)  # Padroniza a chave (minúsculas).
            chave_ajustada = gerar_chave(texto, chave)  # Gera a chave ajustada com base no tamanho do texto.
            texto_criptografado = criptografar(texto, chave_ajustada, alfabeto)  # Criptografa o texto.
            print("Texto criptografado: {}".format(texto_criptografado))  # Exibe o texto criptografado.

        elif opcao == 2:  # Caso a opção seja "Descriptografar"
            texto = input("Digite o texto para descriptografar: ")  # Solicita o texto a ser descriptografado.
            chave = input("Digite a chave para descriptografia (somente letras): ")  # Solicita a chave de descriptografia.

            # Verifica se a chave contém apenas letras
            if not chave.isalpha():
                print("Erro: a chave deve conter apenas letras.")  # Exibe erro se a chave tiver outros caracteres.
                continue  # Volta ao início do laço.

            texto = preparar_texto(texto)  # Padroniza o texto (minúsculas).
            chave = preparar_texto(chave)  # Padroniza a chave (minúsculas).
            chave_ajustada = gerar_chave(texto, chave)  # Gera a chave ajustada com base no tamanho do texto.
            texto_descriptografado = descriptografar(texto, chave_ajustada, alfabeto)  # Descriptografa o texto.
            print("Texto descriptografado: {}".format(texto_descriptografado))  # Exibe o texto descriptografado.

        elif opcao == 3:  # Caso a opção seja "Sair"
            print("Encerrando o programa...")  # Exibe mensagem de encerramento.
            break  # Sai do laço e encerra o programa.

        else:  # Caso o usuário insira uma opção inválida
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 3.")  # Exibe mensagem de erro.


# Chama o menu para iniciar o programa
menu()
