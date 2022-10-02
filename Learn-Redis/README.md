# learn-redis

## 概述

### 简介

-    Redis 是完全开源免费的，遵守BSD协议，是一个高性能的key-value数据库。

-    Redis 与其他 key - value 缓存产品有以下三个特点：

    -    Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
    -    Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
    -    Redis支持数据的备份，即master-slave模式的数据备份。

### 优势

-    性能极高 – Redis能读的速度是110000次/s,写的速度是81000次/s 。
-    丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。
-    原子 – Redis的所有操作都是原子性的，意思就是要么成功执行要么失败完全不执行。单个操作是原子性的。
-    丰富的特性 – Redis还支持 publish/subscribe, 通知, key 过期等等特性。

## 部署 redis

### 直接 docker 吧

创建 `data` 目录 `conf` 目录 

`conf` 目录下面创建 `redis.conf` (我已经上传了)

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fz19kp3w9qj210c04umy8.jpg)

```sh
docker run -d --privileged=true -p 6379:6379 -v `pwd`/conf/redis.conf:/etc/redis/redis_default.conf -v `pwd`/data:/data --name redis redis:4.0
```

测试一下

```sh
telnet 127.0.0.1 6379 
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
ping
+PONG
# 输入 ping 有 pong 就稳了
```

## 配置

### 通过 CONFIG 命令查看或设置配置项

`redis 127.0.0.1:6379> CONFIG GET CONFIG_SETTING_NAME`

```sh
# loglevel config
CONFIG GET loglevel
# 获取所有配置项
CONFIG GET *
```

### `redis.conf` 参数说明

1. Redis默认不是以守护进程的方式运行，可以通过该配置项修改，使用yes启用守护进程

    `daemonize no`

2. 当Redis以守护进程方式运行时，Redis默认会把pid写入/var/run/redis.pid文件，可以通过pidfile指定

    `pidfile /var/run/redis.pid`

3. 指定Redis监听端口，默认端口为6379，作者在自己的一篇博文中解释了为什么选用6379作为默认端口，因为6379在手机按键上MERZ对应的号码，而MERZ取自意大利歌女Alessia Merz的名字

    `port 6379`

4. 绑定的主机地址

    `bind 127.0.0.1`

5.当 客户端闲置多长时间后关闭连接，如果指定为0，表示关闭该功能

`timeout 300`

6. 指定日志记录级别，Redis总共支持四个级别：debug、verbose、notice、warning，默认为verbose

`loglevel verbose`

7. 日志记录方式，默认为标准输出，如果配置Redis为守护进程方式运行，而这里又配置为日志记录方式为标准输出，则日志将会发送给/dev/null

`logfile stdout`

8. 设置数据库的数量，默认数据库为0，可以使用SELECT <dbid>命令在连接上指定数据库id

`databases 16`

9. 指定在多长时间内，有多少次更新操作，就将数据同步到数据文件，可以多个条件配合

`save <seconds> <changes>`

Redis默认配置文件中提供了三个条件：

```sh
save 900 1

save 300 10

save 60 10000
```

分别表示900秒（15分钟）内有1个更改，300秒（5分钟）内有10个更改以及60秒内有10000个更改。 

10. 指定存储至本地数据库时是否压缩数据，默认为yes，Redis采用LZF压缩，如果为了节省CPU时间，可以关闭该选项，但会导致数据库文件变的巨大

`rdbcompression yes`

11. 指定本地数据库文件名，默认值为dump.rdb

`dbfilename dump.rdb`

12. 指定本地数据库存放目录

`dir ./`

13. 设置当本机为slav服务时，设置master服务的IP地址及端口，在Redis启动时，它会自动从master进行数据同步

`slaveof <masterip> <masterport>`

14. 当master服务设置了密码保护时，slav服务连接master的密码

`masterauth <master-password>`

15. 设置Redis连接密码，如果配置了连接密码，客户端在连接Redis时需要通过AUTH <password>命令提供密码，默认关闭

`requirepass foobared`

16. 设置同一时间最大客户端连接数，默认无限制，Redis可以同时打开的客户端连接数为Redis进程可以打开的最大文件描述符数，如果设置 maxclients 0，表示不作限制。当客户端连接数到达限制时，Redis会关闭新的连接并向客户端返回max number of clients reached错误信息

`maxclients 128`

17. 指定Redis最大内存限制，Redis在启动时会把数据加载到内存中，达到最大内存后，Redis会先尝试清除已到期或即将到期的Key，当此方法处理 后，仍然到达最大内存设置，将无法再进行写入操作，但仍然可以进行读取操作。Redis新的vm机制，会把Key存放内存，Value会存放在swap区

`maxmemory <bytes>`

18. 指定是否在每次更新操作后进行日志记录，Redis在默认情况下是异步的把数据写入磁盘，如果不开启，可能会在断电时导致一段时间内的数据丢失。因为 redis本身同步数据文件是按上面save条件来同步的，所以有的数据会在一段时间内只存在于内存中。默认为no

`appendonly no`

19. 指定更新日志文件名，默认为appendonly.aof

`appendfilename appendonly.aof`

20. 指定更新日志条件，共有3个可选值： 

    -   no：表示等操作系统进行数据缓存同步到磁盘（快） 
    -   always：表示每次更新操作后手动调用fsync()将数据写到磁盘（慢，安全） 
    -   everysec：表示每秒同步一次（折中，默认值）

    `appendfsync everysec`

21. 指定是否启用虚拟内存机制，默认值为no，简单的介绍一下，VM机制将数据分页存放，由Redis将访问量较少的页即冷数据swap到磁盘上，访问多的页面由磁盘自动换出到内存中（在后面的文章我会仔细分析Redis的VM机制）

    `vm-enabled no`

22. 虚拟内存文件路径，默认值为/tmp/redis.swap，不可多个Redis实例共享

     `vm-swap-file /tmp/redis.swap`

23. 将所有大于vm-max-memory的数据存入虚拟内存,无论vm-max-memory设置多小,所有索引数据都是内存存储的(Redis的索引数据 就是keys),也就是说,当vm-max-memory设置为0的时候,其实是所有value都存在于磁盘。默认值为0

     `vm-max-memory 0`

24. Redis swap文件分成了很多的page，一个对象可以保存在多个page上面，但一个page上不能被多个对象共享，vm-page-size是要根据存储的 数据大小来设定的，作者建议如果存储很多小对象，page大小最好设置为32或者64bytes；如果存储很大大对象，则可以使用更大的page，如果不 确定，就使用默认值

     `vm-page-size 32`

