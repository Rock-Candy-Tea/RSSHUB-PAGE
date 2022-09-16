
---
title: '如何优雅地编写一个高逼格的JS插件惊艳你的领导和同事？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f6898609c354178a6a10e3a6a7a947d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 03:44:01 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f6898609c354178a6a10e3a6a7a947d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:30px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:60px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:24px 0 12px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li::marker,.markdown-body ul li::marker&#123;color:#a862ea&#125;.markdown-body ol li.task-list-item,.markdown-body ul li.task-list-item&#123;list-style:none&#125;.markdown-body ol li.task-list-item ol,.markdown-body ol li.task-list-item ul,.markdown-body ul li.task-list-item ol,.markdown-body ul li.task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body a,.markdown-body code,.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6,.markdown-body li,.markdown-body p&#123;opacity:.85;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body a:hover,.markdown-body code:hover,.markdown-body h1:hover,.markdown-body h2:hover,.markdown-body h3:hover,.markdown-body h4:hover,.markdown-body h5:hover,.markdown-body h6:hover,.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:1px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;transition:transform .2s ease 0s;background-color:#f8f5ff;box-shadow:0 0 10px #e7daff&#125;.markdown-body img:hover&#123;opacity:1;box-shadow:0 0 20px #e7daff;transform:translateY(-1px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:12px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:3px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body .math&#123;font-style:italic;margin:12px 0;padding:.5em 1em;background-color:#f8f5ff&#125;.markdown-body .math>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:18px;color:#383838;border-radius:2px;scroll-behavior:smooth;box-shadow:0 0 10px #e7daff&#125;.markdown-body pre>code:hover&#123;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;width:100%;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:.5em;border:1px solid #e7daff&#125;.markdown-body tr&#123;background-color:#f8f5ff&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>在一个风和日丽的早晨，我正悠闲地喝着Coffe，突然领导向我走来，我赶紧熟练地切出<strong>VSCode</strong>，淡定自若地问：领导，什么事？领导拍了拍我的肩膀：你上次封装的方法同事跟我反馈使用起来很不错啊，你不如做成<strong>JS插件</strong>给大家用吧。我放下了手中的掘金马克杯，甩了一下眼前仅剩的几根刘海，眼神坚定地回道：没问题啊领导，保证完成任务！</p>
<h1 data-id="heading-0">原型链写法</h1>
<p>要开始编写插件就得先了解<strong>JS模块化</strong>，早期的模块化是利用了<strong>函数自执行</strong>来实现的，在单独的函数作用域中执行代码可以避免插件中定义的变量污染到全局变量，举个栗子🌰，以下代码实现了一个简单随机数生成的插件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">;(<span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-variable language_">global</span></span>) &#123;
    <span class="hljs-string">"use strict"</span>;

    <span class="hljs-keyword">var</span> <span class="hljs-title class_">MyPlugin</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params">name</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">name</span> = name
    &#125;;

    <span class="hljs-title class_">MyPlugin</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span> = &#123;
        <span class="hljs-attr">say</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
            <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'欢迎你：'</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">name</span>)
        &#125;,
        <span class="hljs-attr">random</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params">min = <span class="hljs-number">0</span>, max = <span class="hljs-number">1</span></span>) &#123;
            <span class="hljs-keyword">if</span> (min <= <span class="hljs-title class_">Number</span>.<span class="hljs-property">MAX_SAFE_INTEGER</span> && max <= <span class="hljs-title class_">Number</span>.<span class="hljs-property">MAX_SAFE_INTEGER</span>) &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">floor</span>(<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>() * (max - min + <span class="hljs-number">1</span>)) + min
            &#125;
        &#125;
    &#125;;
    
    <span class="hljs-comment">// 函数自执行将 this（全局下为window）传入，并在其下面挂载方法</span>
    <span class="hljs-variable language_">global</span>.<span class="hljs-property">MyPlugin</span> = <span class="hljs-title class_">MyPlugin</span>;
    <span class="hljs-comment">// 兼容CommonJs规范导出</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-variable language_">module</span> !== <span class="hljs-string">'undefined'</span> && <span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span>) <span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = <span class="hljs-title class_">MyPlugin</span>; 
&#125;)(<span class="hljs-variable language_">this</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接使用 <strong>script</strong> 标签引入该插件，接着 <code>new</code> 一个实例就能使用插件啦：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> aFn = <span class="hljs-keyword">new</span> <span class="hljs-title class_">MyPlugin</span>()

