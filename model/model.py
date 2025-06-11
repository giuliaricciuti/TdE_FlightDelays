import networkx as nx

from database.DAO import DAO
from model.airport import Airport


class Model:
    def __init__(self):
        aeroporti = DAO.getAllAirports()
        self._idMapAeroporti = {}
        for a in aeroporti:
            self._idMapAeroporti[a.ID] = a
        self._graph = nx.Graph()

    def buildGraph(self, cMin):
        self._graph.clear()
        self.addNodes(cMin)
        self.addEdges()

    def addNodes(self, cMin):
        self._graph.clear()
        aeroporti = {}
        voli = DAO.getAirportsAirline()
        for v in voli:
            a1 = self._idMapAeroporti[v[0]]
            a2 = self._idMapAeroporti[v[1]]
            if a1 not in aeroporti.keys():
                aeroporti[a1] = [v[2]] #parentesi quadre necessarie perché si tratta di una lista
            elif v[2] not in aeroporti[a1]:
                aeroporti[a1].append(v[2])
            if a2 not in aeroporti.keys():
                aeroporti[a2] = [v[2]]
            elif v[2] not in aeroporti[a2]:
                aeroporti[a2].append(v[2])

        for a in aeroporti.keys():
            if len(aeroporti[a]) >= cMin:
                self._graph.add_node(a)

    def addEdges(self):
        for n in self._graph.nodes:
            for n1 in self._graph.nodes:
                if n != n1:
                    peso = DAO.getArchiPeso(n.ID, n1.ID)
                    if peso>0:
                        self._graph.add_edge(n, n1, weight=peso)


    def handleConnessi(self, a: Airport):
        vicini = []
        for n in nx.neighbors(self._graph, a):
            numVoli = DAO.getNumVoli(n.ID)
            vicini.append((n, numVoli))
        vicini.sort(key = lambda x: x[1])
        return vicini


    def getNodes(self):
        return list(self._graph.nodes)

    def getNum(self):
        return len(self._graph.nodes()), len(self._graph.edges())




