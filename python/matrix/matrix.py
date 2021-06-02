class Matrix:
    def __init__(self, matrix_string):
        self._grid = []
        # convert the matrix string into
        # list of strings
        # at every new-line character
        rows_str = matrix_string.split('\n')
        
        for row in rows_str:
            # split the rows at each space character
            # and convert them to a float
            # all these brackets almost remind you of lisp :D
            self._grid.append(list(map(lambda x: float(x), row.split(' '))))
        
        # this function essentially makes three passes 
        # atleast that is what I think is going on 
        # can you get it down to just one pass?
        # even if you could, would that be a good solution?

    def row(self, index):
        # could not be simpler
        return self._grid[index-1]

    def column(self, index):
        # this is also quite obvious
        col = []
        for row in self._grid:
            col.append(row[index-1])
        return col
