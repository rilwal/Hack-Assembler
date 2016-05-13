#!/usr/bin/env python3

import symbol_table
import parser
import code

symbols = symbol_table.SymbolTable()
p = parser.Parser(open("add.asm"))

for command in p.commands():
    print(code.translate(command))
