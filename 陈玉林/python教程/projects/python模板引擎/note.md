参考资料：

1.  <https://zhuanlan.zhihu.com/p/27277032>
2. <https://www.shiyanlou.com/courses/583/labs/1936/document/>



## 语法说明

1. 代入数据使用双花括号

   ```html
   <p>Welcome, {{user_name}}!</p>
   ```

2. 取得对象的属性或者词典的键值[todo]

   ```html
   dict.key
   obj.attr
   obj.method
   
   <p>The price is: {{product.price}}, with a {{product.discount}}% discount.</p>
   ```

3. 可以使用过滤器过滤修改数据，过滤器使用管道符号调用[todo]

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
       <li>{{ product.name }}: {{ format_price }}</li>
   {% endfor %}
   </ul>
   ```

6. 注释

   ```python
   {# This is comment! #}
   ```



## 实现方式

解析阶段最后会生成某种可直接运行的代码

渲染阶段可直接运行代码得到结果文本

Jinja2就是采用的这种方式

demo

```html
# 模板
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
```

```python
# 编译生成的函数
def render_function():
    result = []
    result.extend(['<h1>',str(name),'</h1>'])
    if a > b:
        result.extend(['<span>a greater then b</span>'])
    elif a < b:
        result.extend(['<span>a less then b</span>'])
    else:
        result.extend(['<span>a equals to b</span>'])
    result.extend(['<div>test test test</div>'])
    if False:
        result.extend(['<strong>this will not appear</strong>'])
    result.extend(['<span>-----------------</span>'])
    for v in values:
        result.extend(['<li>fruit:',str(v),'</li>'])
        if v == 'pear':
            break
    return "".join(result)

```



