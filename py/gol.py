# FILENAME: gol.py
# First Last: Théa Williams
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: thinkcspy text, Datacamp Intro to Python course, W3schools, Kate M.

"""
   The Rules of Life:
   Survivals:
   * A living cell with 2 or 3 living neighbours will survive for the next generation.
   Deaths:
   * Each cell with >3 neighbours will die from overpopulation.
   * Every cell with <2 neighbours will die from isolation.
   Births:
   * Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive in next generation.
   NOTA BENE:  All births and deaths occur simultaneously. Together, they constitute a single generation.
"""

#create, initialize, and return  empty board (all cells dead)
def createNewBoard(rows, cols):
  board = [["." for c in range(cols)]for r in range(rows)]
  return board
  
#print the board to the terminal
def printBoard(board):

  #traverse through entire array
  for r in range(len(board)):
    for c in range(len(board[r])):
      
      #print out each cell's char
      print(board[r][c], end = " ")
    
    #at the end of each row, put a line break
    print()

#set cell (r,c) to val
def setCell(board, r, c, val):
  board[r][c] = val
#return number of living neigbours of board[r][c]
def countNeighbours(board, row, col):
  count = 0
  for r in range(row-1, row + 2):
    if r < 0: #if r cycles above top row
      continue
    if r >= len(board): #bottom boundary
      break
    for c in range(col-1, col + 2):
      if c < 0: #left boundary
        continue
      if c > len(board[0]): #right boundary
        continue
        
      #don't count the actual middle cell
      if not (r == row and c == col):

        #check if the cell is alive
        if board[r][c] == 'X':

          #increment the count
          count = count + 1
       
  return count

#precond: given a board and a cell
#postcond: return next generation cell state based on CGOL rules (alive 'X', dead ' ')
  
def getNextGenCell(board, r, c ):

  #the next gen character is set to a default of the previous gen's char
  nextGen = board[r][c]
    
  #check the number of neighbours
  n = countNeighbours(board, r, c)
    
  #check to see if it's alive or dead
  isAlive = false
  if board[r][c] == 'X':
    isAlive = true

  #determine if the next gen cell is alive or dead
  #if alive --> when do we kill it?
  #Every cell with <2 neighbours will die from isolation.
  if isAlive and n<2:
    nextGen = '.'
#Each cell with >3 neighbours will die from overpopulation.
  if isAlive and n>3:
    nextGen = '.'

  #if it's dead --> bring to life?
  #Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive in next generation.
  if not(isAlive and n==3):
    nextGen = 'X'

    #keep it otherwise (see how the nextGen was initialized with default value on line 115)
    
  return nextGen

#generate and return a new board representing next generation
def generateNextBoard(board):

  #declare and construct the next gen board (same size as the original board)
  row = len(board)
  col = len(board[0])
  nextGenBoard = createNewBoard(row, col) 

  #for loop below traverses the board
  for r in range(row):
    for c in range (col):
    #get the next gen's char --> put it in the new board
      nextGenBoard[r][c] = getNextGenCell(board, r, c)

    #return the next gen array
  return nextGenBoard

board = createNewBoard(10,10)

#breathe life into some cells with selected cells:
setCell(board, 0, 0, 'X')
setCell(board, 0, 1, 'X')
setCell(board, 1, 0, 'X')
setCell(board, 3, 4, 'X')
setCell(board, 4, 3, 'X')
setCell(board, 3, 3, 'X')
setCell(board, 3, 3, 'X')

print("Gen X:")
printBoard(board)
print("--------------------------\n\n")

#repeat the gen multiple times
for i in range (10):
  board = generateNextBoard(board)
print("Gen X+ "+ (i+1))
printBoard(board)
print("--------------------------\n\n");

"""
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
    // setCell(board, (0, 0), 'X');
    // setCell(board, 0, 1, 'X');
    // setCell(board, 1, 0, 'X');
    // setCell(board, 3, 4, 'X');
    // setCell(board, 4, 3, 'X');
    // setCell(board, 3, 3, 'X');
       setCell(board, (3,3), 'X')
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

}//end class """