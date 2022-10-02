# Learn-MongoDB

## 简介

> MongoDB 是一个基于分布式文件存储的数据库。由 C++ 语言编写。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。

> MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。


## NOSQL

> NoSQL(NoSQL = Not Only SQL )

-   NoSQL，指的是非关系型的数据库。NoSQL有时也称作Not Only SQL的缩写，是对不同于传统的关系型数据库的数据库管理系统的统称。

-   NoSQL用于超大规模数据的存储。（例如谷歌或Facebook每天为他们的用户收集万亿比特的数据）。这些类型的数据存储不需要固定的模式，无需多余操作就可以横向扩展。

> RDBMS 

- 高度组织化结构化数据 
- 结构化查询语言（SQL） (SQL) 
- 数据和关系都存储在单独的表中。 
- 数据操纵语言，数据定义语言 
- 严格的一致性
- 基础事务

> NoSQL 

- 代表着不仅仅是SQL
- 没有声明性查询语言
- 没有预定义的模式
-键 - 值对存储，列存储，文档存储，图形数据库
- 最终一致性，而非ACID属性
- 非结构化和不可预知的数据
- CAP定理 
- 高性能，高可用性和可伸缩性

## 关系型数据库 ACID

## CAP 定理

-   一致性(Consistency) (所有节点在同一时间具有相同的数据)
-   可用性(Availability) (保证每个请求不管成功或者失败都有响应)
-   分隔容忍(Partition tolerance) (系统中任意信息的丢失或失败不会影响系统的继续运作)

```sh
# CAP理论的核心是：一个分布式系统不可能同时很好的满足一致性，可用性和分区容错性这三个需求，最多只能同时较好的满足两个。

# 因此，根据 CAP 原理将 NoSQL 数据库分成了满足 CA 原则、满足 CP 原则和满足 AP 原则三 大类：

1、CA - 单点集群，满足一致性，可用性的系统，通常在可扩展性上不太强大。
2、CP - 满足一致性，分区容忍性的系统，通常性能不是特别高。
3、AP - 满足可用性，分区容忍性的系统，通常可能对一致性要求低一些。
```

