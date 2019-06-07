# 提高代码可读性的改进方式
# 参考： https://zhuanlan.zhihu.com/p/27332647

def _parse_text(self):
    """解析模板"""
    tokens = self.re_tokens.split(self.raw_text)
    handlers = (
        (self.re_variable.match, self._handle_variable),   # {{ variable }}
        (self.re_tag.match, self._handle_tag),             # {% tag %}
        (self.re_comment.match, self._handle_comment),     # {# comment #}
    )
    default_handler = self._handle_string                  # 普通字符串

    for token in tokens:
        for match, handler in handlers:
            if match(token):
                handler(token)
                break
        else:
            default_handler(token)

def _handle_variable(self, token):
    """处理变量"""
    variable = token.strip('{} ')
    self.buffered.append('str({})'.format(variable))

def _handle_comment(self, token):
    """处理注释"""
    pass

def _handle_string(self, token):
    """处理字符串"""
    self.buffered.append('{}'.format(repr(token)))

def _handle_tag(self, token):
    """处理标签"""
    # 将前面解析的字符串，变量写入到 code_builder 中
    # 因为标签生成的代码需要新起一行
    self.flush_buffer()
    tag = token.strip('{%} ')
    tag_name = tag.split()[0]
    self._handle_statement(tag, tag_name)

def _handle_statement(self, tag, tag_name):
    """处理 if/for"""
    if tag_name in ('if', 'elif', 'else', 'for'):
        # elif 和 else 之前需要向后缩进一步
        if tag_name in ('elif', 'else'):
            self.code_builder.backward()
        # if True:, elif True:, else:, for xx in yy:
        self.code_builder.add_line('{}:'.format(tag))
        # if/for 表达式部分结束，向前缩进一步，为下一行做准备
        self.code_builder.forward()
    elif tag_name in ('break',):
        self.code_builder.add_line(tag)
    elif tag_name in ('endif', 'endfor'):
        # if/for 结束，向后缩进一步
        self.code_builder.backward()