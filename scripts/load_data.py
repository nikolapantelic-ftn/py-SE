from modules.parser import Parser
from modules.files import get_html_files
from structs.trie import Trie
import time

trie = Trie()
edge_list = list()


def parse_html(path):
    trie.empty()
    parser = Parser()
    html_paths = get_html_files(path)
    begin_time = time.time()
    for file in html_paths:
        print('Parsing file -- ' + file)
        links, words = parser.parse(file)
        for word in words:
            trie.add_word(word, file)
        for link in links:
            edge_list.append((file, link))
    if html_paths:
        print("Direktorijum parsiran za %s sekundi" % (time.time() - begin_time))