25. 设置swap文件中的page数量，由于页表（一种表示页面空闲或使用的bitmap）是在放在内存中的，，在磁盘上每8个pages将消耗1byte的内存。

     `vm-pages 134217728`

26. 设置访问swap文件的线程数,最好不要超过机器的核数,如果设置为0,那么所有对swap文件的操作都是串行的，可能会造成比较长时间的延迟。默认值为4

     `vm-max-threads 4`

27. 设置在向客户端应答时，是否把较小的包合并为一个包发送，默认为开启

    `glueoutputbuf yes`

28. 指定在超过一定的数量或者最大的元素超过某一临界值时，采用一种特殊的哈希算法

    `hash-max-zipmap-entries 64`

    `hash-max-zipmap-value 512`

29. 指定是否激活重置哈希，默认为开启（后面在介绍Redis的哈希算法时具体介绍）

    `activerehashing yes`

30. 指定包含其它的配置文件，可以在同一主机上多个Redis实例之间使用同一份配置文件，而同时各个实例又拥有自己的特定配置文件

    `include /path/to/local.conf`

## Redis 数据类型

### 支持类型

Redis支持五种数据类型：string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)。

### String（字符串）

string 是 redis 最基本的类型，你可以理解成与 Memcached 一模一样的类型，一个 key 对应一个 value。

string 类型是二进制安全的。意思是 redis 的 string 可以包含任何数据。比如jpg图片或者序列化的对象。

string 类型是 Redis 最基本的数据类型，string 类型的值最大能存储 512MB。

```sh
set name "nihao"
+OK
get name
$5
nihao
```

###  Hash（哈希）

Redis hash 是一个键值(key=>value)对集合。

Redis hash 是一个 string 类型的 field 和 value 的映射表，hash 特别适合用于存储对象。

```sh
HMSET myhash name1 "hh" name2 "xx"
+OK
HGET myhash name1
$2
hh
HGET myhash name2
$2
xx
```

⚠️ 每个 hash 可以存储 2^32 -1 键值对（40多亿）。

### List（列表）

```sh
lpush mylist nihao
:1
lpush mylist bieba
:2
lpush mylist xingba
:3
lrange mylist 0 10
*3
$6
xingba
$5
bieba
$5
nihao
```

⚠️ 列表最多可存储 232 - 1 元素 (4294967295, 每个列表可存储40多亿)。

### Set（集合）

添加一个 string 元素到 key 对应的 set 集合中，成功返回1，如果元素已经在集合中返回 0，如果 key 对应的 set 不存在则返回错误。

`sadd key member`

```sh
sadd myset nihao
:1
sadd myset bieba
:1
sadd myset jiaoyixia
:1
sadd myset nihao
:0
smembers myset
*3
$5
bieba
$5
nihao
$9
jiaoyixia
```

根据集合内元素的唯一性，第二次插入的元素将被忽略。

集合中最大的成员数为 232 - 1(4294967295, 每个集合可存储40多亿个成员)。

### zset(sorted set：有序集合)

Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。
不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。

zset的成员是唯一的,但分数(score)却可以重复。

`zadd key score member `

```sh
zadd myzset 0 nihao
:1
zadd myzset 1 bieba 
:1
zadd myzset 4 xingba
:1
zadd myzset 2 xixi
:1
ZRANGEBYSCORE myzset 0 100
*4
$5
nihao
$5
bieba
$4
xixi
$6
xingba
```

## Redis 命令

在以上实例中我们连接到本地的 redis 服务并执行 PING 命令，该命令用于检测 redis 服务是否启动。

```sh
telnet 127.0.0.1 6379
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
ping
+PONG
# 输入 ping 有 pong 就稳了
```

⚠️ 之前直接用 `telnet` 连接了发觉不是很方便 所以还是直接用一个 `redis-cli`

```sh
$ wget http://download.redis.io/releases/redis-5.0.3.tar.gz
$ tar xzf redis-5.0.3.tar.gz
$ cd redis-5.0.3
$ make
# 运行 redis-cli
cd src
./redis-cli
```

### 在远程服务上执行命令

`$ redis-cli -h host -p port -a password`

```sh
redis-cli -h 127.0.0.1 -p 6379
127.0.0.1:6379> ping
PONG
127.0.0.1:6379>
```

## Redis 键(key)

> Redis 键命令用于管理 redis 的键

### 语法

`COMMAND KEY_NAME`

### 实例

```sh
127.0.0.1:6379> set mykey isvalue
OK
127.0.0.1:6379> get mykey
"isvalue"
127.0.0.1:6379> del mykey
(integer) 1
127.0.0.1:6379> get mykey
(nil)
```

### 详细参数

<table class="reference">
<tbody><tr><th style="width:5%">序号</th><th>命令及描述</th></tr>
<tr><td>1</td><td><a href="/redis/keys-del.html">DEL key</a><br>该命令用于在 key 存在时删除  key。</td></tr>
<tr><td>2</td><td><a href="/redis/keys-dump.html">DUMP key</a> <br>序列化给定 key ，并返回被序列化的值。</td></tr>
<tr><td>3</td><td><a href="/redis/keys-exists.html">EXISTS key</a> <br>检查给定 key 是否存在。</td></tr>
<tr><td>4</td><td><a href="/redis/keys-expire.html">EXPIRE key</a> seconds<br>为给定 key 设置过期时间，以秒计。</td></tr>
<tr><td>5</td><td><a href="/redis/keys-expireat.html">EXPIREAT key timestamp</a> <br>EXPIREAT 的作用和 EXPIRE 类似，都用于为 key 设置过期时间。

