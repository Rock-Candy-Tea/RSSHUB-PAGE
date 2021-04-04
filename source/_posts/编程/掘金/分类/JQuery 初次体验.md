
---
title: 'JQuery 初次体验'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3533'
author: 掘金
comments: false
date: Sat, 03 Apr 2021 19:28:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=3533'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">JavaScript 与 JQuery的关系</h2>
<p>jQuery是JavaScript库中的一种,JavaScript库也可以叫JavaScript函数库<br>
封装了很多js代码的一个js文件就是一个库。 Prototype、YUI(网络反响一般)、Dojo、ExtJS、jQuery等 都是JS库</p>
<h3 data-id="heading-1">jQuery 优点</h3>
<p>写的少做的多,体积小,功能强大,链式编程,隐式迭代.插件丰富,开源,免费,兼容性强</p>
<h3 data-id="heading-2">jQuery的js文件</h3>
<pre><code class="hljs language-js copyable" lang="js">jquery-<span class="hljs-number">1.12</span><span class="hljs-number">.1</span>.js      <span class="hljs-comment">//正常的代码文件</span>
jquery-<span class="hljs-number">1.12</span><span class="hljs-number">.1</span>.min.js  <span class="hljs-comment">//压缩的代码文件，上线的时候使用压缩的</span>

<span class="hljs-comment">//线上CDN</span>
<script src=<span class="hljs-string">"https://cdn.bootcdn.net/ajax/libs/jquery/2.2.1/jquery.js"</span>></script>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://libs.baidu.com/jquery/2.1.1/jquery.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://ajax.aspnetcdn.com/ajax/jquery/jquery-2.1.1.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://code.jquery.com/jquery-2.1.1.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">JQuery中的顶级对象</h2>
<p><code>JQuery</code> -- 可以用<code>$</code>符号来代替<br>
<code>JQuery</code> 的JS文件中的所有的东西都是jQuery或者都是$符号下的</p>
<ul>
<li>如果想要使用jQuery中的属性或者方法,那么需要 <code>jQuery.属性</code>、<code>jQuery.xxx()</code> 来使用</li>
<li>简单的写法: <code>$.属性</code>  <code>$.方法</code></li>
<li>大多数情况下,jQuery中几乎都是方法,属性很少</li>
<li>JQuery中几乎把DOM中的事件都封装成了一个方法,在jQuery中几乎是把on去掉,然后变成方法了</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//jQuery中注册事件</span>
$(<span class="hljs-string">"选择器"</span>).click(匿名函数);

<span class="hljs-comment">//DOM中注册事件</span>
<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"id属性值"</span>).onclick=匿名函数;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>浏览器中的顶级对象:window,浏览器中和页面中所有的东西都是window的</li>
<li>页面中的顶级对象:document,页面中某些东西是document</li>
</ul>
<h2 data-id="heading-4">jquery加载</h2>
<h3 data-id="heading-5">JS DOM中页面加载事件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"好帅"</span>);
&#125;;

<span class="hljs-built_in">window</span>.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"哈哈,我又变帅了"</span>);
&#125;;

