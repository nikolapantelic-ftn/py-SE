class Set:
    def __init__(self):
        self.data = {}

    def __iter__(self):
        return self.data.__iter__()

    def add(self, el):
        self.data[el] = None

    def union(self, *args):
        answer = Set()
        for i in self.data:
            answer.add(i)
        for i in args:
            for j in i:
                answer.add(j)
        return answer

    def intersection(self, s):
        answer = Set()
        for k in s:
            try:
                self.data[k]
                answer.add(k)
            except KeyError:
                pass
        return answer

    def difference(self, s):
        answer = Set()
        for k in s:
            try:
                self.data[k]
            except KeyError:
                answer.add(k)

        return answer
