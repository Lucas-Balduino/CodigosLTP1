namespace App{
    class Carro{
        public string marca;
        public string modelo;
        private int ano;
        public bool automatico = false;
        private string cor;

        public string GetCor(){
            get{return cor;}
            set{cor = value;}
        }

        public int GetAno(){
            return ano;
        }

        public void SetAno(int ano){
            ano = novoAno;
        }

        public void Ligar(){
            Console.WriteLine("O carro esta ligado!")
        }

        public void Acelerar(float velocidade){
            Console.WriteLine($"O carro esta acelerando a {velocidade} km/h!")
        }

        public void Desligar(){
            Console.WriteLine("O carro esta desligado!")
        }


    }
}