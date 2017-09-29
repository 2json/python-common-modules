## json
`json`模块是`python`提供的用于操作`json`数据的一个标准模块。`json`模块提供了一种十分简单的方式来编码和解码`JSON`数据。我们掌握以下四个方法，就能够满足解决大部分`json`操作的问题了。

同样的，在使用之前需要先引入这个模块。

```python
import json
```

### json.dumps()
这个方法主要是用于将`python`中的`json`数据结构转换为对应内容的字符串。如：

```python
import json

data = {
  'name': 'ACME',
  'shares': 100,
  'price': 524.23
}

print json.dumps(data)
```
运行上面的代码会输出：

```python
'{"price": 524.23, "name": "ACME", "shares": 100}'
```

### json.loads()
这个方法主要是将`json`字符串转化为对应的`python`数据结构。如：

```python
json_str = '{"price": 524.23, "name": "ACME", "shares": 100}'
print json.loads(json_str)
```

结果是：

```python
{u'price': 524.23, u'name': u'ACME', u'shares': 100}
```

上面的两个方法都是针对`python`中的变量进行处理的，如果你想处理保存在文件中的python数据，可以使用下面两个方法。

### json.load(f)
这个方法接受一个文件描述符作为参数，读取其中的内容，并将其作为`json`格式输出。如：

```python
with open('package.json', 'r') as f:
  print json.load(f)
```

结果是：

```python
{u'engines': {u'node': u'4.4.7', u'npm': u'2.15.9'}, u'license': u'private', u'repository': u'https://github.com/metabase/metabase', u'description': u'Metabase Analytics Report Server', u'private': True, u'version': u'0.0.0', u'dependencies': {u'babel-polyfill': u'^6.6.1', u'ace-builds': u'^1.2.2'}, u'devDependencies': {u'babel-core': u'^6.20.0', u'add-asset-html-webpack-plugin': u'^2.1.0', u'babel-cli': u'^6.11.4', u'@slack/client': u'^3.5.4'}, u'name': u'metabase'}
```

### json.dump(data, f)
这个方法主要是用于将一个`json`内容写入到`f`所对应的文件中。

```python
with open('package.json', 'w') as f:
  json.dump(datas s, f)
```

上面的这四个基本的方法，已经满足我们大部分的需求了。但是，对于这些方法还有一些可以拓展的部分。

> 在python中，json模块所支持的编码格式的基本类型为`None`，`bool`，`int`，`float`，`str`，以及包含这些类型数据的`list`，`tuple`，`dict`等。对于`dict`类型的数据，键需要是字符串的类型(对于非字符串的类型会先转化为字符串的类型)。但是，为了遵循主流的`JSON`规范，我们应该只使用json模块来操作`list`和`dict`。

如，下面的这些操作都是允许的，但是都不推荐：

 ```python
 In [9]: json.dumps(False)
 Out[9]: 'false'

 In [10]: json.dumps(None)
 Out[10]: 'null'

 In [11]: json.dumps((1,2,3))
 Out[11]: '[1, 2, 3]'

 In [12]: json.dumps(1)
 Out[12]: '1'

 In [13]: json.dumps(1.1)
 Out[13]: '1.1'

 In [14]: json.dumps('hello')
 Out[14]: '"hello"'
 ```
同样，我们也可以通过`json.loads()`方法，将上述输出的数据转化为对应的python数据结构。

> 在我们编码json数据的时候，还有一些很有用的选项。比如，`indent`可以控制格式化输出，`sort_keys`可以控制输出的时候排序键的值。

下面是一些常用的参数：

* `skipkeys`: 默认是`False`。如果设置为`True`，则当`dict`的key不是基本数据类型`(str, unicode, int, long, float, bool, None)`的时候，会跳过，而不是抛出一个`TypeError`

```python
data = {
  (1,2,3): 'tuple type',
  'name': 'string type'
}

print json.dumps(data)  # TypeError: keys must be a string
```

```python
data = {
  (1,2,3): 'tuple type',
  'name': 'string type'
}

print json.dumps(data, skipkeys=True)
```
结果是:

```python
{"name": "string type"}
```

* `ensure_ascii`: 默认是`True`。表示在输出的的结果中，只包含被转义之后的`\uxxxx`的数据。设置为`False`表示可能会包含一些`unicode`类型的字符串。这个参数在输出为乱码的时候经常用到。

* `check_circular`: 默认是`True`。表示会跳过循环引用的结果，如果设置为`False`会抛出一个`OverflowError`异常。

* `indent`: 控制格式化输出时候的缩进。

```python
data = {'a': 1, 'b': 2}
json.dumps(data)
```

```python
{
  'a': 1,
  'b': 2
}
```

* `sort_keys`: 默认`True`。是否对输出的`dict`的`key`进行排序。

* `separators`: 指定分隔符，两个参数，第一个参数是不同元素之间的分隔符，第二个参数是键值对之间的分隔符。