不同在于 EXPIREAT 命令接受的时间参数是 UNIX 时间戳(unix timestamp)。</td></tr>
<tr><td>6</td><td><a href="/redis/keys-pexpire.html">PEXPIRE key milliseconds</a> <br>设置 key 的过期时间以毫秒计。</td></tr>
<tr><td>7</td><td><a href="/redis/keys-pexpireat.html">PEXPIREAT key milliseconds-timestamp</a> <br>设置 key 过期时间的时间戳(unix timestamp) 以毫秒计</td></tr>
<tr><td>8</td><td><a href="/redis/keys-keys.html">KEYS pattern</a> <br>查找所有符合给定模式( pattern)的 key 。 </td></tr>
<tr><td>9</td><td><a href="/redis/keys-move.html">MOVE key db</a> <br>将当前数据库的 key 移动到给定的数据库 db 当中。</td></tr>
<tr><td>10</td><td><a href="/redis/keys-persist.html">PERSIST key</a> <br>移除 key 的过期时间，key 将持久保持。</td></tr>
<tr><td>11</td><td><a href="/redis/keys-pttl.html">PTTL key</a> <br>以毫秒为单位返回 key 的剩余的过期时间。</td></tr>
<tr><td>12</td><td><a href="/redis/keys-ttl.html">TTL key</a> <br>以秒为单位，返回给定 key 的剩余生存时间(TTL, time to live)。</td></tr>
<tr><td>13</td><td><a href="/redis/keys-randomkey.html">RANDOMKEY</a> <br>从当前数据库中随机返回一个 key 。 </td></tr>
<tr><td>14</td><td><a href="/redis/keys-rename.html">RENAME key newkey</a> <br>修改 key 的名称</td></tr>
<tr><td>15</td><td><a href="/redis/keys-renamenx.html">RENAMENX key newkey</a> <br>仅当 newkey 不存在时，将 key 改名为 newkey 。</td></tr>
<tr><td>16</td><td><a href="/redis/keys-type.html">TYPE key</a> <br>返回 key 所储存的值的类型。</td></tr>
</tbody></table>

`rename`

修改key名:    `rename k1 k2`

`renamenx`

修改key名字，与rename区别在于新key存在时renamenx会报错。rename 会直接覆盖。

## Redis 字符串(String)

### 详细参数

<table class="reference">
<tbody><tr><th style="width:5%">序号</th><th>命令及描述</th></tr>
<tr><td>1</td><td><a href="/redis/strings-set.html">SET key value</a> <br>设置指定 key 的值</td></tr>
<tr><td>2</td><td><a href="/redis/strings-get.html">GET key</a> <br>获取指定 key 的值。</td></tr>
<tr><td>3</td><td><a href="/redis/strings-getrange.html">GETRANGE key start end</a> <br>返回 key 中字符串值的子字符</td></tr>
<tr><td>4</td><td><a href="/redis/strings-getset.html">GETSET key value</a><br>将给定 key 的值设为 value ，并返回 key 的旧值(old value)。</td></tr>
<tr><td>5</td><td><a href="/redis/strings-getbit.html">GETBIT key offset</a><br>对 key 所储存的字符串值，获取指定偏移量上的位(bit)。</td></tr>
<tr><td>6</td><td><a href="/redis/strings-mget.html">MGET key1 [key2..]</a><br>获取所有(一个或多个)给定 key 的值。 </td></tr>
<tr><td>7</td><td><a href="/redis/strings-setbit.html">SETBIT key offset value</a><br>对 key 所储存的字符串值，设置或清除指定偏移量上的位(bit)。</td></tr>
<tr><td>8</td><td><a href="/redis/strings-setex.html">SETEX key seconds value</a><br>将值 value 关联到 key ，并将 key 的过期时间设为 seconds (以秒为单位)。</td></tr>
<tr><td>9</td><td><a href="/redis/strings-setnx.html">SETNX key value</a><br>只有在 key 不存在时设置 key 的值。</td></tr>
<tr><td>10</td><td><a href="/redis/strings-setrange.html">SETRANGE key offset value</a><br>用 value 参数覆写给定 key 所储存的字符串值，从偏移量 offset 开始。 </td></tr>
<tr><td>11</td><td><a href="/redis/strings-strlen.html">STRLEN key</a><br>返回 key 所储存的字符串值的长度。</td></tr>
<tr><td>12</td><td><a href="/redis/strings-mset.html">MSET key value [key value ...]</a><br>同时设置一个或多个 key-value 对。</td></tr>
<tr><td>13</td><td><a href="/redis/strings-msetnx.html">MSETNX key value [key value ...]</a> <br>同时设置一个或多个 key-value 对，当且仅当所有给定 key 都不存在。</td></tr>
<tr><td>14</td><td><a href="/redis/strings-psetex.html">PSETEX key milliseconds value</a><br>这个命令和 SETEX 命令相似，但它以毫秒为单位设置 key 的生存时间，而不是像 SETEX 命令那样，以秒为单位。</td></tr>
<tr><td>15</td><td><a href="/redis/strings-incr.html">INCR key</a><br>将 key 中储存的数字值增一。</td></tr>
<tr><td>16</td><td><a href="/redis/strings-incrby.html">INCRBY key increment</a><br>将 key 所储存的值加上给定的增量值（increment） 。</td></tr>
<tr><td>17</td><td><a href="/redis/strings-incrbyfloat.html">INCRBYFLOAT key increment</a><br>将 key 所储存的值加上给定的浮点增量值（increment） 。 </td></tr>
<tr><td>18</td><td><a href="/redis/strings-decr.html">DECR key</a><br>将 key 中储存的数字值减一。</td></tr>
<tr><td>19</td><td><a href="/redis/strings-decrby.html">DECRBY key decrement</a><br> key 所储存的值减去给定的减量值（decrement） 。 </td></tr>
<tr><td>20</td><td><a href="/redis/strings-append.html">APPEND key value</a><br>如果 key 已经存在并且是一个字符串， APPEND 命令将指定的 value 追加到该 key 原来值（value）的末尾。 </td></tr>
</tbody></table>

## Redis 哈希(Hash)

### 详细参数

<table class="reference">
<tbody><tr><th style="width:5%">序号</th><th>命令及描述</th></tr>
<tr><td>1</td><td><a href="/redis/hashes-hdel.html">HDEL key field1 [field2]</a> <br>删除一个或多个哈希表字段</td></tr>
<tr><td>2</td><td><a href="/redis/hashes-hexists.html">HEXISTS key field</a> <br>查看哈希表 key 中，指定的字段是否存在。</td></tr>
<tr><td>3</td><td><a href="/redis/hashes-hget.html">HGET key field</a> <br>获取存储在哈希表中指定字段的值。</td></tr>
<tr><td>4</td><td><a href="/redis/hashes-hgetall.html">HGETALL key</a> <br>获取在哈希表中指定 key 的所有字段和值</td></tr>
<tr><td>5</td><td><a href="/redis/hashes-hincrby.html">HINCRBY key field increment</a> <br>为哈希表 key 中的指定字段的整数值加上增量 increment 。</td></tr>
<tr><td>6</td><td><a href="/redis/hashes-hincrbyfloat.html">HINCRBYFLOAT key field increment</a> <br>为哈希表 key 中的指定字段的浮点数值加上增量 increment 。</td></tr>
<tr><td>7</td><td><a href="/redis/hashes-hkeys.html">HKEYS key</a> <br>获取所有哈希表中的字段</td></tr>
<tr><td>8</td><td><a href="/redis/hashes-hlen.html">HLEN key</a> <br>获取哈希表中字段的数量</td></tr>
<tr><td>9</td><td><a href="/redis/hashes-hmget.html">HMGET key field1 [field2]</a> <br>获取所有给定字段的值</td></tr>
<tr><td>10</td><td><a href="/redis/hashes-hmset.html">HMSET key field1 value1 [field2 value2 ]</a> <br>同时将多个 field-value (域-值)对设置到哈希表 key 中。</td></tr>
<tr><td>11</td><td><a href="/redis/hashes-hset.html">HSET key field value</a> <br>将哈希表 key 中的字段 field 的值设为 value 。</td></tr>
<tr><td>12</td><td><a href="/redis/hashes-hsetnx.html">HSETNX key field value</a> <br>只有在字段 field 不存在时，设置哈希表字段的值。</td></tr>
<tr><td>13</td><td><a href="/redis/hashes-hvals.html">HVALS key</a> <br>获取哈希表中所有值</td></tr>
<tr><td>14</td><td>HSCAN key cursor [MATCH pattern] [COUNT count] <br>迭代哈希表中的键值对。</td></tr>
</tbody></table>

