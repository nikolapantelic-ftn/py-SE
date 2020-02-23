from scripts.load_data import trie


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
    doc_list = set()
    string_list, mandatory_string, excluding_string = parse_search(search_string)
    for string in string_list:
        doc_list.update(trie.find_word(string).keys())
    if mandatory_string:
        doc_list = doc_list.intersection(set(trie.find_word(mandatory_string).keys()))
    if excluding_string:
        doc_list = doc_list.difference(set(trie.find_word(excluding_string)))

    return doc_list
