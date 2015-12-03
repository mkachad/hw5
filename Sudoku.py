
#known numbers for the grid
class known():
    def __init__(self,number):
        self.number = number

    def count(self):
        return 1

#unknown numbers for the grid
#each one has a certainty associated with it
#and a list of possibilities based on col, row, and subsquare
class unknown():
    def __init__(self,number):
        self.number = number
        possiblecolnum = []
        possiblerownum = []
        possiblesquarenum = []
        self.certainty = 0

    #certainty will start at 0 and slowly increase
    #can only be 1 if the other 8 numbers in the section are known
    #certainty will represent % chance that the number is accurate
    def count(self):
        return self.certainty

    #NEEDED:
    #takes a list of possibilities, sets the certainty of the unknown number
    #def setcertainty(self,i,numlist):
        
        
#collection of 9 numbers
class Sudokulist():
    #has list of numbers
    def __init__(self,list):
        self.list = list
    
    #checks to see if all 9 integers are unique
    def isValid(self):
        for i in range (1,9):
            x = 0
            for e in self.list:
                if i == e.number:
                    x += 1
            if x > 1:
                return False
        return True
    
    #returns the number of known items in list as the sum of the certainty
    def numberKnown(self):
        sum = 0
        for e in self.list:
            sum += e.count()
        return sum

    #checks possible numbers and return a list of possibilities for that list
    def possibilities(self):
        #start with all possible numbers
        possiblenum = [1,2,3,4,5,6,7,8,9]

        #if the number is a known number in the list, remove it
        for e in self.list:
            if e.count() == 1:
                possiblenum.remove(e.number)

        #return the list
        return possiblenum

    #NEEDED: method that assigns possible numbers to uncertain numbers
        
            

    #sudoku grid is a set of 9 sudoku lists
    #these 8 sudoku lists represent the 9 rows
class Sudokugrid():
    def __init__(self,list):
        self.list = list

    #takes a column number i and returns a sudoku list of the numbers at index i
    #this represents a sudoku column
    def getcolumn(self,i):
        col = []
        for e in self.list:
            col.append(e[i])
        return col

    #takes a row number i and returns that row
    def getrow(self,i):
        return self.list[i]

    #takes a subsquare number i and returns a sudoku list of the numbers within that subsquare
    #subsquares numbers from left to right, up to down, starting at upper left corner:
    #e.g.:
    #[1, 2, 3
    #4,5,6
    #7,8,9]
    #it follows that the subsquare must be in 1 of 3 rows, and 1 of 3 columns
    def getsubsquare(self,i):
        subsquare = []
        index1 = [1,4,7]
        index2 = [2,5,8]
        index3 = [3,6,9]
        rows = []
        colindex = []

        #define which rows the subsquare is in
        if i <= 3:
            rows = self.list[1:3]
        elif 3 < i <= 6:
            rows = self.list[4:6]
        elif 6 < i <= 9:
            rows = self.list[7:]

        #take the elements in the row that are in the subsquare
        #and add to subsquare list
        if i in index1:
            for e in rows:
                subsquare.append(e[1])
                subsquare.append(e[2])
                subsquare.append(e[3])
        elif i in index2:
            for e in rows:
                subsquare.append(e[4])
                subsquare.append(e[5])
                subsquare.append(e[6])
        elif i in index3:
            for e in rows:
                subsquare.append(e[7])
                subsquare.append(e[8])
                subsquare.append(e[9])

        return subsquare
    
#test cases

a = known(5)
b = known(6)
c = known(7)
d = known(8)
e = unknown(1)
f = unknown(2)
g = unknown(3)
h = unknown(4)
i = known(9)
test_1 = Sudokulist([a,b,c,d,e,f,g,h,i])
test_2 = Sudokulist([a,a,b,e,e,e,e,f,g])
print(test_1.isValid())
print(test_2.isValid())
print(test_1.numberKnown())
print(test_2.numberKnown())
        

