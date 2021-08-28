
---
title: 'JavaScript 迭代器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5321'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 06:39:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=5321'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第27天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<h3 data-id="heading-1">吃饱饭才有力气写代码~</h3>
<p>今天学习一下JavaScript的迭代器相关知识。</p>
<h3 data-id="heading-2">理解迭代</h3>
<p>首先先来理解一下迭代，在JavaScript中最简单的迭代：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>;i <= <span class="hljs-number">10</span>;i++)&#123;
    <span class="hljs-built_in">console</span>.log(i);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>循环是迭代机制的基础，它可以指定迭代的次数，以及每次迭代要执行的操作。<br>
迭代会在一个有序集合上进行，所谓有序可以理解为集合中的所有项都可以按照既定的顺序被遍历到，特别是开始项和结束项有明确的定义。比如数组：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-string">'aaa'</span>,<span class="hljs-string">'bbb'</span>,<span class="hljs-string">'ccc'</span>];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;index < arr.length; ++index)&#123;
    <span class="hljs-built_in">console</span>.log(arr[index]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为数组有已知的长度，且数组每一项都可以通过索引获得，所以整个数组可以通过递增索引来遍历。但是这种循环来执行例程并不理想。原因如下：</p>
<ul>
<li>迭代之前需要事先知道如何使用数据结构</li>
<li>遍历顺序并不是数据结构固有的</li>
</ul>
<br>
在早期的版本中，执行迭代必须使用循环或者其它辅助结构。随着代码量的增加，代码会越来越混乱，后来的解决方案就是**迭代器模式**。
<h3 data-id="heading-3">迭代器模式</h3>
<p>迭代器模式描述了一个方案，即可以把有些结构称为可迭代对象，因为它们实现了正式的Iterable，而且可以通过迭代器Iterator消费。
<br>
基本上可以把可迭代对象理解成数组或集合这样的集合类型的对象。它们的元素都是有限的，而且都具有无歧义的遍历顺序。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//数组的元素是有限的</span>
<span class="hljs-comment">//递增索引可以按序访问每个元素</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>];
<span class="hljs-comment">//集合的元素是有限的</span>
<span class="hljs-comment">//可以按插入顺序访问每个元素</span>
<span class="hljs-keyword">let</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>().add(<span class="hljs-number">3</span>).add(<span class="hljs-number">2</span>).add(<span class="hljs-number">1</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过，可迭代对象不一定是集合对象，也可以是仅仅具有类似数组行为的其他数据结构。比如最开始的那个计数循环，在那个循环中生成的值是暂时的，但循环本身是在执行迭代，计数循环和数组都具有可迭代对象的行为。
<br>
突然fa</p></div>  
</div>
            