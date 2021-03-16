// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.*;
// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		HashMap<String, Integer> occur = new HashMap<String,Integer>();
		for(int i =0;i<n;i++){
		    char tempArray[] = in.next().toCharArray(); 
            
            Arrays.sort(tempArray); 
            String sorted = new String(tempArray);
            if(occur.containsKey(sorted)){
                occur.put(sorted,occur.get(sorted)+1);
            }else{
                occur.put(sorted,1);   
            }
		}
		System.out.println(Collections.max(occur.values()));
	}
}