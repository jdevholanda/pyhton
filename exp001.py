altura = float(input("Qual sua altura ? "))
peso = float(input("Qual seu peso:  "))

x = altura * altura
y = peso 

imc = y / x

if imc >= 40:
    print("__________________")
    print("O seu IMC é de: ", imc )

    print("Obesidade Grau III")
    print("__________________")

elif imc < 40 and imc  >= 35:
    print("__________________")
    print("O seu IMC é de: ", imc )

    print("Obesidade Grau II")
    print("__________________")

elif imc >= 30 and imc <= 34.9: 
    print("__________________")
    print("O seu IMC é de: ", imc )

    print("Obesidade Grau I")
    print("__________________")

elif imc >= 18.5 and imc <= 24.9:
    print("__________________")
    print("O seu IMC é de: ", imc )

    print("Peso normal")
    print("__________________")

else: 
    print("O seu IMC é de: ", imc)

    print("Você está abaixo da média de IMC! )")



