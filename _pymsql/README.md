## PyMySQL

`PyMySQL`是python用于操作`mysql`的一个模块。

### 安装

```bash
pip install PyMySQL
```
安装成功后，在需要使用的文件中引入。

```python
import pymsql
```
### 连接数据库

`pymysql`提供的api并不是很多，所以学习起来是比较方便的。在操作数据库之前，我们需要先连接数据库，连接数据库的基本语法如下：

```python
connection = pymysql.connect(
    host = '数据库服务器所在的域名,'
    user = '连接数据库所用的用户,'
    password = '连接数据库所用的密码,'
    database = '数据库连接成功的时候使用的数据库,'
    port = '连接数据库的端口'
    charset = '连接数据库使用的编码'
    autocommit = '布尔值，是否自动提交事务'
    db = 'database的别名'
    passwd = 'password的别名'
)
```

比如：

```python
connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    db = 'py_explore',
    port = 3306,
    charset = 'utf8'
)
```

连接成功后，返回一个数据库连接对象，这个对象中包含了一些操作数据库的方法。

#### connection.autocommit_mode

设置自动提交的模式，会覆盖默认值。默认是`False`。比如，向数据库中插入一条语句：

```python
with connection.cursor() as cursor:
    sql = 'insert into `users` (`email`, `password`) values (%s, %s)'
    cursor.execute(sql, ('pavoooo@163.com','2json'))
```
从数据库查询：

```mysql
select * from users
```

![](http://ww1.sinaimg.cn/large/006FmM8yly1fjzk732t3lj30ev01h749.jpg)

虽然语句之行成功，但是数据没有插入到数据库中，这就是因为`pymsql`默认是不自动提交更新的。把代码改成下面这样：

```python
connection.autocommit_mode = True
with connection.cursor() as cursor:
    sql = 'insert into `users` (`email`, `password`) values (%s, %s)'
    cursor.execute(sql, ('pavoooo@163.com','2json'))
```
按道理来说，这个操作应该能够让语句插入到数据库中，但是，经笔者实验，数据并不能够成功插入到数据库。但是我们如果在连接数据库的时候，指定`autocommit`的值为`true`。则这个值也是`true`，而且数据能够成功的插入到数据库中。所以笔者猜测，难道这个值是只读的？（希望有人能够指正）。

#### connection.begin()
开始一个事务操作

#### connection.rollback()
回滚数据库的更改，不仅仅只包括事务的操作。

```python
# 开启一个事务
connection.begin()
#向数据库中插入几条语句
for i in range(5):
     with connection.cursor() as cursor:
         sql = 'insert into `users` (`email`, `password`) values (%s, %s)'
         cursor.execute(sql, ('pavoooo@163.com','2json'))
```
我们执导这个时候数据是没有插入到数据库中的。下面进行回滚操作，然后`commit()`，但是数据库中仍是没有刚才插入的几条语句。注意，不管有没有使用`connection.begin()`开启一个事务，在`connection.commit()`之前进行`connection.rollback()`操作，数据库的更改都不会成功保存到数据中。

```python
In [11]: connection.rollback()
In [12]: connection.commit()
```

![](http://ww1.sinaimg.cn/large/006FmM8yly1fjzkptoemzj30jn04nglx.jpg)

#### connection.commit()
提交数据库的更改

#### connection.cursor()
创建一个游标，返回一个游标对象，这个对象包含了一些操作数据库的方法。下面会详细讲解。

#### connection.ping()
检查mysql服务器是否可用。

```python
connection.ping()
```

```python
Out[16]: <pymysql.connections.OKPacketWrapper at 0x7f078804ae10>
```
说明可用。

#### connection.select_db(dbName)
选择数据库，会覆盖连接数据库的时候所指定的值。比如：

```python
connection.select_db('test')
with connection.cursor() as cursor:
    sql = 'select * from users'
    cursor.execute(sql)
```
报错，说明数据库更改成功了。

```python
ProgrammingError: (1146, u"Table 'test.users' doesn't exist")
```

#### connection.show_warnings()
显示数据库操作的警告和错误。

#### connection.close()
关闭数据库连接

### 游标对象
游标对象包含了操作数据库的一些方法。可以通过下面两种方式获取游标对象。

```python
cursor = connection.cursor()
```

```python
with connection.cursor() as cursor:
    # ...
```

#### ursor.execute(query, args=None)
这个方法上面已经用到过，主要是用于执行一个sql语句，args要是用于想query传递参数。args可以是tuple，list或者一个map对象。如果是list或者tuple，则query可以使用%s进行占位，如果是一个map则query可以使用%(name)s进行占位。返回的值是本次操作所影响的行数。

#### cursor.fetchall()
获取查询出的全部的数据。

```python
cursor.execute('select * from users')
cursor.fetchall()
```
结果是：

```python
(
    (13, u'pavoooo@163.com', u'2json'),
    (14, u'pavoooo@163.com', u'2json'),
    (15, u'pavoooo@163.com', u'2json'),
    (16, u'pavoooo@163.com', u'2json'),
    (17, u'pavoooo@163.com', u'2json')
 )
```

#### cursor.fetchone()
获取一条数据。

```python
cursor.execute('select * from users')
cursor.fetchone()
```
结果是：

```python
(13, u'pavoooo@163.com', u'2json')
```


#### cursor.fetchmany(size=None)
获取多行数据。

```python
cursor.execute('select * from users')
cursor.fetchmany(3)
```
结果是：

```python
(
    (13, u'pavoooo@163.com', u'2json'),
    (14, u'pavoooo@163.com', u'2json'),
    (15, u'pavoooo@163.com', u'2json')
 )
```

#### connection.close()
用语关闭一个游标对象。