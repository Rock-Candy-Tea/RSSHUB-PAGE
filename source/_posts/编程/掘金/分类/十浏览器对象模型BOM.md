
---
title: '十.浏览器对象模型BOM'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46409f6ada144b558d27c566e240f9c7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 25 May 2021 04:47:37 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46409f6ada144b558d27c566e240f9c7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>BOM( Browser Object Model )即浏览器对象模型，它提供了独立于内容而与浏览器窗口进行交互的对象，其核心对象是 window。</p>
<p><strong>DOM文档对象模型:</strong></p>
<ul>
<li>DOM 就是把「文档」当做一个「对象」来看待</li>
<li>DOM 的顶级对象是 document</li>
<li>DOM 主要学习的是操作页面元素</li>
<li>DOM 是 W3C 标准规范</li>
</ul>
<p><strong>BOM浏览器对象模型:</strong></p>
<ul>
<li>把「浏览器」当做一个「对象」来看待</li>
<li>BOM 的顶级对象是 window</li>
<li>BOM 学习的是浏览器窗口交互的一些对象</li>
<li>BOM 是浏览器厂商在各自浏览器上定义的，兼容性较差中</li>
<li>BOM 包含 DOM</li>
</ul>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46409f6ada144b558d27c566e240f9c7~tplv-k3u1fbpfcp-watermark.image" alt="src=http___s15.sinaimg.cn_bmiddle_5f30c4c9x71d110b3d3fe&690&refer=http___s15.sinaimg.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一.window对象</h2>
<p>window 是客户端浏览器对象模型的基类，window 对象是客户端 JavaScript 的全局对象。一个 window 对象实际上就是一个独立的窗口，对于框架页面来说，浏览器窗口每个框架都包含一个 window 对象。</p>
<blockquote>
<p>双重角色:</p>
<blockquote>
<ul>
<li>1.它是 JS 访问浏览器窗口的一个接口。</li>
<li>2.它是一个全局对象。定义在全局作用域中的变量、函数都会变成 window 对象的属性和方法（全局变量=window 的属性：“window.变量名”就能打印出该变量的值，同样，函数则变成 window 的方法）。在调用的时候可以省略 window，前面学习的对话框都属于 window 对象方法，如 alert()、prompt()等。</li>
</ul>
</blockquote>
</blockquote>
<h3 data-id="heading-1"><strong>1.1 使用系统对话框-三个人机交互的方法</strong></h3>
<blockquote>
<ul>
<li>
<p>1.<code>alert()</code>：确定提示框。由浏览器向用户弹出提示性信息。该方法包含一个可选的提示信息参数。如果没有指定参数，则弹出一个空的对话框。</p>
</li>
<li>
<p>2.<code>confirm()</code>：选择提示框。。由浏览器向用户弹出提示性信息，弹出的对话框中包含两个按钮，分别表示“确定”和“取消”按钮。如果点击“确定”按钮，则该方法将返回 true；单击“取消”按钮，则返回 false。confirm() 方法也包含一个可选的提示信息参数，如果没有指定参数，则弹出一个空的对话框。</p>
</li>
<li>
<p>3.<code>prompt()</code>：输入提示框。可以接收用户输入的信息，并返回输入的信息。prompt() 方法也包含一个可选的提示信息参数，如果没有指定参数，则弹出一个没有提示信息的输入文本对话框。</p>
</li>
</ul>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">var</span> user = prompt(<span class="hljs-string">"请输入您的用户名"</span>);
      <span class="hljs-keyword">if</span> (!!user) &#123;
        <span class="hljs-comment">//把输入的信息转换为布尔值</span>
        <span class="hljs-keyword">var</span> ok = confirm(<span class="hljs-string">"您输入的用户名为：\n"</span> + user + <span class="hljs-string">"\n 请确认。"</span>); <span class="hljs-comment">//输入信息确认</span>
        <span class="hljs-keyword">if</span> (ok) &#123;
          alert(<span class="hljs-string">"欢迎您：\n"</span> + user);
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">//重新输入信息</span>
          user = prompt(<span class="hljs-string">"请重新输入您的用户名："</span>);
          alert(<span class="hljs-string">"欢迎您：\n"</span> + user);
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">//提示输入信息</span>
        user = prompt(<span class="hljs-string">"请输入您的用户名："</span>);
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2"><strong>1.2 窗口事件</strong></h3>
<h4 data-id="heading-3">1.2.1 窗口加载事件<code> window.onload</code></h4>
<blockquote>
<ul>
<li>window.onload 是窗口(页面）加载事件,当文档内容完全加载完成会触发该事件(包括图像、脚本文件、CSS 文件等),就调用的处理函数。</li>
<li>有了 window.onload 就可以把 JS 代码写到页面元素的上方，因为 onload 是等页面内容全部加载完毕，再去执行处理函数。</li>
<li>window.onload 传统注册事件方式只能写一次，如果有多个，会以最后一个 window.onload 为准。<code>如果使用 addEventListener 则没有限制</code></li>
</ul>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span> .onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-comment">//在里面写js代码</span>
&#125;
<span class="hljs-comment">//或者</span>
<span class="hljs-built_in">window</span>.addEventListener (<span class="hljs-string">"load"</span> , <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; 
<span class="hljs-comment">//在里面写js代码</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">1.2.2 <code>窗口加载事件 DOMContentLoaded</code></h4>
<blockquote>
<ul>
<li>DOMContentLoaded 事件触发时，仅当 DOM 加载完成，不包括样式表，图片，flash 等等。</li>
<li>如果页面的图片很多的话,从用户访问到 onload 触发可能需要较长的时间,交互效果就不能实现，必然影响用户的体验，此时用 DOMContentLoaded 事件比较合适。</li>
<li>DOMContentLoaded 是 DOM 加载完毕，不包含图片 flash css 等就可以，执行加载速度比 load 更快一些</li>
<li>le9 以上才支持;</li>
<li></li>
</ul>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">"DOMContentLoaded"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;

&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">1.2.3 调整窗口大小事件<code>resize</code></h4>
<blockquote>
<ul>
<li>window.onresize 是调整窗口大小加载事件，当触发时就调用的处理函数。</li>
<li>注意 ∶</li>
</ul>
<blockquote>
<p>只要窗口大小发生像素变化，就会触发这个事件。<br>
我们经常利用这个事件完成响应式布局。使用 window.innerWidth 获取当前屏幕的宽度</p>
</blockquote>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.onresize = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;;
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"resize"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6"><strong>1.3 定时器</strong></h3>
<blockquote>
<p>window 对象包含 4 个定时器专用方法，说明如下表所示，使用它们可以实现代码定时执行，或者延迟执行，使用定时器可以设计演示动画。</p>
<p><code>setTimeout(回调函数,延时时间(毫秒));</code> 倒计时结束之后调用函数</p>
<p><code>clearTimeout(定时器名字)</code>： 清除 setTimeOut 的定时器；</p>
<p><code>setInterval(回调函数,间隔时间)</code>： 每间隔多少时间就执行一次回调函数</p>
<p><code>clearInterval(定时器名字)</code>： 清除 setInterval 的定时器；<br><br>
<strong>区别：</strong></p>
<ul>
<li>
<p>setTimeout() 方法主要用来延迟代码执行，而 setInterval() 方法主要实现周期性执行代码。它们都可以设计周期性动作，其中 setTimeout() 方法适合不定时执行某个动作，而 setInterval() 方法适合定时执行某个动作。</p>
</li>
<li>
<p>setTimeout() 方法不会每隔固定时间就执行一次动作，它受 JavaScript 任务队列的影响，只有前面没有任务时，才会按时延迟执行动作。而 setInterval() 方法不受任务队列的限制，它只是简单的每隔一定的时间就重复执行一次动作，如果前面任务还没有执行完毕，setInterval()  可能会插队按时执行动作。</p>
</li>
</ul>
</blockquote>
<h2 data-id="heading-7">二.navigator对象</h2>
<blockquote>
<p>navigator 对象存储了与浏览器相关的基本信息，如名称、版本和系统等。通过 window.navigator 可以引用该对象，并利用它的属性来读取客户端基本信息。</p>
<p>navigator 对象包含有关浏览器的信息，它有很多属性，我们最常用的是 <code>userAgent</code>，该属性可以返回由客户机发送服务器的 user-agent 头部的值。</p>
</blockquote>
<p>下面前端代码可以判断用户那个终端打开页面，实现跳转:</p>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">if</span>((navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|
      Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS
      |Symbian|Windows Phone)/i))) &#123;
       <span class="hljs-built_in">window</span>.location.href = <span class="hljs-string">""</span>; <span class="hljs-comment">//手机</span>
      &#125;
      <span class="hljs-keyword">else</span> &#123;
       <span class="hljs-built_in">window</span>.location.href = <span class="hljs-string">""</span>; <span class="hljs-comment">//电脑</span>
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">三.location 对象</h2>
<blockquote>
<p>window 对象给我们提供了一个 location 属性用于获取或设置窗体的 URL，并且可以用于解析 URL。因为这个属性返回的是一个对象，所以我们将这个属性也称为 location 对象。</p>
<p><code>URL</code>:统一资源定位符(Uniform Resource Locator,URL)是互联网上标准资源的地址。互联网上的每个文件都有一个唯一的 URL，它包含的信息指出文件的位置以及浏览器应该怎么处理它。</p>
</blockquote>
<h3 data-id="heading-9">3.1 location对象的属性</h3>
<p>以该url举例：<a href="http://www.baidu.com:8080/web/javascript/test.js#12345?a=10&b=20" target="_blank" rel="nofollow noopener noreferrer">www.baidu.com:8080/web/javascr…</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f82b19d0d7e4a8f8bbc6d6a88b45efc~tplv-k3u1fbpfcp-watermark.image" alt="捕获2222.PNG" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">3.2 自定义查询字符串参数返回对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//假设当前URL：'http://www.maxiaofei.com/Web/test.js?name=mafei&age=24&sex=m'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getQueryObj</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> location = <span class="hljs-built_in">window</span>.location;
    <span class="hljs-keyword">let</span> queryStr = location.search.length > <span class="hljs-number">0</span> ? location.search.substring(<span class="hljs-number">1</span>) : <span class="hljs-string">''</span>;
    <span class="hljs-keyword">let</span> obj = &#123;&#125;,item;
    <span class="hljs-keyword">let</span> queryArr = queryStr.length > <span class="hljs-number">0</span> ? queryStr.split(<span class="hljs-string">'&'</span>) : []
    
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<queryArr.length;i++)&#123;
        item = queryArr[i].split(<span class="hljs-string">'='</span>);
        obj[item[<span class="hljs-number">0</span>]] = item[<span class="hljs-number">1</span>]
    &#125;

    <span class="hljs-keyword">return</span> obj
