import java.util.*;

 

public class Main

{

  static int MAX = 5000000;

  static long m[] = new long[MAX];

 

  public static long f(long n, long p, long q, long x, long y)

  {

    if (n <= 0) return 1;    

    if (n < MAX && m[(int)n] > 0) return m[(int)n];

   

    long temp = f(n/p-x,p,q,x,y) + f(n/q-y,p,q,x,y);

    if (n < MAX) m[(int)n] = temp;

 

    return temp;   

  }

 

  public static void main(String[] args)

  {

    Scanner con = new Scanner(System.in);

   

    long n = con.nextLong();

    long p = con.nextLong();

    long q = con.nextLong();

    long x = con.nextLong();

    long y = con.nextLong();

   

    long res = f(n,p,q,x,y);

    System.out.println(res);

    con.close();

  }

}