![](https://i.loli.net/2019/01/17/5c3ffc29279e9.png)

## 分布式计算的优点

-   可靠性（容错） ：

    分布式计算系统中的一个重要的优点是可靠性。一台服务器的系统崩溃并不影响到其余的服务器。

-   可扩展性：

    在分布式计算系统可以根据需要增加更多的机器。

-   资源共享：

    共享数据是必不可少的应用，如银行，预订系统。

-   灵活性：

    由于该系统是非常灵活的，它很容易安装，实施和调试新的服务。

-   更快的速度：

    分布式计算系统可以有多台计算机的计算能力，使得它比其他系统有更快的处理速度。

-   开放系统：

    由于它是开放的系统，本地或者远程都可以访问到该服务。

-   更高的性能：

    相较于集中式计算机网络集群可以提供更高的性能（及更好的性价比）。

## BASE

> BASE是NoSQL数据库通常对可用性及一致性的弱要求原则:

-   Basically Availble --基本可用
-   Soft-state --软状态/柔性事务。 "Soft state" 可以理解为"无连接"的, 而 "Hard state" 是"面向连接"的
-   Eventual Consistency -- 最终一致性， 也是是 ACID 的最终目的。

## ACID vs BASE

<table class="reference"><tbody><tr><th>ACID</th><th>BASE</th></tr><tr><td>原子性(<strong>A</strong>tomicity)</td><td>基本可用(<strong>B</strong>asically<strong>A</strong>vailable)</td></tr><tr><td>一致性(<strong>C</strong>onsistency)</td><td>软状态/柔性事务(<strong>S</strong>oft state)</td></tr><tr><td>隔离性(<strong>I</strong>solation)</td><td>最终一致性(<strong>E</strong>ventual consistency)</td></tr><tr><td>持久性(<strong>D</strong>urable)</td><td>&nbsp;</td></tr></tbody></table>

## NoSQL 数据库分类

<table class="reference"><tbody><tr><td>类型</td><td>部分代表<p></p></td><td>特点</td></tr><tr><td>列存储</td><td><p><span style="font-size:14px;font-family:宋体;">Hbase</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p><p><span style="font-size:14px;font-family:宋体;">Cassandra</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p><p><span style="font-size:14px;font-family:宋体;">Hypertable</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td><td><p><span style="font-size:14px;font-family:宋体;">顾名思义，是按列存储数据的。最大的特点是方便存储结构化和半结构化数据，方便做数据压缩，对针对某一列或者某几列的查询有非常大的IO优势。</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td></tr><tr><td><p><span style="font-size:14px;font-family:宋体;">文档存储</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td><td><p><span style="font-size:14px;font-family:宋体;">MongoDB</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p><p><span style="font-size:14px;font-family:宋体;">CouchDB</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td><td><p><span style="font-size:14px;font-family:宋体;">文档存储一般用类似json的格式存储，存储的内容是文档型的。这样也就有机会对某些字段建立索引，实现关系数据库的某些功能。</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td></tr><tr><td><p><span style="font-size:14px;font-family:宋体;">key-value存储</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td><td><p><span style="font-size:14px;font-family:宋体;">Tokyo&nbsp;Cabinet&nbsp;/&nbsp;Tyrant</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p><p><span style="font-size:14px;font-family:宋体;">Berkeley&nbsp;DB</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p><p><span style="font-size:14px;font-family:宋体;">MemcacheDB</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p><p><span style="font-size:14px;font-family:宋体;">Redis</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td><td><p><span style="font-size:14px;font-family:宋体;">可以通过key快速查询到其value。一般来说，存储不管value的格式，照单全收。（Redis包含了其他功能）</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td></tr><tr><td><p><span style="font-size:14px;font-family:宋体;">图存储</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td><td><p><span style="font-size:14px;font-family:宋体;">Neo4J</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p><p><span style="font-size:14px;font-family:宋体;">FlockDB</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td><td><p><span style="font-size:14px;font-family:宋体;">图形关系的最佳存储。使用传统关系数据库来解决的话性能低下，而且设计使用不方便。</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td></tr><tr><td><p><span style="font-size:14px;font-family:宋体;">对象存储</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td><td><p><span style="font-size:14px;font-family:宋体;">db4o</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p><p><span style="font-size:14px;font-family:宋体;">Versant</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td><td><p><span style="font-size:14px;font-family:宋体;">通过类似面向对象语言的语法操作数据库，通过对象的方式存取数据。</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td></tr><tr><td><p><span style="font-size:14px;font-family:宋体;">xml数据库</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td><td><p><span style="font-size:14px;font-family:宋体;">Berkeley&nbsp;DB&nbsp;XML</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p><p><span style="font-size:14px;font-family:宋体;">BaseX</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td><td><p><span style="font-size:14px;font-family:宋体;">高效的存储XML数据，并支持XML的内部查询语法，比如XQuery,Xpath。</span><span style="font-size:12.0000pt;font-family:'宋体';"></span></p></td></tr></tbody></table>


## MongoDB 主要特点

-   MongoDB 是一个**面向文档**存储的数据库，操作起来比较简单和容易。
-   你可以在MongoDB记录中设置任何属性的索引 (如：FirstName="Sameer",Address="8 Gandhi Road")来实现更快的排序。
-   你可以通过本地或者网络创建数据镜像，这使得MongoDB有更强的扩展性。
-   如果负载的增加（需要更多的存储空间和更强的处理能力） ，它可以分布在计算机网络中的其他节点上这就是所谓的分片。
-   Mongo支持丰富的查询表达式。查询指令使用JSON形式的标记，可轻易查询文档中内嵌的对象及数组。
-   MongoDb 使用update()命令可以实现替换完成的文档（数据）或者一些指定的数据字段 。
-   Mongodb中的Map/reduce主要是用来对数据进行批量处理和聚合操作。
-   Map和Reduce。Map函数调用emit(key,value)遍历集合中所有的记录，将key与value传给Reduce函数进行处理。
-   Map函数和Reduce函数是使用Javascript编写的，并可以通过db.runCommand或mapreduce命令来执行MapReduce操作。
-   GridFS是MongoDB中的一个内置功能，可以用于存放大量小文件。
-   MongoDB允许在服务端执行脚本，可以用Javascript编写某个函数，直接在服务端执行，也可以把函数的定义存储在服务端，下次直接调用即可。
-   MongoDB支持各种编程语言:RUBY，PYTHON，JAVA，C++，PHP，C#等多种语言。
-   MongoDB安装简单。

## SQL 和 MongoDB 對應的概念

<table class="reference"><tbody><tr><th>SQL术语/概念</th><th>MongoDB术语/概念</th><th>解释/说明</th></tr><tr><td>database</td><td>database</td><td>数据库</td></tr><tr><td>table</td><td>collection</td><td>数据库表/集合</td></tr><tr><td>row</td><td>document</td><td>数据记录行/文档</td></tr><tr><td>column</td><td>field</td><td>数据字段/域</td></tr><tr><td>index</td><td>index</td><td>索引</td></tr><tr><td>table joins</td><td>&nbsp;</td><td>表连接,MongoDB不支持</td></tr><tr><td>primary key</td><td>primary key</td><td>主键,MongoDB自动将_id字段设置为主键</td></tr></tbody></table>

## 自有数据库

-   admin： 从权限的角度来看，这是"root"数据库。要是将一个用户添加到这个数据库，这个用户自动继承所有数据库的权限。一些特定的服务器端命令也只能从这个数据库运行，比如列出所有的数据库或者关闭服务器。
-   local: 这个数据永远不会被复制，可以用来存储限于本地单台服务器的任意集合
-   config: 当Mongo用于分片设置时，config数据库在内部使用，用于保存分片的相关信息。

### 数据库命名规范

-   不能是空字符串（"")。
-   不得含有' '（空格)、.、$、/、\和\0 (空字符)。
-   **应全部小写。**
-   最多64字节。

## 文档(Documents)

文档是一组键值(key-value)对(即BSON)

### 命名规范

-   键不能含有\0 (空字符)。这个字符用来表示键的结尾。
-   .和$有特别的意义，只有在特定环境下才能使用。
-   以下划线"_"开头的键是保留的(不是严格要求的)。

## 集合(Collection)

-   集合名不能是空字符串""。
-   集合名不能含有\0字符（空字符)，这个字符表示集合名的结尾。
-   集合名不能以"system."开头，这是为系统集合保留的前缀。
-   用户创建的集合名字不能含有保留字符。有些驱动程序的确支持在集合名里面包含，这是因为某些系统生成的集合中包含该字符。除非你要访问这种系统创建的集合，否则千万不要在名字里出现$。

### **capped collections**

>   Capped collections 就是固定大小的collection。

