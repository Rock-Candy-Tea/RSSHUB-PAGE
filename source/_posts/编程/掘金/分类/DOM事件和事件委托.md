
---
title: 'DOM事件和事件委托'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4b50b5f54a748e09fd5b0f518573389~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 17 Apr 2021 00:23:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4b50b5f54a748e09fd5b0f518573389~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">DOM 事件模型及DOM 事件机制</h2>
<p>通俗理解，事件是用户或者浏览器自己执行的某种动作，是文档或者浏览器发生的一些交互瞬间，比如点击（click）按钮等，这里的click就是事件的名称。JS与html之间的交互是通过事件实现的，DOM支持大量的事件。</p>
<h3 data-id="heading-1">事件流</h3>
<p>规定的事件流有三个阶段： 事件捕获阶段，目标阶段，事件冒泡阶段。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4b50b5f54a748e09fd5b0f518573389~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>示例：</p>
<pre><code class="hljs language-js copyable" lang="js"> <div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"A"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"B"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"C"</span>></span>
        Click 
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">捕获</h4>
<p>捕获是从A -> B -> C；看有没有函数监听
由网景公司提出的：事件有父元素传递到子元素的过程就叫捕获</p>
<h4 data-id="heading-3">冒泡</h4>
<p>冒泡是从C -> B -> A；看有没有函数监听
由微软提出的：事件由子元素传递到父元素传递的过程，叫做冒泡</p>
<h4 data-id="heading-4">总结</h4>
<p>由外向内找监听函数叫事件捕获；
由内向外找监听函数叫事件冒泡。</p>
<h4 data-id="heading-5">W3C标准</h4>
<p>W3C标准：首先捕获，再冒泡
绑定在C的事件是按照代码的顺序发生的，其他非C元素则是通过冒泡或者捕获的触发。按照W3C的标准，先发生捕获事件，后发生冒泡事件。
所以事件的整体顺序是：
A元素捕获 -> B元素捕获 -> C元素代码顺序 -> B元素冒泡 -> A元素冒泡</p>
<h4 data-id="heading-6">事件绑定</h4>
<h5 data-id="heading-7">API addEventListener</h5>
<p>W3C: <code>baba.addEventListener('click',fn,bool)</code></p>
<p>如果不传bool值 默认为false，冒泡</p>
<p>如果 bool 值为 true， 捕获</p>
<h4 data-id="heading-8">target 与 currentTarget 区别</h4>
<p><code>e.target</code> 用户操作的元素
<code>e.currentTarget</code> 程序员监听的元素</p>
<h4 data-id="heading-9">取消冒泡</h4>
<p>捕获不能取消，冒泡可以 <code>e.stopPropagation</code> 中断冒泡</p>
<h2 data-id="heading-10">事件委托</h2>
<h4 data-id="heading-11">原理：DOM元素的事件冒泡</h4>
<p>事件委托是JavaScript中常用绑定事件的常用技巧，也叫事件代理(Event Delegation)，顾名思义，“事件委托”是把原本需要绑定在子元素的响应事件(click、keydown...)委托给父元素，让父元素担当事件监听的职务。</p>
<h4 data-id="heading-12">事件委托的优点</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"list"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>click1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>click2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>click3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    
    <span class="hljs-comment"><!--   ...  --></span>
    
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>clickn<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>可以节省内存占用，减少事件注册（比如在ul上代理所有li的click事件）</strong></li>
</ul>
<p>如上面代码所示，如果给每个 <code><li></code> 列表项都绑定一个函数，那对内存的消耗是非常大的，因此较好的解决办法就是将<code><li></code>元素的点击事件绑定到它的父元素<code><ul></code>身上，执行事件的时候再去匹配判断目标元素。</p>
<ul>
<li><strong>可以监听动态元素（监听目前不存在的元素的点击事件）</strong></li>
</ul>
<p>上述的例子中列表项<code><li></code>数量很少，我们给每个列表项都绑定了事件。</p>
<p>在很多时候，我们需要通过用户操作动态的增加或者删除列表项<code><li></code>元素，那么在每一次改变的时候都需要重新给新增的元素绑定事件，给即将删去的元素解绑事件。</p>
<p>如果用事件委托就没有这种麻烦，因为事件是绑定在父层，和目标元素的增减没有关系，执行到目标元素是在真正响应执行事件函数的过程中匹配的，所以使用事件在动态绑定事件的情况下可以减少很多重复性的工作。</p>
<p>示例：<a href="http://js.jirengu.com/lofareteni/1/edit?html,js,output" target="_blank" rel="nofollow noopener noreferrer">js.jirengu.com/lofareteni/…</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
  <span class="hljs-keyword">const</span> button = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'button'</span>)
  button.textContent=<span class="hljs-string">'click1'</span>
  div1.appendChild(button)
&#125;,<span class="hljs-number">1000</span>)

div1.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function">(<span class="hljs-params">e</span>)=></span>&#123;
  <span class="hljs-keyword">const</span> t =e.target
  <span class="hljs-keyword">if</span>(t.tagName.toLowerCase()===<span class="hljs-string">'button'</span>)&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'button被click'</span>)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">封装事件委托</h4>
<p>示例： <a href="http://js.jirengu.com/wapuposire/1/edit?html,js,output" target="_blank" rel="nofollow noopener noreferrer">js.jirengu.com/wapuposire/…</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> button = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'button'</span>)
  button.textContent = <span class="hljs-string">'click1'</span>
  div1.appendChild(button)
&#125;, <span class="hljs-number">1000</span>)

on(<span class="hljs-string">'click'</span>, <span class="hljs-string">'#div1'</span>, <span class="hljs-string">'button'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'button被点击了'</span>)
&#125;)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">on</span>(<span class="hljs-params">eventType, element, selector, fn</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!(element <span class="hljs-keyword">instanceof</span> Element)) &#123;
    element = <span class="hljs-built_in">document</span>.querySelector(element)
  &#125;
  element.addEventListener(eventType, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> t = e.target
    <span class="hljs-keyword">if</span> (t.matches(selector)) &#123;
      <span class="hljs-comment">//给元素添加一个监听，看当前的target是不是满足selector如果满足调用函数，不满足跳过</span>
      fn(e)
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">总结</h5>
<p>事件委托就是把事件监听放在祖先元素（如父元素、爷爷元素）上。
好处是：1 节约监听数量 2 可以监听动态生成的元素。</p>
<blockquote>
<p>引用了<a href="https://jirengu.com/" target="_blank" rel="nofollow noopener noreferrer">饥人谷</a>教学图片，代码</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            