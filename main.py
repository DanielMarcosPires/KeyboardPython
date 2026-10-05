import datetime
import time
import keyboard
import os

class profile:
    gastos = ()
    def __init__(self):
        self.name = ""
        self.salario = 0
        
    getterSalario = property(lambda self: self.salario)
    getterName = property(lambda self: self.name)
    
    def setName(self, name):
        input("pressione Enter para começar a alterar o nome...")
        self.name = input("Digite o nome: ")
        print(f"Nome alterado para: {self.name} - Pressione 'i' para voltar")
    
    def setSalario(self):
        input("pressione Enter para começar a alterar o salário...")
        self.salario = inputGastos("Digite o valor do salário: ")
        print(f"Salário alterado para: {self.salario:.2f}R$ - Pressione 'i' para voltar")    

    def addGasto(self):
        input("pressione Enter para começar a adicionar um gasto...")
        gasto = inputGastos("Digite o valor do gasto: ")
        
        print(f"Gasto adicionado: {gasto:.2f}R$ - Pressione 'i' para voltar")
        self.gastos = self.gastos + (gasto,)
    
    def listGastos(self):
        print(f"Gastos: {self.gastos}")
        
    def totalGastos(self):
        return sum(self.gastos)
    
    def receitaLiquida(self):
        return self.salario - self.totalGastos()

hourInitialized = datetime.datetime.now().strftime("%H:%M %p")
dateInitialized = datetime.datetime.now().strftime("%d/%m/%Y")
profile_instance = profile()


def inputGastos(placeholder):
    time.sleep(0.5)
    while True:
        valor = input(placeholder)
        try:
            gasto = float(valor.replace(',', '.'))
            if gasto <= 0:
                raise ValueError
            return gasto
        except ValueError:
            print("Valor inválido! Digite um valor em real.")

def systemInfo():
    os.system('cls')
    print(f"Horário de Inicialização: [{hourInitialized}]")
    print(f"Data: [{dateInitialized}]")
    print(f"Nome: [{profile_instance.getterName}]")
    print(f"Salário: [{profile_instance.getterSalario:.2f}R$]\n")
    
    print('=' * 50)
    print(f"Total de Gastos: [{profile_instance.totalGastos():.2f}R$]")
    print(f"Receita Líquida: [{profile_instance.receitaLiquida():.2f}R$]")
    print('=' * 50+'\n')
    
    time.sleep(1)
            
    print("Teclado ativado! \n")
        
    print(f"Pressione 'a' para inserir um gasto.")
    print(f"Pressione 'e' para alterar o salário.")
    print(f"Pressione 'n' para alterar o nome.")
    print(f"Pressione 'enter' para ver suas informações.")
    
    

def keyboardControl(addGasto,info,updateName,updateSalario):
    while True:
        keyboard.add_hotkey(
            f'{addGasto}', 
            lambda: profile_instance.addGasto(),
        )
        keyboard.add_hotkey(
            f'{updateSalario}', 
            lambda: profile_instance.setSalario(),
        )
        keyboard.add_hotkey(
            f'{updateName}', 
            lambda: profile_instance.setName(),
        )
        keyboard.add_hotkey(
            'enter', 
            lambda: systemInfo()
        )

if __name__ == "__main__":
        print("*" * 50)
        systemInfo()
        
        keyboardControl(
            addGasto='a',
            info='w',
            updateName='n',
            updateSalario='e',
        )
        print("* " * 50)