<span class="hljs-keyword">var</span> num = aFn.<span class="hljs-title function_">random</span>(<span class="hljs-number">10</span>, <span class="hljs-number">20</span>)
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(num) <span class="hljs-comment">// 打印一个 10~20 之间的随机数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">闭包式写法</h1>
<p>上面的插件使用时如果调用 <code>say</code> 方法，会打印方法中的欢迎字样，并显示初始化的 <code>name</code> 值：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> aFn = <span class="hljs-keyword">new</span> <span class="hljs-title class_">MyPlugin</span>(<span class="hljs-string">'呀哈哈'</span>)
aFn.<span class="hljs-title function_">say</span>() <span class="hljs-comment">// 欢迎你: 呀哈哈</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但由于属性能被直接访问，插件中的变量就可以随意修改，这可能是我们不想看到的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> aFn = <span class="hljs-keyword">new</span> <span class="hljs-title class_">MyPlugin</span>(<span class="hljs-string">'呀哈哈'</span>)
aFn.<span class="hljs-property">name</span> = <span class="hljs-literal">null</span>
aFn.<span class="hljs-title function_">say</span>() <span class="hljs-comment">// 欢迎你: null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么如果要创建<strong>私有变量</strong>，可以利用<strong>JS闭包</strong>原理来编写插件，我们使用<strong>工厂模式</strong>来创建函数，再举个栗子🌰，如下代码实现了一个简单正则校验的插件：</p>
<pre><code class="hljs language-js copyable" lang="js">; (<span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-variable language_">global</span></span>) &#123;
    <span class="hljs-string">"use strict"</span>;

    <span class="hljs-keyword">var</span> <span class="hljs-title class_">MyPlugin</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) &#123;
        <span class="hljs-keyword">var</span> val = value
        <span class="hljs-keyword">var</span> reg = &#123;
            <span class="hljs-attr">phone</span>: <span class="hljs-regexp">/^1[3456789]\d&#123;9&#125;$/</span>,
            <span class="hljs-attr">number</span>: <span class="hljs-regexp">/^-?\d*\.?\d+$/</span>
        &#125;;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-title function_">getRegs</span>(<span class="hljs-params"></span>) &#123;
                <span class="hljs-keyword">return</span> reg
            &#125;,
            <span class="hljs-title function_">setRegs</span>(<span class="hljs-params">params</span>) &#123;
                reg = &#123; ...reg, ...params &#125;
            &#125;,
            <span class="hljs-title function_">isPhone</span>(<span class="hljs-params"></span>) &#123;
                reg.<span class="hljs-property">phone</span>.<span class="hljs-title function_">test</span>(val) && <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'这是手机号'</span>)
                <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>
            &#125;,
            <span class="hljs-title function_">isNumber</span>(<span class="hljs-params"></span>) &#123;
                reg.<span class="hljs-property">number</span>.<span class="hljs-title function_">test</span>(val) && <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'这是数字'</span>)
                <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>
            &#125;
        &#125;;
    &#125;;

    <span class="hljs-comment">// 函数自执行将 this（全局下为window）传入，并在其下面挂载方法</span>
    <span class="hljs-variable language_">global</span>.<span class="hljs-property">MyPlugin</span> = <span class="hljs-title class_">MyPlugin</span>;
    <span class="hljs-comment">// 兼容CommonJs规范导出</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-variable language_">module</span> !== <span class="hljs-string">'undefined'</span> && <span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span>) <span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = <span class="hljs-title class_">MyPlugin</span>;
&#125;)(<span class="hljs-variable language_">this</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时我们再调用插件，其内部的变量是不可访问的，只能通过插件<strong>内部的方法查看/修改</strong>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> aFn = <span class="hljs-keyword">new</span> <span class="hljs-title class_">MyPlugin</span>()

<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>( aFn.<span class="hljs-property">reg</span> ) <span class="hljs-comment">// undefined</span>

<span class="hljs-keyword">var</span> reg = aFn.<span class="hljs-title function_">getRegs</span>()
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>( reg ) <span class="hljs-comment">// &#123;"phone":&#123;....&#125;,"number":&#123;.....&#125;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中我们在 <code>isPhone</code> <code>isNumber</code> 方法的最后都返回了 <code>this</code>，这是为了实现如下的链式调用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> aFn = <span class="hljs-keyword">new</span> <span class="hljs-title class_">MyPlugin</span>(<span class="hljs-number">13800138000</span>)

