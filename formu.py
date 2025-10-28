import re
# Implementar computacionalmente em um linguagem de programação de alto nível, uma 
# aplicação para validar o preenchimento de um formulário feito por algum usuário. 
# Para isso você deverá utilizar a bilblioteca de expressões da linguagem de programação, 
# que em python é "import re". O formulário deverá conter os seguintes campos:

#Nome: no máximo 50 símbolos alfabéticos e espaço [a-zA-Z ].
#CPF: somente algarismos numéricos [0-9] ou algarismos no formato padrão do 
#CPF "000.000.000-00", ou seja, com ponto na posições 3 e 7 da string e hífen na posição 11. 
#E-mail: o nome de usuário deverá ter no mínimo 2 símbolos alfanuméricos, ponto, underline 
#ou hífen [\w\._-] seguido de '@', que por sua vez concatena com o domínio (utilizar a mesma 
#regra do nome do usuário). Para terminar, depois do domínio, deverá ter, obrigatoriamente, 
#um ponto seguido do tipo de registro, que é formado por três símbolos alfabéticos minúsculos 
#[a-z], e o código do país, que contempla: br, ao, pt, es, de, uk. Lembre-se que domínios 
#registrados nos EUA não têm código do país e também deve ser reconhecido. 
#Telefone: dois formatos possíveis, sendo o primeiro constituído por somente 11 números; e 
#o segundo pelo formato "(00)00000-0000".
#Além da validação dos campos do formulário, sua aplicação deverá varrer o texto abaixo e 
#extrair todos os e-mails válidos, ignorando os inválidos. Utilize a expressão regular 
#apresentada no item 3 para identificar os e-mails válidos. Texto para extração esta no arquivo texto.txt

def validar_nome(nome):
    padrao = r'^[a-zA-ZÀ-ú ]{1,50}$'
    return re.match(padrao, nome) is not None

def validar_cpf(cpf):
    padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    padrao_numerico = r'^\d{11}$'
    if re.match(padrao, cpf):
        return True
    return re.match(padrao_numerico, cpf) is not None

def validar_email(email):
    padrao = r'^[\w\._-]{2,}@[\w\._-]+\.[a-z]{2,3}(?:\.(?:br|ao|pt|es|de|uk))?$'
    return re.match(padrao, email) is not None

def validar_telefone(telefone):
    padrao1 = r'^\d{11}$'
    padrao2 = r'^\(\d{2}\)\d{5}-\d{4}$'
    return re.match(padrao1, telefone) is not None or re.match(padrao2, telefone) is not None

def extrair_emails(texto):
    padrao = r'[\w\._-]{2,}@[\w\._-]+\.[a-z]{2,3}(?:\.(?:br|ao|pt|es|de|uk))?'
    return re.findall(padrao, texto)

# Exemplo de uso
if __name__ == "__main__":
    nome = "João da Silva"
    cpf = "123.456.789-00"
    email = "joao.silva@example.com"
    telefone = "(12)34567-8901"
    texto = """Aqui estão alguns e-mails:
    joao.silva@example.com
    maria.santos@exemplo.com.br
    pedro.almeida@teste.com.pt
    email-invalido@.com
    """
    print(f"Nome válido: {validar_nome(nome)}")
    print(f"CPF válido: {validar_cpf(cpf)}")
    print(f"Email válido: {validar_email(email)}")
    print(f"Telefone válido: {validar_telefone(telefone)}")
    print(f"E-mails extraídos do texto: {extrair_emails(texto)}")

    try:
        with open('texto.txt', 'r', encoding='utf-8') as file:
            conteudo = file.read()
            emails_extraidos = extrair_emails(conteudo)
            print(f"E-mails extraídos do arquivo: {emails_extraidos}")
    except FileNotFoundError:
        print("Arquivo texto.txt não encontrado.")
