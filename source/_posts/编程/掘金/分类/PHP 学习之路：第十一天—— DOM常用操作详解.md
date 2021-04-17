
---
title: 'PHP 学习之路：第十一天—— DOM常用操作详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66a1db19a8d74ca6910bdd7a4ca6b537~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 17 Apr 2021 00:43:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66a1db19a8d74ca6910bdd7a4ca6b537~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、类数组</h1>
<h2 data-id="heading-1">1.类数组的定义</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 类数组,其实是一个特殊的对象,长得像数组,但它又不是数组</span>
<span class="hljs-comment">// 类数组有二个特征：</span>
<span class="hljs-comment">//   1. 有一个length属性</span>
<span class="hljs-comment">//   2. 有递增的正整数索引</span>
<span class="hljs-keyword">const</span> brand = &#123;
    <span class="hljs-number">0</span>: <span class="hljs-string">'HUAWEI'</span>,
    <span class="hljs-number">1</span>: <span class="hljs-string">'APPLE'</span>,
    <span class="hljs-number">2</span>: <span class="hljs-string">'XIAOMI'</span>,
    <span class="hljs-attr">length</span>: <span class="hljs-number">3</span>,
&#125;;
<span class="hljs-built_in">console</span>.log(brand);
<span class="hljs-built_in">console</span>.log(brand.length);
<span class="hljs-built_in">console</span>.log(brand[<span class="hljs-number">0</span>], brand[<span class="hljs-number">1</span>], brand[<span class="hljs-number">2</span>]);
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.isArray(brand)); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(brand <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>类数组和数组的区别</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 数组可以使用 push(): 从尾部向数组追加一个成员</span>
<span class="hljs-comment">// 类数组则会报错 "brand.push is not a function"</span>
<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-built_in">console</span>.log(arr);  <span class="hljs-comment">// [1, 2, 3]</span>
arr.push(<span class="hljs-number">4</span>);
<span class="hljs-built_in">console</span>.log(arr); <span class="hljs-comment">// [1, 2, 3, 4]</span>

<span class="hljs-keyword">const</span> brand = &#123;
    <span class="hljs-number">0</span>: <span class="hljs-string">'HUAWEI'</span>,
    <span class="hljs-number">1</span>: <span class="hljs-string">'APPLE'</span>,
    <span class="hljs-number">2</span>: <span class="hljs-string">'XIAOMI'</span>,
    <span class="hljs-attr">length</span>: <span class="hljs-number">3</span>,
&#125;;
brand.push(<span class="hljs-string">"OnePlus"</span>); <span class="hljs-comment">// "brand.push is not a function"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>类数组转为真正的数组</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> brand = &#123;
    <span class="hljs-number">0</span>: <span class="hljs-string">'HUAWEI'</span>,
    <span class="hljs-number">1</span>: <span class="hljs-string">'APPLE'</span>,
    <span class="hljs-number">2</span>: <span class="hljs-string">'XIAOMI'</span>,
    <span class="hljs-attr">length</span>: <span class="hljs-number">3</span>,
&#125;;
<span class="hljs-comment">// 将“类数组”转为真正的数组，方便我们使用强大的数组方法来操作</span>
<span class="hljs-comment">// 1. Array.from()</span>
<span class="hljs-keyword">let</span> arr1 = <span class="hljs-built_in">Array</span>.from(brand);
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.isArray(arr1)); <span class="hljs-comment">// true</span>
arr1.push(<span class="hljs-string">"vivo"</span>);
<span class="hljs-built_in">console</span>.log(arr1); <span class="hljs-comment">// ["HUAWEI", "APPLE", "XIAOMI", "vivo"]</span>

<span class="hljs-comment">// 2. [...rest]:归并参数,rest语法</span>
<span class="hljs-comment">// 直接转换时报错 "brand is not iterable"</span>
<span class="hljs-comment">// let arr2 = [...brand];  // "brand is not iterable"</span>
<span class="hljs-comment">// js为一些预置的类型创建了迭代器接口,但是自定义的类型就没有，只有我们自己手工创建</span>
<span class="hljs-built_in">Object</span>.defineProperty(brand, <span class="hljs-built_in">Symbol</span>.iterator, &#123;
<span class="hljs-function"><span class="hljs-title">value</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">const</span> keys = <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">this</span>);
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">next</span>: <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">done</span>: index >= keys.length - <span class="hljs-number">1</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-built_in">this</span>[keys[index++]],
      &#125;;
    &#125;,
  &#125;;
