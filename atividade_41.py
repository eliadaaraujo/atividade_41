# Validação de Login com While
# Permita que o usuário tente fazer login até digitar a senha correta ("1234"). Mostre uma mensagem de erro a cada tentativa incorreta.

senha = str(input("Digite a senha: "))
while senha == "1234":
    print("Certo")
    break
else:
    print("Erro")