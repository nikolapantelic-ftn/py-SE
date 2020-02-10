from scripts.load_data import trie


def parse_search(search_string):
    string_list = search_string.split()
    if string_list.any(["AND", "OR", "NOT"]):
        if len(string_list) == 3:
            if string_list[1] == "AND":
                return [string_list[0]], string_list[2], None
            if string_list[1] == "OR":
                return [string_list[0], string_list[2]], None, None
            if string_list[1] == "NOT":
                return [string_list[0]], None, string_list[2]
        print("Neispravno unet upit pretrage sa logickim operatorom.")
        return [], None, None
    else:
        return string_list, None, None


def search_documents(search_string):
    doc_list = []
    string_list, mandatory_string, excluding_string = parse_search(search_string)
    for string in string_list:
        docs = trie.find_word(string).keys()
        for doc in docs:
            if doc not in doc_list:
                doc_list.append(doc)
    if mandatory_string:
        docs = trie.find_word(mandatory_string).keys()
        doc_list = [doc for doc in doc_list if doc in docs]
    if excluding_string:
        exclude_docs = trie.find_word(excluding_string)
        doc_list = [doc for doc in doc_list if doc not in exclude_docs]

    return doc_list
