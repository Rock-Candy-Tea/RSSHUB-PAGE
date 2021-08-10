
---
title: 'RabbitMQ 3.8.20 & 3.9.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8286'
author: 开源中国
comments: false
date: Tue, 10 Aug 2021 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8286'
---

<div>   
<div class="content">
                                                                                            <p>RabbitMQ 3.8.20 & 3.9.2 发布，上述两个版本至少需要 Erlang 23.2，并支持最新的 Erlang 24 版本。更新内容如下：</p> 
<h3>CLI 工具（3.8.20 & 3.9.2）</h3> 
<p>错误修复</p> 
<ul> 
 <li><code>rabbitmq-upgrade drain</code> 和 <code>rabbitmq-upgrade revive</code> 现在记录 <code>warning</code> 和 <code>info</code> 级别，而不是 <code>alert</code>；</li> 
</ul> 
<h3><strong>Shovel</strong> 插件（3.8.20 & 3.9.2）</h3> 
<p>错误修复</p> 
<ul> 
 <li>在某些涉及节点重启失败的情况下，可能会启动多个 Shovels；</li> 
</ul> 
<h3><strong>Federation</strong> 插件（3.8.20 & 3.9.2）</h3> 
<p>错误修复</p> 
<ul> 
 <li>在某些涉及节点重启失败的情况下，可以会启动多个 Federation 链接；</li> 
</ul> 
<h3><strong>Dependency</strong> 升级（3.9.2）</h3> 
<ul> 
 <li>Osiris 已经更新到 1.1.0 了；</li> 
</ul> 
<h3><strong>Core Server</strong>（3.8.20 ）</h3> 
<p>增强</p> 
<ul> 
 <li>当主机名包含非 ASCII 字符时，节点无法启动；</li> 
 <li>代理协议 header 中传递的 TLS 信息现在被附加到连接指标中，就像它是由一个非代理客户端提供的一样；</li> 
</ul> 
<h3>管理插件（3.8.20）</h3> 
<p>错误修复</p> 
<ul> 
 <li>HTTP API 现在将 WWW-Authenticate 标头纳入对包含无效凭证的请求的 401 响应中；</li> 
 <li>现在根据 AMQP 0-9-1 规范验证队列名称的长度。</li> 
</ul> 
<h3><strong>RabbitMQ Erlang</strong> 客户端（3.8.20）</h3> 
<p>错误修复</p> 
<ul> 
 <li>客户端的新版本再次发布到 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fhex.pm%2F" target="_blank">Hex.pm</a>；</li> 
 <li><code>connection_timeout</code> 被调整以避免出现混乱的警告；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.8.20" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.8.20</a> & <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.9.2" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.9.2</a></p>
                                        </div>
                                      
</div>
            