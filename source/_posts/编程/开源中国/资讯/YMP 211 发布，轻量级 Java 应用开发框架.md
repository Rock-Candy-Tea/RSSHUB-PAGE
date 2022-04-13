
---
title: 'YMP 2.1.1 发布，轻量级 Java 应用开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6966'
author: 开源中国
comments: false
date: Wed, 13 Apr 2022 09:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6966'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>YMP 是一个非常简单、易用的轻量级 Java 应用开发框架，涵盖 AOP、IoC、WebMVC、ORM、Validation、Plugin、Serv、Cache 等特性，主要技术特点：</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>采用组件化、模块方式打包，可按需装配，灵活可扩展；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>采用微内核实现 AutoScan、AOP、IoC、Events 等，涵盖 SSH 和 SSM 框架中绝大部分核心功能；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>统一配置体系结构，感受不一样的文件资源配置及管理模式；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>整合多种日志系统（Log4j、JCL、Slf4j 等）、日志文件可分离存储；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>轻量级持久化层封装，针对 RDBMS（MySQL、SQL Server、Oracle、PostgreSQL）和 NoSQL（MongoDB、Redis）提供支持；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>完善的插件机制，助力于更细颗粒度的业务拆分；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>独特的独立服务（Serv）开发体验；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>功能强大的验证框架，完全基于 Java 注解，易于使用和扩展；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>灵活的缓存服务，支持 EhCache、Redis 和多级缓存（MultiLevel）技术；</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>配置简单的 MVC 架构，强大且易于维护和扩展，支持 RESTful 风格，支持 JSP、HTML、Binary、Freemarker、Velocity 等多种视图技术；</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>官网及文档已同步更新，新版本已提交至 Maven 中央库，可以通过以下配置获取各模块依赖：</span></p> 
<pre style="text-align:left"><span><dependency></span>
<span>  <groupId>net.ymate.platform</groupId></span>
<span>  <artifactId>ymate-platform-<MODULE_NAME></artifactId></span>
<span>  <version>2.1.1</version></span>
<span></dependency></span></pre> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>请将<MODULE_NAME>替换为具体模块名，模块详见: </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsearch.maven.org%2Fsearch%3Fq%3Dnet.ymate.platform" target="_blank"><span>The Central Repository Search Engine</span></a></span></p> 
</blockquote> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>相关链接：</span></p> 
<blockquote> 
 <p style="margin-left:.8em; margin-right:0"><span>GitHub：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsuninformation%2Fymate-platform-v2" target="_blank"><span>https://github.com/suninformation/ymate-platform-v2</span></a></span></p> 
 <p style="margin-left:.8em; margin-right:.8em"><span>Gitee： </span><span><a href="https://gitee.com/suninformation/ymate-platform-v2"><span>https://gitee.com/suninformation/ymate-platform-v2</span></a></span></p> 
 <p style="margin-left:0; margin-right:.8em"><span>   文档： </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fymate.net%2Fguide%2F" target="_blank"><span>https://ymate.net/guide/</span></a></span></p> 
</blockquote> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>框架主要更新内容：</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>【JDBC】</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>补充常规运算函数相关内容</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化常规运算函数的减法和除法的参数顺序</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>修正GroupBy分组对象构造方法调用错误</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化以支持$表达式允许通过冒号分隔符指定其数据类型</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>将EntityMeta类中有关于属性与字段名之间转换的方法移至ClassUtils类并更新相关文档</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>【Serv】</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化统一线程的命名规则</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化服务线程命名并为心跳包内容增加空判断</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>移除不必要的日志输出代码</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化判断并修正在未开启空闲会话检测时执行会话管理器关闭操作可能产生的空指针异常</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>【Configuration】</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>增加配置文件存放的基准目录名称参数项</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>【Other】</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>更新依赖包版本</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>更新文档及配置</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>同时更新的还包括以下扩展工具及模块：</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>任务调度（Schedule）v1.0.1</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>为 YMP 框架提供基于 Quartz 技术的任务调度服务集成与模块封装。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-module-schedule">https://gitee.com/suninformation/ymate-module-schedule</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>单点登录（SSO）v2.0.1</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>基于 YMP 框架实现的单点登录模块封装。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-module-sso">https://gitee.com/suninformation/ymate-module-sso</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>YMP 框架工程原型（Archetypes）</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>本项目为快速搭建基于 YMP 轻量级 Java 应用开发框架的工程代码而提供的一系列 Maven Archetypes 模板。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-maven-archetypes">https://gitee.com/suninformation/ymate-maven-archetypes</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>YMP 框架 Maven 插件 v1.0.1</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>本项目为基于 YMP 轻量级 Java 应用开发框架开发的小伙伴儿们提供的一系列 Maven 插件工具，辅助快速生成代码与服务等。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-maven-plugin">https://gitee.com/suninformation/ymate-maven-plugin</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>还有更多扩展模块待整理后发布，请关注： </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fymate.net%2Fmodules" target="_blank">https://ymate.net/modules</a></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<h3 style="text-align:start"><span>One More Thing</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>YMP 不仅提供便捷的 Web 及其它 Java 项目的快速开发体验，也将不断提供更多丰富的项目实践经验。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>了解更多有关 YMP 框架的内容，请访问官网：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fymate.net%2F" target="_blank"><span>https://ymate.net</span></a></span></p> 
<p> </p>
                                        </div>
                                      
</div>
            