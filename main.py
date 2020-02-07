from scripts.load_data import parse_html

key = ""
print("|----------------------|\n|\t py-SE\t       |\n|----------------------|\n")
while key != "0":
    print("Izaberite opciju:")
    print("1 - Parsiranje dokumenata")
    print("0 - Izlaz")
    key = input()
    if key == "1":
        print("Unesite direktorijum za parsiranje:")
        path = input()
        parse_html(path)
