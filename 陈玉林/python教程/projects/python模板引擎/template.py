import re
from code_builder import CodeBuilder

class Template:

    def __init__(self, text, indent_level=0):
        self.text = text
        self.indent_level = indent_level
        self.code_builder = CodeBuilder(indent_level=indent_level)
        self.build_code()
        
        
    def build_code(self):
        self.code_builder.add_line('def render_function():')
        self.code_builder.indent()
        self.code_builder.add_line('result = []')
        self.parse_text()
        self.code_builder.add_line('return "".join(result)')

        
    def parse_text(self):
        buffer = []

        # (?s)是一个flag，它表示.同样可以匹配一个\n
        tokens = re.split(r"(?s)({{.*?}}|{%.*?%}|{#.*?#})", self.text)
        for token in tokens:
            # {{ expression }}
            if token.startswith('{{'):
                expression = token.strip('} {')
                # 不直接传入expression是为了处理数学表达式
                buffer.append('str({})'.format(expression)) 
            # {# comment #}
            elif token.startswith('{#'):
                continue
            # {% control flow %}
            elif token.startswith('{%'):
                # flush buffer
                if buffer:
                    self.code_builder.add_line('result.extend([{}])'.format(','.join(buffer)))
                    buffer = []

                expression = token.strip('}% {')
                tag = expression.split()[0]
                if tag in ('if', 'for'):
                    self.code_builder.add_line(expression + ':')
                    self.code_builder.indent()
                elif tag in ('elif', 'else'):
                    self.code_builder.dedent()
                    self.code_builder.add_line(expression + ':')
                    self.code_builder.indent()
                elif tag in ('break', 'continue'):
                    self.code_builder.add_line(tag)
                elif tag in ('endif', 'endfor'):
                    self.code_builder.dedent()
            else:
                if token.strip() != '':
                    buffer.append(repr(token.strip()))

        if buffer:
            self.code_builder.add_line('result.extend([{}])'.format(','.join(buffer)))


    def render(self, context=None):
        namespace = {}
        if context:
            namespace.update(context)

        exec(str(self.code_builder), namespace)
        return namespace['render_function']()

        
if __name__ == '__main__':
    t = Template('''
    <h1>{{ name }}</h1>
    {# comment #}
    {% if a > b %}
        <span>a greater then b</span>
    {% elif a < b %}
        <span>a less then b</span>
    {% else %}
        <span>a equals to b</span>
    {% endif %}
    <div>test test test</div>
    {% if False %}
        <strong>this will not appear</strong>
    {% endif %}
    <span>-----------------</span>
    {% for v in values %}
        <li>fruit: {{v}}</li>
        {% if v == 'pear' %}
            {% break %}
        {% endif %}
    {% endfor %}
    ''')
    print(t.code_builder)
    result = t.render({'name':'hello', 'values': ['apple', 'banana', 'pear', 'lemon'], 'a':100, 'b':200})
    print(result)

