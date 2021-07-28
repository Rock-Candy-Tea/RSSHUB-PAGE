
---
title: 'iframe相关及跨域解决方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd3fa621e383440ca00ee599353bf892~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 08:26:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd3fa621e383440ca00ee599353bf892~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>[toc]</p>
<h2 data-id="heading-0">获取iframe的window、document</h2>
<p>页面：</p>
<pre><code class="hljs language-html copyable" lang="html">
<span class="hljs-tag"><<span class="hljs-name">iframe</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"frameSon"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"frame"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300px"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"300px"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"http://b.laihua.com:4444"</span> <span class="hljs-attr">frameborder</span>=<span class="hljs-string">"1"</span>></span><span class="hljs-tag"></<span class="hljs-name">iframe</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>通过<code>contentDocument</code>或者<code>contentWindow</code>：</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">const</span> frame = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'frame'</span>)

<span class="hljs-keyword">const</span> fwindow = frame.contentWindow

<span class="hljs-keyword">const</span> fdoc1 = frame.contentDocument

<span class="hljs-keyword">const</span> fdoc2 = frame.contentWindow.document

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd3fa621e383440ca00ee599353bf892~tplv-k3u1fbpfcp-watermark.image" alt="20210724172850.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>通过<code>window.frames</code>和iframe的<code>name</code>属性.这种方式直接获取到的是<strong>iframe页面的window对象</strong>：</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">const</span> frame = <span class="hljs-built_in">window</span>.frames[<span class="hljs-string">'frameSon'</span>]

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`frame:`</span>,frame);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`frame.document:`</span>,frame.document);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7cc918c00df46bf84be4b71e6b8a5c7~tplv-k3u1fbpfcp-watermark.image" alt="20210724172625.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">读取或者调用iframe内部的方法</h2>
<p>如果要读取或者操作iframe中的内容，要确保在iframe加载完成后再进行操作，如果iframe还未加载完成就开始调用里面的方法或变量，会产生错误。判断iframe是否加载完成有两种方法：</p>
<ol>
<li>
<p>通过上面第一种方式获取到得iframe是iframeDOM元素，可以直接通过<code>frame.onload</code>回调来判断iframe加载完成</p>
</li>
<li>
<p>通过上面第一种方式获取到得iframe是iframe的window对象，但并没有onload方法，所以可以用当前页面的<code>window.onload</code>回调或者 <code>document.readyState=="complete"</code> 来判断</p>
</li>
</ol>
<p>例如，我们要调用子iframe中的<code>test</code>方法，两种方式：</p>
<p>第一种方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">const</span> frame = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'frame'</span>)

<span class="hljs-keyword">const</span> fdoc = frame.contentDocument || frame.contentWindow.document

frame.onload = <span class="hljs-function">() =></span> &#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`frame.contentWindow.test:`</span>, frame.contentWindow.test);

frame.contentWindow.test()

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二种方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">const</span> frame = <span class="hljs-built_in">window</span>.frames[<span class="hljs-string">'frameSon'</span>]

<span class="hljs-keyword">const</span> fdoc = frame.document

<span class="hljs-built_in">window</span>.onload = <span class="hljs-function">() =></span> &#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`frame.test:`</span>, frame.test);

frame.test()

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">主域相同、二级域名不同的两个页面获取对方dom导致的跨域问题</h2>
<p>主页面是<code>a.baidu.com</code>，以iframe的形式引入了<code>b.baidu.com</code>子页面。子页面中声明了一个全局方法<code>test</code>，在父页面中调用这个方法发现跨域了：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a518b8580ee476c98be4d9a16ed2677~tplv-k3u1fbpfcp-watermark.image" alt="20210724175304.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这种情况下，父页面和iframe主域相同，只是二级域名不同，可以通过两个页面同时同时把<code>document.domain</code>设置为相同的主域来解决：</p>
<blockquote>
<p>另外，通过给主域相同、二级域名不同的页面设置相同的<code>document.domain</code>，也可以解决cookie的跨域问题。Cookie 是服务器写入浏览器的一小段信息，只有同源的网页才能共享。但浏览器允许通过设置<code>document.domain</code>共享 Cookie。</p>
</blockquote>
<p>父页面：</p>
<pre><code class="hljs language-html copyable" lang="html">
<span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h1</span>></span>page1<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>