&#125;,
&#125;);
<span class="hljs-keyword">let</span> arr2 = [...brand];
<span class="hljs-built_in">console</span>.log(arr2, <span class="hljs-built_in">Array</span>.isArray(arr2)); <span class="hljs-comment">// ["HUAWEI", "APPLE", "XIAOMI"] true</span>
arr2.push(<span class="hljs-string">'OPPO'</span>);
<span class="hljs-built_in">console</span>.log(arr2); <span class="hljs-comment">// ["HUAWEI", "APPLE", "XIAOMI", "OPPO"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">二、快速获取 DOM 元素</h1>
<h2 data-id="heading-3">1.使用 js 基本语法，仿写 jQuery 的 "$"</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item4<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item5<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-comment">// $("body"): jQuery 用这个语法来获取'body'元素</span>
      <span class="hljs-keyword">let</span> $ = <span class="hljs-function"><span class="hljs-params">selector</span> =></span> <span class="hljs-built_in">document</span>.querySelector(selector);
      <span class="hljs-built_in">console</span>.log($);
      <span class="hljs-built_in">console</span>.log($(<span class="hljs-string">"body"</span>));
      <span class="hljs-comment">// 设置 body 的背景颜色</span>
      $(<span class="hljs-string">'body'</span>).style.background = <span class="hljs-string">"lightcyan"</span>;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">2.获取所有满足条件的元素的集合</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item4<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item5<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">// 获取满足条件的元素的集合</span>
    <span class="hljs-keyword">const</span> items = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">".list .item"</span>);
    <span class="hljs-comment">// NodeList: 类数组</span>
    <span class="hljs-comment">// 遍历 items 元素</span>
    <span class="hljs-comment">// NodeList有一个forEach()接口</span>
    <span class="hljs-comment">// item: 正在遍历的当前元素,必选</span>
    <span class="hljs-comment">// index: 当前元素的索引</span>
    <span class="hljs-comment">// items: 当前遍历的数组对象</span>
    items.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">item, index, items</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(item, index, items);
    &#125;);
    <span class="hljs-comment">// 使用箭头函数简化，以后这个语法使用更多</span>
    items.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> <span class="hljs-built_in">console</span>.log(item));

    <span class="hljs-comment">// 思考：如何获取第一个满足条件的元素？</span>
    <span class="hljs-keyword">let</span> firstItem = items[<span class="hljs-number">0</span>];
    <span class="hljs-built_in">console</span>.log(firstItem);
    firstItem.style.background = <span class="hljs-string">"lightgreen"</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">3.获取满足条件的元素集合中的第一个元素</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item4<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item5<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 获取满足条件的元素集合中的第一个元素</span>
  firstItem = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".list .item"</span>);
  <span class="hljs-built_in">console</span>.log(firstItem);
  firstItem.style.background = <span class="hljs-string">"green"</span>;
  <span class="hljs-comment">// querySelector()总是返回唯一元素，常用于 id</span>

  <span class="hljs-comment">// querySelectorAll, querySelector, 也可以用在元素上</span>
  <span class="hljs-keyword">let</span> list = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".list"</span>);
  <span class="hljs-keyword">let</span> items = list.querySelectorAll(<span class="hljs-string">".item"</span>);
  <span class="hljs-built_in">console</span>.log(items);
  <span class="hljs-comment">// NodeList它自了一个迭代器接口, for-of 进行遍历</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> items) &#123;
    <span class="hljs-built_in">console</span>.log(item);
  &#125;

  <span class="hljs-comment">//  以下传统方式, es6 以后不推荐使用</span>
  <span class="hljs-comment">//   document.getElementById()</span>
  <span class="hljs-comment">//   document.getElementsByTagName()</span>
  <span class="hljs-comment">//   document.getElementsByName()</span>
  <span class="hljs-comment">//   document.getElementsByClassName()</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">4.快速获取一些特定的元素</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item4<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item5<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

