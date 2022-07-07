
---
title: 'Apache Dubbo 2.7.16 发布，分布式 RPC 服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2719'
author: 开源中国
comments: false
date: Thu, 07 Jul 2022 07:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2719'
---

<div>   
<div class="content">
                                                                                            <p>Apache Dubbo 2.7.16 已发布，这是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用、智能容错和负载均衡，以及服务自动注册和发现。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Feature</strong></p> 
<ul> 
 <li>Feat：consumer 支持指定序列化类型 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9550" target="_blank">#9550</a></li> 
 <li>Feat：telnet 调用命令的上下文参数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9974" target="_blank">#9974</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Bugfix</strong></p> 
<ul> 
 <li>修复回调超时问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9463" target="_blank">#9463</a></li> 
 <li>修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F9086" target="_blank">#9086</a> 以解决 race condition issue <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9588" target="_blank">#9588</a></li> 
 <li>修复使用 static tags 时 tag routing 不起作用的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9512" target="_blank">#9512</a></li> 
 <li>修复 failback 模式下重试次数错误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9525" target="_blank">#9525</a></li> 
 <li>修复 @DubboReference 参数未能正确放入 methodParameters 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9599" target="_blank">#9599</a></li> 
 <li>修复 getAttchments 返回 copy map 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9571" target="_blank">#9571</a></li> 
 <li>修复 ExtensionLoader 无法正确按类型注入的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9187" target="_blank">#9187</a></li> 
 <li>修复 lazy client share_executor 为空的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9701" target="_blank">#9701</a></li> 
 <li>修复声明的 url 的并发修改异常 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9779" target="_blank">#9779</a></li> 
 <li>将 registry id 设置为自动生成的 metada <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9782" target="_blank">#9782</a></li> 
 <li>修复 forking npe <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9613" target="_blank">#9613</a></li> 
 <li>修复 2.7 多注册表 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9787" target="_blank">#9787</a></li> 
 <li>修复 stubevent 不起作用的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9825" target="_blank">#9825</a></li> 
 <li>修复 #9847 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9848" target="_blank">#9848</a></li> 
 <li>修复问题 #9953 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9978" target="_blank">#9978</a></li> 
 <li>修复问题 #9922，合并提供方参数排除标记 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9933" target="_blank">#9933</a></li> 
 <li>修复 ZookeeperDynamicConfiguration 删除缓存监听器的错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10106" target="_blank">#10106</a></li> 
 <li>修复 metadata-report 支持单独的配置用户名和密码 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9921" target="_blank">#9921</a></li> 
 <li>修复使用 Nacos 时无法通过用户名和密码进行身份验证的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9941" target="_blank">#9941</a></li> 
 <li>修复服务长时间离线未重新注册的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10182" target="_blank">#10182</a></li> 
 <li>调整了代码，使其更加简洁 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10208" target="_blank">#10208</a></li> 
 <li>修复 LFUCache 内存泄漏问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10086" target="_blank">#10086</a></li> 
 <li>修复内存泄漏 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10231" target="_blank">#10231</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Dependency Upgrade</strong></p> 
<ul> 
 <li>升级 log4j2 版本：2.17.0 -> 2.17.2 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9791" target="_blank">#9791</a></li> 
 <li>升级 log4j 版本：1.2.16 -> 1.2.17 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9791" target="_blank">#9791</a></li> 
 <li>升级 logback 版本：1.2.2 -> 1.2.11 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9791" target="_blank">#9791</a></li> 
 <li>升级 fastjson 版本：1.2.70 -> 1.2.83 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10189" target="_blank">#10189</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Freleases%2Ftag%2Fdubbo-2.7.16" target="_blank">https://github.com/apache/dubbo/releases/tag/dubbo-2.7.16</a></p>
                                        </div>
                                      
</div>
            