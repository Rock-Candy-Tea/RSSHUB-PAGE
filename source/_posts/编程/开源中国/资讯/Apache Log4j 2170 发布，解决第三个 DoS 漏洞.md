
---
title: 'Apache Log4j 2.17.0 发布，解决第三个 DoS 漏洞'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=609'
author: 开源中国
comments: false
date: Sat, 18 Dec 2021 20:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=609'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Apache Log4j 2.17.0 版本已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flogging.apache.org%2Flog4j%2F2.x%2Findex.html" target="_blank">发布</a>，解决了被发现的第三个<span style="background-color:#ffffff; color:#333333">安全漏洞 CVE-2021-45105</span>。</p> 
<p style="margin-left:0; margin-right:0">Apache Log4j2 版本 2.0-alpha1 到 2.16.0 没有防止 self-referential 查找的不受控制的递归。当日志配置使用非默认的 Pattern Layout 与 Context Lookup（例如，$$&#123;ctx:loginId&#125;）时，控制线程上下文映射 (MDC) 输入数据的攻击者可以制作包含递归查找的恶意输入数据，导致 StackOverflowError，从而终止进程。这也称为 DoS 攻击。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">从 2.17.0 版本开始（针对 Java 8），只有配置中的查找字符串才会被递归扩展；在任何其他用法中，仅解析顶层查找，不解析任何嵌套查找。</p> 
<p style="margin-left:0; margin-right:0">在以前的版本中，可以通过确保你的日志记录配置执行以下操作来缓解此问题：</p> 
<ul> 
 <li>在日志记录配置的 PatternLayout 中，用 Thread Context Map 模式（%X、%mdc 或 %MDC）替换 $&#123;ctx:loginId&#125; 或 $$&#123;ctx:loginId&#125; 等 Context Lookups。</li> 
 <li>否则，在配置中删除对 $&#123;ctx:loginId&#125; 或 $&#123;ctx:loginId&#125; 等 Context Lookups 的引用；它们源自应用程序外部的源，如 HTTP headers 或 user input.。</li> 
</ul> 
<p>2.17.0 版本的具体更新内容包括有：</p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#333333">修复字符串替换递归。</span>修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FLOG4J2-3230" target="_blank">LOG4J2-3230</a></li> 
 <li>将 JNDI 仅限于 java 协议。默认情况下，JNDI 将保持禁用状态。将 JNDI 启用属性从“log4j2.enableJndi”重命名为“log4j2.enableJndiLookup”、“log4j2.enableJndiJms”和“log4j2.enableJndiContextSelector”。修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FLOG4J2-3242" target="_blank">LOG4J2-3242</a></li> 
 <li>JNDI 仅限于 java 协议。默认情况下，JNDI 将保持禁用状态。启用属性已重命名为“log4j2.enableJndiJava”。修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FLOG4J2-3242" target="_blank">LOG4J2-3242</a></li> 
 <li>不要将 log4j-api-java9 和 log4j-core-java9 声明为依赖项，因为这会导致 Maven enforcer 插件出现问题。修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FLOG4J2-3241" target="_blank">LOG4J2-3241</a></li> 
 <li>解析属性文件过滤器时的 PropertiesConfiguration.parseAppenderFilters NPE。修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FLOG4J2-3247" target="_blank">LOG4J2-3247</a></li> 
 <li>Syslog Appender 的 Log4j 1.2 bridge 默认为端口 512 而不是 514。修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FLOG4J2-3249" target="_blank">LOG4J2-3249</a></li> 
 <li>Log4j 1.2 bridge API 将 Syslog 协议硬编码为 TCP。修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FLOG4J2-3237" target="_blank">LOG4J2-3237</a></li> 
</ul> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flogging.apache.org%2Flog4j%2F2.x%2Fdownload.html" target="_blank">https://logging.apache.org/log4j/2.x/download.html</a></p>
                                        </div>
                                      
</div>
            