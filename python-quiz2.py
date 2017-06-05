'''
Christie Brandao
'''

#Part 2
#Q5
testdata = [ [ 'x', 4.700, 2.275, 4.476],
             [ 'y', 10.791, 5.005, 9.407 ],
             [ 'x', 18.782, 7.558, 13.532 ],
             [ 'x', 29.425, 14.364, 24.165 ],
             [ 'x', 35.331, 17.314, 28.188 ],
             [ 'y', 41.028, 20.517, 32.218 ] ]
sum_of_x = 0
for i in testdata:
    if i[0] == 'x':
        sum_of_x = sum_of_x + i[1] + i[2] + i[3]
print sum_of_x

#Q6
sum_of_x_total = 0
sum_of_x_list = [j[1] + j[2] + j[3] for j in testdata if j[0] == 'x']
sum_of_x_total = sum_of_x_total + sum(sum_of_x_list)
print sum_of_x_total

#Q7
print [ [i, j] for i in range(5) for j in range(4)]
print
print [ [i for i in range(5)] for j in range(4)]
print
'''
The first does a cross multiplication type of arrangement with x spanning
from 0-4 and y spanning from 0 - 3 starting with (0,0) and ending in (4,3). It
creates a list of lists which are of size 2.

The second creates a list of 4 lists which have 5 numbers that are all the same
which is [0, 1, 2, 3, 4]. 

'''

#Q9
def get_int(data):
    list_of_ints = []
    for i in data:
        if isinstance(i, int):
            list_of_ints.append(i)
    for j in list_of_ints:
        if isinstance(j, bool):
            list_of_ints.remove(j)
    return list_of_ints
list1 = ['xyz', 3>1, 13, 55, 55.5, 12.1, 'temp']
list2 = [55, 66, 77, 'string', True]
print get_int(list1)
print get_int(list2)

#Part 3
#Q10
"""
Examples
 
  >>> import sys
  >>> sys.path.append('/Users/xiao/programs/gis-algorithms/gisalgs')
  >>> from geom.point import *
  >>> from indexing.pointquadtree1 import *
  >>>
  >>> data = [ [i, j] for i in range(10) for j in range(10) ]
  >>> points = [Point(d[0], d[1]) for d in data]
  >>> q = pointquadtree(points)
  >>> rect = [ [5, 7], [5, 6] ]
  >>>
  >>> found = []
  >>> pq_range_query_orthogonal(q, rect, found)
  >>> found
  [(5.0, 6.0), (6.0, 6.0), (7.0, 6.0), (5.0, 5.0), (6.0, 5.0), (7.0, 5.0)]
 
"""
def pq_range_query_orthogonal(t, rect, found, depth=0):
    """
    Orthogonal range query for point quad trees
 
    Input
      t      An instance of the PQuadTreeNode class (pointquadtree1.py)
      rect   2D list defining a rectangle as [ [xmin, xmax], [ymin, ymax] ]
      found  a list to hold points found, declared outside
      depth  not used in the current code
 
    Output
      This function does not return any values. However, all the points
      found during the query process will be appended to list found.
    """
    if t is None:
        return
    x, y = t.point.x, t.point.y
    if x < rect[0][0]:
        pq_range_query_orthogonal(t.ne, rect, found, depth+1)
        pq_range_query_orthogonal(t.se, rect, found, depth+1)
        return
    if x > rect[0][1]:
        pq_range_query_orthogonal(t.ne, rect, found, depth+1)
        pq_range_query_orthogonal(t.nw, rect, found, depth+1)
        return
    if y < rect[1][0]:
        pq_range_query_orthogonal(t.nw, rect, found, depth+1)
        pq_range_query_orthogonal(t.sw, rect, found, depth+1)
        return
    if y > rect[1][1]:
        pq_range_query_orthogonal(t.se, rect, found, depth+1)
        pq_range_query_orthogonal(t.sw, rect, found, depth+1)
        return
    if not (rect[0][0]>x or rect[0][1]<x or rect[1][0]>y or rect[1][1]<y):
        found.append(t.point)
    pq_range_query_orthogonal(t.nw, rect, found, depth+1)
    pq_range_query_orthogonal(t.ne, rect, found, depth+1)
    pq_range_query_orthogonal(t.se, rect, found, depth+1)
    pq_range_query_orthogonal(t.sw, rect, found, depth+1)
    return

#Q11
'''
1) The root node will be the first x,y coordinate which is [77,93] in the list
2) rect = [ [30, 80], [30, 70] ] ---> [xmin, xmax] [ymin, ymax]
If the x coordinate is not inside the range of between 30 and 80 or if the y coordinate
does not fall in the range of 30, 70 then the points will not be examined.