## Redis 列表(List)

### 详细参数

<table class="reference">
<tbody><tr><th style="width:5%">序号</th><th>命令及描述</th></tr>
<tr><td>1</td><td><a target="_blank" href="/redis/lists-blpop.html">BLPOP key1 [key2 ] timeout</a> <br>移出并获取列表的第一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。</td></tr>
<tr><td>2</td><td><a target="_blank" href="/redis/lists-brpop.html">BRPOP key1 [key2 ] timeout</a> <br>移出并获取列表的最后一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。</td></tr>
<tr><td>3</td><td><a target="_blank" href="/redis/lists-brpoplpush.html">BRPOPLPUSH source destination timeout</a> <br>从列表中弹出一个值，将弹出的元素插入到另外一个列表中并返回它； 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。</td></tr>
<tr><td>4</td><td><a target="_blank" href="/redis/lists-lindex.html">LINDEX key index</a> <br>通过索引获取列表中的元素</td></tr>
<tr><td>5</td><td><a target="_blank" href="/redis/lists-linsert.html">LINSERT key BEFORE|AFTER pivot value</a> <br>在列表的元素前或者后插入元素</td></tr>
<tr><td>6</td><td><a target="_blank" href="/redis/lists-llen.html">LLEN key</a> <br>获取列表长度</td></tr>
<tr><td>7</td><td><a target="_blank" href="/redis/lists-lpop.html">LPOP key</a> <br>移出并获取列表的第一个元素</td></tr>
<tr><td>8</td><td><a target="_blank" href="/redis/lists-lpush.html">LPUSH key value1 [value2]</a> <br>将一个或多个值插入到列表头部</td></tr>
<tr><td>9</td><td><a target="_blank" href="/redis/lists-lpushx.html">LPUSHX key value</a> <br>将一个值插入到已存在的列表头部</td></tr>
<tr><td>10</td><td><a target="_blank" href="/redis/lists-lrange.html">LRANGE key start stop</a> <br>获取列表指定范围内的元素</td></tr>
<tr><td>11</td><td><a target="_blank" href="/redis/lists-lrem.html">LREM key count value</a> <br>移除列表元素</td></tr>
<tr><td>12</td><td><a target="_blank" href="/redis/lists-lset.html">LSET key index value</a> <br>通过索引设置列表元素的值</td></tr>
<tr><td>13</td><td><a target="_blank" href="/redis/lists-ltrim.html">LTRIM key start stop</a> <br>对一个列表进行修剪(trim)，就是说，让列表只保留指定区间内的元素，不在指定区间之内的元素都将被删除。</td></tr>
<tr><td>14</td><td><a target="_blank" href="/redis/lists-rpop.html">RPOP key</a> <br>移除列表的最后一个元素，返回值为移除的元素。</td></tr>
<tr><td>15</td><td><a target="_blank" href="/redis/lists-rpoplpush.html">RPOPLPUSH source destination</a> <br>移除列表的最后一个元素，并将该元素添加到另一个列表并返回</td></tr>
<tr><td>16</td><td><a target="_blank" href="/redis/lists-rpush.html">RPUSH key value1 [value2]</a> <br>在列表中添加一个或多个值</td></tr>
<tr><td>17</td><td><a target="_blank" href="/redis/lists-rpushx.html">RPUSHX key value</a> <br>为已存在的列表添加值</td></tr>
</tbody></table>

## Redis 集合(Set)

集合成员是唯一的，这就意味着集合中不能出现重复的数据。

### 详细参数

<table class="reference">
<tbody><tr><th style="width:5%">序号</th><th>命令及描述</th></tr>
<tr><td>1</td><td><a href="/redis/sets-sadd.html">SADD key member1 [member2]</a> <br>向集合添加一个或多个成员</td></tr>
<tr><td>2</td><td><a href="/redis/sets-scard.html">SCARD key</a> <br>获取集合的成员数</td></tr>
<tr><td>3</td><td><a href="/redis/sets-sdiff.html">SDIFF key1 [key2]</a> <br>返回给定所有集合的差集</td></tr>
<tr><td>4</td><td><a href="/redis/sets-sdiffstore.html">SDIFFSTORE destination key1 [key2]</a> <br>返回给定所有集合的差集并存储在 destination 中</td></tr>
<tr><td>5</td><td><a href="/redis/sets-sinter.html">SINTER key1 [key2]</a> <br>返回给定所有集合的交集</td></tr>
<tr><td>6</td><td><a href="/redis/sets-sinterstore.html">SINTERSTORE destination key1 [key2]</a> <br>返回给定所有集合的交集并存储在 destination 中</td></tr>
<tr><td>7</td><td><a href="/redis/sets-sismember.html">SISMEMBER key member</a> <br>判断 member 元素是否是集合 key 的成员</td></tr>
<tr><td>8</td><td><a href="/redis/sets-smembers.html">SMEMBERS key</a> <br>返回集合中的所有成员</td></tr>
<tr><td>9</td><td><a href="/redis/sets-smove.html">SMOVE source destination member</a> <br>将 member 元素从 source 集合移动到 destination 集合</td></tr>
<tr><td>10</td><td><a href="/redis/sets-spop.html">SPOP key</a> <br>移除并返回集合中的一个随机元素</td></tr>
<tr><td>11</td><td><a href="/redis/sets-srandmember.html">SRANDMEMBER key [count]</a> <br>返回集合中一个或多个随机数</td></tr>
<tr><td>12</td><td><a href="/redis/sets-srem.html">SREM key member1 [member2]</a> <br>移除集合中一个或多个成员</td></tr>
<tr><td>13</td><td><a href="/redis/sets-sunion.html">SUNION key1 [key2]</a> <br>返回所有给定集合的并集</td></tr>
<tr><td>14</td><td><a href="/redis/sets-sunionstore.html">SUNIONSTORE destination key1 [key2]</a> <br>所有给定集合的并集存储在 destination 集合中</td></tr>
<tr><td>15</td><td><a href="/redis/sets-sscan.html">SSCAN key cursor [MATCH pattern] [COUNT count]</a> <br>迭代集合中的元素</td></tr>
</tbody></table>

