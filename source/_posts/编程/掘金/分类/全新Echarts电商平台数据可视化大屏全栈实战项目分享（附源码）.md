
---
title: '全新Echarts电商平台数据可视化大屏全栈实战项目分享（附源码）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19618af9ce3d4dfa8f6457feba39d948~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 08 May 2021 19:33:27 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19618af9ce3d4dfa8f6457feba39d948~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. 前言</h1>
<blockquote>
<p>五一假期重学了新版Echarts，一个基于JavaScript的开源可视化图表库，收集参考了很多网上资料，最终选择电商平台作为练手项目。此篇涉及技术知识点有：Vue全家桶、WebSocket前后端数据推送、后端框架Koa2、Echarts新版图表组件（折线图、柱状图、饼图、地图、散点图），还支持主题切换, 展示酷炫的图表效果，同时也能够支持大屏和小屏的切换，保证了图表在不同屏幕上呈现的效果。</p>
</blockquote>
<h1 data-id="heading-1">2. 入门篇（新手指南）</h1>
<p><a href="https://juejin.cn/post/6916739355088420878" target="_blank">ECharts数据可视化快速入门</a></p>
<h1 data-id="heading-2">3. 实战篇（上下两部）</h1>
<p><a href="https://juejin.cn/post/6844904158181457933" target="_blank">Vue+Echarts构建可视化大数据平台实战项目分享</a></p>
<h1 data-id="heading-3">4. 进阶篇</h1>
<h2 data-id="heading-4">4.1 前后端分离</h2>
<p>前端项目采用的技术栈是基于Vue + Echarts，用vue-cli构建前端界面，后端项目采用的技术栈是基于Node.js + Koa2 + WebSocket，用Koa2搭建的后端服务器。</p>
<p>在线演示DEMO地址👉：<a href="http://106.55.168.13:8999/" target="_blank" rel="nofollow noopener noreferrer">http://106.55.168.13:8999/</a></p>
<p>附上详细的思维导图如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19618af9ce3d4dfa8f6457feba39d948~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>分享之前，我们先来了解一下新版 Echarts 5.x，都有哪些变化，如下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34f91af8b99f4fcebbbc09c95f3110fb~tplv-k3u1fbpfcp-watermark.image" alt="echarts-5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">4.2 后端部分</h2>
<h3 data-id="heading-6">4.2.1 Koa2的介绍</h3>
<ul>
<li>基于 Node.js 平台的Web服务器框架</li>
<li>由 Express 原班人马打造，Express、Koa、Koa2 都是 Web 服务器的框架，他们之间的区别如下图：</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4341a088e534023b790ffd4fb4c78c8~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>环境依赖 Node v7.6.0 及以上</li>
</ul>
<p>由于 Koa2 它是支持 async 和 await ，所以它对 Node 的版本是有要求的，它要求 Node 的版本至少是在7.6级以上,因为语法糖 async和await 是在 Node7.6 版本之后出现才支持</p>
<ul>
<li>洋葱模型的中间件</li>
</ul>
<p>如下图所示, 对于服务器而言，它其实就是来处理一个又一个的请求， Web 服务器接收由浏览器发
过来的一个又一个请求之后，它形成一个又一个的响应返回给浏览器. 而请求到达我们的服务器是
需要经过程序处理的,程序处理完之后才会形成响应，返回给浏览器，我们服务器处理请求的这一
块程序，在 Koa2 的世界当中就把它称之为中间件</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b25978ff48b40f09af6d031be23ea33~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这种中间件可能还不仅仅只有一个，可能会存在多个，比如上图所示, 它就存在三层中间件，这三
层中间件在处理请求的过程以及它调用的顺序为:</p>
<ul>
<li>当一个请求到达咱们的服务器，最先最先处理这个请求的是第一层中间件</li>
<li>第一层的中间件在处理这个请求之后，它会把这个请求给第二层的中间件</li>
<li>第二层的中间件在处理这个请求之后，它会把这个请求给第三层的中间件</li>
<li>第三层中间件内部并没有中间件了, 所以第三层中间件在处理完所有的代码之后，这个请求又会到了第二层的中间件，所以第二层中间件对这个请求经过了两次的处处理</li>
<li>第二层的中间件在处理完这个请求之后，又到了第一层的中间件, 所以第一层的中间件也对这个请求经过了两次的处理</li>
</ul>
<p>这个调用顺序就是洋葱模型, 中间件对请求的处理有一种先进后出的感觉，请求最先到达第一层中
间件，而最后也是第一层中间件对请求再次处理了一下</p>
<h3 data-id="heading-7">4.2.2 Koa2的快速上手</h3>
<h4 data-id="heading-8">4.2.2.1 检查node版本，Koa2的使用要求node版本在7.6以上</h4>
<pre><code class="hljs language-js copyable" lang="js">node -v
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">4.2.2.2 安装 Koa2</h4>
<pre><code class="hljs language-js copyable" lang="js">npm init -y
npm install koa
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果下载特别慢，可以将npm的下载源换成国内的下载源，命令如下：</p>
<pre><code class="hljs language-js copyable" lang="js">npm set registry https:<span class="hljs-comment">//registry.npm.taobao.org/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">4.2.2.3 编写入口文件app.js</h4>
<ul>
<li>创建Koa的实例对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa'</span>) <span class="hljs-comment">// 导入构造方法</span>
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa() <span class="hljs-comment">// 通过构造方法，创建实例对象</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>编写响应函数（中间件）</p>
<p>响应函数是通过use的方式才能产生效果, 这个函数有两个参数, 一个是 ctx，一个是 next</p>
<p><strong>ctx</strong>：上下文, 指的是请求所处于的Web容器,我们可以通过 ctx.request 拿到请求对象, 也可以通过 ctx.response 拿到响应对象</p>
<p><strong>next</strong>：内层中间件执行的入口</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">app.use(<span class="hljs-function">(<span class="hljs-params">ctx, next</span>) =></span> &#123;
    ctx.response.body = <span class="hljs-string">'Hello Echarts'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>绑定端口号</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">app.listen(<span class="hljs-number">9898</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>启动服务器</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">node app.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在浏览器中输入 <a href="http://localhost:9898/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:9898/</a> 你将会看到浏览器中出现 Hello Echarts 的字符串, 并且在服务器的终端中, 也能看到请求的 url</p>
<h3 data-id="heading-11">4.2.3 Koa2中间件的特点</h3>
<ul>
<li>Koa2 的实例对象通过 use 方法加入一个中间件</li>
<li>一个中间件就是一个函数,这个函数具备两个参数,分别是 ctx 和 next</li>
<li>中间件的执行符合洋葱模型</li>
<li>内层中间件能否执行取决于外层中间件的 next 函数是否调用</li>
<li>调用 next 函数得到的是 Promise 对象, 如果想得到 Promise 所包装的数据, 可以结合 await 和 async</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123; 
    <span class="hljs-comment">// 刚进入中间件想做的事情 </span>
    <span class="hljs-keyword">await</span> next() 
    <span class="hljs-comment">// 内层所有中间件结束之后想做的事情 </span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">4.2.4 后端项目</h3>
<h4 data-id="heading-13">4.2.4.1 目标</h4>
<p>我们已学完 Koa2 的快速上手, 并且对 Koa2 当中的中间件的特点进行了了解. 接下来就是利用Koa2 的知识来进行后台项目的开发，后台项目需要达到以下几个目标:</p>
<ul>
<li>
<p>计算服务器处理请求的总耗时</p>
<p>计算出服务器对于这个请求它的所有中间件总耗时时长究竟是，我们需要计算一下</p>
</li>
<li>
<p>在响应头上加上响应内容的 mime 类型</p>
<p>加入mime类型, 可以让浏览器更好的来处理由服务器返回的数据</p>
<p>如果响应给前端浏览器是 json 格式的数据，这时候就需要在咱们的响应头当中增加 Content- Type 它的值就是 application/json ， application/json 就是 json 数据类型的 mime 类型</p>
</li>
<li>
<p>根据URL读取指定目录下的文件内容</p>
<p>为了简化后台服务器的代码，前端图表所要的数据, 并没有存在数据库当中，而是将存在文件当中</p>
</li>
</ul>
<p>的，这种操作只是为了简化咱们后台的代码. 所以咱们是需要去读取某一个目录下面的文件内容
的。</p>
<p>每一个目标就是一个中间件需要实现的功能, 所以后台项目中需要有三个中间件</p>
<h4 data-id="heading-14">4.2.4.2 步骤</h4>
<p>创建一个新的文件夹 koa-server , 这个文件夹就是后台项目的文件夹</p>
<h5 data-id="heading-15">4.2.4.2.1 项目准备</h5>
<ul>
<li>安装包</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">npm init -y 
npm install koa
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>创建文件和目录结构</p>
<p>app.js 是后台服务器的入口文件</p>
<p>data 目录是用来存放所有模块的 json 文件数据</p>
<p>middleware 是用来存放所有的中间件代码</p>
<p>koa_response_data.js 是业务逻辑中间件</p>
<p>koa_response_duration.js 是计算服务器处理时长的中间件</p>
<p>koa_response_header.js 是用来专门设置响应头的中间件</p>
</li>
</ul>
<p>接着将各个模块的 json 数据文件复制到 data 的目录之下, 接着在 app.js 文件中写上代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 服务器的入口文件 </span>
<span class="hljs-comment">// 1.创建KOA的实例对象 </span>
<span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa'</span>) 
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa() 
<span class="hljs-comment">// 2.绑定中间件 </span>
<span class="hljs-comment">// 绑定第一层中间件 </span>
<span class="hljs-comment">// 绑定第二层中间件 </span>
<span class="hljs-comment">// 绑定第三层中间件 </span>
<span class="hljs-comment">// 3.绑定端口号 9898 </span>
app.listen(<span class="hljs-number">9898</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">4.2.4.2.2 总耗时中间件</h5>
<ul>
<li>
<p>第1层中间件</p>
<p>总耗时中间件的功能就是计算出服务器所有中间件的总耗时，应该位于第一层，因为第一层的中间件是最先处理请求的中间件，同时也是最后处理请求的中间件</p>
</li>
<li>
<p>计算执行时间</p>
<p>第一次进入咱们中间件的时候，就记录一个开始的时间，当其他所有中间件都执行完之后，再记录下结束时间以后，将两者相减就得出总耗时</p>
</li>
<li>
<p>设置响应头</p>
<p>将计算出来的结果,设置到响应头的 X-Response-Time 中, 单位是毫秒 ms</p>
</li>
</ul>
<p>具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// app.js 文件</span>
<span class="hljs-comment">// 绑定第一层中间件 </span>
<span class="hljs-keyword">const</span> respDurationMiddleware = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./middleware/koa_response_duration'</span>) app.use(respDurationMiddleware)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// koa_response_duration.js 文件</span>
<span class="hljs-comment">// 计算服务器消耗时长的中间件 </span>
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">async</span> (ctx, next) => &#123; 
<span class="hljs-comment">// 记录开始时间</span>
<span class="hljs-keyword">const</span> start = <span class="hljs-built_in">Date</span>.now() 
<span class="hljs-comment">// 让内层中间件得到执行 </span>
<span class="hljs-keyword">await</span> next() 
<span class="hljs-comment">// 记录结束的时间 </span>
<span class="hljs-keyword">const</span> end = <span class="hljs-built_in">Date</span>.now() 
<span class="hljs-comment">// 设置响应头 X-Response-Time </span>
<span class="hljs-keyword">const</span> duration = end - start 
<span class="hljs-comment">// ctx.set 设置响应头 </span>
ctx.set(<span class="hljs-string">'X-Response-Time'</span>, duration + <span class="hljs-string">'ms'</span>) &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">4.2.4.2.3 响应头中间件</h5>
<ul>
<li>
<p>第2层中间件</p>
<p>这个第2层中间件没有特定的要求</p>
</li>
<li>
<p>获取mime类型</p>
<p>由于咱们所响应给前端浏览器当中的数据都是 json 格式的字符串，所以 mime 类型可以统一的给它写成 application/json , 当然这一块也是简化的处理，因为 mime 类型有几十几百种，我们没有必要在项目当中考虑那么多，所以这里简化处理一下</p>
</li>
<li>
<p>设置响应头</p>
<p>响应头的key是 Content-Type ，它的值是 application/json , 顺便加上 charset=utf-8 告诉浏览器，我这部分响应的数据，它的类型是 application/json ，同时它的编码是 utf- 8</p>
</li>
</ul>
<p>具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// app.js 文件</span>
<span class="hljs-comment">// 绑定第二层中间件 const respHeaderMiddleware = require('./middleware/koa_response_header') </span>
app.use(respHeaderMiddleware)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// koa_response_header.js 文件</span>
<span class="hljs-comment">// 设置响应头的中间件 </span>
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">async</span> (ctx, next) => &#123; 
<span class="hljs-keyword">const</span> contentType = <span class="hljs-string">'application/json; charset=utf-8'</span> 
ctx.set(<span class="hljs-string">'Content-Type'</span>, contentType) 
<span class="hljs-keyword">await</span> next() &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18">4.2.4.2.4 业务逻辑中间件</h5>
<ul>
<li>
<p>第3层中间件</p>
<p>这个第3层中间件没有特定的要求</p>
</li>
<li>
<p>读取文件内容</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 获取 URL 请求路径</span>
<span class="hljs-keyword">const</span> url = ctx.request.url
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 根据URL请求路径,拼接出文件的绝对路径</span>
<span class="hljs-keyword">let</span> filePath = url.replace(<span class="hljs-string">'/api'</span>, <span class="hljs-string">''</span>) 
filePath = <span class="hljs-string">'../data'</span> + filePath + <span class="hljs-string">'.json'</span> 
filePath = path.join(__dirname, filePath)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 filePath 就是需要读取文件的绝对路径</p>
<p>读取这个文件的内容，使用 fs 模块中的 readFile 方法进行实现</p>
<ul>
<li>设置响应体</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">ctx.response.body
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// app.js 文件</span>
<span class="hljs-comment">// 绑定第三层中间件 const respDataMiddleware = require('./middleware/koa_response_data') </span>
app.use(respDataMiddleware)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// koa_response_data.js 文件</span>
<span class="hljs-comment">// 处理业务逻辑的中间件,读取某个json文件的数据 </span>
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>) 
<span class="hljs-keyword">const</span> fileUtils = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../utils/file_utils'</span>) 

