class HTMLInfo:
    def __init__(self, path, links):
        self._path = path
        self._links = links
        self._linked_in = []

    @property
    def path(self):
        return self._path

    @property
    def links(self):
        return self._links

    @property
    def linked_in(self):
        return self._linked_in