<span class="hljs-comment">/* 
哈哈,我又变帅了
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>⚠️<strong>注意:</strong> 页面全部加载完毕才触发(标签,文字,图片,引入的文件)</p>
<h3 data-id="heading-6">JQuery中页面加载的事件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 方法1</span>
$(<span class="hljs-built_in">window</span>).load(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"第1种页面加载的事件"</span>);
&#125;);

<span class="hljs-comment">// 方法2</span>
<span class="hljs-comment">// 这种采用的事件比方法1快，页面中的基本的元素加载后就触发</span>
$(<span class="hljs-built_in">document</span>).ready(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"第2种页面加载的事件"</span>);
&#125;);

<span class="hljs-comment">// 方法3</span>
<span class="hljs-comment">// 页面中基本的元素加载后就触发了</span>
jQuery(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"第3种页面加载的事件"</span>);
&#125;);

<span class="hljs-comment">//简写</span>
$(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123; &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">window.onload 和 $(function) 区别</h3>
<ul>
<li><code>window.onload</code> 只能定义一次,如果定义多次，后边的会将前边的覆盖掉</li>
<li><code>$(function)</code> 可以定义多次的</li>
</ul>
<h2 data-id="heading-8">jQuery对象和DOM对象互转的问题</h2>
<pre><code class="hljs language-js copyable" lang="js">jq -> js
jq对象[索引] 或者 jq对象.get(索引)

js -> jq
$(js对象)



<script src=<span class="hljs-string">"https://cdn.bootcdn.net/ajax/libs/jquery/2.2.1/jquery.js"</span>></script>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">var</span> btn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"btn"</span>);
  <span class="hljs-comment">// DOM对象转jQuery对象</span>
  $(btn).click(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-string">"JQ注册点击事件"</span>);
  &#125;);
  <span class="hljs-comment">// //错误的</span>
  <span class="hljs-comment">// btn.click(function () &#123;</span>
  <span class="hljs-comment">//   alert("哈哈,小苏太帅了");</span>
  <span class="hljs-comment">// &#125;);</span>


  <span class="hljs-comment">//jQuery对象转DOM对象</span>
  <span class="hljs-keyword">var</span> btn2 = $(<span class="hljs-string">"#btn"</span>);
  btn2[<span class="hljs-number">0</span>].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-string">"哈哈,我又变帅了"</span>);
  &#125;;
  <span class="hljs-comment">// //错误的</span>
  <span class="hljs-comment">// btn2.onclick = function () &#123;</span>
  <span class="hljs-comment">//   console.log("助教比小杨帅");</span>
  <span class="hljs-comment">// &#125;;</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么要把DOM对象转jQuery对象,为什么又把jQuery对象转DOM对象?</p>
<ul>
<li>DOM操作很麻烦(兼容,一个功能写好多代码) -> 转jQuery对象,操作简单(使用jQuery中的方法或属性),不需要写兼容，</li>
<li>jQuery操作中有一些兼容没封装在jQuery中,转DOM对象,通过原生的js代码实现功能,如果后面都解决了,又想简单的写代码操作内容,再转回jQuery对象</li>
</ul>
<p>⚠️<strong>注意:</strong> DOM对象调用jQuery的方法不能实现,必须是jQuery对象调用jQuery的方法</p>
<h2 data-id="heading-9">开关灯案例</h2>
<p><strong>DOM版本</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><input type=<span class="hljs-string">"button"</span> id=<span class="hljs-string">"btn"</span> value=<span class="hljs-string">"开灯"</span>>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css"><span class="hljs-selector-class">.cls</span>&#123;<span class="hljs-attribute">background-color</span>: black;&#125;</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"btn"</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> body = <span class="hljs-built_in">document</span>.body;
    <span class="hljs-keyword">if</span> (body.className == <span class="hljs-string">"cls"</span>) &#123;
      body.className = <span class="hljs-string">""</span>;
      <span class="hljs-built_in">this</span>.value = <span class="hljs-string">"关灯"</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      body.className = <span class="hljs-string">"cls"</span>;
      <span class="hljs-built_in">this</span>.value = <span class="hljs-string">"开灯"</span>;
    &#125;
  &#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>JQ版本</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><script src=<span class="hljs-string">"https://libs.baidu.com/jquery/2.1.1/jquery.min.js"</span>></script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"开灯"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-class">.cls</span> &#123; <span class="hljs-attribute">background-color</span>: black; &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

  <span class="hljs-comment">//方法1 </span>
  <span class="hljs-comment">// $("#btn").click(function () &#123;</span>
  <span class="hljs-comment">//   if ($(this).val() == "开灯") &#123;</span>
  <span class="hljs-comment">//     $("body").css("background-color", "black");</span>
  <span class="hljs-comment">//     $(this).val("关灯");</span>
  <span class="hljs-comment">//   &#125; else &#123;</span>
  <span class="hljs-comment">//     $("body").css("background-color", "gray");</span>
  <span class="hljs-comment">//     $(this).val("开灯");</span>
  <span class="hljs-comment">//   &#125;</span>
  <span class="hljs-comment">// &#125;)</span>

  <span class="hljs-comment">//方法2</span>
  $(<span class="hljs-string">"#btn"</span>).click(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    $(<span class="hljs-string">"body"</span>).hasClass(<span class="hljs-string">"cls"</span>) ? $(<span class="hljs-built_in">this</span>).val(<span class="hljs-string">"开灯"</span>) : $(<span class="hljs-built_in">this</span>).val(<span class="hljs-string">"关灯"</span>)
    $(<span class="hljs-string">"body"</span>).hasClass(<span class="hljs-string">"cls"</span>) ? $(<span class="hljs-string">"body"</span>).removeClass(<span class="hljs-string">"cls"</span>) : $(<span class="hljs-string">"body"</span>).addClass(<span class="hljs-string">"cls"</span>)
  &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            