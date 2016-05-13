
from parser import Command

def translate(command):
    if command.type == Command.C_COMMAND:
        return "111{:07b}{:03b}{:03b}".format(comp(command), dest(command), jump(command))
    elif command.type == Command.A_COMMAND:
        return "0{:015b}".format(int(command.symbol))
    else:
        raise NotImplementedError


def dest(command):
    """ Takes a C command object and returns the
        binary representation of the dest
    """
    translation_table = {
        None:  0b000,
        "m":   0b001,
        "d":   0b010,
        "md":  0b011,
        "a":   0b100,
        "am":  0b101,
        "ad":  0b110,
        "amd": 0b111
    }

    if not command.dest in translation_table:
        raise ValueError("Invalid value for dest")

    return translation_table[command.dest]


def comp(command):
    translation_table = {
        "0":   0b0101010,
        "1":   0b0111111,
        "-1":  0b0111010,
        "d":   0b0001100,
        "a":   0b0110000,
        "!d":  0b0001101,
        "!a":  0b0110001,
        "-d":  0b0001111,
        "-a":  0b0110011,
        "d+1": 0b0011111,
        "a+1": 0b0110111,
        "d-1": 0b0001110,
        "a-1": 0b0110010,
        "d+a": 0b0000010,
        "d-a": 0b0010011,
        "a-d": 0b0000111,
        "d&a": 0b0000000,
        "d|a": 0b0010101,
        "m":   0b1110000,
        "!m":  0b1110001,
        "-m":  0b1110011,
        "m+1": 0b1110111,
        "m-1": 0b1110010,
        "d+m": 0b1000111,
        "d-m": 0b1010011,
        "m-d": 0b1000111,
        "d&m": 0b1000000,
        "d|m": 0b1010101
    }

    if not command.comp in translation_table:
        raise ValueError("Invalid value for comp")

    return translation_table[command.comp]


def jump(command):
    """ Takes a C command object and returns the
        binary representation of the jump
    """
    translation_table = {
        None:  0b000,
        "jgt": 0b001,
        "jeq": 0b010,
        "jge": 0b011,
        "jlt": 0b100,
        "jne": 0b101,
        "jle": 0b110,
        "jmp": 0b111
    }

    if not command.jump in translation_table:
        raise ValueError("Invalid value for jump")

    return translation_table[command.jump]