<span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">action</span>=<span class="hljs-string">""</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"hello"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"login"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"email"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"demo@email.com"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span>></span>提交<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">form</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 快速获取一些特定的元素</span>
  <span class="hljs-comment">// body</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.body);
  <span class="hljs-comment">// head</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.head);
  <span class="hljs-comment">// title</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.title);
  <span class="hljs-comment">// html</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.documentElement);

  <span class="hljs-comment">//forms</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.forms);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.forms[<span class="hljs-number">0</span>]);
  <span class="hljs-comment">// <form action="" name="hello" id="login"></span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.forms[<span class="hljs-string">"hello"</span>]);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.forms[<span class="hljs-string">"login"</span>]);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.forms.item(<span class="hljs-number">0</span>));
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.forms.item(<span class="hljs-string">"hello"</span>));
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.forms.item(<span class="hljs-string">"login"</span>));
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.forms.namedItem(<span class="hljs-string">"hello"</span>));
  <span class="hljs-comment">// forms.id</span>
  <span class="hljs-comment">// 推荐用id,因为id方便添加样式</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.forms.login);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.forms.hello);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">三、DOM 树的遍历和元素的获取</h1>
<h2 data-id="heading-8">1. 将类数组转为真正的数组类型</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item4<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item5<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item6<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// dom树中的所有内容都是:节点</span>
  <span class="hljs-comment">// 节点是有类型的: 元素,文本,文档,属性..</span>
  <span class="hljs-keyword">let</span> nodes = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".list"</span>);
  <span class="hljs-built_in">console</span>.log(nodes.childNodes);
  <span class="hljs-comment">// 通常只关注元素类型的节点</span>
  <span class="hljs-built_in">console</span>.log(nodes.children);
  <span class="hljs-keyword">let</span> eles = nodes.children;

  <span class="hljs-comment">// 遍历</span>
  <span class="hljs-comment">// 将类数组转为真正的数组类型</span>
  <span class="hljs-built_in">console</span>.log([...eles]);
  [...eles].forEach(<span class="hljs-function"><span class="hljs-params">ele</span> =></span> <span class="hljs-built_in">console</span>.log(ele));
  <span class="hljs-comment">// 获取第一个</span>
  <span class="hljs-keyword">let</span> firstItem = eles[<span class="hljs-number">0</span>];
  firstItem.style.background = <span class="hljs-string">"yellow"</span>;
  <span class="hljs-comment">// 最后一个</span>
  <span class="hljs-comment">//   let lastItem = eles[4];</span>
  <span class="hljs-keyword">let</span> lastItemIndex = eles.length - <span class="hljs-number">1</span>;
  <span class="hljs-keyword">let</span> lastItem = eles[lastItemIndex];
  lastItem.style.background = <span class="hljs-string">"lightblue"</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">2. 使用 js 提供的快捷方式来获取第一个和最后一个</h2>
<ul>
<li><code>firstElementChild</code> 获取第一个</li>
<li><code>lastElementChild</code> 获取最后一个</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item4<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item5<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item6<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// js提供一些快捷方式来获取第一个和最后一个</span>
  <span class="hljs-keyword">const</span> list = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".list"</span>);
  firstItem = list.firstElementChild;
  firstItem.style.background = <span class="hljs-string">"seagreen"</span>;

  lastItem = list.lastElementChild;
  lastItem.style.background = <span class="hljs-string">"yellow"</span>;

  <span class="hljs-built_in">console</span>.log(eles.length);
  <span class="hljs-built_in">console</span>.log(list.childElementCount);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">3. 兄弟节点的获取</h2>