-   capped collection 中，你能添加新的对象。
-   能进行更新，然而，对象不会增加存储空间。如果增加，更新就会失败 。
-   使用 Capped Collection 不能删除一个文档，可以使用 drop() 方法删除 collection 所有的行。
-   删除之后，你必须显式的重新创建这个 collection。
-   在32bit机器中，capped collection 最大存储为 1e9( 1X109)个字节。

## 元数据

在MongoDB数据库中名字空间 `<dbname>.system.*` 是包含多种系统信息的特殊集合(Collection)，如下:

<table class="reference"><tbody><tr><th>集合命名空间</th><th>描述</th></tr><tr><td>dbname.system.namespaces</td><td>列出所有名字空间。</td></tr><tr><td>dbname.system.indexes</td><td>列出所有索引。</td></tr><tr><td>dbname.system.profile</td><td>包含数据库概要(profile)信息。</td></tr><tr><td>dbname.system.users</td><td>列出所有可访问数据库的用户。</td></tr><tr><td>dbname.local.sources</td><td>包含复制对端（slave）的服务器信息和状态。</td></tr></tbody></table>

### 对于修改系统集合中的对象有如下限制。

-   在{{system.indexes}}插入数据，可以创建索引。但除此之外该表信息是不可变的(特殊的drop index命令将自动更新相关信息)。

-   {{system.users}}是可修改的。 {{system.profile}}是可删除的。

## 数据类型

<table class="reference"><tbody><tr><th>数据类型</th><th>描述</th></tr><tr><td>String</td><td>字符串。存储数据常用的数据类型。在MongoDB中，UTF-8编码的字符串才是合法的。</td></tr><tr><td>Integer</td><td>整型数值。用于存储数值。根据你所采用的服务器，可分为32位或64位。</td></tr><tr><td>Boolean</td><td>布尔值。用于存储布尔值（真/假）。</td></tr><tr><td>Double</td><td>双精度浮点值。用于存储浮点值。</td></tr><tr><td>Min/Max keys</td><td>将一个值与BSON（二进制的JSON）元素的最低值和最高值相对比。</td></tr><tr><td>Array</td><td>用于将数组或列表或多个值存储为一个键。</td></tr><tr><td>Timestamp</td><td>时间戳。记录文档修改或添加的具体时间。</td></tr><tr><td>Object</td><td>用于内嵌文档。</td></tr><tr><td>Null</td><td>用于创建空值。</td></tr><tr><td>Symbol</td><td>符号。该数据类型基本上等同于字符串类型，但不同的是，它一般用于采用特殊符号类型的语言。</td></tr><tr><td>Date</td><td>日期时间。用UNIX时间格式来存储当前日期或时间。你可以指定自己的日期时间：创建Date对象，传入年月日信息。</td></tr><tr><td>Object ID</td><td>对象ID。用于创建文档的ID。</td></tr><tr><td>Binary Data</td><td>二进制数据。用于存储二进制数据。</td></tr><tr><td>Code</td><td>代码类型。用于在文档中存储JavaScript代码。</td></tr><tr><td>Regular expression</td><td>正则表达式类型。用于存储正则表达式。</td></tr></tbody></table>

### ObjectId

ObjectId 类似唯一主键，可以很快的去生成和排序，包含 12 bytes，含义是：

-   前 4 个字节表示创建 unix 时间戳,格林尼治时间 UTC 时间，比北京时间晚了 8 个小时
-   接下来的 3 个字节是机器标识码
-   紧接的两个字节由进程 id 组成 PID
-   最后三个字节是随机数

