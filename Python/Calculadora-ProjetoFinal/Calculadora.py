import math
import tkinter as tk

class Calculadora:
    def __init__(self):
        self.resultado = 0

    def adicionar(self, valor):
        self.resultado += valor
        return self.resultado

    def subtrair(self, valor):
        self.resultado -= valor
        return self.resultado

    def multiplicar(self, valor):
        self.resultado *= valor
        return self.resultado

    def dividir(self, valor):
        if valor != 0:  
            self.resultado /= valor
        else:
            return "Erro, Divisão por 0"
        return self.resultado
    
    def raiz(self, valor, indice):
        self.resultado = math.pow(valor, 1/(indice))
        return self.resultado
    
    def potencia(self, valor, indice):
        self.resultado = 1
        for i in range(indice):
            self.resultado *= valor
        #self.resultado = math.pow(valor, indice)
        return self.resultado


class CalculadoraGUI:
    def __init__(self, janela):
        self.janela = janela
        
        self.calculadora = Calculadora()

        # Adicionar widgets (botões, entradas, etc.)
        self.resultado_label = tk.Label(janela, text="Resultado:")
        self.resultado_label.pack()

        self.entrada = tk.Entry(janela)
        self.entrada.pack()

        # Botões para operações
        self.botao_adicionar = tk.Button(janela, text="+",font=("Arial",12), width= 5,height=2,command=self.adicionar)
        self.botao_adicionar.pack()

        self.botao_subtrair = tk.Button(janela, text="-", font=("Arial",12), width= 5,height=2,command=self.subtrair)
        self.botao_subtrair.pack()
        
        self.botao_multiplicar = tk.Button(janela, text="x",font=("Arial",12), width= 5,height=2,command=self.multiplicar)
        self.botao_multiplicar.pack()

        self.botao_dividir = tk.Button(janela, text="/", font=("Arial",12), width= 5,height=2,command=self.dividir)
        self.botao_dividir.pack()

        # Continue adicionando botões para multiplicar e dividir

    def adicionar(self):
        valor = float(self.entrada.get())
        self.calculadora.adicionar(valor)
        self.atualizar_resultado()
            
    def subtrair(self):
        valor = float(self.entrada.get())
        self.calculadora.subtrair(valor)
        self.atualizar_resultado()
    
    def multiplicar(self):
        valor = float(self.entrada.get())
        self.calculadora.multiplicar(valor)
        self.atualizar_resultado()
    
    def dividir(self):
        valor = float(self.entrada.get())
        self.calculadora.dividir(valor)
        self.atualizar_resultado()
            
    def atualizar_resultado(self):
        self.resultado_label.config(text="Resultado: " + str(self.calculadora.resultado))

if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Super Calculadora")
    janela.geometry("400x400")
    janela.configure(background="#f0f0f0")
    calculadora = Calculadora()
    app = CalculadoraGUI(janela)
    janela.mainloop()

