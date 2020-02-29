# 基于 Python 轻松自建 App 服务器

[toc]



项目地址：https://juejin.im/book/5ac160745188255c3200df1c/section/5ac160756fb9a028b548074c

## 01App 与后端服务器通信方法简介

### 1.学到内容：

- 腾讯云上配置开发环境 
- 基于 Tornado 的 HTTP 服务器框架 
-  App 客户端/服务器端之间的数据通信
- 服务器端对数据库 MySQL 的操作 
- 基于 Nginx 的反向代理及基于 HTTPS 的数据加密 
- 完成一款大型服务器的进阶方案和演进路线...



### 2.通信方法简介（APP客户端与服务器的通信连接）

1.短连接，http

2.长连接，socket，服务端压力比较大，一般用于游戏、服务端主动向客户端推送消息的时候比较常用

3.客户端与服务端的数据交互：json

### 3.http

#### 1.http协议：

超文本传输协议（HTTP）是一个客户端和服务器端请求和应答的标准（TCP）。通过使用 App 客户端、Web 浏览器或者其他的工具，客户端发起一个到服务器上指定端口（默认端口为 80）的 HTTP 请求
    

#### 2.get方法

##### 参数在url当中

请求特点：

            * GET 请求可被缓存
            * GET 请求保留在浏览器历史记录中
            * GET 请求可被收藏为书签
            * GET 请求不应在处理敏感数据时使用
            * GET 请求有长度限制
            * GET 请求只应当用于取回数据
        3.POST 方法



#### 3.post 请求

##### 请求的参数在请求的body当中

请求特点：

            * POST 请求不会被缓存
            * POST 请求不会保留在浏览器历史记录中
            * POST 不能被收藏为书签
   * POST 请求对数据长度没有要求



#### 4.json

轻量级的数据交换格式，键值对保存对象，必须双引号，和字典很像

GET/POST 采用键/值对的方式，信息保密性要求高些，或键/值对多些时，使用 POST 方式。



## 02学习目标（通信场景功能）

3种场景：简单的数据请求响应、图片上传加载及 H5 页面请求加载

场景一：用户注册

App 客户端发送 HTTP 请求注册用户信息，服务器端收到 HTTP 请求后，校验请求并写入数据库，返回注册成功或失败信息

场景二：图片上传加载

App 客户端发起图片上传，服务器端收到 HTTP 请求后，校验并接收图片上传，写入硬盘和数据库，并返回图片上传成功或失败信息。App 客户端根据返回的图片链接，请求加载图片。

场景三：加载 H5 页面

App 客户端用户登录，服务器端校验通过后返回首页 H5 URL，App 客户端加载请求首页页面，服务器端收到 HTTP 请求后，校验并更新数据库，返回预设的 H5 页面。 



## 03服务器端组件框架的选择与介绍

支持高并发、易扩展并真正能阐释代码简洁美的框架。

在调研了众多的 HTTP 服务器框架之后（如 Django、Pyramid），笔者最终选择了 Tornado。

简洁高效，易扩展，高并发。

著名的知乎也是建立在 Tornado 之上。

编程语言：python3.6.2

服务器框架：tornado

操作系统：centos7.2  x64

数据库：mysql，使用orm操作

服务器端整体架构框架： 


CentOS ：CentOS 是大名鼎鼎的 Red Hat 的开源版本，由 Red Hat 公司维护测试，并在 Linux 内核稳定分支上进行开发，系统相对稳定。 Red Hat 一早就在中国布局，市面上书籍众多，网上资料丰富，很多公司，第一版优先支持的版本也是 CentOS，这也是我们选择 CentOS 的原因，当出现疑难杂症时，能第一时间找到解决方案。在本次服务器端开发中，我们并不需要精通 CentOS，只需要会简单地使用 Linux 的命令即可，如 yum install 。 

MySQL：MySQL 是最流行的关系型数据库管理系统，在 Web 应用方面是最好的关系型数据库管理系统软件之一， 也是最早一批被国内用户熟知的数据库软件之一。 同样，当出现疑难杂症时，丰富的图书及网络资源能帮助我们尽快找到解决方案。

SQLAlchemy ：在操作数据（如 MySQL）的过程中，我们可以使用原生的 MySQL 语句（如insert、update、delete），也可以使用 ORM（Object Relational Mapping）的方式。简单来说，可以使用第三方软件来操作数据库，使用第三方的好处是很多底层 MySQL 的命令被封装成简单的API暴露给用户，并提供强大的整合功能。当然坏处也有，如相对于原生命令效率低些，学习成本高些。而选择 SQLAlchemy 的原因是其使用 Pythonic 的代码风格，在本小册中不会给读者增加太多学习成本，另外，SQLAlchemy 全面的 API 参考文档也是我们选择它的原因之一。 

