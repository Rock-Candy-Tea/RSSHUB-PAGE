
---
title: '各组织_开源项目对 Log4Shell 漏洞的响应汇总'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9032'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 08:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9032'
---

<div>   
<div class="content">
                                                                                            <p>本文旨在介绍 Log4shell 漏洞，并<strong>收集各组织/开源项目对该漏洞的响应</strong>，以让各大开发者对该漏洞的危害有所了解，避免更多损失。</p> 
<h2>Log4shell 漏洞背景说明</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Apache Log4j2 是一个基于 Java 的日志记录工具。该工具重写了 Log4j 框架，并且引入了大量丰富的特性，被大量用于业务系统开发，用来记录日志信息。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CVE-2021-44228 远程控制漏洞（RCE）影响从 2.0-beta9 到 2.14.1 的  Log4j  版本。受影响的 Log4j 版本包含 Java 命名和目录接口  (JNDI) 功能，可以执行如消息查找替换等操作，攻击者可以通过向易受攻击的系统提交特制的请求，从而完全控制系统，远程执行任意代码，然后进行窃取信息、启动勒索软件或其他恶意活动。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Apache Log4j2 安全补丁更新过程</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>2021 年 12 月 11 日：发布<span> </span><strong>2.15.0</strong><span> </span>版本，对<strong><span> </span></strong>JNDI 查询功能进行限制。但<strong>此版本的修复不完整，导致了第二个 Log4j 漏洞漏洞： CVE-2021-45046</strong>。</li> 
 <li>2021-12-13<strong>：</strong><span> </span>发布<span> </span><strong>2.16.0</strong> 版本，为了解决 CVE-2021-45046 漏洞， Log4j 2.16.0 直接禁用了 JDNI 功能。</li> 
