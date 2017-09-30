## getpass

这个模块提供了两个函数: `getpass()`和`getuser()`。

使用前先引入：

```python
import getpass
```

### getpass([prompt, [stream]])

这个方法用于提示用户输入密码，并且输入的密码是不会在屏幕上显示出来的。返回值就是用户的输入值。参数`prompt`用于向用户给出提示语。`stream`默认是终端(/dev/tty)，当然，你也可以指定一个文件打开标识。

```python
In [2]: getpass.getpass('Password: ')
Password:
Out[2]: '123456'
```

### getuser()

获取当前的登录用用户。这个方法会依次查找环境变量`LOGNAME`,`USER`,`LNAME`,`USERNAME`。直到发现一个非空的值并将其作为返回值。

```python
In [7]: getpass.getuser()
Out[7]: 'pavoooo'

➜ /Users/pavoooo >echo $LOGNAME
pavoooo
➜ /Users/pavoooo >echo $USER
pavoooo
➜ /Users/pavoooo >echo $LNAME

➜ /Users/pavoooo >echo $USERNAME
pavoooo
```

在这里这个方法返回的就是环境变量`LOGNAME`的值。
