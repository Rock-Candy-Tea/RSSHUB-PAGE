
---
title: 'EMQ X v4.3 正式发布：性能大幅提升，更好用的多语言扩展'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.emqx.net/images/d6670380723eb008bcda0a52573712d0.png'
author: 开源中国
comments: false
date: Sat, 15 May 2021 08:07:00 GMT
thumbnail: 'https://static.emqx.net/images/d6670380723eb008bcda0a52573712d0.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.cn%2Fproducts%2Fbroker" target="_blank">连接海量物联网设备的 MQTT 消息服务器 - EMQ X</a> 是基于高并发的 Erlang/OTP 语言平台开发，支持百万级连接和分布式集群架构。EMQ X 已经在全球物联网市场广泛应用，无论是产品原型设计、物联网创业公司、还是大规模的商业部署，都支持免费使用。</p> 
<p>产品介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.cn%2Fproducts%2Fbroker" target="_blank">https://www.emqx.cn/products/broker</a></p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.cn%2Fdownloads%23broker" target="_blank">https://www.emqx.cn/downloads#broker</a></p> 
<h2>概览</h2> 
<p>EMQ X v4.3.0 版本修复了一些已知问题并新增了诸多特性，在通配符订阅性能、路由表内存占用、规则引擎性能以及大量客户端离线处理性能方面做了较大改进，同时将 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.emqx.cn%2Fbroker%2Fv4.3%2Fadvanced%2Flang-exhook.html" target="_blank">多语言</a> 扩展底层通信方式由 erlport 更换为更为灵活的 gRPC 通信。</p> 
<p>该版本是 4.x 最后一个次要版本，旨在于为用户提供一个功能丰富、性能稳定的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.cn%2Fproducts%2Fbroker" target="_blank">MQTT 服务器</a>，推荐所有 4.x 用户升级到此版本，此后 4.x 版本将进入维护状态，EMQ X Team 将进入到后续 5.0 版本开发工作中。</p> 
<p>访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femqx%2Femqx" target="_blank">EMQ X GitHub</a> 仓库，点击右上角的 <strong>Watch</strong> 即可关注 EMQ X 5.0 最新动态。</p> 
<p><img alt="性能测试图" src="https://static.emqx.net/images/d6670380723eb008bcda0a52573712d0.png" referrerpolicy="no-referrer"></p> 
<p>特性概览：observer_cli 查看 Erlang VM 运行状况</p> 
<h2>升级到 4.3 版本</h2> 
<p>查看升级指南：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.emqx.cn%2Fbroker%2Fv4.3%2Fchanges%2Fupgrade-4.3.html%23%E5%8D%87%E7%BA%A7%E5%88%B0-4-3-%E7%89%88%E6%9C%AC" target="_blank">https://docs.emqx.cn/broker/v4.3/changes/upgrade-4.3.html#升级到-4-3-版本</a></p> 
<p>详细更新日志：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.emqx.cn%2Fbroker%2Fv4.3%2Fchanges%2Fchanges-4.3.html" target="_blank">https://docs.emqx.cn/broker/v4.3/changes/changes-4.3.html</a></p> 
<h2>性能改进</h2> 
<h3>多语言扩展功能底层实现方式由 erlport 改为 gRPC</h3> 
<p>多语言扩展允许用户使用其它编程语言如 Python、 Java 等直接向 EMQ X 挂载钩子进行业务处理，接收并处理监听器字节数据报文实现自定义协议的解析。</p> 
<p>多语言扩展能以用户熟悉的编程语言处理客户端连接生命周期，快速集成到物联网应用中；接入任意的私有协议，享受由 EMQ X 带来的诸多性能和功能优势。</p> 
<p>此前 EMQ X 多语言扩展基于 erlport 进行跨语言通信，考虑到语言支持层面不广、性能水平不足且会与 EMQ X 自身功能产生资源竞争问题。在此版本中我们将底层方式更换为 gRPC，能够更好的实现跨语言和跨平台工作，提供更高的性能和清晰的管理能力，有效改善用户开发和维护难度。</p> 
<h3>提升规则引擎的性能</h3> 
<p>此前我们为规则引擎添加了所有可用的钩子，即使没有创建规则 EMQ X 触发任何事件时都会尝试去匹配规则，导致不必要的开销。</p> 
<p>此版本中我们进行了改进，仅为已创建的规则添加必要的钩子，有效降提升了规则引擎性能。</p> 
<h3>支持路由表压缩，减少内存占用</h3> 
<p>支持路由表压缩，减少内存占用并增强订阅性能，但发布性能会略受影响，因此提供了关闭选项。</p> 
<h3>优化通配符订阅性能</h3> 
<p>优化 EMQ X 集群条件下通配符订阅性能，比之前版本提升了 10 倍以上。</p> 
<h3>提升大量客户端同时离线时的处理性能</h3> 
<p>此前下线消息和新上线消息会在 Broker 进程堆积，我们修复该问题实现了性能提升。</p> 
<h2>新增特性</h2> 
<h3>规则引擎</h3> 
<ul> 
 <li>规则引擎新增更新资源逻辑，可以在不删除规则的情况下更换动作使用的资源</li> 
 <li>规则引擎 SQL 函数支持 unix 时间戳与 rfc3339 格式时间之间的转换</li> 
 <li>保持对 EMQ X Broker 启动后连接失败的资源进行重试，避免资源短暂宕机恢复之后规则无法恢复使用</li> 
