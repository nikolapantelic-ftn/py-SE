def rank(graph, res):
    rank_page= {}

    for page in res.keys():

        word_count=res[page]
        ingoing=graph.ingoing_links(page)
        num_links=len(ingoing)
        num_in_links=0
        for link in ingoing:
            if link in res.keys():
                num_in_links+=res[link]

        rank_page[page]=int(word_count+num_links*0.6  +num_in_links*0.2)

    print(rank_page)
    return rank_page
