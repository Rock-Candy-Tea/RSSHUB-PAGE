
---
title: 'MVC、MVP和MVVM的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37807d54c09d42169652a712b80b57c2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 07:57:45 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37807d54c09d42169652a712b80b57c2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>这是我参与更文挑战的第1天，活动详情查看<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战 </a></p>
<p>在web1.0时代时，那个时候程序猿还没有前后端之分，程序员开发的时候，都是要前后端一起写的，前后端代码都是杂揉在一起，如图下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37807d54c09d42169652a712b80b57c2~tplv-k3u1fbpfcp-watermark.image" alt="web1.0.jpg" loading="lazy" referrerpolicy="no-referrer">
这种开发模式的话，开发的时候因为不需要和其他人员沟通协作，前后端代码都是写在一起，优缺点如下：</p>
<p><strong>优点</strong>：简单快捷</p>
<p><strong>缺点</strong>：代码难以维护</p>
<p>为了让开发更加便捷，代码更易于维护，前后端职责更加清晰。便衍生出MVC开发模式和框架，前端展示以模板的形式出现。我当时实习的时候，所在的公司开发模式就是使用这种开发模式，开发模式如图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/193ba2d00c564146a48a422f4ecc04ae~tplv-k3u1fbpfcp-watermark.image" alt="后端MVC.jpg" loading="lazy" referrerpolicy="no-referrer">
使用这种分层架构，前后端职责清晰，代码也易于维护。但是这里的MVC仅限于后端，前后端形成了一定的分离，前端只完成了后端开发中的view层</p>
<p><strong>缺点</strong>：</p>
<ol>
<li>前端页面开发效率不高</li>
<li>前后端职责不够清晰　</li>
</ol>
<p>自从Gmail的出现，ajax技术开始风靡全球。有了ajax之后，前后端的职责就更加清晰了。因为前端可以通过ajax与后端进行数据交互，因此，整体的架构图也就变化成了下面这幅图。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b860d956caa4d57ad8cb2a8740229f7~tplv-k3u1fbpfcp-watermark.image" alt="Ajax-mvc.jpg" loading="lazy" referrerpolicy="no-referrer">
通过ajax与后台服务器进行数据交换，前端开发人员，只需要开发页面这部分内容，数据可由后台进行提供。而且ajax可以在不重载整个页面的情况下对网页的某些部分进行更新，减少了服务端负载和流量消耗，用户体验也更佳。这时，才开始有专职的前端工程师，同时前端的类库也慢慢的开始发展，例如当时最著名的jquery。</p>
<p><strong>缺点</strong>：缺乏可行的开发模式承载更复杂的业务需求，页面内容都杂糅在一起，一旦应用规模增大，就会导致项目难以维护。因此，前端的MVC框架也就随之而来了</p>
<h3 data-id="heading-1">前后端分离后的架构演变--MVC、MVP、MVVM</h3>
<h4 data-id="heading-2">MVC</h4>
<p>前端的MVC与后端类似，具备着view、controller和Model。</p>
<ul>
<li>Model：负责保存应用数据，与后端数据进行同步</li>
<li>Controller：负责业务逻辑，根据用户行为对model数据进行修改</li>
<li>View：负责视图展示，将model中的数据可视化出来</li>
</ul>
<p>三者形成了如图所示的模型：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/576ed6246fec45f0a4574a4dd4976c8c~tplv-k3u1fbpfcp-watermark.image" alt="理想型MVC.jpg" loading="lazy" referrerpolicy="no-referrer">
实际开发中，我们往往会看到另外一种模式：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27e7073bd25244a6baa5e09426200e0d~tplv-k3u1fbpfcp-watermark.image" alt="实际MVC.jpg" loading="lazy" referrerpolicy="no-referrer">
这种模式在开发中更加的灵活，backbone.js就是这种模式</p>
<p>但是，这种灵活可能导致严重的问题：</p>
<p>数据流混乱。如下图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1f86fe07f274a1eb12c1fb686c74427~tplv-k3u1fbpfcp-watermark.image" alt="数据混乱的MVC.jpg" loading="lazy" referrerpolicy="no-referrer">
view比较庞大，而Controller比较单薄：由于很多的开发者都会在view中写一些逻辑代码，逐渐的就导致view中的内容越来越庞大，而controller变得越来越单薄</p>
<p>既然有缺陷，就会有变革，前端的变化中，似乎跳过了MVP这种模式，是因为Angular早早的将MVVM框架带入了前端。MVP模式虽然前端开发中并不常见，但是在安卓等原生开发中，还是会考虑它</p>
<h4 data-id="heading-3">MVP</h4>
<p>MVP和MVC很接近，P指的是Presenter，presenter可以理解为一个中间人，它负责着View和Model之间的数据流动 ，防止View和Model之间直接交流。我们可以看一下图示</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5d23819893142de8eb13579c8a899ee~tplv-k3u1fbpfcp-watermark.image" alt="MVP.jpg" loading="lazy" referrerpolicy="no-referrer">
我们通过图可以看到，Presenter负责和Model进行双向交互，这种交互方式，相对于MVC来说，少了一些灵活，View变成了被动视图，并且本身变得很小，虽然它分了view和model，但是应用逐渐变大之后，导致Presenter的体积增大，难以维护，要解决这个问题。或许可以从MVVM的思想中找到答案</p>
<h4 data-id="heading-4">MVVM</h4>
<p>什么是MVVM？MVVM可以分解为Model-View—ViewModel，ViewModel可以理解为在Presenter基础上的进阶版本，如图所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3faba6af91c4411199c738f478330af9~tplv-k3u1fbpfcp-watermark.image" alt="MVVM.jpg" loading="lazy" referrerpolicy="no-referrer">
ViewModel通过实现一套数据响应式机制自动响应Model中数据变化；</p>
<p>同时ViewModel会实现一套更新策略自动将数据变化转换为视图更新</p>
<p>通过事件监听响应View中交互修改Model中数据</p>
<p>这样在ViewModel中就娴熟了大量DOM操作代码</p>
<p>MVVM在保持VIEW和Model松耦合的同时，还减少了维护他们关系的代码，使用户专注于业务逻辑，兼顾开发效率和可维护性</p>
<h4 data-id="heading-5">总结</h4>
<ul>
<li>这三者都是框架模式，他们设计的目标都是为了解决Model和View的耦合问题。</li>
<li>MVC模式出现较早，主要应用在后端，如Spring MVC、Asp.NET MVC等，在前端领域的早期也有应用，如Backbone.js。它的优点是分层清晰，缺点是数据流混乱，灵活性带来的维护性问题</li>
<li>MVP模式是在MVC的进化形式，Presenter作为中间层负责MV通信，解决了两者耦合问题，但P层过于臃肿会导致维护问题</li>
<li>MVVM模式是目前前端的主流模式，在前端领域有着广泛应用，它不仅解决MV耦合问题，还同时解决了维护两者映射关系的大量繁杂代码和DOM操作代码，在提高开发效率、可读性同时还保持了优越的性能表现</li>
</ul></div>  
</div>
            