def preparar_texto(texto):
    """
    Remove espaços e transforma o texto para letras minúsculas.
    """
    # Substitui espaços por nada e transforma todas as letras para minúsculas
    # Isso padroniza o texto para facilitar a criptografia e descriptografia
    return texto.replace(" ", "").lower()

def gerar_chave(texto, chave):
    """
    Gera uma chave repetida até o tamanho do texto.
    """
    # Transforma a chave em uma lista de caracteres para facilitar a manipulação
    chave = list(chave)
    
    # Se a chave já tiver o mesmo tamanho do texto, não há necessidade de alteração
    if len(chave) == len(texto):
        # Retorna a chave como string ao invés de uma lista
        return "".join(chave)
    else:
        # Se a chave for menor, ela é repetida até alcançar o tamanho do texto
        for i in range(len(texto) - len(chave)):
            # Utiliza o operador % para repetir os caracteres da chave original
            chave.append(chave[i % len(chave)])
    # Junta os caracteres da lista de volta em uma string e retorna a chave ajustada
    return "".join(chave)

def criptografar(texto, chave):
    """
    Realiza a criptografia usando a cifra de Vigenère.
    """
    # Lista que armazenará o texto criptografado
    texto_convertido = []
    
    # Itera sobre cada caractere do texto
    for i in range(len(texto)):
        # Calcula o novo índice da letra com base no valor ASCII do texto e da chave
        # Faz o cálculo de deslocamento com base no alfabeto (mod 26)
        x = (ord(texto[i]) + ord(chave[i])) % 26
        
        # Adiciona o valor ASCII de 'a' para obter a letra correta no alfabeto
        x += ord('a')
        
        # Converte o valor numérico para a letra correspondente e adiciona ao texto criptografado
        texto_convertido.append(chr(x))
    
    # Junta os caracteres convertidos em uma string e retorna o texto criptografado
    return "".join(texto_convertido)

def descriptografar(texto, chave):
    """
    Realiza a descriptografia usando a cifra de Vigenère.
    """
    # Lista que armazenará o texto descriptografado
    texto_convertido = []
    
    # Itera sobre cada caractere do texto
    for i in range(len(texto)):
        # Faz o cálculo de inversão da criptografia subtraindo o valor da chave
        # Adiciona 26 para garantir que o índice seja positivo, em seguida faz mod 26
        x = (ord(texto[i]) - ord(chave[i]) + 26) % 26
        
        # Adiciona o valor ASCII de 'a' para obter a letra correta no alfabeto
        x += ord('a')
        
        # Converte o valor numérico para a letra correspondente e adiciona ao texto descriptografado
        texto_convertido.append(chr(x))
    
    # Junta os caracteres convertidos em uma string e retorna o texto descriptografado
    return "".join(texto_convertido)

def menu():
    """
    Exibe o menu de opções e permite ao usuário criptografar, descriptografar ou sair.
    """
    # Laço infinito para manter o menu ativo até o usuário decidir sair
    while True:
        # Exibe o menu de opções
        print("\n*** Menu Cifra de Vigenère ***")
        print("1. Criptografar Texto")
        print("2. Descriptografar Texto")
        print("3. Sair")
        
        # Tenta ler a entrada do usuário e converter para um número inteiro
        try:
            opcao = int(input("Escolha uma opção (1-3): "))
        except ValueError:
            # Se o usuário inserir algo que não seja número, exibe erro e reinicia o laço
            print("Entrada inválida. Por favor, insira um número entre 1 e 3.")
            continue  # Volta ao início do laço, solicitando nova entrada

        # Se o usuário escolher a opção de criptografar (1)
        if opcao == 1:
            # Solicita o texto e a chave
            texto = input("Digite o texto para criptografar (somente letras): ")
            chave = input("Digite a chave para criptografia (somente letras): ")

            # Verifica se o texto e a chave contêm apenas letras (sem números ou símbolos)
            if not texto.isalpha() or not chave.isalpha():
                print("Erro: o texto e a chave devem conter apenas letras.")
                continue  # Volta ao início do laço

            # Prepara o texto e a chave, removendo espaços e convertendo para minúsculas
            texto = preparar_texto(texto)
            chave = preparar_texto(chave)
            
            # Gera uma chave do mesmo tamanho que o texto
            chave_ajustada = gerar_chave(texto, chave)
            
            # Criptografa o texto com a chave ajustada
            texto_criptografado = criptografar(texto, chave_ajustada)
            
            # Exibe o texto criptografado
            print(f"Texto criptografado: {texto_criptografado}")

        # Se o usuário escolher a opção de descriptografar (2)
        elif opcao == 2:
            # Solicita o texto e a chave
            texto = input("Digite o texto para descriptografar (somente letras): ")
            chave = input("Digite a chave para descriptografia (somente letras): ")

            # Verifica se o texto e a chave contêm apenas letras
            if not texto.isalpha() or not chave.isalpha():
                print("Erro: o texto e a chave devem conter apenas letras.")
                continue  # Volta ao início do laço

            # Prepara o texto e a chave, removendo espaços e convertendo para minúsculas
            texto = preparar_texto(texto)
            chave = preparar_texto(chave)
            
            # Gera uma chave do mesmo tamanho que o texto
            chave_ajustada = gerar_chave(texto, chave)
            
            # Descriptografa o texto com a chave ajustada
            texto_descriptografado = descriptografar(texto, chave_ajustada)
            
            # Exibe o texto descriptografado
            print(f"Texto descriptografado: {texto_descriptografado}")

        # Se o usuário escolher a opção de sair (3)
        elif opcao == 3:
            # Exibe uma mensagem e encerra o programa
            print("Encerrando o programa...")
            break  # Sai do laço, encerrando o menu

        # Se o usuário digitar uma opção inválida
        else:
            # Exibe uma mensagem de erro e volta ao início do laço
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 3.")

# Inicia o menu e, portanto, o programa
menu()
