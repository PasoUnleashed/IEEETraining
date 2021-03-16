// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		in.nextLine();
		HashMap<String,Integer> occurence = new HashMap<String,Integer>();
		for(int i =0;i<n;i++){
		    String word = in.nextLine();
		    char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String anagram = new String(chars);
            if(occurence.containsKey(anagram)){
                occurence.put(anagram,occurence.get(anagram)+1);
            }else{
                occurence.put(anagram,1);
            }
		}
		System.out.println(Collections.max(occurence.values()));
		
	}
}