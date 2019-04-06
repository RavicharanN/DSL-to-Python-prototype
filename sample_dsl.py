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

parser = Lark(print_grammar)

def run_instruction(inst):
    if inst.data == "repeat":
        count, block = inst.children
        for i in range(int(count)):
            run_instruction(block)

    elif inst.data == "print":
        # n1, n2 = inst.children
        print(*inst.children)
    
    elif inst.data == "code_block":
        for cmd in inst.children:
            run_instruction(cmd)

    else:
        raise SyntaxError("Invalid Instructuion: %s"%inst.data)

def run_printer(code):
    parse_tree = parser.parse(code)
    print(parse_tree.pretty())
    for instruction in parse_tree.children:
        run_instruction(instruction)


sample_code = """
    repeat 9 {
        print helloworld
    }
"""
run_printer(sample_code)