
---
title: 'less与sass区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6635'
author: 掘金
comments: false
date: Fri, 21 May 2021 19:21:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=6635'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">less与sass区别</h2>
<h3 data-id="heading-1">1.编译环境不同</h3>
<ul>
<li>Less是基于JavaScript，是在客户端处理的。</li>
<li>Sass是基于Ruby的，是在服务器端处理的。</li>
</ul>
<h3 data-id="heading-2">2.变量符不一样</h3>
<ul>
<li>变量在Less和Sass中的唯一区别就是Less用@，Sass用$</li>
</ul>
<h3 data-id="heading-3">3.输出设置</h3>
<ul>
<li>Less没有输出设置，Sass提供4中输出选项：nested（嵌套输出）, compact（紧凑输出）, compressed（压缩输出） 和 expanded（展开输出）</li>
</ul>
<p>举个例子：.scss</p>
<pre><code class="copyable">nav &#123;  
  ul &#123;  
    margin: 0;  
    padding: 0;  
    list-style: none;  
  &#125;  
  
  li &#123; display: inline-block; &#125;  
  
  a &#123;  
    display: block;  
    padding: 6px 12px;  
    text-decoration: none;  
  &#125;  
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">1>nested（嵌套输出）:</h5>
<pre><code class="copyable">nav ul &#123;  
  margin: 0;  
  padding: 0;  
  list-style: none; &#125;  
nav li &#123;  
  display: inline-block; &#125;  
nav a &#123;  
  display: block;  
  padding: 6px 12px;  
  text-decoration: none; &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">2>expanded(展开输出)：</h5>
<pre><code class="copyable">nav ul &#123;  
  margin: 0;  
  padding: 0;  
  list-style: none;  
&#125;  
nav li &#123;  
  display: inline-block;  
&#125;  
nav a &#123;  
  display: block;  
  padding: 6px 12px;  
  text-decoration: none;  
&#125; 

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">3> compact(紧凑输出):</h5>
<pre><code class="copyable">nav ul &#123; margin: 0; padding: 0; list-style: none; &#125;  
nav li &#123; display: inline-block; &#125;  
nav a &#123; display: block; padding: 6px 12px; text-decoration: none; &#125;  
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">4>compressed(压缩输出)：</h5>
<pre><code class="copyable">nav ul&#123;margin:0;padding:0;list-style:none&#125;nav li&#123;display:inline-block&#125;nav a&#123;display:block;padding:6px 12px;text-decoration:none&#125;  
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">4.条件语句不同</h3>
<ul>
<li>sass支持条件语句，可以使用if&#123;&#125;else&#123;&#125;,for&#123;&#125;循环等等。而less不支持</li>
</ul>
<h3 data-id="heading-9">5.Sass和Less的工具库不同</h3>
<ul>
<li>Sass有工具库Compass, 简单说，Sass和Compass的关系类似于像Javascript和jQuery的关系,Compass在Sass的基础上，封装了一系列有用的模块和模板，补充强化了Sass的功能。</li>
<li>Less有UI组件库Bootstrap,Bootstrap是web前端开发中一个比较有名的前端UI组件库，Bootstrap的样式文件部分源码就是采用Less语法编写。</li>
</ul></div>  
</div>
            