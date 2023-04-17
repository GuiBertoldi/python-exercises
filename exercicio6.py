import random

comidas = ["Pizza", "Hambúrguer", "Sushi", "Massa", "Churrasco", "Tacos", "Risoto", "Ceviche", "Curry", "Feijoada", "Tempura", "Fondue", "Paella", "Ramen", "Bife"]

def gerar_senha():
    # Escolher um alimento aleatoriamente
    alimento = random.choice(comidas)
    
    # Gerar uma senha com letras minúsculas, maiúsculas, números e símbolos
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
    senha = ''.join(random.choice(caracteres) for _ in range(12))  # 12 caracteres de senha
    
    # Combinar o nome do alimento com a senha gerada
    senha = alimento + senha
    
    return senha

# Exemplo de uso
senha = gerar_senha()
print("Senha gerada:", senha)
