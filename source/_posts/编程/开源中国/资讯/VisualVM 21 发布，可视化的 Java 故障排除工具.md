
---
title: 'VisualVM 2.1 发布，可视化的 Java 故障排除工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2509'
author: 开源中国
comments: false
date: Sat, 24 Jul 2021 07:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2509'
---

<div>   
<div class="content">
                                                                                            <p>VisualVM 是一个集成了命令行 JDK 工具和轻量级剖析功能的可视化工具，设计用于开发和生产时使用。VisualVM 2.1 正式发布，更新内容如下：</p> 
<p><strong>支持的操作系统：</strong></p> 
<ul> 
 <li>微软 Windows；</li> 
 <li>Linux：Intel 平台、ARM HFLT、AArch64；</li> 
 <li>macOS：Intel 平台、苹果 M1；</li> 
</ul> 
<p><strong>所需软件：</strong></p> 
<ul> 
 <li>Oracle JDK 8~17；</li> 
 <li>OpenJDK 8~17；</li> 
 <li>GraalVM 19~21；</li> 
 <li>经测试可与 OpenJDK 17 Early-Access Build 31 配合使用；</li> 
</ul> 
<p><strong>功能和改进：</strong></p> 
<ul> 
 <li>完全支持在 JDK 17 上运行/监控和分析； 
  <ul> 
   <li>GH-299：支持 JDK 17；</li> 
  </ul> </li> 
 <li>JFR 改进：为运行中的 Java 进程启动/转储/停止 JFR： 
  <ul> 
   <li>GH-297: 允许保存 JFR 记录</li> 
  </ul> </li> 
 <li>资源支持的改进： 
  <ul> 
   <li>GH-327: 在核心工具中提供转到源码支持；</li> 
   <li>GH-302: 让定义 JDK 根目录更容易；</li> 
  </ul> </li> 
 <li>新的命令行选项 <code>--threaddump</code>, <code>--heapdump</code>, <code>--start-cpu-sampler</code>, <code>--start-memory-sampler</code>, <code>--snapshot-sampler</code>, <code>--stop-sampler</code>, <code>--start-jfr</code>, <code>--dump-jfr</code>, <code>--stop-jfr</code>, <code>--window to front</code>:</li> 
 <li>由 NetBeans Platform 12.4 提供支持： 
  <ul> 
   <li>GH-316: 将 NetBeans Platform 更新至 12.4</li> 
  </ul> </li> 
</ul> 
<p><strong>错误修复：</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fvisualvm%2Fissues%2F289" target="_blank">GH-289</a>: IOException：不能连接到当前的虚拟机；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fvisualvm%2Fissues%2F291" target="_blank">GH-291</a>: 尝试避免 JMX 连接，直到用户打开应用程序；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fvisualvm%2Fissues%2F292" target="_blank">GH-292</a>: 插件|设置|代理设置按钮不工作</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fvisualvm%2Fissues%2F300" target="_blank">GH-300</a>: 完整的类名称在 JFR 中以粗体显示</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fvisualvm%2Fissues%2F307" target="_blank">GH-307</a>: 无休止的线程转储计算</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fvisualvm%2Fissues%2F308" target="_blank">GH-308</a>: 线程转储计算缓慢</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fvisualvm%2Fissues%2F310" target="_blank">GH-310</a>: VisualVM 无法分析 TruffleRuby</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fvisualvm%2Fissues%2F311" target="_blank">GH-311</a>: macOS 上的日志文件/选项位置说明不清楚</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fvisualvm%2Fissues%2F314" target="_blank">GH-314</a>: 特定 OQL 查询的第二次调用不显示任何内容；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvisualvm.github.io%2Frelnotes.html" target="_blank">https://visualvm.github.io/relnotes.html</a></p>
                                        </div>
                                      
</div>
            