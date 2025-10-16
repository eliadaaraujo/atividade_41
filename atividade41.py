# Validação de Login com While
# Permita que o usuário tente fazer login até digitar a senha correta ("1234").
#  Mostre uma mensagem de erro a cada tentativa incorreta.


senha_correta = "1234"
usuario = str(input("Digite a senha: "))

while usuario != senha_correta:
    print("Erro!")
    usuario = (input("Digite a senha novamente: "))

else:
    print("Senha aceita!")