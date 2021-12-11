
---
title: 'Apache Log4j 2.15.0 发布，安全漏洞已得到解决'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8429'
author: 开源中国
comments: false
date: Sat, 11 Dec 2021 08:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8429'
---

<div>   
<div class="content">
                                                                                            <p>Apache Log4j 是一个知名的记录应用程序行为的框架。Log4j 2 是 Log4j 的升级版，与它的前身 Log4j 1.x 相比，提供了显著的改进，并提供了许多其他现代功能。</p> 
<p>Apache Log4j 2.15.0 版本正式发布，安全漏洞 CVE-2021-44228 在 Log4j 2.15.0 中已得到解决。</p> 
<h3>Log4j 2.15.0 的一些新特性包括：</h3> 
<ul> 
 <li>支持仲裁器，它是条件性的，可以使日志配置的部分被包含或排除。</li> 
 <li>支持 Jakarta EE 9，这在功能上等同于 Log4j 的 log4j-web 模块。</li> 
 <li>各种性能改进。</li> 
</ul> 
<h3>需要注意的关键变化：</h3> 
<ul> 
 <li>在这个版本之前，Log4j 会自动解析消息中包含的查找或在 Pattern Layout 中的参数。现在，这个行为不再是默认的，必须通过指定 <code>%msg&#123;lookup&#125;</code> 来启用。</li> 
 <li>JNDI 查询已被限制为默认情况下只支持 java、ldap 和 ldaps 协议。LDAP 也不再支持实现 Referenceable 接口的类，并将可序列化的类限制为默认的 Java 原始类，并要求指定一个允许列表来访问远程 LDAP 服务器。</li> 
 <li>Log4j 2.15.0 的 API 以及许多核心组件与以前的版本保持兼容。</li> 
</ul> 
<p>可以从 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flogging.apache.org%2Flog4j%2F2.x%2Fdownload.html" target="_blank">https://logging.apache.org/log4j/2.x/download.html</a> 下载最新版本。</p>
                                        </div>
                                      
</div>
            