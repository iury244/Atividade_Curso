class Calculadora:
    def __init__(self):
        while True:
            escolha = int(input("Digite uma das opçães:\n"
                                "1 - Soma\n"
                                "2 - subtracao\n"
                                "3 - Sair\n"))
            match escolha:
                case 1:
                    self.soma()
                case 2:
                    self.subtracao() 
                case 3:
                    print("Saindo...")
                    break                       
                case _:
                    print("Opção inválida")

    def soma(self):
        num1 = int(input("Digite o primeiro valor: "))
        num2 = int(input("Digite o segundo valor: "))

        print(f"o valor da soma é {num1 + num2}")

    def subtracao(self):
        num1 = int(input("Digite o primeiro valor: "))
        num2 = int(input("Digite o segundo valor: "))

        print(f"O valor da subtração é {num1 - num2}")

    
Calculadora = Calculadora()