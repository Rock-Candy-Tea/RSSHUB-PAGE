
---
title: 'Zabbix监控简单安装'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/16547068-f7d60536aed4bcc6.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/16547068-f7d60536aed4bcc6.png'
---

<div>   
<h3>监控系统</h3>
<p>在运维领域，监控系统即用于监控生产环境所使用的硬件、软件或者是业务的运行情况的报警系统。其能够对生产环境所产生的异常作出报警，使得管理员能够及时获知报警信息，保证业务的正常运行。<br>
监控系统功能可以分为以下几个模块：</p>
<ul>
<li>
<strong>采样</strong>：即周期性地获取某个关注指标相关的数据，一个监控系统通常支持多种采样手段，常见的手段有：ssh/telnet、agent、IPMI、SNMP、JMX等等。</li>
<li>
<strong>存储</strong>：即用于存储采样所收集到的数据，以便于管理员进行回溯查看。其存储的数据可分为历史数据和趋势数据，其中历史数据即每次采样所收集到的数据结果，通常保存周期为三个月到半年；而另一个趋势数据即为一段时间内的所采样的数据的最大值、最小值、平均值等数据，因数据量较小，通常保存较长的时间。监控系统常用的存储系统有Mysql、mariadb、Oracle、rrd等等。</li>
<li>
<strong>报警</strong>：即当监控的对象发生异常时，系统用于通常管理员或其他相关人员的报警媒介。常用的报警媒介有：邮件、短信、微信、脚本等等。</li>
<li>
<strong>展示</strong>：监控系统通过采样收集得到的数据，那么肯定得通过展示才能让管理人员更加方便的知道当前的监控项的运行情况。展示就是监控系统把数据从数据库中读取出来，然后通过统一的整理归类为标准的图形化进行输出展示，常见的展示接口有：webGUI、GUI、APP等等。</li>
</ul>
<blockquote>
<p>监控系统端称为NMS，被监控端称为agent；可分为无agent和有agent；<br>
无agent方式包括：ssh，snmp，telnet；基于web监控可使用curl命令；<br>
agent一般都是专业开发的；</p>
</blockquote>
<p>监控通道：ssh，snmp（简单网络管理协议simple network management protocol），telnet，agent，IPMI接口，...</p>
<h4>SNMP</h4>
<p>SNMP即Simple Network Management Protocol，简单网络管理协议，是用于在网络实体或节点之间交换管理或监控信息的协议，最通用的监控系统；只要配置了snmp的监控端，就能监控所有设备；</p>
<blockquote>
<p>v1 老版本，没有认证功能，通信过程没有加密；很多网络设备仅支持v1版本；<br>
v2c 社区版本，有身份识别机制，基于预密钥系统，加密方式不成熟；<br>
v3 包括了安全认证，通信过程加密；</p>
</blockquote>
<h5>SNMP优点：</h5>
<ul>
<li>标准化协议：SNMP协议属于TCP/IP协议中的标准网络管理协议，因此其兼容大多数的网络设备。</li>
<li>认可度高/流行度高：几乎所有主流的厂商都支持SNMP，所有使用SNMP管理的设备都使用相同的管理接口以支持通用的管理消息集合。</li>
<li>可移植性高：SNMP独立于操作系统和编程语言，SNMP的功能设计是可移植的，它定义了一套核心操作集，所有支持SNMP的设备都需要支持这套操作。</li>
<li>轻量级：SNMP协议的工作不会对设备的操作或性能产生冲击，网络设备只需以极小的资源消耗和负载即可增加对SNMP的管理支持。</li>
<li>扩展性高：因为所有的SNMP管理的设备上都会支持相同的一套核心操作集，而且SNMP也支持计算机网络设备中各种类型的设备的信息交互，因此添加设备变得很简单</li>
</ul>
<p><strong>SNMP的监控端就是一个命令行，安装一个程序包即可；</strong></p>
<blockquote>
<p>目前比较流行的开源监控系统由：zabbix、cacti、nagios、ganglia等等。<br>
snmp没有周期性特性，早期只能创建一个周期性任务计划周期性执行；</p>
</blockquote>
<h5>cacti</h5>
<p>提供简单web监控配置接口；利用snmp协议，用snmpget自动定义cron任务，到被监控主机上采样数据，cacti存储在自己的rrd（轮询）数据库中，但没有报警功能；</p>
<p>rrd数据库类似于一个环，一共能存储356天的数据，也就是在这个环上有365或366个固定的位置来存储每天的数据；存满之后，会覆盖最老的数据；每天的平均数据，是趋势数据；从创建的那一刻起，空间就固定了；好处是自动能清除数据；每一个数据指标就需要一个rrd；</p>
<p>cacti利用snmp客户端的工具像snmpget或snmpgetnext命令工具，到被监控端的agent上获取数据，然后存储咋rrd当中，周期性获取的，想查看某一天数据时，cacti提供了网页是通过php程序开发的，只要部署好了httpd、php，让php能够从rrd数据库当中加载数据，并且能即时把数据绘图，动态成图，例如每隔5秒钟或5分钟自动到rrd中加载数据，把新的数据再重新绘图；因此，这图的动态的，不断的再绘制的；但告警能力很有限；</p>
<p>所以，较早前cacti通常与另一个程序nagios一同实现；nagios系统能够实现对所关注的业务，能够制定合理区间，如果不在合理区间要做从软状态到硬状态变换；例如发现80端口不提供服务，采样一次为web服务down状态，连续采样3次都是down状态时，才认为从OK到problem状态发生改变；但是nagios不记录采样的数据，只记录几个窗口中的数据；例如，只记录过去到现在的8次数据；保存在内存中，一旦发现状态变化，就能实现告警操作，而nagios的告警功能非常强大；<br>
但把cacti和nagios结合起来使用，有些不方便；</p>
<p><strong>zabbix出现，就实现了上述的功能；既能实现采样、存储、告警、展示等功能；</strong></p>
<blockquote>
<p>nagios报警功能强大，但不能存储数据；<br>
zabbix：实现采样、存储、告警、展示；<br>
ganglia：较早的工具，但现在强大的数据聚合功能；</p>
</blockquote>
<h2>zabbix：</h2>
<p>LTS：长期支持维护版本：3.0，4.0</p>
<p><strong>zabbix多种监控功能：</strong></p>
<ul>
<li>支持Zabbix Agent</li>
<li>SNMP Agent</li>
<li>IPMI Agent</li>
<li>无代理监控</li>
<li>web服务监控</li>
<li>数据库监控</li>
<li>zabbix内部监控</li>
<li>计算以后进行监控展示</li>
<li>客户自定义命令监控</li>
</ul>
<h3>zabbix特性</h3>
<blockquote>
<p>数据采样：支持snmp，ssh，telnet，agent，ipmi，jmx；<br>
支持自定义检测机制：通过UserParameter实现；<br>
支持自定义指定时间间隔；历史数据保存多久，趋势数据保存多久；</p>
</blockquote>
<blockquote>
<p>支持实时绘图：展示，通过内置绘图模板，读取数据库数据完成绘图；<br>
graph 绘图；<br>
map 绘制网络拓扑图；<br>
screen 定义一个屏幕展示各种图；<br>
slide show 支持使用幻灯片机制显示；</p>
</blockquote>
<blockquote>
<p>告警：<br>
支持告警升级；<br>
定义脚本script<br>
notification发通知，发邮件通知</p>
</blockquote>
<blockquote>
<p>数据存储：<br>
数据库：自动超期数据清理<br>
mysql，pgsql</p>
</blockquote>
<blockquote>
<p>支持使用模板：完成快速监控和配置；</p>
</blockquote>
<blockquote>
<p>网络自动发现：zabbix可自动扫描网段，发现即可添加被监控主机；</p>
</blockquote>
<blockquote>
<p>分布式监控：<br>
server <--> proxy代理 <--> agent/ssh/ipmi<br>
所有配置都在server端进行，自动推送；</p>
</blockquote>
<blockquote>
<p>API接口：支持研发扩展；</p>
</blockquote>
<h3>zabbix的程序架构</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="666" data-height="444"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-f7d60536aed4bcc6.png" data-original-width="666" data-original-height="444" data-original-format="image/png" data-original-filesize="230791" src="https://upload-images.jianshu.io/upload_images/16547068-f7d60536aed4bcc6.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<blockquote>
<p>zabbix database负责专用于存储所有配置信息以及由Zabbix收集的数据；<br>
zabbix server负责接收agnet发送的报告信息的核心组件，所有配置、统计数据及操作数据均由其组织进行；</p>
</blockquote>
<blockquote>
<p>zabbix server在zabbix服务器端运行一个进程就叫zabbix server；这个进程有n种子进程，对于每一种不同的监控接口，都有专用的子进程完成此类监控收集数据的实现；例如web页面监控，通过ICMP/IPMI/SNMP等协议监控设备，通过agent监控操作系统及对JMX（j2ee）监控；因此，每一类监控，都应该启动一个或几个子进程进行监控，启动多少个子进程，取决于监控指标的个数；<br>
zabbix server就是靠这些协议不断收集数据，并存储在zabbix database数据库中；<br>
如果想查看，就通过zabbix web GUI查看，zabbix web GUI使用php语言研发，所有的配置也在GUI接口上完成，通常与Zabbix server运行在同一台主机上；</p>
</blockquote>
<blockquote>
<p>proxy的可选组件，常用于分布监控环境中，代理server收集部分被监控端的监控数据并统一发往server端；<br>
agent是部署在被监控主机上，负责收集本地数据并发往server端或proxy端；<br>
zabbix支持分布式监控：所有数据存储在数据库中，例如zabbix server只监控5万个指标，另外2万个指标交给代理服务器进行监控，代理监控服务器先把收集的数据放在本地数据库，每隔一段时间，连接zabbix server后，把数据统计汇总后一次性发出；这样减轻了连接的压力；</p>
</blockquote>
<blockquote>
<p>在大规模监控中，Zabbix server、Zabbix database、Zabbix web GUI有可能是分别的主机提供，彼此间通过socket进行通信；</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="911" data-height="518"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-4b68833046bbd364.png" data-original-width="911" data-original-height="518" data-original-format="image/png" data-original-filesize="131945" src="https://upload-images.jianshu.io/upload_images/16547068-4b68833046bbd364.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<blockquote>
<p>server1运行Zabbix sever，server2运行Zabbix web gui和apache、php（mysql或pgsql），server3运行mysql或pgsql数据库；<br>
通过server2的web页面进行配置和展示，Zabbix server把采集的数据存储在数据库中；<br>
Zabbix server所有运行通过Zabbix_server.conf配置文件加载，运行中的所有日志信息，记录在Zabbix_server.log文件中；<br>
Zabbix agent每个agent端运行一个zabbix_agentd守护进程，zabbix_agentd通过负责在本地监控各种应用，例如数据库、硬件设备、应用程序等等，把收集的数据通过zabbix协议发送给zabbix server，然后进行存储；<br>
对于agent通过zabbix_agentd.conf配置文件加载自己的配置，每个zabbix agent产生的日志信息记录在zabbix_agentd.log文件中；<br>
zabbix proxy也需要配置文件zabbix_proxy.conf，日志文件zabbix_proxy.log；<br>
配置好zabbix_agentd，在zabbix server端通过使用zabbix_get命令手动获取zabbix agent端数据测试，被动监控；zabbix agent端通过使用zabbix_sender命令，手动向zabbix server发送数据测试，主动监控；</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="910" data-height="462"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-a787692a34a406aa.png" data-original-width="910" data-original-height="462" data-original-format="image/png" data-original-filesize="194835" src="https://upload-images.jianshu.io/upload_images/16547068-a787692a34a406aa.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p><strong>zabbix监控java应用时，通过java gateway组件与java应用程序通信</strong></p>
<table>
<thead>
<tr>
<th style="text-align:center">zabbix程序的构成</th>
<th style="text-align:center"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">zabbix_server</td>
<td style="text-align:center">服务端守护进程</td>
</tr>
<tr>
<td style="text-align:center">zabbix_agentd</td>
<td style="text-align:center">agent端守护进程</td>
</tr>
<tr>
<td style="text-align:center">zabbix_proxy</td>
<td style="text-align:center">代理服务器，可选组件</td>
</tr>
<tr>
<td style="text-align:center">zabbix_get</td>
<td style="text-align:center">命令行工具，通常用于手动向agent发起数据采集请求；（测试数据采集）</td>
</tr>
<tr>
<td style="text-align:center">zabbix_sender</td>
<td style="text-align:center">命令行工具，通常运行与agent端，手动向server端发送数据</td>
</tr>
<tr>
<td style="text-align:center">zabbix_java_gateway</td>
<td style="text-align:center">JMX接口用到的组件，zabbix2.0引入，java网关类似于zabbix_agentd，但只用于监控java或JVM虚拟机相关程序；只能是单单向，由zabbix server从JMX来取数据</td>
</tr>
</tbody>
</table>
<h4>zabbix常用术语</h4>
<table>
<thead>
<tr>
<th style="text-align:center">zabbix常用术语</th>
<th style="text-align:center">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">主机（host）</td>
<td style="text-align:center">要监控的网络设备；可有ip后dns名称指定</td>
</tr>
<tr>
<td style="text-align:center">主机组（host group）</td>
<td style="text-align:center">主机的逻辑容器；可以包含主机和模板，但同一组内的主机模板不能互相连接，主机组通常给用户或用户组指派权限时使用</td>
</tr>
<tr>
<td style="text-align:center">监控项（item）</td>
<td style="text-align:center">监控的数据指标，zabbix每一个item用一个key标识，可有用于标明的监控项，一个监控项就是一个采集指标，所以定义监控项就是定义一个key；key指明了用什么命令采集数据；这个key就是定义的采集指标或指标采集时所用到的命令的简写标识</td>
</tr>
<tr>
<td style="text-align:center">触发器（trigger）</td>
<td style="text-align:center">一个表达式，用于评估某监控对象的某特定item内所接收到的数据是否在合理范围内，即阈值；接收到的数据量大于阈值时，触发器状态将从OK转变为Problem，当数据量再次回归到合理范围内时，其状态将从Problem转换回Ok</td>
</tr>
<tr>
<td style="text-align:center">事件（event）</td>
<td style="text-align:center">即发生的一个值得关注的事情，例如触发器的状态转变，新的agent或重新上线的agnet的自动注册等</td>
</tr>
<tr>
<td style="text-align:center">动作（action）</td>
<td style="text-align:center">指对于特定事件事先定义的处理方法，通过包含操作（如发通知）和条件（何时执行操作）</td>
</tr>
<tr>
<td style="text-align:center">报警升级（escalation）</td>
<td style="text-align:center">发生报警或执行远程命令的自定义方案，如每隔5分钟发生一次警报，共发送5次等</td>
</tr>
<tr>
<td style="text-align:center">媒介（media）</td>
<td style="text-align:center">发送通知的手动或通道，如email，Jabber或SMS等</td>
</tr>
<tr>
<td style="text-align:center">通知（notification）</td>
<td style="text-align:center">通过选定的媒介向用户发送的有关某事件的信息</td>
</tr>
<tr>
<td style="text-align:center">远程命令（remote command）</td>
<td style="text-align:center">预定义的命令，可在被监控主机处于某特定条件下自动执行</td>
</tr>
<tr>
<td style="text-align:center">模板（template）</td>
<td style="text-align:center">用于快速定义被监控主机的预设条目集合，通常包含了item、trigger、graph、screen、application以及low-level discovery rule；模板可以直接链接至单个主机</td>
</tr>
<tr>
<td style="text-align:center">应用（application）</td>
<td style="text-align:center">一组item相关联的集合</td>
</tr>
<tr>
<td style="text-align:center">web场景（web scennario）</td>
<td style="text-align:center">用于检测web站点可用性的一个或多个HTTP请求</td>
</tr>
<tr>
<td style="text-align:center">前端（frontend）</td>
<td style="text-align:center">zabbix的web接口</td>
</tr>
</tbody>
</table>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="813" data-height="562"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-3bd1cb6527a94600.png" data-original-width="813" data-original-height="562" data-original-format="image/png" data-original-filesize="49799" src="https://upload-images.jianshu.io/upload_images/16547068-3bd1cb6527a94600.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<blockquote>
<p>zabbix server端由zabbix poller进程从各被监控端拉取数据，例如每5分钟poller进程向zabbix agent端、snmp端或基于internal机制，向被监控项发起数据采集请求；任何poller的执行都基于items监控项进行的；定义了监控项就意味着基于某个命令来完成数据采集；<br>
item会采集出时间序列数据，对每个数据判断是否在有效区间内，大多数item都需要定义触发器trigger，超过阈值进行触发一个报警事件；<br>
触发器一旦触发一个事件，action能订阅事件，来触发某一动作；所以在trigger之上，还要定义触发事件执行的动作以便完成报警通知或执行远程脚本；<br>
某一个监控项都是被监控主机上的某一指标；<br>
可把主机定义一个组，在套用模板时方便批量监控部署操作；<br>
maintenance是维护模式，不让触发器报警；</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="818" data-height="515"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-45e47ce51674dd97.png" data-original-width="818" data-original-height="515" data-original-format="image/png" data-original-filesize="82669" src="https://upload-images.jianshu.io/upload_images/16547068-45e47ce51674dd97.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<table>
<thead>
<tr>
<th style="text-align:center">zabbix server端的子进程</th>
<th style="text-align:center"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">poller</td>
<td style="text-align:center">通用的，基于agent实现采集</td>
</tr>
<tr>
<td style="text-align:center">httppoller</td>
<td style="text-align:center">执行基于http协议监控数据采集</td>
</tr>
<tr>
<td style="text-align:center">housekeeper进程</td>
<td style="text-align:center">负责清理过期数据；例如每5分钟检查一次是否有过期数据</td>
</tr>
<tr>
<td style="text-align:center">pinger进程</td>
<td style="text-align:center">探测主机是否在线</td>
</tr>
<tr>
<td style="text-align:center">nodewatcher进程</td>
<td style="text-align:center">监控节点是否在线</td>
</tr>
<tr>
<td style="text-align:center">alerter</td>
<td style="text-align:center">报警器，执行报警时可分级escalator</td>
</tr>
<tr>
<td style="text-align:center">discoverer</td>
<td style="text-align:center">可实现自动发现</td>
</tr>
<tr>
<td style="text-align:center">db_config_syncer</td>
<td style="text-align:center">与代理通信时发送数据配置同步</td>
</tr>
<tr>
<td style="text-align:center">db_data_syncer</td>
<td style="text-align:center">与代理通信时发送数据同步</td>
</tr>
<tr>
<td style="text-align:center">watchdog进程</td>
<td style="text-align:center">用来监控每个子进程是否OK</td>
</tr>
</tbody>
</table>
<h3>安装zabbix</h3>
<h4>配置服务端</h4>
<p>192.168.0.103</p>
<p><strong>配置MySQL</strong></p>
<pre><code>[root@zabbix ~]# yum install mariadb-server -y
[root@zabbix ~]# vim /etc/my.cnf
#添加如下两行
skip_name_resolve = ON #禁止数据库反解主机名
innodb_file_per_table = ON #开启独立表空间
[root@zabbix ~]# systemctl start mariadb.service
[root@zabbix ~]# ss -tnl
State       Recv-Q Send-Q     Local Address:Port                    Peer Address:Port              
LISTEN      0      50                     *:3306                               *:*   
[root@zabbix ~]# systemctl enable mariadb.service #设置开机自启
[root@zabbix ~]# mysql
MariaDB [(none)]>CREATE DATABASE zabbix CHARSET 'utf8';
MariaDB [(none)]> GRANT ALL ON zabbix.* TO zbxuser@'127.0.0.1' IDENTIFIED BY 'zbxpass';
MariaDB [(none)]> GRANT ALL ON zabbix.* TO zbxuser@'192.%.%.%' IDENTIFIED BY 'zbxpass';
MariaDB [(none)]> FLUSH PRIVILEGES;
</code></pre>
<p><strong>安装zabbix官方仓库</strong></p>
<pre><code>[root@zabbix ~]# yum -y install http://repo.zabbix.com/zabbix/3.0/rhel/7/x86_64/zabbix-release-3.0-1.el7.noarch.rpm
[root@zabbix ~]# cat /etc/yum.repos.d/zabbix.repo
[zabbix]
name=Zabbix Official Repository - $basearch
baseurl=http://repo.zabbix.com/zabbix/3.0/rhel/7/$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-ZABBIX

