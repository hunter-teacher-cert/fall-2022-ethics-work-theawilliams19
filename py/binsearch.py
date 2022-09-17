# FILENAME: binsearch.py
# First Last: Théa Williams
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: thinkcspy text, Datacamp Intro to Python course

import py.io.*;
import py.util.*;

public class SortSearchDriver {
    public static void main(String[] args) {


	// Uncomment these to test part 1
	
	SortSearch ss = new SortSearch(20);
	System.out.println(ss);
	
		
	// // Uncomment these to test part 2

	int i;
	i = ss.findSmallestIndex(0);
  System.out.println("\nPrint results when started at index 0 in the array:\nss[smallestIndex] = value : data");
  System.out.println("--------------------------------");
	System.out.println("ss["+ i +"] = "+ss.get(i)+" : " + ss);

	i = ss.findSmallestIndex(10);
  System.out.println("\nPrint results when started at index 3 in the array:\nss[smallestIndex] = value : data");
   System.out.println("--------------------------------");
	 System.out.println("ss["+ i + "] = "+ss.get(i)+" : " + ss);
	
	// // Uncomment these to test part 3
  System.out.println("\n----------------Print array----------------");
	System.out.println(ss);
  System.out.println("\n-------------Print sorted array-------------");
  
  long start,elapsed; // "long" is like a long int. int go to 16 digits and "long"'s go to 32 digits.

	start = System.currentTimeMillis(); //We are setting/initializing the "start" variable to the current time. This method is build into the System class library.
	ss.sort();//calling the sort method

	elapsed = System.currentTimeMillis() - start;//setting/initializing the "elapsed" variable to the current time - the time now, which is equal to the elapsed time.
	System.out.println("-> Size: 15, Time: " + elapsed);//prints out the size of the array and the time elapsed
	System.out.println(ss);
	
  System.out.println("\n-------------LinearSearch Method Test -------------");
  System.out.println(ss.linearSearch(0));
  System.out.println(ss.linearSearch(10));
  System.out.println(ss.linearSearch(21));

  System.out.println("\n-------------BinarySearch Method Test -------------");
  System.out.println(ss.binarySearch(0));
  System.out.println(ss.binarySearch(10));
  System.out.println(ss.binarySearch(21));
  
  int size = 15;
  System.out.println("\n--------------Binary Search Recursive Method Test--------------");
  System.out.println(ss);
  System.out.print("Index of 0: ");
  System.out.println(ss.binarySearchRecursive(0, 0, size-1));
  System.out.print("Index of 10: ");
  System.out.println(ss.binarySearchRecursive(10, 0, size-1));
  System.out.print("Index of 21: ");
	System.out.println(ss.binarySearchRecursive(21, 0, size-1));

  System.out.println("\n--------------Speed test sort Test--------------");
  size = 1000;
  ss = new SortSearch(size);
  start = System.currentTimeMillis(); 
	ss.sort();
	elapsed = System.currentTimeMillis() - start;
	System.out.println("-> Size: " + size + ",  Time: " + elapsed);//prints out the size of the array and the time elapsed

  size = 10000;
  ss = new SortSearch(size);
  start = System.currentTimeMillis(); 
	ss.sort();
	elapsed = System.currentTimeMillis() - start;
	System.out.println("-> Size: " + size + ",  Time: " + elapsed);//prints out the size of the array and the time elapsed

  size = 50000;
  ss = new SortSearch(size);
  start = System.currentTimeMillis(); 
	ss.sort();
	elapsed = System.currentTimeMillis() - start;
	System.out.println("-> Size: " + size + ",  Time: " + elapsed);//prints out the size of the array and the time elapsed

  System.out.println();
  SortSearch test = new SortSearch(size);
  System.out.println("50k, 100k, 500k, 1m, 5m search testing 0, mid, size");
  System.out.println("\n------------------speed test - 50k------------------");   
  int mid = size / 2;
  start = System.currentTimeMillis(); 
  test.linearSearch(0);
  test.linearSearch(mid);
  test.linearSearch(size-1);
	elapsed = System.currentTimeMillis() - start;
  System.out.print("Linear search: ");
  System.out.println("Time to execute test with of size " + size + ": " + elapsed + " ms");
  mid = size / 2;
  start = System.currentTimeMillis(); 
  test.binarySearch(0);
  test.binarySearch(mid);
  test.binarySearch(size-1);
	elapsed = System.currentTimeMillis() - start; 
  System.out.print("Binary search: ");    
  System.out.println("Time to execute test with of size " + size + ": " + elapsed + " ms"); 
  start = System.currentTimeMillis(); 
  test.binarySearchRecursive(0, 0, size-1);
  test.binarySearchRecursive(mid, 0, size-1);
  test.binarySearchRecursive(size-1, 0, size-1);
	elapsed = System.currentTimeMillis() - start;
  System.out.print("Rec Binary search: ");    
  System.out.println("Time to execute test with of size " + size + ": " + elapsed + " ms"); 
  
  System.out.println("\n------------------speed test - 100k------------------");   
      
  size = 100000; // CHANGE THIS AFTER COPY FOR BIGGER TEST
  test = new SortSearch(size); // update to the new size
  mid = size /2; // update the new mid
  start = System.currentTimeMillis(); 
  test.linearSearch(0);
  test.linearSearch(mid);
  test.linearSearch(size-1);
	elapsed = System.currentTimeMillis() - start;
  System.out.print("Linear search: ");
  System.out.println("Time to execute test with of size " + size + ": " + elapsed + " ms");
  mid = size / 2;
  start = System.currentTimeMillis(); 
  test.binarySearch(0);
  test.binarySearch(mid);
  test.binarySearch(size-1);
	elapsed = System.currentTimeMillis() - start; 
  System.out.print("Binary search: ");    
  System.out.println("Time to execute test with of size " + size + ": " + elapsed + " ms"); 
  start = System.currentTimeMillis(); 
  test.binarySearchRecursive(0, 0, size-1);
  test.binarySearchRecursive(mid, 0, size-1);
  test.binarySearchRecursive(size-1, 0, size-1);
	elapsed = System.currentTimeMillis() - start;
  System.out.print("Rec Binary search: ");    
  System.out.println("Time to execute test with of size " + size + ": " + elapsed + " ms"); 


    System.out.println("\n------------------buildIncreasingArrayList Test-----------------");  
    ArrayList<Integer> a= ss.buildIncreasingList(20);
	System.out.println(a);

  System.out.println("\n------------------list1-----------------");  
  ArrayList<Integer> list1= ss.buildIncreasingList(5);
	System.out.println(list1);

  // build a second Arralist here

  System.out.println("\n------------------list2-----------------");  
  ArrayList<Integer> list2= ss.buildIncreasingList(5);
	System.out.println(list2);

  // test your merge routine here
  System.out.println("\n------------------mergeList test-----------------");  
    ArrayList<Integer> mergeList= ss.merge(list1,list2);
	System.out.println(mergeList);

	
  //test your mergeSort here
  System.out.println("\n------------------mergeSort Test-----------------");
      size = 10; // CHANGE THIS AFTER COPY FOR BIGGER TEST
      SortSearch mergeSS = new SortSearch(size); // update to the new size
      mergeSS.msort();
      System.out.println(mergeSS);
        
     }//ends main method

  
}//ends driver class