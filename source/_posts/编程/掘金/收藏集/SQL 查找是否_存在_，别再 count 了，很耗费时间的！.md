
---
title: 'SQL 查找是否_存在_，别再 count 了，很耗费时间的！'
categories: 
 - 编程
 - 掘金
 - 收藏集
headimg: 'https://picsum.photos/400/300?random=3976'
author: 掘金
comments: false
date: Fri, 26 Feb 2021 00:08:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=3976'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ul>
<li>目前多数人的写法</li>
<li>优化方案</li>
<li>总结</li>
</ul>
<p>根据某一条件从数据库表中查询 『有』与『没有』，只有两种状态，那为什么在写SQL的时候，还要SELECT count(*) 呢？</p>
<p>无论是刚入道的程序员新星，还是精湛沙场多年的程序员老白，都是一如既往的count
目前多数人的写法
多次REVIEW代码时，发现如现现象：
业务代码中，需要根据一个或多个条件，查询是否存在记录，不关心有多少条记录。普遍的SQL及代码写法如下</p>
<h4 data-id="heading-0">SQL写法:</h4>
<pre><code class="copyable">SELECT count(*) FROM table WHERE a = 1 AND b = 2
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">Java写法:</h4>
<pre><code class="copyable">int nums = xxDao.countXxxxByXxx(params);
if ( nums > 0 ) &#123;
  //当存在时，执行这里的代码
&#125; else &#123;
  //当不存在时，执行这里的代码
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是感觉很OK，没有什么问题
优化方案
推荐写法如下：</p>
<h4 data-id="heading-2">SQL写法:</h4>
<pre><code class="copyable">SELECT 1 FROM table WHERE a = 1 AND b = 2 LIMIT 1
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">Java写法:</h4>
<pre><code class="copyable">Integer exist = xxDao.existXxxxByXxx(params);
if ( exist != NULL ) &#123;
  //当存在时，执行这里的代码
&#125; else &#123;
  //当不存在时，执行这里的代码
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SQL不再使用count，而是改用LIMIT 1，让数据库查询时遇到一条就返回，不要再继续查找还有多少条了
业务代码中直接判断是否非空即可</p>
<h4 data-id="heading-4">总结</h4>
<p>根据查询条件查出来的条数越多，性能提升的越明显，在某些情况下，还可以减少联合索引的创建。</p></div>  
</div>
            