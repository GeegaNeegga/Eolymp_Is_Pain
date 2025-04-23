import java.util.*;

 

public class Main

{

  static Map<Long, Long> m = new HashMap<Long, Long>();

 

  public static long calc(long n, long p, long q)

  {

    if (m.containsKey(n)) return m.get(n);

    if (n == 0) return 1;

    long res = calc(n/p,p,q) + calc(n/q,p,q);

    m.put(n,res);

    return res;

  }

 

  public static void main(String[] args)

  {

    Scanner con = new Scanner(System.in);

    long n = con.nextLong(),

         p = con.nextLong(),

         q = con.nextLong();

    System.out.println(calc(n,p,q));

  }

}