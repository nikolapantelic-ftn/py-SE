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
    doc_list = {}
    string_list, mandatory_string, excluding_string = parse_search(search_string)
    for string in string_list:
        docs = trie.find_word(string)
        for doc in docs.keys():
            if doc in doc_list:
                doc_list[doc] = doc_list[doc] + docs[doc]
            else:
                doc_list[doc] = docs[doc]
    if mandatory_string:
        temp_doc_list = {}
        mandatory_docs = trie.find_word(mandatory_string)
        for doc in mandatory_docs.keys():
            if doc in doc_list:
                temp_doc_list[doc] = doc_list[doc] + mandatory_docs[doc]
        doc_list = temp_doc_list
    if excluding_string:
        excluding_docs = trie.find_word(excluding_string)
        for doc in excluding_docs.keys():
            try:
                doc_list.pop(doc)
            except KeyError as e:
                pass
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