<span class="hljs-tag"><<span class="hljs-name">iframe</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"frameSon"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"frame"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300px"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"300px"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"http://b.baidu.com:4444"</span>

<span class="hljs-attr">frameborder</span>=<span class="hljs-string">"1"</span>></span><span class="hljs-tag"></<span class="hljs-name">iframe</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-built_in">document</span>.domain = <span class="hljs-string">'baidu.com'</span>

<span class="hljs-keyword">const</span> frame = <span class="hljs-built_in">window</span>.frames[<span class="hljs-string">'frameSon'</span>]

<span class="hljs-keyword">const</span> fdoc = frame.document

<span class="hljs-built_in">window</span>.onload = <span class="hljs-function">() =></span> &#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`frame.test:`</span>, frame.test);

frame.test()

&#125;

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>iframe子页面：</p>
<pre><code class="hljs language-html copyable" lang="html">
<span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h1</span>></span>page2d<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-built_in">document</span>.domain = <span class="hljs-string">'baidu.com'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`222:`</span>,<span class="hljs-number">222</span>);

&#125;

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用结果成功：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9896576ff304db599ec15f31da7ed44~tplv-k3u1fbpfcp-watermark.image" alt="20210724175939.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">两个页面域名完全不同</h2>
<p>如果两个网页不同源，就无法拿到对方的DOM。例如iframe引入和<code>window.open</code>方法打开的窗口，它们之间的窗口无法通信。</p>
<p>例如，父页面是<code>baidu.com</code>，子页面是<code>zijie.com</code>，父页面向调用子页面中的全局方法<code>test</code>。</p>
<p>子页面中声明了<code>test</code>全局方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`222:`</span>,<span class="hljs-number">222</span>);

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>父页面通过iframe引入子页面并尝试调用其<code>test</code>方法：</p>
<pre><code class="hljs language-html copyable" lang="html">
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h1</span>></span>page1<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>

<span class="hljs-tag"><<span class="hljs-name">iframe</span>

<span class="hljs-attr">name</span>=<span class="hljs-string">"frameSon"</span>

<span class="hljs-attr">id</span>=<span class="hljs-string">"frame"</span>

<span class="hljs-attr">src</span>=<span class="hljs-string">"http://zijie.com:4444"</span>

<span class="hljs-attr">width</span>=<span class="hljs-string">"300px"</span>

<span class="hljs-attr">height</span>=<span class="hljs-string">"300px"</span>

<span class="hljs-attr">frameborder</span>=<span class="hljs-string">"1"</span>></span>

<span class="hljs-tag"></<span class="hljs-name">iframe</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">const</span> frame = <span class="hljs-built_in">window</span>.frames[<span class="hljs-string">'frameSon'</span>]

<span class="hljs-keyword">const</span> fdoc = frame.document

<span class="hljs-built_in">window</span>.onload = <span class="hljs-function">() =></span> &#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`frame.test:`</span>, frame.test);

frame.test()

&#125;

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果报错跨域：</p>
<pre><code class="hljs language-bash copyable" lang="bash">
(index):54 Uncaught DOMException: Blocked a frame with origin <span class="hljs-string">"http://baidu.com:3333"</span> from accessing a cross-origin frame.

