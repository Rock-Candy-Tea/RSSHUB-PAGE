
---
title: 'Apache Dubbo 2.7.13 发布，分布式 RPC 服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5102'
author: 开源中国
comments: false
date: Tue, 03 Aug 2021 06:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5102'
---

<div>   
<div class="content">
                                                                                            <p>Apache Dubbo 2.7.13 已发布，这是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用、智能容错和负载均衡，以及服务自动注册和发现。</p> 
<p><strong>特性：</strong></p> 
<ul> 
 <li>将文件参数添加到 MetadataReportBuilder( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8031" target="_blank">#8031</a> )</li> 
 <li>如果发生异常，延迟导出服务器应打印堆栈跟踪。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8125" target="_blank">#8125</a>）</li> 
 <li>增加 redisRegistry 消费者端的服务检测逻辑（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7929" target="_blank">#7929</a>）</li> 
 <li>使用旧命名空间时，支持 xml 中的 dubbo:annotation 元素标签。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7995" target="_blank">#7995</a>）</li> 
 <li>支持禁用  shutdown hook ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8369" target="_blank">#8369</a> )</li> 
</ul> 
<p><strong>Bug 修复：</strong></p> 
<ul> 
 <li>修复实例更改事件名称格式问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8346" target="_blank">#8346</a>）</li> 
 <li>修复 String.format 缺少来自 BroadcastClusterInvoker 链接的 arg ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8348" target="_blank">#8348</a> )</li> 
 <li>默认禁用 telnet 并修复 ut，重置资源 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8239" target="_blank">#8239</a> )</li> 
 <li>注释无法序列化，因此更改为 String ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F7908" target="_blank">#7908</a> )</li> 
 <li>修复 ReferenceConfigCache#destroy 方法没有调用 proxy.$destroy() 的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8065" target="_blank">#8065</a> )</li> 
 <li>修复 multi-registry bug ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8034" target="_blank">#8034</a> )</li> 
 <li>[Dubbo-6720] 修复同界面 unexport 和 export 失败的 bug。还支持热加载服务 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F6720" target="_blank">#6720</a> )</li> 
 <li>修复 urls 可能为 null，在 ConfigValidationUtils 中会抛出 NullPointerException ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F8020" target="_blank">#8020</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8021" target="_blank">#8021</a> )</li> 
 <li>修复重复导入 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8015" target="_blank">#8015</a> )</li> 
 <li>修复 spring spi 扩展在启动过程中保持 printing warn log 的问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F6144" target="_blank">#6144</a>）</li> 
 <li>[Dubbo-8172] DefaultFuture. closeChannel() 时不关闭 ExecutorService。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8188" target="_blank">#8188</a> )</li> 
</ul> 
<p><strong>优化：</strong></p> 
<ul> 
 <li>优化 ShortestResponseLoadBalance 活动参数 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8318" target="_blank">#8318</a> )</li> 
 <li>为本地 hessian 和 hessian rpc 协议设置特定的序列化程序 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8238" target="_blank">#8238</a> )</li> 
 <li>增强元数据报告配置。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8268" target="_blank">#8268</a>）</li> 
 <li>对于兼容的 nacos 服务器低版本，应该检查来自 nacos 服务器的响应是否为空。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8229" target="_blank">#8229</a>）</li> 
 <li>使用服务名称映射键避免逻辑冲突。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8184" target="_blank">#8184</a>）</li> 
 <li>测试回调方法的事务<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fissues%2F8098" target="_blank">#8098</a> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8120" target="_blank">#8120</a> )</li> 
 <li>改进 URLStrParser.java 的代码（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8085" target="_blank">#8085</a>）</li> 
 <li>删除冗余类：\common\utils\ClassHelper.java ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8084" target="_blank">#8084</a> )</li> 
 <li>......</li> 
</ul> 
<p><strong>代码改进</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8264" target="_blank">#8264</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8258" target="_blank">#8258</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8136" target="_blank">#8136</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8141" target="_blank">#8141</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8114" target="_blank">#8114</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8023" target="_blank">#8023</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8000" target="_blank">#8000</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8001" target="_blank">#8001</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8006" target="_blank">#8006</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8355" target="_blank">#8355</a></li> 
</ul> 
<p><strong>依赖升级</strong></p> 
<ul> 
 <li>升级 artifact com.alibaba.spring.spring-context-support: 1.0.11 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8217" target="_blank">#8217</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Freleases%2Ftag%2Fdubbo-2.7.13" target="_blank">https://github.com/apache/dubbo/releases/tag/dubbo-2.7.13</a></p>
                                        </div>
                                      
</div>
            