from database.DAO import DAO
from model.model import Model

m = Model()
m.buildGraph(5)
print(m.getNum())
a = m.getNodes()[0]
for n in (m.handleConnessi(a)):
    print(n)
