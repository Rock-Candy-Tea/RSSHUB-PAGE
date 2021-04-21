
---
title: '三段代码区别Node中的exports和module.exports'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=42'
author: 掘金
comments: false
date: Wed, 21 Apr 2021 01:25:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=42'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在学习<code>Node</code>过程中，对<code>exports</code>和<code>module.exports</code>有所混淆，所以在弄清楚这两者的区别之后决定用博客记录下两者的区别。
多说不易，先直接上代码，利用<code>exports</code>导出<code>a</code>函数，<code>module.exports</code>导出<code>b</code>函数
text.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span> (<span class="hljs-params"></span>)</span>&#123;
  
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span> (<span class="hljs-params"></span>)</span>&#123;
  
&#125;
<span class="hljs-built_in">exports</span>.a = a
<span class="hljs-built_in">module</span>.exports.b = b
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们打印test模块最终导出的对象将会是下列这种情况</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> test = <span class="hljs-built_in">require</span>(<span class="hljs-string">"test.js)
/**
  test: &#123;
  a: function(),
  b: function()
  &#125; **/
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>这时你会发现<code>a</code>和<code>b</code>函数竟然都被导出，那是不是<code>exports</code>和<code>module.exports</code>导出的是一个对象呢?我们来看看下一个代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span> (<span class="hljs-params"></span>)</span>&#123;
  
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span> (<span class="hljs-params"></span>)</span>&#123;
  
&#125;
<span class="hljs-built_in">exports</span>.a = a
<span class="hljs-built_in">module</span>.exports = &#123;
  b
&#125;
<span class="hljs-comment">/**以上的module.exports = &#123;
 b
&#125;
等同于以下的代码
const newObj = &#123;
 b: b
&#125;
module.exports = newObj
**/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而此时的test.js导出的对象是这样的</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> test = <span class="hljs-built_in">require</span>(<span class="hljs-string">"test.js)
/**
  test: &#123;
  b: function()
  &#125; **/
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>这时导出的对象中就只有<code>b</code>这一个函数，说明这时<code>module.exports = &#123;b&#125;</code>的<code>&#123;&#125;</code>对象是作为我们<code>test.js</code>最终导出的对象。那就是当我们没有对<code>moudle.exports</code>导出的对象进行更改时，将会导出默认对象，并且<code>exports</code>也是指向该对象的。当我们通过<code>module.exports</code>的对象不是默认对象时，<code>exports</code>的指向会在哪里呢?来看看下一列代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span> (<span class="hljs-params"></span>)</span>&#123;
  
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span> (<span class="hljs-params"></span>)</span>&#123;
  
&#125;
<span class="hljs-built_in">module</span>.exports = &#123;
  b
&#125;
<span class="hljs-built_in">exports</span>.a = a
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次打印导出的对象</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> test = <span class="hljs-built_in">require</span>(<span class="hljs-string">"test.js)
/**
  test: &#123;
  b: function()
  &#125; **/
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这三次的示例代码，相信已经对<code>module.exports</code>和<code>exports</code>之间的关系有所理解了。当我们从某个模块中导入时，其实导入了<code>module.exports</code>定义的对象，而<code>exports</code>是<code>module.exports</code>没有改变导出的对象，即默认导出对象的一个引用。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            