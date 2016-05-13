
import re

lst = ["test", "what", "hello"]
sum([len(elem) for elem in lst])

class Command:
    """ This represents a single hack assembly command. """
    A_COMMAND = 0
    C_COMMAND = 1
    L_COMMAND = 2

    _a_command_regex = re.compile(r"^@([^\n]+)$")
    _c_command_regex = re.compile(r"^(?:(?P<dest>[^=\n]+)=)?(?P<comp>[^;\n]+)(?:;(?P<jump>[^\n]+))?$")
    _l_command_regex = re.compile(r"^\(([^)]+)\)$")

    def __init__(self, command):
        self.command = command

        a_match = Command._a_command_regex.match(command)
        l_match = Command._l_command_regex.match(command)
        c_match = Command._c_command_regex.match(command)

        if a_match is not None:
            self.type = Command.A_COMMAND
            self.symbol = a_match.group(1)

        elif l_match is not None:
            self.type = Command.L_COMMAND
            self.symbol = l_match.group(1)

        elif c_match is not None:
            self.type = Command.C_COMMAND

            self.dest = c_match.group("dest")
            self.comp = c_match.group("comp")
            self.jump = c_match.group("jump")


    def __str__(self):
        string = "Str:\t{}\n".format(self.command)
        if self.type == Command.A_COMMAND:
            string += "Type:\tA_COMMAND\n"
            string += "Symbol:\t{}".format(self.symbol)
        elif self.type == Command.L_COMMAND:
            string += "Type:\tL_COMMAND\n"
            string += "Symbol:\t{}".format(self.symbol)
        elif self.type == Command.C_COMMAND:
            string += "Type\tC_COMMAND\n"
            string += "Dest:\t{}\nComp:\t{}\nJump:\t{}\n".format(
                self.dest, self.comp, self.jump)
        string += "\n"
        return string


class Parser:
    """ This class is used to parse hack assembly """

    _comment_regex = re.compile(r"\/\/[^\n]*$")

    def __init__(self, file):
        self.file = file

    def commands(self):
        """ Generator to get the commands in the hack assembly file """
        for line in self.file:
            # remove comments and whitespace
            line = Parser._comment_regex.sub("", line)
            line = line.strip().lower()

            # yield a line only if it is not now blank
            if not line == "":
                yield Command(line)