![](https://i.loli.net/2019/01/17/5c403d687e826.png)

### 字符串

> BSON 字符串都是 UTF-8 编码

### 时间戳

-   BSON 有一个特殊的时间戳类型用于 MongoDB 内部使用，与普通的 日期 类型不相关。 时间戳值是一个 64 位的值。其中：

-   前32位是一个 time_t 值（与Unix新纪元相差的秒数）
-   后32位是在某秒中操作的一个递增的序数
-   在单个 mongod 实例中，时间戳值通常是唯一的。

-   在复制集中， oplog 有一个 ts 字段。这个字段中的值使用 BSON 时间戳表示了操作时间。


### 日期

-   日期类型

```js
> var mydate1 = new Date()     //格林尼治时间
> mydate1
ISODate("2018-03-04T14:58:51.233Z")
> typeof mydate1
object

// or

> var mydate2 = ISODate() //格林尼治时间
> mydate2
ISODate("2018-03-04T15:00:45.479Z")
> typeof mydate2
object
```

-   时间类型

```js
> var mydate1str = mydate1.toString()
> mydate1str
Sun Mar 04 2018 14:58:51 GMT+0000 (UTC) 
> typeof mydate1str
string

// or

> Date()
Sun Mar 04 2018 15:02:59 GMT+0000 (UTC)   
```

## MongoDB 连接

`mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
`

-   mongodb:// 这是固定的格式，必须要指定。

-   username:password@ 可选项，如果设置，在连接数据库服务器之后，驱动都会尝试登陆这个数据库

-   host1 必须的指定至少一个host, host1 是这个URI唯一要填写的。它指定了要连接服务器的地址。如果要连接复制集，请指定多个主机地址。

-   portX 可选的指定端口，如果不填，默认为27017

-   /database 如果指定username:password@，连接并验证登陆指定数据库。若不指定，默认打开 test 数据库。

-   ?options 是连接选项。如果不使用/database，则前面需要加上/。所有连接选项都是键值对name=value，键值对之间通过&或;（分号）隔开

<table class="reference"><tbody><tr><th>选项</th><th>描述</th></tr><tr><td>replicaSet=name</td><td>验证replica set的名称。Impliesconnect=replicaSet.</td></tr><tr><td>slaveOk=true|false</td><td><ul><li>true:在connect=direct模式下，驱动会连接第一台机器，即使这台服务器不是主。在connect=replicaSet模式下，驱动会发送所有的写请求到主并且把读取操作分布在其他从服务器。</li><li>false:在connect=direct模式下，驱动会自动找寻主服务器.在connect=replicaSet模式下，驱动仅仅连接主服务器，并且所有的读写命令都连接到主服务器。</li></ul></td></tr><tr><td>safe=true|false</td><td><ul><li>true:在执行更新操作之后，驱动都会发送getLastError命令来确保更新成功。(还要参考wtimeoutMS).</li><li>false:在每次更新之后，驱动不会发送getLastError来确保更新成功。</li></ul></td></tr><tr><td>w=n</td><td>驱动添加{w:n}到getLastError命令.应用于safe=true。</td></tr><tr><td>wtimeoutMS=ms</td><td>驱动添加{wtimeout:ms}到getlasterror命令.应用于safe=true.</td></tr><tr><td>fsync=true|false</td><td><ul><li>true:驱动添加{fsync:true}到getlasterror命令.应用于safe=true.</li><li>false:驱动不会添加到getLastError命令中。</li></ul></td></tr><tr><td>journal=true|false</td><td>如果设置为true,同步到journal(在提交到数据库前写入到实体中).应用于safe=true</td></tr><tr><td>connectTimeoutMS=ms</td><td>可以打开连接的时间。</td></tr><tr><td>socketTimeoutMS=ms</td><td>发送和接受sockets的时间。</td></tr></tbody></table>


## MongoDB 创建数据库

`use DATABASE_NAME`

如果数据库不存在，则创建数据库，否则切换到指定数据库。

`db` 查看当前使用的数据库

`show dbs` 查看所有数据库

```sh

# 创建数据库
> use runoob
switched to db runoob
> db
runoob
> 

# 查询所有数据库
> show dbs
admin   0.000GB
local   0.000GB
> 

#可以看到，我们刚创建的数据库 runoob 并不在数据库的列表中， 要显示它，我们需要向 runoob 数据库插入一些数据。

> db.runoob.insert({"name":"菜鸟教程"})
WriteResult({ "nInserted" : 1 })
> show dbs
local   0.078GB
runoob  0.078GB
test    0.078GB
> 
```

⚠️ 在 MongoDB 中，集合只有在内容插入后才会创建! 就是说，创建集合(数据表)后要再插入一个文档(记录)，集合才会真正创建。

## 删除数据库

`db.dropDatabase()`

删除当前数据库，默认为 test，你可以使用 db 命令查看当前数据库名。

## 创建集合

`db.createCollection(name, options)`

<table class="reference"><thead><tr><th>字段</th><th>类型</th><th>描述</th></tr></thead><tbody><tr><td>capped</td><td>布尔</td><td>（可选）如果为true，则创建固定集合。固定集合是指有着固定大小的集合，当达到最大值时，它会自动覆盖最早的文档。<br><strong>当该值为true时，必须指定size参数。</strong></td></tr><tr><td>autoIndexId</td><td>布尔</td><td>（可选）如为true，自动在_id字段创建索引。默认为false。</td></tr><tr><td>size</td><td>数值</td><td>（可选）为固定集合指定一个最大值（以字节计）。<br><strong>如果capped为true，也需要指定该字段。</strong></td></tr><tr><td>max</td><td>数值</td><td>（可选）指定固定集合中包含文档的最大数量。</td></tr></tbody></table>

🎸 在 MongoDB 中，你不需要创建集合。当你插入一些文档时，MongoDB 会自动创建集合。

```sh
> db.nihao.insert({'name':'ronething'})
WriteResult({ "nInserted" : 1 })
> show collections;
nihao
```

## 删除集合

`db.collection.drop()`

```
> use jiaoyixia
switched to db jiaoyixia
> db
jiaoyixia
> db.nihao.insert({'name':'ronething'})
WriteResult({ "nInserted" : 1 })
> show collections;
nihao
> db.nihao.drop()
true
> show collections;
> 
```

## 插入文档

-   文档的数据结构和JSON基本一样。

-   所有存储在集合中的数据都是BSON格式。

-   BSON是一种类json的一种二进制形式的存储格式,简称Binary JSON。

> MongoDB 使用 insert() 或 save() 方法向集合中插入文档，语法如下：

`db.COLLECTION_NAME.insert(document)`

可以先定义一个变量 然后插入

```sh
> xixi=({title: 'MongoDB 教程', 
...     description: 'MongoDB 是一个 Nosql 数据库',
...     by: '菜鸟教程',
...     url: 'http://www.runoob.com',
...     tags: ['mongodb', 'database', 'NoSQL'],
...     likes: 100
... });
{
	"title" : "MongoDB 教程",
	"description" : "MongoDB 是一个 Nosql 数据库",
	"by" : "菜鸟教程",
	"url" : "http://www.runoob.com",
	"tags" : [
		"mongodb",
		"database",
		"NoSQL"
	],
	"likes" : 100
}

# 插入
> db.nihao.insert(xixi)
WriteResult({ "nInserted" : 1 })
```

⚠️ 也可以使用 db.col.save(document) 命令。如果不指定 _id 字段 save() 方法类似于 insert() 方法。如果指定 _id 字段，则会更新该 _id 的数据。


## 更新文档

> MongoDB 使用 update() 和 save() 方法来更新集合中的文档。接下来让我们详细来看下两个函数的应用及其区别。

### update()

```sh
db.collection.update(
   <query>,
   <update>,
   {
     upsert: <boolean>,
     multi: <boolean>,
     writeConcern: <document>
   }
)
```

### save()

```sh
db.collection.save(
   <document>,
   {
     writeConcern: <document>
   }
)
```

📒 ps: db.${collection}.find().pretty() 输出的格式容易看些。

```sh
# 给大于 99 的 likes 增加 1

> db.nihao.find().pretty()
{ "_id" : ObjectId("5c4046f3f1db4c3b46576840"), "name" : "ronething" }
{
	"_id" : ObjectId("5c404903f1db4c3b46576841"),
	"title" : "MongoDB 教程",
	"description" : "MongoDB 是一个 Nosql 数据库",
	"by" : "菜鸟教程",
	"url" : "http://www.runoob.com",
	"tags" : [
		"mongodb",
		"database",
		"NoSQL"
	],
	"likes" : 100
}
> db.nihao.update({"likes":{$gt:99}},{$inc:{"likes":1}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.nihao.find().pretty()
{ "_id" : ObjectId("5c4046f3f1db4c3b46576840"), "name" : "ronething" }
{
	"_id" : ObjectId("5c404903f1db4c3b46576841"),
	"title" : "MongoDB 教程",
	"description" : "MongoDB 是一个 Nosql 数据库",
	"by" : "菜鸟教程",
	"url" : "http://www.runoob.com",
	"tags" : [
		"mongodb",
		"database",
		"NoSQL"
	],
	"likes" : 101
}
```

> 可以注意到 likes 由 100 增加 1 变成 101


## 删除文档

🎸 在执行remove()函数前先执行find()命令来判断执行的条件是否正确，这是一个比较好的习惯。

```sh
db.collection.remove(
   <query>,
   {
     justOne: <boolean>,
     writeConcern: <document>
   }
)
```

-   query :（可选）删除的文档的条件。
-   justOne : （可选）如果设为 true 或 1，则只删除一个文档，如果不设置该参数，或使用默认值 false，则删除所有匹配条件的文档。
-   writeConcern :（可选）抛出异常的级别。

⚠️ remove() 方法 并不会真正释放空间。需要继续执行 `db.repairDatabase()` 来回收磁盘空间。

> 还有其他方法

-   如删除集合下全部文档：`db.inventory.deleteMany({})`

-   删除 status 等于 A 的全部文档：`db.inventory.deleteMany({ status : "A" })`

-   删除 status 等于 D 的一个文档：`db.inventory.deleteOne( { status: "D" } )`

## 查询文档

`db.collection.find(query, projection)`

-   query ：可选，使用查询操作符指定查询条件
-   projection ：可选，使用投影操作符指定返回的键。查询时返回文档中所有键值， 只需省略该参数即可（默认省略）。

⚠️ 第一个{} 放where条件 第二个{} 指定那些列显示和不显示 （0表示不显示 1表示显示)

