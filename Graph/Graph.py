class Graph:
    def __init__(self):
        self.adj_list = {}

    def print(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 not in self.adj_list.keys() or v2 not in self.adj_list.keys():
            return False
        try:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
        except ValueError:
            pass
        return True

    def remove_vertex(self, vertex):

        if vertex not in self.adj_list.keys():
            return False

        for other_vertex in self.adj_list[vertex]:
            self.adj_list[other_vertex].remove(vertex)

        del self.adj_list[vertex]
        return True


my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')

my_graph.remove_vertex('D')

my_graph.print()
