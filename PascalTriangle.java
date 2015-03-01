import java.util.Vector;
import java.io.*;
/**
* @author abdbaddude@gmail.com
*/

public class PascalTriangle{

	private static Vector<Integer> pascalTriangle = new Vector<>();
	private static Vector<Integer> pascalTriangles = new Vector<>();
	
	/**
	* @description Combonaction using  Iterative Algorith approach to solve C(n,k)
	* C(n,k) = n!/(k!)(n-k)! = (n/1)*(n-1)/2*(n-2)/3*(n-k+1)/k
	* @param n int
	* @param k int
	* @return combination
	* Iterative implementation for solving combination 
	* C(n,k) = n!/(k!)(n-k)! = (n/1)*(n-1)/2*(n-2)/3*(n-k+1)/k
	*/	
	public static int iterativeCombination(int n , int k ){
		if ( n<2 || k==0 || k == n ) return 1;
		int coefficient = 1;
		for (int j = 1; j <= k ; j++){
			coefficient = coefficient *  (n-j+1)/j;
		}
		return coefficient;
	}
	
	public static void doPascalTriangles(int depth) {
		for (int i= 0 ; i  <= depth ; i++){
			for (int k= 0 ; k  <= i ; k++)
				pascalTriangle.add(iterativeCombination(i,k));
		}
		pascalTriangles.addAll(pascalTriangle);
		for (int coefficient = 0 ; coefficient < pascalTriangles.size()  ; coefficient++ )
			System.out.printf("%d ",pascalTriangles.get(coefficient));
		System.out.println("");	
	}
	
	public static void main(String[] args) throws FileNotFoundException,IOException{
		File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        int test_case_nr = 0;
        int MAX_TEST_CASES = 40;
        while ((line = buffer.readLine()) != null) {    	
            line = line.trim();
            if(!line.isEmpty()  && !line.equals("") && !line.equals("\n") ){
            	if(test_case_nr++ >= MAX_TEST_CASES ) break; //Test Cases must be less than MAX_TEST_CASES
            	doPascalTriangles(Integer.parseInt(line));
            }
        }	
        System.exit(1);			
	}
}