at window.onload (http://baidu.com:3333/:54:42)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4739ab97fe804970826e1bcac8e4ef14~tplv-k3u1fbpfcp-watermark.image" alt="20210724181519.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以通过<code>postMessage</code>、片段标识符、<code>window.name</code>来解决，下面主要介绍前两个：</p>
<h3 data-id="heading-4"><code>window.postMessage</code></h3>
<p><code>window.postMessage</code>方法允许跨窗口通信，不论这两个窗口是否同源。</p>
<p>大概的实现逻辑是：</p>
<p>一个窗口可以获得对另一个窗口的引用（比如iframe的contentWindow属性、执行window.open返回的窗口对象、或者是命名过或数值索引的window.frames），调用这个窗口引用上的<code>postMessage</code>方法分发一个MessageEvent 消息。然后子窗口中通过监听<code>message</code>事件来获取父窗口传递的消息即可。</p>
<p>子页面向父窗口发送消息同理，不同一点是子窗口可以通过<code>MessageEvent.source</code>来获取父窗口的引用。</p>
<p><strong>语法：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
otherWindow.postMessage(message, targetOrigin);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>otherWindow</code></strong> ：要给其发送消息的目标窗口的引用；</p>
<p><strong>第一个参数<code>message</code></strong> ： 具体的消息内容；</p>
<p><strong>第二个参数<code>targetOrigin</code></strong> ：<strong>指定哪些窗口能接收到消息事件。可以指定接收消息的窗口的源（origin），即"协议 + 域名 + 端口"。也可以设为"*"，表示不限制域名，向所有窗口发送。</strong> 在发送消息的时候，如果目标窗口的协议、主机地址或端口这三者的任意一项不匹配targetOrigin提供的值，那么消息就不会被发送；只有三者完全匹配，消息才会被发送。这个机制用来控制消息可以发送到哪些窗口。</p>
<p>监听<code>message</code>时间的时候，可以通过<code>MessageEvent</code>对象获取下面三个参数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
MessageEvent.source：发送消息的窗口引用

MessageEvent.origin: 发送消息的来源origin

MessageEvent.data: 消息内容

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>看一下如何通过<code>postMessage</code>解决上面出现的跨域问题：</strong></p>
<p>父页面可以获取到子页面的引用后，调用其<code>postMessage</code>方法并将需要调用的方法通过参数传递过去：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-built_in">window</span>.onload = <span class="hljs-function">() =></span> &#123;

frame.postMessage(&#123; <span class="hljs-attr">fn</span>: <span class="hljs-string">'test'</span> &#125;, <span class="hljs-string">"http://zijie.com:4444"</span>)

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>子页面中监听<code>message</code>时间，并对<code>event.origin</code>和<code>event.data</code>作出判断后，调用相应的方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`222:`</span>,<span class="hljs-number">222</span>);

&#125;

<span class="hljs-built_in">window</span>.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;

<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`e:`</span>,e);

<span class="hljs-keyword">if</span>(e.origin === <span class="hljs-string">'http://baidu.com:3333'</span> && e.data.fn === <span class="hljs-string">'test'</span>)&#123;

test()

&#125;

&#125;)

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行结果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b730dcd571f41e7815e8c7966ee30ff~tplv-k3u1fbpfcp-watermark.image" alt="20210725225754.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果子页面执行完方法需要向父页面作出通知，可以在子页面中<strong>通过<code>event.source</code>获取父页面的引用</strong>，调用其<code>poseMessage</code>方法，然后父页面中通过监听<code>message</code>时间实现。</p>
<p>子页面：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`222:`</span>,<span class="hljs-number">222</span>);

&#125;

<span class="hljs-built_in">window</span>.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;

<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`e:`</span>,e);

<span class="hljs-keyword">if</span>(e.origin === <span class="hljs-string">'http://baidu.com:3333'</span> && e.data.fn === <span class="hljs-string">'test'</span>)&#123;

test()

<span class="hljs-comment">// 向父页面发出通知</span>

e.source.postMessage(<span class="hljs-string">'执行完毕'</span>, <span class="hljs-string">'*'</span>)

&#125;

&#125;)

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>父页面：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-built_in">window</span>.onload = <span class="hljs-function">() =></span> &#123;

frame.postMessage(&#123; <span class="hljs-attr">fn</span>: <span class="hljs-string">'test'</span> &#125;, <span class="hljs-string">"http://zijie.com:4444"</span>)

<span class="hljs-comment">// 接受子页面通知</span>

<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`e.data:`</span>,e.data);

