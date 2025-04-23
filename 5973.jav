import java.util.*;

 

public class Main

{

  public static void main(String[] args)

  {

    long res[] = new long[91];

    res[1] = 1; res[2] = 2;

    for(int i = 3; i < 91; i++)

      res[i] = res[i-1] + res[i-2] + 1;

 

    Scanner con = new Scanner(System.in);   

    int n = con.nextInt();

    System.out.println(res[n]);

    con.close();

  }

}   