```sh
> db.nihao.find({"title":{$type:"string"}},{"title":1,"_id":0})
{ "title" : "MongoDB 教程" }
> db.nihao.find({"title":{$type:"string"}},{"title":0,"_id":0})
{ "description" : "MongoDB 是一个 Nosql 数据库", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "mongodb", "database", "NoSQL" ], "likes" : 100 }
```

## MongoDB 与 RDBMS Where 语句比较

<table class="reference"><thead><tr><th>操作</th><th>格式</th><th>范例</th><th>RDBMS中的类似语句</th></tr></thead><tbody><tr><td>等于</td><td><code>{&lt;key&gt;:&lt;value&gt;</code>}</td><td><code>db.col.find({"by":"菜鸟教程"}).pretty()</code></td><td><code>where by='菜鸟教程'</code></td></tr><tr><td>小于</td><td><code>{&lt;key&gt;:{$lt:&lt;value&gt}}</code></td><td><code>db.col.find({"likes":{$lt:50}}).pretty()</code></td><td><code>where likes&lt;50</code></td></tr><tr><td>小于或等于</td><td><code>{&lt;key&gt;:{$lte:&lt;value&gt}}</code></td><td><code>db.col.find({"likes":{$lte:50}}).pretty()</code></td><td><code>where likes&lt;=50</code></td></tr><tr><td>大于</td><td><code>{&lt;key&gt;:{$gt:&lt;value&gt}}</code></td><td><code>db.col.find({"likes":{$gt:50}}).pretty()</code></td><td><code>where likes&gt;50</code></td></tr><tr><td>大于或等于</td><td><code>{&lt;key&gt;:{$gte:&lt;value&gt}}</code></td><td><code>db.col.find({"likes":{$gte:50}}).pretty()</code></td><td><code>where likes&gt;=50</code></td></tr><tr><td>不等于</td><td><code>{&lt;key&gt;:{$ne:&lt;value&gt}}</code></td><td><code>db.col.find({"likes":{$ne:50}}).pretty()</code></td><td><code>where likes!=50</code></td></tr></tbody></table>

### AND

MongoDB 的 find() 方法可以传入多个键(key)，每个键(key)以逗号隔开，即常规 SQL 的 AND 条件。

`>db.col.find({key1:value1, key2:value2}).pretty()`

### OR

🎸 使用 `$or` 关键字

```sh
>db.col.find(
   {
      $or: [
         {key1: value1}, {key2:value2}
      ]
   }
).pretty()
```

### AND 和 OR 联合使用


