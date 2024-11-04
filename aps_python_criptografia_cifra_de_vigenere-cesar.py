import os  # Importa o módulo os para executar comandos do sistema, como limpar a tela.

def preparar_texto(texto):
    # Inicializa a variavel vazia para armazenar caracteres do texto.
    resultado = ''
    
    # Itera sobre cada caractere em 'texto'.
    for letra in texto:
        # Adiciona o caractere à letra 'resultado'.
        resultado += letra
    # Retorna a letra 'resultado' apenas com os caracteres.
    return resultado

def gerar_chave(texto, chave):
    # Remove caracteres indesejados da chave.
    chave = preparar_texto(chave)
    # Converte a chave em uma lista para permitir modificação.
    chave = list(chave)
    
    # Verifica se a chave está vazia e lança um erro se necessário.
    if len(chave) == 0:
        raise ValueError('A chave não pode ser vazia.')

    # Expande a chave repetindo seus caracteres até que tenha o mesmo tamanho de 'texto'.
    for indice in range(len(texto) - len(chave)):
        # Adiciona caracteres da chave original ciclicamente.
        chave.append(chave[indice % len(chave)])
    
    # Retorna a chave em forma de lista de inteiros, onde 'a' = 0, 'b' = 1, etc.
    return [ord(c) - ord('a') for c in chave]

def cifra_cesar(chave):
    # Solicita um valor numérico para o deslocamento da cifra de César.
    while True:
        deslocamento = input('Escolha um número para criptografar sua chave: ')
        # Verifica se o valor é numérico.
        if deslocamento.isdigit():
            deslocamento = int(deslocamento)  # Converte para inteiro se for numérico.
            break
        else:
            print('Erro: o valor de deslocamento deve ser um número. Tente novamente.')

    # Define o alfabeto como uma string de letras minúsculas.
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    # Inicializa uma string para armazenar a chave criptografada.
    chave_convertida = ''

    # Itera sobre cada letra em 'chave'.
    for letra in chave:
        # Verifica se a letra está no alfabeto.
        if letra in alfabeto:
            # Encontra a posição da letra no alfabeto.
            indice_original = alfabeto.index(letra)
            # Calcula a nova posição somando o deslocamento e aplicando módulo.
            indice_novo = (indice_original + deslocamento) % len(alfabeto)
            # Adiciona a letra deslocada à chave convertida.
            chave_convertida += alfabeto[indice_novo]
        else:
            # Se o caractere não é uma letra, adiciona-o sem alterações.
            chave_convertida += letra

    # Retorna a chave convertida após a aplicação da cifra de César.
    return chave_convertida

def criptografar(texto, chave, alfabeto):
    # Inicializa uma string para armazenar o texto criptografado.
    texto_convertido = ''
    # Armazena o tamanho do alfabeto.
    tamanho = len(alfabeto)
    # Define o índice inicial da chave.
    chave_index = 0

    # Itera sobre cada letra no 'texto'.
    for letra in texto:
        # Verifica se a letra está no alfabeto.
        if letra in alfabeto:
            # Encontra a posição original da letra.
            indice_original = alfabeto.index(letra)
            # Calcula a nova posição somando o valor da chave.
            indice_novo = (indice_original + chave[chave_index]) % tamanho
            # Adiciona a nova letra criptografada ao texto convertido.
            texto_convertido += alfabeto[indice_novo]
            # Avança para o próximo caractere da chave.
            chave_index += 1
        else:
            # Se o caractere não é uma letra, adiciona-o sem alterações.
            texto_convertido += letra

    # Retorna o texto criptografado.
    return texto_convertido

