import re
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
