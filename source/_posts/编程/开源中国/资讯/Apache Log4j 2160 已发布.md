
---
title: 'Apache Log4j 2.16.0 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9300'
author: 开源中国
comments: false
date: Tue, 14 Dec 2021 10:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9300'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>Apache Log4j 2.16.0 现已可用。 </span><span> </span><span>Apache Log4j 2 团队宣布 Log4j 2.16.0 发布！</span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>你可以从以下位置下载工件</span><span> </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flogging.apache.org%2Flog4j%2F2.x%2Fdownload.html" target="_blank">https://logging.apache.org/log4j/2.x/download.html</a></span><span>。</span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>此版本包含一项更改，如下所述。</span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>由于 SLF4J 绑定中的兼容性中断，Log4j 现在发布两个版本的 SLF4J 到 Log4j 的适配器。</span><span><code>log4j-slf4j-impl</code></span><span>对应 </span><span><code>SLF4J 1.7.x</code></span><span> 及更早版本； </span><span><code>log4j-slf4j18-impl</code></span><span>对应</span><span><code>SLF4J 1.8.x</code></span><span> 及更高版本一起使用。SLF4J-2.0.0 alpha 版本目前还不完全支持。 详细说明请查看：</span><span> </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FLOG4J2-2975" target="_blank">https://issues.apache.org/jira/browse/LOG4J2-2975</a></span><span> </span><span> </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.qos.ch%2Fbrowse%2FSLF4J-511" target="_blank">https://jira.qos.ch/browse/SLF4J-511</a></span><span>。</span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>一些更改</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>删除了消息Lookups。目的是采取强化措施以防止 CVE-2021-44228，此举措不是修复 CVE-2021-44228所必须的。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>虽然版本 2.15.0 删除了处理Lookups和利用JNDI从日志消息和地址访问的问题，Log4j团队认为默认启用 JNDI 会引入未知的风险。从版本 2.16.0 开始，JNDI 功能是默认情况下禁用，可以通过 </span><span><code>log4j2.enableJndi</code></span><span>重新启用系统属性。在不受保护的上下文中使用 JNDI 是一个很大的问题</span><span> </span><span>安全风险，应该在这个库和</span><span> </span><span>所有其他使用 JNDI 的 Java 库。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>在 2.15.0 版本之前，Log4j 会在模式布局（Pattern Layout）中包含的消息或参数中自动解析 Lookups。这行为不再是默认值，必须通过指定启用</span><span><code>%msg&#123;lookup&#125;</code></span><span>。</span></p> </li> 
</ul> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span><strong><span>强烈推荐升级2.16.0。</span></strong></span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>修正错误</span></h3> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>LOG4J2-3208：默认禁用 JNDI。需要 </span><span><code>log4j2.enableJndi</code></span><span>设置为 </span><span><code>true</code></span><span> 以允许 JNDI。</span><span> </span><span>LOG4J2-3211：完全删除对消息查找的支持。</span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>Apache Log4j 2.16.0 至少需要 Java 8 才能构建和运行。Log4j 2.12.1 是最后一个支持 Java 7 的版本。Java 7 不是Log4j 团队的长期支持版本。</span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>有关 Apache Log4j 2 的完整信息，包括有关如何提交错误报告、补丁或改进建议，请参阅 Apache Apache Log4j 2 网站：</span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flogging.apache.org%2Flog4j%2F2.x%2F" target="_blank">https://logging.apache.org/log4j/2.x/</a></span></p>
                                        </div>
                                      
</div>
            