using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace first_blood
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Введите число!");
            string x1 = Console.ReadLine();
            long a = Convert.ToInt64(x1);
            switch (a)
            {
                case 1:
                    Console.WriteLine("Eto 1");
                    break;
                case 2:
                    Console.WriteLine("Eto 2");
                    break;
                case 123:
                    Console.WriteLine("LOOOOH");
                    string result = a > 100 ? "Bolshe 100" : "Menshe 100";
                    Console.WriteLine(result);
                    break;
                default:
                    Console.WriteLine("Eto ne 1 ili 2");
                    goto case 123;
                    }
            Console.WriteLine("FIN");
        }
    }
}
