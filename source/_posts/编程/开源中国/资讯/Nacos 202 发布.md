
---
title: 'Nacos 2.0.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://github.com/alibaba/nacos/raw/develop/doc/Nacos_Logo.png'
author: 开源中国
comments: false
date: Mon, 14 Jun 2021 08:00:00 GMT
thumbnail: 'https://github.com/alibaba/nacos/raw/develop/doc/Nacos_Logo.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>一、介绍Nacos</h2> 
<p>Nacos 致力于帮助您发现、配置和管理微服务。Nacos 提供了一组简单易用的特性集，帮助您快速实现动态服务发现、服务配置、服务元数据及流量管理。</p> 
<p>Nacos 帮助您更敏捷和容易地构建、交付和管理微服务平台。 Nacos 是构建以“服务”为中心的现代应用架构 (例如微服务范式、云原生范式) 的服务基础设施。</p> 
<p>说的直白一点，Nacos就是管理微服务应用的注册和发现功能。也就是应用注册到nacos，并通过nacos暴露给网关和负载模块。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fnacos%2Fblob%2Fdevelop%2Fdoc%2FNacos_Logo.png" target="_blank"><img height="50%" src="https://github.com/alibaba/nacos/raw/develop/doc/Nacos_Logo.png" width="50%" referrerpolicy="no-referrer"></a></p> 
<p> </p> 
<h2>二、更新内容</h2> 
<p>在这个版本中，Nacos社区针对1.X到2.0.X升级的特性做了很多优化，比如修复升级过程中可能遇到的问题，增加了一些API来查询和修复升级过程中的数据。升级。</p> 
<p>同时，Nacos社区也加强了功能，比如配置CAS发布、增加Distro同步统计、优化日志错误信息等。</p> 
<p>更重要的是，Nacos 社区做了大量的重构和单元测试。</p> 
<p>详见如下：</p> 
<h3>2.1 特征</h3> 
<ul> 
 <li>在客户端添加 CAS 发布配置。</li> 
 <li>在命名性能日志中添加发行版监视器信息。</li> 
 <li>添加一些 API 来查询和修复升级数据。</li> 
 <li>支持为 createService 指定临时值。</li> 
 <li>功能使命名 rpc 客户端知道服务器列表更改。</li> 
 <li>支持从具有命名空间的端点获取服务器列表。</li> 
</ul> 
<h3>2.2 增强</h3> 
<ul> 
 <li>支持通过 ',' 和 ';' 配置多个服务器列表。</li> 
 <li>支持指定 NAMING_CACHE_REGISTRY_DIR 属性。</li> 
 <li>保持集群升级状态。</li> 
 <li>增强控制台中的查询配置行为。</li> 
 <li>增强 gRPC 错误提示日志。</li> 
 <li>在调用服务器之前添加/删除客户端实例缓存。</li> 
</ul> 
<h3>2.3 重构</h3> 
<ul> 
 <li>常量变量的增强。</li> 
 <li>重构 nacos 示例。</li> 
 <li>增强代码质量。</li> 
 <li>重构 resourceParser groupName 更改拼接方法。</li> 
</ul> 
<h3>2.4 错误修正</h3> 
<ul> 
 <li>删除降级的成员版本信息。</li> 
 <li>当我将源代码分支切换到 2.0.0 时，修复无法解析符号“istio”。</li> 
 <li>修复升级到 2.0.X 后关闭服务 groupName。</li> 
 <li>修复升级到 2.0.X 后删除的服务仍然存在。</li> 
 <li>修复localhost无法在 nacos-server 中使用。</li> 
 <li>修复了 DoubleWrite 删除任务无法删除 v2 模型的持久实例。</li> 
 <li>修复升级后的服务器无法降级和再次升级。</li> 
 <li>修复命名客户端在重新连接到服务器时可能会注册旧的一个实例。</li> 
 <li>修复创建用户错误。</li> 
 <li>修复 doubleWrite 可能将持久性实例注册为临时的。</li> 
 <li>修复当其中一个节点重启时服务器可能降级到 1.X 模型。</li> 
 <li>修复 notifyCenter 可能导致命名数据不一致的问题。</li> 
 <li>修复重启 2.0 模型服务器后 tcp 检查无效的问题。</li> 
 <li>修复导入配置文件时无法覆盖原始配置文件的问题。</li> 
 <li>使用 ak sk 时修复客户端的身份验证问题。</li> 
 <li>修复 Naming API 升级到 v2.x 后无法适配的问题。</li> 
</ul> 
<h3>2.5 测试</h3> 
<ul> 
 <li>为nacos 2.0添加单元测试。</li> 
</ul> 
<h3>三、文档地址</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnacos.io%2Fzh-cn%2F" target="_blank">https://nacos.io/zh-cn/</a></p>
                                        </div>
                                      
</div>
            