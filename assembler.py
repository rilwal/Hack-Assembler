#!/usr/bin/env python3

import argparse

from hack_parser import Parser, Command
import symbol_table
import code


def main():
    argparser = argparse.ArgumentParser(description='Assembler for Hack assembly language')
    argparser.add_argument("input", help="The file to assemble")
    argparser.add_argument("-o", "--output", help="The output file", required=False)
    argparser.add_argument("-v", "--verbose", action='store_true')
    args = argparser.parse_args()

    input_file = open(args.input)
    output_file = open(args.output or (args.input[:-4] if args.input[-4:] == ".asm" else args.input) + ".hack", "w")
    verbose = args.verbose

    p = Parser(input_file)
    symbols = symbol_table.SymbolTable()

    # first pass
    pc = 0
    for command in p.commands():
        if command.type in {Command.A_COMMAND, Command.C_COMMAND}:
            pc += 1

        if command.type == Command.L_COMMAND:
            symbols[command.symbol] = pc

    try:
        ram_address = 16
        # second pass
        for command in p.commands():
            if not command.type == Command.L_COMMAND:
                if command.type == Command.A_COMMAND:
                    if not command.symbol.isdigit():
                        if command.symbol in symbols:
                            command.symbol = symbols[command.symbol]
                        else:
                            symbols[command.symbol] = ram_address
                            command.symbol = ram_address
                            ram_address += 1

                output_file.write(code.translate(command) + "\n")
                if verbose:
                    print(command)
    except:
        print(command)

    output_file.close()

if __name__ == '__main__':
    main()
