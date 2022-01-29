
---
title: 'OpenRASP v1.3.7发布，增加JNDI_DNS检测点，修复多个BUG'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4248'
author: 开源中国
comments: false
date: Fri, 28 Jan 2022 18:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4248'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:start">OpenRASP 抛弃了传统防火墙依赖请求特征检测攻击的模式，创造性的使用RASP技术（应用运行时自我保护），直接注入到被保护应用的服务中提供函数级别的实时防护，可以在不更新策略以及不升级被保护应用代码的情况下检测/防护未知漏洞，尤其适合大量使用开源组件的互联网应用以及使用第三方集成商开发的金融类应用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">另外，OpenRASP 提供的IAST解决方案，相比于与传统的DAST方案有着革命性提升。漏洞检测无需动态爬虫或者旁路代理，扫描更全面；结合应用探针准确的识别漏洞类型，通过针对性扫描大幅度提升检测效率；商业版新增的动态污点追踪能力，还可以在不扫描的情况下，预判接口是否存在漏洞。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">OpenRASP 是经过开源社区大规模验证过的产品，目前客户数量已经过百，QQ群人数超过1700人。如果你在使用过程中遇到任何问题，请在官网找到技术讨论群群号，并联系我们处理。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">在这个版本里，我们为JavaAgent增加了JNDI和DNS检测点，并修复了多个BUG。具体改进点如下:</p> 
<h3 style="text-align:start">优化改进</h3> 
<p style="color:#333333; text-align:start">管理后台</p> 
<ul style="margin-left:.85em; margin-right:0"> 
 <li>支持按照主机名、RASP ID或者主机IP搜索报警</li> 
 <li>增加心跳时间索引，解决大规模主机搜索卡顿问题</li> 
 <li>为了提高查询效率，主机离线判定方式改为固定的360s，不再根据心跳配置动态计算</li> 
 <li>支持在后台导出单条报警</li> 
 <li>支持删除过期依赖库数据，感谢@国产大熊猫反馈</li> 
 <li>升级beego到v1.12.3，感谢@大剑士反馈后台编译问题</li> 
 <li>Kafka推送时，将@timestamp从数字改为字符串，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fissues%2F240" target="_blank">感谢 @xizhimen 反馈</a></li> 
 <li>增加漏洞级别字段，aka event_level</li> 
 <li>推送测试报警时，不再使用写死的假报警，而是从ES里搜索最新的报警作为测试数据</li> 
 <li>合入@strawberrybiscuits的补丁，解决IAST死锁问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fpull%2F316" target="_blank">#316</a></li> 
</ul> 
<p style="color:#333333; text-align:start">Java 版本</p> 
<ul style="margin-left:.85em; margin-right:0"> 
 <li>修复当Java不在$PATH时，resin安装会抛出异常的问题，感谢 @叶 反馈</li> 
 <li>修复WebLogic Windows下面自动安装失败的问题</li> 
 <li>修复Weblogic下面无法加载的问题(v1.3.3 引入)</li> 
 <li>修复log.path配置不生效的问题</li> 
 <li>修复快手公司反馈的字节流Hook错误的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fpull%2F293" target="_blank">#293</a></li> 
 <li>修复@killer1278反馈的NIO文件删除hook点类型错误的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fissues%2F280" target="_blank">#280</a></li> 
 <li>修复奇安信公司反馈的依赖库代码问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fissues%2F265" target="_blank">#265</a></li> 
 <li>合入@jekkay的补丁，修复非HTTP攻击报警数据会被覆盖的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fpull%2F264" target="_blank">#264</a></li> 
 <li>合入@strawberrybiscuits的3个补丁，修复Apache Dubbo支持问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fpull%2F313" target="_blank">#313</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fpull%2F314" target="_blank">#314</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fpull%2F315" target="_blank">#315</a></li> 
 <li>合入安天公司的多个补丁，由@xuing提供 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复某些情况下虚拟网卡mac可能为空的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fpull%2F260" target="_blank">#260</a></li> 
   <li>修复Windows JDK9以上版本命令执行hook失效问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fpull%2F271" target="_blank">#271</a></li> 
   <li>修复MySQL 8.X ClientPreparedStatement Hook无效的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fpull%2F277" target="_blank">#277</a></li> 
  </ul> </li> 
 <li>合入快手公司多个补丁，由@Venscor提供 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复配置合法性校验代码中，未能检查key长度的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fpull%2F307" target="_blank">#307</a></li> 
   <li>修复BESResponseBodyHook参数个数错误问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fpull%2F305" target="_blank">#306</a></li> 
  </ul> </li> 
 <li>合入东方通官方提供的补丁 
  <ul style="margin-left:0; margin-right:0"> 
   <li>增加TongWeb 7.X版本支持<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaidu%2Fopenrasp%2Fpull%2F318" target="_blank">#318</a></li> 
  </ul> </li> 
 <li>增加JNDI检测点，并增加一个阻断所有JNDI加载的算法</li> 
 <li>增加DNS检测点，并增加DNSLog域名的检测算法</li> 
 <li>安装程序增加<code>-debuglevel</code>参数，支持安装时修改调试级别</li> 
</ul> 
<p style="color:#333333; text-align:start">PHP 版本</p> 
<ul style="margin-left:.85em; margin-right:0"> 
 <li>增加PHP 7.4支持</li> 
 <li>修复PHP 5.5下面，include检测点可能会崩溃的问题</li> 
</ul> 
<p style="color:#333333; text-align:start">检测插件</p> 
<ul style="margin-left:.85em; margin-right:0"> 
 <li>修复 @月射寒江 发现的Oracle SQL异常无法报警的问题</li> 
 <li>修复 @mattF123 报告的多个XXE绕过问题</li> 
 <li>按照 @Holy 的建议，增加反射写jspx文件的检测</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            