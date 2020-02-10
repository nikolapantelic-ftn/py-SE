from scripts.load_data import parse_html
from scripts.search import search_documents

key = ""
print("|----------------------|\n|\t py-SE\t       |\n|----------------------|\n")
while key != "0":
    print("Izaberite opciju:")
    print("1 - Parsiranje dokumenata")
    print("2 - Unos upita za pretragu")
    print("0 - Izlaz")
    key = input()
    if key == "1":
        print("Unesite direktorijum za parsiranje:")
        path = input()
        parse_html(path)
    if key == "2":
        print("Pretrazi: ")
        search_string = input()
        docs = search_documents(search_string)
        if docs:
            print("Rezultat pretrage: ")
            print(docs)
        else:
            print("Pretraga - " + search_string + " - se ne poklapa ni sa jednim dokumentom.")
        input("Pritisni Enter za nastavak...")