<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">async</span> (ctx, next) => &#123; 
<span class="hljs-comment">// 根据url </span>
<span class="hljs-keyword">const</span> url = ctx.request.url <span class="hljs-comment">// /api/seller ../data/seller.json </span>
<span class="hljs-keyword">let</span> filePath = url.replace(<span class="hljs-string">'/api'</span>, <span class="hljs-string">''</span>) <span class="hljs-comment">// /seller </span>
filePath = <span class="hljs-string">'../data'</span> + filePath + <span class="hljs-string">'.json'</span> <span class="hljs-comment">// ../data/seller.json </span>
filePath = path.join(__dirname, filePath) 
<span class="hljs-keyword">try</span> &#123; 
    <span class="hljs-keyword">const</span> ret = <span class="hljs-keyword">await</span> fileUtils.getFileJsonData(filePath) 
    ctx.response.body = ret
&#125; <span class="hljs-keyword">catch</span> (error) &#123; 
    <span class="hljs-keyword">const</span> errorMsg = &#123; 
            <span class="hljs-attr">message</span>: <span class="hljs-string">'读取文件内容失败, 文件资源不存在'</span>, 
            <span class="hljs-attr">status</span>: <span class="hljs-number">404</span> 
        &#125;
        ctx.response.body = <span class="hljs-built_in">JSON</span>.stringify(errorMsg) 
    &#125;
    <span class="hljs-built_in">console</span>.log(filePath) 
    <span class="hljs-keyword">await</span> next() 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// file_utils.js 文件</span>
<span class="hljs-comment">// 读取文件的工具方法 </span>
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>) 

<span class="hljs-built_in">module</span>.exports.getFileJsonData = <span class="hljs-function">(<span class="hljs-params">filePath</span>) =></span> &#123; 
    <span class="hljs-comment">// 根据文件的路径, 读取文件的内容 </span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123; 
        fs.readFile(filePath, <span class="hljs-string">'utf-8'</span>, <span class="hljs-function">(<span class="hljs-params">error, data</span>) =></span> &#123; 
            <span class="hljs-keyword">if</span>(error) &#123; 
                <span class="hljs-comment">// 读取文件失败 </span>
                reject(error) 
            &#125; <span class="hljs-keyword">else</span> &#123; 
                <span class="hljs-comment">// 读取文件成功 </span>
                resolve(data) 
            &#125; 
        &#125;) 
    &#125;) 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-19">4.2.4.2.5 允许跨域</h5>
<ul>
<li>设置响应头</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123; 
    ctx.set(<span class="hljs-string">"Access-Control-Allow-Origin"</span>, <span class="hljs-string">"*"</span>) 
    ctx.set(<span class="hljs-string">"Access-Control-Allow-Methods"</span>, <span class="hljs-string">"OPTIONS, GET, PUT, POST, DELETE"</span>) 
    <span class="hljs-keyword">await</span> next(); 
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">4.3 前端部分</h2>
<h3 data-id="heading-21">4.3.1 前端项目的准备</h3>
<h4 data-id="heading-22">4.3.1.1 vue-cli 脚手架创建项目</h4>
<p><strong>vue-cli 脚手架安装</strong></p>
<pre><code class="hljs language-js copyable" lang="js">npm install -g @vue/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>创建工程项目</strong></p>
<pre><code class="hljs language-js copyable" lang="js">vue create screen
<span class="copy-code-btn">复制代码</span></code></pre>
<p>手动选择配置项如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/554db112ba7d425f9554d04df6783c29~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0119853eccb74b50b1da0407d041869d~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a831057730fc44b09e206e389bb46a01~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca693d6049284b88bee1c6571e1ecec5~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c5122dbba464bf2a30a0dbfef68b59d~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b282805961894676bfbfb86aa4ff40f2~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffa22d48d1044fd48527c5d4cfbc7079~tplv-k3u1fbpfcp-watermark.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45ba4acbf4e3412b8b924742cf5c2b24~tplv-k3u1fbpfcp-watermark.image" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffe3133790cd4ecfbf2610f06e666d1d~tplv-k3u1fbpfcp-watermark.image" alt="12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bc9323799f744aa9d7f0856694c1321~tplv-k3u1fbpfcp-watermark.image" alt="13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>安装成功执行以下命令：</p>
<pre><code class="hljs language-js copyable" lang="js">cd screen
npm run serve
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>删除无关代码</strong></p>
<ul>
<li>修改 App.vue 中的代码,将布局和样式删除, 变成如下代码：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-comment"><!-- 路由占位符 --></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>删除 components/HelloWorld.vue 这个文件</li>
<li>删除 views/About.vue 和 views/Home.vue 这两个文件</li>
<li>修改 router/index.js 中的代码,去除路由配置和 Home 组件导入的代码</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

Vue.use(VueRouter)

<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/screen'</span>
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/screen'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/screenPage'</span>)
  &#125;
]

