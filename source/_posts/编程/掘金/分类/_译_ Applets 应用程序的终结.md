
---
title: '_译_ Applets 应用程序的终结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1915'
author: 掘金
comments: false
date: Sat, 10 Apr 2021 04:00:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=1915'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://www.infoq.com/news/2021/03/end-of-applets" target="_blank" rel="nofollow noopener noreferrer">The End of Applets</a></li>
<li>原文作者：<a href="https://www.infoq.com/profile/Erik-Costlow/" target="_blank" rel="nofollow noopener noreferrer">Erik-Costlow</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/The-End-of-Applets.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/5Reasons" target="_blank" rel="nofollow noopener noreferrer">5Reasons</a></li>
<li>校对者：<a href="https://github.com/PassionPenguin" target="_blank" rel="nofollow noopener noreferrer">PassionPenguin</a>、<a href="https://github.com/wumrwds" target="_blank" rel="nofollow noopener noreferrer">wumrwds</a></li>
</ul>
</blockquote>
<h1 data-id="heading-0">Applets 应用程序的终结</h1>
<p>Oracle 在 <a href="https://openjdk.java.net/jeps/398" target="_blank" rel="nofollow noopener noreferrer">JEP-398</a> 中将 Applet 相关的 API 标记为 “已弃用”。在进入 21 世纪后，所有的主流浏览器都不再支持 Java Applets 所依赖的 NPAPI 插件，在这样的背景下，Oracle 多年来一直都在发布即将弃用 Applets 的公告（<a href="https://openjdk.java.net/jeps/289" target="_blank" rel="nofollow noopener noreferrer">JEP-289</a>）。</p>
<p>在若干年前浏览器的功能较弱、程序开发相关标准尚未完善的时候，Java Applets 就较早地做到了支持富互联网应用。支持 Java Applets 的能力是由 <a href="https://en.wikipedia.org/wiki/NPAPI" target="_blank" rel="nofollow noopener noreferrer">网景插件应用程序接口</a>（简称 NPAPI）提供的，它能够在浏览器的沙盒环境下运行 Java 应用。NPAPI 第一次出现在浏览器中是在 1995 年，比 <a href="https://www-archive.mozilla.org/press/mozilla-2005-08-03.html" target="_blank" rel="nofollow noopener noreferrer">Mozilla 基金会的成立</a> (2005) 和 <a href="https://en.wikipedia.org/wiki/Google_Chrome#Public_release" target="_blank" rel="nofollow noopener noreferrer">Chrome 的第一个版本</a> (2008) 都要早得多。</p>
<p>在现代浏览器标准出现之前，这些 Applets 应用层序通常被用于文件传输、用户鉴权以及处理各种 Javascript 在当时无法处理的情况。各大浏览器在 2015 年开始 <a href="https://blog.mozilla.org/futurereleases/2015/10/08/npapi-plugins-in-firefox/" target="_blank" rel="nofollow noopener noreferrer">移除对 NPAPI 的支持</a>，以此简化浏览器的维护工作，并和 Oracle 发布的关于 Applets 的一份白皮书文件：<a href="https://www.oracle.com/technetwork/java/javase/migratingfromapplets-2872444.pdf" target="_blank" rel="nofollow noopener noreferrer">从 Java Applet 迁移到无插件的 Java 技术</a> 保持同步。</p>
<p>在 2015 年 API 的变化之前， Java Applet 应用的安全性就一直广为讨论，但许多组织能够通过使用管理工具 (例如：<a href="https://blogs.oracle.com/java-platform-group/introducing-deployment-rule-sets" target="_blank" rel="nofollow noopener noreferrer">部署规则集</a>) 或者在一个孤立的 Citrix 环境中将 Java 和浏览器的兼容性锁定在一起来保护客户端。</p>
<p>尽管在之前的 Java 版本中就已经为 Java Applets 打上了已被弃用的标签，但相关的 API 仍被暂时保留了下来，以防一些没有实际使用相关 API 却仍旧调用了相关 API 的应用程序遭遇编译或运行错误。事实上，在 Java 和 OpenJDK 平台近 20 年的标准文档中，Applet 这一特性都被标注为“已弃用”和“将被移除”。</p>
<p>InfoQ 与 <a href="https://twitter.com/DrDeprecator" target="_blank" rel="nofollow noopener noreferrer">Dr. Deprecator</a> 以及 OpenJDK 的贡献者 Stuart Marks 进行了交流，探访 OpenJDK 项目是怎么界定、使用 @Deprecated 标签的，并了解都有哪些 API 已经被弃用。</p>
<p>Java 9 增强了 <a href="https://docs.oracle.com/en/java/javase/15/docs/api/java.base/java/lang/Deprecated.html" target="_blank" rel="nofollow noopener noreferrer">@Deprecated 弃用注解</a>，为其新增了 forRemoval 属性。随着 JEP-398 提出的改变，Applet API 将被设置为 <code>forRemoval = true</code>，在这些 API 被真正移除前，forRemoval 属性将让编译器和相关工具为开发者弹出更严重的警告。通过渐进式地设置多个警告可以有效的避免开发社区内的代码混乱，这秉承了语言架构师 Brian Goetz 在 2015 年的演讲 “<a href="https://www.youtube.com/watch?v=ibYrHlwCKB4" target="_blank" rel="nofollow noopener noreferrer">谨慎演进，避免破坏</a>” 中所传达的思想。</p>
<p>已被从核心的 Java APIs 移除的其他项目包括：</p>
<ul>
<li>CORBA，<a href="https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture" target="_blank" rel="nofollow noopener noreferrer">一个互操作式框架</a>，由对象管理组织 (OMG) 于 1991 年发布，其最新版本在 2012 年发布</li>
<li>JAXB，<a href="https://eclipse-ee4j.github.io/jaxb-ri/" target="_blank" rel="nofollow noopener noreferrer">一个 XML 相关 API 的集合</a>，现在被置于 Jakarta EE 库中进行维护</li>
<li><a href="https://www.infoq.com/news/2018/06/deprecate-nashorn/" target="_blank" rel="nofollow noopener noreferrer">Nashorn</a>，一个 JavaScript 执行引擎</li>
<li>一些小变化，例如 <a href="https://docs.oracle.com/javase/7/docs/technotes/guides/concurrency/threadPrimitiveDeprecation.html" target="_blank" rel="nofollow noopener noreferrer">Thread.stop(Throwable)</a>, <a href="https://bugs.openjdk.java.net/browse/JDK-8198250" target="_blank" rel="nofollow noopener noreferrer">System.runFinalizersOnExit</a>, 以及 <a href="https://bugs.openjdk.java.net/browse/JDK-8217412" target="_blank" rel="nofollow noopener noreferrer">RMI Stub Compiler</a></li>
</ul>
<p>如果想知道上述改变是否会影响到他们的应用程序或者依赖，用户们可以尝试在代码和依赖中使用这两个工具：</p>
<ul>
<li><a href="https://docs.oracle.com/javase/9/tools/jdeps.htm#JSWOR690" target="_blank" rel="nofollow noopener noreferrer">jdeps</a>，这是一个能分析是否使用了有不兼容风险的 API 的工具。它可以帮助开发团队排查项目中是否使用了已经发生改变的、不规范的 API</li>
<li><a href="https://docs.oracle.com/en/java/javase/15/docs/specs/man/jdeprscan.html" target="_blank" rel="nofollow noopener noreferrer">jdeprscan</a>，这是一个能够分析 @Deprecated 弃用注解的工具，它会分析如果不对已弃用的 API 进行调整的话，项目会面临怎样的风险</li>
</ul>
<p>当被问及 Applet 的弃用是否可以应用于序列化、Applet 安全管理器和一些其他方面时，相关提案者简单地回答道:“<a href="https://twitter.com/DrDeprecator/status/1368359481684336640" target="_blank" rel="nofollow noopener noreferrer">等着瞧吧（Hold my beer）</a>”，这暗示着相关的更改可能已经正在进行了。</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            