[zabbix-non-supported]
name=Zabbix Official Repository non-supported - $basearch 
baseurl=http://repo.zabbix.com/non-supported/rhel/7/$basearch/
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-ZABBIX
gpgcheck=1
</code></pre>
<p><strong>安装epel源，若无wget命令，手动安装<code>yum -y install wget</code></strong></p>
<pre><code>[root@zabbix ~]# wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
...
</code></pre>
<p><strong>安装zabbix-server-mysql，zabbix-get</strong><br>
安装过程中，可能由于读条慢导致安装报错，重复执行安装命令之道进度条达100%即可</p>
<pre><code>[root@zabbix ~]# yum install zabbix-server-mysql zabbix-get -y
...complete!
</code></pre>
<p><strong>初始化zabbix的数据库，有专用的zabbix脚本实现</strong><br>
zabbix的2.0与3.0不一样，2.0有三个sql脚本而且要安装特定的固定顺序依次执行；<br>
3.0只有一个sql脚本create.sql，需要把脚本导入到mysql数据库中；</p>
<pre><code>[root@zabbix ~]# rpm -ql zabbix-server-mysql
/etc/logrotate.d/zabbix-server
/etc/zabbix/zabbix_server.conf
/usr/lib/systemd/system/zabbix-server.service
/usr/lib/tmpfiles.d/zabbix-server.conf
/usr/lib/zabbix/alertscripts
/usr/lib/zabbix/externalscripts
/usr/sbin/zabbix_server_mysql
/usr/share/doc/zabbix-server-mysql-3.0.28
/usr/share/doc/zabbix-server-mysql-3.0.28/AUTHORS
/usr/share/doc/zabbix-server-mysql-3.0.28/COPYING
/usr/share/doc/zabbix-server-mysql-3.0.28/ChangeLog
/usr/share/doc/zabbix-server-mysql-3.0.28/NEWS
/usr/share/doc/zabbix-server-mysql-3.0.28/README
/usr/share/doc/zabbix-server-mysql-3.0.28/create.sql.gz
/usr/share/man/man8/zabbix_server.8.gz
/var/log/zabbix
/var/run/zabbix
[root@zabbix ~]# cd /usr/share/doc/zabbix-server-mysql-3.0.28/
[root@zabbix ~]# gzip -d create.sql.gz
[root@zabbix ~]# mysql -uzbxuser -h127.0.0.1 -pzbxpass zabbix < /usr/share/doc/zabbix-server-mysql-3.0.28/create.sql
[root@zabbix ~]# mysql -uzbxuser -h127.0.0.1 -pzbxpass
MariaDB [(none)]> use zabbix;
Database changed
MariaDB [zabbix]> show tables;
+----------------------------+
| Tables_in_zabbix           |
+----------------------------+
| acknowledges               |
| actions                    |
| alerts                     |
| application_discovery      |
| application_prototype      |
| application_template       |
......
</code></pre>
<p><strong>修改zabbix配置文件</strong></p>
<pre><code>[root@zabbix ~]# cp /etc/zabbix/zabbix_server.conf zabbix_server.conf_20191013 #备份配置文件
[root@zabbix ~]# vim /etc/zabbix/zabbix_server.conf
其中：
在GENERAL PARAMETERS段：

