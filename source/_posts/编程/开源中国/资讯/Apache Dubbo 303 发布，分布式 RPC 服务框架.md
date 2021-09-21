
---
title: 'Apache Dubbo 3.0.3 发布，分布式 RPC 服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1512'
author: 开源中国
comments: false
date: Tue, 21 Sep 2021 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1512'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>Apache Dubbo 3.0.3 已发布，这是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用、智能容错和负载均衡，以及服务自动注册和发现。</p> 
 <h3>功能</h3> 
 <ul> 
  <li>当 triple 的响应为异常时支持附件（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8488" target="_blank">#8488</a>）</li> 
  <li>提取 DubboSpringInitializer 并支持自定义初始化（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8495" target="_blank">#8495</a>）</li> 
  <li>支持 triple 服务器流（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8542" target="_blank">#8542</a>）</li> 
  <li>增强和修复检查配置（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8483" target="_blank">#8483</a>）</li> 
  <li>Dubbo 编译器支持流（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8566" target="_blank">#8566</a>）</li> 
  <li>支持忽略的网络接口（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8616" target="_blank">#8616</a>）</li> 
  <li>多实例支持（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8662" target="_blank">#8662</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8669" target="_blank">#8669</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8684" target="_blank">#8684</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8717" target="_blank">#8717</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8728" target="_blank">#8728</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8736" target="_blank">#8736</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8737" target="_blank">#8737</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8766" target="_blank">#8766</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8779" target="_blank">#8779</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8789" target="_blank">#8789</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8786" target="_blank">#8786</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8810" target="_blank">#8810</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8818" target="_blank">#8818</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8819" target="_blank">#8819</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8825" target="_blank">#8825</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8823" target="_blank">#8823</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8829" target="_blank">#8829</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8831" target="_blank">#8831</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8824" target="_blank">#8824</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8835" target="_blank">#8835</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8832" target="_blank">#8832</a>）</li> 
  <li>支持配置 HTTP2 设置（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8700" target="_blank">#8700</a>）</li> 
 </ul> 
 <h3><strong>错误修正</strong></h3> 
 <ul> 
  <li>避免调用 destroy 时资源没有释放（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8459" target="_blank">#8459</a>）</li> 
  <li>修复使用 triple 协议不可用返回真实异常（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8458" target="_blank">#8458</a>）</li> 
  <li>Triple：当附件是对象实例时去除 auto wrap（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8473" target="_blank">#8473</a>）</li> 
  <li>解决服务发现场景下的地址传递问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8492" target="_blank">#8492</a>）</li> 
  <li>修复 2181 端口的地址使用错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8466" target="_blank">#8466</a>）</li> 
  <li>修复广播日志格式错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8484" target="_blank">#8484</a>）</li> 
  <li>修复一些注释（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8526" target="_blank">#8526</a>）</li> 
  <li>修复类转换错误并为 ZoneAwareClusterInvoker 添加单元测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8503" target="_blank">#8503</a>）</li> 
  <li>修复 nacos 组在消费者端不可用的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8533" target="_blank">#8533</a>）</li> 
  <li>修复请求超时时序列化检查的 NPE（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8547" target="_blank">#8547</a>）</li> 
  <li>将编译器版本提升到 0.0.3 版本</li> 
 </ul> 
 <h3>优化</h3> 
 <ul> 
  <li>Triple：优化连接和删除执行器（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8486" target="_blank">#8486</a>）</li> 
  <li>压缩一些没有地址的注册表（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8496" target="_blank">#8496</a>）</li> 
  <li>优化 shortestResponseLoadBalance（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8441" target="_blank">#8441</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8519" target="_blank">#8519</a>）</li> 
  <li>优化 dubbo 监控配置（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8477" target="_blank">#8477</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8549" target="_blank">#8549</a>）</li> 
  <li>重构参考配置（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8455" target="_blank">#8455</a>）</li> 
  <li>修复错别字（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8499" target="_blank">#8499</a>）</li> 
  <li>优化所有测试案例中的 zookeeper 超时（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8564" target="_blank">#8564</a>）</li> 
  <li>创建引用时忽略异常（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8534" target="_blank">#8534</a>）</li> 
  <li>为 ListenableRouter 中的一些变量添加 volatile 修饰符（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8579" target="_blank">#8579</a>）</li> 
  <li>调整应用程序、组和 url 版本值的获取（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8582" target="_blank">#8582</a>）</li> 
  <li>为 Triple 协议添加标题过滤器（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8585" target="_blank">#8585</a>）</li> 
 </ul> 
 <h3>依赖项的变化</h3> 
 <ul> 
  <li>升级 curator：5.0.0 -> 5.1.0</li> 
  <li>升级 nacos：2.0.2->2.0.3</li> 
 </ul> 
 <h3>兼容性</h3> 
 <ul> 
  <li>兼容 spring 3.2.x（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8430" target="_blank">#8430</a>）</li> 
 </ul> 
 <p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Freleases%2Ftag%2Fdubbo-3.0.3" target="_blank">https://github.com/apache/dubbo/releases/tag/dubbo-3.0.3</a></p> 
</div>
                                        </div>
                                      
</div>
            