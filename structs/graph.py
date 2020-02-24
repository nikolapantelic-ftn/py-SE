class Graph(object):

    def __init__(self):
        self._ingoing = {}
        self._outgoing = {}

    def insert_vertex(self, e):
        self._outgoing[e] = []
        self._ingoing[e] = []

    def insert_edge(self, u, v):
        self._outgoing[u].append(v)
        self._ingoing[v].append(u)

    def ingoing_links(self, v):
        return self._ingoing[v]

    def outgoing_links(self, v):
        return self._outgoing[v]

    def __str__(self):

        ret = ""

        for key in self._outgoing.keys():
            list1 = self._outgoing[key]
            list2 = self._ingoing[key]

            ret += ("\n*" + str(key) + " out link = " + str(len(list1)) + " in link = " + str(len(list2)))
            ret += "\n"
            ret +="\n OUT: \n"
            for o in list1:
                ret += str("{} -- {}\n".format(" " * 20, o))

            ret += "\n IN: \n"
            for i in list2:
                ret += str("{} -- {}\n".format(" " * 20, i))

        return str(ret)
