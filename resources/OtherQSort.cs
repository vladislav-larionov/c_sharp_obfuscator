using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace qsort
{
    class OtherQSort
    {
        static int[] Sort(int[] arr, int l, int r)
        {
            //i и j нужны для цикла
            int i = l;
            int j = r;
            int x = arr[(l + r) / 2]; //Опорная
                                      //Цикл сортировка
            while (i <= j)
            {
                //Деление на меньше и больше опорного
                while (arr[i] < x) i++;
                while (arr[j] > x) j--;
                //Если i<=j:
                if (i <= j)
                {
                    //меняем значение элемонтов
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                    i++;
                    j--;
                }
            }
            //Рекурсия
            if (l < j) Sort(arr, l, j);
            if (i < r) Sort(arr, i, r);
            return arr;
        }
        static void Main(string[] args)
        {
            int[] arr = new int[] { 1, 50, 3, 5, -1, 100, -100, 1, 2, 1, 5555 };
            Console.WriteLine("массив: {0}", string.Join(", ", arr));
            Console.WriteLine("Упорядоченный массив: {0}", string.Join(", ", Sort(arr, 0, arr.Length - 1)));
            Console.ReadLine();
        }
    }
}
