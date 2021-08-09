
---
title: '6种方法教你更好的使用EF Core构建应用程序——第二篇'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5827b8eb504340318df5721c80daa02e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 05:19:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5827b8eb504340318df5721c80daa02e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第8天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【CSDN】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 序言</h1>
<p>大家都知道，ORM（实体关系映射模型）能帮助我们快速构建应用程序，而在使用.net 技术栈工作时，一定会首选Microsoft的数据库访问框架Entity Framework Core（EF Core）来构建应用程序，这里我们就谈谈你们中许多人都熟悉的软件原理和模式。
如果对前三种原则感兴趣的可以发翻看第一篇文章。</p>
<h1 data-id="heading-1">🎏1.仓储</h1>
<p>我们可以通过多种不同的方式访问数据库，并从其他应用程序隐藏EF访问层。在下图中，我显示了四种不同的数据访问模式。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5827b8eb504340318df5721c80daa02e~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
四种类型的数据库访问模式是：</p>
<ul>
<li>仓储+工作单元（Repo + UOW）: 这会将所有EF Core隐藏在为EF提供不同接口的代码后面。您可以用另一个数据库访问框架替换EF，而无需更改调用Repo + UOW的方法。</li>
<li>EF仓储: 这是一个仓储模式，它不会像Repo + UOW模式那样尝试隐藏EF代码。EF仓储假定您作为开发人员知道EF的规则，例如使用跟踪的实体并调用SaveChanges进行更新，因此您将遵守它们。</li>
<li>查询对象:  查询对象封装了数据库查询（即数据库读取）的代码。它们保存了查询的整个代码，或者包含了查询部分的复杂查询。查询对象通常使用IQueryable 输入和输出作为扩展方法构建，以便可以将它们链接在一起以构建更复杂的查询。</li>
<li>直接调用EF。这表示您只是将所需的EF代码放在需要它的方法中的情况。</li>
</ul>
<p>Repo + UOW模式，虽然是很多人推荐的方法，但太重了,不建议使用。直接调用EF,无法分离关注点,一般也不推荐。</p>
<p>因此，在排除了两个极端之后，我建议：</p>
<ul>
<li>查询对象，通常将大型查询分解为一系列查询对象</li>
<li>对于“创建，更新和删除”，我使用DDD风格的访问方法，即，我在实体类中创建了一个方法来更新属性或关系。这样可以隔离EF代码，并使重构或性能优化变得更加容易。</li>
</ul>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title">ChangePubDateService</span> : <span class="hljs-title">IChangePubDateService</span>
&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">readonly</span> EfCoreContext _context;
 
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">ChangePubDateService</span>(<span class="hljs-params">EfCoreContext context</span>)</span>
    &#123;
        _context = context;
    &#125;
 
    <span class="hljs-function"><span class="hljs-keyword">public</span> ChangePubDateDto <span class="hljs-title">GetOriginal</span>(<span class="hljs-params"><span class="hljs-built_in">int</span> id</span>)</span>    
    &#123;
        <span class="hljs-keyword">return</span> _context.Books
            .Select(p => <span class="hljs-keyword">new</span> ChangePubDateDto      
            &#123;                                      
                BookId = p.BookId,                 
                Title = p.Title,                   
                PublishedOn = p.PublishedOn        
            &#125;)                                     
            .Single(k => k.BookId == id);          
    &#125;
 
    <span class="hljs-function"><span class="hljs-keyword">public</span> Book <span class="hljs-title">UpdateBook</span>(<span class="hljs-params">ChangePubDateDto dto</span>)</span>   
    &#123;
        <span class="hljs-keyword">var</span> book = _context.Books.Find(dto.BookId);
        book.PublishedOn = dto.PublishedOn;        
        _context.SaveChanges();                    
        <span class="hljs-keyword">return</span> book;                               
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">🎏2.依赖注入</h1>
<p><strong>.NetCore 完全支持依赖注入（DI），你也应该顺应时代了。</strong></p>
<ul>
<li>将每个数据库访问代码都放入仓储库中。</li>
<li>为每个EF存储库类添加一个接口。</li>
<li>在DI提供程序中针对其接口注册EF存储库类。</li>
<li>然后，您需要将其注入到需要它的前端方法中。</li>
</ul>
<pre><code class="hljs language-csharp copyable" lang="csharp">[<span class="hljs-meta">HttpPost</span>]
[<span class="hljs-meta">ValidateAntiForgeryToken</span>]
<span class="hljs-function"><span class="hljs-keyword">public</span> IActionResult <span class="hljs-title">ChangePubDate</span>(<span class="hljs-params">ChangePubDateDto dto,
   [FromServices]IChangePubDateService service</span>)</span>
   &#123;
      service.UpdateBook(dto);
      <span class="hljs-keyword">return</span> View(<span class="hljs-string">"BookUpdated"</span>,
         <span class="hljs-string">"Successfully changed publication date"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">🎏3.建立业务逻辑</h1>
<p>实际应用的构建是为了提供某种服务，范围从在计算机上保存文件到管理核反应堆。</p>
<p><strong>现实世界中每个不同的问题都有一组规则，通常称为业务规则，或更通用的名称，称为领域规则。</strong></p>
<p>太多人提DDD了,你可以查阅大量的实践文章,这里只讲一点:</p>
<p><strong>您要解决的业务问题必须驱动整个开发。</strong></p>
<p>关于EF Core是否适用于DDD方法存在很多争论，因为业务逻辑代码通常与映射到数据库的EF实体类是分开的。我们开发时的一大原则是：“不要与您的框架作斗争，寻求保持领域驱动设计的方法，并在框架处于敌对状态时放弃细节”。</p>
<ul>
<li>重点考虑业务逻辑，定义好数据库结构，解决领域模型和EF模型的出入。</li>
<li>业务逻辑不应分心，编写业务逻辑本身就很困难，将其与除实体类之外的所有其他应用程序层隔离。当编写业务逻辑时，只需要考虑要解决的业务问题。</li>
<li>业务逻辑应该认为<strong>它正在处理内存数据</strong></li>
<li>将数据库访问代码隔离到一个单独的项目中</li>
<li>业务逻辑不应直接调用EF Core的SaveChanges</li>
</ul>
<h1 data-id="heading-4">🎏4.使您的EF代码正常工作，然后需要时优化它。</h1>
<p><strong>开发的原则是使其工作！</strong></p>
<p>无论哪种方式，这些原则都表明我们应该将性能调优放到最后，并仅在需要时才调整性能。</p>
<p>快速的在EF中开发复杂的数据库访问-至少比使用ADO.NET或Dapper快五倍。不利的一面是EF并不总是会产生性能最好的SQL命令：有时是因为EF没有提供良好的SQL转换，有时是因为我编写的LINQ代码效率不如我想象的那样。</p>
<p><strong>问题是：这有关系吗？</strong></p>
<p>当然优化是需要代价的，后面展示了如何在一系列阶段中改进，每个阶段都变得越来越复杂，并且花费了更多的开发时间：</p>
<ul>
<li>通过重新排列或完善EF代码来改善基本的EF命令吗？</li>
<li>将部分或全部EF代码转换为直接SQL命令，计算所得的列，存储过程等吗？</li>
<li>是否可以更改数据库结构（例如对数据库进行非规范化）以提高搜索性能？</li>
</ul>
<p><strong>规划可能的性能调整</strong></p>
<p>尽管我完全同意过早进行性能调整的想法，但是明智的做法是提前计划您可能的性能调整。</p>
<h1 data-id="heading-5">🎏5.结论</h1>
<p>每一种技术都是越来越难，因为学习任何新技术都需要花费一些时间才能使其变得平滑自然。</p>
<p>已经有许多伟大的软件思想家，还有一些伟大的原理和实践。因此，当下次我们想做的更好时，不妨去看看其他人的想法。</p>
<p>哦哦，祝您编码愉快！</p>
<p>例行小结，理性看待。</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            