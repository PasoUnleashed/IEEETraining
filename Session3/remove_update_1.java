// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
    static int max(int[] x){
        int ret = x[0];
        for(int i=0;i<x.length;i++){
            ret= Math.max(ret,x[i]);
        }
        return ret;
        
    }
    static class Update{
        int l,r,x;
        public Update(int l,int r,int x){
            this.l=l;
            this.r=r;
            this.x=x;
        }
        public void add(int[] a){
            for(int i=l-1;i<r;i++){
                a[i]+=x;
            }
        }
        public void subtract(int[] a){
            for(int i=l-1;i<r;i++){
                a[i]-=x;
            }
        }
    }
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int q = in.nextInt();
		int[] values = new int[n];
		Update[] updates = new Update[q];
		for(int i=0;i<q;i++){
		    updates[i] = new Update(in.nextInt(),in.nextInt(),in.nextInt());
		    updates[i].add(values);
		}
		int min = 1000000001;
		for(int i=0;i<q;i++){
		    updates[i].subtract(values);
		    min = Math.min(min,max(values));
		    updates[i].add(values);
		}
		System.out.println(min);
		
	}
}   