ListenPort=10051

SourceIP= 执行监控操作时，zabbix server有多个ip时，指定使用的IP，因为客户端在执行监控时要验证服务端ip的，基于ip授权；

日志设置
日志类型有三种方式：
system  - syslog 写入系统日志；
file    - file specified with LogFile parameter 自定义单独使用日志文件；
console - standard output 日志发往控制台，调试才使用；
LogType=file 日志类型
LogFile=/var/log/zabbix/zabbix_server.log
LogFileSize=0 设置日志文件大小，超过后自动滚动；0表示不滚动；
PidFile=/var/run/zabbix/zabbix_server.pid 服务端pid文件的路径；

DBHost=127.0.0.1 数据库服务器地址；如果不在当前主机此项是必须改的；
DBName=zabbix 数据库名
DBUser=zbxuser 数据库登录用户
DBPassword=zbxpass 数据库登录密码
DBSocket=/var/lib/mysql/mysql.sock 因为mysql数据库在本地，所以，此项为本土通信使用；
</code></pre>
<p><strong>启动zabbix</strong></p>
<pre><code>[root@zabbix ~]# vim /etc/sysconfig/selinux  #修改为disabled
SELINUX=disabled
[root@zabbix ~]# reboot
[root@zabbix ~]# systemctl stop firewalld.service
[root@zabbix ~]# systemctl disable firewalld.service
[root@zabbix ~]# systemctl start zabbix-server.service 
[root@zabbix ~]# ss -tnl #10051端口开启
LISTEN      0      128                    *:10051                              *:*                  
LISTEN      0      128                   :::22                                :::*                  
LISTEN      0      100                  ::1:25                                :::*                  
LISTEN      0      128                   :::10051                             :::*      
</code></pre>
<p>注意：centos7.1中trousers程序包版本不支持zabbix，所以只有centos7.2以上版本才支持，因此，需升级trousers版本到trousers-0.3.13-1.el7.x86_64.rpm，如果未安装trousers，直接yum安装</p>
<h4>配置web端</h4>
<p><strong>开启node1：192.168.0.104，部署web界面</strong><br>
安装zabbix仓库步骤省略</p>
<pre><code>[root@node1 ~]# yum install httpd php-mysql php-mbstring php-gd php-bcmath php-ldap php-xml -y
[root@node1 ~]# yum install zabbix-web zabbix-web-mysql -y
</code></pre>
<p>指明zabbix的时区，即配置php的时区指定；两种方式修改php时区，一个是全局php.ini，一个是zabbix在php中自己的配置文件/etc/httpd/conf.d/zabbix.conf；</p>
<pre><code>[root@node1 ~]# vim /etc/httpd/conf.d/zabbix.conf
其中：
Alias /zabbix /usr/share/zabbix 路径别名，所有的zabbix页面文件是在/usr/share/zabbix文件中；
仅修改：
php_value date.timezone Asia/Shanghai
其它都是定义授权项的无需修改；
[root@node1 ~]# systemctl start httpd.service
[root@node1 ~]# ss -tnl
State       Recv-Q Send-Q       Local Address:Port                      Peer Address:Port              
LISTEN      0      128                      *:22                                   *:*                  
LISTEN      0      100              127.0.0.1:25                                   *:*                  
LISTEN      0      128                     :::80                                  :::* 
</code></pre>
<p>访问web界面，浏览器输入：<a href="https://links.jianshu.com/go?to=http%3A%2F%2F192.168.0.104%2Fzabbix" target="_blank">http://192.168.0.104/zabbix</a></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1286" data-height="705"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-d4466c7ccbf3f695.png" data-original-width="1286" data-original-height="705" data-original-format="image/png" data-original-filesize="63397" src="https://upload-images.jianshu.io/upload_images/16547068-d4466c7ccbf3f695.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">zabbix欢迎界面</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="876" data-height="523"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-19ed4f33ffdc4ec0.png" data-original-width="876" data-original-height="523" data-original-format="image/png" data-original-filesize="48506" src="https://upload-images.jianshu.io/upload_images/16547068-19ed4f33ffdc4ec0.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">相关组件检查</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="861" data-height="535"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-15dd7c4dc6212ddf.png" data-original-width="861" data-original-height="535" data-original-format="image/png" data-original-filesize="41171" src="https://upload-images.jianshu.io/upload_images/16547068-15dd7c4dc6212ddf.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">MySQL连接</div>
</div>
<p>zabbix server需要改成服务端IP，图中localhost有误</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="867" data-height="533"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-09b60fa45aeea9fd.png" data-original-width="867" data-original-height="533" data-original-format="image/png" data-original-filesize="46303" src="https://upload-images.jianshu.io/upload_images/16547068-09b60fa45aeea9fd.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="862" data-height="536"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-e2cf1feace24a50a.png" data-original-width="862" data-original-height="536" data-original-format="image/png" data-original-filesize="36591" src="https://upload-images.jianshu.io/upload_images/16547068-e2cf1feace24a50a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>安装后配置文件：<code>/etc/zabbix/web/zabbix.conf.php</code>，若之前填写出现错误，可以修改</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="389" data-height="462"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-9099e4ba7dd63cf8.png" data-original-width="389" data-original-height="462" data-original-format="image/png" data-original-filesize="15334" src="https://upload-images.jianshu.io/upload_images/16547068-9099e4ba7dd63cf8.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">登录界面</div>
</div>
<p><strong>默认管理员账户/密码：admin/zabbix</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1017" data-height="940"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-8eef12f35c54bddb.png" data-original-width="1017" data-original-height="940" data-original-format="image/png" data-original-filesize="89371" src="https://upload-images.jianshu.io/upload_images/16547068-8eef12f35c54bddb.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">zabbix控制面板</div>
</div>
<h4>配置agent</h4>
<p>192.168.0.105</p>
<p><strong>安装agent</strong></p>
<pre><code>[root@agent ~]# yum install zabbix-agent zabbix-sender -y
...
complete!
[root@agent ~]# rpm -ql zabbix-agent
/etc/logrotate.d/zabbix-agent
/etc/zabbix/zabbix_agentd.conf
/etc/zabbix/zabbix_agentd.d
/etc/zabbix/zabbix_agentd.d/userparameter_mysql.conf
/usr/lib/systemd/system/zabbix-agent.service
/usr/lib/tmpfiles.d/zabbix-agent.conf
/usr/sbin/zabbix_agentd
/usr/share/doc/zabbix-agent-3.0.28
/usr/share/doc/zabbix-agent-3.0.28/AUTHORS
/usr/share/doc/zabbix-agent-3.0.28/COPYING
/usr/share/doc/zabbix-agent-3.0.28/ChangeLog
/usr/share/doc/zabbix-agent-3.0.28/NEWS
/usr/share/doc/zabbix-agent-3.0.28/README
/usr/share/doc/zabbix-agent-3.0.28/userparameter_examples.conf
/usr/share/man/man8/zabbix_agentd.8.gz
/var/log/zabbix
/var/run/zabbix
</code></pre>
<blockquote>
<p>配置文件：/etc/zabbix/zabbix_agentd.conf<br>
Unitd File：zabbix-agent.service</p>
</blockquote>
<p><strong>编辑配置文件</strong></p>
<pre><code>[root@agent ~]# vim /etc/zabbix/zabbix_agentd.conf
##### Passive checks related（被动检测相关的配置：agent等待server过来请求数据）
Server=192.168.0.103
可使用逗号分隔授权给哪些zabbix-server或zabbix-proxy过来采集数据的服务器地址列表；
ListenPort=10050 本机的监听端口
ListenIP=0.0.0.0 监听主机，表示本机所有地址；
StartAgents=3 启动agent进程数；

