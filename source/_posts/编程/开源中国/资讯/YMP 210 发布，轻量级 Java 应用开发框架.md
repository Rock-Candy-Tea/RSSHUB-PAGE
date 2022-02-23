
---
title: 'YMP 2.1.0 发布，轻量级 Java 应用开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9066'
author: 开源中国
comments: false
date: Wed, 23 Feb 2022 04:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9066'
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
<span>  <version>2.1.0</version></span>
<span></dependency></span></pre> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>请将<MODULE_NAME>替换为具体模块名，模块详见: </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsearch.maven.org%2Fsearch%3Fq%3Dnet.ymate.platform" target="_blank"><span>The Central Repository Search Engine</span></a></span></p> 
</blockquote> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>相关链接：</span></p> 
<blockquote> 
 <p style="margin-left:.8em; margin-right:0"><span>GitHub：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsuninformation%2Fymate-platform-v2" target="_blank"><span>https://github.com/suninformation/ymate-platform-v2</span></a></span></p> 
 <p style="margin-left:.8em; margin-right:.8em"><span>Gitee： </span><span><a href="https://gitee.com/suninformation/ymate-platform-v2"><span>https://gitee.com/suninformation/ymate-platform-v2</span></a></span></p> 
 <p style="margin-left:0; margin-right:.8em"><span>文档： </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fymate.net%2Fguide%2F" target="_blank"><span>https://ymate.net/guide/</span></a></span></p> 
</blockquote> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>本次大版本更新间隔时间较长，主要是对模块的加载机制进行了大的优化调整，在近两年时间，通过实际项目使用过程中不断完善、打磨各个模块的细节，尽可能的做到让它更方便、更实用、更稳定。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>在兼容性方面，由于工程的包结构有所调整，部份类所在包名与 YMP v2.0.x 版本存在差异，因此升级时需要重新导入，除此之外，功能及使用上 100% 覆盖。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>另外，最耗时费力的就编写文档，也是 YMP 框架发布以来最全面的一次文档更新。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>本次除发布框架新版本之外，一同发布的还有以下扩展工具及模块：</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>接口文档生成器（Apidocs)：</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>为 YMP 框架开发提供的一套基于 Java 注解实现的接口开发文档自动生成工具，支持 HTML、Gitbook、Postman、JSON、 Markdown 等格式。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-apidocs">https://gitee.com/suninformation/ymate-apidocs</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>验证码（Captcha）</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>基于 YMP 框架实现的验证码模块，支持图片、邮件和短信三种验证类型，采用注解验证，配置简单、灵活，可自定义扩展。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-module-captcha">https://gitee.com/suninformation/ymate-module-captcha</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>嵌入式容器（Embed）</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>本项目为可执行嵌入式 Web 容器，在原始 WAR 包文件结构的基础上为其指定引导程序及相关依赖文件，并通过命令行方式直接启动 Web 服务，从而达到简化 Web 工程部署流程的目的。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-embed">https://gitee.com/suninformation/ymate-embed</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>文件上传（Fileuploader）</span><span> </span><span>基于 YMP 框架实现的文件上传及资源访问服务模块。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-module-fileuploader">https://gitee.com/suninformation/ymate-module-fileuploader</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>任务调度（Schedule）</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>为 YMP 框架提供基于 Quartz 技术的任务调度服务集成与模块封装。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-module-schedule">https://gitee.com/suninformation/ymate-module-schedule</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>单点登录（SSO）</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>基于 YMP 框架实现的单点登录模块封装。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-module-sso">https://gitee.com/suninformation/ymate-module-sso</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>WEB 标签库（Taglib）</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>为 YMP 框架提供的一套 JSP 标签库。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-web-taglib">https://gitee.com/suninformation/ymate-web-taglib</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>集成测试（Test）</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>为 YMP 框架集成 JUnit 测试开发工具包。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-platform-test">https://gitee.com/suninformation/ymate-platform-test</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Unpack</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>基于 YMP 框架实现的文件解包器模块封装，用于自动执行文件解压。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-module-unpack">https://gitee.com/suninformation/ymate-module-unpack</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Websocket</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>为 YMP 框架提供对 WebSocket 技术的集成与模块封装。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-module-websocket">https://gitee.com/suninformation/ymate-module-websocket</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>YMP 框架工程原型（Archetypes）</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>本项目为快速搭建基于 YMP 轻量级 Java 应用开发框架的工程代码而提供的一系列 Maven Archetypes 模板。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-maven-archetypes">https://gitee.com/suninformation/ymate-maven-archetypes</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>YMP 框架 Maven 插件</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>本项目为基于 YMP 轻量级 Java 应用开发框架开发的小伙伴儿们提供的一系列 Maven 插件工具，辅助快速生成代码与服务等。</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>码云：</span><span><a href="https://gitee.com/suninformation/ymate-maven-plugin">https://gitee.com/suninformation/ymate-maven-plugin</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>还有更多扩展模块待整理后发布，请关注： </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fymate.net%2Fmodules" target="_blank">https://ymate.net/modules</a></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<h3 style="text-align:start"><span>One More Thing</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>YMP 不仅提供便捷的 Web 及其它 Java 项目的快速开发体验，也将不断提供更多丰富的项目实践经验。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>了解更多有关 YMP 框架的内容，请访问官网：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fymate.net%2F" target="_blank"><span>https://ymate.net</span></a></span></p>
                                        </div>
                                      
</div>
            