
---
title: 'NodeJS实现一个聊天室'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a24ff6b4890a4d95afdbaed4bebbf738~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 22:46:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a24ff6b4890a4d95afdbaed4bebbf738~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">文章目录</h3>
<ul>
<li>
<ul>
<li>
<ul>
<li>
<ul>
<li><a href="https://juejin.cn/post/6943479404462866462#_1">看效果</a></li>
<li><a href="https://juejin.cn/post/6943479404462866462#_6">前文</a></li>
<li><a href="https://juejin.cn/post/6943479404462866462#_9">客户端代码</a></li>
<li><a href="https://juejin.cn/post/6943479404462866462#_104">服务端代码</a></li>
<li><a href="https://juejin.cn/post/6943479404462866462#_147">服务跑起来</a></li>
<li>
<ul>
<li><a href="https://juejin.cn/post/6943479404462866462#node_153">安装node</a></li>
<li><a href="https://juejin.cn/post/6943479404462866462#packagejs_156">初始化package.js</a></li>
<li><a href="https://juejin.cn/post/6943479404462866462#nodemon_159">安装nodemon</a></li>
<li><a href="https://juejin.cn/post/6943479404462866462#socketio_161">安装socket.io</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/6943479404462866462#_164">感谢阅读</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h4 data-id="heading-1"><a href="https://juejin.cn/post/6943479404462866462"></a>看效果</h4>
<p>一直说我喜欢卖关子，这次直接看效果：<br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a24ff6b4890a4d95afdbaed4bebbf738~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
聊天界面（喜欢的可以自己画一个比较逼真的页面）<br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07f3c2908579416f978d312b838c794c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2"><a href="https://juejin.cn/post/6943479404462866462"></a>前文</h4>
<p>先说一下为什么写这个东西，最近不是在写NodeJS知识点的梳理嘛，但是我发现梳理的过程着实无聊的要死，虽然已经快梳理一半了，只是还没发布，这个不重要，重要的是不做点什么东西确实无聊，所以今天把我做这个的过程记录给你们看一下，喜欢的可以拿去玩玩。实现的功能是可以聊天，可以显示用户自定义的昵称，并且显示发送时间<br>
PS：这个功能如果我们使用webstorm新建一个express app的项目的话，是可以省很多代码的，但是这里我们选择原生实现它，原因是我们写代码不可能一直依赖于别人搭建好的框架或者轮子，虽然我们提倡不重复造轮子，但是如果每一个程序员都这样想的话，这个行业面临的将是一个轮子都没有。</p>
<h4 data-id="heading-3"><a href="https://juejin.cn/post/6943479404462866462"></a>客户端代码</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>http_demo<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"/socket.io/socket.io.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>
        WelCome to CSDN of clearlove
    <span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
        If you like my article, you can follow my blog
    <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>公屏聊天<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"infos"</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-top: 5vh;
    width: 100px;
    height: 40px;
    border: 1px solid #ffffff;
    border-radius: 4px;
    color: #000000;
    padding-left: 10px"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"nick"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">""</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"昵称"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"send_info"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">""</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请输入您想说的话"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn"</span>></span>发送<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">//创建一个io对象</span>
    <span class="hljs-keyword">var</span> socket = io();
    <span class="hljs-comment">//用户点击发送的时候直接将昵称和信息内容发送过去，如果没有昵称，显示匿名，判断是不是有值</span>
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"btn"</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"send_info"</span>).value)&#123;
            socket.emit(<span class="hljs-string">"link_to_server"</span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"send_info"</span>).value, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"nick"</span>).value ? <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"nick"</span>).value : <span class="hljs-string">'匿名'</span>)
        &#125;<span class="hljs-keyword">else</span>&#123;
            alert(<span class="hljs-string">`发送内容不可以为空`</span>)
        &#125;
        
    &#125;
    <span class="hljs-comment">// 收到的信息展示出来，新建一个元素，append到div中</span>
    socket.on(<span class="hljs-string">'link_to_client'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">msg</span>) </span>&#123;
        <span class="hljs-keyword">var</span> h6 = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'h6'</span>);
        h6.innerText = <span class="hljs-string">`<span class="hljs-subst">$&#123;msg&#125;</span>`</span>;
        <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'infos'</span>).append(h6)
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-tag">body</span> &#123;
        <span class="hljs-attribute">background</span>: <span class="hljs-number">#307ac6</span>;
        <span class="hljs-attribute">text-align</span>: center;
        <span class="hljs-attribute">color</span>: aliceblue;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0%</span> <span class="hljs-number">10%</span>
    &#125;

    <span class="hljs-selector-tag">p</span> &#123;
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">2rem</span>
    &#125;

    <span class="hljs-selector-tag">input</span> &#123;
        <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">5vh</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
        <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ffffff</span>;
        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">4px</span>;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#000000</span>;
        <span class="hljs-attribute">padding-left</span>: <span class="hljs-number">10px</span>;
    &#125;

    <span class="hljs-selector-tag">button</span> &#123;
        <span class="hljs-attribute">border</span>: none;
        <span class="hljs-attribute">background</span>: <span class="hljs-number">#ffffff</span>;
        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">4px</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">90px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">42px</span>;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#000000</span>;
    &#125;

    <span class="hljs-selector-id">#infos</span> &#123;
        <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">25vw</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">500px</span>;
        <span class="hljs-attribute">overflow</span>: scroll;
        <span class="hljs-attribute">border</span>: none;
        <span class="hljs-attribute">background</span>: <span class="hljs-number">#ffffff</span>;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#000000</span>;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4"><a href="https://juejin.cn/post/6943479404462866462"></a>服务端代码</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@author <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@aim </span>测试连接一个socket.io通信 广播
 */</span>
