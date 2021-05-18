
---
title: '分布式RPC服务调用框架选型：使用Dubbo实现分布式服务调用'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=5365'
author: 掘金
comments: false
date: Mon, 17 May 2021 20:15:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=5365'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Dubbo概念</h1>
<ul>
<li>Dubbo是一个高性能,轻量级的RPC分布式服务框架</li>
<li>提供了三核心能力:
<ul>
<li><strong>面向接口的远程方法调用</strong>(@Reference)</li>
<li><strong>智能容错</strong></li>
<li><strong>负载均衡</strong></li>
</ul>
</li>
<li><strong>Dubbo特点:</strong> 按照分层的方式来架构,可以使各个层之间解耦合</li>
<li><strong>Dubbo的角色:</strong>
<ul>
<li>提供方:<strong>Provider</strong></li>
<li>消费方:<strong>Consumer</strong></li>
<li>Dubbo的提供非常简单的服务模型,要么是提供方提供服务,要么是消费方消费服务</li>
</ul>
</li>
</ul>
<h1 data-id="heading-1">Dubbo的服务治理</h1>
<ul>
<li><strong>透明远程调用:</strong> 调用远程方法就像调用本地方法一样,只需简单配置,没有任何API侵入</li>
<li><strong>负载均衡机制:</strong> Client端LB,在内网替代F5等硬件负载均衡器</li>
<li><strong>容错重试机制:</strong> 服务Mock数据,重试次数,超时机制</li>
<li><strong>自动注册发现:</strong> 注册中心基于接口名查询服务提供者的IP地址,可以添加和删除服务提供者</li>
<li><strong>性能日志监控:</strong> Monitor,统计服务的调用次数和调用时间的监控中心</li>
<li><strong>服务治理中心:</strong> 路由规则,动态配置,服务降级,访问控制,权重调整,负载均衡</li>
</ul>
<h1 data-id="heading-2">Dubbo的核心功能</h1>
<ul>
<li><strong>Remoting:</strong> 远程通讯,提供对多种NIO框架抽象封装,包括"同步转异步"和"请求-响应"模式的信息交换方式</li>
<li><strong>Cluster:</strong> 服务框架,提供基于接口方法的透明远程过程调用,包括:<strong>多协议支持,软负载均衡,容错重试,路由规则,动态配置</strong>等集群支持</li>
<li><strong>Registry:</strong> 服务注册中心,服务自动发现.基于注册中心目录服务,使服务消费方能动态地查找服务提供方,使地址透明,使服务提供方可以平滑地增加和减少机器</li>
</ul>
<pre><code class="copyable">通信模型:
BIO : 同步并阻塞
NIO : 异步并阻塞
AIO : 异步非阻塞

通信框架 : netty
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">Dubbo组件角色</h1>

































<table><thead><tr><th>组件角色</th><th>说明</th></tr></thead><tbody><tr><td>Provider</td><td>暴露服务的服务提供方</td></tr><tr><td>Consumer</td><td>调用远程服务的服务消费方</td></tr><tr><td>Registry</td><td>服务注册与发现的注册中心</td></tr><tr><td>Monitor</td><td>统计服务调用次数和调用时间的监控中心</td></tr><tr><td>Container</td><td>服务运行容器</td></tr><tr><td>### 组件调用关系说明</td><td></td></tr></tbody></table>
<ul>
<li>服务容器<strong>Container</strong>负责启动,加载,运行服务提供者</li>
<li>服务提供者<strong>Provider</strong>在启动时,向注册中心注册自己提供的服务</li>
<li>服务消费者<strong>Consumer</strong>在启动时,向注册中心订阅自己所需的服务</li>
<li>注册中心<strong>Registry</strong>返回服务提供者地址列表给消费者,如果有变更,注册中心将基于长连接推送变更数据给消费者</li>
<li>服务消费者<strong>Consumer</strong>从提供者地址列表中,基于负载均衡算法,选择一台提供者进行调用,如果调用失败,再选另一台进行调用</li>
<li>服务消费者<strong>Consumer</strong>和服务提供者<strong>Provider</strong>,在内存中累计调用次数和调用时间,定时每分钟发送一次统计数据到监控中心</li>
</ul>
<h1 data-id="heading-4">Dubbo Admin管理控制台</h1>
<ul>
<li>管理控制台的主要功能:
<ul>
<li><strong>路由规则</strong></li>
<li><strong>动态配置</strong></li>
<li><strong>服务降级</strong></li>
<li><strong>访问控制</strong></li>
<li><strong>权限调整</strong></li>
<li><strong>负载均衡</strong></li>
</ul>
</li>
</ul></div>  
</div>
            