Tornado ：Tornado 作为我们选用的 HTTP 服务器框架，在后续的章节中，我们将作详尽的诠释。

## 04基于腾讯云的服务器端环境搭建



在不区分软硬件的情况下，服务器端开发需要准备的环境主要有如下几个： 

- 服务器：服务器端代码开发及执行环境； 
-  Linux 虚拟终端软件：登录服务器，并编辑和执行服务器端代码，推荐 secureCRT； 
- 代码编辑器：通过 FTP/SFTP 获取服务器端代码并编写代码的工具。 

下面分别展开介绍及配置

### 1.选择云服务器：

我这里使用本人购买的腾讯云服务器。

### 2.Linux虚拟终端软件：Xshell

### 3.配置开发环境

安装： Python 3、Tornado、MySQL 和 SQLAlchemy

#### 1.安装依赖包：

```shell
yum -y groupinstall "Development tools" 
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```



#### 2.安装python部分

```shell
下载python3.6.2: wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz
创建安装目录: mkdir /usr/local/python3

安装 gcc

由于 Python 3.6.2 的编译需要编译环境，故需安装 gcc。
yum -y install gcc

安装 Python 3.6.2 
解压 Python 3.6.2 并安装在 /usr/local/python3 目录下。 
tar -xvJf Python-3.6.2.tar.xz
cd Python-3.6.2
./configure --prefix=/usr/local/python3
make && make install
创建软连
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
测试 python3
```



#### 3.安装tornado部分

CentOS 下还无法直接使用 yum install tornado，但可以使用 pip 安装 Tornado。

先执行 pip3 install --upgrade pip 命令升级 pip，再执行 pip3 install tornado 命令安装 Tornado。

检测tornado是否安装成功， 执行 import tornado 没有报错，表示 Tornado 已安装成功。

#### 4.安装mysql

```shell
yum install mysql-devel
wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
rpm -ivh mysql-community-release-el7-5.noarch.rpm
yum -y install mysql-community-server
pip3 install mysqlclient service mysqld restart
```



安装 MySQL 会比较久，大概 10 分钟左右，当看到 “Complete!” 后，表示安装成功。
测试 MySQL 安装是否成功： 

#### 5.安装 SQLAlchemy

使用 pip3 安装 SQLAlchemy：
pip3 install SQLAlchemy

测试 SQLAlchemy 是否安装成功，服务器端依次输入如下命令。

```python
python3
import sqlalchemy
```



#### 6.代码编辑器 Notepad++

配置 Notepad++ Notepad++ 下载下来后，并不能立即通过 SFTP 的方法从远端服务器拉取源代码到本地计算机进行编辑，还需要安装 NppFTP 来实现这个功能。 

安装远程编辑功能插件 NppFTP 

打开 Notepad++，依次选择“插件” -> “Plugin Manager” -> “Show Plugin Manager”，找到NppFTP。 

配置远程远端服务器

打开 NppFTP 插件面板 

配置远程服务器

本小册的后续所有代码将存放在远程服务器的 data 目录下，这里配置服务器端目录时，直接拉取 data 目录。



获取远端目录文件

首先我们在服务器的 data 目录下，创建 demo 目录，并使用 Notepad++ 拉取该目录。





#### 7.上传下载远端目录文件

安装 lrzsz，lrzsz 包的 rz 命令能支持从本地 Windows 上传小文件到远端服务器，而 sz 命令支持从远端服务器下载小文件到本地 Windows 上。

```shell
常用参数 
    -b：以二进制方式，默认为文本方式（Binary (tell it like it is) file transfer override.）
    -e：对所有控制字符转义（Force sender to escape all control characters; normally XON, XOFF, DLE, CR-@-CR, and Ctrl-X are escaped.）
```



如果要保证上传的文件内容在服务器端保存之后与原始文件一致，最好同时设置这两个标志，如下所示方式使用：
rz -be

至此，我们已完成了服务器端的环境搭建。



## 05基于 Tornado 的 HTTP 服务器简介及代码组织框架

Tornado 是一个 Python Web 框架和异步网络库，最初是在 FriendFeed 开发的。通过使用非阻塞网络I/O，Tornado 可以扩展到数以万计的开放连接，但却在创建和编写时足够的轻量级。

### 1.Tornado 的特点 



Tornado 和现在的很多主流 Web 服务器框架（包括大多数 Python 框架）有着明显的区别：它是非阻塞式异步服务器。大多数社交网络应用都会展示实时更新来提醒新消息、状态变化以及用户通知，客户端需要保持一个打开的连接来等待服务器端的任何响应。这些长连接或推送请求使得非异步服务器线程池迅速饱和。一旦线程池的资源耗尽，服务器将不能再响应新的请求。异步服务器在这一场景中的应用则不同，当负载增加时，诸如 Tornodo 这样的服务器，会把当前请求正在等待来自其他资源的数据，加以控制并挂起请求，以满足新的请求。这也是 Tornado 在高并发、高效率的 Web 服务器应用很广的原因之一。

