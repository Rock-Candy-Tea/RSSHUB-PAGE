
---
title: '【Android篇】老生常谈之Android架构（MVC，MVP，MVVM）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://raw.githubusercontent.com/Yunze-Li/BlogPictures/master/BlogPictures/%E6%8E%98%E9%87%91/MVC.png'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 20:26:27 GMT
thumbnail: 'https://raw.githubusercontent.com/Yunze-Li/BlogPictures/master/BlogPictures/%E6%8E%98%E9%87%91/MVC.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战</a>！」</p>
<p>Android架构算是面试中非常常见的一类问题，最近在整理Android相关的一系列基础知识，所以在此对于常见的三种架构： MVC，MVP，MVVM来进行一个简单的梳理和总结。</p>
<h2 data-id="heading-0">Android架构的优势</h2>
<ul>
<li>灵活的可拓展性</li>
<li>方便进行重构</li>
<li>更容易进行单元测试</li>
<li>较强的可读性</li>
</ul>
<h2 data-id="heading-1">MVC（Model - View - Controller）</h2>
<ul>
<li><strong>Model</strong> 包括了所有<strong>数据模型与数据状态</strong>，同时负责数据的交互与存储；</li>
<li><strong>View</strong> 包括了<strong>呈现给用户的UI以及其他所有和用户的交互</strong>；</li>
<li><strong>Controller</strong> 包括了<strong>业务逻辑以及Model与View之间的交互</strong>，它像是Model与View之间的桥梁，通过Controller可以去操作Model并返回结果显示在View上。</li>
</ul>
<p>MVC架构的架构图如下：</p>
<img src="https://raw.githubusercontent.com/Yunze-Li/BlogPictures/master/BlogPictures/%E6%8E%98%E9%87%91/MVC.png" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-2">优势</h3>
<ul>
<li>Model和View进行了解耦，Model易于进行单元测试</li>
<li>整体架构比较简单，开发周期短，速度快</li>
</ul>
<h3 data-id="heading-3">劣势</h3>
<ul>
<li>对于安卓来说，Controller中<strong>既包含View也包含Controller</strong>，十分难以扩展和修改，也很难进行单元测试；</li>
<li>Model可以直接操作View，所以当View改动时Model和Controller都会需要进行改动。</li>
</ul>
<h2 data-id="heading-4">MVP</h2>
<ul>
<li><strong><code>Model</code></strong> 包括了所有<strong>数据模型与数据状态</strong>，同时负责数据的交互与存储（和MVC相同）；</li>
<li><strong><code>View</code></strong> 包括了<strong>呈现给用户的UI以及其他所有和用户的交互</strong>，但同时它包括了<strong>一组View Interface</strong>可供Presenter进行调用；</li>
<li><strong><code>Presenter</code></strong> 包括了<strong>业务逻辑以及Model与View之间的交互</strong>，除此之外它还<strong>调用了View提供的一组接口</strong>，通过接口与View进行通信从而达成了解耦的目的。</li>
</ul>
<p>MVP架构的架构图如下：</p>
<img src="https://raw.githubusercontent.com/Yunze-Li/BlogPictures/master/BlogPictures/%E6%8E%98%E9%87%91/MVP.png" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-5">优势</h3>
<ul>
<li>通过View Interface<strong>解耦了View和Presenter</strong>, 在MVP架构中Activity/Fragment<strong>只承担VIew的作用</strong>从使得Presenter的改变不影响View，反之亦然；</li>
<li>Model和View同时<strong>也进行了解耦</strong>，View的改变同时也不会影响Model，反之亦然；</li>
<li>Presenter<strong>非常容易进行单元测试</strong>，并且可以灵活地进行重构，改写或扩展；</li>
<li>View只含有纯UI的代码，<strong>易于复用</strong>以及在不同View间切换。</li>
</ul>
<h3 data-id="heading-6">劣势</h3>
<ul>
<li>会引入大量接口，导致<strong>项目代码量激增</strong>，</li>
<li>代码<strong>结构更复杂</strong>，难以管理和阅读</li>
</ul>
<h2 data-id="heading-7">MVVM</h2>
<ul>
<li><strong><code>Model</code></strong> 包括了所有<strong>数据模型与数据状态</strong>，同时负责数据的交互与存储（和MVC， MVP相同）；</li>
<li><strong><code>View</code></strong> 包括了<strong>呈现给用户的UI以及其他所有和用户的交互</strong>，在MVVM中一般使用xml文件来承载UI，这样可以使用DataBinding框架来进行数据绑定；</li>
<li><strong><code>ViewModel</code></strong> 包括了<strong>业务逻辑以及Model与View之间的交互</strong>，和MVP中Presenter的职责基本一致，唯一的区别是<strong>ViewModel通过DataBinging与View进行通信</strong>。使用DataBinding不仅可以大大简化代码量，而且可以感知组件的生命周期，减少内存泄漏。</li>
</ul>
<p>MVVM架构的架构图如下：</p>
<img src="https://raw.githubusercontent.com/Yunze-Li/BlogPictures/master/BlogPictures/%E6%8E%98%E9%87%91/MVVM.png" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-8">优势</h3>
<ul>
<li>View和ViewModel<strong>通过DataBinding框架实现了松耦合</strong>；</li>
<li>ViewModel易于进行单元测试，因为XML文件不需要测试，所以总体的测试覆盖率非常高。</li>
</ul>
<h3 data-id="heading-9">劣势</h3>
<ul>
<li>对于复杂的UI，XML文件的代码量比较大，也比较复杂；</li>
<li>整体的代码量也较大，比较冗余。</li>
</ul>
<h2 data-id="heading-10">比较&总结</h2>
<p>用一个表格来总结一下三种架构的区别：</p>
<img src="https://raw.githubusercontent.com/Yunze-Li/BlogPictures/master/BlogPictures/%E6%8E%98%E9%87%91/Android%E6%9E%B6%E6%9E%84%E5%AF%B9%E6%AF%94.png" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-11">参考链接</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fanmolsehgal.medium.com%2Fcommon-android-architectures-mvc-vs-mvp-vs-mvvm-afd8461e1fee" target="_blank" rel="nofollow noopener noreferrer" title="https://anmolsehgal.medium.com/common-android-architectures-mvc-vs-mvp-vs-mvvm-afd8461e1fee" ref="nofollow noopener noreferrer">Common Android Architecture</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.mindorks.com%2Fmvc-mvp-mvvm-architecture-in-android" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.mindorks.com/mvc-mvp-mvvm-architecture-in-android" ref="nofollow noopener noreferrer">MVC vs MVP vs MVVM Architecture in Android</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fwq6ylg08%2Farticle%2Fdetails%2F105023009" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/wq6ylg08/article/details/105023009" ref="nofollow noopener noreferrer">Android安卓架构MVC、MVP、MVVM之间的区别和联系(图解+案例+源码)</a></p></div>  
</div>
            