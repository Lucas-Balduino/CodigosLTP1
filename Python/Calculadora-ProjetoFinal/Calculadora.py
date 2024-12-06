import tkinter as tk
from tkinter import ttk

# Classe da lógica da calculadora
class Calculadora:
    def __init__(self):
        self.resultado = 0
        self.operacao = None  # Adicionei essa "operacao" que vai armazenar a operação atual

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

    def definir_operacao(self, operacao):  # método define a operação q vai acontecer
        self.operacao = operacao

    def executar_operacao(self, valor):  #executar  operação q ta armazenada
        if self.operacao:
            return self.operacao(valor)
        return self.resultado


# Classe da interface gráfica
class CalculadoraGUI:
    def __init__(self, master):
        self.master = master
        self.calculadora = Calculadora()

        # Configuração da janela
        self.master.title("Calculadora :)")
        self.master.geometry("350x500")
        self.master.configure(bg="#dce7f3")

        # Estilo
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 14), padding=10)
        self.style.configure("TLabel", background="#dce7f3", font=("Arial", 16), anchor="center")

        # Rótulo para exibir apenas o valor
        self.resultado_label = tk.Label(master, text="", font=("Arial", 20, "bold"), bg="#dce7f3", fg="#34495e")
        self.resultado_label.pack(pady=20)

        # Campo de entrada
        self.entrada = ttk.Entry(master, font=("Arial", 14), justify="center")
        self.entrada.pack(pady=10, ipadx=5, ipady=5)

        # Frame para organizar os botões
        self.botao_frame = tk.Frame(master, bg="#dce7f3")
        self.botao_frame.pack(pady=20)

        # Criar botões
        self._criar_botoes()

    def _criar_botoes(self):
        botoes = [
            ("7", lambda: self.numero(7)),
            ("8", lambda: self.numero(8)),
            ("9", lambda: self.numero(9)),
            ("/", lambda: self.definir_operacao(self.calculadora.dividir)),
            ("4", lambda: self.numero(4)),
            ("5", lambda: self.numero(5)),
            ("6", lambda: self.numero(6)),
            ("*", lambda: self.definir_operacao(self.calculadora.multiplicar)),
            ("1", lambda: self.numero(1)),
            ("2", lambda: self.numero(2)),
            ("3", lambda: self.numero(3)),
            ("-", lambda: self.definir_operacao(self.calculadora.subtrair)),
            ("0", lambda: self.numero(0)),
            ("C", self.zerar),
            ("=", self.igual),
            ("+", lambda: self.definir_operacao(self.calculadora.adicionar)),
        ]

        for i, (texto, comando) in enumerate(botoes):
            botao = tk.Button(self.botao_frame, text=texto, command=comando, font=("Arial", 14),
                              bg="#f7f9fc", fg="#34495e", activebackground="#e0f7fa", activeforeground="#34495e",
                              relief="flat", bd=0)
            botao.grid(row=i // 4, column=i % 4, padx=5, pady=5, ipadx=10, ipady=10)

            # Efeito hover
            botao.bind("<Enter>", lambda e, b=botao: b.config(bg="#d6eaf8"))
            botao.bind("<Leave>", lambda e, b=botao: b.config(bg="#f7f9fc"))

    def numero(self, numero):
        self.entrada.insert(tk.END, str(numero))

    def igual(self):
        valor = self._get_valor_entrada()
        if valor is not None:
            resultado = self.calculadora.executar_operacao(valor)
            self.entrada.delete(0, tk.END)
            if resultado == "Erro: Divisão por zero":
                self.entrada.insert(0, "Erro: Divisão por zero")
                self.entrada.config(fg="red")
            else:
                self.entrada.insert(0, str(resultado))
                self.entrada.config(fg="#34495e")

    def definir_operacao(self, operacao):
        valor = self._get_valor_entrada()
        if valor is not None:
            self.calculadora.resultado = valor
            self.calculadora.definir_operacao(operacao)
            self._limpar_entrada()

    def zerar(self):
        self.calculadora.resultado = 0
        self.calculadora.operacao = None  # Limpei a operação qnd zerar a calculadora
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, "0")
        self.entrada.config(fg="#34495e")

    def _get_valor_entrada(self):
        try:
            return float(self.entrada.get())
        except ValueError:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, "Erro: Entrada inválida")
            self.entrada.config(fg="red")
            return None

    def _limpar_entrada(self):
        self.entrada.delete(0, tk.END)

    def _atualizar_resultado(self):
        self.resultado_label.config(text=f"Resultado: {self.calculadora.resultado}")


# Inicializando a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()