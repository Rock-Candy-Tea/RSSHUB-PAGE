
---
title: '为什么服务端渲染有利于SEO'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79a60a2954134c1793bb27122ededf29~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 30 Mar 2021 01:17:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79a60a2954134c1793bb27122ededf29~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote class="multiquote-1">
<p>为实现中华民族伟大复兴而读书。</p>
</blockquote>
<h3 data-id="heading-0"><span></span><span class="prefix"></span><span class="content">前情回顾</span><span class="suffix"></span></h3>
<p>上篇文章聊了的一个<code>基于Vue的服务端渲染的</code>问题，只是粗略的介绍了一下它的优缺点，其中涉及到一个<code>SEO</code>,<code>SEO</code>的全称是<code>Search Engine Optimise</code> 即，搜索引擎优化。</p>
<p>谈到<code>seo</code>这个问题，可能需要了解一下搜索引擎的原理，涉及比较深的算法问题我也说不清楚，只是简单的说一下自己对这个问题的理解吧。</p>
<h3 data-id="heading-1"><span></span><span class="prefix"></span><span class="content">引擎工作原理</span><span class="suffix"></span></h3>
<p>(官方答案)搜索引擎的工作原理是从互联网上抓取网页，建立索引数据库，在索引数据库中搜索排序。它的整个工作过程大体分为信息采集、信息分析、信息查询和用户接口四部分。信息采集是网络机器人扫描一定IP地址范围内的网站，通过链接遍历Web空间，来进行采集网页资料，为保证采集的资料最新，网络机器人还会回访已抓取过的网页；信息分析是通过分析程序，从采集的信息中提取索引项，用索引项表示文档并生成文档库的索引表，从而建立索引数据库；信息查询是指用户以关键词查找信息时，搜索引擎会根据用户的查询条件在索引库中快速检索文档，然后对检出的文档与查询条件的相关度进行评价，最后根据相关度对检索结果进行排序并输出。</p>
<p>如果用自己的图解释这个过的话。
<img alt="引擎工作原理" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79a60a2954134c1793bb27122ededf29~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>但是假如说问: 这个信息分析，建立索引是怎样的一个过程，这个我也不清楚，有的文献找不到，找到了也看不了。。。</p>
<h3 data-id="heading-2"><span></span><span class="prefix"></span><span class="content">为什么服务端渲染有利于SEO</span><span class="suffix"></span></h3>
<p>首先我们需要明白一点，<code>SEO</code>并不是一项技术，而是一种针对搜索引擎的策略，它的目的的让搜索引擎的爬虫，更快，更准确的爬取到我们开发的网站。</p>
<p>如果我们有人写过爬虫的话(我们暂且认为搜索引擎的爬虫跟我们平时写的是一个东西)，那么会了解，我们的爬虫爬取的其实是网页里的标签内容，通过获取这些内容进行分析。假设我们的网站都是采用前后端分离进行开发，界面都需要用js去请求接口，等到接口返回之后才展示真个界面。那么我们的爬虫也需根本获取不到我们想要的内容。</p>
<p>而通过服务渲染，服务端将整个界面的数据填充完整之后，直接返回这个界面。第一，少了客户端请求的过程。第二，返回的直接就是整个界面。必然使爬虫能够更快，更准确的爬取到它想要的信息。</p>
<p>所以有这么一个结论<code>服务端渲染有利于SEO</code>。</p>
<h3 data-id="heading-3"><span></span><span class="prefix"></span><span class="content">最后说两句</span><span class="suffix"></span></h3>
<ol>
<li>动一动您发财的小手，<strong><code>「点个赞吧」</code></strong></li><li>动一动您发财的小手，<strong><code>「点个在看」</code></strong></li><li>都看到这里了，不妨  <strong><code>「加个关注」</code></strong></li><li>不妨  <strong><code>「转发一下」</code></strong>，好东西要记得分享</li></ol>
<figure><img alt="javascript基础知识总结" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1f07f79f5384a28b9b0fa8b2aab9b7c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><figcaption>javascript基础知识总结</figcaption></figure>
</div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            