```sh
# 类似常规 SQL 语句为： 'where likes>50 AND (by = '菜鸟教程' OR title = 'MongoDB 教程')'

>db.col.find({"likes": {$gt:50}, $or: [{"by": "菜鸟教程"},{"title": "MongoDB 教程"}]}).pretty()
```

## MongoDB 条件操作符

-   (>) 大于 - $gt
-   (<) 小于 - $lt
-   (>=) 大于等于 - $gte
-   (<= ) 小于等于 - $lte


### MongoDB 使用 (<) 和 (>) 查询 - $lt 和 $gt

`db.col.find({likes : {$lt :200, $gt : 100}})`

### `$type`

<table border="1"class="docutils"><colgroup><col width="25%"><col width="25%"><col width="25%"><col width="25%"></colgroup><thead valign="bottom"><tr class="row-odd"><th class="head">Type</th><th class="head">Number</th><th class="head">Alias</th><th class="head">Notes</th></tr></thead><tbody valign="top"><tr class="row-even"><td>Double</td><td>1</td><td>“double”</td><td>&nbsp;</td></tr><tr class="row-odd"><td>String</td><td>2</td><td>“string”</td><td>&nbsp;</td></tr><tr class="row-even"><td>Object</td><td>3</td><td>“object”</td><td>&nbsp;</td></tr><tr class="row-odd"><td>Array</td><td>4</td><td>“array”</td><td>&nbsp;</td></tr><tr class="row-even"><td>Binary data</td><td>5</td><td>“binData”</td><td>&nbsp;</td></tr><tr class="row-odd"><td>Undefined</td><td>6</td><td>“undefined”</td><td>Deprecated.</td></tr><tr class="row-even"><td>ObjectId</td><td>7</td><td>“objectId”</td><td>&nbsp;</td></tr><tr class="row-odd"><td>Boolean</td><td>8</td><td>“bool”</td><td>&nbsp;</td></tr><tr class="row-even"><td>Date</td><td>9</td><td>“date”</td><td>&nbsp;</td></tr><tr class="row-odd"><td>Null</td><td>10</td><td>“null”</td><td>&nbsp;</td></tr><tr class="row-even"><td>Regular Expression</td><td>11</td><td>“regex”</td><td>&nbsp;</td></tr><tr class="row-odd"><td>DBPointer</td><td>12</td><td>“dbPointer”</td><td>Deprecated.</td></tr><tr class="row-even"><td>JavaScript</td><td>13</td><td>“javascript”</td><td>&nbsp;</td></tr><tr class="row-odd"><td>Symbol</td><td>14</td><td>“symbol”</td><td>Deprecated.</td></tr><tr class="row-even"><td>JavaScript(with scope)</td><td>15</td><td>“javascriptWithScope”</td><td>&nbsp;</td></tr><tr class="row-odd"><td>32-bit integer</td><td>16</td><td>“int”</td><td>&nbsp;</td></tr><tr class="row-even"><td>Timestamp</td><td>17</td><td>“timestamp”</td><td>&nbsp;</td></tr><tr class="row-odd"><td>64-bit integer</td><td>18</td><td>“long”</td><td>&nbsp;</td></tr><tr class="row-even"><td>Decimal128</td><td>19</td><td>“decimal”</td><td>New in version 3.4.</td></tr><tr class="row-odd"><td>Min key</td><td>-1</td><td>“minKey”</td><td>&nbsp;</td></tr><tr class="row-even"><td>Max key</td><td>127</td><td>“maxKey”</td><td>&nbsp;</td></tr></tbody></table>


⚠️ `db.nihao.insert({"title":123})` 插入的 title 的 123 是 Double 类型 不是 int 或者 long

## MongoDB Limit与Skip方法

## Limit()

`>db.COLLECTION_NAME.find().limit(NUMBER)`

## Skip()

可以使用skip()方法来跳过指定数量的数据

`>db.COLLECTION_NAME.find().skip(NUMBER)`

or

`>db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER)`

## MongoDB 排序

### sort()

-   sort() 方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式，其中 1 为升序排列，而 -1 是用于降序排列。

`>db.COLLECTION_NAME.find().sort({KEY:1})`

## MongoDB 索引

### createIndex() 

`>db.collection.createIndex(keys, options)`

> 语法中 Key 值为你要创建的索引字段，1 为指定按升序创建索引，如果你想按降序来创建索引指定为 -1 即可。


-   查看集合索引 `db.col.getIndexes()`
-   查看集合索引大小 `db.col.totalIndexSize()`
-   删除集合所有索引 `db.col.dropIndexes()`
-   删除集合指定索引 `db.col.dropIndex("索引名称")`