<span class="hljs-comment">//引入fs</span>
<span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-comment">//引入http </span>
<span class="hljs-keyword">var</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>)
<span class="hljs-keyword">var</span> date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@FormDate </span>格式化时间
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>date  当前时间
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FormDate</span>(<span class="hljs-params">date</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;date.getFullYear()&#125;</span>-<span class="hljs-subst">$&#123;date.getMonth() + <span class="hljs-number">1</span>&#125;</span>-<span class="hljs-subst">$&#123;date.getDate()&#125;</span>  <span class="hljs-subst">$&#123;date.getHours()&#125;</span>:<span class="hljs-subst">$&#123;date.getMinutes()&#125;</span>`</span>
&#125;
<span class="hljs-comment">/**
 * 搭建一个服务器
 */</span>
<span class="hljs-keyword">var</span> server = http.createServer(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res, res</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (res.url !== <span class="hljs-string">'/favicon.ico'</span>) &#123;
        res.writeHead(<span class="hljs-number">200</span>, &#123; <span class="hljs-string">"Content-type"</span>: <span class="hljs-string">"text/html"</span> &#125;)
        <span class="hljs-keyword">const</span> myreadstream = fs.createReadStream(__dirname + <span class="hljs-string">'/views/http_demo.html'</span>, <span class="hljs-string">'utf-8'</span>)
        myreadstream.pipe(res)
    &#125;
&#125;)
<span class="hljs-comment">//引入socket.io  这里是两步，第一步是io = require('socket.io') 第二步是一个新的变量.server 合成一步就是下面的代码</span>
<span class="hljs-keyword">var</span> io = <span class="hljs-built_in">require</span>(<span class="hljs-string">'socket.io'</span>)(server);

io.on(<span class="hljs-string">"connection"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">socket</span>) </span>&#123;
    <span class="hljs-comment">//这里获取到对方的ip地址，可以展示，也可以不展示，也可以进行ip的过滤</span>
    <span class="hljs-keyword">var</span> clientIp = socket.request.connection.remoteAddress
    <span class="hljs-built_in">console</span>.info(<span class="hljs-string">"一个socket连接成功了"</span>)
    socket.on(<span class="hljs-string">"link_to_server"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">msg, nick</span>) </span>&#123;
        <span class="hljs-comment">//这里使用io发送 </span>
        io.emit(<span class="hljs-string">'link_to_client'</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;nick&#125;</span> : <span class="hljs-subst">$&#123;msg&#125;</span>  <span class="hljs-subst">$&#123;FormDate(date)&#125;</span>`</span>)
    &#125;)
&#125;)
server.listen(<span class="hljs-number">5000</span>, <span class="hljs-string">'0.0.0.0'</span>);
<span class="hljs-built_in">console</span>.info(<span class="hljs-string">"server is running..."</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5"><a href="https://juejin.cn/post/6943479404462866462"></a>服务跑起来</h4>
<ul>
<li>隐藏一下ip吧，为了安全<br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3786b6d86d14d2d913bb95390a8e79c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<blockquote>
<p>当然上面我用的一些可能比较‘原生’，直接创建元素什么的，我是因为没有引入类似jquery这样的框架进来，引入的话就比较简单的，但是不影响我们实现这个基础的聊天功能，上面可能有一些你们不明白的地方或者是你们都明白，包括为什么上面启动的时候不是node+文件名字而是nodemon+文件名，有什么区别，有什么好处，都没关系，后面的文章我都会介绍上面用到的所有的知识点，具体怎么使用的，怎么出来的， 为什么这么写，怎么一步一步实现目前的这个效果，后面的文章我都会更新，为什么这个时候写这个呢？原因是我想让更多的人知道NodeJS本身是一个很好玩的语言，可以做的事情很多。如果你们看了我的文章以后喜欢上了NodeJS我的目的就达到了，毕竟我还是觉得NodeJS是一个非常强大的语言，我希望更多的人使用它。</p>
</blockquote>
<blockquote>
<p>如果有人觉得不想看那么多就想玩玩这个效果的，也可以，直接安装node、然后本地初始化一个package.json，然后安装nodemon、socket.io就可以了，具体怎么安装，emmmmm</p>
</blockquote>
<h5 data-id="heading-6"><a href="https://juejin.cn/post/6943479404462866462"></a>安装node</h5>
<p>下载<a href="http://nodejs.cn/" target="_blank" rel="nofollow noopener noreferrer">node</a><br>
下一步下一步就好了</p>
<h5 data-id="heading-7"><a href="https://juejin.cn/post/6943479404462866462"></a>初始化package.js</h5>
<p>npm init</p>
<ul>
<li>输入名字 版本号之后 一直回车就好了</li>
</ul>
<h5 data-id="heading-8"><a href="https://juejin.cn/post/6943479404462866462"></a>安装nodemon</h5>
<p>npm install -g nodemon --save-dev</p>
<h5 data-id="heading-9"><a href="https://juejin.cn/post/6943479404462866462"></a>安装socket.io</h5>
<p>npm install socket.io --save-dev</p>
<blockquote>
<p>写的可能比较简单，原因是后面我还会详细介绍，这里就不写了…</p>
</blockquote>
<h4 data-id="heading-10"><a href="https://juejin.cn/post/6943479404462866462"></a>感谢阅读</h4></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            