`SDIFF`

差集的结果来自前面的 **FIRST_KEY** ,而不是后面的 OTHER_KEY1，也不是整个 FIRST_KEY OTHER_KEY1..OTHER_KEYN 的差集。

```sh
key1 = {a,b,c,d}
key2 = {c}
key3 = {a,c,e}
SDIFF key1 key2 key3 = {b,d}
```

## Redis 有序集合(sorted set)

不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。

有序集合的成员是唯一的,但分数(score)却可以重复。

### 详细参数

<table class="reference">
<tbody><tr><th style="width:5%">序号</th><th>命令及描述</th></tr>
<tr><td>1</td><td><a href="/redis/sorted-sets-zadd.html">ZADD key score1 member1 [score2 member2]</a> <br>向有序集合添加一个或多个成员，或者更新已存在成员的分数</td></tr>
<tr><td>2</td><td><a href="/redis/sorted-sets-zcard.html">ZCARD key</a> <br>获取有序集合的成员数</td></tr>
<tr><td>3</td><td><a href="/redis/sorted-sets-zcount.html">ZCOUNT key min max</a> <br>计算在有序集合中指定区间分数的成员数</td></tr>
<tr><td>4</td><td><a href="/redis/sorted-sets-zincrby.html">ZINCRBY key increment member</a> <br>有序集合中对指定成员的分数加上增量 increment</td></tr>
<tr><td>5</td><td><a href="/redis/sorted-sets-zinterstore.html">ZINTERSTORE destination numkeys key [key ...]</a> <br>计算给定的一个或多个有序集的交集并将结果集存储在新的有序集合 key 中</td></tr>
<tr><td>6</td><td><a href="/redis/sorted-sets-zlexcount.html">ZLEXCOUNT key min max</a> <br>在有序集合中计算指定字典区间内成员数量</td></tr>
<tr><td>7</td><td><a href="/redis/sorted-sets-zrange.html">ZRANGE key start stop [WITHSCORES]</a> <br>通过索引区间返回有序集合成指定区间内的成员</td></tr>
<tr><td>8</td><td><a href="/redis/sorted-sets-zrangebylex.html">ZRANGEBYLEX key min max [LIMIT offset count]</a> <br>通过字典区间返回有序集合的成员</td></tr>
<tr><td>9</td><td><a href="/redis/sorted-sets-zrangebyscore.html">ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT]</a> <br>通过分数返回有序集合指定区间内的成员</td></tr>
<tr><td>10</td><td><a href="/redis/sorted-sets-zrank.html">ZRANK key member</a> <br>返回有序集合中指定成员的索引</td></tr>
<tr><td>11</td><td><a href="/redis/sorted-sets-zrem.html">ZREM key member [member ...]</a> <br>移除有序集合中的一个或多个成员</td></tr>
<tr><td>12</td><td><a href="/redis/sorted-sets-zremrangebylex.html">ZREMRANGEBYLEX key min max</a> <br>移除有序集合中给定的字典区间的所有成员</td></tr>
<tr><td>13</td><td><a href="/redis/sorted-sets-zremrangebyrank.html">ZREMRANGEBYRANK key start stop</a> <br>移除有序集合中给定的排名区间的所有成员</td></tr>
<tr><td>14</td><td><a href="/redis/sorted-sets-zremrangebyscore.html">ZREMRANGEBYSCORE key min max</a> <br>移除有序集合中给定的分数区间的所有成员</td></tr>
<tr><td>15</td><td><a href="/redis/sorted-sets-zrevrange.html">ZREVRANGE key start stop [WITHSCORES]</a> <br>返回有序集中指定区间内的成员，通过索引，分数从高到底</td></tr>
<tr><td>16</td><td><a href="/redis/sorted-sets-zrevrangebyscore.html">ZREVRANGEBYSCORE key max min [WITHSCORES]</a> <br>返回有序集中指定分数区间内的成员，分数从高到低排序</td></tr>
<tr><td>17</td><td><a href="/redis/sorted-sets-zrevrank.html">ZREVRANK key member</a> <br>返回有序集合中指定成员的排名，有序集成员按分数值递减(从大到小)排序</td></tr>
<tr><td>18</td><td><a href="/redis/sorted-sets-zscore.html">ZSCORE key member</a> <br>返回有序集中，成员的分数值</td></tr>
<tr><td>19</td><td><a href="/redis/sorted-sets-zunionstore.html">ZUNIONSTORE destination numkeys key [key ...]</a> <br>计算给定的一个或多个有序集的并集，并存储在新的 key 中</td></tr>
<tr><td>20</td><td><a href="/redis/sorted-sets-zscan.html">ZSCAN key cursor [MATCH pattern] [COUNT count]</a> <br>迭代有序集合中的元素（包括元素成员和元素分值）</td></tr>
</tbody></table>

## **Redis HyperLogLog**

Redis HyperLogLog 是用来做基数统计的算法，HyperLogLog 的优点是，在输入元素的数量或者体积非常非常大时，计算基数所需的空间总是固定 的、并且是很小的。

在 Redis 里面，每个 HyperLogLog 键只需要花费 12 KB 内存，就可以计算接近 2^64 个不同元素的基 数。这和计算基数时，元素越多耗费内存就越多的集合形成鲜明对比。

但是，因为 HyperLogLog 只会根据输入元素来计算基数，而不会储存输入元素本身，所以 HyperLogLog 不能像集合那样，返回输入的各个元素。

### 详细参数