</ul> 
<h2>官方通告</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-44228" target="_blank"><strong>CVE-2021-44228</strong></a><strong>（Log4j2 初始漏洞）</strong></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Apache Log4j 2 2.0-beta9 到 2.12.1 和 2.13.0 到 2.15.0 版本的 JNDI 功能在配置、日志消息和参数中使用，无法防止攻击者控制的 LDAP 和其他 JNDI 相关端点。当启用消息查找替换时，控制日志消息或日志消息参数的攻击者可以执行从 LDAP 服务器加载的任意代码。从 log4j 2.15.0 开始，默认情况下已禁用此行为。从版本 2.16.0 开始，此功能已完全删除。请注意，此漏洞特定于 log4j-core，不会影响 log4net、log4cxx 或其他 Apache 日志服务项目。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-45046" target="_blank"><strong>CVE-2021-45046</strong></a><strong>（Log4j 2.15.0 未完整修复的漏洞）</strong></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Apache Log4j 2.15.0 中针对 CVE-2021-44228 的修复在某些非默认配置中不完整。当日志配置使用非默认模式布局和上下文查找（例如，$$&#123;ctx:loginId&#125;）或线程上下文映射模式（ %X、%mdc 或 %MDC）使用 JNDI 查找模式制作恶意输入数据，从而导致拒绝服务 (DOS) 攻击。默认情况下，Log4j 2.15.0 尽最大努力将 JNDI LDAP 查找限制为 localhost。Log4j 2.16.0 通过删除对消息查找模式的支持和默认禁用 JNDI 功能来修复此问题。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-4104" target="_blank"><strong>CVE-2021-4104</strong></a><strong>（Log4j 1.2 版本问题）</strong></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">当攻击者对 Log4j 配置具有写访问权限时，Log4j 1.2 中的 JMSAppender 容易受到不可信数据的反序列化。攻击者可以提供 TopicBindingName 和 TopicConnectionFactoryBindingName 配置，导致 JMSAppender 以类似于 CVE-2021-44228 的方式执行 JNDI 请求，从而导致远程代码执行。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">注意， JMSAppender 不是 Log4j 的默认配置，因此此漏洞<strong>仅在特别配置为 JMSAppender 时才会影响 Log4j 1.2</strong>。事实上 Apache Log4j 1.2 已于 2015 年 8 月终止生命周期。用户应该升级到Log4j 2，因为它解决了以前版本的许多其他问题。</p> 
<h2>组织/开源项目的响应</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>已修复/更新：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>Metabase</strong><span> </span>：<a href="https://www.oschina.net/news/173590/metabase-0-41-4-released"><span> </span>v0.41.4 发布，解决 log4j2 漏洞问题</a></li> 
 <li><strong>openEuler</strong>：<a href="https://my.oschina.net/openeuler/blog/5359350">欧拉开源社区 Log4j 高危安全漏洞修复完成</a></li> 
 <li><strong>KubeSphere：</strong><a href="https://my.oschina.net/u/4197945/blog/5370085">Apache Log4j 2 远程代码执行最新漏洞的修复方案</a></li> 
 <li><strong>MateCloud<span> </span></strong>：<a href="https://www.oschina.net/news/173821" target="_blank">4.2.8 正式版发布，修复 Log4j2 的安全漏洞</a></li> 
 <li><strong>openLooKeng<span> </span></strong>开源社区：<span> </span><a href="https://www.oschina.net/news/173802/openlookeng-log4j2-fix" target="_blank">Apache Log4j2 高危安全漏洞修复完成</a></li> 
 <li><strong>JPress</strong><span> </span>博客系统：<a href="https://www.oschina.net/news/172952/jpress-4-2-0-released" target="_blank">发布新版，修复 Log4j 漏洞问题</a></li> 
 <li><strong>Netty</strong><span> </span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftower.im%2Fteams%2F779130%2Ftodos%2F11874%2FNetty%25204.1.72.Final%2520%25E5%258F%2591%25E5%25B8%2583%25EF%25BC%258C%25E6%259B%25B4%25E6%2596%25B0%2520Log4j2%2520%25E7%2589%2588%25E6%259C%25AC" target="_blank">4.1.72.Final 发布，更新 Log4j2 版本</a></li> 
 <li><strong>Apache NiFi</strong><span> </span>：<a href="https://www.oschina.net/news/173940/apache-nifi-1-5-1-released">1.5.1 紧急发布，修复 log4j2 相关问题</a></li> 
 <li><strong>Jedis</strong><span> </span>：<a href="https://www.oschina.net/news/173389/jedis-4-0-0-rc2-released" target="_blank">3.7.1、4.0.0-rc2 发布，修复 Log4j 安全问题</a></li> 
 <li><strong>Eurynome Cloud<span> </span></strong>：<span> </span><a href="https://www.oschina.net/news/173440/eurynome-cloud-2-6-2-10-released">v2.6.2.10 发布，修复 Apache Log4j2 安全问题</a></li> 
 <li><strong>Jedis</strong>：<span> </span><a href="https://www.oschina.net/news/173389/jedis-4-0-0-rc2-released" target="_blank">3.7.1、4.0.0-rc2 发布，修复 Log4j 安全问题</a></li> 
 <li><strong>Apache Solr<span> </span></strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsolr.apache.org%2Fsecurity.html%23apache-solr-affected-by-apache-log4j-cve-2021-44228" target="_blank">发布漏洞影响情况和缓解措施</a></li> 
 <li><strong>Minecraft ：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.minecraft.net%2Fen-us%2Farticle%2Fimportant-message--security-vulnerability-java-edition" target="_blank">发布漏洞声明和缓解方案</a></li> 
 <li><strong>Apache Flink</strong><span> </span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fflink.apache.org%2F2021%2F12%2F10%2Flog4j-cve.html" target="_blank">关于 Apache Log4j 零日 (CVE-2021-44228) 的建议</a></li> 
 <li><strong>Apache Druid</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.apache.org%2Fthread%2Fr5pf1vf0758cv4pszcz61pbk34kw02y4" target="_blank">建议所有用户升级到 Druid 0.22.1</a></li> 
 <li><strong>OpenSearch：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensearch.org%2Fblog%2Freleases%2F2021%2F12%2Fupdate-to-1-2-1%2F" target="_blank">重要提示：更新到 OpenSearch 1.2.1</a></li> 
 <li><strong>OpenNMS：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opennms.com%2Fen%2Fblog%2F2021-12-10-opennms-products-affected-by-apache-log4j-vulnerability-cve-2021-44228%2F" target="_blank">受 Apache Log4j 漏洞影响的 OpenNMS 产品 </a></li> 
 <li><strong>IBM Cúram</strong><span> </span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.ibm.com%2Fblogs%2Fpsirt%2Fsecurity-bulletin-vulnerability-in-apache-log4j-may-affect-cram-social-program-management-cve-2019-17571%2F" target="_blank">可能会影响 Cúram Social Program</a></li> 
 <li><strong>IBM WebSphere：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.ibm.com%2Fblogs%2Fpsirt%2Fsecurity-bulletin-vulnerability-in-apache-log4j-affects-websphere-application-server-cve-2021-44228%2F" target="_blank">受影响，已更新</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>不受影响：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>Anolis OS</strong>：<a href="https://my.oschina.net/u/5265430/blog/5361164"><span> </span>不受 Log4j 高危安全漏洞影响</a></li> 
 <li><strong>SUSE<span> </span></strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.suse.com%2Fc%2Fsuse-statement-on-log4j-log4shell-cve-2021-44228-vulnerability%2F" target="_blank">产品均不受影响</a></li> 
 <li><strong>Apache Spark</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FSPARK-37630" target="_blank">不受影响</a></li> 
 <li><strong>Curl / Libcurl<span> </span></strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftwitter.com%2Fbagder%2Fstatus%2F1470879113116360706" target="_blank">不受影响</a></li> 
 <li><strong>Zabbix<span> </span></strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.zabbix.com%2Fzabbix-not-affected-by-the-log4j-exploit%2F17873%2F" target="_blank">不受影响</a></li> 
 <li><strong>DBeaver<span> </span></strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbeaver.io%2F2021%2F12%2F15%2Flog4shell-vulnerability-is-not-dangerous-for-dbeaver-users%2F" target="_blank">Log4j2 漏洞对我们的用户不危险</a></li> 
 <li><strong>VideoLAN：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.videolan.org%2Fnews.html%23news-2021-12-15" target="_blank">核心已移植到 Kotlin ，不用 Log4j</a></li> 
 <li><strong>Cloudflare：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fhow-cloudflare-security-responded-to-log4j2-vulnerability-zh-cn%2F" target="_blank">Cloudflare 如何安全应对 Log4j 2 漏洞</a></li> 
 <li><strong>LastPass：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsupport.logmeininc.com%2Flastpass%2Fhelp%2Flog4j-vulnerability-faq-for-lastpass-universal-proxy" target="_blank">不受影响</a></li> 
 <li><strong>HackerOne</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftwitter.com%2Fjobertabma%2Fstatus%2F1469490881854013444" target="_blank">不受影响，能利用漏洞影响 H1 的人可获得 25000 美金奖励</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>影响待定</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>华为</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.huawei.com%2Fcn%2Fpsirt%2Fsecurity-notices%2Fhuawei-sn-20211210-01-log4j2-cn" target="_blank">启动了调查分析，相关排查还在持续进行</a></li> 
 <li><strong>微软</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmsrc-blog.microsoft.com%2F2021%2F12%2F11%2Fmicrosofts-response-to-cve-2021-44228-apache-log4j2%2F" target="_blank">除了明确涉及 Minecraft，其他的情况仍在调查</a></li> 
 <li><strong>JetBrains：<span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fblog%2F2021%2F12%2F13%2Flog4j-vulnerability-and-jetbrains-products-and-services%2F" target="_blank">YouTrack Standalone、Hub、Upsource 和 Floating 许可证服务器受影响但已修复，其余仍在测试</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>发布漏洞相关工具</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>360CERT</strong>：<a href="https://my.oschina.net/u/4600927/blog/5371617">发布Log4j2恶意荷载批量检测调查工具</a></li> 
 <li><strong>腾讯容器安全</strong>：<a href="https://www.oschina.net/news/173667">发布开源 Log4j2 漏洞缓解工具</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>此列表将持续更新</strong>，俺一个人能力有限，欢迎大家在评论区分享你所了解的公司/组织/开源项目对 Log4shell 漏洞的回应，格式为<span> </span><code><strong>公司/组织/项目名称 | 回应类别（已更新/修复/不受影响等）| 回应链接<span> </span></strong></code><strong>。</strong>此漏洞影响面太广，希望大家一起合作，避免更多组织或个人因此受到损失。</p>
                                        </div>
                                      
</div>
            