<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  <span class="hljs-attr">base</span>: process.env.BASE_URL,
  routes
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">4.3.1.2 项目基本配置</h4>
<p>在项目根目录下创建 vue.config.js 文件，新增以下代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 使用vue-cli创建出来的vue工程, Webpack的配置是被隐藏起来了的 </span>
<span class="hljs-comment">// 如果想覆盖Webpack中的默认配置,需要在项目的根路径下增加vue.config.js文件</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">devServer</span>: &#123;
        <span class="hljs-attr">port</span>: <span class="hljs-number">8999</span>, <span class="hljs-comment">// 端口号配置</span>
        <span class="hljs-comment">// open: true // 自动打开浏览器</span>
    &#125;,
    <span class="hljs-attr">productionSourceMap</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 生产环境是否生成 sourceMap 文件</span>
    <span class="hljs-attr">configureWebpack</span>: <span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (process.env.NODE_ENV === <span class="hljs-string">'production'</span>) &#123; <span class="hljs-comment">// 为生产环境修改配置...</span>
            config.mode = <span class="hljs-string">'production'</span>;
            config[<span class="hljs-string">"performance"</span>] = &#123; <span class="hljs-comment">//打包文件大小配置</span>
                <span class="hljs-string">"maxEntrypointSize"</span>: <span class="hljs-number">10000000</span>,
                <span class="hljs-string">"maxAssetSize"</span>: <span class="hljs-number">30000000</span>
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">4.3.1.3 全局echarts对象</h4>
<ul>
<li>引入echarts文件</li>
</ul>
<p>在public/index.html文件中引入外部CDN文件echarts.min.js，如下图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/911174d2f88648118f30f3ceddcc8b4f~tplv-k3u1fbpfcp-watermark.image" alt="14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>全局echarts挂载到Vue原型对象上并使用</li>
</ul>
<p>在src/main.js文件中挂载，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 将全局的echarts对象挂载到Vue的原型对象上</span>
<span class="hljs-comment">// 在别的组件中使用 this.$echarts</span>
Vue.prototype.$echarts = <span class="hljs-built_in">window</span>.echarts
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">4.3.1.4 axios的处理</h4>
<p><strong>安装axios包</strong></p>
<pre><code class="hljs language-js copyable" lang="js">npm install axios
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>封装与使用axios</strong></p>
<p>在 src/main.js 文件中配置 axios 并且挂载到Vue的原型对象上，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 将axios挂载到Vue的原型对象上</span>
<span class="hljs-comment">// 在别的组件中使用 this.$http</span>
Vue.prototype.$http = axios
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">4.3.2 单独图表组件开发</h3>
<p>每个图表会单独进行开发，最后再将所有的图表合并到一个页面中，在单独开发每个图表的时候，一个图表会用一个单独的路径进行全屏展示，他们分别是：</p>
<ul>
<li>商家销售统计</li>
</ul>
<p><a href="http://localhost:8999/sellerPage" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8999/sellerPage</a></p>
<ul>
<li>销量趋势分析</li>
</ul>
<p><a href="http://localhost:8999/trendPage" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8999/trendPage</a></p>
<ul>
<li>商家地图分布</li>
</ul>
<p><a href="http://localhost:8999/mapPage" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8999/mapPage</a></p>
<ul>
<li>地区销量排行</li>
</ul>
<p><a href="http://localhost:8999/rankPage" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8999/rankPage</a></p>
<ul>
<li>热销商品占比</li>
</ul>
<p><a href="http://localhost:8999/hotPage" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8999/hotPage</a></p>
<ul>
<li>库存销量分析</li>
</ul>
<p><a href="http://localhost:8999/stockPage" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8999/stockPage</a></p>
<h4 data-id="heading-27">4.3.2.1 商家销量统计</h4>
<p>最终效果如下图所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f697ef35ec24b7da66df5c9cbac94db~tplv-k3u1fbpfcp-watermark.image" alt="15.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>组件结构设计</strong></p>
<p>在 src/components/ 目录下建立 Seller.vue , 这个组件是真实展示图表的组件</p>
<ul>
<li>给外层div增加类样式 com-container</li>
<li>建立一个显示图表的div元素</li>
<li>给新增的这个div增加类样式 com-chart</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"com-container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"com-chart"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"seller_ref"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript"> 
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123; 
    data () &#123; 
        <span class="hljs-keyword">return</span> &#123;&#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;&#125; 
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span> 

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span> <span class="hljs-attr">scoped</span>></span> 
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 src/views/ 目录下建立 sellerPage.vue，这个组件是对应于路由 /seller 而展示的</p>
<ul>
<li>给外层div元素增加样式 com-page</li>
<li>在 sellerPage 中引入 Seller 组件，并且注册和使用</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"com-page"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Seller</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> Seller <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/Seller"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    Seller,
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;&#125;;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;&#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span> <span class="hljs-attr">scoped</span>></span>
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>增加路由规则, 在 src/router/index.js 文件新增如下代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> routes = [ 
    &#123; 
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/sellerPage'</span>, 
        <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/sellerPage'</span>) 
    &#125; 
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建 src/assets/css/global.less 增加宽高样式</p>
<p>原则就是将所有的容器的宽度和高度设置为占满父容器</p>
<pre><code class="hljs language-js copyable" lang="js">html, 
body, 
#app &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>%;
    height: <span class="hljs-number">100</span>%;
    padding: <span class="hljs-number">0</span>;
    margin: <span class="hljs-number">0</span>;
    overflow: hidden;
&#125;

.com-page, 
.com-container,
.com-chart &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>%;
    height: <span class="hljs-number">100</span>%;
    overflow: hidden;
&#125;

canvas &#123;
    border-radius: 20px;
&#125;

.com-container &#123;
    <span class="hljs-attr">position</span>: relative;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 main.js 中引入样式</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-string">'./assets/css/global.less'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开浏览器, 输入 <a href="http://localhost:8999/sellerPage" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8999/sellerPage</a> 看Seller组件是否能够显示</p>
<p><strong>图表Seller.vue基本功能实现</strong></p>
<ul>
<li>在mounted生命周期中初始化 echartsInstance 对象</li>
<li>在mounted中获取服务器的数据</li>
<li>将获取到的数据设置到图表上</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-keyword">import</span> &#123; mapState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;
<span class="hljs-keyword">import</span> &#123; getThemeValue &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@/utils/theme_utils"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">myChart</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// echarts实例对象</span>
      <span class="hljs-attr">allData</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 服务器获取的所有数据</span>
    &#125;;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.initChart();
    <span class="hljs-built_in">this</span>.getData();
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">// 初始化echartsInstance对象</span>
    <span class="hljs-function"><span class="hljs-title">initChart</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.myChart = <span class="hljs-built_in">this</span>.$echarts.init(<span class="hljs-built_in">this</span>.$refs.seller_ref, <span class="hljs-built_in">this</span>.theme);
    &#125;,
    <span class="hljs-comment">// 获取服务端的数据</span>
   <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getData</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: ret &#125; = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.$http.get(<span class="hljs-string">"seller"</span>);
      <span class="hljs-comment">// console.log("获取后端数据===", ret);</span>
      <span class="hljs-built_in">this</span>.allData = ret;
      <span class="hljs-comment">// 对数据排序</span>
      <span class="hljs-built_in">this</span>.allData.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> a.value - b.value;
      &#125;);
      <span class="hljs-built_in">this</span>.updateChart();
    &#125;,
    <span class="hljs-comment">// 更新图表</span>
    <span class="hljs-function"><span class="hljs-title">updateChart</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> sellerName = showData.map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> item.name;
      &#125;);

      <span class="hljs-keyword">const</span> sellerValue = showData.map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> item.value;
      &#125;);

      <span class="hljs-keyword">const</span> dataOption = &#123;
        <span class="hljs-attr">xAxis</span>: &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">"value"</span>
        &#125;,
        <span class="hljs-attr">yAxis</span>: &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">"category"</span>,
          <span class="hljs-attr">data</span>: sellerName,
        &#125;,
        <span class="hljs-attr">series</span>: [
          &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">"bar"</span>,
            <span class="hljs-attr">data</span>: sellerValue,
          &#125;,
        ],
      &#125;;

      <span class="hljs-built_in">this</span>.myChart.setOption(dataOption);
    &#125;,
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拆分配置项option</p>
<p>初始化配置项</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3804591a730a4661840f7f0a10aa3cee~tplv-k3u1fbpfcp-watermark.image" alt="21.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>拥有数据之后的配置项</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1f8798144ec430287997bd87b00dd18~tplv-k3u1fbpfcp-watermark.image" alt="22.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>分页动画实现</strong></p>
<ul>
<li>数据的处理, 每5个元素显示一页</li>
</ul>
<p>数据的处理</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36330061854f4a7b93a117dedd036bc6~tplv-k3u1fbpfcp-watermark.image" alt="22.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb4f8b10d34745e89683a5fd3d4ab378~tplv-k3u1fbpfcp-watermark.image" alt="23.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f1040fc5d1c4723b61ca9982b06c394~tplv-k3u1fbpfcp-watermark.image" alt="24.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>动画的启动和停止</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd8de4f860d4441295a794e533c2f114~tplv-k3u1fbpfcp-watermark.image" alt="25.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc4aaeed261346f2bb665e82373bc395~tplv-k3u1fbpfcp-watermark.image" alt="26.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34ec94b56b324de69069830c87cdf6ef~tplv-k3u1fbpfcp-watermark.image" alt="27.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>鼠标事件的处理</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78d3b3e2e0ee41d7b062dba3082f19ab~tplv-k3u1fbpfcp-watermark.image" alt="28.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>UI效果调整</strong></p>
<p>主题的指定，在初始化echarts实例对象的时候指定</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/components/Seller.vue</span>
<span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">initChart</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.myChart = <span class="hljs-built_in">this</span>.$echarts.init(<span class="hljs-built_in">this</span>.$refs.seller_ref, <span class="hljs-string">'dark'</span>);
      <span class="hljs-comment">// 对图表对象进行鼠标事件的监听</span>
      <span class="hljs-built_in">this</span>.myChart.on(<span class="hljs-string">"mouseover"</span>, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.timer);
      &#125;);
      <span class="hljs-built_in">this</span>.myChart.on(<span class="hljs-string">"mouseout"</span>, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.startInterval();
      &#125;);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>边框圆角设置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//  src/assets/css/global.less</span>
canvas &#123;
    border-radius: 20px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他图标样式配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 标题的位置和颜色</span>
<span class="hljs-keyword">const</span> initOption = &#123;
    <span class="hljs-attr">title</span>: &#123;
      <span class="hljs-attr">text</span>: <span class="hljs-string">"▎ 商家销售统计"</span>,
      <span class="hljs-attr">textStyle</span>: &#123;
        <span class="hljs-attr">fontSize</span>: <span class="hljs-number">66</span>,
      &#125;,
      <span class="hljs-attr">left</span>: <span class="hljs-number">20</span>,
      <span class="hljs-attr">top</span>: <span class="hljs-number">20</span>,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 坐标轴的大小</span>
<span class="hljs-keyword">const</span> initOption = &#123;
    <span class="hljs-attr">grid</span>: &#123;
      <span class="hljs-attr">top</span>: <span class="hljs-string">"20%"</span>,
      <span class="hljs-attr">left</span>: <span class="hljs-string">"3%"</span>,
      <span class="hljs-attr">right</span>: <span class="hljs-string">"6%"</span>,
      <span class="hljs-attr">bottom</span>: <span class="hljs-string">"3%"</span>,
      <span class="hljs-attr">containLabel</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 距离包含坐标轴上的文字</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 工具提示和背景</span>
<span class="hljs-keyword">const</span> initOption = &#123;
    <span class="hljs-attr">tooltip</span>: &#123;
      <span class="hljs-attr">trigger</span>: <span class="hljs-string">"axis"</span>,
      <span class="hljs-attr">axisPointer</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'shadow'</span>
      &#125;,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 文字显示和位置</span>
<span class="hljs-keyword">const</span> initOption = &#123;
    <span class="hljs-attr">series</span>: [
      &#123;
        <span class="hljs-attr">label</span>: &#123;
          <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">position</span>: <span class="hljs-string">"right"</span>,
          <span class="hljs-attr">textStyle</span>: &#123;
            <span class="hljs-attr">color</span>: <span class="hljs-string">'#fff'</span>,
          &#125;,
        &#125;
     ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 柱宽度和柱圆角的实现</span>
<span class="hljs-keyword">const</span> initOption = &#123;
    <span class="hljs-attr">series</span>: [
      &#123;
        <span class="hljs-attr">barWidth</span>: <span class="hljs-number">66</span>,
            <span class="hljs-attr">itemStyle</span>: &#123;
              <span class="hljs-attr">barBorderRadius</span>: [<span class="hljs-number">0</span>, <span class="hljs-number">33</span>, <span class="hljs-number">33</span>, <span class="hljs-number">0</span>],
            &#125;,
        &#125;
     ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 柱颜色渐变的实现，线性渐变可以通过 LinearGradient 进行实现</span>
<span class="hljs-comment">// LinearGradient 需要传递5个参数, 前四个代表两个点的相对位置，第五个参数代表颜色变化的范围 </span>
<span class="hljs-comment">// 0, 0, 1, 0 代表的是从左往右的方向</span>
<span class="hljs-keyword">const</span> initOption = &#123;
    <span class="hljs-attr">series</span>: [
      &#123;
            <span class="hljs-attr">itemStyle</span>: &#123;
              <span class="hljs-attr">barBorderRadius</span>: [<span class="hljs-number">0</span>, <span class="hljs-number">33</span>, <span class="hljs-number">33</span>, <span class="hljs-number">0</span>],
              <span class="hljs-comment">// 指明颜色渐变的方向</span>
              <span class="hljs-comment">// 指明不同百分比之下颜色的值</span>
              <span class="hljs-attr">color</span>: &#123;
                <span class="hljs-attr">type</span>: <span class="hljs-string">"linear"</span>,
                <span class="hljs-attr">x</span>: <span class="hljs-number">0</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-number">0</span>,
                <span class="hljs-attr">x2</span>: <span class="hljs-number">1</span>,
                <span class="hljs-attr">y2</span>: <span class="hljs-number">0</span>,
                <span class="hljs-attr">colorStops</span>: [
                  &#123;
                    <span class="hljs-attr">offset</span>: <span class="hljs-number">0</span>,
                    <span class="hljs-attr">color</span>: <span class="hljs-string">"#5052EE"</span>, <span class="hljs-comment">// 0% 处的颜色</span>
                  &#125;,
                  &#123;
                    <span class="hljs-attr">offset</span>: <span class="hljs-number">1</span>,
                    <span class="hljs-attr">color</span>: <span class="hljs-string">"#AB6EE5"</span>, <span class="hljs-comment">// 100% 处的颜色</span>
                  &#125;,
                ],
                <span class="hljs-attr">global</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 缺省为 false</span>
              &#125;,
            &#125;,
        &#125;
     ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>分辨率适配</strong></p>
<ul>
<li>对窗口大小变化的事件进行监听</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"resize"</span>, <span class="hljs-built_in">this</span>.screenAdapter);
&#125;

<span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 在组件销毁时，需将监听器注销</span>
    <span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">"resize"</span>, <span class="hljs-built_in">this</span>.screenAdapter);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>获取图表容器的宽度计算字体大小</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 当浏览器的大小发生变化时，会调用的方法，来完成屏幕的适配</span>
<span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">screenAdapter</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> titleFontSize = (<span class="hljs-built_in">this</span>.$refs.seller_ref.offsetWidth / <span class="hljs-number">100</span>) * <span class="hljs-number">3.6</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>将字体大小的值设置给图表的某些区域</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 标题大小、背景大小、柱宽度、圆角大小</span>
<span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">screenAdapter</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> titleFontSize = (<span class="hljs-built_in">this</span>.$refs.seller_ref.offsetWidth / <span class="hljs-number">100</span>) * <span class="hljs-number">3.6</span>;
      <span class="hljs-keyword">const</span> adapterOption = &#123;
        <span class="hljs-attr">title</span>: &#123;
          <span class="hljs-attr">textStyle</span>: &#123;
            <span class="hljs-attr">fontSize</span>: titleFontSize,
          &#125;,
        &#125;,
        <span class="hljs-attr">tooltip</span>: &#123;
          <span class="hljs-attr">axisPointer</span>: &#123;
            <span class="hljs-attr">lineStyle</span>: &#123;
              <span class="hljs-attr">width</span>: titleFontSize,
            &#125;,
          &#125;,
        &#125;,
        <span class="hljs-attr">series</span>: [
          &#123;
            <span class="hljs-attr">barWidth</span>: titleFontSize,
            <span class="hljs-attr">itemStyle</span>: &#123;
              <span class="hljs-attr">borderRadius</span>: [<span class="hljs-number">0</span>, titleFontSize / <span class="hljs-number">2</span>, titleFontSize / <span class="hljs-number">2</span>, <span class="hljs-number">0</span>],
            &#125;,
          &#125;,
        ],
      &#125;;
      <span class="hljs-built_in">this</span>.myChart.setOption(adapterOption);
      <span class="hljs-comment">// 手动调用图表对象的resize才能生效</span>
      <span class="hljs-built_in">this</span>.myChart.resize();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">4.3.2.2 销量趋势分析</h4>
<p>最终效果如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/deec27b1392f4c66b4c1af3a22f4c785~tplv-k3u1fbpfcp-watermark.image" alt="17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>代码环境准备</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// trendPage.vue</span>
<span class="hljs-comment">// 针对于 /trendPage 这条路径而显示出来的 在这个组件中, 通过子组件注册的方式, 要显示出Trend.vue这个组件</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"com-page"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Trend</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> Trend <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/Trend"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    Trend,
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;&#125;;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;&#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span> <span class="hljs-attr">scoped</span>></span>
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Trend.vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"com-container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"com-chart"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"trend_ref"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">myChart</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">allData</span>: <span class="hljs-literal">null</span>
    &#125;;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.initChart();
    <span class="hljs-built_in">this</span>.getData();
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"resize"</span>, <span class="hljs-built_in">this</span>.screenAdapter);
    <span class="hljs-built_in">this</span>.screenAdapter();
  &#125;,
  <span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">"resize"</span>, <span class="hljs-built_in">this</span>.screenAdapter);
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">initChart</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.myChart = <span class="hljs-built_in">this</span>.$echarts.init(<span class="hljs-built_in">this</span>.$refs.trend_ref, <span class="hljs-string">'dark'</span>);
      <span class="hljs-keyword">const</span> initOption = &#123;&#125;;
      <span class="hljs-built_in">this</span>.myChart.setOption(initOption);
    &#125;,
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getData</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: ret &#125; = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.$http.get(<span class="hljs-string">"trend"</span>);
      <span class="hljs-built_in">this</span>.allData = ret;
      <span class="hljs-built_in">this</span>.updateChart();
    &#125;,
    <span class="hljs-function"><span class="hljs-title">updateChart</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> dataOption = &#123;&#125;;
      <span class="hljs-built_in">this</span>.myChart.setOption(dataOption);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">screenAdapter</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> adapterOption = &#123;&#125;;
      <span class="hljs-built_in">this</span>.myChart.setOption(adapterOption);
      <span class="hljs-built_in">this</span>.myChart.resize();
    &#125;
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span> <span class="hljs-attr">scoped</span>></span>
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// router/index.js</span>
<span class="hljs-keyword">const</span> routes = [
  &#123;
     <span class="hljs-attr">path</span>: <span class="hljs-string">'/trendPage'</span>,
     <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/trendPage'</span>)
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>图表基本功能的实现</li>
</ul>
<p>数据的获取</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 获取服务器的数据, 对this.allData进行赋值之后, 调用updateChart方法更新图表</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getData</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: ret &#125; = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.$http.get(<span class="hljs-string">"trend"</span>);
  <span class="hljs-built_in">this</span>.allData = ret;
  <span class="hljs-built_in">this</span>.updateChart();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数据的处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">updateChart</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-comment">// 类目轴数据</span>
  <span class="hljs-keyword">const</span> timeArr = <span class="hljs-built_in">this</span>.allData.common.month;
  <span class="hljs-comment">// y轴数据 series下的数据</span>
  <span class="hljs-comment">// map代表地区销量趋势 </span>
  <span class="hljs-comment">// seller代表商家销量趋势 </span>
  <span class="hljs-comment">// commodity代表商品销量趋势</span>
  <span class="hljs-keyword">const</span> valueArr = <span class="hljs-built_in">this</span>.allData.map.data;
  <span class="hljs-comment">// 图表数据, 一个图表中显示5条折线图</span>
  <span class="hljs-keyword">const</span> seriesArr = valueArr.map(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">name</span>: item.name,
      <span class="hljs-attr">type</span>: <span class="hljs-string">"line"</span>,
      <span class="hljs-attr">data</span>: item.data,
      <span class="hljs-attr">smooth</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">stack</span>: <span class="hljs-string">'map'</span> <span class="hljs-comment">// stack值相同, 可以形成堆叠图效果</span>
    &#125;;
  &#125;);
  <span class="hljs-comment">// 图例数据</span>
  <span class="hljs-keyword">const</span> legendArr = valueArr.map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> item.name;
  &#125;);
  <span class="hljs-keyword">const</span> dataOption = &#123;
    <span class="hljs-attr">xAxis</span>: &#123;
      <span class="hljs-attr">data</span>: timeArr,
    &#125;,
    <span class="hljs-attr">legend</span>: &#123;
      <span class="hljs-attr">data</span>: legendArr,
    &#125;,
    <span class="hljs-attr">series</span>: seriesArr,
  &#125;;
  <span class="hljs-built_in">this</span>.myChart.setOption(dataOption);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> initOption = &#123;
    <span class="hljs-attr">xAxis</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">"category"</span>,
        <span class="hljs-attr">boundaryGap</span>: <span class="hljs-literal">false</span>
    &#125;,
    <span class="hljs-attr">yAxis</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">"value"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>UI效果调整</li>
</ul>
<p>主题的使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">initChart</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-built_in">this</span>.myChart = <span class="hljs-built_in">this</span>.$echarts.init(<span class="hljs-built_in">this</span>.$refs.trend_ref, <span class="hljs-string">'dark'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>坐标轴大小和位置，工具提示，图例位置和形状</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> initOption = &#123;
    <span class="hljs-comment">// 坐标轴大小和位置</span>
    <span class="hljs-attr">grid</span>: &#123;
      <span class="hljs-attr">left</span>: <span class="hljs-string">"3%"</span>,
      <span class="hljs-attr">top</span>: <span class="hljs-string">"30%"</span>,
      <span class="hljs-attr">right</span>: <span class="hljs-string">"4%"</span>,
      <span class="hljs-attr">bottom</span>: <span class="hljs-string">"1%"</span>,
      <span class="hljs-attr">containLabel</span>: <span class="hljs-literal">true</span>,
    &#125;,
    <span class="hljs-comment">// 工具提示</span>
    <span class="hljs-attr">tooltip</span>: &#123;
      <span class="hljs-attr">trigger</span>: <span class="hljs-string">"axis"</span>,
    &#125;,
    <span class="hljs-comment">// 图例位置和形状</span>
    <span class="hljs-attr">legend</span>: &#123;
      <span class="hljs-attr">left</span>: <span class="hljs-number">20</span>,
      <span class="hljs-attr">top</span>: <span class="hljs-string">"15%"</span>,
      <span class="hljs-attr">icon</span>: <span class="hljs-string">"circle"</span>,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>区域面积和颜色渐变的设置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">updateChart</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 半透明颜色值</span>
      <span class="hljs-keyword">const</span> colorArr1 = [
        <span class="hljs-string">"rgba(73, 146, 255, .5)"</span>,
        <span class="hljs-string">"rgba(124, 255, 178, .5)"</span>,
        <span class="hljs-string">"rgba(253, 221, 96, .5)"</span>,
        <span class="hljs-string">"rgba(255, 110, 118, .5)"</span>,
        <span class="hljs-string">"rgba(88, 217, 249, .5)"</span>,
      ];
      <span class="hljs-comment">// 全透明颜色值</span>
      <span class="hljs-keyword">const</span> colorArr2 = [
        <span class="hljs-string">"rgba(73, 146, 255, 0)"</span>,
        <span class="hljs-string">"rgba(124, 255, 178, 0)"</span>,
        <span class="hljs-string">"rgba(253, 221, 96, 0)"</span>,
        <span class="hljs-string">"rgba(255, 110, 118, 0)"</span>,
        <span class="hljs-string">"rgba(88, 217, 249, 0)"</span>,
      ];
      <span class="hljs-keyword">const</span> seriesArr = valueArr.map(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-comment">// 区域面积只需要给series的每一个对象增加一个 areaStyle 即可</span>
          <span class="hljs-attr">areaStyle</span>: &#123;
            <span class="hljs-comment">// 颜色渐变可以通过 LinearGradient 进行设置, 颜色渐变的方向从上往下</span>
            <span class="hljs-attr">color</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">this</span>.$echarts.graphic.LinearGradient(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>, [
              &#123;
                <span class="hljs-attr">offset</span>: <span class="hljs-number">0</span>,
                <span class="hljs-attr">color</span>: colorArr1[index],
              &#125;,
              &#123;
                <span class="hljs-attr">offset</span>: <span class="hljs-number">1</span>,
                <span class="hljs-attr">color</span>: colorArr2[index],
              &#125;,
            ]),
          &#125;,
        &#125;;
      &#125;);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>切换图表</p>
</li>
<li>
<p>分辨率适配</p>
</li>
</ul>
<p>分辨率适配主要就是在 screenAdapter 方法中进行, 需要获取图表容器的宽度，计算出标题字体大小，将字体的大小赋值给 titleFontSize</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">titleFontSize</span>: <span class="hljs-number">0</span>
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">screenAdapter</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-built_in">this</span>.titleFontSize = (<span class="hljs-built_in">this</span>.$refs.trend_ref.offsetWidth / <span class="hljs-number">100</span>) * <span class="hljs-number">3.6</span>;
        &#125;
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 titleFontSize 去设置给标题文字的大小和图例的大小</p>
<p>标题文字的大小，增加计算属性comStyle并设置给对应的div，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"com-container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"title"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"comStyle"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; "▎ " + showTitle &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">"iconfont icon-arrow-down title-icon"</span>
        <span class="hljs-attr">:style</span>=<span class="hljs-string">"comStyle"</span>
        @<span class="hljs-attr">click</span>=<span class="hljs-string">"showChoice = !showChoice"</span>
      ></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">titleFontSize</span>: <span class="hljs-number">0</span>
        &#125;
    &#125;,
    <span class="hljs-attr">computed</span>: &#123;
        <span class="hljs-comment">// 设置给标题的样式</span>
        <span class="hljs-function"><span class="hljs-title">comStyle</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">fontSize</span>: <span class="hljs-built_in">this</span>.titleFontSize + <span class="hljs-string">"px"</span>
          &#125;;
        &#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>图例的大小</p>
<pre><code class="hljs language-js copyable" lang="js">methods: &#123;
    <span class="hljs-function"><span class="hljs-title">screenAdapter</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.titleFontSize = (<span class="hljs-built_in">this</span>.$refs.trend_ref.offsetWidth / <span class="hljs-number">100</span>) * <span class="hljs-number">3.6</span>;
      <span class="hljs-keyword">const</span> adapterOption = &#123;
        <span class="hljs-attr">legend</span>: &#123;
          <span class="hljs-attr">itemWidth</span>: <span class="hljs-built_in">this</span>.titleFontSize,
          <span class="hljs-attr">itemHeight</span>: <span class="hljs-built_in">this</span>.titleFontSize,
          <span class="hljs-attr">itemGap</span>: <span class="hljs-built_in">this</span>.titleFontSize,
          <span class="hljs-attr">textStyle</span>: &#123;
            <span class="hljs-attr">fontSize</span>: <span class="hljs-built_in">this</span>.titleFontSize / <span class="hljs-number">2</span>,
          &#125;,
        &#125;,
      &#125;;
      <span class="hljs-built_in">this</span>.myChart.setOption(adapterOption);
      <span class="hljs-built_in">this</span>.myChart.resize();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">4.3.2.3 商家地图分布</h4>
<p>最终效果如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c57e5d8dbbd549c49073f1b1c80b9d11~tplv-k3u1fbpfcp-watermark.image" alt="18.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>如需获取更多资料及思维导图，可以关注作者公众号《懒人码农》，后台回复关键词“大屏”即可获取</p>
</blockquote>
<p>查看完整源代码，请移步到github访问👉：<a href="https://github.com/jackchen0120/EC-Platform-Monitor" target="_blank" rel="nofollow noopener noreferrer">github.com/jackchen012…</a></p>
<h4 data-id="heading-30">4.3.2.4 地区销量排行</h4>
<p>最终效果如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32b6d14f923440c0a23ec24f8253df6b~tplv-k3u1fbpfcp-watermark.image" alt="16.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-31">4.3.2.5 热销商品占比</h4>
<p>最终效果如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67f8a7e28de647b6a832db89e50eebdc~tplv-k3u1fbpfcp-watermark.image" alt="19.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-32">4.3.2.6 库存销量分析</h4>
<p>最终效果如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55fa8d7704c54a28b76a3376b556f69a~tplv-k3u1fbpfcp-watermark.image" alt="20.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-33">4.3.3 WebScoket的使用</h3>
<h4 data-id="heading-34">4.3.3.1 后端代码</h4>
<p><strong>安装WebSocket包</strong></p>
<pre><code class="hljs language-js copyable" lang="js">npm install ws -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>创建 service\web_socket_service.js 文件</strong></p>
<ul>
<li>创建WebSocket实例对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> WebSocket = <span class="hljs-built_in">require</span>(<span class="hljs-string">'ws'</span>);
<span class="hljs-comment">// 创建websocket服务端的对象，绑定端口号为9998</span>
<span class="hljs-keyword">const</span> wss = <span class="hljs-keyword">new</span> WebSocket.Server(&#123;
<span class="hljs-attr">port</span>: <span class="hljs-number">9998</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>监听事件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">wss.on(<span class="hljs-string">"connection"</span>, <span class="hljs-function"><span class="hljs-params">client</span> =></span> &#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"有客户端连接..."</span>) 
    client.on(<span class="hljs-string">"message"</span>, <span class="hljs-function"><span class="hljs-params">msg</span> =></span> &#123; 
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"客户端发送数据过来了"</span>) 
        <span class="hljs-comment">// 发送数据给客户端 </span>
        client.send(<span class="hljs-string">'hello socket'</span>) 
    &#125;) 
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在app.js中引入web_scoket_service.js这个文件，并调用listen方法</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> webSocketService = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./service/web_socket_service'</span>)
<span class="hljs-comment">// 开启服务端的监听，监听客户端的连接</span>
<span class="hljs-comment">// 当某一个客户端连接成功之后，就会对这个客户端进行message事件的监听</span>
webSocketService.listen()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>约定好喝客户端之前数据交互的格式和含义</li>
</ul>
<p>客户端和服务端之间的数据交互采用 JSON 格式</p>
<p>客户端发送数据给服务端的字段如下：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123; 
  <span class="hljs-string">"action"</span>: <span class="hljs-string">"getData"</span>, 
  <span class="hljs-string">"socketType"</span>: <span class="hljs-string">"trendData"</span>, 
  <span class="hljs-string">"chartName"</span>: <span class="hljs-string">"trend"</span>, 
  <span class="hljs-string">"value"</span>: <span class="hljs-string">""</span> 
&#125;
或者
&#123; 
  <span class="hljs-string">"action"</span>: <span class="hljs-string">"fullScreen"</span>, 
  <span class="hljs-string">"socketType"</span>: <span class="hljs-string">"fullScreen"</span>, 
  <span class="hljs-string">"chartName"</span>: <span class="hljs-string">"trend"</span>, 
  <span class="hljs-string">"value"</span>: <span class="hljs-literal">true</span> 
&#125;
或者
&#123; 
  <span class="hljs-string">"action"</span>: <span class="hljs-string">"themeChange"</span>, 
  <span class="hljs-string">"socketType"</span>: <span class="hljs-string">"themeChange"</span>, 
  <span class="hljs-string">"chartName"</span>: <span class="hljs-string">""</span>, 
  <span class="hljs-string">"value"</span>: <span class="hljs-string">"dark"</span> 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>action : 代表某项行为,可选值有</strong></p>
<ul>
<li>getData 代表获取图表数据</li>
<li>fullScreen 代表产生了全屏事件</li>
<li>themeChange 代表产生了主题切换的事件</li>
</ul>
<p><strong>socketType : 代表业务模块类型, 这个值代表前端注册数据回调函数的标识, 可选值有:</strong></p>
<ul>
<li>trendData</li>
<li>sellerData</li>
<li>mapData</li>
<li>rankData</li>
<li>hotData</li>
<li>stockData</li>
<li>fullScreen</li>
<li>themeChange</li>
</ul>
<p><strong>chartName : 代表图表名称, 如果是主题切换事件, 可不传此值, 可选值有:</strong></p>
<ul>
<li>trend</li>
<li>seller</li>
<li>map</li>
<li>rank</li>
<li>hot</li>
<li>stock</li>
</ul>
<p><strong>value : 代表 具体的数据值, 在获取图表数据时, 可不传此值, 可选值有</strong></p>
<ul>
<li>如果是全屏事件, true 代表全屏, false 代表非全屏</li>
<li>如果是主题切换事件, 可选值有 chalk 或者 vintage</li>
</ul>
<p><strong>服务端发送给客户端的数据如下:</strong></p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-string">"action"</span>: <span class="hljs-string">"getData"</span>,
    <span class="hljs-string">"socketType"</span>: <span class="hljs-string">"trendData"</span>,
    <span class="hljs-string">"chartName"</span>: <span class="hljs-string">"trend"</span>,
    <span class="hljs-string">"value"</span>: <span class="hljs-string">""</span>,
    <span class="hljs-string">"data"</span>: <span class="hljs-string">"从文件读取出来的json文件的内容"</span>
&#125;
或者
&#123;
    <span class="hljs-string">"action"</span>: <span class="hljs-string">"fullScreen"</span>,
    <span class="hljs-string">"socketType"</span>: <span class="hljs-string">"fullScreen"</span>,
    <span class="hljs-string">"chartName"</span>: <span class="hljs-string">"trend"</span>,
    <span class="hljs-string">"value"</span>: <span class="hljs-literal">true</span>
&#125;
或者
 &#123;
    <span class="hljs-string">"action"</span>: <span class="hljs-string">"themeChange"</span>,
    <span class="hljs-string">"socketType"</span>: <span class="hljs-string">"themeChange"</span>,
    <span class="hljs-string">"chartName"</span>: <span class="hljs-string">""</span>,
    <span class="hljs-string">"value"</span>: <span class="hljs-string">"dark"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意, 除了 action 为 getData 时, 服务器会在客户端发过来数据的基础之上, 增加 data 字段，其他的情况, 服务器会原封不动的将从某一个客户端发过来的数据转发给每一个处于连接状态
的客户端</p>
<ul>
<li>代码实现</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> fileUtils = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../utils/file_utils'</span>);
<span class="hljs-keyword">const</span> WebSocket = <span class="hljs-built_in">require</span>(<span class="hljs-string">'ws'</span>);
<span class="hljs-comment">// 创建websocket服务端的对象，绑定端口号为9998</span>
<span class="hljs-keyword">const</span> wss = <span class="hljs-keyword">new</span> WebSocket.Server(&#123;
<span class="hljs-attr">port</span>: <span class="hljs-number">9998</span>
&#125;)

<span class="hljs-built_in">module</span>.exports.listen = <span class="hljs-function">() =></span> &#123;
<span class="hljs-comment">// 对客户端的连接事件进行监听</span>
<span class="hljs-comment">// client代表是客户端的连接socket对象</span>
wss.on(<span class="hljs-string">'connection'</span>, <span class="hljs-function"><span class="hljs-params">client</span> =></span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'有客户端连接成功...'</span>);
<span class="hljs-comment">// 对客户端的连接对象进行message事件的监听</span>
<span class="hljs-comment">// msg由客户端发送给服务端的数据</span>
client.on(<span class="hljs-string">'message'</span>, <span class="hljs-keyword">async</span> msg => &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'客户端发送数据给服务端==='</span>, msg);
<span class="hljs-keyword">let</span> payload = <span class="hljs-built_in">JSON</span>.parse(msg);
<span class="hljs-keyword">const</span> action = payload.action;
<span class="hljs-keyword">if</span> (action === <span class="hljs-string">'getData'</span>) &#123;
<span class="hljs-keyword">let</span> filePath = <span class="hljs-string">'../data/'</span> + payload.chartName + <span class="hljs-string">'.json'</span>;
<span class="hljs-comment">// trend seller map rank hot stock</span>
<span class="hljs-comment">// payload.chartName</span>
filePath = path.join(__dirname, filePath);
<span class="hljs-keyword">const</span> ret = <span class="hljs-keyword">await</span> fileUtils.getFileJsonData(filePath);
<span class="hljs-comment">// 需要在服务端获取到数据的基础之上，增加一个data的字段</span>
<span class="hljs-comment">// data所对应的值，就是某个json文件的内容</span>
payload.data = ret;
client.send(<span class="hljs-built_in">JSON</span>.stringify(payload));
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-comment">// 原封不动的将所接收到的数据转发给每一个处于连接状态的客户端</span>
<span class="hljs-comment">// wss.clients 所有客户端的连接</span>
wss.clients.forEach(<span class="hljs-function"><span class="hljs-params">client</span> =></span> &#123;
client.send(msg);
&#125;)
&#125;
<span class="hljs-comment">// 服务端向客户端发送数据</span>
<span class="hljs-comment">// client.send('hello socket form backend');</span>
&#125;)
&#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-35">4.3.3.2 前端代码</h4>
<ul>
<li>定义单例，创建WebSocket实例对象</li>
</ul>
<p>创建scr/utils/socket_service.js文件，定义单例代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SocketService</span> </span>&#123;
  <span class="hljs-comment">// 单例模式</span>

  <span class="hljs-keyword">static</span> instance = <span class="hljs-literal">null</span>;
  <span class="hljs-keyword">static</span> get Instance () &#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.instance) &#123;
      <span class="hljs-built_in">this</span>.instance = <span class="hljs-keyword">new</span> SocketService();
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.instance;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>监听WebSocket事件</li>
</ul>
<p>定义connect函数，将创建的WebSocket赋值给实例属性，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 实例属性ws和服务端连接的socket对象</span>
ws = <span class="hljs-literal">null</span>;

<span class="hljs-comment">// 定义连接服务器的方法</span>
connect () &#123;
    <span class="hljs-comment">// 连接服务器</span>
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">window</span>.WebSocket) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'您的浏览器不支持websocket'</span>);
    &#125;
    <span class="hljs-built_in">this</span>.ws = <span class="hljs-keyword">new</span> WebSocket(<span class="hljs-string">`ws://106.55.168.13:9998/ws/webSocket`</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>监听事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">connect</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">window</span>.WebSocket) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'您的浏览器不支持 WebSocket!'</span>)
  &#125;
  <span class="hljs-built_in">this</span>.ws = <span class="hljs-keyword">new</span> WebSocket(<span class="hljs-string">'ws://localhost:9998'</span>)
  <span class="hljs-comment">// 监听连接成功 </span>
  <span class="hljs-built_in">this</span>.ws.onopen = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'WebSocket 连接成功'</span>)
  &#125;
  <span class="hljs-comment">// 服务器连接不成功，服务器关闭了连接 </span>
  <span class="hljs-built_in">this</span>.ws.onclose = <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'服务器关闭了连接'</span>)
  &#125;
  <span class="hljs-comment">// 监听接收消息 </span>
  <span class="hljs-built_in">this</span>.ws.onmessage = <span class="hljs-function"><span class="hljs-params">msg</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'WebSocket 接收到数据'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义注册函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SocketService</span> </span>&#123; 
  <span class="hljs-comment">// 业务类型和回调函数的对于关系 </span>
  callBackMapping = &#123;&#125; 
  <span class="hljs-comment">/*** socketType 
   * trendData sellerData mapData rankData hotData stockData 
   * fullScreen 
   * themeChange 
   * callBack 
   * 回调函数 
  */</span> 
 registerCallBack (socketType, callBack) &#123; 
   <span class="hljs-comment">// 往 callBackMap中存放回调函数 </span>
   <span class="hljs-built_in">this</span>.callBackMapping[socketType] = callBack 
  &#125;
  unRegisterCallBack (socketType) &#123; 
    <span class="hljs-built_in">this</span>.callBackMapping[socketType] = <span class="hljs-literal">null</span> 
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>连接服务端</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在 main.js 中连接服务器端</span>
<span class="hljs-keyword">import</span> SocketService <span class="hljs-keyword">from</span> <span class="hljs-string">'@/utils/socket_service'</span> SocketService.Instance.connect()

<span class="hljs-comment">// 将 SocketService 实例对象挂载到 Vue 的原型对象上</span>
Vue.prototype.$socket = SocketService.Instance
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发送数据给服务端</p>
<p>在 socket_service.js 中定义发送数据的方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SocketService</span> </span>&#123;
    send (data) &#123; 
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'发送数据给服务器:'</span>) 
        <span class="hljs-built_in">this</span>.ws.send(<span class="hljs-built_in">JSON</span>.stringify(data)) 
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先修改 Trend.vue 文件，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 当socket来数据的时候, 会调用getData这个函数 </span>
    <span class="hljs-built_in">this</span>.$socket.registerCallBack(<span class="hljs-string">'trendData'</span>, <span class="hljs-built_in">this</span>.getData)
    <span class="hljs-comment">// 往 socket 发送数据, 目的是想让服务端传输销量趋势这个模块的数据</span>
    <span class="hljs-built_in">this</span>.initChart();
    <span class="hljs-comment">// this.getData();</span>
    <span class="hljs-comment">// 发送数据给服务端，告诉服务端，前端现在需要数据</span>
    <span class="hljs-built_in">this</span>.$socket.send(&#123;
      <span class="hljs-attr">action</span>: <span class="hljs-string">"getData"</span>,
      <span class="hljs-attr">socketType</span>: <span class="hljs-string">"trendData"</span>,
      <span class="hljs-attr">chartName</span>: <span class="hljs-string">"trend"</span>,
      <span class="hljs-attr">value</span>: <span class="hljs-string">""</span>
    &#125;)
&#125;
<span class="hljs-comment">// action的值不变，都是getData </span>
<span class="hljs-comment">// socketType的可选值有：trendData,sellerData,mapData,rankData,hotData,stockData</span>
<span class="hljs-comment">// chartName的可选值有: trend,seller,map,rank,hot,stock</span>

destroyed () &#123; 
    <span class="hljs-built_in">this</span>.$socket.unRegisterCallBack(<span class="hljs-string">'trendData'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行代码, 发现数据发不出去</p>
<p>因为在刷新界面之后, 客户端和服务端的连接并不会立马连接成功, 在处于连接状态下就调用
send 是发送不成功的, 因此需要修改 service_socket.js 中的 send 方法进行容错处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 标识是否连接成功</span>
connected = <span class="hljs-literal">false</span>;

<span class="hljs-comment">// 记录重试的次数</span>
sendRetryCount = <span class="hljs-number">0</span>;

<span class="hljs-comment">// 发送数据的方法</span>
send (data) &#123;
    <span class="hljs-comment">// 判断现在是否有连接成功</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.connected) &#123;
      <span class="hljs-built_in">this</span>.sendRetryCount = <span class="hljs-number">0</span>;
      <span class="hljs-built_in">this</span>.ws.send(<span class="hljs-built_in">JSON</span>.stringify(data));
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.sendRetryCount++;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.send(data);
      &#125;, <span class="hljs-built_in">this</span>.sendRetryCount * <span class="hljs-number">500</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 onopen 时设置 connected 的值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义连接服务器的方法</span>
connect () &#123;
    <span class="hljs-comment">// 连接成功的事件</span>
    <span class="hljs-built_in">this</span>.ws.onopen = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'连接服务端成功'</span>);
      <span class="hljs-built_in">this</span>.connected = <span class="hljs-literal">true</span>;
      <span class="hljs-built_in">this</span>.connectRetryCount = <span class="hljs-number">0</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 socket_service.js 中修改接收到消息的代码处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义连接服务器的方法</span>
connect () &#123;
    <span class="hljs-comment">// 得到服务端发送过来的数据</span>
    <span class="hljs-built_in">this</span>.ws.onmessage = <span class="hljs-function"><span class="hljs-params">msg</span> =></span> &#123;
      <span class="hljs-comment">// console.log('从服务端获取到的数据===', msg);</span>
      <span class="hljs-comment">// 真正服务端发送过来的原始数据时在msg中的data字段</span>
      <span class="hljs-keyword">const</span> recvData = <span class="hljs-built_in">JSON</span>.parse(msg.data);
      <span class="hljs-keyword">const</span> socketType = recvData.socketType;
      <span class="hljs-comment">// 判断回调函数是否存在</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.callBackMapping[socketType]) &#123;
        <span class="hljs-keyword">const</span> action = recvData.action
        <span class="hljs-keyword">if</span> (action === <span class="hljs-string">'getData'</span>) &#123;
          <span class="hljs-keyword">const</span> realData = <span class="hljs-built_in">JSON</span>.parse(recvData.data);
          <span class="hljs-built_in">this</span>.callBackMapping[socketType].call(<span class="hljs-built_in">this</span>, realData);
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (action === <span class="hljs-string">'fullScreen'</span>) &#123;
          <span class="hljs-built_in">this</span>.callBackMapping[socketType].call(<span class="hljs-built_in">this</span>, recvData);
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (action === <span class="hljs-string">'themeChange'</span>) &#123;
          <span class="hljs-built_in">this</span>.callBackMapping[socketType].call(<span class="hljs-built_in">this</span>, recvData);
        &#125;
      &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>断开重连机制</p>
<p>如果初始化连接服务端不成功, 或者连接成功了, 后来服务器关闭了, 这两种情况都会触发 onclose 事件,我们需要在这个事件中,进行重连</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">connect</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 监听连接成功 </span>
    <span class="hljs-built_in">this</span>.ws.onopen = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 连接成功之后, 重置重连次数</span>
      <span class="hljs-built_in">this</span>.connectRetryCount = <span class="hljs-number">0</span>; 
    &#125;
    <span class="hljs-comment">// 连接服务端失败</span>
    <span class="hljs-comment">// 当连接成功之后，服务端关闭的情况</span>
    <span class="hljs-built_in">this</span>.ws.onclose = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'连接服务端失败'</span>);
      <span class="hljs-built_in">this</span>.connected = <span class="hljs-literal">false</span>;
      <span class="hljs-built_in">this</span>.connectRetryCount++;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.connect();
      &#125;, <span class="hljs-built_in">this</span>.connectRetryCount * <span class="hljs-number">500</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">4.3.4 组件合并</h3>
<ul>
<li>创建screenPage.vue文件，并配置路由规则，代码如下：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// router/index.js</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

Vue.use(VueRouter)

<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/screen'</span>
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/screen'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/screenPage'</span>)
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>代码实现</li>
</ul>
<p>静态图片资源放在public/static/img目录之下，完整代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// screenPage.vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"screen-container"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"containerStyle"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">header</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"screen-header"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"headerSrc"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"logo"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"logoSrc"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"title"</span>></span>电商平台数据大屏实时监控系统<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"title-right"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"themeSrc"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"qiehuan"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleChangeTheme"</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"datetime"</span>></span>&#123;&#123; timeValue &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">header</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"screen-body"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">section</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"screen-left"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>
          <span class="hljs-attr">id</span>=<span class="hljs-string">"left-top"</span>
          <span class="hljs-attr">:class</span>=<span class="hljs-string">"[fullScreenStatus.trend ? 'fullscreen' : '']"</span>
        ></span>
          <span class="hljs-comment"><!-- 销量趋势图表 --></span>
          <span class="hljs-tag"><<span class="hljs-name">Trend</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"trend"</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"resize"</span>></span>
            <span class="hljs-comment"><!-- icon-compress-alt --></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>
              @<span class="hljs-attr">click</span>=<span class="hljs-string">"changeSize('trend')"</span>
              <span class="hljs-attr">:class</span>=<span class="hljs-string">"[
                'iconfont',
                fullScreenStatus.trend
                  ? 'icon-compress-alt'
                  : 'icon-expand-alt',
              ]"</span>
            ></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>
          <span class="hljs-attr">id</span>=<span class="hljs-string">"left-bottom"</span>
          <span class="hljs-attr">:class</span>=<span class="hljs-string">"[fullScreenStatus.seller ? 'fullscreen' : '']"</span>
        ></span>
          <span class="hljs-comment"><!-- 商家销售金额图表 --></span>
          <span class="hljs-tag"><<span class="hljs-name">Seller</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"seller"</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"resize"</span>></span>
            <span class="hljs-comment"><!-- icon-compress-alt --></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>
              @<span class="hljs-attr">click</span>=<span class="hljs-string">"changeSize('seller')"</span>
              <span class="hljs-attr">:class</span>=<span class="hljs-string">"[
                'iconfont',
                fullScreenStatus.seller
                  ? 'icon-compress-alt'
                  : 'icon-expand-alt',
              ]"</span>
            ></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">section</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"screen-middle"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>
          <span class="hljs-attr">id</span>=<span class="hljs-string">"middle-top"</span>
          <span class="hljs-attr">:class</span>=<span class="hljs-string">"[fullScreenStatus.map ? 'fullscreen' : '']"</span>
        ></span>
          <span class="hljs-comment"><!-- 商家分布图表 --></span>
          <span class="hljs-tag"><<span class="hljs-name">Map</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"map"</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"resize"</span>></span>
            <span class="hljs-comment"><!-- icon-compress-alt --></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>
              @<span class="hljs-attr">click</span>=<span class="hljs-string">"changeSize('map')"</span>
              <span class="hljs-attr">:class</span>=<span class="hljs-string">"[
                'iconfont',
                fullScreenStatus.map ? 'icon-compress-alt' : 'icon-expand-alt',
              ]"</span>
            ></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>
          <span class="hljs-attr">id</span>=<span class="hljs-string">"middle-bottom"</span>
          <span class="hljs-attr">:class</span>=<span class="hljs-string">"[fullScreenStatus.rank ? 'fullscreen' : '']"</span>
        ></span>
          <span class="hljs-comment"><!-- 地区销量排行图表 --></span>
          <span class="hljs-tag"><<span class="hljs-name">Rank</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"rank"</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"resize"</span>></span>
            <span class="hljs-comment"><!-- icon-compress-alt --></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>
              @<span class="hljs-attr">click</span>=<span class="hljs-string">"changeSize('rank')"</span>
              <span class="hljs-attr">:class</span>=<span class="hljs-string">"[
                'iconfont',
                fullScreenStatus.rank ? 'icon-compress-alt' : 'icon-expand-alt',
              ]"</span>
            ></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">section</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"screen-right"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"right-top"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"[fullScreenStatus.hot ? 'fullscreen' : '']"</span>></span>
          <span class="hljs-comment"><!-- 热销商品占比图表 --></span>
          <span class="hljs-tag"><<span class="hljs-name">hot</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"hot"</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"resize"</span>></span>
            <span class="hljs-comment"><!-- icon-compress-alt --></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>
              @<span class="hljs-attr">click</span>=<span class="hljs-string">"changeSize('hot')"</span>
              <span class="hljs-attr">:class</span>=<span class="hljs-string">"[
                'iconfont',
                fullScreenStatus.hot ? 'icon-compress-alt' : 'icon-expand-alt',
              ]"</span>
            ></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>
          <span class="hljs-attr">id</span>=<span class="hljs-string">"right-bottom"</span>
          <span class="hljs-attr">:class</span>=<span class="hljs-string">"[fullScreenStatus.stock ? 'fullscreen' : '']"</span>
        ></span>
          <span class="hljs-comment"><!-- 库存销量分析图表 --></span>
          <span class="hljs-tag"><<span class="hljs-name">Stock</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"stock"</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"resize"</span>></span>
            <span class="hljs-comment"><!-- icon-compress-alt --></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>
              @<span class="hljs-attr">click</span>=<span class="hljs-string">"changeSize('stock')"</span>
              <span class="hljs-attr">:class</span>=<span class="hljs-string">"[
                'iconfont',
                fullScreenStatus.stock
                  ? 'icon-compress-alt'
                  : 'icon-expand-alt',
              ]"</span>
            ></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> Hot <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/Hot.vue"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-built_in">Map</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/Map.vue"</span>;
