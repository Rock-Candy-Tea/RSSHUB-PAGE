
---
title: 'EMQX 4.x 版本更新：Kafka 与 RocketMQ 集成安全增强'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7027cf65344737a8d9db7630dd26603d4a5.png'
author: 开源中国
comments: false
date: Mon, 22 Aug 2022 06:16:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7027cf65344737a8d9db7630dd26603d4a5.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>近日，EMQX 开源版 v4.3.17、v4.3.18、v4.4.6、v4.4.7，与企业版 v4.3.12、v4.3.13、v4.4.6、v4.4.7 八个维护版本正式发布。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>此次发布包含了多个功能更新：规则引擎 RocketMQ 支持 ACL 检查、Kafka 支持 SASL/SCRAM 与 SASL/GSSAPI 认证以适配更多部署方式，提升规则引擎 TDengine 写入性能以及 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fblog%2Fintroduction-to-mqtt5-protocol-shared-subscription" target="_blank"><span>MQTT 共享订阅</span></a></span><span>性能，同时在 CLI 中提供了配置文件检查命令，方便用户修改 EMQX 配置。此外还修复了多项已知 BUG。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>欢迎下载使用：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Ftry%3Fproduct%3Denterprise" target="_blank"><span>https://www.emqx.com/zh/try</span></a></span></p> 
<h2 style="text-align:start"><span>规则引擎新功能</span></h2> 
<h3 style="text-align:start"><span>RocketMQ 支持携带用户信息实现 ACL 检查</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>包含版本 </span><span><code>企业版 v4.3.12</code></span><span> </span><span><code>企业版 v4.4.6</code></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>RocketMQ 在 4.4.0 版本开始支持 ACL，通过创建多个用户并为其赋予不同的 Topic 和消费组权限，以达到用户之间的权限隔离。开启 ACL 访问控制会导致没有配置认证信息的客户端连接中断。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>本次发布 EMQX 新增了 RocketMQ ACL 支持，在资源创建页面填入用户信息即可连接至启用 ACL 的 RocketMQ 示例，以实现更安全的数据集成。</span></p> 
<h3 style="text-align:start"><span>Kafka 支持 SASL/SCRAM 与 SASL/GSSAPI 认证</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>包含版本 </span><span><code>企业版 v4.4.6</code></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>SCRAM 是 SASL 机制家族的一种，是针对 SASL/PLAIN 方式的不足而提供的另一种认证方式。这种方式能够支持动态添加用户，同时使用 sha256 或 sha512 对密码加密，安全性相对会高一些。SASL/GSSAPI 主要是给 Kerberos 使用的。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>新增的两种认证方式让 EMQX 能够用于更多的 Kafka 环境，满足企业用户不同的安全配置需求。</span></p> 
<h3 style="text-align:start"><span>提升规则引擎中 TDengine 的写入性能</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>包含版本 </span><span><code>企业版 v4.3.12</code></span><span> </span><span><code>企业版 v4.4.6</code></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>优化底层驱动实现 TDengine 写入性能的提升，同时写入数据到 TDengine 的动作中新增 </span><span><code>db_name</code></span><span> 字段以改善对超级表的支持。</span></p> 
<h3 style="text-align:start"><span>规则引擎支持分页和搜索</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>包含版本 </span><span><code>开源版 v4.3.17</code></span><span> </span><span><code>开源版 v4.4.6</code></span><span> </span><span><code>企业版 v4.3.12</code></span><span> </span><span><code>企业版 v4.4.6</code></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>规则引擎列表查看 REST API 支持分页与模糊搜索包括规则的 SQL、Topics 列表、动作列表等。此特性旨在于让用户更方便地管理规则，尤其是规则数量较多的时候。</span></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>本次更新默认兼容旧版本 API，仅在 Query 中携带指定参数才会返回分页格式数据。</span></p> 
</blockquote> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Query 查询参数：</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="956" src="https://oscimg.oschina.net/oscnet/up-7027cf65344737a8d9db7630dd26603d4a5.png" width="2002" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start"><span>通过 CLI 检查配置是否正确</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>包含版本 </span><span><code>开源版 v4.3.17</code></span><span> </span><span><code>开源版 v4.4.6</code></span><span> </span><span><code>企业版 v4.3.12</code></span><span> </span><span><code>企业版 v4.4.6</code></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>在重启 EMQX 之前使用 CLI 命令测试当前配置是否正确，能够检测包括配置语法、配置文件格式、配置项引起的错误，避免应用配置时因为配置错误 block EMQX 启动。</span></p> 
<pre style="text-align:left"><span>./bin/emqx check_conf</span></pre> 
<h2 style="text-align:start"><span>Dashboard 支持清除历史告警</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>包含版本 </span><span><code>企业版 v4.3.12</code></span><span> </span><span><code>企业版 v4.4.6</code></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>EMQX 内置监控告警功能，支持监控 CPU 占用率、（系统/进程）内存占用率、进程数量、规则引擎资源状态、集群脑裂与愈合并进行告警。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>此前 EMQX 已经支持历史告警清除 REST API，本次发布在 Dashbaord 实现了告警清除能力。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="818" src="https://oscimg.oschina.net/oscnet/up-1e56e96f7546de4151ae78b880f58716e7a.png" width="1520" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start"><span>新增 TLS 垃圾回收配置</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>包含版本 </span><span><code>开源版 v4.3.18</code></span><span> </span><span><code>开源版 v4.4.7</code></span><span> </span><span><code>企业版 v4.3.13</code></span><span> </span><span><code>企业版 v4.4.7</code></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>允许配置连接进程在 TLS 握手完成后进行垃圾回收以减少内存占用，这可以使每个 SSL 连接减少大约 35% 的内存消耗，但相应地会增加 CPU 的消耗。</span></p> 
<h2 style="text-align:start"><span>其他重要变更</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化共享订阅性能</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>开源版 v4.3.13 升级了 OTP 版本以解决 OTP Bug 导致的随机进程失去响应的问题（出现概率较低），建议仍在使用 v4.3 的用户升级到此版本</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>允许配置 TLS 握手日志的日志等级以便查看详细的握手过程</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>从下一版本起，我们将停止对 macOS 10 的支持，转为提供 macOS 11 的安装包</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>BUG 修复</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>各版本 BUG 修复详情请查看：</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>开源版 v4.3.17： </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fchangelogs%2Fbroker%2F4.3.17" target="_blank">https://www.emqx.com/zh/changelogs/broker/4.3.17</a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>开源版 v4.3.18： </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fchangelogs%2Fbroker%2F4.3.18" target="_blank">https://www.emqx.com/zh/changelogs/broker/4.3.18</a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>开源版 v4.4.6： </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fchangelogs%2Fbroker%2F4.4.6" target="_blank">https://www.emqx.com/zh/changelogs/broker/4.4.6</a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>开源版 v4.4.7： </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fchangelogs%2Fbroker%2F4.4.7" target="_blank">https://www.emqx.com/zh/changelogs/broker/4.4.7</a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>企业版 v4.3.12：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fchangelogs%2Fenterprise%2F4.3.12" target="_blank">https://www.emqx.com/zh/changelogs/enterprise/4.3.12</a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>企业版 v4.3.13：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fchangelogs%2Fenterprise%2F4.3.13" target="_blank">https://www.emqx.com/zh/changelogs/enterprise/4.3.13</a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>企业版 v4.4.6： </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fchangelogs%2Fenterprise%2F4.4.6" target="_blank">https://www.emqx.com/zh/changelogs/enterprise/4.4.6</a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>企业版 v4.4.7： </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fchangelogs%2Fenterprise%2F4.4.7" target="_blank">https://www.emqx.com/zh/changelogs/enterprise/4.4.7</a></span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            