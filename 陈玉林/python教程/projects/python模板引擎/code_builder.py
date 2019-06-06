class CodeBuilder:
    indent_style = '    '

    def __init__(self, indent_level):
        self.indent_level = indent_level
        self.lines = []

    def indent(self):
        self.indent_level += 1

    def dedent(self):
        self.indent_level -= 1

    def add_line(self, line):
        self.lines.append(self.indent_level * self.indent_style + line)

    def __str__(self):
        return ''.join('{}\n'.format(line) for line in self.lines)

    def __repr__(self):
        return str(self)