aFn.<span class="hljs-title function_">isPhone</span>().<span class="hljs-title function_">isNumber</span>() <span class="hljs-comment">// log: > 这是手机号 > 这是数字</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">仿 JQuery 写法</h1>
<p>这种写法是仿造<strong>JQ</strong>实现的一种编写模式，可以省去调用时<code>new</code>实例化的步骤，并实现类似 <code>$(xxx).someFn(....)</code> 这样的调用方法，在需要频繁<strong>DOM</strong>操作的时候就很适合这么编写插件。笔者以前会在小项目中自己实现一些类<strong>JQ</strong>选择器操作的功能插件，来避免引入整个<strong>JQ</strong>，实现插件的核心思路如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> <span class="hljs-title class_">Fn</span> = <span class="hljs-title class_">Function</span>(params) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Fn</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-title function_">init</span>(params)
&#125;

<span class="hljs-title class_">Fn</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span> = &#123;
    <span class="hljs-attr">init</span>: <span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) &#123;&#125;
&#125;

<span class="hljs-title class_">Fn</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">init</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span> = <span class="hljs-title class_">Fn</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>可以看出核心是对<strong>JS原型链</strong>的极致利用，首先主动对其原型上的<code>init</code>方法进行实例化并返回，<code>init</code>相当于构造函数的效果，而此时返回的实例里并没有包含<code>Fn</code>的方法，我们调用时<strong>JS</strong>自然就会从<code>init</code>的原型对象上去查找，于是最终<code>init</code>下的原型才又指向了<code>Fn</code>的原型，通过这种"套娃"的手法，使得我们能够不通过实例化<code>Fn</code>又能正确地访问到<code>Fn</code>下的原型对象。</p>
</blockquote>
<p>说了这么多，还是举个栗子🌰，以下代码实现了一个简单的样式操作插件：</p>
<pre><code class="hljs language-js copyable" lang="js">;(<span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-variable language_">global</span></span>) &#123;
  <span class="hljs-string">"use strict"</span>;

  <span class="hljs-keyword">var</span> <span class="hljs-title class_">MyPlugin</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params">el</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">MyPlugin</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-title function_">init</span>(el)
  &#125;;

  <span class="hljs-title class_">MyPlugin</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span> = &#123;
    <span class="hljs-attr">init</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params">el</span>) &#123;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">el</span> = <span class="hljs-keyword">typeof</span> el === <span class="hljs-string">"string"</span> ? <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">querySelector</span>(el) : el;
    &#125;,
    <span class="hljs-attr">setBg</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params">bg</span>) &#123;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">el</span>.<span class="hljs-property">style</span>.<span class="hljs-property">background</span> = bg;
      <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>
    &#125;,
    <span class="hljs-attr">setWidth</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params">w</span>) &#123;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">el</span>.<span class="hljs-property">style</span>.<span class="hljs-property">width</span> = w;
      <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>
    &#125;,
    <span class="hljs-attr">setHeight</span>: <span class="hljs-keyword">function</span> (<span class="hljs-params">h</span>) &#123;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">el</span>.<span class="hljs-property">style</span>.<span class="hljs-property">height</span> = h;
      <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>
    &#125;
  &#125;;

  <span class="hljs-title class_">MyPlugin</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">init</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span> = <span class="hljs-title class_">MyPlugin</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>
  <span class="hljs-comment">// script标签引入插件后全局下挂载一个_$的方法</span>
  <span class="hljs-variable language_">global</span>.<span class="hljs-property">_$</span> = <span class="hljs-title class_">MyPlugin</span>;
&#125;)(<span class="hljs-variable language_">this</span> || <span class="hljs-variable language_">window</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用演示：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 页面元素 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>hello world<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为元素设置背景：</p>
<pre><code class="hljs language-ruby copyable" lang="ruby">_<span class="hljs-variable">$(</span><span class="hljs-string">'#app'</span>).setBg(<span class="hljs-string">'#ff0'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f6898609c354178a6a10e3a6a7a947d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为元素设置背景并改变宽高：</p>
<pre><code class="hljs language-ruby copyable" lang="ruby">_<span class="hljs-variable">$(</span><span class="hljs-string">'#app'</span>).setBg(<span class="hljs-string">'#ff0'</span>).setHeight(<span class="hljs-string">'100px'</span>).setWidth(<span class="hljs-string">'200px'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6b10eab0fff4a48b0751b6f3cb606bc~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">工程化插件</h1>
<p>前面讲的插件编写方法已经足够优雅了，但还不够逼格，假设以后会有多人同时开发的情况，仅靠一个<strong>JS</strong>维护大型插件肯定是独木难支，这时候就需要组件化把颗粒度打细，将插件拆分成多个文件，分别负责各自的功能，最终再打包成一个文件引用。如今<strong>ES</strong>模块化已经可以轻松应对功能拆分了，所以我们只需要一个打包器，<strong>Rollup.js</strong> 就是不错的选择，有了它我们可以更优雅地编写插件，它会帮我们打包。许多大型框架例如 <strong>Vue</strong>、<strong>React</strong> 都是用它打包的。</p>
<blockquote>
<p>Rollup 是一个用于 JavaScript 的模块打包器，它将小段代码编译成更大更复杂的东西，例如库或应用程序。<a href="https://link.juejin.cn/?target=https%3A%2F%2Frollupjs.org%2Fguide%2Fen%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://rollupjs.org/guide/en/" ref="nofollow noopener noreferrer">官网链接</a></p>
</blockquote>
<p>下面我们一步步实现这个工程化的插件，没有那么复杂，先创建一个目录：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">mkdir</span> -p my-project/src
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着运行 <code>npm init</code> 进行项目初始化，一路回车，接着为项目安装 <strong>Rollup</strong>：</p>
<pre><code class="hljs language-css copyable" lang="css">npm install <span class="hljs-attr">--save-dev</span> rollup
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根目录下创建入口文件 <strong>index.js</strong>，以及 <strong>src</strong>下的<strong>main.js</strong>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> main <span class="hljs-keyword">from</span> <span class="hljs-string">'./src/main.js'</span>;

<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(main);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/main.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-string">'hello world!'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根目录下创建 <code>rollup.config.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> babel <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-babel'</span>
<span class="hljs-keyword">import</span> commonjs <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-commonjs'</span>
<span class="hljs-keyword">import</span> resolve <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-node-resolve'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">input</span>: <span class="hljs-string">'index.js'</span>,
  <span class="hljs-attr">output</span>: [
    &#123;
      <span class="hljs-attr">file</span>: <span class="hljs-string">'dist/main.umd.js'</span>,
      <span class="hljs-attr">format</span>: <span class="hljs-string">'umd'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'bundle-name'</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">file</span>: <span class="hljs-string">'dist/main.es.js'</span>,
      <span class="hljs-attr">format</span>: <span class="hljs-string">'es'</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">file</span>: <span class="hljs-string">'dist/main.cjs.js'</span>,
      <span class="hljs-attr">format</span>: <span class="hljs-string">'cjs'</span>,
    &#125;,
  ],
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-title function_">babel</span>(&#123;
      <span class="hljs-attr">exclude</span>: <span class="hljs-string">'node_modules/**'</span>,
    &#125;),
    <span class="hljs-title function_">resolve</span>(&#123;
      <span class="hljs-attr">jsnext</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">main</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">browser</span>: <span class="hljs-literal">true</span>,
    &#125;),
    <span class="hljs-title function_">commonjs</span>(),
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>稍微解释上面配置的插件：</p>
<p><code>babel</code>：将最终代码编译成 <strong>es5</strong>，我们的开发代码可以不用处理兼容性。</p>
<p><code>resolve</code>、<code>commonjs</code>：用于兼容可以依赖 <strong>commonjs</strong> 规范的包。</p>
</blockquote>
<p>把上面的依赖安装一下：</p>
<pre><code class="hljs language-scss copyable" lang="scss">npm install <span class="hljs-attr">--save-dev</span> <span class="hljs-keyword">@babel</span>/core <span class="hljs-keyword">@babel</span>/preset-env rollup-plugin-babel<span class="hljs-keyword">@latest</span> rollup-plugin-node-resolve rollup-plugin-commonjs
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <strong>package.json</strong>，增加一条脚本命令：</p>
<pre><code class="hljs language-erlang copyable" lang="erlang">.......
<span class="hljs-string">"scripts"</span>: &#123;
    ......
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"rollup -c -w"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行 <code>npm run dev</code> 看看效果吧：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0d0fb40554947d8a5e3d19a5edb9cf7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>













<table><thead><tr><th>打包文件</th><th>测试运行</th></tr></thead><tbody><tr><td><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f0853ca1723411285874f51f0c93407~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></td><td><code>node dist/main.cjs.js</code>: <br> <img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62546144ecca4644a2dfe3a59cce76b9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></td></tr></tbody></table>
<h3 data-id="heading-4">打包文件格式说明</h3>
<ol>
<li><strong>umd</strong></li>
</ol>
<p>集合了 <strong>CommonJS</strong>、<strong>AMD</strong>、<strong>CMD</strong>、<strong>IIFE</strong> 为一体的打包模式，看看上面的 <strong>hello world</strong> 会被打包成什么：</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-variable language_">global</span>, factory</span>) &#123;
    <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">exports</span> === <span class="hljs-string">'object'</span> && <span class="hljs-keyword">typeof</span> <span class="hljs-variable language_">module</span> !== <span class="hljs-string">'undefined'</span> ? <span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = <span class="hljs-title function_">factory</span>() :
    <span class="hljs-keyword">typeof</span> define === <span class="hljs-string">'function'</span> && define.<span class="hljs-property">amd</span> ? <span class="hljs-title function_">define</span>(factory) :
    (<span class="hljs-variable language_">global</span> = <span class="hljs-keyword">typeof</span> globalThis !== <span class="hljs-string">'undefined'</span> ? globalThis : <span class="hljs-variable language_">global</span> || self, <span class="hljs-variable language_">global</span>[<span class="hljs-string">"bundle-name"</span>] = <span class="hljs-title function_">factory</span>());
&#125;)(<span class="hljs-variable language_">this</span>, (<span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123; <span class="hljs-string">'use strict'</span>;

    .....代码省略.....
    
    <span class="hljs-keyword">return</span> xxxxxxxx;
&#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出导出的文件就是我们前面一直使用的<strong>函数自执行</strong>开发方式，其中加了各种兼容判断代码将在哪个环境下导入。</p>
<ol start="2">
<li><strong>es</strong></li>
</ol>
<p>现代JS的标准，导出的文件只能使用 <strong>ES模块化</strong> 方式导入。</p>
<ol start="3">
<li><strong>cjs</strong></li>
</ol>
<p>这个是指 <strong>CommonJS</strong> 规范导出的格式，只可在 <strong>Node</strong> 环境下导入。</p>
<h1 data-id="heading-5">补充：模块化的发展</h1>
<ul>
<li>早期利用<strong>函数自执行</strong>实现，在单独的函数作用域中执行代码（如 JQuery ）</li>
<li><strong>AMD</strong>：引入 <code>require.js</code> 编写模块化，引用依赖必须提前声明</li>
<li><strong>CMD</strong>：引入 <code>sea.js</code> 编写模块化，特点是可以动态引入依赖</li>
<li><strong>CommonJS</strong>：NodeJs 中的模块化，只在服务端适用，是同步加载</li>
<li><strong>ES Modules</strong>：ES6 中新增的模块化，是目前的主流</li>
</ul>
<p>本文前三种插件编写方式均属于利用函数自执行（<strong>IIFE</strong>）实现的插件，同时在向全局注入插件时兼容了 <strong>CommonJS</strong> 规范，但并未兼容 AMD CMD，是因为目前基本没有项目会使用到这两种模块化。</p>
<h1 data-id="heading-6">自动化API文档</h1>
<p>私以为一个好的 <strong>JS</strong> 插件决不能没有一份文档，如果别人使用你的插件，他不可能去查看源码才知道这个插件有哪些方法，是做什么的，要传哪些参数等。这里我们使用 <strong>JSDoc</strong> 来创建 <strong>API文档</strong>，它使用简单，只需要在代码中编写规范的<strong>注释</strong>，即能根据注释自动生成文档，一举多得，非常优雅！</p>
<pre><code class="hljs language-arduino copyable" lang="arduino">npm install --save-dev jsdoc open
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <strong>package.json</strong>，增加一条脚本命令：</p>
<pre><code class="hljs language-erlang copyable" lang="erlang">.......
<span class="hljs-string">"scripts"</span>: &#123;
    ......
    <span class="hljs-string">"doc"</span>: <span class="hljs-string">"jsdoc dist/main.es.js && node server.js"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根目录下创建文件 <strong>server.js</strong>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> open = <span class="hljs-built_in">require</span>(<span class="hljs-string">'open'</span>);
<span class="hljs-title function_">open</span>(<span class="hljs-string">`out/index.html`</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，现在可以使用 <code>npm run doc</code> 命令来生成文档了，依然是举个栗子🌰，我们在<strong>src</strong>目录下添加一个文件 <code>ArrayDelSome.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 *
 * <span class="hljs-doctag">@desc</span> 对象数组去重
 * <span class="hljs-doctag">@param</span> &#123;<span class="hljs-type">Array</span>&#125; <span class="hljs-variable">arr</span>
 * <span class="hljs-doctag">@param</span> &#123;<span class="hljs-type">String</span>&#125; 对象中相同的关键字(如id)
 * <span class="hljs-doctag">@return</span> &#123;<span class="hljs-type">Array</span>&#125; 返回新数组，eg: ArrayDelSome([&#123;id: 1&#125;,&#123;id: 2&#125;,&#123;id: 1&#125;], 'id') -> 返回: [&#123;id: 1&#125;,&#123;id: 2&#125;]
 */</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">ArrayDelSome</span>(<span class="hljs-params">arr, key</span>) &#123;
  <span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Map</span>()
  <span class="hljs-keyword">return</span> arr.<span class="hljs-title function_">filter</span>(<span class="hljs-function">(<span class="hljs-params">x</span>) =></span> !map.<span class="hljs-title function_">has</span>(x[key]) && map.<span class="hljs-title function_">set</span>(x[key], <span class="hljs-literal">true</span>))
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">ArrayDelSome</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>本例只演示最基础的用法，<strong>JSDoc</strong>有许多类型注释大家可以自行搜索学习下，不过本例最基本的这几个注释依旧是够用的。</p>
</blockquote>
<p>运行 <code>npm run doc</code>，将会打开一个网页，查看我们刚写的工具函数：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/921973979c6a4115bb9110b2391a81bb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-7">发布插件</h1>
<p>还没发布过npm包？<a href="https://juejin.cn/post/6979531144043692039/" target="_blank" title="https://juejin.cn/post/6979531144043692039/">参考这篇文章</a>。</p>
<h3 data-id="heading-8">私有源发布</h3>
<p>如果你的公司有私域npm管理源，或者平时喜欢用淘宝源，推荐使用 <code>nrm</code> 进行切换：</p>
<pre><code class="hljs language-css copyable" lang="css">npm <span class="hljs-selector-tag">i</span> nrm -g
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>查看源: <code>nrm ls</code></li>
<li>添加源: <code>nrm add name http//:xxx.xxx.xxx.xxx:4873/</code></li>
<li>删除源: <code>nrm del name</code></li>
<li>使用指定源: <code>nrm use npm</code></li>
</ol>
<h1 data-id="heading-9">总结</h1>
<p>功能较简单的<strong>JS</strong>插件我们可以直接采用前三种方式开发，如果涉及<strong>DOM</strong>操作较多，可以编写仿<strong>JQ</strong>的插件更好用，如果插件功能较多，有可能形成长期维护的大型插件，那么可以采用工程化的方式开发，方便多人协作，配套生成文档也利于维护。</p>
<h1 data-id="heading-10">往期精彩</h1>
<p><a href="https://juejin.cn/post/7142672017262084103" target="_blank" title="https://juejin.cn/post/7142672017262084103"># 语义化 HTML 编写一个原生 Web Components 组件</a></p>
<p><a href="https://juejin.cn/post/7142273336280612877" target="_blank" title="https://juejin.cn/post/7142273336280612877"># CSS 容器查询来了，你不能错过的10个精彩案例分享！</a></p>
<p><a href="https://juejin.cn/post/7130089643256578078" target="_blank" title="https://juejin.cn/post/7130089643256578078"># 给掘金写了个有趣又好玩的一键三连插件 | 仿B站效果</a></p>
<p><a href="https://juejin.cn/post/7139739843776806942" target="_blank" title="https://juejin.cn/post/7139739843776806942"># 时隔一年多 jQuery 再度发布新版本，你还在用JQ吗？</a></p></div>  
</div>
            