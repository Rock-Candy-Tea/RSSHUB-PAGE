
---
title: 'TypeScript上手01 常用数据类型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5152'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 01:28:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=5152'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第1天，活动详情查看<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h1 data-id="heading-0">1.ts定义静态类型</h1>
<p>TypeScript 的一个最主要特点就是可以定义静态类型，英文是 Static Typing。那到底是什么意思那？太复杂的概念性东西这里就不讲了，你可以简单的理解“静态类型”为，就是你一旦定义了，就不可以再改变了。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> <span class="hljs-built_in">number</span>: <span class="hljs-built_in">number</span> = <span class="hljs-number">1</span>;
<span class="hljs-comment">//自定义静态类型</span>
<span class="hljs-keyword">interface</span> XiaoJieJie &#123;
    <span class="hljs-attr">uname</span>: <span class="hljs-built_in">string</span>;
    age: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">const</span> xiaohong: XiaoJieJie = &#123;
    <span class="hljs-attr">uname</span>: <span class="hljs-string">"小红"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果使用了静态类型，不仅意味着变量的类型不可以改变，
还意味着类型的属性和方法也跟着确定了。这个特点就大大提高了程序的健壮性，
并且编辑器这时候也会给你很好的语法提示，加快了你的开发效率。</p>
<h1 data-id="heading-1">2. 基础静态类型和对象类型</h1>
<h2 data-id="heading-2">2.1 基础静态类型</h2>
<p>基础静态类型非常简单，只要在声明变量的后边加一个<code>:</code>号，然后加上对应的类型哦。比如下面的代码，就是声明了一个数字类型的变量，叫做count。
<code>string number null undefined symbol Boolean void</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> count : <span class="hljs-built_in">number</span> = <span class="hljs-number">918</span>;
<span class="hljs-keyword">const</span> myName : <span class="hljs-built_in">string</span> = <span class="hljs-string">'peng'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">2.2 对象类型</h2>
<p>2.2.1 对象类型可以是对象</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> xiaoJieJie: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>,
  &#125; = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"柏特"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
  &#125;;
  <span class="hljs-built_in">console</span>.log(xiaoJieJie.name);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.2.2 对象类型可以数组</p>
<p>String[]代表数组中必须是字符串,出现数字会出现报错的情况</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> xiaoJieJies: <span class="hljs-built_in">String</span>[] = [<span class="hljs-string">"111"</span>, <span class="hljs-string">"222"</span>, <span class="hljs-string">"333"</span>]; 

<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.2.3 用类的形式定义变量</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;&#125;
<span class="hljs-keyword">const</span> better: Person = <span class="hljs-keyword">new</span> Person();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>better必须是person类对应的一个对象</p>
<p>2.2.4 定义一个函数类型</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> jianXiaoJieJie: <span class="hljs-function">() =></span> string = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">"better"</span>;
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>总结: 对象类型可以有的形式: 对象类型 数组类型 类类型 函数,类型</p>
</blockquote></div>  
</div>
            