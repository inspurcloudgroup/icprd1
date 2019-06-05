引擎语法基于Django



## 语法说明

1. 代入数据使用双花括号

   ```html
   <p>Welcome, {{user_name}}!</p>
   ```

2. 取得对象的属性或者词典的键值

   ```html
   dict.key
   obj.attr
   obj.method
   
   <p>The price is: {{product.price}}, with a {{product.discount}}% discount.</p>
   ```

3. 可以使用过滤器过滤修改数据，过滤器使用管道符号调用

   ```html
   <p>Short name: {{story.subject|slugify|lower}}</p>
   ```

4. 使用条件判断

   ```html
   {% if user.is_logged_in %}
       <p>Welcome, {{ user.name }}!</p>
   {% endif %}
   ```

5. 使用for循环

   ```python
   <p>Products:</p>
   <ul>
   {% for product in product_list %}
       <li>{{ product.name }}: {{ product.price|format_price }}</li>
   {% endfor %}
   </ul>
   ```

6. 注释

   ```python
   {# This is the best template ever! #}
   ```



## 实现方式

解析阶段最后会生成某种可直接运行的代码

渲染阶段可直接运行代码得到结果文本

Jinja2就是采用的这种方式

demo

```html
# 模板
<p>Welcome, {{user_name}}!</p>
<p>Products:</p>
<ul>
{% for product in product_list %}
    <li>{{ product.name }}:
        {{ product.price|format_price }}</li>
{% endfor %}
</ul>
```

```python
# 编译生成的函数
def render_function(context, do_dots):
    c_user_name = context['user_name']
    c_product_list = context['product_list']
    c_format_price = context['format_price']

    result = []
    append_result = result.append
    extend_result = result.extend
    to_str = str

    extend_result([
        '<p>Welcome, ',
        to_str(c_user_name),
        '!</p>\n<p>Products:</p>\n<ul>\n'
    ])
    for c_product in c_product_list:
        extend_result([
            '\n    <li>',
            to_str(do_dots(c_product, 'name')),
            ':\n        ',
            to_str(c_format_price(do_dots(c_product, 'price'))),
            '</li>\n'
        ])
    append_result('\n</ul>\n')
    return ''.join(result)
```

解释：

1. 模版都会被转换为render_function函数
2. context上下文环境存储导入的数据词典
3. do_dots存储用来取得对象属性或者词典键值
4. 从头开始分析这段代码，最开始是对输入的数据词典进行解包，得到的每个变量都使用`c_`作为前缀
5. 使用队列来存储中间结果
6. 替换数据
7. 把队列合成一个字符串作为结果文本返回