<ul>
<li><code>nextElementSibling</code> 下一个兄弟节点</li>
<li><code>previousElementSibling</code> 前一个兄弟节点</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item4<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item5<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>item6<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">//   如何想获取第二个元素怎么办?</span>
  <span class="hljs-comment">//   第二个元素就是第一个元素的下一个兄弟节点</span>
  <span class="hljs-keyword">let</span> secondItem = firstItem.nextElementSibling;
  secondItem.style.background = <span class="hljs-string">"red"</span>;

  <span class="hljs-comment">// 获取第5个, 是最后一个元素的前一个兄弟节点</span>
  <span class="hljs-keyword">let</span> fiveItem = lastItem.previousElementSibling;
  fiveItem.style.background = <span class="hljs-string">"cyan"</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">四、DOM 元素的内容</h1>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> box = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".box"</span>);
  <span class="hljs-keyword">const</span> p = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"p"</span>);
  <span class="hljs-comment">// textContent: 添加文本</span>
  p.textContent = <span class="hljs-string">"hello world"</span>;
  <span class="hljs-comment">// html字符串</span>
  p.textContent = <span class="hljs-string">'<em style="color:red">php.cn</em>'</span>;

  <span class="hljs-comment">// 如果想将html字符串渲染出来应该使用innerHTML</span>
  p.innerHTML = <span class="hljs-string">'<em style="color:red">php.cn</em>'</span>;

  <span class="hljs-comment">// outerHTML: 使用当成的文本将当前节点直接替换掉(实际上就是当前内容的父节点)</span>
  p.outerHTML = <span class="hljs-string">'<em style="color:red">php.cn</em>'</span>;
  <span class="hljs-built_in">console</span>.log(box);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">五、dataset 自定义数据属性</h1>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"user"</span> <span class="hljs-attr">email</span>=<span class="hljs-string">"a@qq.com"</span> <span class="hljs-attr">data-email</span>=<span class="hljs-string">"admin@php.cn"</span> <span class="hljs-attr">data-my-age</span>=<span class="hljs-string">"99"</span>></span>我的档案<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> p = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"p"</span>);
  <span class="hljs-comment">// id是默认的内置的标准属性,所以可以直接用点语法进行访问</span>
  <span class="hljs-built_in">console</span>.log(p.id);
  <span class="hljs-comment">// email是非内置属性</span>
  <span class="hljs-built_in">console</span>.log(p.email);

  <span class="hljs-comment">// 1.对于自定义的数据属性"data-",使用dataset对象来操作</span>
  <span class="hljs-built_in">console</span>.log(p.dataset.email);

  <span class="hljs-comment">// console.log(p.dataset["my-age"]);</span>
  <span class="hljs-comment">// 2.多个单词要转换为驼峰式</span>
  <span class="hljs-built_in">console</span>.log(p.dataset.myAge);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">六、DOM 树元素的增删改查</h1>
<h2 data-id="heading-14">1.创建 DOM 元素，并添加到页面显示</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建dom元素</span>
<span class="hljs-keyword">let</span> div = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
<span class="hljs-keyword">let</span> span = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"span"</span>);
span.textContent = <span class="hljs-string">"hello"</span>;

<span class="hljs-comment">// append(ele,'text'),将参数做为父元素的最后一个子元素追加到列表中,无返回值</span>
<span class="hljs-comment">// span 添加到 div中</span>
<span class="hljs-comment">// div.append(span);</span>
<span class="hljs-comment">// 将 span,"world"，添加到 div中</span>
div.append(span, <span class="hljs-string">" world"</span>);
<span class="hljs-comment">// 方式一： 将 div 添加到页面</span>
<span class="hljs-built_in">document</span>.body.append(div);
<span class="hljs-built_in">console</span>.log(div)

<span class="hljs-comment">// 方式二：将 span, " world" 添加到页面</span>
<span class="hljs-comment">// document.body.append(span, " world");</span>
<span class="hljs-comment">// console.log(div)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">2.为什么div中的span消失了?</h2>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66a1db19a8d74ca6910bdd7a4ca6b537~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2572a0bd36542eb8e6dafebcf22d6df~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 为什么div中的span消失了?</span>
<span class="hljs-comment">// 新元素span只能插入到一个地方;span在div,现在span在body中,相当于剪切操作</span>
<span class="hljs-comment">// 如果想保留span在div中,要克隆span</span>
<span class="hljs-comment">// cloneNode(true), true: 是完整的保留元素内部结构</span>
<span class="hljs-built_in">document</span>.body.append(span.cloneNode(<span class="hljs-literal">true</span>), <span class="hljs-string">" world"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如图：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2fca994b246446da4961bab9dcc0524~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">3. DOM 树元素的增删改</h2>
<ul>
<li><code>append()</code>:在尾部追加</li>
<li><code>prepend()</code>:在头部追加</li>
<li><code>before()</code>:在参考点之前添加一个新节点</li>
<li><code>after()</code>:在参考点之后添加一个新节点</li>
<li><code>replaceWith()</code>:替换元素</li>
<li><code>remove(无参数)</code>:删除元素</li>
<li><code>afterBegin</code>: 开始标签之后,第一个子元素</li>
<li><code>beforeBegin</code>: 开始标签之前,是它的前一个兄弟元素</li>
<li><code>afterEnd</code>: 结束标签之后,它的下一个兄弟元素</li>
<li><code>beforeEnd</code>: 结束标签之前,它的最后一个子元素</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// append()创建一个列表</span>
<span class="hljs-keyword">const</span> ul = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"ul"</span>);
<span class="hljs-comment">// 循环来生成多个列表项 li</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i <= <span class="hljs-number">5</span>; i++) &#123;
<span class="hljs-keyword">let</span> li = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"li"</span>);
li.textContent = <span class="hljs-string">`item<span class="hljs-subst">$&#123;i&#125;</span>`</span>;
ul.append(li);
&#125;
<span class="hljs-built_in">document</span>.body.append(ul);

