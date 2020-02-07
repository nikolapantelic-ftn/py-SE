from modules.parser import Parser
from modules.files import get_html_files
from structs.trie import Trie

link_list = []
word_list = []
trie = Trie()


def parse_html(path):
    global link_list, word_list, trie
    parser = Parser()
    html_files = get_html_files(path)
    for file in html_files:
        print('Parsing file"' + file + '"')
        links, words = parser.parse(file)
        link_list = link_list + links
        word_list = word_list + words

    for word in word_list:
        trie.add_word(word)
