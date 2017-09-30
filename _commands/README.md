## commands
`commands`是对`os.poen()`方法的封装，系统命令以字符串的形式传入到方法中。方法的返回值是命令行的输出，也可以选择输出命令的退出吗。

`commands`模块具有下面的一些方法：

`commands.getstatusoutput(cmd)`: 使用`os.popen()`方法执行一个shell命令，返回值是一个元组`(status, output)`。`cmd`实际上以`{ cmd; } 2>&1`进行了错误的重定向，以便出错的时候能够将错误的信息包含在返回值中。

`commands.getoutput(cmd)`: 同`getstatusoutput()`方法，只是返回值中不包含退出码。

`commands.getstatus(file)`: 命令`ls -ld file`的简写，内部使用了`getoutput()`方法。

例子：
```python
# 使用前先引入
import commands

# stdout
In [3]: commands.getstatusoutput('ls /bin/ls')
Out[3]: (0, '/bin/ls')

# stderr
In [4]: commands.getstatusoutput('cat ./hello')
Out[4]: (256, 'cat: ./hello: No such file or directory')

In [5]: commands.getoutput('ls /bin/ls')
Out[5]: '/bin/ls'

In [6]: commands.getstatus('/bin/ls')
Out[6]: '-rwxr-xr-x  1 root  wheel  38512 10 18  2015 /bin/ls'

# result is the same as above
In [7]: ls -ld /bin/ls
-rwxr-xr-x  1 root  wheel  38512 10 18  2015 /bin/ls*
```