<table class="reference"><tbody><tr><th style="width:10%;">Parameter</th><th style="width:10%;">Type</th><th>Description</th></tr><tr style=""><td>background</td><td>Boolean</td><td>建索引过程会阻塞其它数据库操作，background可指定以后台方式创建索引，即增加"background"可选参数。"background"默认值为<b>false</b>。</td></tr><tr><td>unique</td><td>Boolean</td><td>建立的索引是否唯一。指定为true创建唯一索引。默认值为<b>false</b>.</td></tr><tr style=""><td>name</td><td>string</td><td>索引的名称。如果未指定，MongoDB的通过连接索引的字段名和排序顺序生成一个索引名称。</td></tr><tr><td>dropDups</td><td>Boolean</td><td><span class="important">3.0+版本已废弃。</span>在建立唯一索引时是否删除重复记录,指定true创建唯一索引。默认值为<b>false</b>.</td></tr><tr style=""><td>sparse</td><td>Boolean</td><td>对文档中不存在的字段数据不启用索引；这个参数需要特别注意，如果设置为true的话，在索引字段中不会查询出不包含对应字段的文档.。默认值为<b>false</b>.</td></tr><tr><td>expireAfterSeconds</td><td>integer</td><td>指定一个以秒为单位的数值，完成TTL设定，设定集合的生存时间。</td></tr><tr style=""><td>v</td><td>index version</td><td>索引的版本号。默认的索引版本取决于mongod创建索引时运行的版本。</td></tr><tr><td>weights</td><td>document</td><td>索引权重值，数值在1到99,999之间，表示该索引相对于其他索引字段的得分权重。</td></tr><tr style=""><td>default_language</td><td>string</td><td>对于文本索引，该参数决定了停用词及词干和词器的规则的列表。默认为英语</td></tr><tr><td>language_override</td><td>string</td><td>对于文本索引，该参数指定了包含在文档中的字段名，语言覆盖默认的language，默认值为language.</td></tr></tbody></table>

## MongoDB 聚合

### aggregate()

`>db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)`

<table class="reference"><tbody><tr><th style="width:10%;">表达式</th><th style="width:50%">描述</th><th>实例</th></tr><tr><td>$sum</td><td>计算总和。</td><td>db.mycol.aggregate([{$group:{_id:"$by_user",num_tutorial:{$sum:"$likes"}}}])</td></tr><tr><td>$avg</td><td>计算平均值</td><td>db.mycol.aggregate([{$group:{_id:"$by_user",num_tutorial:{$avg:"$likes"}}}])</td></tr><tr><td>$min</td><td>获取集合中所有文档对应值得最小值。</td><td>db.mycol.aggregate([{$group:{_id:"$by_user",num_tutorial:{$min:"$likes"}}}])</td></tr><tr><td>$max</td><td>获取集合中所有文档对应值得最大值。</td><td>db.mycol.aggregate([{$group:{_id:"$by_user",num_tutorial:{$max:"$likes"}}}])</td></tr><tr><td>$push</td><td>在结果文档中插入值到一个数组中。</td><td>db.mycol.aggregate([{$group:{_id:"$by_user",url:{$push:"$url"}}}])</td></tr><tr><td>$addToSet</td><td>在结果文档中插入值到一个数组中，但不创建副本。</td><td>db.mycol.aggregate([{$group:{_id:"$by_user",url:{$addToSet:"$url"}}}])</td></tr><tr><td>$first</td><td>根据资源文档的排序获取第一个文档数据。</td><td>db.mycol.aggregate([{$group:{_id:"$by_user",first_url:{$first:"$url"}}}])</td></tr><tr><td>$last</td><td>根据资源文档的排序获取最后一个文档数据</td><td>db.mycol.aggregate([{$group:{_id:"$by_user",last_url:{$last:"$url"}}}])</td></tr></tbody></table>

### 管道

-   $project：修改输入文档的结构。可以用来重命名、增加或删除域，也可以用于创建计算结果以及嵌套文档。
-   $match：用于过滤数据，只输出符合条件的文档。$match使用MongoDB的标准查询操作。
-   $limit：用来限制MongoDB聚合管道返回的文档数。
-   $skip：在聚合管道中跳过指定数量的文档，并返回余下的文档。
-   $unwind：将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值。
-   $group：将集合中的文档分组，可用于统计结果。
-   $sort：将输入文档排序后输出。
-   $geoNear：输出接近某一地理位置的有序文档。

```sh
# $project

db.article.aggregate(
    { $project : {
        title : 1 ,
        author : 1 ,
    }}
 );

 # $match

 db.articles.aggregate( [
                        { $match : { score : { $gt : 70, $lte : 90 } } },
                        { $group: { _id: null, count: { $sum: 1 } } }
                       ] );

# ¥skip

db.article.aggregate(
    { $skip : 5 });
```

## MongoDB 复制（副本集）

-   MongoDB复制是将数据同步在多个服务器的过程。

-   复制提供了数据的冗余备份，并在多个服务器上存储数据副本，提高了数据的可用性， 并可以保证数据的安全性。

-   复制还允许您从硬件故障和服务中断中恢复数据

### 什么是复制

-   保障数据的安全性
-   数据高可用性 (24*7)
-   灾难恢复
-   无需停机维护（如备份，重建索引，压缩）
-   分布式读取数据

### 复制原理

mongodb的复制至少需要两个节点。其中一个是主节点，负责处理客户端请求，其余的都是从节点，负责复制主节点上的数据。

mongodb各个节点常见的搭配方式为：一主一从、一主多从。

主节点记录在其上的所有操作oplog，从节点定期轮询主节点获取这些操作，然后对自己的数据副本执行这些操作，从而保证从节点的数据与主节点一致。

