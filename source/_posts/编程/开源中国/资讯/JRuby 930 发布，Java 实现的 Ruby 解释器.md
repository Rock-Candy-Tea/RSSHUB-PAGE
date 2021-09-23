
---
title: 'JRuby 9.3.0 发布，Java 实现的 Ruby 解释器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1331'
author: 开源中国
comments: false
date: Thu, 23 Sep 2021 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1331'
---

<div>   
<div class="content">
                                                                                            <p>JRuby 是一个采用 Java 实现的 Ruby 解释器，由 JRuby 团队开发。JRuby 与 Java 紧密结合，允许将解释器嵌入任何 Java 应用程序，在 Java 和 Ruby 代码之间进行完全的双向访问（类似于 Python 语言的 Jython）。</p> 
<p>JRuby 9.3.x 与 Ruby 2.6.x 兼容，并与 C Ruby 保持同步。</p> 
<h3>兼容性</h3> 
<ul> 
 <li>Ruby 语言的兼容性已经更新，以匹配 Ruby 2.6.8 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F5576" target="_blank">#5576</a>)</li> 
 <li>require/load/autoload 子系统已被重写，以更好地匹配 Ruby 行为。这改善了对 Zeitwerk 加载器的支持，并修正了许多长期存在的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F2794" target="_blank">#2794</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F3656" target="_blank">#3656</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F5403" target="_blank">#5403</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F5466" target="_blank">#5466</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F5590" target="_blank">#5590</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F5618" target="_blank">#5618</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F5638" target="_blank">#5638</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F5717" target="_blank">#5717</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fpull%2F5763" target="_blank">#5763</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fpull%2F5764" target="_blank">#5764</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F6347" target="_blank">#6347</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F6445" target="_blank">#6445</a>)</li> 
 <li>改进了处理复杂方法和常量查找的逻辑，例如在预置、细化或超级调用的情况下。这些形式的大多数已知问题已经被修复 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F596" target="_blank">596</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F2155" target="_blank">#2155</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F4678" target="_blank">#4678</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F6271" target="_blank">#6271</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fpull%2F6712" target="_blank">#6712</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fpull%2F6777" target="_blank">#6777</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fpull%2F6778" target="_blank">#6778</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fpull%2F6785" target="_blank">#6785</a>)</li> 
</ul> 
<h3>标准库</h3> 
<ul> 
 <li>标准库已经更新，以匹配 Ruby 2.6.8。一些库现在使用了官方的 gems，允许它们独立于 JRuby 进行升级 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F4875" target="_blank">#4875</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fpull%2F6150" target="_blank">#6150</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F6797" target="_blank">#6797</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F6796" target="_blank">#6796</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F6795" target="_blank">#6795</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F6794" target="_blank">#6794</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F6533" target="_blank">#6533</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F6802" target="_blank">#6802</a>)</li> 
</ul> 
<h3>Java 集成</h3> 
<ul> 
 <li>JRuby 支持 8 到 17 版本的 Java，并且应该能与任何支持的 OpenJDK 构建良好地工作。未来的 JRuby 版本可能会放弃对 Java 8 到 10 的支持，所以鼓励用户尽快升级旧的应用程序。</li> 
 <li>用于从 Ruby 扩展 Java 类的 Java 集成逻辑已被重写，以更好地支持 Java 构造函数，并从我们的 Java 集成库的其他部分重用更多逻辑 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F449" target="_blank">#449</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F2369" target="_blank">#2369</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F4165" target="_blank">#4165</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fissues%2F5270" target="_blank">#5270</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fpull%2F6422" target="_blank">#6422</a>)</li> 
 <li>JRuby 现在为 Maven Central 提供了一个新的 "jruby-base" jar 构件。它提供了一个基本的 JRuby jar 文件，其中不包含任何依赖项或标准库。我们将来可能会弃用并移除 "jruby-core" (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjruby%2Fjruby%2Fpull%2F6233" target="_blank">#6233</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jruby.org%2F2021%2F09%2F22%2Fjruby-9-3-0-0.html" target="_blank">https://www.jruby.org/2021/09/22/jruby-9-3-0-0.html</a></p>
                                        </div>
                                      
</div>
            