# DSL-to-Python-prototype
A parser and a source code generator that uses Lark to create a DSL and then converts a given script written in that DSL to Python.

### Dependencies

* Lark

### Description

#### Grammar

A simple grammar is defined for a print statement and a loop in Python as follows:

```start : instruction+
   instruction : "print" STRING [STRING]  -> print
                | "repeat" NUMBER code_block  -> repeat

    code_block : "{" instruction+ "}" 
    STRING:  LETTER+

    %import common.LETTER
    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
```

As we input the `repeat 9 print HelloWorld` to the script, it prints HelloWorld for the specified number of times.

#### Parsing and Code Generation

Given an input to the DSL, a parse tree is constructed using the `Lark` library and a corresponding code is generated in Python and stored in the 'output.py' file. 

For example the previously mentioned example when given as an input to the program, it generates a file containing the code:
```
for i in range(9):
  print "Hello World"
```



