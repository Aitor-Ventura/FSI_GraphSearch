# Search methods

import search

inicio = 'A' #@param ['A', 'B','C', 'D','E','F','G','H','I', 'L','N','O','P','R','S','T','U','V','Z']
fin    = 'B' #@param ['A', 'B','C', 'D','E','F','G','H','I', 'L','N','O','P','R','S','T','U','V','Z']

ab = search.GPSProblem(inicio, fin, search.romania)

def visualizar(a, name):
    print(name+"\t", a[1], "\t", a[0].path())

visualizar(search.breadth_first_graph_search(ab), "# Breadth First " + inicio + fin + "\t")
visualizar(search.depth_first_graph_search(ab), "# Depth First " + inicio + fin + "\t")
visualizar(search.branch_and_bound_search(ab), "# Branch and Bound " + inicio + fin + "\t")
visualizar(search.branch_and_bound_heuristic_search(ab), "# Branch and Bound H " + inicio + fin + "\t")
print("\n")
visualizar(search.breadth_first_graph_search(search.GPSProblem('B', 'Z', search.romania)), "# Breadth First BZ\t")
visualizar(search.depth_first_graph_search(search.GPSProblem('B', 'Z', search.romania)), "# Depth First BZ\t")
visualizar(search.branch_and_bound_search(search.GPSProblem('B', 'Z', search.romania)), "# Branch and Bound BZ\t")
visualizar(search.branch_and_bound_heuristic_search(search.GPSProblem('B', 'Z', search.romania)), "# Branch and Bound H BZ\t")
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