<span class="hljs-comment">// append():在尾部追加</span>
<span class="hljs-comment">// prepend():在头部追加</span>
li = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"li"</span>);
li.textContent = <span class="hljs-string">"first item"</span>;
li.style.color = <span class="hljs-string">"red"</span>;
ul.prepend(li);

<span class="hljs-comment">// 如果想在除了头尾之外的地方添加怎么操作?</span>
<span class="hljs-comment">// 必须要有一个参考节点的位置,否则就不知道要添加到哪个节点的前面或后面</span>
<span class="hljs-comment">// 以第四个节点为参考</span>
<span class="hljs-keyword">const</span> referNode = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"li:nth-of-type(4)"</span>);
referNode.style.background = <span class="hljs-string">"cyan"</span>;
<span class="hljs-comment">// 在它之前添加一个新节点</span>
li = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"li"</span>);
li.textContent = <span class="hljs-string">"在参考节点之前插入"</span>;
li.style.background = <span class="hljs-string">"yellow"</span>;
<span class="hljs-comment">// referNode.before(el),在插入位置(参考节点)上调用</span>
referNode.before(li);

<span class="hljs-comment">// 在它之后添加一个新节点</span>
li = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"li"</span>);
li.textContent = <span class="hljs-string">"在参考节点之后插入"</span>;
li.style.background = <span class="hljs-string">"violet"</span>;
<span class="hljs-comment">// referNode.after(el),在插入位置(参考节点)上调用</span>
referNode.after(li);

<span class="hljs-comment">// 替换节点</span>
<span class="hljs-comment">// 将最后一个节点用链接替换</span>
<span class="hljs-keyword">let</span> lastItem = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"ul li:last-of-type"</span>);
<span class="hljs-keyword">let</span> a = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"a"</span>);
a.textContent = <span class="hljs-string">"php中文网"</span>;
a.href = <span class="hljs-string">"https://php.cn"</span>;
lastItem.replaceWith(a);

<span class="hljs-comment">// 删除节点,在被删除的节点上直接调用</span>
<span class="hljs-comment">// 将ul的第6个删除,remove(无参数)</span>
ul.querySelector(<span class="hljs-string">":nth-of-type(6)"</span>).remove();

<span class="hljs-comment">// 再介绍几个更牛的</span>
<span class="hljs-comment">// insertAdjacentElement('插入位置', 元素)</span>
<span class="hljs-comment">// 插入位置有四个</span>
<span class="hljs-comment">// afterBegin: 开始标签之后,第一个子元素</span>
<span class="hljs-comment">// beforeBegin: 开始标签之前,是它的前一个兄弟元素</span>
<span class="hljs-comment">// afterEnd: 结束标签之后,它的下一个兄弟元素</span>
<span class="hljs-comment">// beforeEnd: 结束标签之前,它的最后一个子元素</span>
<span class="hljs-comment">// 插入第一个子元素之前(在起始标签之后);</span>
li = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"li"</span>);
li.textContent = <span class="hljs-string">"第一个子元素"</span>;
ul.insertAdjacentElement(<span class="hljs-string">"afterbegin"</span>, li);
ul.insertAdjacentElement(<span class="hljs-string">"beforebegin"</span>, li);

