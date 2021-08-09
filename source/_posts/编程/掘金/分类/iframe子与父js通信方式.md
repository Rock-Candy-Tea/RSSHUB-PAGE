
---
title: 'iframe子与父js通信方式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6091'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 01:20:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=6091'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<p>在写微前端时 登陆页是iframe来写的 登陆 这就需要iframe通信。</p>
<p><strong>iframe</strong>框架中的页面与主页面之间的通信方式根据iframe中src属性是同域链接还是跨域链接，有明显不同的通信方式，同域下的数据交换和DOM元素互访就简单的多了，而跨域的则需要一些巧妙的方式来实现通信。</p>
<h2 data-id="heading-0">同域下父子页面的通信</h2>
<p><strong>父页面 parent.html</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>/></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span>(<span class="hljs-params"></span>) </span>&#123;
            alert(<span class="hljs-string">"parent.html------>I'm at parent.html"</span>);
        &#125;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callChild</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-comment">//document.frames["myFrame"].window.say();//只适用于ie浏览器</span>
            myFrame.window.say();
            myFrame.window.document.getElementById(<span class="hljs-string">"button"</span>).value = <span class="hljs-string">"我变了"</span>;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">button</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"调用child.html中的函数say()"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"callChild()"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">iframe</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"myFrame"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"child.html"</span>></span><span class="hljs-tag"></<span class="hljs-name">iframe</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>子页面 child.html</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span>(<span class="hljs-params"></span>) </span>&#123;
            alert(<span class="hljs-string">"child.html--->I'm at child.html"</span>);
        &#125;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callParent</span>(<span class="hljs-params"></span>) </span>&#123;
            parent.say();
            parent.window.document.getElementsByName(<span class="hljs-string">"myFrame"</span>)[<span class="hljs-number">0</span>].style.height = <span class="hljs-string">"100px"</span>;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">button</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"调用parent.html中的say()函数"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"callParent()"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">方法调用</h3>
<p>如上面示例所示父页面调用子页面的方法可通过：FrameName.window.childMethod();(这种方式兼容各种浏览器)
子页面调用父页面的方法：parent.window.parentMethod();</p>
<h3 data-id="heading-2">DOM元素访问</h3>
<p>根据FrameName.window得到了子窗口对象之后，再访问其中的DOM元素就跟访问同一页面中的DOM元素没区别了都可以通过document.getElementById(),document.getElementsByName()[index]。如：parent.window.document.getElementsByName("myFrame")[0],myFrame.window.document.getElementById("button")其中的window都是可以省略的。</p>
<h3 data-id="heading-3">注意事项</h3>
<p>要确保在Iframe加载完成后再进行操作，如果Iframe还未加载完成就开始调用里面的方法或变量，无疑会产生错误。判断Iframe是否加载完毕有两种方法：
1.在Iframe上用onload事件;
2.用document.readyState=="complete"来判断</p>
<h2 data-id="heading-4">二、跨域父子页面通信方法</h2>
<p>如果iframe所链接的是外部页面，因为安全机制则不能使用同域名下的通信方式了。</p>
<h3 data-id="heading-5">父页面向子页面传递数据</h3>
<p>实现的技巧就是利用 location 对象的 hash 值，通过它传递通信数据，我们只需要在父页面设置 iframe的 src 后面多加个#data 字符串（data就是你要传递的数据），然后在 子页面 中通过某种方式能即时的获取到这儿 data 就可以了，其实常用的一种方式就是：</p>
<ol>
<li>在 子页面 中通过 setInterval 方法设置定时器， 监听 location.href 的变化即可获得上面的 data 信息</li>
<li>然后 子页面 就能根据这个 data 信息进行相应的逻辑处理。</li>
<li></li>
</ol>
<h3 data-id="heading-6">子页面向父页面传递数据</h3>
<p>实现的技巧就是利用一个代理 Iframe C，它嵌入到 子页面中，并且和父页面必须保持是同域，然后我们通过它充分利用上面第一种通信方式的实现原理就能把 子页面的数据传递给 iframeC，接下来的问题就是怎么让iframeC把数据传递给主页面A ，因为，iframeC 和主页面是同域的，所以它们之间传递数据就变得简单多了，属于同域名下的通信问题了，如前面所讨论的，在这里的可以使用一个经常使用的属性 window.top (也可以使用window.parent.parent)，它返回对载入浏览器得最顶层 window 对象的引用，这样我们就能直接条用父页面中方法。</p></div>  
</div>
            