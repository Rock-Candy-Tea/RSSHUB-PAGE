
---
title: 'Redis 7.0正式发布，对子系统进行了多项改进'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=7260'
author: Dockone
comments: false
date: 2022-05-27 02:58:33
thumbnail: 'https://picsum.photos/400/300?random=7260'
---

<div>   
<br>新版DBMS Redis 7.0现已火热发布。除了键/值数据存储功能之外，Redis还支持列表、哈希和集合等结构化数据格式，同时提供在服务器端运行Lua脚本驱动程序的功能。<br>
<br>与Memcached等内存内存储系统不同，Redis依靠磁盘实现持久存储，并可在异常关闭时保障数据库安全。Redis项目的源代码遵循BSD许可。<br>
<br>客户端库则支持各类最流行的编程语言，包括Perl、Python、PHP、Java、Ruby以及Tcl。Redis中的事务机制允许大家在单一步骤中执行一组命令，确保此命令组在执行时的连贯性与一致性（不会被来自其他请求的命令所阻塞），而且能够在发生问题时执行变更回滚。全部数据都被完全缓存在RAM当中。<br>
<h3>Redis 7.0新特性一览</h3>简而言之，此次Redis 7.0几乎囊括对各个方面的增量式改进。其中最值得注意的当数Redis Functions、ACLv2、命令自查及Sharded Pub/Sub。这些都是根据用户反馈和生产经验，对现有功能做出的重大改进性成果。<br>
<br>在此次公布的新版本中，Redis新增对服务器端函数的支持。而且与以往支持的服务器端Lua脚本不同，最新支持的函数不再特定于应用程序，而属于能够实现服务器功能扩展的附加逻辑。<br>
<br>换言之，这些函数与数据及数据库本身（而非应用程序）高度相关，可实现复制、持久存储等具体功能。<br>
<br>7.0版本还增加了近50个新的命令与选项，负责支持并扩展Redis的现有功能。例如，位图、列表、集合、排序集合和流数据等类型都迎来了新的数据管理功能。此外，缓存语义也得到扩展，已经能够支持存在与比较修饰符。<br>
<br>Redis 7.0版本的另一大亮点则是ACLv2的引入。它允许用户以键为基础控制数据访问，并为命令定义不同的访问规则集，同时将多个选择器（权限集）绑定给每个用户。如此一来，每个密钥都可被标记为特定权限，例如为密钥中的特定子集设定只读或写入权限。<br>
<br>同样值得关注的是，Redis 7.0还提供发布-订阅消息传递范式的碎片化实现——也就是在集群上将消息发送至通道所链接的特定节点，再进一步将消息重新定向至其余节点。如此一来，无论是接入主节点还是各辅节点，客户端都可以通过订阅通道接收到消息内容。<br>
<br>此外，新版本还支持在单次CONFIG SET/GET调用中一次处理多个配置，同时为redis-cli工具添加了“-json”、“-2”、“-scan”、“-functions-rdb”等选项。<br>
<br>除了面向用户的功能之外，新版本中还出现了众多“无名英雄”的身影——也就是那些努力让Redis更高效、更稳定、更精简的特性。开发团队将大部分精力都投入到了提升资源效率、优化操作性能的工作当中。Redis 7.0所管理的几乎每个子系统都迎来了多项改进，包括内存、计算、网络和存储。部分优化已经默认启用，也有一部分需要手动开启。关于更多细节信息，请参阅<a href="https://github.com/redis/redis/blob/7.0/redis.conf">redis.conf文件</a>中的内联文档。<br>
<br>默认情况下，客户端无法访问到可能影响安全性的设置和命令（例如禁用DEBUG和MODULE命令，禁用PROTECTED_CONFIG设置变更标记等）。Redis-cli也不再向历史文件发送包含敏感数据的命令。<br>
<br>另外，新版本还进一步增强性能、减少了内存占用量。以启用集群模式、执行写入时复制操作、使用hash和zset键等为例，这些场景下的内存占用量均已显著减少。此外，将数据刷新至磁盘的逻辑（即fsync操作）也得到了优化。<br>
<br>修复了Lua脚本执行环境中的CVE_2022-24735漏洞。此漏洞可能导致用户覆盖掉自己的Lua代码，并使其运行在其他用户的上下文（包括具有更高权限的用户）当中。<br>
<br>此外，我们也修复了用于Ubuntu和Debian的Redis软件包中的CVE-2022-0543漏洞（此问题只针对单一程序集，与Redis本身无关），其允许在远程执行任意Lua代码、并绕过沙箱隔离机制在Redis中运行脚本。<br>
<br>CVE-2022-24736也已得到解决，此漏洞可能允许redis服务器进程由于空指针取消引用而产生崩溃。攻击者往往会加载特制的Lua脚本以利用这项漏洞。<br>
<h3>写在最后</h3>Redis的版本升级一直比较简单，整个项目也一直将向下兼容作为重要的设计原则。但在升级至Redis 7.0之前，建议大家花几分钟认真阅读<a href="https://github.com/redis/redis/blob/7.0/00-RELEASENOTES">发行版说明</a>。<br>
<br>原文链接：<br>
<ul><li><a href="https://www.linuxadictos.com/redis-7-0-llega-con-mejoras-de-rendimiento-correccion-de-errores-y-mas.html">Redis 7.0 llega con mejoras de rendimiento, corrección de errores y mas</a></li><li><a href="https://redis.com/blog/redis-7-generally-available/">Redis 7.0 Is Out!</a></li></ul>
                                
                                                              
</div>
            