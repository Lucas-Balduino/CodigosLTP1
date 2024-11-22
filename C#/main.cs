using System;

namespace App{

    class Program{

        public static void Main (string[] args){

        Carro carro = new Carro();
        carro1.marca = "Ford"
        carro1.modelo = "Ka"
        carro1.ano = 2024
        carro1.automatico = false

        Console.WriteLine($"Marca: {carro1.marca}, Modelo:{carro1.modelo}")
        carro1.Ligar();
        carro1.Acelerar(80);
        carro1.Desligar();
        carro1.cor = "Azul";
        Console.WriteLine(carro1.cor);
        }
    }
}