
---
title: 'Dubbo 2.7.11 发布，分布式 RPC 服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5585'
author: 开源中国
comments: false
date: Sat, 08 May 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5585'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Dubbo 2.7.11 已发布，这是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用、智能容错和负载均衡，以及服务自动注册和发现。</p> 
<h3><strong>优化：</strong></h3> 
<ul> 
 <li>使用 nodeCache 来代替 treeCache (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7466" target="_blank">#7466</a>)</li> 
 <li>当第一次使用 getServiceAppMapping 时，减少一次网络传输 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7298" target="_blank">#7298</a>)</li> 
 <li>优化循环条件下的代码 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7480" target="_blank">#7480</a>)</li> 
 <li>当注册表不支持服务自检架构时，兼容切换到接口级服务发现 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7506" target="_blank">#7506</a>)</li> 
 <li>优化通用 releaize 和 generalize (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7520" target="_blank">#7520</a>)</li> 
 <li>使用 @SPI 的封装方法来报告空指针异常bug (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7326" target="_blank">#7326</a>)</li> 
 <li>当从属性文件的数据绑定上遇到错误时抛出异常 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F4757" target="_blank">#4757</a>)</li> 
 <li>简化 OptionUtil#prefixEndOf (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F5833" target="_blank">#5833</a>)</li> 
 <li>修复密码以纯文本打印的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F6931" target="_blank">#6931</a>)</li> 
 <li>优化一些与 consul 相关的代码 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7523" target="_blank">#7523</a>)</li> 
 <li>将 ContextFilter 移至最低级别 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7533" target="_blank">#7533</a>)</li> 
 <li>当 getRegistry 出错时，记录错误 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7545" target="_blank">#7545</a>)</li> 
 <li>将 ClusterRules LoadbalanceRules 添加到 dubbo common (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7534" target="_blank">#7534</a>)</li> 
 <li>使用 CollectionUtils 方法来执行 Collection 的空验证 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7559" target="_blank">#7559</a>)</li> 
 <li>SPI 默认名称调整 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7557" target="_blank">#7557</a>)</li> 
 <li>合并异常，删除多余的接口实现 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F4730" target="_blank">#4730</a>)</li> 
 <li>优化代码，删除无用的对象 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7582" target="_blank">#7582</a>)</li> 
 <li>使用双重检查从缓存中获取元素 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7583" target="_blank">#7583</a>)</li> 
 <li>删除多余的引用 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7604" target="_blank">#7604</a>)</li> 
 <li>修复默认配置无效的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7607" target="_blank">#7607</a>)</li> 
 <li>优化 ZookeeperDynamicConfiguration 中 ThreadPoolExecutor 执行器的创建 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7617" target="_blank">#7617</a>)</li> 
 <li>当提出一个通用的dubbo服务请求时，将检查设置为true可能会导致内存泄漏 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7599" target="_blank">#7599</a>)</li> 
 <li>删除重复调用 metadataInfo#calAndGetRevision 方法 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7630" target="_blank">#7630</a>)</li> 
 <li>删除 DubboBootstrap 中的 EventListener 用法 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7638" target="_blank">#7638</a>)</li> 
 <li>将 GenericFilter 中 PojoUtils.realization 产生的 IllegalArgumentException 转换为 RpcException (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7643" target="_blank">#7643</a>)</li> 
 <li>修复 Dubbo 新版本中 ProtocolConfig 需要一个名字参数的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7624" target="_blank">#7624</a>)</li> 
 <li>使 Dubbo2.7.x 默认不在注册表上注册 serviceNameMapping 信息 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7672" target="_blank">#7672</a>)</li> 
</ul> 
<h3>新<strong>特性：</strong></h3> 
<ul> 
 <li>为 JdkCompiler 添加选项配置机制 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7232" target="_blank">#7232</a>)</li> 
 <li>为 ConditionRouter 添加参数路由 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7378" target="_blank">#7378</a>)</li> 
 <li>解决重复注册提供者 BeanDefinition 的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7494" target="_blank">#7494</a>)</li> 
 <li>为 matedata 定义添加注释字段 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7660" target="_blank">#7660</a>)</li> 
</ul> 
<h3><strong>依赖项升级</strong></h3> 
<ul> 
 <li>升级 <code>org.javassist.javassist:3.23.1-GA</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7516" target="_blank">#7516</a></li> 
 <li>升级 <code>com.alibaba.nacos.nacos-client:1.4.1</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7676" target="_blank">#7676</a></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Freleases%2Ftag%2Fdubbo-2.7.11" target="_blank">https://github.com/apache/dubbo/releases/tag/dubbo-2.7.11</a></p>
                                        </div>
                                      
</div>
            