<table class="reference">
<tbody><tr><th style="width:5%">序号</th><th>命令及描述</th></tr>
<tr><td>1</td><td><a href="/redis/hyperloglog-pfadd.html">PFADD key element [element ...]</a> <br>添加指定元素到 HyperLogLog 中。</td></tr>
<tr><td>2</td><td><a href="/redis/hyperloglog-pfcount.html">PFCOUNT key [key ...]</a> <br>返回给定 HyperLogLog 的基数估算值。</td></tr>
<tr><td>3</td><td><a href="/redis/hyperloglog-pfmerge.html">PFMERGE destkey sourcekey [sourcekey ...]</a> <br>将多个 HyperLogLog 合并为一个 HyperLogLog </td></tr>
</tbody></table>

`PFMERGE`

Redis PFMERGE 命令将多个 HyperLogLog 合并为一个 HyperLogLog ，合并后的 HyperLogLog 的基数估算值是通过对所有 给定 HyperLogLog 进行并集计算得出的。

## Redis 发布订阅

### 示例

订阅 `redisChat`

```sh
127.0.0.1:6379> SUBSCRIBE redisChat
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "redisChat"
3) (integer) 1
```

另开一个终端 `redis-cli` 发布消息

```sh
127.0.0.1:6379> PUBLISH redisChat "Redis is a great caching technique"
(integer) 1
```

此时第一个终端会接受到频道发布的消息

```sh
# 订阅者接收到消息如下
1) "message"
2) "redisChat"
3) "Redis is a great caching technique"
```

### 详细参数

<table class="reference">
<tbody><tr><th style="width:5%">序号</th><th>命令及描述</th></tr>
<tr><td>1</td><td><a href="/redis/pub-sub-psubscribe.html">PSUBSCRIBE pattern [pattern ...]</a> <br>订阅一个或多个符合给定模式的频道。</td></tr>
<tr><td>2</td><td><a href="/redis/pub-sub-pubsub.html">PUBSUB subcommand [argument [argument ...]]</a> <br>查看订阅与发布系统状态。</td></tr>
<tr><td>3</td><td><a href="/redis/pub-sub-publish.html">PUBLISH channel message</a> <br>将信息发送到指定的频道。</td></tr>
<tr><td>4</td><td><a href="/redis/pub-sub-punsubscribe.html">PUNSUBSCRIBE [pattern [pattern ...]]</a> <br>退订所有给定模式的频道。 </td></tr>
<tr><td>5</td><td><a href="/redis/pub-sub-subscribe.html">SUBSCRIBE channel [channel ...]</a> <br>订阅给定的一个或多个频道的信息。</td></tr>
<tr><td>6</td><td><a href="/redis/pub-sub-unsubscribe.html">UNSUBSCRIBE [channel [channel ...]]</a> <br>指退订给定的频道。</td></tr>
</tbody></table>

## Redis 事务

单个 Redis 命令的执行是原子性的，但 Redis 没有在事务上增加任何维持原子性的机制，所以 Redis 事务的执行并不是原子性的。

事务可以理解为一个打包的批量执行脚本，但批量指令并非原子化的操作，中间某条指令的失败不会导致前面已做指令的回滚，也不会造成后续的指令不做。

### 详细参数

<table class="reference">
<tbody><tr><th style="width:5%">序号</th><th>命令及描述</th></tr>
<tr><td>1</td><td><a href="/redis/transactions-discard.html">DISCARD</a> <br>取消事务，放弃执行事务块内的所有命令。</td></tr>
<tr><td>2</td><td><a href="/redis/transactions-exec.html">EXEC</a> <br>执行所有事务块内的命令。</td></tr>
<tr><td>3</td><td><a href="/redis/transactions-multi.html">MULTI</a> <br>标记一个事务块的开始。</td></tr>
<tr><td>4</td><td><a href="/redis/transactions-unwatch.html">UNWATCH</a> <br>取消 WATCH 命令对所有 key 的监视。</td></tr>
<tr><td>5</td><td><a href="/redis/transactions-watch.html">WATCH key [key ...]</a> <br>监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断。</td></tr>
</tbody></table>

⚠️ (error) ERR WATCH inside MULTI is not allowed

## Redis 脚本

### 详细参数

<table class="reference">
<tbody><tr><th style="width:5%">序号</th><th>命令及描述</th></tr>
<tr><td>1</td><td><a href="/redis/scripting-eval.html">EVAL script numkeys key [key ...] arg [arg ...]</a> <br>执行 Lua 脚本。</td></tr>
<tr><td>2</td><td><a href="/redis/scripting-evalsha.html">EVALSHA sha1 numkeys key [key ...] arg [arg ...]</a> <br>执行 Lua 脚本。</td></tr>
<tr><td>3</td><td><a href="/redis/scripting-script-exists.html">SCRIPT EXISTS script [script ...]</a> <br>查看指定的脚本是否已经被保存在缓存当中。</td></tr>
<tr><td>4</td><td><a href="/redis/scripting-script-flush.html">SCRIPT FLUSH</a> <br>从脚本缓存中移除所有脚本。</td></tr>
<tr><td>5</td><td><a href="/redis/scripting-script-kill.html">SCRIPT KILL</a> <br>杀死当前正在运行的 Lua 脚本。</td></tr>
<tr><td>6</td><td><a href="/redis/scripting-script-load.html">SCRIPT LOAD script</a> <br>将脚本 script 添加到脚本缓存中，但并不立即执行这个脚本。</td></tr>
</tbody></table>

## Redis 连接

### 详细参数

<table class="reference">
<tbody><tr><th style="width:5%">序号</th><th>命令及描述</th></tr>
<tr><td>1</td><td><a href="/redis/connection-auth.html">AUTH password</a> <br>验证密码是否正确</td></tr>
<tr><td>2</td><td><a href="/redis/connection-echo.html">ECHO message</a> <br>打印字符串</td></tr>
<tr><td>3</td><td><a href="/redis/connection-ping.html">PING</a> <br>查看服务是否运行</td></tr>
<tr><td>4</td><td><a href="/redis/connection-quit.html">QUIT</a> <br>关闭当前连接</td></tr>
<tr><td>5</td><td><a href="/redis/connection-select.html">SELECT index</a> <br>切换到指定的数据库</td></tr>
</tbody></table>

## Redis 服务器

> Redis 服务器命令主要是用于管理 redis 服务。

### 详细参数

