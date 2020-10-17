// Don't place your source in a package
// https://csacademy.com/contest/archive/task/word_permutation/
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
    static class Entry implements Comparable<Entry>{
        String word;
        int index;
        public Entry(String word,int index){
            this.word= word;
            this.index = index;
        }
        @Override
        public int compareTo(Entry o){
            return word.compareTo(o.word);   
        }
    }
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		Entry[] words = new Entry[n];
		for(int i =0;i<n;i++){
		    words[i] = new Entry(in.next(),i+1);
		}
		Arrays.sort(words);
		String f = "";
		for(int i =0;i<n;i++){
		    System.out.print(Integer.toString(words[i].index));
		    if(i<n-1){
		        System.out.print(" ");
		    }
		}
		System.out.print("\n");
	}
}