![](https://raw.githubusercontent.com/ronething/Image-Hosting/master/img/20190118114747.png)

### 副本集特征

-   N 个节点的集群
-   任何节点可作为主节点
-   所有写入操作都在主节点上
-   自动故障转移
-   自动恢复

**--replSet**

rs.initiate()

rs.conf()

rs.status()

`>rs.add(HOST_NAME:PORT)`

⚠️ MongoDB的副本集与我们常见的主从有所不同，主从在主机宕机后所有服务将停止，而副本集在主机宕机后，副本会接管主节点成为主节点，不会出现宕机的情况。

## MongoDB 分片

-   复制所有的写入操作到主节点
-   延迟的敏感数据会在主节点查询
-   单个副本集限制在12个节点
-   当请求量巨大时会出现内存不足。
-   本地磁盘不足
-   垂直扩展价格昂贵

![](https://raw.githubusercontent.com/ronething/Image-Hosting/master/img/20190118140842.png)

-   Shard:

    用于存储实际的数据块，实际生产环境中一个shard server角色可由几台机器组成一个replica set承担，防止主机单点故障

-   Config Server:

    mongod实例，存储了整个 ClusterMetadata，其中包括 chunk信息。

-   Query Routers:
    
    前端路由，客户端由此接入，且让整个集群看上去像单一数据库，前端应用可以透明使用。

### [分片实例](http://www.runoob.com/mongodb/mongodb-sharding.html)

```sh
Shard Server 1：27020
Shard Server 2：27021
Shard Server 3：27022
Shard Server 4：27023
Config Server ：27100
Route Process：40000
```

启动 `Shard Serer`

```
[root@100 /]# mkdir -p /www/mongoDB/shard/s0
[root@100 /]# mkdir -p /www/mongoDB/shard/s1
[root@100 /]# mkdir -p /www/mongoDB/shard/s2
[root@100 /]# mkdir -p /www/mongoDB/shard/s3
[root@100 /]# mkdir -p /www/mongoDB/shard/log
[root@100 /]# /usr/local/mongoDB/bin/mongod --port 27020 --dbpath=/www/mongoDB/shard/s0 --logpath=/www/mongoDB/shard/log/s0.log --logappend --fork
....
[root@100 /]# /usr/local/mongoDB/bin/mongod --port 27023 --dbpath=/www/mongoDB/shard/s3 --logpath=/www/mongoDB/shard/log/s3.log --logappend --fork
```

启动 `Config Server`

```
[root@100 /]# mkdir -p /www/mongoDB/shard/config
[root@100 /]# /usr/local/mongoDB/bin/mongod --port 27100 --dbpath=/www/mongoDB/shard/config --logpath=/www/mongoDB/shard/log/config.log --logappend --fork
```

启动 `Route Process`

```
/usr/local/mongoDB/bin/mongos --port 40000 --configdb localhost:27100 --fork --logpath=/www/mongoDB/shard/log/route.log --chunkSize 500
```

配置 Sharing

```
[root@100 shard]# /usr/local/mongoDB/bin/mongo admin --port 40000
MongoDB shell version: 2.0.7
connecting to: 127.0.0.1:40000/admin
mongos> db.runCommand({ addshard:"localhost:27020" })
{ "shardAdded" : "shard0000", "ok" : 1 }
......
mongos> db.runCommand({ addshard:"localhost:27029" })
{ "shardAdded" : "shard0009", "ok" : 1 }
mongos> db.runCommand({ enablesharding:"test" }) #设置分片存储的数据库
{ "ok" : 1 }
mongos> db.runCommand({ shardcollection: "test.log", key: { id:1,time:1}})
{ "collectionsharded" : "test.log", "ok" : 1 }
```

最后，直接按照连接普通的mongo数据库那样，将数据库连接接入接口40000

## 备份(mongodump)与恢复(mongorestore)

### 备份

`>mongodump -h dbhost -d dbname -o dbdirectory`

-   -h：MongDB所在服务器地址，例如：127.0.0.1，当然也可以指定端口号：127.0.0.1:27017

-   -d：需要备份的数据库实例，例如：test

-   -o：备份的数据存放位置，该目录需要提前建立，在备份完成后，系统自动在目录下建立一个test目录，这个目录里面存放该数据库实例的备份数据。

<table class="reference"><tbody><tr><th style="width:40%">语法</th><th style="width:30%">描述</th><th>实例</th></tr><tr><td>mongodump--host HOST_NAME--port PORT_NUMBER</td><td>该命令将备份所有MongoDB数据</td><td>mongodump--host runoob.com--port 27017</td></tr><tr><td>mongodump--dbpath DB_PATH--out BACKUP_DIRECTORY</td><td></td><td>mongodump--dbpath/data/db/--out/data/backup/</td></tr><tr><td>mongodump--collection COLLECTION--db DB_NAME</td><td>该命令将备份指定数据库的集合。</td><td>mongodump--collection mycol--db test</td></tr></tbody></table>

### 恢复

`>mongorestore -h <hostname><:port> -d dbname <path>`

-   --host <:port>, -h <:port>：MongoDB所在服务器地址，默认为： localhost:27017

-   --db , -d ：需要恢复的数据库实例，例如：test，当然这个名称也可以和备份时候的不一样，比如test2

-   --drop：恢复的时候，先删除当前数据，然后恢复备份的数据。就是说，恢复后，备份后添加修改的数据都会被删除，慎用哦！

-   <path>：mongorestore 最后的一个参数，设置备份数据所在位置，例如：/data/db/test。你不能同时指定 <path> 和 --dir 选项，--dir也可以设置备份目录。

-   --dir：指定备份的目录 你不能同时指定 <path> 和 --dir 选项。

## MongoDB 监控

`mongostat`

`mongotop`

mongotop提供每个集合的水平的统计数据。

-   ns：包含数据库命名空间，后者结合了数据库名称和集合。

-   db：包含数据库的名称。名为 . 的数据库针对全局锁定，而非特定数据库。

-   total：mongod花费的时间工作在这个命名空间提供总额。

-   read：提供了大量的时间，这mongod花费在执行读操作，在此命名空间。

-   write：提供这个命名空间进行写操作，这mongod花了大量的时间。