<table class="reference">
<tbody><tr><th style="width:5%">序号</th><th>命令及描述</th></tr>
<tr><td>1</td><td><a href="/redis/server-bgrewriteaof.html">BGREWRITEAOF</a> <br>异步执行一个 AOF（AppendOnly File） 文件重写操作</td></tr>
<tr><td>2</td><td><a href="/redis/server-bgsave.html">BGSAVE</a> <br>在后台异步保存当前数据库的数据到磁盘</td></tr>
<tr><td>3</td><td><a href="/redis/server-client-kill.html">CLIENT KILL [ip:port] [ID client-id]</a>  <br>关闭客户端连接</td></tr>
<tr><td>4</td><td><a href="/redis/server-client-list.html">CLIENT LIST</a> <br>获取连接到服务器的客户端连接列表</td></tr>
<tr><td>5</td><td><a href="/redis/server-client-getname.html">CLIENT GETNAME</a> <br>获取连接的名称</td></tr>
<tr><td>6</td><td><a href="/redis/server-client-pause.html">CLIENT PAUSE timeout</a> <br>在指定时间内终止运行来自客户端的命令</td></tr>
<tr><td>7</td><td><a href="/redis/server-client-setname.html">CLIENT SETNAME connection-name</a> <br>设置当前连接的名称</td></tr>
<tr><td>8</td><td><a href="/redis/server-cluster-slots.html">CLUSTER SLOTS</a> <br>获取集群节点的映射数组</td></tr>
<tr><td>9</td><td><a href="/redis/server-command.html">COMMAND</a> <br>获取 Redis 命令详情数组</td></tr>
<tr><td>10</td><td><a href="/redis/server-command-count.html">COMMAND COUNT</a> <br>获取 Redis 命令总数</td></tr>
<tr><td>11</td><td><a href="/redis/server-command-getkeys.html">COMMAND GETKEYS</a> <br>获取给定命令的所有键</td></tr>
<tr><td>12</td><td><a href="/redis/server-time.html">TIME</a> <br>返回当前服务器时间</td></tr>
<tr><td>13</td><td><a href="/redis/server-command-info.html">COMMAND INFO command-name [command-name ...]</a> <br>获取指定 Redis 命令描述的数组</td></tr>
<tr><td>14</td><td><a href="/redis/server-config-get.html">CONFIG GET parameter</a> <br>获取指定配置参数的值</td></tr>
<tr><td>15</td><td><a href="/redis/server-config-rewrite.html">CONFIG REWRITE</a> <br>对启动 Redis 服务器时所指定的 redis.conf 配置文件进行改写</td></tr>
<tr><td>16</td><td><a href="/redis/server-config-set.html">CONFIG SET parameter value</a> <br>修改 redis 配置参数，无需重启</td></tr>
<tr><td>17</td><td><a href="/redis/server-config-resetstat.html">CONFIG RESETSTAT</a> <br>重置 INFO 命令中的某些统计数据</td></tr>
<tr><td>18</td><td><a href="/redis/server-dbsize.html">DBSIZE</a> <br>返回当前数据库的 key 的数量</td></tr>
<tr><td>19</td><td><a href="/redis/server-debug-object.html">DEBUG OBJECT key</a> <br>获取 key 的调试信息</td></tr>
<tr><td>20</td><td><a href="/redis/server-debug-segfault.html">DEBUG SEGFAULT</a> <br>让 Redis 服务崩溃</td></tr>
<tr><td>21</td><td><a href="/redis/server-flushall.html">FLUSHALL</a> <br>删除所有数据库的所有key</td></tr>
<tr><td>22</td><td><a href="/redis/server-flushdb.html">FLUSHDB</a> <br>删除当前数据库的所有key</td></tr>
<tr><td>23</td><td><a href="/redis/server-info.html">INFO [section]</a> <br>获取 Redis 服务器的各种信息和统计数值</td></tr>
<tr><td>24</td><td><a href="/redis/server-lastsave.html">LASTSAVE</a> <br>返回最近一次 Redis 成功将数据保存到磁盘上的时间，以 UNIX 时间戳格式表示</td></tr>
<tr><td>25</td><td><a href="/redis/server-monitor.html">MONITOR</a> <br>实时打印出 Redis 服务器接收到的命令，调试用</td></tr>
<tr><td>26</td><td><a href="/redis/server-role.html">ROLE</a> <br>返回主从实例所属的角色</td></tr>
<tr><td>27</td><td><a href="/redis/server-save.html">SAVE</a> <br>同步保存数据到硬盘</td></tr>
<tr><td>28</td><td><a href="/redis/server-shutdown.html">SHUTDOWN [NOSAVE] [SAVE]</a> <br>异步保存数据到硬盘，并关闭服务器</td></tr>
<tr><td>29</td><td><a href="/redis/server-slaveof.html">SLAVEOF host port</a> <br>将当前服务器转变为指定服务器的从属服务器(slave server)</td></tr>
<tr><td>30</td><td><a href="/redis/server-showlog.html">SLOWLOG subcommand [argument]</a> <br>管理 redis 的慢日志</td></tr>
<tr><td>31</td><td><a href="/redis/server-sync.html">SYNC</a> <br> 用于复制功能(replication)的内部命令</td></tr>

</tbody></table>

## Redis 数据备份与恢复

### 保存数据

Redis SAVE 命令用于创建当前数据库的备份。

该命令将在 redis 安装目录中创建dump.rdb文件。

### 恢复数据

如果需要恢复数据，只需将备份文件 (dump.rdb) 移动到 redis 安装目录并启动服务即可。获取 redis 目录可以使用 CONFIG 命令，如下所示：

```sh
127.0.0.1:6379> CONFIG GET dir
1) "dir"
2) "/data"
```

所以目录是 `/data`

### BGSAVE

在后台异步(Asynchronously)保存当前数据库的数据到磁盘。

BGSAVE 命令执行之后立即返回 OK ，然后 Redis fork 出一个新子进程，原来的 Redis 进程(父进程)继续处理客户端请求，而子进程则负责将数据保存到磁盘，然后退出。

客户端可以通过 LASTSAVE 命令查看相关信息，判断 BGSAVE 命令是否执行成功。

```sh
127.0.0.1:6379> BGSAVE
Background saving started
```

### LASTSAVE

返回最近一次 Redis 成功将数据保存到磁盘上的时间，以 UNIX 时间戳格式表示。

返回值：一个 UNIX 时间戳。

```sh
127.0.0.1:6379> LASTSAVE
(integer) 1547111021
```

## Redis 安全

我们可以通过 redis 的配置文件设置密码参数，这样客户端连接到 redis 服务就需要密码验证，这样可以让你的 redis 服务更安全。

```sh
127.0.0.1:6379> CONFIG get requirepass
1) "requirepass"
2) ""
```

### 设置密码

```sh
127.0.0.1:6379> CONFIG set requirepass redis
OK
# 认证
127.0.0.1:6379> AUTH redis
OK
127.0.0.1:6379> CONFIG get requirepass
1) "requirepass"
2) "redis"
# 如果验证失败
127.0.0.1:6379> auth java
(error) ERR invalid password
127.0.0.1:6379> CONFIG get requirepass
(error) NOAUTH Authentication required.
```

