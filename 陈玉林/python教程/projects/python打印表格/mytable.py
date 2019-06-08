#!/usr/bin/env python3

import re
'''
边框字符参考:
    https://en.wikipedia.org/wiki/Box-drawing_character
'''

LEFT = '<'
RIGHT = '>'
CENTER = '^'

class MyTable:
    '''
    1. 支持中文,解决全角字符对齐问题
    2. 支持设置对齐方式(左,右,居中)
    3. 支持自定义单元格最大长度(默认为10个半角字符)
    4. 超出显示范围的字符串以'..'方法结尾
    5. 该类的主要作用是输出表格,没有过多考虑性能问题,包含大量字符串拼接
    '''

    def __init__(self, data, pos=0, max_len=10):
        '''
        pos=0: 左对齐(默认)
        pos=1: 右对齐
        pos=2: 居中
        '''
        if not data or not data[0]:
            raise Exception('Invalid data!', data)
        self.data = data
        self.row = self._get_row()
        self.col = self._get_col()
        if pos == 1:
            self.position = RIGHT
        elif pos == 2:
            self.position = CENTER
        else:
            self.position = LEFT
        for row in range(self.row):
            for col in range(self.col):
                # data[row][col] = '{0:.{1}}'.format(str(data[row][col]), max_len)
                if len(str(data[row][col])) > max_len:
                    data[row][col] = str(data[row][col])[:max_len] + '..'
                else:
                    data[row][col] = str(data[row][col])


    def _get_row(self):
        return len(self.data)

    def _get_col(self):
        return len(self.data[0])

    def _length_list(self):
        result = []
        for col in range(self.col):
            col_data = [len(self.data[row][col]) for row in range(self.row)]
            max_length = max(col_data)
            result.append(max_length)
        return result

    def render(self):
        max_lengths = self._length_list()

        # 1. border_top
        border_top = '┌─'
        border_top += '─┬─'.join(['─'*length for length in max_lengths])
        border_top += '─┐'
        print(border_top)

        # 2. data_line
        for row in range(self.row):
            data_line = '│ '
            chinese_pattern = u'[?([\u4E00-\u9FA5]'
            line_data = [] 
            for col in range(self.col):
                full_width_char_num = len(re.findall(chinese_pattern,self.data[row][col]))
                line_data.append('{0:{1}{2}}'.
                    format(self.data[row][col], self.position, max_lengths[col]-full_width_char_num)) 
            #data_line += ' │ '.join(['{0:{1}{2}}'.
            #    format(self.data[row][col], self.position, max_lengths[col]-full_width_char_num) 
            #        for col in range(self.col)])
            data_line += ' │ '.join(line_data)
            data_line += ' │'
            print(data_line)
            if row != self.row-1:

                # 3. separate_line
                separate_line = '├─'
                separate_line += '─┼─'.join(['─'*length for length in max_lengths])
                separate_line += '─┤'
                print(separate_line)

        # 4. border_bottom
        border_bottom = '└─'
        border_bottom += '─┴─'.join(['─'*length for length in max_lengths])
        border_bottom += '─┘'
        print(border_bottom)


if __name__ == '__main__':
    data = [
        ['row1 col1', 'hello', '2333333333333333333333', 'abc'],
        ['row2 col1', 'row2 col2', 'hi', 123],
        ['中文测试', '中文', 'England', 'Franch']
    ]
    table = MyTable(data)
    #table = MyTable(data, 2)
    #print(table._get_row())
    #print(table._get_col())
    #print(table._length_list())
    table.render()

