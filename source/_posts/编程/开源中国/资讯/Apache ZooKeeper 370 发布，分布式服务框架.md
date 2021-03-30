
---
title: 'Apache ZooKeeper 3.7.0 发布，分布式服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8358'
author: 开源中国
comments: false
date: Tue, 30 Mar 2021 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8358'
---

<div>   
<div class="content">
                                                                                            <p>Apache ZooKeeper 是 Apache 软件基金会的一个软件项目，它为大型分布式计算提供开源的分布式配置服务、同步服务和命名注册。ZooKeeper 曾经是 Hadoop 的一个子项目，但现在是一个独立的顶级项目。</p> 
<p>ZooKeeper 的架构通过冗余服务实现高可用性。因此，如果第一次无应答，客户端就可以询问另一台 ZooKeeper 主机。ZooKeeper 节点将它们的数据存储于一个分层的命名空间，非常类似于一个文件系统或一个前缀树结构。客户端可以在节点读写，从而以这种方式拥有一个共享的配置服务。</p> 
<p>Apache ZooKeeper 3.7.0 正式发布，本次部分更新内容如下：</p> 
<h3><strong>新功能</strong></h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-1112" target="_blank">ZOOKEEPER-1112</a> - 增加对 C 客户端 SASL 认证的支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3264" target="_blank">ZOOKEEPER-3264</a> - Zookeeper 的基准测试工具；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3301" target="_blank">ZOOKEEPER-3301</a> - 强制执行配额限制；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3681" target="_blank">ZOOKEEPER-3681</a> - 添加对 Travis CI 构建的 s390x 支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3714" target="_blank">ZOOKEEPER-3714</a> - 向 Perl 客户端添加（Cyrus）SASL 身份验证支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3874" target="_blank">ZOOKEEPER-3874</a> - 从 Java 启动 ZooKeeper 服务器的官方 API；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3948" target="_blank">ZOOKEEPER-3948</a> - 为 ZooKeeperServer 测试引入确定性的运行时行为注入框架；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3959" target="_blank">ZOOKEEPER-3959</a> - 允许具有 SASL 的多个超级用户；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3969" target="_blank">ZOOKEEPER-3969</a> - 添加 whoami API 和 Cli 命令；</li> 
</ul> 
<h3><strong>改进</strong></h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-1871" target="_blank">ZOOKEEPER-1871</a> - 向 zkCli 添加选项以在执行命令之前等待连接；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-2272" target="_blank">ZOOKEEPER-2272</a> - ZooKeeperServer 和 KerberosName 中的代码清理；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-2649" target="_blank">ZOOKEEPER-2649</a> - ZooKeeper 不会在客户端已通过身份验证的日志会话 ID 中写入；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-2779" target="_blank">ZOOKEEPER-2779</a> - 添加选项以不会为重新配置节点设置ACL；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3101" target="_blank">ZOOKEEPER-3101</a> - 添加注释提醒用户在向 ZOO_ERRORS 添加值时向 zerror 添加大小写；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3342" target="_blank">ZOOKEEPER-3342</a> - 使用标准字符集；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3411" target="_blank">ZOOKEEPER-3411</a> - 删除不建议使用的 CLI:ls2 和 rmr；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3427" target="_blank">ZOOKEEPER-3427</a> - 引入 SnapshotComparer，可帮助调试快照；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3482" target="_blank">ZOOKEEPER-3482</a> - 用于客户端和 Quorum 的 SSL 的 SASL（Kerberos）身份验证；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3567" target="_blank">ZOOKEEPER-3567</a> - 为 zk python 客户端添加 SSL 支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3582" target="_blank">ZOOKEEPER-3582</a> - 将异步 api 调用重构为 lambda 样式；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3638" target="_blank">ZOOKEEPER-3638</a> - 将 Jetty 更新为 9.4.24.v20191120；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3640" target="_blank">ZOOKEEPER-3640</a> - 在 cli_mt 中实现“批处理模式”；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3649" target="_blank">ZOOKEEPER-3649</a> - ls -s CLI 需要换行；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3662" target="_blank">ZOOKEEPER-3662</a> - 删除 Follower Class 中的 NPE Possibility；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3663" target="_blank">ZOOKEEPER-3663</a> - 清理 ZNodeName 类；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-4048" target="_blank">ZOOKEEPER-4048</a> - 将 Mockito 升级到 3.6.2 —— 允许在 JDK16 上构建；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-4188" target="_blank">ZOOKEEPER-4188</a> - 添加有关 whoami CLI 的文档；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-4209" target="_blank">ZOOKEEPER-4209</a> - 在 3.5 分支上，将 Netty 版本更新为 4.1.53.Final ；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-4221" target="_blank">ZOOKEEPER-4221</a> - 改善消息超出 jute.maxbufer 大小时的错误消息；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-4231" target="_blank">ZOOKEEPER-4231</a> - 为快照压缩配置添加文档；</li> 
</ul> 
<h2><strong>Bug</strong></h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-1105" target="_blank">ZOOKEEPER-1105</a> - C 客户端 zookeeper_close 不向服务器发送 CLOSE_OP 请求；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-1677" target="_blank">ZOOKEEPER-1677</a> - INET_ADDRSTRLEN 的滥用；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-1998" target="_blank">ZOOKEEPER-1998</a> - C库从 zookeeper_interest 无条件调用 getaddrinfo；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-2307" target="_blank">ZOOKEEPER-2307</a> - ZooKeeper 无法启动，因为 acceptedEpoch 小于 currentEpoch；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-2475" target="_blank">ZOOKEEPER-2475</a> - 在 Zoookeeper Javadoc 中包含 ZKClientConfig API；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-2490" target="_blank">ZOOKEEPER-2490</a> - 在 Windows 上无限连接；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3112" target="_blank">ZOOKEEPER-3112</a> - 由于连接时出现 UnresolvedAddressException 而导致 fd 泄漏；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3613" target="_blank">ZOOKEEPER-3613</a> - 用户意外在值的末尾包含空格时，ZKConfig无法在getBoolean() 上返回正确的值；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3651" target="_blank">ZOOKEEPER-3651</a> - NettyServerCnxnFactoryTest 异常；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-4200" target="_blank">ZOOKEEPER-4200</a> - 修复 WatcherCleanerTest 在 macOS Catalina 上失败的问题；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-4201" target="_blank">ZOOKEEPER-4201</a> - C 客户端：macOS Catalina 上与 SASL 相关的编译问题；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-4205" target="_blank">ZOOKEEPER-4205</a> - 使用端口 8080 时测试失败；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-4230" target="_blank">ZOOKEEPER-4230</a> - 在 RestMain 中使用动态临时文件夹而不是静态临时文件夹；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-4232" target="_blank">ZOOKEEPER-4232</a> - InvalidSnapshotTest 破坏了其自己的测试数据；</li> 
</ul> 
<h2><strong>Wish</strong></h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3415" target="_blank">ZOOKEEPER-3415</a> - 转换内部逻辑以使用 Java 8 流；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FZOOKEEPER-3763" target="_blank">ZOOKEEPER-3763</a> - 还原 ZKUtil.deleteRecursive 以帮助与 3.5 和 3.6 的应用程序兼容；</li> 
</ul> 
<p>完整详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzookeeper.apache.org%2Fdoc%2Fr3.7.0%2Freleasenotes.html" target="_blank">https://zookeeper.apache.org/doc/r3.7.0/releasenotes.html</a></p>
                                        </div>
                                      
</div>
            