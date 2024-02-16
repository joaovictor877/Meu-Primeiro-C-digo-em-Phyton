
    using System;

namespace MeuAppConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Bem-vindo ao Meu App Console!");
            
            // Solicita o nome do usuário
            Console.Write("Digite seu nome: ");
            string nome = Console.ReadLine();

            // Sauda o usuário
            Console.WriteLine($"Olá, {nome}! Bem-vindo ao mundo do C#.");

            // Aguarda a entrada do usuário antes de fechar
            Console.WriteLine("Pressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}

