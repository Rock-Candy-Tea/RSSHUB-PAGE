
---
title: 'YMP 2.0.11 发布，轻量级 Java 应用开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5336'
author: 开源中国
comments: false
date: Sat, 11 Dec 2021 01:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5336'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>本次更新为紧急版本升级，主要针对 </span><span><a href="https://www.oschina.net/news/172999"><span>Apache Log4j2 远程代码执行漏洞</span></a></span><span> 进行问题修复、依赖包及日志模块逻辑代码升级更新。新版本已提交至Maven中央库，可以通过以下配置获取各模块依赖：</span></p> 
<pre style="text-align:left"><span><dependency></span>
<span>  <groupId>net.ymate.platform</groupId></span>
<span>  <artifactId>ymate-platform-<MODULE_NAME></artifactId></span>
<span>  <version>2.0.11</version></span>
<span></dependency></span></pre> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>请将<MODULE_NAME>替换为具体模块名，模块详见: </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsearch.maven.org%2Fsearch%3Fq%3Dnet.ymate.platform" target="_blank"><span>The Central Repository Search Engine</span></a></span></p> 
</blockquote> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>相关链接：</span></p> 
<blockquote> 
 <p style="margin-left:.8em; margin-right:0"><span>GitHub：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsuninformation%2Fymate-platform-v2" target="_blank"><span>https://github.com/suninformation/ymate-platform-v2</span></a></span></p> 
 <p style="margin-left:.8em; margin-right:.8em"><span>码云地址：</span><span><a href="https://gitee.com/suninformation/ymate-platform-v2"><span>https://gitee.com/suninformation/ymate-platform-v2</span></a></span></p> 
 <p style="margin-left:.8em; margin-right:.8em"><span>开发手册：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fymate.net%2Fguide%2F" target="_blank"><span>https://ymate.net/guide/</span></a></span></p> 
</blockquote> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<h3 style="text-align:start"><span>主要更新内容：</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>【Core】</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化调整日志模块初始化逻辑并更新 Log4j2 版本以解决 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnvd.nist.gov%2Fvuln%2Fdetail%2FCVE-2021-44228" target="_blank"><span>CVE-2021-44228</span></a></span><span> 问题；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>更新依赖包版本</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>【Redis】</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化客户端名称和密码参数值为空时的处理逻辑；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>修正端口配置项常量值错误；</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>【Cache】</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化EhCache缓存销毁逻辑以免产生IllegalStateException异常；</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<h3 style="text-align:start"><span>One More Thing</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>YMP 是一个非常简单、易用的轻量级Java应用开发框架，涵盖 AOP、IoC、WebMVC、ORM、Validation、Plugin、Serv、Cache 等特性，主要技术特点：</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>采用组件化、模块化打包方式，可按需装配，灵活可扩展；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>采用微内核实现Autoscan、AOP、IoC、Event等，涵盖SSH框架中绝大部分核心功能；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>统一配置体系结构，感受不一样的文件资源配置及管理模式；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>整合多种日志系统（log4j、jcl、slf4j）、日志文件可分离存储；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>轻量级持久化层封装，针对RDBMS（MySQL、SQLServer、Oracle、PostgreSQL等）和NoSQL（MongoDB、Redis等）提供支持；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>完善的插件机制，助力于更细颗粒度的业务拆分；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>独特的独立服务开发体验；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>功能强大的验证框架，完全基于Java注解，易于使用和扩展；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>灵活的缓存服务，支持EhCache、Redis和多级缓存（MultiLevel）技术；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>配置简单的MVC架构，强大且易于维护和扩展，支持RESTful风格，支持JSP、HTML、Binary、Freemarker、Velocity、Beetl等多种视图技术；</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>YMP 不仅提供便捷的 Web 及其它 Java 项目的快速开发体验，也将不断提供更多丰富的项目实践经验。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>了解更多有关 YMP 框架的内容，请访问官网：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fymate.net%2F" target="_blank"><span>https://ymate.net/</span></a></span></p>
                                        </div>
                                      
</div>
            