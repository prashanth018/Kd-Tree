import Queue

#Querying the Tree Yet to be written

class Tree:
    left = 0
    right = 0
    data = 0
    def __init__(self):
        self.right = None
        self.left = None
        self.data = None

class KDTree:
    k = 0
    NumOfPoints = 0
    Points = []
    root = None
    
    def __init__(self,k,NumOfPoints):
        self.k = k
        self.NumOfPoints = NumOfPoints

    def ReadPoints(self):
        temp = ""
        for i in range(self.NumOfPoints):
            temp = raw_input()
            temp = temp.split()
            for j in range(self.k):
                temp[j] = int(temp[j])
            self.Points.append(tuple(temp))

    def PrintTree(self,Root):
        #Level Order Print
        Q = Queue.Queue(maxsize=0)
        Q.put((Root,0))
        while not Q.empty():
            temp = Q.get()
            if temp[0].left!=None:
                Q.put((temp[0].left,temp[1]+1))
            if temp[0].right!=None:
                Q.put((temp[0].right,temp[1]+1))
            print temp[1],temp[0].data
        
            
            

    def CreateTree(self):
        self.root = Tree()
        self.root.data = self.Points[0]
        for i in range(1,len(self.Points)):
            temp = self.root
            ct=0
            parent = temp
            while temp!=None:
                parent = temp
                if temp.data[ct%self.k]<=self.Points[i][ct%self.k]:
                    temp = temp.right
                else:
                    temp = temp.left
                ct+=1
            if ct!=0:
                ct-=1
            if parent.data[ct%self.k]<=self.Points[i][ct%self.k]:
                parent.right = Tree()
                parent.right.data = self.Points[i]
            else:
                parent.left = Tree()
                parent.left.data = self.Points[i]
            #self.PrintTree(self.root)
        return self.root
                
def main():
    Kdt = KDTree(2,7)
    print "Awaiting to read",Kdt.NumOfPoints,"points."
    Kdt.ReadPoints()
    print "Points Read, Creating Tree"
    Root = Kdt.CreateTree()
    print "Tree Created"
    print "Printing Tree"
    Kdt.PrintTree(Root)

main()
    
    
    
            
