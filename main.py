from KdTree import KDTree,Tree

Dim = raw_input()
Dim = int(Dim)

NoofPts = raw_input()
NoofPts = int(NoofPts)

Kdt = KDTree(Dim,NoofPts)
print "Awaiting to read",Kdt.NumOfPoints,"points."
Kdt.ReadPoints()
print "Points Read, Creating Tree"
Root = Kdt.CreateTree()
print "Tree Created"
print "Printing Tree"
Kdt.PrintTree(Root)
