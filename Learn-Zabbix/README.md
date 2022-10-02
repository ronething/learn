![](https://i.loli.net/2019/01/07/5c331af49473e.png)

# 学习 zabbix4.0

⚠️ [中文文档地址](https://www.zabbix.com/documentation/4.0/zh/manual) 不过翻译滞后了，更新的比较慢 [英文文档地址](https://www.zabbix.com/documentation/4.0/manual)比较好点

## 简介

### [手册目录结构](https://www.zabbix.com/documentation/4.0/zh/manual/introduction/manual_structure)

### Zabbix 介绍

- Zabbix 是一个企业级分布式开源监控解决方案。

- Zabbix 软件能够监控众多网络参数和服务器的健康度、完整性。Zabbix 使用灵活的告警机制，允许用户为几乎任何事件配置基于邮件的告警。这样用户可以快速响应服务器问题。Zabbix 基于存储的数据提供出色的报表和数据可视化功能。

- Zabbix 支持主动轮询和被动捕获。所有的 Zabbix 报告、统计信息和配置参数都可以通过基于 Web 的前端页面进行访问。基于 Web 的前端页面确保您的网络状态和服务器健康状况等可以从任何地方访问。

### [Zabbix 功能](https://www.zabbix.com/documentation/4.0/zh/manual/introduction/features)

-   数据采集
-   灵活的阈值定义
-   高度可配置化的告警
-   实时图形
-   Web 监控功能
-   丰富的可视化选项
-   历史数据存储
-   配置简单
-   套用模板
-   网络发现
-   快捷的 Web 界面
-   Zabbix API
-   权限管理系统
-   权限管理系统
-   功能强大且易于扩展的 Zabbix Agent
-   二进制守护进程
-   适应更复杂的环境

### [Zabbix 概述](https://www.zabbix.com/documentation/4.0/zh/manual/introduction/overview)

> Zabbix 由几个主要的功能组件组成:

-   Server
-   数据库
-   Web 界面
-   Proxy
    -   Zabbix proxy 可以替 Zabbix server 收集性能和可用性数据。Zabbix proxy 是 Zabbix 环境部署的可选部分；然而，它对于单个 Zabbix server 负载的分担是非常有益的。
-   Agent
-   数据流(感觉类似于flow 有触发条件之类的)


### [Zabbix 4.0.0 新特征](https://www.zabbix.com/documentation/4.0/manual/introduction/whatsnew400)

-   改进的仪表板
-   添加了另一个默认仪表板，专注于显示Zabbix服务器性能：Zabbix服务器运行状况 默认情况下， 此仪表板仅与Zabbix管理员组共享。
-   立即检索指标 ⚠️ 检查新值时，不会更新配置缓存，因此这些值不会反映项目/发现规则配置的最新更改。因此，也无法检查刚刚创建的项目/规则的新值。
-   新的HTTP项类型
    -   引入了新的HTTP项类型，允许使用HTTP / HTTPS协议进行数据轮询。
-   新模板
    -   新模板可用于监控某些IBM，Dell，HP，Cisco UCS和Supermicro Aten硬件
-   Item prototypes can depend on regular items
-   Low-level discovery macros in item preprocessing
-   Substring extraction of low-level discovery macro value
-   触发级别的主机维护
-   使用webserver进行单点登录
-   更灵活的活动代理自动注册
-   支持MySQL 8.0
-   Elasticsearch的基于日期的索引设置
-   更安全的代理连接
-   可以更改问题严重性
-   处理问题
-   新的图形小部件
-   时间选择器重新设计
-   前端页面的Kiosk模式
-   紧凑的问题视图
-   监控→已删除触发器
    -   在监视 → 问题成为需要查看当前问题的首选部分时，已决定从“监视”菜单中删除“ 触发器”部分。
-   Inventory macro support in event tags
-   灵活地防止单位转换
    -   In the new version, any unit can be prevented from being converted by using a ! prefix, for example !B
        ```
        1024 !B -> 1024 B
        1024 B -> 1 KB
        61 !s -> 61 s
        61 s -> 1m 1s
        0 !uptime -> 0 uptime
        0 uptime -> 00:00:00
        0 !! -> 0 !
        0 ! -> 0
        ```
-   一个用户媒体中的多封电子邮件
-   Real-time export of events, values, trends
-   基于标签的权限
-   服务器代理通信的压缩
    -   压缩可降低带宽要求并提高数据传输速度。[Zlib](https://zlib.net/) library is required for compression support.
-   Improved database down messages
-   Use of "not" keyword
    
    ![](https://i.loli.net/2019/01/06/5c31941fd1171.png)
-   Items
    -   New items
    -   Updated items
    -   JMX monitoring
    -   External script argument wrapping
    -   Searching IPMI sensor by full name
-   触发器
    -   时间触发器由历史同步器处理
    -   Miscellaneous
-   前端
    -   必填字段标记
    -   键盘导航
    -   日期选择器重新设计
    -   颜色选择器重新设计
        
        颜色选择器经过重新设计，提供更大的颜色选择
    -   弹出窗口由叠加对话框替换
-   过滤
    -   通过标签过滤更灵活的问题
    -   主机列表
    -   物品清单
-   触发器配置列表中显示的触发值
-   Renamed operators
-   Renamed widgets, screen elements and reports
-   Multiple item support in plain text widget
-   事件状态颜色调整
-   “主机质量更新”表单中的更改
-   “用户媒体”表单中的更改
-   Twin boxes replaced with auto-select
-   改进的小部件配置
-   小部件中的图形视觉改进
-   前端顶部栏菜单改进
-   无障碍
-   高对比度主题
-   守护进程
-   API improvements
    
    From now on [user.checkAuthentication](https://www.zabbix.com/documentation/4.0/manual/api/reference/user/user.checkauthentication) method contains additional parameter “extend”.

## [定义](https://www.zabbix.com/documentation/4.0/manual/definitions)

-   主机（host）
    
    你想要监控的联网设备，有IP/DNS。

-   主机组（host group)
    
    主机的逻辑组；可能包含主机和模板。一个主机组里的主机和模板之间并没有任何直接的关联。通常在给不同用户组的主机分配权限时候使用主机组。

-   监控项（item）

    你想要接收的主机的特定数据，一个度量/指标数据。

-   值预处理（value preprocessing）

    转化/预处理接收到的指标数据 存入数据库之前。

-   触发器（trigger）

    一个被用于定义问题阈值和“评估”监控项接收到的数据的逻辑表达式。
    
    当接收到的数据高于阈值时，触发器从“OK”变成“Problem”状态。当接收到的数据低于阈值时，触发器保留/返回“OK”的状态。

-   事件（event）

    一次发生的需要注意的事情，例如触发器状态改变、发现/监控代理自动注册

-   事件标签（event tag）

    提前设置的事件标记可以被用于事件关联，权限细化设置等。

-   事件关联（event correlation）

    自动灵活的、精确的关联问题和解决方案

    比如说，你可以定义触发器A告警的异常可以由触发器B解决，触发器B可能采用完全不同的数据采集方式。

-   异常（problems）

    一个处在“异常”状态的触发器

-   异常更新（problem update）

    Zabbix提供的问题管理选项，例如添加评论、确认异常、改变问题级别或者手动关闭等。

-   动作（action）

    预先定义的应对事件的操作

    一个动作由操作(例如发出通知)和条件(什么时间进行操作)组成

-   升级（escalation）

    一个在动作内执行操作的自定义方式; 发送通知/执行远程命令的顺序安排。

-   媒介（media）
    
    发送告警通知的方式；传送途径

-   通知（notification）

    关于事件的信心，将通过选设定的媒介途径发送给用户。

-   远程命令（remote command）

    一个预定义好的，满足特定条件的情况下，可以在被监控主机上自动执行的命令。

-   模版（template）

    一组可以被应用到一个或多个主机上的实体（监控项，触发器，图形，聚合图形，应用，LLD，Web场景）的集合

    模版的应用使得主机上的监控任务部署快捷方便；也可以使监控任务的批量修改更加简单。模版是直接关联到每台单独的主机上。

-   应用（application）

    一组监控项组成的逻辑分组

-   Web场景（web scenario）

    检查网站可浏览性的一个或多个HTTP请求

-   前端（frontend)

    Zabbix提供的web界面

-   Zabbix API

    Zabbix API允许用户使用JSON RPC协议来创建、更新和获取Zabbix对象（如主机、监控项、图形和其他）信息或者执行任何其他的自定义的任务

-   Zabbix server

    Zabbix监控的核心程序，主要功能是与Zabbix proxies和Agents进行交互、触发器计算、发送告警通知；并将数据集中保存等

-   Zabbix agent

    部署在监控对象上的，能够主动监控本地资源和应用的程序

-   Zabbix proxy

    一个帮助Zabbix Server收集数据，分担Zabbix Server的负载的程序

-   加密（encryption）

    支持Zabbix组建之间的加密通讯(server, proxy, agent, zabbix_sender 和 zabbix_get 程序) 使用TLS（Transport Layer Security ）协议。

## [Zabbix processes](https://www.zabbix.com/documentation/4.0/manual/concepts)

### [Server](https://www.zabbix.com/documentation/4.0/manual/concepts/server)

#### 概述

-   基本的 Zabbix Server 的功能分解成为三个不同的组件。他们是：Zabbix server、Web前端和数据库。

-   Zabbix Server 负责执行数据的主动轮询和被动获取，计算触发器条件，向用户发送通知。它是 Zabbix Agent 和 Proxy 报告系统可用性和完整性数据的核心组件。Server 自身可以通过简单服务远程检查网络服务（如Web服务器和邮件服务器）。Zabbix Server是所有配置、统计和操作数据的中央存储中心，也是Zabbix监控系统的告警中心。在监控的系统中出现任何异常，将被发出通知给管理员。

-   Zabbix 的所有配置信息都存储在 Server 和Web前端进行交互的数据库中。例如，当你通过Web前端（或者API）新增一个监控项时，它会被添加到数据库的监控项表里。然后，Zabbix server 以每分钟一次的频率查询监控项表中的有效项，接着将它存储在 Zabbix server 中的缓存里。这就是为什么 Zabbix 前端所做的任何更改需要花费两分钟左右才能显示在最新的数据段的原因。

#### Running server

##### 通过二进制包安装的组件

> Zabbix server 进程以守护进程（Deamon）运行。Zabbix server 的启动可以通过执行以下命令来完成：

```sh
shell> service zabbix-server start

or

shell> /etc/init.d/zabbix-server start

# 类似的，停止、重启、查看状态，则需要执行以下命令：
shell> service zabbix-server stop
shell> service zabbix-server restart
shell> service zabbix-server status
```

##### 手动启动

```sh
# 如果以上操作均无效，您可能需要手动启动，找到 Zabbix Server 二进制文件的路径并且执行：
shell> zabbix_server

# 可以将以下命令行参数用于 Zabbix server
-c --config <file>              配置文件路径（默认的是 /usr/local/etc/zabbix_server.conf）
-R --runtime-control <option>   执行管理功能
-h --help                       帮助
-V --version                    显示版本号

# 示例
shell> zabbix_server -c /usr/local/etc/zabbix_server.conf
shell> zabbix_server --help
shell> zabbix_server -V
```

##### 运行时控制

<table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0">Option</th><th class="col1">Description</th><th class="col2">Target</th>
	</tr>
	</thead>
	<tbody><tr class="row1">
		<td class="col0">config_cache_reload</td><td class="col1">Reload configuration cache. Ignored if cache is being currently loaded.</td><td class="col2"> </td>
	</tr>
	<tr class="row2">
		<td class="col0">housekeeper_execute</td><td class="col1">Start the housekeeping procedure. Ignored if the housekeeping procedure is currently in progress.</td><td class="col2"> </td>
	</tr>
	<tr class="row3">
		<td class="col0">log_level_increase[=&lt;<strong>target</strong>&gt;]</td><td class="col1">Increase log level, affects all processes if target is not specified.</td><td class="col2" rowspan="2"><strong>process type</strong> - All processes of specified type (e.g., poller)<br>
See all <a href="#server_process_types" title="manual:concepts:server ↵" class="wikilink1">server process types</a>.<br>
<strong>process type,N</strong> - Process type and number (e.g., poller,3)<br>
<strong>pid</strong> - Process identifier (1 to 65535). For larger values specify target as 'process type,N'.</td>
	</tr>
	<tr class="row4">
		<td class="col0">log_level_decrease[=&lt;<strong>target</strong>&gt;]</td><td class="col1">Decrease log level, affects all processes if target is not specified.</td>
	</tr>
</tbody></table>

例如，使用 config_cache_reload 选项重新加载 server 的配置缓存：

```sh
shell> zabbix_server -c /usr/local/etc/zabbix_server.conf -R config_cache_reload
```

例如，使用 housekeeper_execute 选项来触发管家服务执行：

```sh
shell> zabbix_server -c /usr/local/etc/zabbix_server.conf -R housekeeper_execute
```

增加所有进程的日志级别：

```sh
shell> zabbix_server -c /usr/local/etc/zabbix_server.conf -R log_level_increase
```

增加第二个 Poller 进程的日志级别：

```sh
shell> zabbix_server -c /usr/local/etc/zabbix_server.conf -R log_level_increase=poller,2
```

增加 PID 为 1234 进程的日志级别：

```sh
shell> zabbix_server -c /usr/local/etc/zabbix_server.conf -R log_level_increase=1234
```

降低 `http poller` 进程的日志级别：

```sh
shell> zabbix_server -c /usr/local/etc/zabbix_server.conf -R log_level_decrease="http poller"
```

##### 进程用户

Zabbix server 允许使用非 root 用户运行。它将以任何非 root 用户的身份运行。因此，使用非 root 用户运行 server 是没有任何问题的.

如果你试图以“root”身份运行它，它将会切换到一个已经“写死”的“zabbix”用户，您可以参考 安装 章节。按此相应地修改 Zabbix server 配置文件中的“AllowRoot”参数，则可以只以“root”身份运行 Zabbix server。

如果 Zabbix server 和 agent 均运行在同一台服务器上，建议您使用不同的用户运行 server 和 agent 。否则,，如果两者都以相同的用户运行，Agent 可以访问 Server 的配置文件, 任何 Zabbix 管理员级别的用户都可以很容易地检索到 Server 的信息。例如，数据库密码。

##### [配置文件](https://www.zabbix.com/documentation/4.0/manual/appendix/config/zabbix_server)

##### 启动脚本

这些脚本用于在系统启动和关闭期间自动启动和停止 Zabbix 进程。 此脚本位于 misc/init.d 目录下。

##### 服务器进程类型

-   alert manager - manager of alerter tasks
-   alerter - process for sending notifications
-   configuration syncer - process for managing in-memory cache of configuration data
-   discoverer - process for discovery of devices
-   escalator - process for escalation of actions
-   history syncer - history DB writer
-   housekeeper - process for removal of old historical data
-   http poller - web monitoring poller
-   icmp pinger - poller for icmpping checks
-   ipmi manager - IPMI poller manager
-   ipmi poller - poller for IPMI checks
-   java poller - poller for Java checks
-   poller - normal poller for passive checks
-   preprocessing manager - manager of preprocessing tasks
-   preprocessing worker - process for data preprocessing
-   proxy poller - poller for passive proxies
-   self-monitoring - process for collecting internal server statistics
-   snmp trapper - trapper for SNMP traps
-   task manager - process for remote execution of tasks requested by other components (e.g. close problem, acknowledge problem, check item value now, remote command functionality)
-   timer - timer for processing maintenances
-   trapper - trapper for active checks, traps, proxy communication
-   unreachable poller - poller for unreachable devices
-   vmware collector - VMware data collector responsible for data gathering from VMware services

### [Agent](https://www.zabbix.com/documentation/4.0/zh/manual/concepts/agent)

#### 概述

-   Zabbix agent 部署在被监控目标上，以主动监控本地资源和应用程序（硬盘、内存、处理器统计信息等）。

-   Zabbix agent 收集本地的操作信息并将数据报告给 Zabbix server 用于进一步处理。一旦出现异常 (例如硬盘空间已满或者有崩溃的服务进程)，Zabbix server 会主动警告管理员指定机器上的异常。

-   Zabbix agents 的极高效率缘于它可以利用**本地系统调用**来完成统计数据的采集。

#### 被动和主动检查

-   在被动检查 模式中 agent 应答数据请求。Zabbix server（或 proxy）询求数据，例如 CPU load，然后 Zabbix agent 返还结果。

-   主动检查 处理过程将相对复杂。Agent 必须首先从 Zabbix sever 索取监控项列表以进行独立处理，然后会定期发送采集到的新值给 Zabbix server。

##### 通过二进制包安装的组件

Zabbix agent 进程以守护进程（Deamon）运行。Zabbix agent 的启动可以通过执行以下命令来完成：

```sh
shell> service zabbix-agent start

or

shell> /etc/init.d/zabbix-agent start

# 类似的，停止、重启、查看状态，则需要执行以下命令：

shell> service zabbix-agent stop
shell> service zabbix-agent restart
shell> service zabbix-agent status
```

##### 手动启动

```sh
# 找到 Zabbix agent 二进制文件的路径并且执行：

shell> zabbix_agentd
```

#### Windows 系统上的 Agent

> Windows 系统上的 Zabbix agent 作为一个Windows服务运行。

#### 其他 Agent 选项

##### 命令行参数

<table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0"><strong>参数</strong></th><th class="col1"><strong>描述</strong></th>
	</tr>
	<tr class="row1">
		<th class="col0 centeralign" colspan="2">  <strong>UNIX 和 Windows agent</strong>  </th>
	</tr>
	</thead>
	<tbody><tr class="row2">
		<td class="col0 leftalign">-c --config &lt;config-file&gt;  </td><td class="col1 leftalign">配置文件的绝对路径。<br>
您可以使用此选项来制定配置文件，而不是使用默认文件。<br>
在 UNIX 上，默认的配置文件是 /usr/local/etc/zabbix_agentd.conf 或 由 <a href="/documentation/4.0/manual/installation/install#installing_zabbix_daemons" class="wikilink1" title="manual:installation:install">compile-time</a> 中的 <em>--sysconfdir</em> 或  <em>--prefix</em> 变量来确定。 <br>
在 Windows上, 默认的配置文件是 c:\zabbix_agentd.conf  </td>
	</tr>
	<tr class="row3">
		<td class="col0 leftalign">-p --print  </td><td class="col1">输出已知的监控项并退出。<br>
<em>注意</em>： 要返回 <a href="/documentation/4.0/manual/config/items/userparameters" class="wikilink1" title="manual:config:items:userparameters">用户自定义参数</a> 的结果，您必须指定配置文件（如果它不在默认路径下）。 </td>
	</tr>
	<tr class="row4">
		<td class="col0 leftalign">-t --test &lt;item key&gt;  </td><td class="col1">测试指定的监控项并退出。<br>
<em>注意</em>：要返回 <a href="/documentation/4.0/manual/config/items/userparameters" class="wikilink1" title="manual:config:items:userparameters">用户自定义参数</a> 的结果，您必须指定配置文件（如果它不在默认路径下）。</td>
	</tr>
	<tr class="row5">
		<td class="col0 leftalign">-h --help  </td><td class="col1">显示帮助信息 </td>
	</tr>
	<tr class="row6">
		<td class="col0 leftalign">-V --version  </td><td class="col1 leftalign">显示版本号  </td>
	</tr>
	<tr class="row7">
		<th class="col0 centeralign" colspan="2">  <strong>仅 UNIX agent</strong>  </th>
	</tr>
	<tr class="row8">
		<td class="col0 leftalign">-R --runtime-control &lt;option&gt;  </td><td class="col1 leftalign">执行管理功能。请参阅 <a href="/documentation/4.0/manual/concepts/agent#runtime_control" class="wikilink1" title="manual:concepts:agent">运行时机制的控制</a>。  </td>
	</tr>
	<tr class="row9">
		<th class="col0 centeralign" colspan="2">  <strong>仅 Windows agent </strong>  </th>
	</tr>
	<tr class="row10">
		<td class="col0 leftalign">-m --multiple-agents  </td><td class="col1">使用多 Agent 实例（使用 -i、-d、-s、-x）。<br>
为了区分实例的服务名称，每项服务名都会包涵来自配置文件里的 Hostname 值。 </td>
	</tr>
	<tr class="row11">
		<th class="col0 centeralign" colspan="2">  <strong>仅 Windows agent （功能）</strong>  </th>
	</tr>
	<tr class="row12">
		<td class="col0 leftalign">-i --install  </td><td class="col1">以服务的形式安装 Zabbix Windows agent。</td>
	</tr>
	<tr class="row13">
		<td class="col0 leftalign">-d --uninstall  </td><td class="col1 leftalign">卸载 Zabbix indows agent 服务。  </td>
	</tr>
	<tr class="row14">
		<td class="col0 leftalign">-s --start  </td><td class="col1 leftalign">启动 Zabbix Windows agent 服务。  </td>
	</tr>
	<tr class="row15">
		<td class="col0 leftalign">-x --stop  </td><td class="col1 leftalign">停止 Zabbix Windows agent 服务。  </td>
	</tr>
</tbody></table>

```sh
# installing a “Zabbix Agent [Hostname]” service for Windows using the configuration file zabbix_agentd.conf located in the same folder as agent executable and make the service name unique by extending it by Hostname value from the config file

shell> zabbix_agentd.exe -i -m -c zabbix_agentd.conf
```

##### 运行时控制

<table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0">Option</th><th class="col1">Description</th><th class="col2">Target</th>
	</tr>
	</thead>
	<tbody><tr class="row1">
		<td class="col0 leftalign">log_level_increase[=&lt;target&gt;]  </td><td class="col1 leftalign">Increase log level.<br>
If target is not specified, all processes are affected.  </td><td class="col2 leftalign" rowspan="2">Target can be specified as:<br>
<strong>process type</strong> - all processes of specified type (e.g., listener)<br>
See all <a href="#agent_process_types" title="manual:concepts:agent ↵" class="wikilink1">agent process types</a>.<br>
<strong>process type,N</strong> - process type and number (e.g., listener,3)<br>
<strong>pid</strong> - process identifier (1 to 65535). For larger values specify target as 'process-type,N'.  </td>
	</tr>
	<tr class="row2">
		<td class="col0 leftalign">log_level_decrease[=&lt;target&gt;]  </td><td class="col1 leftalign">Decrease log level.<br>
If target is not specified, all processes are affected.  </td>
	</tr>
</tbody></table>

-   给所有进程增加日志级别。
-   给第三个监听进程增加日志级别。
-   给 PID 号为 1234 的进程增加日志级别。
-   给所有主动检查进程降低日志级别。

```sh
shell> zabbix_agentd -R log_level_increase
shell> zabbix_agentd -R log_level_increase=listener,3
shell> zabbix_agentd -R log_level_increase=1234
shell> zabbix_agentd -R log_level_decrease="active checks"
```

#### Agent process types

-   active checks - process for performing active checks
-   collector - process for data collection
-   listener - process for listening to passive checks

#### 进程用户

-   Zabbix agent 在 UNIX 上允许使用非 root 用户运行。它将以任何非 root 用户的身份运行。因此，使用非 root 用户运行 agent 是没有任何问题的.

-   如果你试图以“root”身份运行它，它将会切换到一个已经“写死”的“zabbix”用户，该用户必须存在于您的系统上。如果您只想以“root”用户运行 agent，您必须在 agent 配置文件里修改‘AllowRoot‘参数。

#### 配置文件 

-   [zabbix_agentd](https://www.zabbix.com/documentation/4.0/manual/appendix/config/zabbix_agentd)
-   [Windows agent](https://www.zabbix.com/documentation/4.0/manual/appendix/config/zabbix_agentd_win)

#### 语言环境

Zabbix agent 需要 `UTF-8` 语言环境，以便某些文本 Zabbix agent 监控项可以返回预期的内容。

#### Exit code

在 2.2 版之前，Zabbix agent 在成功退出时返回0，在异常时返回255。 从版本 2.2 及更高版本开始，Zabbix agent 在成功退出时返回0，在异常时返回1。

### [Proxy](https://www.zabbix.com/documentation/4.0/manual/concepts/proxy)

#### 概述

-   Zabbix proxy 是一个可以从一个或多个受监控设备采集监控数据并将信息发送到 Zabbix server 的进程，主要是代表 Zabbix server 工作。 所有收集的数据都在本地缓存，然后传输到 proxy 所属的 Zabbix server。

-   部署Zabbix proxy 是可选的，但可能非常有利于分担单个 Zabbix server 的负载。 如果只有代理采集数据，则 Zabbix server 上会减少 CPU 和磁盘 I/O 的开销。

-   Zabbix proxy 是无需本地管理员即可集中监控远程位置、分支机构和网络的理想解决方案。

-   Zabbix proxy 需要使用独立的数据库。⚠️ Zabbix proxy 支持 SQLite、MySQL和PostgreSQL 作为数据库。使用 Oracle 或 DB2 需要您承担一定的风险，例如，在自动发现规则中的遇到问题 [返回值](https://www.zabbix.com/documentation/4.0/manual/discovery/low_level_discovery#overview) 。

#### Running proxy

##### 通过二进制包安装的组件

Zabbix proxy 进程以守护进程（Deamon）运行。Zabbix proxy 的启动可以通过执行以下命令来完成：

```sh
shell> service zabbix-proxy start

or

shell> /etc/init.d/zabbix-proxy start

# 类似的，Zabbix proxy 的停止、重启、查看状态，则需要执行以下命令：

shell> service zabbix-proxy stop
shell> service zabbix-proxy restart
shell> service zabbix-proxy status
```

##### 手动启动

如果以上操作均无效，您可能需要手动启动，找到 Zabbix proxy 二进制文件的路径并且执行：

```sh
shell> zabbix_proxy
```

##### 命令行参数

```sh
-c --config <file>              配置文件路径
-R --runtime-control <option>   执行管理功能
-h --help                       帮助
-V --version                    显示版本号
```

使用命令行参数运行 Zabbix proxy 的示例:：

```sh
shell> zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf
shell> zabbix_proxy --help
shell> zabbix_proxy -V
```

##### 运行时控制

<table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0">Option</th><th class="col1">Description</th><th class="col2">Target</th>
	</tr>
	</thead>
	<tbody><tr class="row1">
		<td class="col0">config_cache_reload</td><td class="col1">Reload configuration cache. Ignored if cache is being currently loaded.<br>
Active Zabbix proxy will connect to the Zabbix server and request configuration data.</td><td class="col2"> </td>
	</tr>
	<tr class="row2">
		<td class="col0">housekeeper_execute</td><td class="col1">Start the housekeeping procedure. Ignored if the housekeeping procedure is currently in progress.</td><td class="col2"> </td>
	</tr>
	<tr class="row3">
		<td class="col0">log_level_increase[=&lt;<strong>target</strong>&gt;]</td><td class="col1">Increase log level, affects all processes if target is not specified.</td><td class="col2 leftalign" rowspan="2"><strong>process type</strong> - All processes of specified type (e.g., poller)<br>
See all <a href="#proxy_process_types" title="manual:concepts:proxy ↵" class="wikilink1">proxy process types</a>.<br>
<strong>process type,N</strong> - Process type and number (e.g., poller,3)<br>
<strong>pid</strong> - Process identifier (1 to 65535). For larger values specify target as 'process type,N'.  </td>
	</tr>
	<tr class="row4">
		<td class="col0">log_level_decrease[=&lt;<strong>target</strong>&gt;]</td><td class="col1">Decrease log level, affects all processes if target is not specified.</td>
	</tr>
</tbody></table>

例如，使用 config_cache_reload 选项重新加载 proxy 的配置缓存：

```sh
shell> zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf -R config_cache_reload
```

例如，使用 housekeeper_execute 选项来触发管家服务执行：

```
shell> zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf -R housekeeper_execute
```

```sh
# 增加所有进程的日志级别：

shell> zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf -R log_level_increase

# 增加第二个 Poller 进程的日志级别：

shell> zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf -R log_level_increase=poller,2

# 增加 PID 为 1234 进程的日志级别：

shell> zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf -R log_level_increase=1234

# 降低 http poller 进程的日志级别：

shell> zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf -R log_level_decrease="http poller"
```

##### 进程用户

-   Zabbix proxy 允许使用非 root 用户运行。它将以任何非 root 用户的身份运行。因此，使用非 root 用户运行 proxy 是没有任何问题的.

-   如果你试图以“root”身份运行它，它将会切换到一个已经“写死”的“zabbix”用户，该用户必须存在于您的系统上。如果您只想以“root”用户运行 proxy，您必须在 proxy 配置文件里修改‘AllowRoot‘参数。

是不是感觉和前面的差不多:)

我也觉得。。

##### [配置文件](https://www.zabbix.com/documentation/4.0/manual/appendix/config/zabbix_proxy)

#### Proxy process types

-   configuration syncer - process for managing in-memory cache of configuration data
-   data sender - proxy data sender
-   discoverer - process for discovery of devices
-   heartbeat sender - proxy heartbeat sender
-   history syncer - history DB writer
-   housekeeper - process for removal of old historical data
-   http poller - web monitoring poller
-   icmp pinger - poller for icmpping checks
-   ipmi manager - IPMI poller manager
-   ipmi poller - poller for IPMI checks
-   java poller - poller for Java checks
-   poller - normal poller for passive checks
-   self-monitoring - process for collecting internal server statistics
-   snmp trapper - trapper for SNMP traps
-   task manager - process for remote execution of tasks requested by other components (e.g. close problem, acknowledge problem, check item value now, remote command functionality)
-   trapper - trapper for active checks, traps, proxy communication
-   unreachable poller - poller for unreachable devices
-   vmware collector - VMware data collector responsible for data gathering from VMware services

#### 语言环境

-   `UTF-8`

### [Java gateway](https://www.zabbix.com/documentation/4.0/manual/concepts/java)

#### 概述

-   为了在特定主机上找到 JMX 计数器的值，Zabbix server 向 Zabbix Java gateway 发送请求，后者使用 JMX 管理 API 来远程查询相关的应用。该应用不需要安装额外的软件。只需要在启动时，命令行添加 `-Dcom.sun.management.jmxremote` 选项即可。

-   Java gateway 接受来自 Zabbix server 或 Zabbix proxy 的传入连接，并且只能用作“被动 proxy”。与 Zabbix proxy 相反，它也可以从 Zabbix proxy （Zabbix proxy 不能被链接）调用。在 Zabbix server 或 Zabbix proxy 配置文件中，可以直接配置每个 Java gateway 的访问，因此每个 Zabbix server 或 Zabbix proxy 只能配置**一个** Java gateway。如果主机将有 JMX agent 或其他类型的监控项，则只将 JMX agent 监控项传递给 Java gateway 进行检索。

-   当必须通过 Java gateway 更新监控项时，Zabbix server 或 proxy 将连接到 Java gateway 并请求该值，Java gateway 将检索该值并将其传递回 Zabbix server 或 Zabbix proxy。 因此，Java gateway **不会**缓存任何值。

-   Zabbix server 或 Zabbix proxy 具有连接到 Java gateway 的特定类型的进程，由 StartJavaPollers 选项控制。在内部，Java gateway 启动多个线程，由 START_POLLERS 选项控制。 在服务器端，如果连接超过 Timeout 选项配置的秒数，它将被终止，但 Java gateway 可能仍在忙于从 JMX 计数器检索值。 为了解决这个问题，从 Zabbix 2.0.15、Zabbix 2.2.10 和 Zabbix 2.4.5 开始，Java gateway 中有 TIMEOUT 选项，允许为 JMX 网络操作设置超时。

-   Zabbix server 或 proxy 尝试尽可能地将请求汇集到单个 JMX 目标（受监控项取值间隔影响），并在单个连接中将它们发送到 Java Gateway 以获得更好的性能。

-   此外，建议让 StartJavaPollers 选项的值小于或等于 START_POLLERS，否则可能会出现 Java gateway 中没有可用线程来为传入请求提供服务的情况。

#### Getting Java gateway

-   You can install Java gateway either from the sources or packages downloaded from Zabbix website.

-   Using the links below you can access information how to get and run Zabbix Java gateway, how to configure Zabbix server (or Zabbix proxy) to use Zabbix Java gateway for JMX monitoring, and how to configure Zabbix items in Zabbix frontend that correspond to particular JMX counters. 

<table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0">Installation from </th><th class="col1">Instructions </th><th class="col2">Instructions </th>
	</tr>
	</thead>
	<tbody><tr class="row1">
		<td class="col0 leftalign"><em>Sources</em>  </td><td class="col1 leftalign"><a href="/documentation/4.0/manual/installation/install#installing_java_gateway" class="wikilink1" title="manual:installation:install">Installation</a>  </td><td class="col2 leftalign"><a href="/documentation/4.0/manual/concepts/java/from_sources" class="wikilink1" title="manual:concepts:java:from_sources">Setup</a>  </td>
	</tr>
	<tr class="row2">
		<td class="col0 leftalign"><em>RHEL/CentOS packages</em>  </td><td class="col1 leftalign"><a href="/documentation/4.0/manual/installation/install_from_packages/rhel_centos#java_gateway_installation" class="wikilink1" title="manual:installation:install_from_packages:rhel_centos">Installation</a>  </td><td class="col2 leftalign"><a href="/documentation/4.0/manual/concepts/java/from_rhel_centos" class="wikilink1" title="manual:concepts:java:from_rhel_centos">Setup</a>  </td>
	</tr>
	<tr class="row3">
		<td class="col0 leftalign"><em>Debian/Ubuntu packages</em>  </td><td class="col1 leftalign"><a href="/documentation/4.0/manual/installation/install_from_packages/debian_ubuntu#java_gateway_installation" class="wikilink1" title="manual:installation:install_from_packages:debian_ubuntu">Installation</a>  </td><td class="col2 leftalign"><a href="/documentation/4.0/manual/concepts/java/from_debian_ubuntu" class="wikilink1" title="manual:concepts:java:from_debian_ubuntu">Setup</a>  </td>
	</tr>
</tbody></table>

### [Sender](https://www.zabbix.com/documentation/4.0/manual/concepts/sender)

#### 概述

-   Zabbix sender 是一个命令行应用程序，可用于将性能数据发送到 Zabbix server 进行处理。

-   该实用程序通常用于长时间运行的用户脚本，用于定期发送可用性和性能数据。

-   要将结果直接发送到 Zabbix server 或 proxy，必须配置 [trapper 监控项](https://www.zabbix.com/documentation/4.0/manual/config/items/itemtypes/trapper) 类型。

#### 运行 Zabbix sender

```sh
# example

shell> cd bin
shell> ./zabbix_sender -z zabbix -s "Linux DB3" -k db.connections -o 43
```

-   z - Zabbix server 主机（也可以使用 IP 地址）
-   s - 被监控主机的名称（在前端注册）
-   k - 监控项键值
-   o - 要发送的值

-   Zabbix sender 接受 UTF-8 编码的字符串（对于类 UNIX 系统和 Windows ），且在文件中没有字节顺序标记（BOM）。

> BOM（Byte Order Mark），字节顺序标记，出现在文本文件头部，Unicode编码标准中用于标识文件是采用哪种格式的编码。

-  Zabbix sender 同样可以在 Windows 上运行：

`zabbix_sender.exe [options]`

-   从 Zabbix 1.8.4 开始，zabbix_sender 实时发送方案已得到改进，可以连续接收多个传递给它的值，并通过单个连接将它们发送到服务器。 两个不超过0.2秒的值可以放在同一堆栈中，但最大 pooling 时间仍然是1秒。

⚠️ Zabbix sender 如果指定的配置文件中存在无效（不遵循 parameter=value 注释）的参数条目，则 Zabbix sender 将终止。

### [Get](https://www.zabbix.com/documentation/4.0/manual/concepts/get)

#### 概述

-   Zabbix get 是一个命令行应用，它可以用于与 Zabbix agent 进行通信，并从 Zabbix agent 那里获取所需的信息。(通常被用于 Zabbix agent **故障排错**。)

#### 运行 Zabbix get

[`Zabbix get 手册`](https://www.zabbix.com/documentation/4.0/manpages/zabbix_get)

一个在 UNIX 下运行 Zabbix get 以从 Zabbix agent 获取 processor load 的值的例子。

```sh
shell> cd bin
shell> ./zabbix_get -s 127.0.0.1 -p 10050 -k system.cpu.load[all,avg1]
```

> 命令行参数：

-   -s --host <host name or IP>      指定目标主机名或IP地址
-   -p --port <port number>          指定主机上运行 Zabbix agent 的端口号。默认端口10050
-   -I --source-address <IP address> 指定源 IP 地址
-   -k --key <item key>              指定要从监控项键值检索的值
-   -h --help                        获得帮助
-   -V --version                     显示版本号

> Zabbix get 同样可以在 Windows 上运行：

`zabbix_get.exe [options]`

## [Installation](https://www.zabbix.com/documentation/4.0/manual/installation)

### [获取 Zabbix](https://www.zabbix.com/documentation/4.0/manual/installation/getting_zabbix)

### [安装要求](https://www.zabbix.com/documentation/4.0/manual/installation/requirements)

#### Zabbix 系统所需磁盘空间

<table class="inline">
	<thead>
	<tr class="row0">
		<th class="col0">参数</th><th class="col1">所需磁盘空间的计算公式 （单位：字节）</th>
	</tr>
	</thead>
	<tbody><tr class="row1">
		<td class="col0 leftalign"><em>Zabbix 配置文件</em>  </td><td class="col1">固定大小。通常为 10MB 或更少。</td>
	</tr>
	<tr class="row2">
		<td class="col0 leftalign"><em>History</em>  </td><td class="col1">days*(items/refresh rate)*24*3600*bytes<br>
items：监控项数量。<br>
days：保留历史数据的天数。<br>
refresh rate：监控项的更新间隔。<br>
bytes：保留单个值所需要占用的字节数，依赖于数据库引擎，通常为 ~90 字节。 </td>
	</tr>
	<tr class="row3">
		<td class="col0 leftalign"><em>Trends</em>  </td><td class="col1 leftalign">days*(items/3600)*24*3600*bytes<br>
items：监控项数量。<br>
days：保留历史数据的天数。<br>
bytes：保留单个趋势数据所需要占用的字节数，依赖于数据库引擎，通常为 ~90 字节。  </td>
	</tr>
	<tr class="row4">
		<td class="col0 leftalign"><em>Events</em>  </td><td class="col1">days*events*24*3600*bytes<br>
events：每秒产生的事件数量。假设最糟糕的情况下，每秒产生 1 个事件。<br>
days：保留历史数据的天数。<br>
bytes：保留单个趋势数据所需的字节数，取决于数据库引擎，通常为 ~170 字节。</td>
	</tr>
</tbody></table>

### [安全设置 Zabbix 的最佳实践](https://www.zabbix.com/documentation/4.0/manual/installation/requirements/best_practices)

#### 概述

-   Zabbix 的功能不依赖于此处的实践。但建议使用它们以提高系统的安全性。

#### Zabbix agent 的安全用户

-   在默认的配置中，Zabbix server 和 Zabbix agent 进程共享一个“zabbix”用户。 如果您希望确保 Zabbix agent 无法访问 Zabbix server 配置中的敏感详细信息（例如，数据库登录信息），则应以不同的用户身份运行 Zabbix agent：

    -   创建一个安全用户；
    
    -   在 Zabbix agent 的 [配置文件](https://www.zabbix.com/documentation/4.0/manual/appendix/config/zabbix_agentd) 中指定此用户（修改 'User' parameter）；
    
    -   以拥有管理员权限的用户重启 Zabbix agent。之后，此权限将赋予给先前指定的用户。

-   UTF-8 encoding

    UTF-8 is the only encoding supported by 
    Zabbix. 

-   Setting up SSL for Zabbix frontend

    On RHEL/Centos, install mod_ssl package:

    `yum install mod_ssl`

    Create directory for SSL keys:

    ```sh
    mkdir -p /etc/httpd/ssl/private
    chmod 700 /etc/httpd/ssl/private
    Create SSL certificate:
    ```

    `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/httpd/ssl/private/apache-selfsigned.key -out /etc/httpd/ssl/apache-selfsigned.crt`

    下面提示内容适当填写。 最重要的一行是请求 Common Name 的行。 您需要输入要与服务器关联的域名。 如果您没有域名，则可以输入公共IP地址。 下面将使用 example.com。

    ```
    Country Name (两个字母) [XX]:
    State or Province Name (全名) []:
    Locality Name (eg, city) [默认的城市]:
    Organization Name (eg, company) [默认的公司名]:
    Organizational Unit Name (eg, section) []:
    Common Name (eg, your name or your server's hostname) []:example.com
    Email Address []:
    ```

    `/etc/httpd/conf.d/ssl.conf`

    ```sh
    DocumentRoot "/usr/share/zabbix"
    ServerName example.com:443
    SSLCertificateFile /etc/httpd/ssl/apache-selfsigned.crt
    SSLCertificateKeyFile /etc/httpd/ssl/private/apache-selfsigned.key
    ```

    Restart the Apache service to apply the changes:

    `systemctl restart httpd.service`

-   在 URL 的根目录上启用 Zabbix

    将虚拟主机添加到 Apache 配置，并将文档根目录的永久重定向设置为 Zabbix SSL URL。 不要忘记将 example.com 替换为服务器的实际名称。

    `/etc/httpd/conf/httpd.conf`

    ```sh
    #Add lines

    <VirtualHost *:*>
        ServerName example.com
        Redirect permanent / http://example.com
    </VirtualHost>
    ```

    重启 Apache 服务使以上修改的配置生效：

    `systemctl restart httpd.service`

-   Enabling HTTP Strict Transport Security (HSTS) on web server

    HSTS（HTTP Strict Transport Security）的作用是强制客户端（如浏览器）使用HTTPS与服务器创建连接。

    For example, to enable HSTS policy for your Zabbix frontend in Apache configuration:

    `/etc/httpd/conf/httpd.conf`
    
    add the following directive to your virtual host's configuration:

    ```sh
    <VirtualHost *:443>
    Header set Strict-Transport-Security "max-age=31536000"
    </VirtualHost>
    ```

    Restart the Apache service to apply the changes:

    `systemctl restart httpd.service`

-   禁用曝光的 Web 服务器信息

    可以通过向 Apache（用作示例）配置文件添加两行来禁用签名：

    ```    
    ServerSignature Off
    ServerTokens Prod
    ```

    可以通过更改 php.ini 配置文件来禁用 PHP 签名（X-Powered-By HTTP header）（默认情况下禁用签名）：

    `expose_php = Off`

### [从容器中安装](https://www.zabbix.com/documentation/4.0/manual/installation/containers)

#### Docker

[Github 仓库地址](https://github.com/zabbix/zabbix-docker)

### [升级](https://www.zabbix.com/documentation/4.0/manual/installation/upgrade)

## [快速入门](https://www.zabbix.com/documentation/4.0/manual/quickstart)

### [登陆和配置用户](https://www.zabbix.com/documentation/4.0/manual/quickstart/login)

### [添加主机](https://www.zabbix.com/documentation/4.0/manual/quickstart/host)

-   Zabbix中的主机（Host）是一个你想要监控的网络实体（物理的，或者虚拟的）。Zabbix中，对于主机的定义非常灵活。它可以是一台物理服务器，一个网络交换机，一个虚拟机或者一些应用。

-   可以通过配置（Configuration） → 主机（Hosts）菜单，查看已配置的主机信息。

-   从右边的选择框中，选择一个或者多个组。所有访问权限都分配到主机组，而不是单独的主机。这也是主机需要属于至少一个组的原因。

### [新建监控项](https://www.zabbix.com/documentation/4.0/manual/quickstart/item)

-   监控项是Zabbix中获得数据的基础。没有监控项，就没有数据。

### [新建触发器](https://www.zabbix.com/documentation/4.0/manual/quickstart/trigger)

-   监控项只是用于收集数据。如果需要自动评估收到的数据，我们则需要定义触发器。触发器包含了一个表达式，这个表达式定义了数据的可接受的阈值级别。

### [获取问题通知](https://www.zabbix.com/documentation/4.0/manual/quickstart/notification)

-   前往管理（Administration） → 媒体类型（Media types），点击预定义媒体类型列表中的Email，以配置E-mail。

-   新建动作以便通知

### [新建模版](https://www.zabbix.com/documentation/4.0/manual/quickstart/template)

-   模版（templates）功能可以实现这一点。模版允许对有用的监控项、触发器和其他对象进行分组，只需要一步就可以对监控主机应用模版，以达到反复重用的目的。

## [Zabbix appliance](https://www.zabbix.com/documentation/4.0/manual/appliance)

### 简介

-   除了手动安装或者重新使用现有的服务器来运行Zabbix外，用户可通过[download](https://www.zabbix.com/download_appliance) 下载Zabbix应用或者包含Zabbix应用的光盘镜像。Zabbix server (MySQL), Zabbix server (PostgreSQL), Zabbix proxy (MySQL) 以及Zabbix proxy (SQLite 3) 可使用Zabbix应用光盘，进行即时部署。

-   仓库

    在/etc/apt/sources.list中添加了官方Zabbix 仓库 :

    ```sh
    ## Zabbix repository
    deb http://repo.zabbix.com/zabbix/3.4/ubuntu trusty main
    deb-src http://repo.zabbix.com/zabbix/3.4/ubuntu trusty main
    ```

-   防火墙

    此应用使用了预定义规则的iptables防火墙:

    -   打开SSH端口(22 TCP);
    -   打开Zabbix agent (10050 TCP) 和 Zabbix trapper (10051 TCP) 端口;
    -   打开HTTP (80 TCP) 和 HTTPS (443 TCP) 端口;
    -   打开SNMP trap 端口 (162 UDP);
    -   打开NTP端口（123 UDP）的出向（outgoing）连接;
    -   ICMP pakets限制为每秒5个数据包;
    -   丢弃所有其他入向（incoming）连接。

## [Configuration](https://www.zabbix.com/documentation/4.0/manual/config)

### Hosts and host groups

-   Typical Zabbix hosts are the devices you wish to monitor (servers, workstations, switches, etc).

#### [Configuring a host](https://www.zabbix.com/documentation/4.0/manual/config/hosts/host)

-   IPMI是智能型平台管理接口（Intelligent Platform Management Interface）的缩写，是管理基于 Intel结构的企业系统中所使用的外围设备采用的一种工业标准，该标准由英特尔、惠普、NEC、美国戴尔电脑和SuperMicro等公司制定。用户可以利用IPMI监视服务器的物理健康特征，如温度、电压、风扇工作状态、电源状态等。而且更为重要的是IPMI是一个开放的免费标准，用户无需为使用该标准而支付额外的费用。

-   嵌套主机组的权限

    -   当将子主机组创建到现有的父主机组时，该子主机组用户组 的权限将从父组级继承, (例如,如果Riga 已经存在，创建 Riga/Zabbix servers)

    -   将父主机组创建到现有的子主机组时，不会设置父级的权限 (例如, 如果Riga/Zabbix servers已经存在，创建Riga)


#### [Inventory](https://www.zabbix.com/documentation/4.0/manual/config/hosts/inventory)

##### 概述

-   Zabbix管理页面有一个特殊的Inventory 菜单。 但你一开始不会看到任何数据，这里你也不能输入任何资产相关的信息。资产信息是在配置主机时人工录入建立的资产数据，或者通过使用某些自动填充选项完成的录入。

##### 构建资产库

-   Manual mode

-   Automatic mode

#### [Mass update](https://www.zabbix.com/documentation/4.0/manual/config/hosts/hostupdate)

