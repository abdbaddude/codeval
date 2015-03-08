
public class SieveEratosthenes
{
	private static final int SIZE = 10000;
	private static boolean[] sieve = new boolean[SIZE];
	public static void main(String[] args)
	{
		initializeSieve();
		printSieve();
	}
	
	private static void initializeSieve()
	{
		for(int i = 2 ; i < SIZE ; i++)
			sieve[i] = true;
		for(int n=2 ; 2*n < SIZE; n++)
			if(sieve[n])
				for (int m = n ; m * n < SIZE ; m++)
					sieve[m*n] = false;
	}
	
	private static void printSieve()
	{
		int n = 0;
		for (int i=0; i < SIZE ; i++)
			if(sieve[i]) System.out.print((n++%10==0?"\n":"\t") + i);
		System.out.println("\n" + n + " primes less than " + SIZE); 
	}
}