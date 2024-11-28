import tkinter as tk
from tkinter import ttk

# Classe da lógica da calculadora
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
            return "Erro: Divisão por zero"
        return self.resultado


# Classe da interface gráfica
class CalculadoraGUI:
    def __init__(self, master):
        self.master = master
        self.calculadora = Calculadora()

        # Estilo para botões e widgets
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 14), padding=10)
        self.style.configure("TLabel", background="#f7f9fc", font=("Arial", 16), anchor="center")

        # Rótulo para mostrar o resultado
        self.resultado_label = ttk.Label(master, text="Resultado: 0", font=("Arial", 18, "bold"))
        self.resultado_label.pack(pady=20)

        # Campo de entrada
        self.entrada = ttk.Entry(master, font=("Arial", 14), justify="center")
        self.entrada.pack(pady=10, ipadx=5, ipady=5)

        # Frame para organizar os botões
        self.botao_frame = tk.Frame(master, bg="#f7f9fc")
        self.botao_frame.pack(pady=20)

        # Botões de operações
        self._criar_botoes()

    def _criar_botoes(self):
        # Botões organizados em uma grade
        botoes = [
            ("1", lambda: self.numero(1)),
            ("2", lambda: self.numero(2)),
            ("3", lambda: self.numero(3)),
            ("4", lambda: self.numero(4)),
            ("6", lambda: self.numero(6)),
            ("5", lambda: self.numero(5)),
            ("7", lambda: self.numero(7)),
            ("8", lambda: self.numero(8)),
            ("9", lambda: self.numero(9)),
            ("+", self.adicionar),
            ("0", lambda: self.numero(0)),
            ("-", self.subtrair),
            ("*", self.multiplicar),
            ("/", self.dividir),
            ("=", self.igual),
            ("Zerar", self.zerar),
            ("Sinal", self.mudarSinal)
        ]

        for i, (texto, comando) in enumerate(botoes):
            botao = ttk.Button(self.botao_frame, text=texto, command=comando)
            botao.grid(row=i // 3, column=i % 3, padx=1, pady=1, ipadx=1, ipady=1)

    def numero(self,numero):
        self.entrada.insert(tk.END, str(numero))

    def igual(self):
        self._atualizar_resultado

    # Métodos para as operações
    def zerar (self):
        self.calculadora.resultado = 0
        self._atualizar_resultado()
        self._limpar_entrada()

    def mudarSinal(self):
        self.calculadora.resultado *= -1
        self._atualizar_resultado()
        self._limpar_entrada()

    def adicionar(self):
        self._executar_operacao(self.calculadora.adicionar)
        self._limpar_entrada()

    def subtrair(self):
        self._executar_operacao(self.calculadora.subtrair)
        self._limpar_entrada()

    def multiplicar(self):
        self._executar_operacao(self.calculadora.multiplicar)
        self._limpar_entrada()

    def dividir(self):
        resultado = self._executar_operacao(self.calculadora.dividir)
        if resultado == "Erro: Divisão por zero":
            self.resultado_label.config(text="Erro: Divisão por zero")
        self._limpar_entrada()

    # Função auxiliar para executar operações
    def _executar_operacao(self, operacao):
        valor = self._get_valor_entrada()
        if valor is not None:
            resultado = operacao(valor)
            self._atualizar_resultado()
            return resultado

    # Função auxiliar para obter o valor de entrada
    def _get_valor_entrada(self):
        try:
            return float(self.entrada.get())
        except ValueError:
            self.resultado_label.config(text="Erro: Entrada inválida")
            return None

    def _limpar_entrada(self):
        self.entrada.delete(0, tk.END)

    # Função auxiliar para atualizar o rótulo de resultado
    def _atualizar_resultado(self):
        self.resultado_label.config(text=f"Resultado: {self.calculadora.resultado}")


# Inicializando a
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.title("Calculadora Avançada")
    root.geometry("500x600")
    root.configure(bg="#f7f9fc")
    root.mainloop()