<span class="hljs-keyword">import</span> Rank <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/Rank.vue"</span>;
<span class="hljs-keyword">import</span> Seller <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/Seller.vue"</span>;
<span class="hljs-keyword">import</span> Stock <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/Stock.vue"</span>;
<span class="hljs-keyword">import</span> Trend <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/Trend.vue"</span>;
<span class="hljs-keyword">import</span> &#123; mapState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;
<span class="hljs-keyword">import</span> &#123; getThemeValue &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@/utils/theme_utils"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    Hot,
    <span class="hljs-built_in">Map</span>,
    Rank,
    Seller,
    Stock,
    Trend,
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// 定义每一个图表的全屏状态</span>
      <span class="hljs-attr">fullScreenStatus</span>: &#123;
        <span class="hljs-attr">trend</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">seller</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">map</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">rank</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">hot</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">stock</span>: <span class="hljs-literal">false</span>,
      &#125;,
      <span class="hljs-attr">timer</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">timeValue</span>: <span class="hljs-string">""</span>,
    &#125;;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 注册接收到数据的回调函数</span>
    <span class="hljs-built_in">this</span>.$socket.registerCallBack(<span class="hljs-string">"fullScreen"</span>, <span class="hljs-built_in">this</span>.recvData);
    <span class="hljs-built_in">this</span>.$socket.registerCallBack(<span class="hljs-string">"themeChange"</span>, <span class="hljs-built_in">this</span>.recvThemeChange);
  &#125;,
  <span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$socket.unRegisterCallBack(<span class="hljs-string">"fullScreen"</span>);
    <span class="hljs-built_in">this</span>.$socket.unRegisterCallBack(<span class="hljs-string">"themeChange"</span>);
    <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.timer);
  &#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.displayTime();
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.timer) &#123;
      <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.timer);
    &#125;
    <span class="hljs-built_in">this</span>.timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.displayTime();
    &#125;, <span class="hljs-number">1000</span>)
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">displayTime</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">//获取系统当前的年、月、日、小时、分钟、毫秒</span>
      <span class="hljs-keyword">let</span> date, year, month, day, h, m, s;
      date = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
      year = date.getFullYear();
      month = date.getMonth() + <span class="hljs-number">1</span>;
      day = date.getDate();
      h = date.getHours();
      m = date.getMinutes();
      s = date.getSeconds();
      month = month < <span class="hljs-number">10</span> ? <span class="hljs-string">"0"</span> + month : month;
      day = day < <span class="hljs-number">10</span> ? <span class="hljs-string">"0"</span> + day : day;
      h = h < <span class="hljs-number">10</span> ? <span class="hljs-string">"0"</span> + h : h;
      m = m < <span class="hljs-number">10</span> ? <span class="hljs-string">"0"</span> + m : m;
      s = s < <span class="hljs-number">10</span> ? <span class="hljs-string">"0"</span> + s : s;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.timeValue = year + <span class="hljs-string">"-"</span> + month + <span class="hljs-string">"-"</span> + day + <span class="hljs-string">"  "</span> + h + <span class="hljs-string">":"</span> + m + <span class="hljs-string">":"</span> + s;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">changeSize</span>(<span class="hljs-params">chartName</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(chartName);
      <span class="hljs-comment">// 将数据发送给服务端</span>
      <span class="hljs-keyword">const</span> targetValue = !<span class="hljs-built_in">this</span>.fullScreenStatus[chartName];
      <span class="hljs-built_in">this</span>.$socket.send(&#123;
        <span class="hljs-attr">action</span>: <span class="hljs-string">"fullScreen"</span>,
        <span class="hljs-attr">socketType</span>: <span class="hljs-string">"fullScreen"</span>,
        <span class="hljs-attr">chartName</span>: chartName,
        <span class="hljs-attr">value</span>: targetValue,
      &#125;);
    &#125;,
    <span class="hljs-comment">// 接收到全屏数据之后的处理</span>
    <span class="hljs-function"><span class="hljs-title">recvData</span>(<span class="hljs-params">data</span>)</span> &#123;
      <span class="hljs-comment">// 取出是哪一个图表需要进行切换</span>
      <span class="hljs-keyword">const</span> chartName = data.chartName;
      <span class="hljs-comment">// 取出, 切换成什么状态</span>
      <span class="hljs-keyword">const</span> targetValue = data.value;
      <span class="hljs-built_in">this</span>.fullScreenStatus[chartName] = targetValue;
      <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.$refs[chartName].screenAdapter();
      &#125;);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">handleChangeTheme</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 修改VueX中数据</span>
      <span class="hljs-built_in">this</span>.$socket.send(&#123;
        <span class="hljs-attr">action</span>: <span class="hljs-string">"themeChange"</span>,
        <span class="hljs-attr">socketType</span>: <span class="hljs-string">"themeChange"</span>,
        <span class="hljs-attr">chartName</span>: <span class="hljs-string">""</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-string">""</span>,
      &#125;);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">recvThemeChange</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">"changeTheme"</span>);
    &#125;,
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">logoSrc</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">"/static/img/"</span> + getThemeValue(<span class="hljs-built_in">this</span>.theme).logoSrc;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">headerSrc</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">"/static/img/"</span> + getThemeValue(<span class="hljs-built_in">this</span>.theme).headerBorderSrc;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">themeSrc</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">"/static/img/"</span> + getThemeValue(<span class="hljs-built_in">this</span>.theme).themeSrc;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">containerStyle</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">backgroundColor</span>: getThemeValue(<span class="hljs-built_in">this</span>.theme).backgroundColor,
        <span class="hljs-attr">color</span>: getThemeValue(<span class="hljs-built_in">this</span>.theme).titleColor,
      &#125;;
    &#125;,
    ...mapState([<span class="hljs-string">"theme"</span>]),
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span> <span class="hljs-attr">scoped</span>></span><span class="css">
// 全屏样式的定义
<span class="hljs-selector-class">.fullscreen</span> &#123;
  <span class="hljs-attribute">position</span>: fixed <span class="hljs-meta">!important</span>;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span> <span class="hljs-meta">!important</span>;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span> <span class="hljs-meta">!important</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span> <span class="hljs-meta">!important</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span> <span class="hljs-meta">!important</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-meta">!important</span>;
  <span class="hljs-attribute">z-index</span>: <span class="hljs-number">9999</span>;
&#125;

<span class="hljs-selector-class">.screen-container</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span> <span class="hljs-number">20px</span>;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#2e2e2f</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
  <span class="hljs-attribute">box-sizing</span>: border-box;
&#125;
<span class="hljs-selector-class">.screen-header</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
  <span class="hljs-attribute">position</span>: relative;
  > <span class="hljs-selector-tag">div</span> &#123;
    <span class="hljs-selector-tag">img</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    &#125;
  &#125;
  <span class="hljs-selector-class">.title</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>);
  &#125;
  <span class="hljs-selector-class">.title-right</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">align-items</span>: center;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">right</span>: <span class="hljs-number">0px</span>;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(-<span class="hljs-number">80%</span>);
  &#125;
  <span class="hljs-selector-class">.qiehuan</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">28px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">21px</span>;
    <span class="hljs-attribute">cursor</span>: pointer;
  &#125;
  <span class="hljs-selector-class">.datetime</span> &#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">15px</span>;
    <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">10px</span>;
  &#125;
  <span class="hljs-selector-class">.logo</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(-<span class="hljs-number">80%</span>);
    <span class="hljs-selector-tag">img</span> &#123;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">35px</span>;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">154px</span>;
    &#125;
  &#125;
&#125;
<span class="hljs-selector-class">.screen-body</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">10px</span>;
  <span class="hljs-selector-class">.screen-left</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">27.6%</span>;
    <span class="hljs-selector-id">#left-top</span> &#123;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">53%</span>;
      <span class="hljs-attribute">position</span>: relative;
    &#125;
    <span class="hljs-selector-id">#left-bottom</span> &#123;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">31%</span>;
      <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">25px</span>;
      <span class="hljs-attribute">position</span>: relative;
    &#125;
  &#125;
  <span class="hljs-selector-class">.screen-middle</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">41.5%</span>;
    <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">1.6%</span>;
    <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">1.6%</span>;
    <span class="hljs-selector-id">#middle-top</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">56%</span>;
      <span class="hljs-attribute">position</span>: relative;
    &#125;
    <span class="hljs-selector-id">#middle-bottom</span> &#123;
      <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">25px</span>;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">28%</span>;
      <span class="hljs-attribute">position</span>: relative;
    &#125;
  &#125;
  <span class="hljs-selector-class">.screen-right</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">27.6%</span>;
    <span class="hljs-selector-id">#right-top</span> &#123;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">46%</span>;
      <span class="hljs-attribute">position</span>: relative;
    &#125;
    <span class="hljs-selector-id">#right-bottom</span> &#123;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">38%</span>;
      <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">25px</span>;
      <span class="hljs-attribute">position</span>: relative;
    &#125;
  &#125;
&#125;
<span class="hljs-selector-class">.resize</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">right</span>: <span class="hljs-number">20px</span>;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">20px</span>;
  <span class="hljs-attribute">cursor</span>: pointer;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">4.3.5 全屏切换</h3>
<ul>
<li>全屏状态数据定义</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// 定义每一个图表的全屏状态</span>
      <span class="hljs-attr">fullScreenStatus</span>: &#123;
        <span class="hljs-attr">trend</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">seller</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">map</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">rank</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">hot</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">stock</span>: <span class="hljs-literal">false</span>,
      &#125;,
      <span class="hljs-attr">timer</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">timeValue</span>: <span class="hljs-string">""</span>,
    &#125;;
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>全屏状态样式定义</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><style lang=<span class="hljs-string">"less"</span> scoped>
<span class="hljs-comment">// 全屏样式的定义</span>
.fullscreen &#123;
  <span class="hljs-attr">position</span>: fixed !important;
  top: <span class="hljs-number">0</span> !important;
  left: <span class="hljs-number">0</span> !important;
  width: <span class="hljs-number">100</span>% !important;
  height: <span class="hljs-number">100</span>% !important;
  margin: <span class="hljs-number">0</span> !important;
  z-index: <span class="hljs-number">9999</span>;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>class值得处理</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"left-top"</span> :<span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"[fullScreenStatus.trend ? 'fullscreen' : '']"</span>>
    <!-- 销量趋势图表 -->
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Trend</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"trend"</span> /></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"resize"</span>></span>
    <span class="hljs-comment"><!-- icon-compress-alt --></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>
      @<span class="hljs-attr">click</span>=<span class="hljs-string">"changeSize('trend')"</span>
      <span class="hljs-attr">:class</span>=<span class="hljs-string">"[
        'iconfont',
        fullScreenStatus.trend
          ? 'icon-compress-alt'
          : 'icon-expand-alt',
      ]"</span>
    ></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>全屏点击事件的处理</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">changeSize</span>(<span class="hljs-params">chartName</span>)</span> &#123;
          <span class="hljs-built_in">console</span>.log(chartName);
          <span class="hljs-comment">// 将数据发送给服务端</span>
          <span class="hljs-keyword">const</span> targetValue = !<span class="hljs-built_in">this</span>.fullScreenStatus[chartName];
          <span class="hljs-built_in">this</span>.$socket.send(&#123;
            <span class="hljs-attr">action</span>: <span class="hljs-string">"fullScreen"</span>,
            <span class="hljs-attr">socketType</span>: <span class="hljs-string">"fullScreen"</span>,
            <span class="hljs-attr">chartName</span>: chartName,
            <span class="hljs-attr">value</span>: targetValue,
          &#125;);
        &#125;,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>created时注册回调函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 注册接收到数据的回调函数</span>
        <span class="hljs-built_in">this</span>.$socket.registerCallBack(<span class="hljs-string">"fullScreen"</span>, <span class="hljs-built_in">this</span>.recvData);
        <span class="hljs-built_in">this</span>.$socket.registerCallBack(<span class="hljs-string">"themeChange"</span>, <span class="hljs-built_in">this</span>.recvThemeChange);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>destoryed时取消回调函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.$socket.unRegisterCallBack(<span class="hljs-string">"fullScreen"</span>);
        <span class="hljs-built_in">this</span>.$socket.unRegisterCallBack(<span class="hljs-string">"themeChange"</span>);
        <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.timer);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>得到数据的处理</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-comment">// 接收到全屏数据之后的处理</span>
        <span class="hljs-function"><span class="hljs-title">recvData</span>(<span class="hljs-params">data</span>)</span> &#123;
          <span class="hljs-comment">// 取出是哪一个图表需要进行切换</span>
          <span class="hljs-keyword">const</span> chartName = data.chartName;
          <span class="hljs-comment">// 取出, 切换成什么状态</span>
          <span class="hljs-keyword">const</span> targetValue = data.value;
          <span class="hljs-built_in">this</span>.fullScreenStatus[chartName] = targetValue;
          <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">this</span>.$refs[chartName].screenAdapter();
          &#125;);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>socket_service.js 代码如下：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> action = recvData.action