<span class="hljs-comment">// 还有一个plus,可以直接使用html字符串当元素,省去了创建元素的过程</span>
<span class="hljs-comment">// 追加到结尾</span>
ul.insertAdjacentHTML(<span class="hljs-string">"beforeEnd"</span>, <span class="hljs-string">'<li style="color:red">最后一个子元素</li>'</span>);

<span class="hljs-comment">// 还可以直接插入文本</span>
<span class="hljs-keyword">const</span> h2 = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"h2"</span>);
h2.insertAdjacentText(<span class="hljs-string">"beforeend"</span>, ul.lastElementChild.textContent);
<span class="hljs-built_in">console</span>.log(h2);
<span class="hljs-built_in">document</span>.body.insertAdjacentElement(<span class="hljs-string">"afterend"</span>, h2);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-17">七、css 操作</h1>
<h2 data-id="heading-18">1.行内样式</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>Hello World<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> p = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"p"</span>);
  <span class="hljs-comment">// 添加行内样式</span>
  p.style.color = <span class="hljs-string">"red"</span>;
  <span class="hljs-built_in">console</span>.log(p);
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">2.  类样式 <code>classList</code></h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-class">.bgc-cyan</span> &#123;
    <span class="hljs-attribute">background-color</span>: cyan;
  &#125;
  <span class="hljs-selector-class">.bgc-yellow</span> &#123;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#ff0</span>;
  &#125;
  <span class="hljs-selector-class">.border</span> &#123;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">3px</span> solid <span class="hljs-number">#000</span>;
  &#125;
  <span class="hljs-selector-class">.bolder</span> &#123;
    <span class="hljs-attribute">font-weight</span>: bolder;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>Hello World<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"toggleBorder"</span>></span>切换边框<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> p = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"p"</span>);
  <span class="hljs-comment">// add() 添加样式，可同时添加多个</span>
  p.classList.add(<span class="hljs-string">"bgc-cyan"</span>);
  p.classList.add(<span class="hljs-string">"border"</span>, <span class="hljs-string">"bolder"</span>);
  <span class="hljs-comment">// remove() 删除样式</span>
  p.classList.remove(<span class="hljs-string">"border"</span>);
  <span class="hljs-comment">// replace() 替换样式</span>
  p.classList.replace(<span class="hljs-string">"bgc-cyan"</span>, <span class="hljs-string">"bgc-yellow"</span>);

  btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// toggle: 样式自动切换, 如果已存在则删除, 如果不存在则添加;</span>
    p.classList.toggle(<span class="hljs-string">"border"</span>);
  &#125;;

  <span class="hljs-comment">// className 每次只能添加一个样式，不推荐使用</span>
  <span class="hljs-comment">// p.className = "bgc-yellow";</span>
  <span class="hljs-comment">// p.className = "bgc-yellow border";</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">3.计算样式</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"height: 50px; background-color: #ff0; color: red"</span>></span>Hello World<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> div = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"div"</span>);
  <span class="hljs-comment">// 一个元素最终应该渲染成什么样式，由浏览器来决定</span>
  <span class="hljs-comment">// 浏览器根据一个元素的行内样式,内部样式,外部样式表来计算出最终的样式</span>
  
  <span class="hljs-comment">// getComputedStyle(要查看样式的元素 , 伪元素)</span>
  <span class="hljs-keyword">let</span> styles = <span class="hljs-built_in">window</span>.getComputedStyle(p, <span class="hljs-literal">null</span>);
  
  <span class="hljs-comment">//得到背景色，不同浏览器得到的不一样,chrom 浏览器报错</span>
  <span class="hljs-comment">// let styles = document.defaultView.getComputedStyle("p", null);</span>
  
  <span class="hljs-comment">// 计算样式都是只读的</span>
  <span class="hljs-comment">// console.log(styles);</span>
  <span class="hljs-built_in">console</span>.log(styles.getPropertyValue(<span class="hljs-string">"height"</span>));
  <span class="hljs-built_in">console</span>.log(styles.getPropertyValue(<span class="hljs-string">"background-color"</span>));
  <span class="hljs-built_in">console</span>.log(styles.getPropertyValue(<span class="hljs-string">"color"</span>));
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            