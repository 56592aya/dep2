import networkx as nx
from pathlib import Path
class DAG:
    def __init__(file):
        self.file = file
        self.dag = self.create_dag()
        self.predecessors = self.get_predecessors()
        self.attrs = self.init_attrs()

    def create(self):
        # reads in node and edges
        self.node, self.edges = read_file(self.file)
        # create a DAG given the adjlist 
        dag = nx.DiGraph()
        for edge in self.edges:
            dag.add_edge(edge[0], edge[1])
        return dag
    
    def get_predecessors(self):
        predecessors = {}
        for node in self.nodes:
            predecessors[node] = nx.predecessors(self.dag, node)
        return predecessors
    
    def init_attrs(self):
        # we need to create attributes for each node
        attrs = {node:{} for node in self.nodes}
        for node in self.nodes:
            attrs[node] = {node:None | p for p in self.predecessors[node]}
            self.dag.set_attributes(node, attrs[node])
    
    def save_dag(self):
        save(self.dag, "../data/dag.txt")
    
    