##### Active checks related（主动检测相关的配置：agent主动向server发送监控数据）
ServerActive=192.168.0.103 
以逗号分隔的，当前agent主动发送监控数据过去的server端；
Hostname=node2 在zabbix主机上的主机名；
</code></pre>
<p><strong>启动zabbix-agent</strong></p>
<pre><code>[root@agent ~]# systemctl start zabbix-agent.service      
[root@agent ~]# ss -tnl
State       Recv-Q Send-Q     Local Address:Port                    Peer Address:Port              
LISTEN      0      128                    *:22                                 *:*                  
LISTEN      0      100            127.0.0.1:25                                 *:*                  
LISTEN      0      128                    *:10050                              *:*                  
LISTEN      0      128                   :::22                                :::*                  
LISTEN      0      100                  ::1:25                                :::*                  
LISTEN      0      128                   :::10050                             :::*                     
</code></pre>
<h3>配置监控</h3>
<p>一次完整的简单监控配置：<br>
host group --> host --> [application] --> item --> trigger (Events) --> (Media Type,User Group,User) --> action(conditions,operations(send message,remote script))</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1043" data-height="937"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-ce3e560fa54530ff.png" data-original-width="1043" data-original-height="937" data-original-format="image/png" data-original-filesize="67072" src="https://upload-images.jianshu.io/upload_images/16547068-ce3e560fa54530ff.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">快速配置</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="941" data-height="726"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-cb6651b4ba96949f.png" data-original-width="941" data-original-height="726" data-original-format="image/png" data-original-filesize="65895" src="https://upload-images.jianshu.io/upload_images/16547068-cb6651b4ba96949f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="936" data-height="101"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-c2c25209171c9a15.png" data-original-width="936" data-original-height="101" data-original-format="image/png" data-original-filesize="15388" src="https://upload-images.jianshu.io/upload_images/16547068-c2c25209171c9a15.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="938" data-height="459"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-1a8376e53f0d1625.png" data-original-width="938" data-original-height="459" data-original-format="image/png" data-original-filesize="41158" src="https://upload-images.jianshu.io/upload_images/16547068-1a8376e53f0d1625.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="853" data-height="821"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-2238174e1d7a2e32.png" data-original-width="853" data-original-height="821" data-original-format="image/png" data-original-filesize="56898" src="https://upload-images.jianshu.io/upload_images/16547068-2238174e1d7a2e32.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">配置item</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="939" data-height="449"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-edffb70333b38047.png" data-original-width="939" data-original-height="449" data-original-format="image/png" data-original-filesize="45246" src="https://upload-images.jianshu.io/upload_images/16547068-edffb70333b38047.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1102" data-height="481"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-e28d818ecc4831b9.png" data-original-width="1102" data-original-height="481" data-original-format="image/png" data-original-filesize="47471" src="https://upload-images.jianshu.io/upload_images/16547068-e28d818ecc4831b9.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h4>参数简述</h4>
<p><strong>主机配置：</strong><br>
监控主机的接口：4种</p>
<ul>
<li>Agent interfaces</li>
<li>SNMP interfaces</li>
<li>JMX interfaces</li>
<li>IPMI interfaces</li>
</ul>
<h5>定义item：key+parameters</h5>
<p>key：2种</p>
<ul>
<li>zabbix内建：预定义；内建key有n种分类；<br>
type：agent（被动），agent（主动），snmp v1，...</li>
<li>用户自定义：在客户端进行定义，在服务端进行添加；</li>
</ul>
<table>
<thead>
<tr>
<th style="text-align:center">采集到的信息的种类</th>
<th style="text-align:center"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">numeric</td>
<td style="text-align:center">数值，无符号，浮点数</td>
</tr>
<tr>
<td style="text-align:center">charactor</td>
<td style="text-align:center">字符串数据</td>
</tr>
<tr>
<td style="text-align:center">log</td>
<td style="text-align:center">日志数据</td>
</tr>
<tr>
<td style="text-align:center">text</td>
<td style="text-align:center">文本数据</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th style="text-align:center">数据的类型</th>
<th style="text-align:center"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">boolean</td>
<td style="text-align:center">布尔型</td>
</tr>
<tr>
<td style="text-align:center">octal</td>
<td style="text-align:center">八进制数据</td>
</tr>
<tr>
<td style="text-align:center">decimal</td>
<td style="text-align:center">十进制数据</td>
</tr>
<tr>
<td style="text-align:center">hexadecimal</td>
<td style="text-align:center">十六进制数据</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th style="text-align:center">store value</th>
<th style="text-align:center"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">AS is</td>
<td style="text-align:center">数据不做任何处理；采样的是什么就记录什么</td>
</tr>
<tr>
<td style="text-align:center">Delta（Simple change）</td>
<td style="text-align:center">本次采样数据减去前一次采样数据</td>
</tr>
<tr>
<td style="text-align:center">Delta（speed per second）</td>
<td style="text-align:center">本次采样数据减去前一次采样数据，而后除以采样间隔时长</td>
</tr>
</tbody>
</table>
<h5>trigger：触发器</h5>
<p>逻辑表达式：<code>&#123;<server>:<item>.<function>(<parameters<)&#125;<operator><constant></code></p>
<table>
<thead>
<tr>
<th style="text-align:center">参数</th>
<th style="text-align:center">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">server</td>
<td style="text-align:center">主机名称</td>
</tr>
<tr>
<td style="text-align:center">key</td>
<td style="text-align:center">主机上关系的相应监控项的key</td>
</tr>
<tr>
<td style="text-align:center">function</td>
<td style="text-align:center">评估采集到的数据是否在合理范围内所使用的函数</td>
</tr>
<tr>
<td style="text-align:center">parameter</td>
<td style="text-align:center">函数参数</td>
</tr>
</tbody>
</table>
<p>触发器所支持的函数有avg、count、change、date、dayofweek、delta、diff、iregexp、last、sum、now等</p>
<blockquote>
<p>大多数数值函数可以接受秒数为其参数，而如果在数值参数之前使用“#”作为前缀，则表示为最近几次的取值，如sum(300)表示300秒内所有取值之和，而sum(#10)则表示最近10此取值之和<br>
此外，avg、count、last、min和max还支持使用第二个参数，用于完成时间限定；<br>
例如，max(1h,7d)将返回一周之前的最大值</p>
</blockquote>
<blockquote>
<p>示例：&#123;<a href="https://links.jianshu.com/go?to=www.magedu.com%3Asystem.cpu.load%255Ball%2Cavg1%255D.last%280%29" target="_blank">www.magedu.com:system.cpu.load[all,avg1].last(0)</a>&#125;>3<br>
表示主机<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fwww.magedu.com" target="_blank">www.magedu.com</a>上所有CPU的过去1分钟内的平均负载的最后一次取值大于3时触发状态变换<br>
对于last函数来说，last(0)相当于last(#1)</p>
</blockquote>
<p>触发器定义了数据指标的阈值；通常<strong>定义不合理区间</strong>；</p>
<ul>
<li>OK:正常状态 --> 老版本为false;</li>
<li>PROBLEM：非正常状态 --> 老版本为true;</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="936" data-height="436"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-bcdeed816494870c.png" data-original-width="936" data-original-height="436" data-original-format="image/png" data-original-filesize="46389" src="https://upload-images.jianshu.io/upload_images/16547068-bcdeed816494870c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">定义触发器</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="898" data-height="603"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-c76245f79b351855.png" data-original-width="898" data-original-height="603" data-original-format="image/png" data-original-filesize="40849" src="https://upload-images.jianshu.io/upload_images/16547068-c76245f79b351855.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">创建触发器</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="940" data-height="420"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-3cfcd66e7e1ada2e.png" data-original-width="940" data-original-height="420" data-original-format="image/png" data-original-filesize="43269" src="https://upload-images.jianshu.io/upload_images/16547068-3cfcd66e7e1ada2e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">触发器设置完成</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="938" data-height="543"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-9ab6baf45bf456a3.png" data-original-width="938" data-original-height="543" data-original-format="image/png" data-original-filesize="59365" src="https://upload-images.jianshu.io/upload_images/16547068-9ab6baf45bf456a3.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">查看监控信息</div>
</div>
<p><strong>安全连接：发邮件时是否使用安全的连接</strong></p>
<table>
<thead>
<tr>
<th style="text-align:center">类型</th>
<th style="text-align:center"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">starttls</td>
<td style="text-align:center">使用smtp协议时，自动触发ssl</td>
</tr>
<tr>
<td style="text-align:center">ssl/tls</td>
<td style="text-align:center">需要额外配置ssl，明确指明使用smtp协议时才会调用ssl</td>
</tr>
</tbody>
</table>
<p>如果使用的是互联网上的邮件服务器，基于认证的方式，填入注册的邮箱、密码即可；</p>
<h5>Action：动作</h5>
<ul>
<li>conditions：触发此动作的条件，一般通过“事件”触发</li>
<li>operations：触发条件满足时采取的动作</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="946" data-height="221"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-73df71ac992c2629.png" data-original-width="946" data-original-height="221" data-original-format="image/png" data-original-filesize="28186" src="https://upload-images.jianshu.io/upload_images/16547068-73df71ac992c2629.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">create action</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="813" data-height="394"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-44e069ffc184bbb5.png" data-original-width="813" data-original-height="394" data-original-format="image/png" data-original-filesize="29737" src="https://upload-images.jianshu.io/upload_images/16547068-44e069ffc184bbb5.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p><strong>①send message</strong></p>
<ul>
<li>Meida Type：传递消息的通道；</li>
<li>script：用来定义信息通道，完成信息传递的脚本；<br>
（1）脚本放置路径：在服务器端/etc/zabbix/zabbix_server.conf<br>
AlertScriptsPath=/usr/lib/zabbix/alerscripts<br>
（2）zabbix会向脚本传递三个参数：<br>
$1：经由此信道发送的信息的接收目标；可以是邮箱地址，电话号码；<br>
$2：信息的主题，subject；<br>
$3：传递信息的内容；</li>
</ul>
<p>3.x版本之后三个参数默认不再传递，需要自行定义；可以使用宏来模拟此前的行为</p>
<p>&#123;ALTET.SENDTO&#125;<br>
&#123;ALERT.SUBJECT&#125;<br>
&#123;ALERT.MESSAGE&#125;</p>
<p>注意：每个信息接收人相对于此媒介来说，得配置相应的接收地址</p>
<p><strong>媒介：定义告警方式的传输信息的通道</strong></p>
<table>
<thead>
<tr>
<th style="text-align:center">Meida Type类型</th>
<th style="text-align:center"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">Email</td>
<td style="text-align:center">邮件，需要定义发件人邮箱地址和SMTP服务器</td>
</tr>
<tr>
<td style="text-align:center">script</td>
<td style="text-align:center">自定义脚本；必须放置在指定路径下，可调用短信网关、微信网关</td>
</tr>
<tr>
<td style="text-align:center">jabber</td>
<td style="text-align:center">即时通信通用框架；基于msn、sq、Yahoo Messenger、google的GTalk的等通信软件</td>
</tr>
<tr>
<td style="text-align:center">SMS</td>
<td style="text-align:center">短信（北美使用）</td>
</tr>
<tr>
<td style="text-align:center">Ez Texting（USA，Canada）</td>
<td style="text-align:center">商业</td>
</tr>
</tbody>
</table>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="943" data-height="314"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-1ec8a5bbbb3f5cba.png" data-original-width="943" data-original-height="314" data-original-format="image/png" data-original-filesize="42232" src="https://upload-images.jianshu.io/upload_images/16547068-1ec8a5bbbb3f5cba.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">创建media type</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="714" data-height="431"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-c48d6b0ca4571546.png" data-original-width="714" data-original-height="431" data-original-format="image/png" data-original-filesize="26935" src="https://upload-images.jianshu.io/upload_images/16547068-c48d6b0ca4571546.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">设置media type</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="819" data-height="716"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-2661608a92ece9b8.png" data-original-width="819" data-original-height="716" data-original-format="image/png" data-original-filesize="64403" src="https://upload-images.jianshu.io/upload_images/16547068-2661608a92ece9b8.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">用户定义midia type</div>
</div>
<p>User：主要定义利用指定信道接收消息；<br>
User Groups：用户的逻辑容器；</p>
<p><strong>②remote command</strong><br>
功能：在agent所在的主机上运行用户指定的命令或脚本来尝试着恢复故障<br>
-重启服务<br>
使用IPMI接口重启服务器；</p>
<ul>
<li>任何自定义脚本可完成的功能<br>
custom script（常用）<br>
ssh<br>
telnet<br>
global script</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="899" data-height="750"><img data-original-src="//upload-images.jianshu.io/upload_images/16547068-849a62d14b65cf97.png" data-original-width="899" data-original-height="750" data-original-format="image/png" data-original-filesize="49640" src="https://upload-images.jianshu.io/upload_images/16547068-849a62d14b65cf97.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">Create action</div>
</div>
<p>remote command中的脚本是远程执行的脚本，而sent message中media type里的脚本是用来发信息的脚本；</p>
<p>在被管理主机上zabbix_agentd进程是以zabbix用户身份运行的，所以要执行远程命令时，会用到管理权限，所以zabbix基于sudo的方式执行命令；</p>
<p><strong>在192.168.0.105被管理终端上：</strong><br>
第一步：开启zabbix用户的sudo管理权限：</p>
<pre><code>[root@agent ~]# visudo
## Allows people in group wheel to run all commands
%wheel  ALL=(ALL)       ALL
zabbix  ALL=(ALL)       NOPASSWD: ALL

#Defaults requiretty #把此项注释掉，否则远程执行命令失败，表示不需要控制终端
</code></pre>
<p>第二步：开启zabbix server执行远程命令</p>
<pre><code>[root@agent ~]# vim /etc/zabbix/zabbix_agentd.conf
EnableRemoteCommands=1 允许远程命令在本机执行
LogRemoteCommands=1 启用远程命名执行的记录日志
[root@agent ~]# systemctl restart zabbix-agent.service
[root@agent ~]# usermod -s /bin/bash zabbix
</code></pre>
<blockquote>
<p>Customed Script前提：<br>
在agent端需要完成的配置：<br>
（1）zabbix用户有所需的管理权限（基于sudo授权实现）；</p>
<ol>
<li>Defaults requiretty，修改为 # Defaults requiretty，表示不需要控制终端；</li>
<li>Defaults requiretty，修改为 Defaults:nobody !requitretty，表示用户不需要控制终端；</li>
</ol>
<p>（2）agent进程要允许执行远程命令；/etc/zabbix/zabbix_agentd.conf<br>
EnableRemoteCommands=1</p>
</blockquote>
<p><strong>可执行的命令类型：5种方式</strong></p>
<ul>
<li>IPMI</li>
<li>ssh：需要提供账号、密码，一般不使用；</li>
<li>telnet</li>
<li>Customed Script：自定义脚本<br>
sudo /usr/bin/systemctl restart httpd.service</li>
<li>Global Script</li>
</ul>
<p>告警升级：<br>
（1）remote command<br>
（2）send message</p>
<p>在zabbix server端编辑发送邮件的脚本：<br>
例如：</p>
<pre><code>[root@agent ~]# vim /usr/lib/zabbix/alertscripts/sendmail.sh
#!/bin/bash
# 
contact=$1
subject=$2
body=$3

echo "$body" | mail -s "$subject" "$contact"

[root@agent ~]# chmod +x /usr/lib/zabbix/alertscripts/sendmail.sh 
[root@agent lib]# /usr/lib/zabbix/alertscripts/sendmail.sh root@localhost "test" "test body"
[root@agent lib]# mail
Heirloom Mail version 12.5 7/5/10.  Type ? for help.
"/var/spool/mail/root": 1 message 1 new
>N  1 root                  Fri Nov 15 19:57  18/598   "test"
& 
</code></pre>
<p>在web页面设置：</p>
<pre><code>[root@agent ~]# vim /etc/zabbix/zabbix_server.conf
DebugLevel=5 开启调试级别
</code></pre>
  
</div>
            