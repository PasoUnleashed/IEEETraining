// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner in = new Scanner(System.in);
	    String order = in.nextLine();
		int n = in.nextInt();
		ArrayList<String> words = new ArrayList<String>();
		in.nextLine();
		for(int i =0;i<n;i++){
		    words.add(in.nextLine());
		}
		Collections.sort(words,new Comparator<String>(){
		    @Override
            public int compare(String w1, String w2) {
                for(int i =0;i<Math.min(w1.length(),w2.length());i++){
                    char w1c = w1.charAt(i);
                    char w2c = w2.charAt(i);
                    int c1value = order.indexOf(Character.toLowerCase(w1c));
                    int c2value = order.indexOf(Character.toLowerCase(w2c));
                    if(Character.isUpperCase(w1c)){
                        c1value+=26;
                    }
                    if(Character.isUpperCase(w2c)){
                        c2value+=26;
                    }
                    int diff = c1value - c2value;
                    if(diff!=0){
                        return diff;
                    }
                }
                
                return w1.length()-w2.length();
            }
		});
		for(int i =0;i<words.size();i++){
            System.out.print(words.get(i).trim());	
            if(i<words.size()-1){
                System.out.print("\n");
            }
		}
	}
}