<span class="hljs-keyword">if</span> (action === <span class="hljs-string">'getData'</span>) &#123;
  <span class="hljs-keyword">const</span> realData = <span class="hljs-built_in">JSON</span>.parse(recvData.data);
  <span class="hljs-built_in">this</span>.callBackMapping[socketType].call(<span class="hljs-built_in">this</span>, realData);
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (action === <span class="hljs-string">'fullScreen'</span>) &#123;
  <span class="hljs-built_in">this</span>.callBackMapping[socketType].call(<span class="hljs-built_in">this</span>, recvData);
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (action === <span class="hljs-string">'themeChange'</span>) &#123;
  <span class="hljs-built_in">this</span>.callBackMapping[socketType].call(<span class="hljs-built_in">this</span>, recvData);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-38">4.3.6 主题切换</h3>
<ul>
<li>当前主题数据的存储</li>
</ul>
<p>当前主题的数据, 会在多个组件中使用, 因此设置在 VueX 中是最合适的, 增加仓库数据 theme , 并增加一个 mutation 用来修改 theme</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// store/index.js</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">theme</span>: <span class="hljs-string">'dark'</span>
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    changeTheme (state) &#123;
      <span class="hljs-keyword">if</span> (state.theme === <span class="hljs-string">'dark'</span>) &#123;
        state.theme = <span class="hljs-string">'default'</span>;
      &#125; <span class="hljs-keyword">else</span> &#123;
        state.theme = <span class="hljs-string">'dark'</span>;
      &#125;
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
  &#125;,
  <span class="hljs-attr">modules</span>: &#123;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>点击切换主题按钮</li>