&#125;

getQueryObj()
<span class="hljs-comment">//=》&#123;</span>
    <span class="hljs-attr">name</span>: <span class="hljs-string">'maxiaofei'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">24</span>,
    <span class="hljs-attr">sex</span>: <span class="hljs-string">'m'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">3.3 修改location</h3>
<blockquote>
<p>每次修改 location 的 hash　以外的任何属性，页面都会以新URL重新加载</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.location = <span class="hljs-string">'http://www.maxiaofei.com'</span>

location.search = <span class="hljs-string">'?name=mafei&age=18'</span>

location.hostname = <span class="hljs-string">'www.baidu.com'</span>

location.pathname = <span class="hljs-string">'web/html/a.html'</span>

location.port = <span class="hljs-string">'1234'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了 hash  值以外的任何修改，都会在浏览器的历史记录中生成一条新的记录，可以通过浏览器的回退按钮导航到前一个页面，可以通过 replace() 方法禁止这种行为，使用 replace 打开的页面，不能返回到前一个页面</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 尝试在浏览器控制台输入如下代码，浏览器将不支持回退</span>
location.replace(<span class="hljs-string">'http://www.baidu.com'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">3.4 重新加载</h3>
<blockquote>
<p>通过 location.reload() 方法可以重新加载页面</p>
<p>location.reload() : 重新加载（有可能会从缓存中加载）</p>
<p>location.reload(true)： 重新加载（从服务器重新加载）</p>
</blockquote>
<h2 data-id="heading-13">四. history对象</h2>
<blockquote>
<p>history 对象保存着用户上网的<code>历史记录</code>，从窗口被打开的那一刻算起，因为 history 是 window 对象的属性，因此每个浏览器窗口，每个标签乃至每个框架，都有自己的 history对象与特定的 window 对象关联
<br><br>
<strong>history 常用的有如下3个方法和一个属性:</strong></p>
<ol>
<li>history.go()</li>
</ol>
<blockquote>
<p>接收一个整数数字或者字符串参数：向最近的一个记录中包含指定字符串的页面跳转</p>
<pre><code class="hljs language-js copyable" lang="js">history.go(<span class="hljs-string">'maixaofei.com'</span>)<span class="hljs-comment">//向前或者向后寻找指定字符串页面，没有找到则无响应</span>
history.go(<span class="hljs-number">3</span>)<span class="hljs-comment">//向前跳转三个记录</span>
history.go(-<span class="hljs-number">1</span>)<span class="hljs-comment">//向后跳转一个记录</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<ol start="2">
<li>history.forward()</li>
</ol>
<blockquote>
<p>向前跳转一个页面</p>
</blockquote>
<ol start="3">
<li>history.back()</li>
</ol>
<blockquote>
<p>向后跳转一个页面</p>
</blockquote>
<ol start="4">
<li>history.length</li>
</ol>
<blockquote>
<p>获取历史记录数，如果是打开的第一个页面，则 history.length == 0，可以用该属性来判断当前打开的网页是不是该窗口打开的首个网页</p>
</blockquote>
</blockquote>
<p>history对象一般在实际开发中比较少用，但是会在一些 OA 办公系统中见到。</p>
<h2 data-id="heading-14">五.screen对象是用处不大的对象</h2>
<p>它基本上只用来表明客户端的能力，其中包括了浏览器窗口外部的显示器信息，比如像素和宽高等，常用属性如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js">availHeight    <span class="hljs-comment">//屏幕的像素高度减去系统部件的高度</span>

availWidth     <span class="hljs-comment">//屏幕的像素宽度减去系统部件的宽度</span>

availLeft        <span class="hljs-comment">//未被系统部件占用的最左侧像素值</span>

availTop       <span class="hljs-comment">// 未被系统部件占用的最上侧像素值</span>

height          <span class="hljs-comment">// 屏幕像素高度</span>

width           <span class="hljs-comment">// 屏幕像素宽度</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">六.其他</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dbbda4ea6f549c5b47b77fc40485a95~tplv-k3u1fbpfcp-watermark.image" alt="169dd79558ce2af9.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">6.1 元素可视区client</h3>
<blockquote>
<p>Element.clientTop 和 Element.clientLeft 获取可视区域的偏移值(实际上就等于元素上下 border 值) 四舍五入（整数）后的结果;
<br><br>
Element.clientWidth 和 Element.clientHeight 获取可视区域（padding + 元素内容区域的宽高，不包含滚动条）的宽高</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/607ba72d27ee4f91985a1a374e7965e7~tplv-k3u1fbpfcp-watermark.image" alt="169dbb46ea695bb6.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">6.2 元素偏移量 offset(块级元素,只读属性)</h3>
<blockquote>
<ol>
<li>Element.offsetParent</li>
</ol>
<blockquote>
<p>Element.offsetParent 是一个只读属性， 返回当前元素最近的一个父级定位元素。</p>
</blockquote>
<ol start="2">
<li>Element.offsetLeft && Element.offsetTop</li>
</ol>
<blockquote>
<p>Element.offsetLeft 和 Element.offsetTop 是一个只读属性，返回当前元素相对于父级元素左侧和上侧的偏移量。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/546e0fb93f1943a0af4e19ddb7a021be~tplv-k3u1fbpfcp-watermark.image" alt="169dbb288cada1ff.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<ol start="3">
<li>Element.offsetWidth && Element.offsetHeight</li>
</ol>
<blockquote>
<p>Element.offsetWidth 和 Element.offsetHeight 是一个只读属性，返回一个元素布局的宽高（元素布局包括： border、滚动条、padidng、内容块）， 该属性返回的值为一个四舍五入的整数.
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07a985aed1164a6995cecac28143a3db~tplv-k3u1fbpfcp-watermark.image" alt="169dbb3b2c0fd276.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<br>
</blockquote>
<h4 data-id="heading-18">6.2.1 offset 与 style 区别</h4>
<blockquote>
<p>offset：</p>
<ul>
<li>offset 可以得到任意样式表中的样式值</li>
<li>offset 系列获得的数值是没有单位的</li>
<li>offsetWidth 包含 padding+border+width·</li>
<li>offsetWidth 等属性是只读属性，只能获取不能赋值·</li>
</ul>
</blockquote>
<p>所以，我们想要获取元素大小位置，用 offset 更合适</p>
<blockquote>
<p>style：</p>
<ul>
<li>style 只能得到行内样式表中的样式值</li>
<li>style.width 获得的是带有单位的字符串</li>
<li>style.width 获得不包含 padding 和 border 的值</li>
<li>style.width 是可读写属性，可以获取也可以赋值</li>
</ul>
</blockquote>
<p>所以，我们想要给元素更改值，则需要用 style 改变·</p>
<h3 data-id="heading-19">6.3 scroll(用于对可滚动元素进行求值)</h3>
<h4 data-id="heading-20">6.3.1 Element.scrollTop 和 Element.scrollLeft</h4>
<blockquote>
<p>用于获取或设置元素被卷起的宽高（子元素顶部或左侧到当前元素可视区域顶部或左侧的距离）</p>
<blockquote>
<p>补充：</p>
<blockquote>
<ul>
<li>对于不可滚动的元素 Element.scrollTop 和 Element.scrollLeft 值为 0<br></li>
<li>如果给 scrollTop（scrollLeft） 设置的值小于0，那么 scrollTop（scrollLeft） 的值将变为0。</li>
<li>如果给 scrollTop（scrollLeft） 设置的值大于元素内容最大宽度，那么 scrollTop（scrollLeft） 的值将被设为元素最大宽度（高度）。</li>
</ul>
</blockquote>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f7259925f6747ddae2a1fd6a41291ed~tplv-k3u1fbpfcp-watermark.image" alt="169dbb4cb83f3aee.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h4 data-id="heading-21">6.3.2 Element.scrollWidth && Element.scrollHeight</h4>
<blockquote>
<ul>
<li>Element.scrollWidth 和 Element.scrollHeight 是<code>只读属性</code>， 表示元素可滚动区域的宽高； 实际上又等于 <code>clientHeight/clientWidth + 未显示在屏幕中内容的宽高</code>;</li>
<li>它们的值等于元素在不使用水平滚动条的情况下适合视口中的所有内容所需的最小宽度。</li>
<li>测量方式与 clientWidth(clientHeight) 相同：它包含元素的内边距，但不包括边框，外边距或垂直滚动条（如果存在）。 它还可以包括伪元素的宽度，例如::before或::after。</li>
<li>如果元素的内容可以适合而不需要水平滚动条，则其 scrollWidth 等于 clientWidth; (最小值为元素的可视区域宽高： clientWidth (clientHeight))</li>
</ul>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bceb2c63a5fc4627aa7051486fcd0852~tplv-k3u1fbpfcp-watermark.image" alt="169dbb519d255fec.jpg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            