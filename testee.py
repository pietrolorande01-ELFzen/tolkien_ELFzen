
print("vamos aqui resolver os testes do professsor =) ")

nome = input("\n\n\nPor favor digite seu nome : ")
print()

dia = int(input("Por favor digite o dia de seu nascimento : "))
mes = int(input("por favor digite o mes de seu aniversário : "))
ano = int(input("por favor digite o ano de seu aniversário: "))
print()

ano_formatado = ( 2026 - ano)

print(f"Seu nome é {nome}")
print()
print(f"sua data de nascimento é : {dia}/{mes}/{ano} ")
print(f"de acordo com o ano indicado acima a sua idade se estima em {ano_formatado}")


print("calculo da área de um círculo")

raio = 5 
valo_raio = (3.14159 * raio**2)
print( f"O valor de área de um circulo com o raio {raio}, é de :{valo_raio} ")
print()
print()

print("termometro de farenheit para celcius ")

farenheit = float(input("Por favor digite um valor que queira transformar em celcius : "))
conta = (farenheit - 32) * 5 / 9 

print(f"O seu valor digitado foi {farenheit}, este valor em celcius equivale a :  {conta:.2f}")
print()
print()

print("Vamos traduzir um valor de celcius para farenheit ")

celcius = float(input("Por favor digite um número para transformar em farenheit : "))
conta_dois = (celcius * 1.8 ) + 32 

print(f"O valor que foi inserido em celcius equivale em farenheit a : {conta_dois:.2f}")