&#125;)

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行结果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/daf99a4d44714ab2b47e746aba5335f1~tplv-k3u1fbpfcp-watermark.image" alt="20210725230139.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>关于<code>postMessage</code>的安全问题</strong></p>
<p>如果不希望从其他网站接收message，不要为message事件添加任何事件侦听器。 这是一个完全万无一失的方式来避免安全问题。</p>
<p>如果确实希望从其他网站接收message，<strong>始终使用<code>MessageEvent.origin</code>和 <code>MessageEvent.source</code> 属性验证发件人的身份</strong>。 任何窗口（包括例如<a href="https://link.juejin.cn/?target=http%3A%2F%2Fevil.example.com%25EF%25BC%2589%25E9%2583%25BD%25E5%258F%25AF%25E4%25BB%25A5%25E5%2590%2591%25E4%25BB%25BB%25E4%25BD%2595%25E5%2585%25B6%25E4%25BB%2596%25E7%25AA%2597%25E5%258F%25A3%25E5%258F%2591%25E9%2580%2581%25E6%25B6%2588%25E6%2581%25AF%25EF%25BC%258C" target="_blank" rel="nofollow noopener noreferrer" title="http://evil.example.com%EF%BC%89%E9%83%BD%E5%8F%AF%E4%BB%A5%E5%90%91%E4%BB%BB%E4%BD%95%E5%85%B6%E4%BB%96%E7%AA%97%E5%8F%A3%E5%8F%91%E9%80%81%E6%B6%88%E6%81%AF%EF%BC%8C" ref="nofollow noopener noreferrer">evil.example.com）都可以向任何其他窗口发送消息，</a></p>
<p>当使用<code>postMessage</code>将数据发送到其他窗口时，始终指定精确的目标origin，而不是*。 恶意网站可以在我们不知情的情况下更改窗口的位置，因此它可以拦截使用postMessage发送的数据。</p>
<h3 data-id="heading-5">片段标识符fragment identifier</h3>
<p>片段标识符（fragment identifier）指的是<strong>URL的#号后面的部分</strong>。比如 “<a href="https://link.juejin.cn/?target=http%3A%2F%2Fexample.com%2Fx.html%23fragment%25E2%2580%259D" target="_blank" rel="nofollow noopener noreferrer" title="http://example.com/x.html#fragment%E2%80%9D" ref="nofollow noopener noreferrer">example.com/x.html#frag…</a> 的“#fragment”。如果只是改变片段标识符，页面不会重新刷新。</p>
<p>父页面把需要调用的方法以hash的形式加在iframe地址后面：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">const</span> frame = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'frame'</span>)

<span class="hljs-built_in">window</span>.onload = <span class="hljs-function">() =></span> &#123;

<span class="hljs-comment">// 通过hash改变iframe的src，不会导致刷新</span>

frame.src = <span class="hljs-string">`http://zijie.com:4444#test`</span>

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>子页面监听<code>hashchage</code>事件来获取当前地址的hash值：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`222:`</span>,<span class="hljs-number">222</span>);

&#125;

<span class="hljs-built_in">window</span>.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;

<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>, <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`e:`</span>,e);

<span class="hljs-comment">// 通过location.hash获取到父页面传递过来的信息</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`window.location.hash:`</span>,<span class="hljs-built_in">window</span>.location.hash);

<span class="hljs-keyword">const</span> fn = <span class="hljs-built_in">window</span>.location.hash.slice(<span class="hljs-number">1</span>)

<span class="hljs-built_in">eval</span>(fn)()

&#125;)

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f6188b7c1ce4f2da0701a97012441e9~tplv-k3u1fbpfcp-watermark.image" alt="20210725233902.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同样的，子窗口也可以改变父窗口的片段标识符。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
parent.location.href= target + <span class="hljs-string">"#"</span> + hash;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">REF</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fu011721501%2Farticle%2Fdetails%2F48877191" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/u011721501/article/details/48877191" ref="nofollow noopener noreferrer">(9条消息) postMessage安全性问题_Exploit的小站~-CSDN博客</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1rk4y127x8%2F%3Fspm_id_from%3D333.788.recommend_more_video.0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1rk4y127x8/?spm_id_from=333.788.recommend_more_video.0" ref="nofollow noopener noreferrer">前端跨域常见解决方案(包括反向代理)_哔哩哔哩_bilibili</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWindow%2FpostMessage" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Window/postMessage" ref="nofollow noopener noreferrer">window.postMessage - Web API 接口参考 | MDN</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jb51.net%2Farticle%2F116273.htm" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jb51.net/article/116273.htm" ref="nofollow noopener noreferrer">利用JS对iframe父子（内外）页面进行操作的方法教程_javascript技巧_脚本之家</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2016%2F04%2Fsame-origin-policy.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ruanyifeng.com/blog/2016/04/same-origin-policy.html" ref="nofollow noopener noreferrer">浏览器同源政策及其规避方法 - 阮一峰的网络日志</a></p></div>  
</div>
            