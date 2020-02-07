from modules.parser import Parser
from modules.files import get_html_files
from structs.html_info import HTMLInfo
from structs.trie import Trie

link_list = []
word_list = []
html_files = []
trie = Trie()


def parse_html(path):
    global link_list, word_list, trie, html_files
    parser = Parser()
    html_paths = get_html_files(path)
    for file in html_paths:
        print('Parsing file"' + file + '"')
        links, words = parser.parse(file)
        html_files.append(HTMLInfo(file, links))
        for word in words:
            trie.add_word(word)

    for file in html_files:
        for check_file in html_files:
            if file.path in check_file.links:
                file.linked_in.append(check_file)
