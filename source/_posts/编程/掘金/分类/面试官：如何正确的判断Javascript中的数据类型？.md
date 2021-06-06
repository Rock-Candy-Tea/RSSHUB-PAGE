
---
title: '面试官：如何正确的判断Javascript中的数据类型？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9063'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 22:53:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=9063'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与更文挑战的第5天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>面试系列又开始更新啦。</p>
<h2 data-id="heading-1">1. 数据类型的区分</h2>
<p>原始类型： <code>undefined</code>, <code>boolean</code>, <code>number</code>, <code>string</code>, <code>bigInt</code>, <code>symbol</code>, <code>null</code></p>
<p>对象类型：<code>Object （Object, Array, Map, Set, WeakMap, WeakSet, Date......）</code></p>
<p>原始类型，它存储的是一个值。 而对象类型，是通过原生<code>Object</code>派生出来的，它存储的是一个位置(地址/指针)。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 对象类型可以调用方法  </span>
<span class="hljs-comment">// list => [1,2,3,4,5] => Array() => Array().filter</span>
<span class="hljs-keyword">const</span> list = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>] <span class="hljs-comment">//对象类型 </span>
<span class="hljs-keyword">const</span> filterItem = list.filter(<span class="hljs-function"><span class="hljs-params">i</span> =></span> i === <span class="hljs-number">2</span>)  <span class="hljs-comment">// [2] </span>

<span class="hljs-comment">//如果在原始类型上调用方法会怎么样？</span>
<span class="hljs-keyword">const</span> number = <span class="hljs-number">1</span>  <span class="hljs-comment">//原始类型</span>
number.toString() <span class="hljs-comment">// "1"</span>

<span class="hljs-comment">// 1. new Number(number) =>  1 (Number对象派生出来的数据)</span>
<span class="hljs-comment">// 2. 调用toString()   1 => Number() => Object() => Object().toString</span>
<span class="hljs-comment">// 3. return 结果， 销毁当前实例。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">2. 类型判断</h3>
<p><code>typeof</code>：只用于检查原始类型，若检查对象类型的数据只会返回<code>object</code>。</p>
<p><code>instanceof</code>：运算符用于检测构造函数的 <code>prototype</code> 属性是否出现在某个实例对象的原型链上。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">//typeof</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-number">42</span>); <span class="hljs-comment">// number</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-string">'aaaaa'</span>); <span class="hljs-comment">// string</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-literal">true</span>); <span class="hljs-comment">//boolean</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> []); <span class="hljs-comment">//object  如果想要打印出array应该怎么做？</span>

<span class="hljs-comment">//instanceof</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span> (<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span> (<span class="hljs-params"></span>)</span>&#123;&#125; 
<span class="hljs-keyword">let</span> c = <span class="hljs-keyword">new</span> a() 

<span class="hljs-built_in">console</span>.log(c <span class="hljs-keyword">instanceof</span> a) <span class="hljs-comment">// true </span>
<span class="hljs-built_in">console</span>.log(c <span class="hljs-keyword">instanceof</span> b) <span class="hljs-comment">// false </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">需要注意的知识点：</h3>
<ol>
<li>
<p><code>undefined</code>, 创建一个变量，但未被赋值，那就会有个<code>默认值</code> ⇒ <code>undefined</code>。</p>
</li>
<li>
<p><code>Object</code>，它是任何 <code>constructed</code> 对象实例的特殊非数据结构类型，几乎所有通过new创建出来的数据类型。</p>
</li>
<li>
<p><code>instanceof</code>原理和原型链</p>
<p>首先确定两个点，第一点是所有对象都有<code>__proto__</code>属性，只有<code>Object.prototype.proto</code>为<code>null</code>。第二点所有构造函数的<code>prototype</code>都指向它的原型对象，而构造函数的实例的<code>__proto__</code>也指向原型对象。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span> (<span class="hljs-params"></span>) </span>&#123;&#125; 
<span class="hljs-keyword">const</span> b = <span class="hljs-keyword">new</span> a () 

<span class="hljs-built_in">console</span>.log(b.__proto__ === a.prototype) <span class="hljs-comment">// true  都指向构造函数a的原型对象</span>
<span class="hljs-built_in">console</span>.log(b <span class="hljs-keyword">instanceof</span> a) <span class="hljs-comment">// true </span>
<span class="hljs-built_in">console</span>.log(b <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true </span>

<span class="hljs-comment">//nstanceof的原理就是比对prototype是否出现在原型链上。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h3 data-id="heading-4">例题</h3>
<blockquote>
<p>有没有什么更好的办法判断类型？</p>
</blockquote>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> checkType  = <span class="hljs-function"><span class="hljs-params">obj</span> =></span> &#123;
<span class="hljs-keyword">const</span> [typeEx, typeEn] = <span class="hljs-built_in">Object</span>.prototype.toString.call(obj).split(<span class="hljs-string">' '</span>)
<span class="hljs-keyword">return</span> typeEn.substring(<span class="hljs-number">0</span>, typeEn.length - <span class="hljs-number">1</span>).toLowerCase()
&#125;

checkType(<span class="hljs-number">1</span>) <span class="hljs-comment">// number </span>
checkType([]) <span class="hljs-comment">// array</span>
checkType(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()) <span class="hljs-comment">// date</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>能手写实现<code>instanceof</code>吗？</p>
</blockquote>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> instanceOf = <span class="hljs-function">(<span class="hljs-params">left, right</span>) =></span> &#123;
<span class="hljs-keyword">const</span> rpt = right.prototype
<span class="hljs-function"><span class="hljs-title">white</span>(<span class="hljs-params"><span class="hljs-literal">true</span></span>)</span>&#123;
<span class="hljs-keyword">if</span>(left === <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span> 
<span class="hljs-keyword">if</span>(left === rpt) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span> 

left = left.__proto__
&#125;
&#125;
instanceOf([], <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true </span>
instanceOf([], <span class="hljs-built_in">String</span>) <span class="hljs-comment">// false </span>
instanceOf(<span class="hljs-string">'a'</span>, <span class="hljs-built_in">String</span>) <span class="hljs-comment">// true </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">最后</h2>
<p>面试系列第一篇：
<a href="https://juejin.im/post/6844903811316711437" target="_blank" rel="nofollow noopener noreferrer">面试官：你知道Callback Hell（回调地狱）吗？
</a></p>
<p>面试系列第二篇：
<a href="https://juejin.im/post/6844903813569052679" target="_blank" rel="nofollow noopener noreferrer">面试官：react和vue有什么区别吗？
</a></p>
<p>面试系列第三篇：
<a href="https://juejin.im/post/6844903813833293838" target="_blank" rel="nofollow noopener noreferrer">面试官：你了解es6的知识吗？
</a></p>
<p>面试系列第四篇：
<a href="https://juejin.im/post/6844903818107305998" target="_blank" rel="nofollow noopener noreferrer">面试官：你了解Webpack吗？
</a></p>
<p>面试系列第五篇：
<a href="https://juejin.cn/post/6844903824356802567" target="_blank">面试官：你使用webpack时手写过loader，分离过模块吗？
</a></p>
<h3 data-id="heading-6">如果您有收获或者疑问请在下方评论，求赞！谢谢观看到这里。</h3></div>  
</div>
            