</ul> 
<h3>运维管理</h3> 
<ul> 
 <li>支持 observer_cli，在 console 启动模式下输入 observer_cli:start(). 可查看 Erlang VM 实时运行详细状况</li> 
 <li>Prometheus 支持集群指标</li> 
 <li>支持单行日志输出，并支持 rfc3339 时间格式</li> 
 <li>支持 IPv6 自动探测</li> 
 <li>所有发行版都支持环境变量覆盖配置文件（以前仅适用于 Docker）</li> 
 <li>开源版支持 Dashboard 上传证书文件（以前仅适用于企业版）</li> 
</ul> 
<h3>MQTT 增强</h3> 
<ul> 
 <li>共享订阅分发策略配置为 round_robin 时随机选择起始点</li> 
 <li>共享订阅支持按源主题的 Hash 分发消息，设备与共享订阅之间可以有固定的分发通道</li> 
</ul> 
<h3>其他功能</h3> 
<ul> 
 <li>WebSocket 连接支持获取真实 IP 与 Port</li> 
 <li>Websocket 监听器支持从 subprotocols 列表中选择支持的 subprotocol</li> 
 <li>支持 MySQL 8.0 的默认认证方法 caching_sha2_password</li> 
 <li>支持 Mnesia 认证信息的导入导出</li> 
 <li>允许使用 Base64 编码的客户端证书或者客户端证书的 MD5 值作为用户名或者 Client ID</li> 
 <li>支持重启监听器，某些在监听器设置无需重启 EMQ X 即可更新</li> 
 <li>仅在正式版本中启用数据遥测功能</li> 
 <li>支持清除所有 ACL 缓存</li> 
 <li>Redis 哨兵模式支持 SSL 连接</li> 
 <li>emqx_auth_clientid 与 emqx_auth_usernmae 合并为 emqx_auth_mnesia。请参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.emqx.io%2Fen%2Fbroker%2Fv4.3%2Fadvanced%2Fdata-import-and-export.html" target="_blank">文档</a> 将数据到旧版本导出，并导入到 4.3 中</li> 
 <li>Docker 默认输出日志到控制台，设置 EMQX_LOG__TO=file 使日志输出到文件</li> 
 <li>支持输出 JSON 格式的日志，某些日志分析系统如 ELK 可以更好的进行配置使用</li> 