</ul>
<p>点击事件的响应</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"title-right"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"themeSrc"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"qiehuan"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleChangeTheme"</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"datetime"</span>></span>&#123;&#123; timeValue &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击事件的处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">methods</span>: &#123;
       <span class="hljs-function"><span class="hljs-title">handleChangeTheme</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-comment">// 修改VueX中数据</span>
          <span class="hljs-built_in">this</span>.$socket.send(&#123;
            <span class="hljs-attr">action</span>: <span class="hljs-string">"themeChange"</span>,
            <span class="hljs-attr">socketType</span>: <span class="hljs-string">"themeChange"</span>,
            <span class="hljs-attr">chartName</span>: <span class="hljs-string">""</span>,
            <span class="hljs-attr">value</span>: <span class="hljs-string">""</span>,
          &#125;);
        &#125;  
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>监听主题的变化</li>
</ul>
<p>以 Seller.vue 为例, 进行主题数据变化的监听</p>
<p>映射 store 中的 theme 作为当前组件的计算属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span> 
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123; 
    <span class="hljs-attr">computed</span>: &#123; 
        ...mapState([<span class="hljs-string">'theme'</span>]);
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>监听theme的变化</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123; 
    <span class="hljs-attr">watch</span>: &#123; 
        theme () &#123; 
            <span class="hljs-built_in">this</span>.myChart.dispose(); <span class="hljs-comment">// 销毁当前的图表</span>
            <span class="hljs-built_in">this</span>.initChart(); <span class="hljs-comment">// 重新以最新的主题名称初始化图表对象</span>
            <span class="hljs-built_in">this</span>.screenAdapter(); <span class="hljs-comment">// 完成屏幕适配</span>
            <span class="hljs-built_in">this</span>.updateChart(); <span class="hljs-comment">// 更新图表展示</span>
        &#125; 
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>主题的切换</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123; 
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-comment">// 初始化echartsInstance对象</span>
        <span class="hljs-function"><span class="hljs-title">initChart</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-built_in">this</span>.myChart = <span class="hljs-built_in">this</span>.$echarts.init(<span class="hljs-built_in">this</span>.$refs.seller_ref, <span class="hljs-built_in">this</span>.theme);
        &#125;
    &#125;   
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这个步骤就可以实现每一个图表组件切换主题了，不过有部分样式需要另外调整</p>
<ul>
<li>主题样式适配</li>
</ul>
<p>创建utils/theme_utils.js文件</p>
<p>定义两个主题下, 需要进行样式切换的样式数据, 并对外导出一个函数, 用于方便的通过主题名称得到对应主题的某些配置项</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> theme = &#123;
  <span class="hljs-attr">dark</span>: &#123;
    <span class="hljs-comment">// 背景颜色</span>
    <span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">'#3f3f46'</span>,
    <span class="hljs-comment">// 图表背景色</span>
    <span class="hljs-attr">bgColor</span>: <span class="hljs-string">'#100c2a'</span>,
    <span class="hljs-comment">// label文字颜色</span>
    <span class="hljs-attr">labelColor</span>: <span class="hljs-string">'#fff'</span>,
    <span class="hljs-comment">// 标题的文字颜色</span>
    <span class="hljs-attr">titleColor</span>: <span class="hljs-string">'#fff'</span>,
    <span class="hljs-comment">// 左上角logo的图标路径</span>
    <span class="hljs-attr">logoSrc</span>: <span class="hljs-string">'logo_dark.png'</span>,
    <span class="hljs-comment">// 切换主题按钮的图片路径</span>
    <span class="hljs-attr">themeSrc</span>: <span class="hljs-string">'qiehuan_dark.png'</span>,
    <span class="hljs-comment">// 页面顶部的边框图片</span>
    <span class="hljs-attr">headerBorderSrc</span>: <span class="hljs-string">'header_border_dark.png'</span>

  &#125;,
  <span class="hljs-attr">default</span>: &#123;
    <span class="hljs-comment">// 背景颜色</span>
    <span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">'#eee'</span>,
    <span class="hljs-comment">// 图表背景色</span>
    <span class="hljs-attr">bgColor</span>: <span class="hljs-string">'#fff'</span>,
    <span class="hljs-comment">// label文字颜色</span>
    <span class="hljs-attr">labelColor</span>: <span class="hljs-string">'#100c2a'</span>,
    <span class="hljs-comment">// 标题的文字颜色</span>
    <span class="hljs-attr">titleColor</span>: <span class="hljs-string">'#000'</span>,
    <span class="hljs-comment">// 左上角logo的图标路径</span>
    <span class="hljs-attr">logoSrc</span>: <span class="hljs-string">'logo_light.png'</span>,
    <span class="hljs-comment">// 切换主题按钮的图片路径</span>
    <span class="hljs-attr">themeSrc</span>: <span class="hljs-string">'qiehuan_light.png'</span>,
    <span class="hljs-comment">// 页面顶部的边框图片</span>
    <span class="hljs-attr">headerBorderSrc</span>: <span class="hljs-string">'header_border_light.png'</span>
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getThemeValue</span> (<span class="hljs-params">themeName</span>) </span>&#123;
  <span class="hljs-keyword">return</span> theme[themeName]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>映射 VueX 中的 theme 数据作为该组件的计算属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// screenPage.vue</span>
<span class="hljs-keyword">import</span> &#123; mapState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span> 
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123; 
<span class="hljs-attr">computed</span>: &#123; 
    ...mapState([<span class="hljs-string">'theme'</span>]) 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义一些控制样式的计算属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// screenPage.vue</span>
<span class="hljs-keyword">import</span> &#123; mapState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;
<span class="hljs-keyword">import</span> &#123; getThemeValue &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@/utils/theme_utils"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">computed</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">logoSrc</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-string">"/static/img/"</span> + getThemeValue(<span class="hljs-built_in">this</span>.theme).logoSrc;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">headerSrc</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-string">"/static/img/"</span> + getThemeValue(<span class="hljs-built_in">this</span>.theme).headerBorderSrc;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">themeSrc</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-string">"/static/img/"</span> + getThemeValue(<span class="hljs-built_in">this</span>.theme).themeSrc;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">containerStyle</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">backgroundColor</span>: getThemeValue(<span class="hljs-built_in">this</span>.theme).backgroundColor,
            <span class="hljs-attr">color</span>: getThemeValue(<span class="hljs-built_in">this</span>.theme).titleColor,
          &#125;;
        &#125;
     &#125;
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将计算属性应用到布局中</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"screen-container"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"containerStyle"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">header</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"screen-header"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"headerSrc"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span> /></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"logo"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"logoSrc"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span> /></span>
          <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"title"</span>></span>电商平台数据大屏实时监控系统<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"title-right"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"themeSrc"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"qiehuan"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleChangeTheme"</span> /></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"datetime"</span>></span>&#123;&#123; timeValue &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">header</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过计算属性动态控制标题样式及下拉框选项</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// trend.vue</span>
<span class="hljs-keyword">import</span> &#123; mapState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;
<span class="hljs-keyword">import</span> &#123; getThemeValue &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@/utils/theme_utils"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    ...mapState([<span class="hljs-string">"theme"</span>]),
    <span class="hljs-function"><span class="hljs-title">selectTypes</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.allData) &#123;
        <span class="hljs-keyword">return</span> [];
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.allData.type.filter(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
          <span class="hljs-keyword">return</span> item.key !== <span class="hljs-built_in">this</span>.choiceType;
        &#125;);
      &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">showTitle</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.allData) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">""</span>;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.allData[<span class="hljs-built_in">this</span>.choiceType].title;
      &#125;
    &#125;,
    <span class="hljs-comment">// 设置给标题的样式</span>
    <span class="hljs-function"><span class="hljs-title">comStyle</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">fontSize</span>: <span class="hljs-built_in">this</span>.titleFontSize + <span class="hljs-string">"px"</span>,
        <span class="hljs-attr">color</span>: getThemeValue(<span class="hljs-built_in">this</span>.theme).labelColor
      &#125;;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">marginStyle</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">marginLeft</span>: <span class="hljs-built_in">this</span>.titleFontSize + <span class="hljs-string">"px"</span>,
        <span class="hljs-attr">backgroundColor</span>: getThemeValue(<span class="hljs-built_in">this</span>.theme).bgColor
      &#125;;
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-39">5. 写在最后</h1>
<ul>
<li>升级Echarts新版本</li>
<li>快速掌握KOA2后端框架开发API</li>
<li>代码简洁优化及功能完善</li>
<li>Axios和WebSocket两种通信方式讲解</li>
<li>适合进阶数据可视化的练手项目</li>
</ul>
<blockquote>
<p>如果对你有些许帮助，可以点赞、评论、转发分享，也是对我的一种支持，万分感谢。如需获取更多实战项目经验或源码资源，请关注我的公众号：「懒人码农」，也可以加我微信【lazycode520】，一起学习一起进步。</p>
</blockquote>
<p>查看完整源代码，请移步到github访问👉：<a href="https://github.com/jackchen0120/EC-Platform-Monitor" target="_blank" rel="nofollow noopener noreferrer">github.com/jackchen012…</a></p>
<p>参考资料：<a href="https://www.bilibili.com/video/BV1Uz4y1S7kr?p=1" target="_blank" rel="nofollow noopener noreferrer">www.bilibili.com/video/BV1Uz…</a></p></div>  
</div>
            