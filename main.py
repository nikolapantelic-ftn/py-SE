from modules.rank import rank
from scripts.load_data import parse_html
from scripts.search import search_documents, advanced_search, lark_enabled
from scripts.load_graph import make_graph
from scripts.load_data import trie


import os

key = ""
print("|----------------------|\n|\t py-SE\t       |\n|----------------------|\n")

os.chdir("test-skup")
os.chdir("python-2.7.7-docs-html\whatsnew")
path = os.path.abspath("")

while key != "0":
    print("Izaberite opciju:")
    print("1 - Parsiranje dokumenata")
    print("2 - Unos upita za pretragu")
    print("3 - Napredna pretraga")
    print("4- Nacrtaj graph")
    print("5- Rangirana pretraga ")
    print("0 - Izlaz")
    key = input()
    if key == "1":
        print("Unesite direktorijum za parsiranje:")
        path = input()
        try:
            edge_list = list()
            parse_html(path, edge_list)
        except NotADirectoryError as nde:
            print("Uneta putanja ne odgovara direktorijumu.")
    if key == "2":
        print("Pretrazi: ")
        search_string = input()
        try:
            docs = search_documents(search_string)
            if docs.data:
                print("Rezultat pretrage: ")
                print(docs)
            else:
                print("Pretraga - " + search_string + " - se ne poklapa ni sa jednim dokumentom.")
        except ValueError as ve:
            print(ve)
        input("Pritisni Enter za nastavak...")
    if key == "3":
        if not lark_enabled:
            print("Lark parser nije instaliran. Instalirajte Lark parser: 'pip install lark-parser'")
            continue
        print("Pretrazi: ")
        search_string = input()
        try:
            advanced_search(search_string)
        except Exception as e:
            print("Pogresan unos upita napredne pretrage")
    if key == "4":
        graph = make_graph(path)
        print(graph)
    if key == "5":
        word = input("")
        print(word)
        #graph = make_graph(path)
        res = trie.find_word(word)
        print(len(res))

        if len(res) > 0:
            rang_res = rank(graph,res)
        else:
            print("neuspesna pretraga")