</ul> 
<h2>安全性提升</h2> 
<ul> 
 <li>保护 EMQ X Broker 免受跨站点 WebSocket 劫持攻击</li> 
 <li>SSL 支持 verify 与 server_name_indication 配置项</li> 
 <li>SSL 支持证书链最大长度以及私钥文件密码配置项</li> 
 <li>JWT 认证支持 JWKS</li> 
</ul> 
<h2>开发构建</h2> 
<ul> 
 <li> <p>支持 Erlang/OTP 23</p> <p>升级到 Erlang/OTP 23 版本，为提高特性更新和错误修复速度，EMQ X fork 并维护了 Erlang/OTP 项目，默认使用 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgithub.com%2Femqx%2Fotp" target="_blank">http://github.com/emqx/otp</a> 进行构建。</p> </li> 
 <li> <p>新安装包仅支持 macOS 10.14 及以上版本</p> </li> 
 <li> <p>项目调整为 umbrella 结构</p> <p>项目结构调整之后降低了依赖管理的复杂度，同依赖之间互相关联的修改原子性得到保障；同时 review 和测试复杂度降低，对社区开发者更加友好。</p> </li> 
 <li> <p>支持使用 Elixir 编译插件</p> </li> 
</ul> 
<h2>错误修复</h2> 
<h3>MQTT 协议</h3> 
<ul> 
 <li>修复 MQTT 心跳报文的处理</li> 
 <li>修复 MQTT 报文接收计数问题</li> 
 <li>限制飞行窗口的最大长度为 65535</li> 
 <li>修复 Server Keep Alive 生效情况下 Dashboard 中 Keep Alive 字段的值未同步的问题</li> 
</ul> 
<h3>网关</h3> 
<ul> 
 <li>修复 CoAP 连接中 ACL 配置不生效的问题</li> 
 <li>修复使用相同 ClientID 的 CoAP 客户端可以同时接入的问题</li> 
 <li>修复 MQTT-SN 睡眠模式不可用的问题</li> 
 <li>修复 MQTT-SN 网关在睡眠模式下会丢弃 DISCONNECT 报文的问题</li> 
 <li>修复 LwM2M 网关将数字编码、解码为无符号整型的问题</li> 
 <li>修复 Clean Session 为 false 的 MQTT-SN 连接在非正常断开时没有发布遗嘱消息的问题</li> 
</ul> 
<h3>资源</h3> 
<ul> 
 <li>修复 MySQL 认证 SSL/TLS 连接功能不可用的问题</li> 
 <li>修复 Redis 重连失败问题</li> 
</ul> 
<h3>其他修复</h3> 
<ul> 
 <li>修复 ekka_locker 在极端条件下内存可能无限增长的问题</li> 
 <li>修复 MQTT 桥接功能中 max_inflight_size 配置项不生效的问题</li> 
 <li>修复 MQTT 桥接飞行窗口的问题</li> 
 <li>修复 MQTT 桥接功能中指标统计错误和 retry_interval 字段进行了多次单位转换的问题</li> 
 <li>修复告警持续时间计算错误的问题</li> 
 <li>修复过长的 Client ID 无法追踪的问题</li> 
 <li>修复查询客户端信息可能出现崩溃的问题</li> 
 <li>修复主题重写与 ACL 在发布订阅时执行顺序不一致的问题</li> 
 <li>修复 WebSocket 连接无法使用对端证书作为用户名的问题</li> 
 <li>修复认证数据无法导入的问题</li> 
 <li>修复 Docker 中 EMQ X 可能启动失败的问题</li> 
 <li>修复 OOM 时快速杀死连接进程</li> 
</ul> 
<blockquote> 
 <p>版权声明： 本文为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.io%2Fcn%2F" target="_blank">EMQ</a> 原创，转载请注明出处。</p> 
 <p>原文链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.cn%2Fblog%2Femqx-4-3-0-release-notes" target="_blank">https://www.emqx.cn/blog/emqx-4-3-0-release-notes</a></p> 
</blockquote>
                                        </div>
                                      
</div>
            