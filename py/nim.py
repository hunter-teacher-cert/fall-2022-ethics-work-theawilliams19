# FILENAME: nim.py
# First Last: Théa Williams
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: thinkcspy text, Datacamp Intro to Python course


import java.io.*;
import java.util.*;
import java.util.Random.*;

public class Nim{

  public static void main(String [] args){
    int stones = 12;
    int userStonesTaken;//stones taken by user
  

    Scanner input = new Scanner(System.in);
    //Include a welcome message with name       of game and object and rules.
    
    //loop until game ends
    while(stones>0){
      
      //prompt for use input (user turn - a       move = taking 1-3 stones
      
      System.out.println ("Your turn, pick between 1 and 3 stones to remove.");
      userStonesTaken = input.nextInt();

      //calculate number of stones                remaining, print
      
        stones -= userStonesTaken;
       //the above is a shortcut - it is the same as - "stones = stones - userStonesTaken"
      System.out.println ("You have selected " + userStonesTaken);
      System.out.println ("There are " + stones + " remaining. ");
        
      //check for win
      if (stones==0){
        System.out.println ("You win!");
        break;
      }

      //machine turn
      Random random = new Random();
      int machineStonesTaken = random.nextInt(2)+1;
      System.out.println("The computer has chosen " + machineStonesTaken);
      
      //calculate number of stones remaining,          print
      stones -= machineStonesTaken;
      System.out.println ("There are " + stones + " remaining. ");
      
      //check win
      if (stones==0){
        System.out.println ("Computer Wins! Sorry, better luck next time. :(");
      }
    }

    
  }
  
}