def descriptografar(texto, chave, alfabeto):
    # Inicializa uma string para armazenar o texto descriptografado.
    texto_convertido = ''
    # Armazena o tamanho do alfabeto.
    tamanho = len(alfabeto)
    # Define o índice inicial da chave.
    chave_index = 0

    # Itera sobre cada letra no 'texto'.
    for letra in texto:
        # Verifica se a letra está no alfabeto.
        if letra in alfabeto:
            # Encontra a posição original da letra.
            indice_original = alfabeto.index(letra)
            # Calcula a nova posição subtraindo o valor da chave.
            indice_novo = (indice_original - chave[chave_index]) % tamanho
            # Adiciona a nova letra descriptografada ao texto convertido.
            texto_convertido += alfabeto[indice_novo]
            # Avança para o próximo caractere da chave.
            chave_index += 1
        else:
            # Se o caractere não é uma letra, adiciona-o sem alterações.
            texto_convertido += letra

    # Retorna o texto descriptografado.
    return texto_convertido

def menu():
    # Define o alfabeto com letras minúsculas.
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    # Laço principal do menu.
    while True:
        # Exibe as opções de menu.
        os.system('cls')
        print('*** Menu Cifra de Vigenère *** \n')
        print('1. Criptografar Texto')
        print('2. Descriptografar Texto')
        print('3. Sair')
        
        # Solicita a escolha do usuário e verifica erros de entrada.
        try:
            opcao = int(input('Escolha uma opção (1-3): '))
        except ValueError:
            print('Entrada inválida. Por favor, insira um número entre 1 e 3.')
            continue

        if opcao == 1:
            os.system('cls')
            print('**Opção 1 - Criptografar** \n')
            # Solicita o texto a ser criptografado e o converte para minúsculas.
            texto = input('Digite o texto para criptografar: ').lower()

            # Laço para garantir que a chave contenha apenas letras.
            while True:
                chave = input('Digite a chave para criptografia (somente letras): ').lower()
                if chave.isalpha():
                    break
                else:
                    print('Erro: a chave deve conter apenas letras, sem espaços ou símbolos. Tente novamente.')

            # Remove caracteres não alfabéticos do texto.
            texto_preparado = preparar_texto(texto)
            # Verifica se o texto não está vazio.
            if not texto_preparado:
                print('Erro: o texto não pode ser vazio.')
                continue

            try:
                # Gera a chave ajustada e criptografa o texto.
                chave_ajustada = gerar_chave(texto_preparado, cifra_cesar(chave))
                texto_criptografado = criptografar(texto_preparado, chave_ajustada, alfabeto)
                print('Texto criptografado: {}'.format(texto_criptografado))
                print('Precione "Enter" para continuar!')
            except ValueError as mensagem:
                print(mensagem)
            input()
            os.system('cls')

        elif opcao == 2:
            os.system('cls')
            print('**Opção 2 - Descriptografar** \n')
            # Solicita o texto a ser descriptografado e o converte para minúsculas.
            texto = input('Digite o texto para descriptografar: ').lower()

            # Laço para garantir que a chave contenha apenas letras.
            while True:
                chave = input('Digite a chave para descriptografia (somente letras): ').lower()
                if chave.isalpha():
                    break
                else:
                    print('Erro: a chave deve conter apenas letras, sem espaços ou símbolos. Tente novamente.')

            # Remove caracteres não alfabéticos do texto.
            texto_preparado = preparar_texto(texto)
            # Verifica se o texto não está vazio.
            if not texto_preparado:
                print('Erro: o texto não pode ser vazio.')
                continue

            try:
                # Gera a chave ajustada e descriptografa o texto.
                chave_ajustada = gerar_chave(texto_preparado, cifra_cesar(chave))
                texto_descriptografado = descriptografar(texto_preparado, chave_ajustada, alfabeto)
                print('Texto descriptografado: {}'.format(texto_descriptografado))
                print('Precione "Enter" para continuar!')
            except ValueError as mensagem:
                print(mensagem)
            input()
            os.system('cls')

        elif opcao == 3:
            os.system('cls')
            print('Encerrando o programa...')
            break

        else:
            print('Opção inválida. Por favor, escolha uma opção entre 1 e 3.')

# Inicia o programa chamando o menu.
menu()
