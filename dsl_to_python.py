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

def generate_code(inst, code, indent_number):
    if inst.data == "print":
        for i in range(indent_number):
            code += "   "
        code += "print " + """ " """ + str(*inst.children) + """ " """ + "\n"
    
    elif inst.data == "repeat": 
        # To deal with nested loops we define a global variable
        # which keeps track of the numberof loops called and the variables are set accordingly
        count, code_block = inst.children
        code += "for i in range(%s):\n"%str(count)
        code, indent_number = generate_code(code_block, code, indent_number)
    
    elif inst.data == "code_block":
        indent_number += 1
        for cmd in inst.children:
            code, indent_number = generate_code(cmd, code, indent_number)
    return code, indent_number

def generate_op(input_dsl_code):
    parse_tree = parser.parse(input_dsl_code)
    print(parse_tree.pretty())
    code = ""
    indent_number = 0
    for instruction in parse_tree.children:
        code, indent_number = generate_code(instruction, code, indent_number)
    return code

parser = Lark(print_grammar)

input_dsl_code = """
    repeat 9 {
        print helloworld
    }
"""

code = generate_op(input_dsl_code)
f = open("output.py", "w+")
f.write(code)
f.close()