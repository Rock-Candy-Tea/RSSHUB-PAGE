
---
title: 'Apache Dubbo 3.0.4 发布，分布式 RPC 服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1448'
author: 开源中国
comments: false
date: Thu, 28 Oct 2021 06:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1448'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Apache Dubbo 3.0.4 已发布，这是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用、智能容错和负载均衡，以及服务自动注册和发现。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">此版本更新内容：</span></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">新特性</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加记录器禁用选项（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8885" target="_blank">#8885</a>）</li> 
 <li>支持后台启动模块（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8869" target="_blank">#8869</a>）</li> 
 <li>支持多订阅服务扩展（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8908" target="_blank">#8908</a>）</li> 
 <li>支持原生 dubbo 3.0.4（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8966" target="_blank">#8966</a>）</li> 
 <li>支持取消 streamObserver （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8946" target="_blank">#8946</a>）</li> 
 <li>三重传输支持消息压缩（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8817" target="_blank">#8817</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9018" target="_blank">#9018</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9021" target="_blank">#9021</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9032" target="_blank">#9032</a>）</li> 
 <li>支持模型字段中的缓存属性（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9025" target="_blank">#9025</a>）</li> 
 <li>支持使用 maven 插件运行 dubbo 原生项目（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8970" target="_blank">#8970</a>）</li> 
 <li>为<span> </span><code>ExtensionLoader<span> </span></code>添加<span> </span><code>ExtensionClassLoaderPackages<span> </span></code>支持（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9061" target="_blank">#9061</a>）</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong> bug 修复</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 appendAttribute 键（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8847" target="_blank">#8847</a>）</li> 
 <li>修复 RpcContext 重复覆盖的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8842" target="_blank">#8842</a>）</li> 
 <li>修复<span> </span><code>addParam()<span> </span></code>的<span> </span><code>StringIndexOutOfBoundsException</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8799" target="_blank">#8799</a>）</li> 
 <li>在<span> </span><code>decode(Channel, InputStream)</code><span> </span>处添加空调用检查（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8812" target="_blank">#8812</a>）</li> 
 <li>修复<span> </span><code>IllegalStateException</code><span> </span>和<span> </span><code>doOverrideIfNecessary NPE</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8768" target="_blank">#8768</a>）</li> 
 <li>添加 zookeeper 节点数据创建事件检查（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8833" target="_blank">#8833</a>）</li> 
 <li>修复：使用多个协议并指定端口时，无法启动服务。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8769" target="_blank">#8769</a>）</li> 
 <li>修复 urlInvokerMap 并发访问问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8701" target="_blank">#8701</a>）</li> 
 <li>修复 bean 的 Deployer State 延迟注入问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8867" target="_blank">#8867</a>）</li> 
 <li>ZookeeperRegistry CountDownLatch 应该被释放并添加一些 UT （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8870" target="_blank">#8870</a>）</li> 
 <li>修复 serialVersionUID（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8852" target="_blank">#8852</a>）</li> 
 <li>修复并发 bean 创建错误的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8883" target="_blank">#8883</a>）</li> 
 <li>恢复 Servlet 页面 API（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8884" target="_blank">#8884</a>）</li> 
 <li>修复 CountDownLatch 未被释放的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8878" target="_blank">#8878</a>）</li> 
 <li>修复订阅时，查看配置部分不可用的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8879" target="_blank">#8879</a>）</li> 
 <li>在发布 ServiceDefinition 时修复 Class.forName（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8894" target="_blank">#8894</a>）</li> 
 <li>Socks 代理过滤本地地址（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8876" target="_blank">#8876</a>）</li> 
 <li>修复延迟导出不适用于 ServiceConfig（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8912" target="_blank">#8912</a>）</li> 
 <li>修复 MergeableClusterInvoker NPE（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8891" target="_blank">#8891</a>）</li> 
 <li>添加 destroy() 调用关闭 tomcat 服务器端口（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8920" target="_blank">#8920</a>）</li> 
 <li>在 LazyConnectExchangeClient 关闭方法中将客户端设置为 null（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8881" target="_blank">#8881</a>）</li> 
 <li>修复：telnet 中 registry cast to AbstractRegistry 错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8619" target="_blank">#8619</a>）</li> 
 <li>修复 AbstractServiceDiscovery#serviceInstance 属性不添加 volatile 修饰符（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8915" target="_blank">#8915</a>）</li> 
 <li>修复地址为空时状态路由器抛出异常（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8951" target="_blank">#8951</a>）</li> 
 <li>在 Injvm Invoke 中重置 ServiceModel（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8952" target="_blank">#8952</a>）</li> 
 <li>修复实例模式 mesh 路由无法获取 url 参数（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8947" target="_blank">#8947</a>）</li> 
 <li>修复异常信息（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8974" target="_blank">#8974</a>）</li> 
 <li>kryo 序列化恢复判断 jdk 的方法（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8968" target="_blank">#8968</a>）</li> 
 <li>修复重复的 ApplicationConfig 错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8989" target="_blank">#8989</a>）</li> 
 <li>testRecover() 覆盖 removeFailedRegisteredTask 和 removeFailedSubscribedTask（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8981" target="_blank">#8981</a>）</li> 
 <li>修复 ConfigManagerTest 拼写错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8990" target="_blank">#8990</a>）</li> 
 <li>修复创建 SPI 的自适应类时的并发问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8998" target="_blank">#8998</a>）</li> 
 <li>修复 Listener 提前初始化（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9006" target="_blank">#9006</a>）</li> 
 <li>在关闭操作时检查 ClosedChannelException（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9010" target="_blank">#9010</a>）</li> 
 <li>NotifyService 回调方法的正确参数类型（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9008" target="_blank">#9008</a>）</li> 
 <li>设置模块在 applicationDeployer 中启动 checkStarted()（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9013" target="_blank">#9013</a>）</li> 
 <li>修复多实例迁移报告（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9020" target="_blank">#9020</a>）</li> 
 <li>在 get 配置中修复 NPE（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9024" target="_blank">#9024</a>）</li> 
 <li>增加检查 localMetadataService.blockUntilUpdated stat 的逻辑（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9002" target="_blank">#9002</a>）</li> 
 <li>在 blockUntilUpdated 处检查 applicationModel 销毁状态（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9001" target="_blank">#9001</a>）</li> 
 <li>移除 RegistryFactory 扩展点的默认实现（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9027" target="_blank">#9027</a>）</li> 
 <li>修复实例更新失败的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9040" target="_blank">#9040</a>）</li> 
 <li>修复 tomcat 端口已被使用时进程无法停止的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8552" target="_blank">#8552</a>）</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>优化</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将 ScopeModel 添加到本地调用（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8849" target="_blank">#8849</a>）</li> 
 <li>修复优化字段范围（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8751" target="_blank">#8751</a>）</li> 
 <li>优化 dubbo 元数据模块的部分代码（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8783" target="_blank">#8783</a>）</li> 
 <li>一开始不显示 replaceWithLazyClient() 警告（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8814" target="_blank">#8814</a>）</li> 
 <li>统一错误信息（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8794" target="_blank">#8794</a>）</li> 
 <li>提取 MigrationRule 的常量（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8850" target="_blank">#8850</a>）</li> 
 <li>改进 MigrationRuleListener#destroy 方法的逻辑（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8853" target="_blank">#8853</a>）</li> 
 <li>添加 ClassLoaderResourceLoader 来缓存 ClassLoader 的资源（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8866" target="_blank">#8866</a>）</li> 
 <li>超时关闭流（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8888" target="_blank">#8888</a>）</li> 
 <li>大幅优化某些 UnitTest 用例成本时间（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8844" target="_blank">#8844</a>）</li> 
 <li>提高单元测试效率（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8877" target="_blank">#8877</a>）</li> 
 <li>当 DefaultFuture 被取消时， TimeoutCheckTask 应该被取消（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8898" target="_blank">#8898</a>）</li> 
 <li>删除无意义的代码（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8887" target="_blank">#8887</a>）</li> 
 <li>尝试从接口参数加载类（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8905" target="_blank">#8905</a>）</li> 
 <li>为 SpringBean Initializer 添加 ModuleModel 限定符（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8904" target="_blank">#8904</a>）</li> 
 <li>调用 timeout 时转换 TimeoutException（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8906" target="_blank">#8906</a>）</li> 
 <li>重构 MetricsConfig（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8785" target="_blank">#8785</a>）</li> 
 <li>当 DefaultFuture2 被取消时，TimeoutCheckTask 应该被取消（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8901" target="_blank">#8901</a>）</li> 
 <li>添加重置帧处理程序（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8871" target="_blank">#8871</a>）</li> 
 <li>优化三服务器发送帧错误处理程序（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8922" target="_blank">#8922</a>）</li> 
 <li>优化多个部分代码（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8900" target="_blank">#8900</a>）</li> 
 <li>MultipleRegistry 去除重复 URL（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8896" target="_blank">#8896</a>）</li> 
 <li>gson格式泛型调用的优化（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8924" target="_blank">#8924</a>）</li> 
 <li>Catch handler.caught() throwable 的 MultiMessageHandler（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8930" target="_blank">#8930</a>）</li> 
 <li>重构 Injvm 调用（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8926" target="_blank">#8926</a>）</li> 
 <li>将调用中的 LinkedHashMap 还原为 HashMap（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8941" target="_blank">#8941</a>）</li> 
 <li>销毁执行器并改进测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8928" target="_blank">#8928</a>）</li> 
 <li>移除 SimpleChannelInboundHandler（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8893" target="_blank">#8893</a>）</li> 
 <li>使用新算法优化哈希负载平衡一致性（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8948" target="_blank">#8948</a>）</li> 
 <li>添加等待注册完成的闩锁（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8962" target="_blank">#8962</a>）</li> 
 <li>删除未使用的客户端处理程序（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8955" target="_blank">#8955</a>）</li> 
 <li>忽略 Injvm 调用副本的通用调用（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8986" target="_blank">#8986</a>）</li> 
 <li>通过 ScopeModelAware 将 applicationModel 注入 TripleHttp2Protocol（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8984" target="_blank">#8984</a>）</li> 
 <li>优化 AbstractRegistry（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8971" target="_blank">#8971</a>）</li> 
 <li>将本地调用者从 Collections.singletonList 更改为 ArrayList（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8997" target="_blank">#8997</a>）</li> 
 <li>添加serializingExecutor（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8999" target="_blank">#8999</a>）</li> 
 <li>发送和删除逻辑前无需估计头部大小（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8802" target="_blank">#8802</a>）</li> 
 <li>添加健康服务取消处理程序（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9004" target="_blank">#9004</a>）</li> 
 <li>删除方法级别的连接配置（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9011" target="_blank">#9011</a>）</li> 
 <li>提取常量并修复错别字（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9019" target="_blank">#9019</a>）</li> 
 <li>用future来替换latch（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9030" target="_blank">#9030</a>）</li> 
 <li>支持默认服务实例的深拷贝（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9029" target="_blank">#9029</a>）</li> 
 <li>添加问题模板（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9036" target="_blank">#9036</a>）</li> 
 <li>为 LazyConnectExchangeClient 重建 InstanceAddressURL 到 ServiceConfigURL（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9041" target="_blank">#9041</a>）</li> 
 <li>填充 ListBoolMatch 代码并优化 DubboAttachmentMatch 代码（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8448" target="_blank">#8448</a>）</li> 
 <li>格式三元组（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9058" target="_blank">#9058</a>）</li> 
 <li>管理全局资源和执行器服务，修复 zk 客户端连接（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9033" target="_blank">#9033</a>）</li> 
 <li>添加已弃用的描述（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9065" target="_blank">#9065</a>）</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>稳定性提升</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>为<span> </span><code>ServiceDefinitionBuilderTest</code><span> </span>添加<span> </span><code>[annotation]</code>测试用例，并删除未使用的参数（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8788" target="_blank">#8788</a>）</li> 
 <li>为<span> </span><code>MetadataReportInstance</code><span> </span>和<span> </span><code>AbstractServiceNameMapping</code><span> </span>添加单元测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8846" target="_blank">#8846</a>）</li> 
 <li>增强<span> </span><code>FailoverClusterInvoker</code><span> </span>单元测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8851" target="_blank">#8851</a>）</li> 
 <li>增强<span> </span><code>FailbackClusterInvoker<span> </span></code>单元测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8861" target="_blank">#8861</a>）</li> 
 <li>增强<span> </span><code>FailfastClusterInvokerTest<span> </span></code>单元测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8864" target="_blank">#8864</a>）</li> 
 <li>增强<span> </span><code>ForkingClusterInvoker<span> </span></code>单元测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8865" target="_blank">#8865</a>）</li> 
 <li>添加<span> </span><code>ZookeeperMetadataReportTest<span> </span></code>测试用例（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8840" target="_blank">#8840</a>）</li> 
 <li>为<span> </span><code>ServiceInstanceMetadataUtilsTest</code><span> </span>添加测试用例（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8914" target="_blank">#8914</a>）</li> 
 <li>为<span> </span><code>CuratorFrameworkUtils</code><span> </span>和<span> </span><code>AbstractServiceDiscoveryFactory</code><span> </span>添加单元测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8886" target="_blank">#8886</a>）</li> 
 <li>修复<code>testInvoke_retryTimes_withBizException</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8910" target="_blank">#8910</a>）</li> 
 <li>为<span> </span><code>StandardMetadataServiceURLBuilder<span> </span></code>添加单元测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8913" target="_blank">#8913</a>）</li> 
 <li>添加一些<span> </span><code>AvailableClusterInvoker</code><span> </span>单元测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8934" target="_blank">#8934</a>）</li> 
 <li>添加单元测试和一些优化（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8945" target="_blank">#8945</a>）</li> 
 <li>补丁关机 hooks 测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8958" target="_blank">#8958</a>）</li> 
 <li>增强可合并集群调用测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8889" target="_blank">#8889</a>）</li> 
 <li>验证远程 url 的远程引用（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8973" target="_blank">#8973</a>）</li> 
 <li>为<span> </span><code>MultiplexProtocolConnectionManagerTest</code><span> </span>配置 tri 扩展（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8979" target="_blank">#8979</a>）</li> 
 <li>为<code><span> </span>Http2ProtocolDetector</code><span> </span>和<span> </span><code>NettyEventLoopF​​actory</code><span> </span>添加单元测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9023" target="_blank">#9023</a>）</li> 
 <li>修复<span> </span><code>AbstractMetadataReportTest</code><span> </span>和<span> </span><code>AbstractMetadataReportFactoryTest</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8807" target="_blank">#8807</a>）</li> 
 <li>为<span> </span><code>ChannelBuffers</code><span> </span>和<span> </span><code>ChannelBufferFactory</code><span> </span>添加单元测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9031" target="_blank">#9031</a>）</li> 
 <li>为<span> </span><code>dubbo-registry-nacos</code><span> </span>添加单元测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9035" target="_blank">#9035</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Freleases%2Ftag%2Fdubbo-3.0.4" target="_blank">https://github.com/apache/dubbo/releases/tag/dubbo-3.0.4</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            