### 2.Tornado 入门 

编写 Hello, world 

在服务器上任意目录下（如 /data ），创建 hello.py 文件，输入如下代码：

```python
import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([ (r"/", MainHandler), ])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```



编写一个 Tornado 应用中最多的工作是定义类继承 Tornado 的 RequestHandler 类。在这个例子中，我们创建了一个简单的应用，Tornado 监听给定的端口 8888，并在根目录（"/"）响应请求，响应的处理方法为继承了 RequestHandler 的 MainHandler 类。在 MainHandler 中返回 Hello, world。

测试代码：

注：

- 服务器上需要放开 8888 端口，如果是公有云云主机，注意安全组配置是否已放开。
- 至此，我们已完成基于 Tornado 服务器的 Hello, world。下面来简单介绍一下 Tornado 的整体框架。



### 3.Tornado 框架 



Tornado 大体上可以被分为 4 个主要的部分: 

- Web 框架 (包括创建 Web 应用的 RequestHandler 类，还有很多其他支持的类)； 

- HTTP的客户端和服务端实现 (HTTPServer and AsyncHTTPClient)；

- 异步网络库 (IOLoop and IOStream), 为HTTP组件提供构建模块，也可以用来实现其他协议； 

- 协程库 (tornado.gen) 允许异步代码写得更直接而不用链式回调的方式。 





这里只做简单的了解，如需深入了解 Tornado，建议读者通读学习 Tornado 官方文档（http://tornado-zh.readthedocs.io/zh/latest/guide.html）。 

代码组织框架 :在某个目录下，创建本次的工程文件，如 demo，并依次创建如下文件： 

目录及文件说明

    common：存放公共类和方法 conf: 存放配置文件 
    log：存放相关日志 
    static：存放静态文件，如样式（CSS）、脚本（js）、图片等 
    templates：公用模板目录，主要存放 HTML 文件 
    views：视图函数，业务逻辑代码目录
    main.py：Tornado 主程序入口 
    models.py：数据库表结构定义




## 06第一次数据请求，服务器接收用户注册信息

现在假设有这样一个 App（见下图），用户需要通过该界面提交注册信息。服务器端在接收到客户端的注册请求后，返回注册成功信息，并将该用户写入数据库表用户信息中。 

### 1.客户端模拟

    使用发包工具：postman或者getman（https://getman.cn/） 约定服务器端 HTTP server 的端口号为 8000，服务器端和客户端定义的请求是 /user/regist，那么完整的 URL 为 http://123.206.44.189:8000/users/regist?（请用自己的云虚拟机 IP 替换其中的 IP）。 参数为手机号（phone）、密码（password）及验证码（code），参数放入 HTTP 的 body 中，具体为： {"phone":"18866668888","password":"demo123456","code":"123456"}
注：
- 确保服务器端 8000 端口已放通；

- 在实际的项目中，密码不会明文的传输，一般会在客户端先使用 md5 进行加密，服务器端存储的也是加密后的密码字符串。本小册作为学习示例，将使用明文讲解。

发包器模拟如下： 客户端的请求至此已初步完成，现在，服务器端接收到客户端这个请求后，将如何处理呢？

### 2.服务器端处理


客户端以 POST 的方式，发送注册请求至服务器端，请求进入服务器端的 main.py 后，将调用 url_router 转发到 users_url.py 中，在 users_urls.py 中，对应的 URL 将调用 users_views.py 的 RegistHandle 类， RegistHandle 为真正的代码处理逻辑，在校验用户信息正确的情况下，返回 JSON 格式的注册成功信息给客户端。
编写服务器端入口函数

main.py 是 Tornado 作为 HTTP 服务器的统一入口，根据前面的约定，Tornado 对外服务的端口号为 8000。

```python
import tornado.ioloop
import tornado.web
import os
import sys
from tornado.options
import define,options
class Application(tornado.web.Application):
    def __init__(self): #定义 Tornado 服务器的配置项，如 static/templates 目录位置、debug 级别等
        settings = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__),"static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates")
            )
        tornado.web.Application.__init__(self, **settings)
    
if __name__ == '__main__':
    print ("Tornado server is ready for service\r")
    tornado.options.parse_command_line()
    Application().listen(8000, xheaders=True)
    tornado.ioloop.IOLoop.instance().start()
```



未完待续（https://juejin.im/book/5ac160745188255c3200df1c/section/5ac8458951882555627d88e2）