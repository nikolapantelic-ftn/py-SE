from modules.rank import rank
from scripts.load_data import parse_html
from scripts.search import search_documents, advanced_search, lark_enabled
from scripts.load_graph import make_graph
from scripts.load_data import trie
from modules.sort import sort


import os

key = ""
print("|----------------------|\n|\t py-SE\t       |\n|----------------------|\n")



while key != "0":
    print("Izaberite opciju:")
    print("1 - Parsiranje dokumenata")
    print("2 - Unos upita za pretragu")
    print("3 - Napredna pretraga")
    print("4 - Nacrtaj graph")
    print("5 - Rangirana pretraga ")
    print("0 - Izlaz")
    key = input()
    if key == "1":
        print("Unesite direktorijum za parsiranje:")
        path = input()
        try:

            parse_html(path)
        except NotADirectoryError as nde:
            print("Uneta putanja ne odgovara direktorijumu.")
    if key == "2":
        print("Pretrazi: ")
        search_string = input()
        try:
            docs = search_documents(search_string)
            if docs:
                print("Stranice koje zadovoljavaju pretragu: ")
                for doc in docs.keys():
                    print(doc)
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
        graph = make_graph()
        print(graph)
    if key == "5":
        print("unesite reci za pretragu:")
        search_string = input("")

        res = search_documents(search_string)

        if len(res) > 0:
            page_size = int(input("Koliko stranica treba prikazati po pretrazi: "))
            num_res = len(res)
            page_num = (num_res // page_size) + 1
            current_page = 0
            rank_res = rank(graph,res)
            list_rank=list(rank_res.items())
            sort(list_rank,0,len(list_rank)-1)
            while current_page != -1:
               if(current_page>=page_num):
                   print("Stranica ne postoji")
                   current_page=-1
               else:
                print("--" * 70)
                print("{:100}      {:4}".format("HTML page", "RANK"))

                for index in range(current_page * page_size, current_page * page_size + page_size):
                    if index < len(list_rank):
                        line = list_rank[index]
                        print("{:100}      {:4}".format(str(line[0]), str(line[1])))
                print("PAGE %d"%current_page)
                tmp=page_num-1
                current_page = int(input("Izaberite broj stranice:    (Od 0 do %d || -1 za izlazak)"%tmp))
        else:
            print("neuspesna pretraga")
