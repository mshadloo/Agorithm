class solution:
    def getPath(self, maze):
        path=[]
        faildPoints=set();

        if(self.pathFinder(maze, len(maze)-1,len(maze[0])-1,faildPoints,path)):
            return path
        return None
    def pathFinder(self,maze, row, col,faildPoints,path):
        point=(row,col)
        if(row<0 or col<0 or not maze[row][col]):
            return False
        if(point in faildPoints):
            return False;
        isOriginate= row==0 and col==0
        if(isOriginate or self.pathFinder(maze,row-1,col,faildPoints,path) or self.pathFinder(maze,row,col-,faildPoints,path)):
            path.append(point);
            return True;
        faildPoints.add(point)
        return False
