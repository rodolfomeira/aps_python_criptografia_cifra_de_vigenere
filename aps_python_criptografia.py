alfabeto = 'abcdefghijklmnopqrstuvwxyz'

# Função para encontrar o índice de uma letra no alfabeto
def indice_alfabeto(letra, alfabeto):
    return alfabeto.index(letra)

def chave_aument(mensagem, chave):
    chave_expandida = ""  # Inicializa a chave expandida
    indice = 0  # Variável para controlar o índice da chave
    tam_chave = len(chave)  # Armazena o tamanho da chave
    
    for letra in mensagem:  # Itera sobre cada caractere da mensagem
        if letra in alfabeto:  # Verifica se o caractere está no alfabeto
            chave_expandida += chave[indice]  # Adiciona o caractere da chave
            indice += 1  # Incrementa o índice da chave
            if indice == tam_chave:  # Reinicia o índice se atingir o tamanho da chave
                indice = 0
        else:
            chave_expandida += letra  # Mantém caracteres que não são letras inalterados
    return chave_expandida  # Retorna a chave expandida

def cifra_vigenere(mensagem, chave):
    resultado = ""  # Inicializa a string para armazenar a mensagem encriptada
    chave_expandida = chave_aument(mensagem, chave)  # Expande a chave para corresponder ao tamanho da mensagem
    tam_alfabeto = len(alfabeto)  # Armazena o tamanho do alfabeto
    
    for i in range(len(mensagem)):  # Itera sobre cada caractere da mensagem
        if mensagem[i] in alfabeto:  # Verifica se o caractere está no alfabeto
            indice_msg = indice_alfabeto(mensagem[i], alfabeto)  # Índice da letra da mensagem
            indice_chave = indice_alfabeto(chave_expandida[i], alfabeto)  # Índice da letra da chave
            novo_indice = indice_msg + indice_chave
            if novo_indice >= tam_alfabeto:  # Se o índice ultrapassar o limite do alfabeto
                novo_indice -= tam_alfabeto  # Subtrai o tamanho do alfabeto para "voltar ao início"

            nova_letra = alfabeto[novo_indice]  # Obtém a nova letra a partir do índice
            resultado += nova_letra  # Adiciona a nova letra ao resultado
        else:
            resultado += mensagem[i]  # Mantém caracteres que não são letras inalterados

    return resultado  # Retorna a mensagem encriptada

def decifra_vigenere(mensagem, chave):
    resultado = ""  # Inicializa a string para armazenar a mensagem descriptografada
    chave_expandida = chave_aument(mensagem, chave)  # Expande a chave para corresponder ao tamanho da mensagem
    tam_alfabeto = len(alfabeto)  # Armazena o tamanho do alfabeto
    
    for i in range(len(mensagem)):  # Itera sobre cada caractere da mensagem
        if mensagem[i] in alfabeto:  # Verifica se o caractere está no alfabeto
            indice_msg = indice_alfabeto(mensagem[i], alfabeto)  # Índice da letra da mensagem
            indice_chave = indice_alfabeto(chave_expandida[i], alfabeto)  # Índice da letra da chave
            novo_indice = indice_msg - indice_chave
            if novo_indice < 0:  # Se o índice for negativo, ajusta manualmente
                novo_indice += tam_alfabeto  # Adiciona o tamanho do alfabeto para "voltar ao final"

            nova_letra = alfabeto[novo_indice]  # Obtém a nova letra a partir do índice
            resultado += nova_letra  # Adiciona a nova letra ao resultado
        else:
            resultado += mensagem[i]  # Mantém caracteres que não são letras inalterados

    return resultado  # Retorna a mensagem descriptografada

# Mensagens para o usuário usuário
mensagem = input("Digite uma mensagem: ")
chave = input("Digite a chave: ")
cd = int(input("Digite 1 para criptografar e 2 para descriptografar: "))
while cd != 1 and cd != 2:
    cd = int(input("Opção incorreta. Digite 1 para criptografar e 2 para descriptografar: "))

if cd == 1:
    mensagem_crip = cifra_vigenere(mensagem, chave)  # Criptografa a mensagem usando a chave
    print("Mensagem Criptografada:", mensagem_crip)  # Exibe a mensagem encriptada
else:
    mensagem_descriptografada = decifra_vigenere(mensagem, chave)  # Desencripta a mensagem encriptada usando a mesma chave
    print("Mensagem Descriptada:", mensagem_descript)  # Exibe a mensagem descriptografada (original)
