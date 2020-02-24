from scripts.load_data import trie
from structs.set import Set

lark_enabled = True
try:
    from modules.advanced_parser import advanced_parse_search
except ModuleNotFoundError as mnfe:
    lark_enabled = False
    print("Lark parser nije instaliran! Napredna pretraga nece biti moguca.\n"
          " Instalirati Lark: 'pip install lark-parser'")


def parse_search(search_string):
    string_list = search_string.split()
    if any(search in ["AND", "OR", "NOT"] for search in string_list):
        if len(string_list) == 3:
            if string_list[1] == "AND":
                return [string_list[0]], string_list[2], None
            if string_list[1] == "OR":
                return [string_list[0], string_list[2]], None, None
            if string_list[1] == "NOT":
                return [string_list[0]], None, string_list[2]
        raise ValueError("Neispravno unet upit pretrage sa logickim operatorom.")
        return [], None, None
    else:
        return string_list, None, None


def search_documents(search_string):
    doc_list = Set()
    string_list, mandatory_string, excluding_string = parse_search(search_string)
    for string in string_list:
        doc_list = doc_list.union(trie.find_word(string).keys())
    if mandatory_string:
        mandatory_docs = Set()
        mandatory_docs = mandatory_docs.union(trie.find_word(mandatory_string).keys())
        doc_list = doc_list.intersection(mandatory_docs)
    if excluding_string:
        excluding_docs = Set()
        excluding_docs = excluding_docs.union(trie.find_word(excluding_string))
        doc_list = doc_list.difference(excluding_docs)

    return doc_list


"""
Napredna pretraga.
Za ispis stabla parsiranja koristiti: 
    print(parse_tree.pretty())
"""


def advanced_search(search_string):
    parse_tree = advanced_parse_search(search_string)
    print(parse_tree.pretty())
    # TO-DO: evaluacija stabla parsiranja
