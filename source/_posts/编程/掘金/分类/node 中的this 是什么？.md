
---
title: 'node 中的this 是什么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31e7e43c5425401da8c2f28d5c7dc2ff~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 29 May 2021 06:16:51 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31e7e43c5425401da8c2f28d5c7dc2ff~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31e7e43c5425401da8c2f28d5c7dc2ff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">和浏览器里面不同的地方：</h2>
<p>创建 <code>main.js</code></p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">this</span>.names = <span class="hljs-string">"anikin"</span>;
    &#125;
    <span class="hljs-built_in">this</span>.names = <span class="hljs-string">'zhangsan'</span>;
    test();
    
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>.name)  <span class="hljs-comment">// &#123;&#125;  zhangsan</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">global</span>.names) <span class="hljs-comment">// aninkin</span>
    
     <span class="hljs-comment">// 在打印一下看看这个this指向哪里呢</span>
     <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span> === <span class="hljs-built_in">module</span>.exports); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的代码分析得出几个结论：</p>
<ul>
<li>函数里面的<code>this</code>指向的是全局的 <code>global</code>。</li>
<li>整个运行文件里面的 <code>this</code>是指向 <code>module.exports</code>的。这个可以参考<a href="https://juejin.cn/post/6966614457603047431" target="_blank">模块化原理</a>。</li>
</ul>
<p>我们都知道 <code>exports = module.exports</code> ，是存在引用关系的，内存引用一般也是服从堆栈调用的规则。因此我们可以使用<code>this</code>来验证一下。</p>
<p>js 里面很基础的引用关系。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"anikin"</span> &#125;;
<span class="hljs-keyword">var</span> b = a;
a = &#123; <span class="hljs-attr">age</span>: <span class="hljs-number">23</span> &#125;;

<span class="hljs-built_in">console</span>.log(a, b); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果是： <code>&#123; age: 23 &#125;  &#123; name: "anikin" &#125;</code>。</p>
<p>所以验证下上面的<code>exports</code>的关系。新建文件<code>test.js</code>:</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span> === <span class="hljs-built_in">exports</span>);  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span> === <span class="hljs-built_in">module</span>.exports); <span class="hljs-comment">// true</span>

<span class="hljs-comment">//</span>
<span class="hljs-built_in">exports</span>.c = <span class="hljs-number">3</span>;
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
  <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>,
&#125;;
<span class="hljs-built_in">this</span>.m = <span class="hljs-number">5</span>;

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);  
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span> === <span class="hljs-built_in">exports</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span> === <span class="hljs-built_in">module</span>.exports);
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">module</span>.exports);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>以此输出结果是：</p>
<pre><code class="hljs language-js copyable" lang="js"> &#123; <span class="hljs-attr">c</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">m</span>: <span class="hljs-number">5</span> &#125;
<span class="hljs-literal">true</span>
<span class="hljs-literal">false</span>
&#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">2</span> &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>解释：在读取文件的时候,内部会调用访问文件函数：__temp.call</p>
<ul>
<li>
<p>在访问模块的时候<code>this</code>指向的是<code>module.exports</code>,而<code>module.exports</code>为一个空对象，<code>exports = module.exports</code>;所以为什么开头一开始问什么打印的全部都是空对象,<code>require</code>函数返回的是<code>module.exports</code>，此时返回的是一个空对象<code>&#123;&#125;</code>。</p>
</li>
<li>
<p><code>exports</code>值也是空对象<code>&#123;&#125;</code>，当给<code>exports</code>赋值时：<code>exports.c=3</code>;此时值为一个引用值，相当于改变了堆地址内的值，但是引用堆房间的地址不变，所以修改<code>exports</code>的值<code>module.exports</code>也会改变，还是空对象<code>&#123;c:3&#125;</code>,此时的<code>this</code>也是<code>&#123;c:3&#125;</code></p>
</li>
<li>
<p><code>module.exports=&#123;a:1,b:2&#125;</code>;现在是改变了值,就相当于在堆中创建了一个新地址引用，然后指向新的房间，</p>
</li>
</ul>
<p>所以<code>this</code>指向的还是原来的引用，故<code>this</code>与<code>module.exports</code>不相等，但是<code>this</code>和<code>exports</code>还是相等的</p>
<h2 data-id="heading-1">和浏览器相同的点：</h2>
<p>类似对象，类，已经箭头函数等的<code>this</code>可以参考浏览器端的实现。</p>
<p>例如箭头函数：<code>this</code>是在定义函数时绑定的，不是在执行过程中绑定的。简单的说，函数在定义时，this就继承了定义函数的对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Events = <span class="hljs-built_in">require</span>(<span class="hljs-string">"events"</span>);
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyEvent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Events</span> </span>&#123;&#125;
<span class="hljs-keyword">var</span> e1 = <span class="hljs-keyword">new</span> MyEvent();

e1.on(<span class="hljs-string">"start"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"start:event "</span>, <span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span> === e1);
&#125;);

e1.on(<span class="hljs-string">"start"</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"start:event "</span>, <span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span> === e1);
&#125;);

e1.emit(<span class="hljs-string">"start"</span>, <span class="hljs-string">"anikin"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行结果是：</p>
<pre><code class="hljs language-js copyable" lang="js"> anikin MyEvent <span class="hljs-literal">true</span>
 &#123;&#125; <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            