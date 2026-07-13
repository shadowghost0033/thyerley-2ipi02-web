#importação da biblioteca time para usar a função sleep

import time

#respostas corretas

senha = "123456" #a senha
nome = "Heitor" #o nome
comida = "pizza" #a comida favorita

#chat inicial

print("Olá, seja bem-vindo ao sistema de segurança do Yhosheph!")
print() #mensagem de boas vindas
time.sleep(2) #pausa de 2 segundos
print("para acessar o sistema, você precisa digitar a senha, o nome e a comida favorita do Heitor...") #mensagem de instrução
print()
time.sleep(3) #pausa de 3 segundos
print("pronto?") #mensagem de confirmação
print()
time.sleep(2) #pausa de 2 segundos
print("vamos lá então...") #mensagem de início
print()
time.sleep(3) #pausa de 3 segundos

print("carregando formulário...") #mensagem de carregamento
print()
time.sleep(4) #pausa de 4 segundos

#verificação

verificacao = input("digite a senha: ")
print()
while verificacao != senha: #enquanto a senha digitada for diferente da senha correta
    print("Poh cara... a senha tá logo alí...") #mensagem de erro
    print()
    verificacao = input("digite a senha certo dessa vez ok?: ")
    print() #solicita a senha novamente

#segunda verificação (de nome)
print("verificando...")
print()
time.sleep(2) #pausa de 2 segundos

verificacao_nome = input("ok man, agora digita o nome aí pfv: ") #solicita o nome
print()
while verificacao_nome != nome: #enquanto o nome digitado for diferente do nome correto
    print("amigo... colabora, não tenho o dia todo não...") #mensagem de erro
    print()
    verificacao_nome = input("digita o nome certo agora... ") #solicita o nome novamente
    print()

#terceira verificação (de comida favorita)
print("deixa eu ver...")
print()
time.sleep(2) #pausa de 2 segundos

verificacao_comida = input("ok,tamo quase lá... digita a comida favorita e acabamos: ") #solicita a comida favorita
print()
while verificacao_comida != comida: #enquanto a comida digitada for diferente da comida correta
    print("ah caraaa colabora aí man!!!! quero ir emboraa") #mensagem de erro
    print()
    verificacao_comida = input("ME POUPA E DIGITA ISSO CERTO: ") #solicita a comida novamente
    print()

print("validando...")
print()
time.sleep(2) #pausa de 2 segundo

print("aee agora sim... pode ir embora " + nome + ", valeu por colaborar!") #mensagem de sucesso