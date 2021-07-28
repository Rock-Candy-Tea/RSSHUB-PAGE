
---
title: 'Jenkins 2.304 发布，Java 编写的持续集成工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9618'
author: 开源中国
comments: false
date: Wed, 28 Jul 2021 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9618'
---

<div>   
<div class="content">
                                                                                            <p>Jenkins 是一款由 Java 编写的开源的持续集成工具。Jenkins 提供了软件开发的持续集成服务。它运行在 Servlet 容器中（例如 Apache Tomcat）。它支持软件配置管理（SCM）工具（包括 AccuRev SCM、CVS、Subversion、Git、Perforce、Clearcase 和 RTC），可以执行基于 Apache Ant 和 Apache Maven 的项目，以及任意的 Shell 脚本和 Windows 批处理命令。Jenkins 是在 MIT 许可证下发布的自由软件。</p> 
<p>Jenkins 2.304 正式发布，本次更新内容如下：</p> 
<ul> 
 <li>当条目的路径前缀与目标位置相同时，修复在极端情况下解压缩档案的问题</li> 
 <li>避免在无法发送使用统计数据时污染日志；</li> 
 <li>将 matrix-auth 从 2.6.7 提升到 2.6.8</li> 
 <li>通过 <code>hudson.Util.useNativeChmodAndMode</code> 系统属性，移除对本地 JNR（Java Native Runtime） <code>chmod(2)</code> 和 <code>stat(2)</code> 实现的支持；</li> 
 <li>开发者：允许 XmlFile 的消费者禁用 <code>fsync(2)</code>；</li> 
 <li>内部：术语清理以修复构建时间趋势的分布式构建，只在控制器有定义代理时显示代理栏；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jenkins.io%2Fchangelog%2F%2F%23v2.304" target="_blank">https://www.jenkins.io/changelog//#v2.304</a></p>
                                        </div>
                                      
</div>
            