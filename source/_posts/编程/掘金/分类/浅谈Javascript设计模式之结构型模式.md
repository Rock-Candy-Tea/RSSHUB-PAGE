
---
title: '浅谈Javascript设计模式之结构型模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be41696a42aa4c19a9d8f397ed30a2fb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 18:15:54 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be41696a42aa4c19a9d8f397ed30a2fb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 10 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>今天我们主要来聊聊设计模式中的结构型模式。</p>
<h2 data-id="heading-1">适配器模式（Adapter Pattern）</h2>
<p>适配器模式可用来在现有接口和不兼容的类之间进行适配，使用这种模式的对象又叫包装器。像日常业务开发过程中，需要和后端对接接口，然后再实现自身的业务逻辑。但是当后端API规格发生变化的时候，我们可能需要又改接口又改业务逻辑，整体将变得不可控。这时候，使用适配器模式就可以解决这一问题。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getList</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// 请求后端API，并实现前端逻辑</span>
    fetch(<span class="hljs-string">'/api'</span>).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> data = Adapter(res.data);
        <span class="hljs-comment">// TODO</span>
    &#125;)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Adapter</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-keyword">for</span>() &#123;
        <span class="hljs-comment">// TODO</span>
    &#125;
    <span class="hljs-keyword">return</span> data
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当后端API发生调整的时候，我们只需要调整适配器代码Adapter，而不需要改动业务逻辑代码。</p>
<h2 data-id="heading-2">桥接模式（Bridge Pattern）</h2>
<p>将抽象部分与它的实现部分分离，使他们都可以独立的变化。 也就是说，桥接模式里面有两个角色：</p>
<ul>
<li>扩充抽象类</li>
<li>具体实现类</li>
</ul>
<p>最简单的桥接模式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> each = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">arr, fn</span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
        <span class="hljs-keyword">var</span> val = arr[i];
        <span class="hljs-keyword">if</span> (fn.call(val, i, val, arr)) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
        &#125;
    &#125;
&#125;;
<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
each(arr, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">i, v</span>) </span>&#123;
    arr[i] = v * <span class="hljs-number">2</span>;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>each函数是一个抽象类，而fn函数则是具体的实现，在这段代码中，抽象部分和实现部分的更改是互不影响的，可以独立的改变，所以，这个例子虽然简单，但是是一个典型的桥接模式的应用。</p>
<h2 data-id="heading-3">过滤器模式（Filter、Criteria Pattern）</h2>
<p>这种模式Javascript已经实现了，就是我们经常用的filter函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>].filter(<span class="hljs-function">(<span class="hljs-params">currentValue,index,arr</span>) =></span> <span class="hljs-literal">true</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>currentValue:必须。当前元素的值</li>
<li>index:可选。当前元素的索引值</li>
<li>arr:可选。当前元素属于的数组对象</li>
</ul>
<h2 data-id="heading-4">组合模式（Composite Pattern）</h2>
<p>像一般的面向对象语言，都会实现继承这个特性，但比如像Go，需要通过组合而并非继承。继承这种模式有很多弊端，因为和本章讨论内容无关，这里就不再赘述。这种模式在写Vue、React的时候接触的会比较多，可能你自己都没有意识到这是一种组合模式。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">A</span> /></span>
            <span class="hljs-tag"><<span class="hljs-name">B</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span> 
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组合模式将对象组合成树形结构，以表示“部分-整体”的层次结构。除了用来表示树形结构之外，组合模式的另一个好处是通过对象的多态性表现，使得用户对单个对象和组合对象的使用具有一致性。</p>
<h2 data-id="heading-5">装饰器模式（Decorator Pattern）</h2>
<p>大家应该使用过mixin（混入）功能，在Vue、React中也有出现。装饰器是旨在提升重用性能的一种结构性设计模式。</p>
<p>它们能够被用来在不需要深度改变使用它们的对象的依赖代码的前提下，变更我们希望向其中附加功能的现有系统之中。开发者使用它们的一个通常的理由是，它们的应用程序也许包含了需要大量彼此不相干类型对象的特性。想象一下不得不要去定义上百个不同对象的构造器，比方说，一个Javascript游戏。</p>
<p>javascript语言动态改变对象相当容易，可以直接改写对象或者对象的某个方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Function</span>.prototype.before = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"> beforefn </span>)</span>&#123;
 <span class="hljs-keyword">var</span> __self = <span class="hljs-built_in">this</span>; <span class="hljs-comment">// 保存原函数的引用</span>
 <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123; <span class="hljs-comment">// 返回包含了原函数和新函数的"代理"函数</span>
 beforefn.apply( <span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span> ); <span class="hljs-comment">// 执行新函数，且保证 this 不被劫持，新函数接受的参数</span>
 <span class="hljs-comment">// 也会被原封不动地传入原函数，新函数在原函数之前执行</span>
 <span class="hljs-keyword">return</span> __self.apply( <span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span> ); <span class="hljs-comment">// 执行原函数并返回原函数的执行结果，</span>
 <span class="hljs-comment">// 并且保证 this 不被劫持</span>
 &#125;
&#125;
<span class="hljs-built_in">Function</span>.prototype.after = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"> afterfn </span>)</span>&#123;
 <span class="hljs-keyword">var</span> __self = <span class="hljs-built_in">this</span>;
 <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
 <span class="hljs-keyword">var</span> ret = __self.apply( <span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span> );
 afterfn.apply( <span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span> );
 <span class="hljs-keyword">return</span> ret;
 &#125;
&#125;; 

work.after(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'work:17:00 - 21:00'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后打波小广告，美团校招社招内推，不限部门，不限岗位，不限投递数量，海量hc，快来快来～</p>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be41696a42aa4c19a9d8f397ed30a2fb~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7f4402074084153af2afb2f2140a66f~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer"></div>  
</div>
            