~~📒  我居然找不到怎么取消密码验证。。~~

其实很简单

```sh
CONFIG SET requirepass ''
```

OK

## Redis 性能测试

### 详细参数

<table class="reference">
<tbody><tr><th style="width:5%">序号</th><th style="width:10%">选项</th><th>描述</th><th style="width:20%">默认值</th></tr>
<tr>
<td>1</td>
<td><b>-h</b></td>
<td>指定服务器主机名</td>
<td>127.0.0.1</td>
</tr>
<tr>
<td>2</td>
<td><b>-p</b></td>
<td>指定服务器端口</td>
<td>6379</td>
</tr>
<tr>
<td>3</td>
<td><b>-s</b></td>
<td>指定服务器 socket</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td><b>-c</b></td>
<td>指定并发连接数</td>
<td>50</td>
</tr>
<tr>
<td>5</td>
<td><b>-n</b></td>
<td>指定请求数</td>
<td>10000</td>
</tr>
<tr>
<td>6</td>
<td><b>-d</b></td>
<td>以字节的形式指定 SET/GET 值的数据大小</td>
<td>2</td>
</tr>
<tr>
<td>7</td>
<td><b>-k</b></td>
<td>1=keep alive 0=reconnect</td>
<td>1</td>
</tr>
<tr>
<td>8</td>
<td><b>-r</b></td>
<td> SET/GET/INCR 使用随机 key, SADD 使用随机值</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td><b>-P</b></td>
<td>通过管道传输 &lt;numreq&gt; 请求</td>
<td>1</td>
</tr>

<tr>
<td>10</td>
<td><b>-q</b></td>
<td>强制退出 redis。仅显示 query/sec 值</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td><b>--csv</b></td>
<td>以 CSV 格式输出</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td><b>-l</b></td>
<td>生成循环，永久执行测试</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td><b>-t</b></td>
<td>仅运行以逗号分隔的测试命令列表。</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td><b>-I</b></td>
<td>Idle 模式。仅打开 N 个 idle 连接并等待。</td>
<td></td>
</tr>
</tbody></table>

```sh
./redis-benchmark -h 127.0.0.1 -p 6379 -t get -n 100000 -q
GET: 9301.46 requests per second

./redis-benchmark -h 127.0.0.1 -p 6379 -t set,lpush -n 10000 -q
SET: 10718.11 requests per second
LPUSH: 10570.83 requests per second
```

## redis 客户端连接

Redis 通过监听一个 TCP 端口或者 Unix socket 的方式来接收来自客户端的连接，当一个连接建立后，Redis 内部会进行以下一些操作：

-    首先，客户端 socket 会被设置为非阻塞模式，因为 Redis 在网络事件处理上采用的是非阻塞多路复用模型。
-    然后为这个 socket 设置 TCP_NODELAY 属性，禁用 Nagle 算法
-    然后创建一个可读的文件事件用于监听这个客户端 socket 的数据发送

### 最大连接数

`config get maxclients`

在服务启动时设置最大连接数为 100000：

`redis-server --maxclients 100000`

### 详细参数

<table class="reference">
<tbody><tr><th style="width:5%">S.N.</th><th style="width:10%">命令</th><th>描述</th></tr>
<tr>
<td>1</td>
<td><b>CLIENT LIST</b></td>
<td>返回连接到 redis 服务的客户端列表</td>
</tr>
<tr>
<td>2</td>
<td><b>CLIENT SETNAME</b></td>
<td>设置当前连接的名称</td>
</tr>
<tr>
<td>3</td>
<td><b>CLIENT GETNAME</b></td>
<td>获取通过 CLIENT SETNAME 命令设置的服务名称</td>
</tr>
<tr>
<td>4</td>
<td><b>CLIENT PAUSE</b></td>
<td>挂起客户端连接，指定挂起的时间以毫秒计</td>
</tr>
<tr>
<td>5</td>
<td><b>CLIENT KILL</b></td>
<td>关闭客户端连接</td>
</tr>
</tbody></table>

## Redis 管道技术

Redis是一种基于客户端-服务端模型以及请求/响应协议的TCP服务。这意味着通常情况下一个请求会遵循以下步骤：

客户端向服务端发送一个查询请求，并监听Socket返回，通常是以阻塞模式，等待服务端响应。
服务端处理命令，并将结果返回给客户端。

### 管道

Redis 管道技术可以在服务端未响应时，客户端可以继续向服务端发送请求，并最终一次性读取所有服务端的响应。

```sh
$(echo -en "PING\r\n SET runoobkey redis\r\nGET runoobkey\r\nINCR visitor\r\nINCR visitor\r\nINCR visitor\r\n"; sleep 10) | nc localhost 6379

+PONG
+OK
redis
:1
:2
:3
```

> 管道技术最显著的优势是提高了 redis 服务的性能。

## Redis 分区

分区是分割数据到多个Redis实例的处理过程，因此每个实例只保存key的一个子集。

### 分区类型

Redis 有两种类型分区。 假设有4个Redis实例 R0，R1，R2，R3，和类似user:1，user:2这样的表示用户的多个key，对既定的key有多种不同方式来选择这个key存放在哪个实例中。也就是说，有不同的系统来映射某个key到某个Redis服务。

#### 范围分区

最简单的分区方式是按范围分区，就是映射一定范围的对象到特定的Redis实例。

比如，ID从0到10000的用户会保存到实例R0，ID从10001到 20000的用户会保存到R1，以此类推。

这种方式是可行的，并且在实际中使用，不足就是要有一个区间范围到实例的映射表。这个表要被管理，同时还需要各 种对象的映射表，通常对Redis来说并非是好的方法。

#### 哈希分区

另外一种分区方法是hash分区。这对任何key都适用，也无需是object_name:这种形式，像下面描述的一样简单：

用一个hash函数将key转换为一个数字，比如使用crc32 hash函数。对key foobar执行crc32(foobar)会输出类似93024922的整数。

对这个整数取模，将其转化为0-3之间的数字，就可以将这个整数映射到4个Redis实例中的一个了。93024922 % 4 = 2，就是说key foobar应该被存到R2实例中。注意：取模操作是取除的余数，通常在多种编程语言中用%操作符实现。

## 参考文档

-    [Redis 命令参考](http://redisdoc.com/index.html)
-    [菜鸟教程](http://www.runoob.com/redis/redis-tutorial.html)
