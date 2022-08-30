
---
title: 'Logback 1.3.0 & 1.4.0 发布，Java 日志框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7248'
author: 开源中国
comments: false
date: Tue, 30 Aug 2022 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7248'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Logback 是由 log4j 创始人设计的又一个开源日志组件，分成三个模块：logback-core、logback- classic 和 logback-access。</p> 
 <ul> 
  <li style="text-align:start">logback-core 是其它两个模块的基础模块。</li> 
  <li style="text-align:start">logback-classic 是 log4j 的一个改良版本，完整实现 SLF4J API ，可以很方便地更换成其它日志系统如 log4j 或 JDK14 Logging。</li> 
  <li style="text-align:start">logback-access 访问模块与 Servlet 容器集成提供通过 Http 来访问日志的功能。</li> 
 </ul> 
</blockquote> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前 Logback 发布了 1.3 & 1.4 两个版本，<span style="color:#000000">logback 1.3.x 支持 Java EE 版本，而 logback 1.4.x 支持 Jakarta EE，两个版本的功能相同。</span>为 logback 1.2 编写的 logback 组件在 1.3 版本中无需更改即可工作。但是 logback 的配置系统 Joran 已经被重写为使用可单独处理的内部表示模型。因此，依赖于 Joran 的代码需要适应 Joran 的变化。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">由于对 Joran 的增强，logback 配置脚本现在基本上是<span> </span><span style="color:#000000">order-free<span> </span></span>的。例在可以在 logger 中首次引用 appender 之后对其进行定义。此外，不再实例化未引用的附加程序。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>更改列表：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Logback-classic 使用名为 DefaultJoranConfigurator 的默认配置器提供自身程序初始化。用户可以通过将自己的自定义配置器提供程序安装为可加载服务，来覆盖默认配置器。</li> 
 <li>因安全原因和缺乏使用， ch.qos.logback.classic.jmx 包被删除。</li> 
 <li>修复了CachingDateFormat 类中 java.time.DateTimeFormatter 的不正确初始化（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.qos.ch%2Fbrowse%2FLOGBACK-1659" target="_blank">LOGBACK-1659</a>）。</li> 
 <li>修正了 FileFilterUtil.filesInFolderMatchingStemRegex 方法的性能问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.qos.ch%2Fbrowse%2FLOGBACK-1409" target="_blank">LOGBACK-1409</a>） 。</li> 
 <li>在 logback-access 中，修复了使用 comitted 状态检索响应状态的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.qos.ch%2Fbrowse%2FLOGBACK-1580" target="_blank">LOGBACK-1580</a>）。</li> 
 <li>在 logback-access 中，修复了 AccessEvent 类的 getRequestContent 和buildRequestParameterMap 方法中的错误处理。</li> 
 <li>修复了与 LoggingEvent 中的纳秒字段相关的一些问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.qos.ch%2Fbrowse%2FLOGBACK-1661" target="_blank">LOGBACK-1661</a>）。 </li> 
 <li>修复了与 LoggingEvent 中的 sequenceNumber 字段相关的一些问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.qos.ch%2Fbrowse%2FLOGBACK-1662" target="_blank">LOGBACK-1662</a><span style="color:#000000"><span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.qos.ch%2Fbrowse%2FLOGBACK-1663" target="_blank">LOGBACK-1663</a>)。 </li> 
 <li>在初始化时打印 Logback-classic 版本号，该信息也可通过 ch.qos.logback.core.util.EnvUtil 中的 logbackVersion() 方法获得（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.qos.ch%2Fbrowse%2FLOGBACK-1597" target="_blank">LOGBACK-1597</a>）。 </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>更新公告：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flogback.qos.ch%2Fnews.html" target="_blank">https://logback.qos.ch/news.html</a></p>
                                        </div>
                                      
</div>
            