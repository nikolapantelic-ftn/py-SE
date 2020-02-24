from modules.parser import Parser
from modules.files import get_html_files
from structs.trie import Trie

link_list = []
word_list = []
trie = Trie()
edge_list=list()



def parse_html(path):
    global link_list, word_list, trie
    parser = Parser()
    html_paths = get_html_files(path)
    for file in html_paths:
        print('Parsing file"' + file + '"')
        links, words = parser.parse(file)
        for word in words:
            trie.add_word(word, file)
        for link in links:
            edge_list.append((file,link))
