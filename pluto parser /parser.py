from lark import Lark

print_grammar = """
   start : instruction+
   instruction : "print" STRING [STRING]  -> print
                | "repeat" NUMBER code_block  -> repeat

    code_block : "{" instruction+ "}" 
    STRING:  LETTER+

    %import common.LETTER
    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
"""