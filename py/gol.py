# FILENAME: nim.py
# First Last: Théa Williams
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: thinkcspy text, Datacamp Intro to Python course

import java.io.*;
import java.util.*;

/**
 * Conway's Game of Life by Team 
 * Collaborators: Théa Williams, Ed Hawkins, Joel Bianchi
 */

/**
   The Rules of Life:
   Survivals:
   * A living cell with 2 or 3 living neighbours will survive for the next generation.
   Deaths:
   * Each cell with >3 neighbours will die from overpopulation.
   * Every cell with <2 neighbours will die from isolation.
   Births:
   * Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive in next generation.
   NOTA BENE:  All births and deaths occur simultaneously. Together, they constitute a single generation.
*/

public class Cgol
{

  //create, initialize, and return  empty board (all cells dead)
  public static char[][] createNewBoard( int rows, int cols )
  {
    //construct a new char 2D array
    char[][] board = new char[rows][cols];

    //traverse through the entire 2D array
    for (int r = 0; r<board.length; r++)
    {
      for (int c = 0; c<board[0].length; c++)
      {
        //Assign a dot to the dead cells
        board[r][c] = '.';
      }
    }
    
    //return the 2D array
    return board;
  }


  //print the board to the terminal
  public static void printBoard( char[][] board )
  {
    //traverse through entire array
    for (int r = 0; r<board.length; r++)
    {
      for (int c = 0; c<board[0].length; c++)
      {
        //print out each cell's char
        System.out.print (board[r][c]);
      }
      //at the end of each row, put a line break
      System.out.println ();
    } 
    
  }


  //set cell (r,c) to val
  public static void setCell( char[][] board, int r, int c, char val )
  {
    board[r][c] = val;
    
  }


  //return number of living neigbours of board[r][c]
  public static int countNeighbours( char[][] board, int row, int col )
  {
    int count = 0;
    for (int r = row-1; r<=row+1; r++)
    {
        if (r<0) //if r cycles above top row
          continue;
        if (r >= board.length) //bottom boundary
          break;
      for (int c = col-1; c<=col+1; c++)   
      {
        if (c <0) //left bound
          continue;
        if (c >= board[0].length) //right bound
          continue;

        //don't count the actual middle cell
        if (!(r == row && c == col)){
          //check if the cell is alive
          if (board[r][c] == 'X')
          {
            //increment the count
            count++;
          }
        }
        //System.out.print(board[row][col] + " "); 
      }
    
   }  
    return count;
  }


  /**
     precond: given a board and a cell
     postcond: return next generation cell state based on CGOL rules
     (alive 'X', dead ' ')
  */
  public static char getNextGenCell( char[][] board,int r, int c )
  {

    //the next gen character is set to a default of the previous gen's char
    char nextGen = board[r][c];
    
    //check the number of neighbours
    int n = countNeighbours (board, r, c);
    
    //check to see if it's alive or dead
    boolean isAlive = false;
    if (board[r][c] == 'X')
    {
      isAlive = true;
    }

    //determine if the next gen cell is alive or dead
    //if alive --> when do we kill it?
    //* Every cell with <2 neighbours will die from isolation.
    if (isAlive && n<2)
    {
      nextGen = '.';
    }
    
    //* Each cell with >3 neighbours will die from overpopulation.
    if (isAlive && n>3)
    {
      nextGen = '.';
    }

    //if it's dead --> bring to life?
    //* Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive in next generation.
    if (!isAlive && n==3)
    {
      nextGen = 'X';
    }

    //keep it otherwise (see how the nextGen was initialized with default value on line 115)
    
    
    return nextGen;
  }


  //generate and return a new board representing next generation
  public static char[][] generateNextBoard( char[][] board )
  {

    //declare and construct the next gen board (same size as the original board)
    int row = board.length;
    int col = board[0].length;
    char[][] nextGenBoard = new char[row][col]; 
    //char[][] nextGenBoard = board;

    //for loop below traverses the board
    for (int r = 0; r<board.length; r++)
    {
      for (int c = 0; c<board[0].length; c++)
      {
        //get the next gen's char --> put it in the new board
        nextGenBoard[r][c] = getNextGenCell(board, r, c);
      }
    }

    //return the next gen array
    return nextGenBoard;
  }

  //randomly assign life to some cells
  public static void randomLife (char[][] board){

    //traverse through the whole board
    for (int r = 0; r<board.length; r++)
    {
      for (int c = 0; c<board[0].length; c++)
      {
        //generate a random number from 0 - 9
        Random rL = new Random ();
        int randomLife = rL.nextInt(9);

        //check if the random number is greater than 4
        if (randomLife > 4)
        {
          setCell(board, r, c,'X');

        }

        
      }
    } 

    
  }

  public static void main( String[] args )
  {
    char[][] board;
    board = createNewBoard(10,10);
    //breathe life into some cells with random selection:
    randomLife (board);
    //breathe life into some cells with selected cells:
    // setCell(board, 0, 0, 'X');
    // setCell(board, 0, 1, 'X');
    // setCell(board, 1, 0, 'X');
    // setCell(board, 3, 4, 'X');
    // setCell(board, 4, 3, 'X');
    // setCell(board, 3, 3, 'X');
    // TASK:
    // Once your initial version is running,
    // try out different starting configurations of living cells...
    // (Feel free to comment out the above three lines.)
    System.out.println("Gen X:");
    printBoard(board);
    System.out.println("--------------------------\n\n");

    //repeat the gen multiple times
    for (int i= 0; i<10; i++)
    {
      board = generateNextBoard(board);
      System.out.println("Gen X+ "+ (i+1));
      printBoard(board);
      System.out.println("--------------------------\n\n");
    }
    

  }//end main()

}//end class