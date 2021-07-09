
---
title: 'DDIA 读书笔记-第一章'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba56b34d4d2742bcad59fd5635d17048~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 22:26:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba56b34d4d2742bcad59fd5635d17048~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba56b34d4d2742bcad59fd5635d17048~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">序</h2>
<p>去年年中断断续续读完[《Designing Data-Intensive Applications》这本书， 因为时间原因没做任何笔记。这次重读一遍，好好做笔记，天天向上。</p>
<h2 data-id="heading-1">正文</h2>
<p>本书的第一章主要是描述了系统设计的非功能性需求，作者提炼了三点可靠性，可扩展性，可维护性。本章也是后续内容的一个提纲，后面展开的11章节将会围绕这三点进行描述。</p>
<h4 data-id="heading-2">可靠性</h4>
<p>影响系统可靠性的三点原因即硬件故障，软件故障，人为因素。</p>
<ul>
<li>
<p>提升硬件可靠性</p>
<p>可以通过硬件冗余以及软件容错方式。</p>
</li>
<li>
<p>提升软件可靠性</p>
<p>通过把易犯错的模块和其他模块进行解耦，此外还需要设置快速回滚配置变更以及明确的监控</p>
</li>
<li>
<p>人为因素</p>
<p>架构设计分层考虑，流程设计有快速恢复机制，进行监控，充分测试。同时对人员进行培训</p>
</li>
</ul>
<h4 data-id="heading-3">可扩展性</h4>
<p>书中举了一个推特的例子，两种方法实现推文在发布者和订阅者时间线上的读或写。在扩展性方面需要通过具体的业务要求，考虑性能和资源之间的关系。不同业务要求是不同的比如在线系统一般会追求响应时间短，能快速给用户回复。而Hadoop则追求吞吐量，每秒能处理的记录条数。</p>
<p>在架构设计的初始不需要考虑过高的负载设计，作者提供了一个参考，初始架构设计应对超出预设目标10倍的实际负载。同时服务应该设计成无状态，无状态的服务具备更易实现的扩展性。在明确扩展后，需要考虑垂直扩展（使用更强大的机器）还是水平扩展（负载分到多台小机器上），同时针对调用频繁的模块考虑是否分拆进行扩展。</p>
<h4 data-id="heading-4">可维护性</h4>
<p>易于维护的系统要遵循这三点</p>
<ul>
<li>
<p>可运维性</p>
<p>运维团队对系统运维的要求：监控健康度，快速恢复；追踪问题原因；保持系统监控；保持环境稳定等。那么设计层面要做的事情就包括：提供系统行为的可观测性，支持自动化，服务与机器解耦，提供默认配置和文档，提供恢复流程。</p>
</li>
<li>
<p>简单性</p>
<p>消除复杂性的最好的手段就是抽象</p>
</li>
<li>
<p>可演化性</p>
<p>系统能够适应不断变化的需求</p>
</li>
</ul>
<h2 data-id="heading-5">其他</h2>
<p>DDIA每章的小结是非常值得一看，这里就不复制了。</p></div>  
</div>
            