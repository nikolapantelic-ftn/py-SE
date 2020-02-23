from lark import Lark

"""
Gramatika za parser upita za naprednu pretragu.
Koristi se Lark parser.

https://github.com/lark-parser/lark
"""

parser = Lark('''
        start : exp
        exp : WORD -> word
            | "(" exp ")"
            | exp "||" exp -> or_op
            | exp "&&" exp -> and_op
            | "!" exp -> not_op

        %import common.WORD
        %import common.WS
        %ignore WS
            ''')

"""
Vraca stablo parsiranja za uneti upit
"""


def advanced_parse_search(search_string):
    return parser.parse(search_string)
