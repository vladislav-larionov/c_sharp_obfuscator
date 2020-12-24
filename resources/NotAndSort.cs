using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace qsort
{
    /*
     This class i
     */
    class NotAndSort
    {
        //метод для обмена элементов массива
        public static void Swap(ref int x, ref int y)
        {
            var t = x;
            x = y;
            y = t;
        }

        //метод возвращающий индекс опорного элемента
       public static int Partition(int[] array, int minIndex, int maxIndex)
        {
            var pivot = minIndex - 1;
            for (var i = minIndex; i < maxIndex; i++)
            {
                if (array[i] < array[maxIndex])
                {
                    pivot++; // Comment
                    Swap(ref array[pivot], ref array[i]);
                }
            }

            pivot++;
            Swap(ref array[pivot], ref array[maxIndex]);
            return pivot;
        }

        //быстрая сортировка
        public static int[] QuickSort(int[] array, int minIndex, int maxIndex)
        {
            if (minIndex >= maxIndex)
            {
                return array;
            }

            var pivotIndex = Partition(array, minIndex, maxIndex);
            QuickSort(array, minIndex, pivotIndex - 1);
            QuickSort(array, pivotIndex + 1, maxIndex);

            return array;
        }

        public static int[] QuickSort(int[] array)
        {
            return QuickSort(array, 0, array.Length - 1);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("QuickSort");
            //  var len = Convert.ToInt32(Console.ReadLine());
            // var a = new int[len];
            int[] arr = new int[] { 1, 50, 3, 5, -1, 100, -100, 1, 2, 1, 5555 };
            var len = arr.Length;

            Console.WriteLine("массив: {0}", string.Join(", ", arr));
            //for (var i = 0; i < arr.Length; ++i)
            // {
            //  Console.Write("a[{0}] = ", i);
            // }
            // arr[i] = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Упорядоченный массив: {0}", string.Join(", ", QuickSort(arr)));
            Console.WriteLine("NODModul: {0}", GetNODModul(15, 100));

            Console.ReadLine();
        }

        static int GetNODModul(int val1, int val2)
        {
            while ((val1 != 0) && (val2 != 0))
            {
                if (val1 > val2)
                    val1 %= val2;
                else
                    val2 %= val1;
            }
            return Math.Max(val1, val2);
        }
    }
}
