using System;
using System.Collections.Generic;

class Program
{
    static List<int> SieveEratosthenes(int n)
    {
        var numbers = new List<int>();

        for (int i = 2; i < n; i++)
        {
            numbers.Add(i);
        }

        for (int i = 0; i < numbers.Count; i++)
        {
            for (int j = 2; j < n; j++)
            {

                numbers.Remove(numbers[i] * j);
            }
        }

        return numbers;
    }


    static void Main(string[] args)
    {
        Console.Write("N = ");
        int n = int.Parse(Console.ReadLine());
        var primeNumbers = SieveEratosthenes(n);
        Console.WriteLine("Простые числа до заданного {0}:", n);
        Console.WriteLine(string.Join(", ", primeNumbers));
        Console.ReadLine();
    }
}