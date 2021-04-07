
---
title: 'NodeJS知识点梳理-第一篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d48d7655f0d9445bbf6fb93783d3bfdc~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 22:46:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d48d7655f0d9445bbf6fb93783d3bfdc~tplv-k3u1fbpfcp-zoom-1.image'
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
<li><a href="https://juejin.cn/post/6943479411282804772#_1">写在前面</a></li>
<li><a href="https://juejin.cn/post/6943479411282804772#NodeJS_3">什么是NodeJS</a></li>
<li><a href="https://juejin.cn/post/6943479411282804772#NodeJS_7">NodeJS为什么会那么火</a></li>
<li><a href="https://juejin.cn/post/6943479411282804772#NodeJS_12">使用NodeJS需要会的技术</a></li>
<li><a href="https://juejin.cn/post/6943479411282804772#NodeJS_17">安装NodeJS</a></li>
<li><a href="https://juejin.cn/post/6943479411282804772#_21">验证安装</a></li>
<li><a href="https://juejin.cn/post/6943479411282804772#_29">工具使用</a></li>
<li><a href="https://juejin.cn/post/6943479411282804772#NodeJS_33">NodeJS全局变量初识</a></li>
<li><a href="https://juejin.cn/post/6943479411282804772#global_67">认识global</a></li>
<li><a href="https://juejin.cn/post/6943479411282804772#V8_73">V8引擎基本介绍</a></li>
<li><a href="https://juejin.cn/post/6943479411282804772#modulenode_84">module介绍（node模块）</a></li>
<li><a href="https://juejin.cn/post/6943479411282804772#Event_192">事件模块（Event）</a></li>
<li><a href="https://juejin.cn/post/6943479411282804772#__fsFileSystem_277">文件系统 (读写 fs-FileSystem)</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h4 data-id="heading-1"><a href="https://juejin.cn/post/6943479411282804772"></a>写在前面</h4>
<p>废话先说好，不然你们看到后面没有耐心以后就不会看我说的废话了，为什么我要写这个node系列的文章呢？我发现现在很多公司对node的要求越来越多了，（虽然也不知道为什么吧，可能是因为他们觉得自己的公司太强大（low）了，需要一些会nodejs的人充场面吧），所以不管怎样我都觉得有必要梳理一下关于nodejs的一些知识点，我梳理的过程可能有一些不严谨的，但是基本上大体上是对的，你们尽管作为一个参考，里面涉及到的代码源码都是我自己运行以后的，所以基本没有错的，抱着对得起粉丝的态度写文章，还是要对自己的粉丝负责任的（虽然粉丝不多），最后希望看我的文章以后可以对nodejs有一个全新或者新的认识，有错误或者不严谨的地方希望各位大佬及时提出来，毕竟鄙人只是一个不那么严谨但是有态度的程序员。因为我要上班，所以只能下班以后晚上更新，慢慢更吧，emmm…废话是有点多，开始吧…</p>
<h4 data-id="heading-2"><a href="https://juejin.cn/post/6943479411282804772"></a>什么是NodeJS</h4>
<ul>
<li>Node.js是一个基本Chrome V8引擎的JavaScript运行环境</li>
<li>Node.js使用了一个事件驱动、非阻塞式I/o的模型，使其轻量又高效</li>
<li>Node.js的包管理器npm（node package mange）是全球最大的开源库生态系统</li>
</ul>
<h4 data-id="heading-3"><a href="https://juejin.cn/post/6943479411282804772"></a>NodeJS为什么会那么火</h4>
<ul>
<li>使用的是javascript</li>
<li>速度非常的快</li>
<li>Nodejs的包管理器是全球最大的开源库</li>
<li>可以节约资源，什么意思呢，如果我们的项目不是很大，处理的数据不是很复杂，我们使用nodejs完全是够用的，也就是说以前我们做一个有数据交互的项目需要最少两个人，一个写前端一个写后端，但是公司里面项目不是很大的话，一个会nodejs的人完全是可以胜任的，可以做一写数据库的操作。</li>
</ul>
<h4 data-id="heading-4"><a href="https://juejin.cn/post/6943479411282804772"></a>使用NodeJS需要会的技术</h4>
<ul>
<li>Command Line</li>
<li>Html+css</li>
<li>javascript</li>
<li>mongo db （这个作为nosql也就是非关系型数据库，我们nodejs选择连接的是它，原因是非关系型数据库查询速度对数据的处理速度是很快的，因为没有那个表之间的各种关联，不像我们的myqsql或者oracle这样的关系型数据库，各种关联，nodejs本身就是一个处理高并发情况的语言，所以对数据操作的速度要求是很高的，这里选择的是mongo db）</li>
</ul>
<h4 data-id="heading-5"><a href="https://juejin.cn/post/6943479411282804772"></a>安装NodeJS</h4>
<ul>
<li><a href="http://nodejs.cn/" target="_blank" rel="nofollow noopener noreferrer">Node</a></li>
<li><a href="http://nodejs.cn/api/" target="_blank" rel="nofollow noopener noreferrer">Node学习</a></li>
<li>下载结束直接安装就可以了</li>
</ul>
<h4 data-id="heading-6"><a href="https://juejin.cn/post/6943479411282804772"></a>验证安装</h4>
<p>直接输入 node -v<br>
<img alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-wJYrvSmC-1574234452713)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p28)]" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d48d7655f0d9445bbf6fb93783d3bfdc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
输入 npm -v<br>
<img alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-FXPQFdnz-1574234452726)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p30)]" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9589a9d369d340a79c554438e17f47f8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
或者我们直接运行一个我们本地的js也是一样的，直接node csdn_demo.js<br>
<img alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-3Uv5xLMb-1574234452726)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p31)]" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29eb99cb2202425daab925e256714630~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7"><a href="https://juejin.cn/post/6943479411282804772"></a>工具使用</h4>
<ul>
<li>webstorm （直接下载使用，这里不写下载和安装的过程了）</li>
<li>vscode （个人建议使用这个，这个是一个比较轻量级的编辑器，重要的是你可以自己定制自己需要的插件）</li>
<li>sublime （这个是最好用的我认为，但是上手就比较难了）</li>
</ul>
<h4 data-id="heading-8"><a href="https://juejin.cn/post/6943479411282804772"></a>NodeJS全局变量初识</h4>
<ul>
<li><a href="http://nodejs.cn/api/globals.html" target="_blank" rel="nofollow noopener noreferrer">node全局变量</a></li>
</ul>
<blockquote>
<p>举个例子</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@author <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@aim </span>测试一个nodejs的全局变量
 * <span class="hljs-doctag">@param </span>time 计时变量
 * <span class="hljs-doctag">@param </span>timer 清除计时器
 * setTimeout  延时操作
 * setInterval 计时循环操作
 */</span>
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.info(<span class="hljs-string">"3秒过去了，我已经执行结束了"</span>)
&#125;, <span class="hljs-number">3000</span>)

<span class="hljs-keyword">var</span> time = <span class="hljs-number">0</span>

<span class="hljs-keyword">let</span> timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    time++
    <span class="hljs-built_in">console</span>.info(time)
    <span class="hljs-keyword">if</span> (time > <span class="hljs-number">10</span>) &#123;
        <span class="hljs-built_in">clearInterval</span>(timer)
        <span class="hljs-built_in">console</span>.info(<span class="hljs-string">"结束了"</span>)
    &#125;
&#125;, <span class="hljs-number">2000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>运行结果<br>
<img alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-d7gci3jH-1574234452727)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p32)]" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2aa9f9c5c31d462eafee9cdf09bd04d1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<blockquote>
<p>还有一点是我们常见的</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.info(__dirname)   <span class="hljs-comment">//w文件路径名字   不不包含文件名  这个也是bnode里面的一个全局变量</span>
<span class="hljs-built_in">console</span>.info(__filename)  <span class="hljs-comment">// 文件完整路径名字  </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9"><a href="https://juejin.cn/post/6943479411282804772"></a>认识global</h4>
<blockquote>
<p>其实这个global和前面两个说的一样都是node里面的全局变量，但是为什么这个要单独拿出来说呢？原因自然是他有自己不一样的地方，我们都知道js里面的全局变量是windows，我们一般都是windows.一个属性，但是在node里面他的老大就是global了，那么我们直接打印出来这个看看究竟是什么</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.info(<span class="hljs-built_in">global</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>-这里就不展示运行结果了，你们自己运行吧，太长了，截图或者直接复制都比较不友好。</p>
<h4 data-id="heading-10"><a href="https://juejin.cn/post/6943479411282804772"></a>V8引擎基本介绍</h4>
<ul>
<li>首先说一下为什么要引擎这个东西，做什么的，我们都知道，我们的计算机时不认识我们写的什么javascript的，计算机可以识别的语言像C、C++等后端语言是可以识别的，但是他不认识我们的js，那么我们的js引擎的作用就是让计算机认识我们的js，node是C++写的，V8引擎是nodejs的核心，V8引擎其实也是C++写的。 流程就是写好的js代码通过v8引擎在node环境下运行，从而达到让计算机认识我们js语言的一个效果，简单的画一个抠脚的流程图，md文档画流程图还是比较简单（caodan）的。</li>
</ul>

<ul>
<li>这里是我的理解，可能有偏差，有大佬看出问题的及时通知我，我会及时更新内容。</li>
</ul>
<h4 data-id="heading-11"><a href="https://juejin.cn/post/6943479411282804772"></a>module介绍（node模块）</h4>
<p><a href="http://nodejs.cn/api/modules.html" target="_blank" rel="nofollow noopener noreferrer">Node模块</a></p>
<ul>
<li>我们写代码的时候一般开发的规则是一个功能一个模块的开发，这样不仅仅是容易开发，其实更便捷的是为了以后维护等别人接收你的代码的时候不至于骂你。所以哦我们node里面其实也是一样的，每一个js都是一个模块。然后写一个总的js统一调用就可以了，我们写一个简单的例子：</li>
<li>-我们新建一个工具类的js，这个目的是为了用户输入一个数据类型，我们输出他的数据类型</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@auhor <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@aim </span>判断用户输入的数据类型
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>params 形参 
 */</span>
<span class="hljs-keyword">var</span> counter = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">params</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> params
&#125;

<span class="hljs-comment">//将当前的工具函数导出去，变为一个任何引入的地方都可以直接使用</span>
<span class="hljs-built_in">module</span>.exports = counter
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在node_demo.js里面我们引入他</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@author <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@aim </span>接收模块的代码
 * <span class="hljs-doctag">@parms </span>counter 将引入的js赋值给counter
 */</span>
<span class="hljs-keyword">let</span> counter = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./stuff"</span>)
<span class="hljs-built_in">console</span>.info(counter(<span class="hljs-literal">false</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行效果：<br>
<img alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-l0peM4Xa-1574234452728)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p33)][外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-IzfEePgt-1574234452729)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p34)]" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75f9f914857b4d3ab67a5b0427f7a9a3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a6d1094c5dc4ee6a5248014e2bbfb6a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这里介绍两个东西，第一是module.exports 第二是require</p>
</blockquote>
<ul>
<li>module.exports目的将当前的工具函数导出去，变为一个任何引入的地方都可以直接使用，这样在别的地方才可以引入</li>
<li>require，直接引入我们需要的js，为什么需要一个变量接收呢？因为不接受的话我们还是找不到引用的方法</li>
</ul>
<blockquote>
<p>那这个时候就有人问了，我们一个方法这样写，多个的时候怎么办呢？看例子：</p>
</blockquote>
<ul>
<li>stuff.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@auhor <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@aim </span>判断用户输入的数据类型
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>params 形参 
 */</span>
<span class="hljs-keyword">var</span> counter = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">params</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> params
&#125;
<span class="hljs-comment">/**
 * 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>a 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>b 
 */</span>
<span class="hljs-keyword">var</span> add = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`计算的结果是： <span class="hljs-subst">$&#123;a+b&#125;</span>`</span>
&#125;
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param </span>pi 圆周率
 */</span>
<span class="hljs-keyword">var</span> pi = <span class="hljs-number">3.141592653589793238462643383279</span>
    <span class="hljs-comment">//将当前的工具函数导出去，变为一个任何引入的地方都可以直接使用</span>
<span class="hljs-built_in">module</span>.exports.counter = counter
<span class="hljs-built_in">module</span>.exports.add = add
<span class="hljs-built_in">module</span>.exports.pi = pi
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>node_demo.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@author <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@aim </span>接收模块的代码
 * <span class="hljs-doctag">@parms </span>counter 将引入的js赋值给counter
 */</span>
<span class="hljs-keyword">let</span> stuff = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./stuff"</span>) <span class="hljs-comment">//此时的stuff是一个对象</span>
<span class="hljs-built_in">console</span>.info(stuff.counter(<span class="hljs-literal">false</span>))
<span class="hljs-built_in">console</span>.info(stuff.add(<span class="hljs-number">584</span>, <span class="hljs-number">654</span>))
<span class="hljs-built_in">console</span>.info(stuff.pi)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>运行结果<br>
<img alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-MN4ZVwLr-1574234452730)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p35)]" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/668cb28acfef43e19d7a3ab92a57e513~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<blockquote>
<p>这里又有人说了，那你这太麻烦了，如果一百个方法是不是你要复制一百次啊，当然不是，我们可以直接将一个对象导出去，看代码：</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">/**
     * 将每一个方法名字均导出去
     */</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">counter</span>: counter,
    <span class="hljs-attr">add</span>: add,
    <span class="hljs-attr">pi</span>: pi
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>这里就不展示运行结果了，和上面的是一样的。还有就是你上面对象的值写你的方法也是可以的，看代码：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">        <span class="hljs-comment">/**
         * <span class="hljs-doctag">@param </span>pi 圆周率
         */</span>
    <span class="hljs-keyword">var</span> pi = <span class="hljs-number">3.141592653589793238462643383279</span>
        <span class="hljs-comment">/**
         * 将每一个方法名字均导出去
         */</span>
    <span class="hljs-built_in">module</span>.exports = &#123;
        <span class="hljs-attr">counter</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">params</span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> params
        &#125;,
        <span class="hljs-attr">add</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a, b</span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">`您计算的结果是：<span class="hljs-subst">$&#123;a + b&#125;</span>`</span>
        &#125;,
        <span class="hljs-attr">pi</span>: pi
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里需要解释一下上面有一句话是这样的：return <code>计算的结果是： $&#123;a+b&#125;</code>那么这句话是es6的一个写法，就黑我们平常写+拼接是一个意思，只是这样写是一个比较非常规的写法而已。</p>
</blockquote>
<h4 data-id="heading-12"><a href="https://juejin.cn/post/6943479411282804772"></a>事件模块（Event）</h4>
<p><a href="http://nodejs.cn/api/events.html" target="_blank" rel="nofollow noopener noreferrer">Node事件</a></p>
<ul>
<li>事件我们在js里面也是经常遇到的，譬如鼠标点击、键盘事件等等，事件是为了解决交互问题，那么node里面也是有事件模块的，他就是我们这里要说的Event<br>
需要注意的三点：<br>
1、大多数的Nodejs核心API都是采用惯用的异步事件驱动架构的（fs/http）<br>
2、所有能触发事件的对象都是EventEmitter类的实例<br>
3、事件的流程是：引入模块->创建EventEmitter对象->注册事件->触发事件</li>
<li>看例子</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@author <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@aim </span>演示基本的事件使用的过程
 * <span class="hljs-doctag">@param </span>myEmitter 创建eventemitter对象
 */</span>
<span class="hljs-comment">//引入事件模块  import event from 'events' 和下面的写法是一样的，只是这个是es6的写法</span>
<span class="hljs-keyword">var</span> event = <span class="hljs-built_in">require</span>(<span class="hljs-string">'events'</span>);
<span class="hljs-comment">//创建eventemitter对象</span>
<span class="hljs-keyword">var</span> myEmitter = <span class="hljs-keyword">new</span> event.EventEmitter();
<span class="hljs-comment">//注册一个事件  （这里解释一下什么是注册一个事件，我们使用jquery的时候会知道，我们想使用一个事件的时候我们是元素之前就创建好的 例如：Element.on('click',function (params) &#123;&#125;)）</span>
myEmitter.on(<span class="hljs-string">'anyevent'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">param</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.info(<span class="hljs-keyword">typeof</span> param)
    <span class="hljs-comment">//return typeof param</span>
&#125;)
<span class="hljs-comment">//触发事件 你可以直接调用这个事件 当然也可以传递参数</span>
<span class="hljs-comment">//myEmitter.emit('anyevent',false) //前者是事件名字，后者是参数</span>
myEmitter.emit(<span class="hljs-string">'anyevent'</span>,<span class="hljs-literal">false</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果：<br>
<img alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-YZYfMQJo-1574234452731)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p36)]" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d646e5939914e708fc1ac4816902d09~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>处理异步执行的情况：<br>
看代码：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@author <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@aim </span>演示异步使用
 * <span class="hljs-doctag">@param </span>myEmitter 创建eventemitter对象
 */</span>
<span class="hljs-keyword">var</span> event = <span class="hljs-built_in">require</span>(<span class="hljs-string">'events'</span>);
<span class="hljs-keyword">var</span> myEmitter = <span class="hljs-keyword">new</span> event.EventEmitter();
myEmitter.on(<span class="hljs-string">'anyevent'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">param</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.info(param)
&#125;)
myEmitter.emit(<span class="hljs-string">'anyevent'</span>,<span class="hljs-string">'我是myEmitter事件'</span>)
<span class="hljs-built_in">console</span>.info(<span class="hljs-string">'我被执行了，在myEmitter事件之后'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果：<br>
<img alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-beKR2950-1574234452731)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p37)]" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05df2d4f840b483da693ad434754be97~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>可以看到我们的代码是顺序执行的，也就是说上面声明的事件执行结束以后下面的事件才开始执行的，那么这个时候我想翻过来执行的顺序怎么办呢？Node官方给出的解决办法是这样的，看代码：</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@author <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@aim </span>演示异步使用
 * <span class="hljs-doctag">@param </span>myEmitter 创建eventemitter对象
 */</span>
<span class="hljs-keyword">var</span> event = <span class="hljs-built_in">require</span>(<span class="hljs-string">'events'</span>);
<span class="hljs-keyword">var</span> myEmitter = <span class="hljs-keyword">new</span> event.EventEmitter();
myEmitter.on(<span class="hljs-string">'anyevent'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">param</span>)</span>&#123;
    <span class="hljs-comment">//EventEmitter 会按照监听器注册的顺序同步地调用所有监听器。 所以必须确保事件的排序正确，且避免竞态条件。 可以使用 setImmediate() 或 process.nextTick() 切换到异步模式</span>
    setImmediate(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.info(param)
    &#125;)
&#125;)
myEmitter.emit(<span class="hljs-string">'anyevent'</span>,<span class="hljs-string">'我是myEmitter事件'</span>)
<span class="hljs-built_in">console</span>.info(<span class="hljs-string">'我被执行了，在myEmitter事件之前'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果：<br>
<img alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-Qn4ThIjX-1574234452732)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p38)]" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/998293afa9f94392a46e6e7ce0d35b66~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>具体下面还有什么once、error或者别的什么方法这里就不写了，都是如出一辙，会了一个就可以了。<br>
多个参数的情况处理，看代码：</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@author <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@aim </span>演示多参数
 * <span class="hljs-doctag">@param </span>myEmitter 创建eventemitter对象
 */</span>
<span class="hljs-keyword">var</span> event = <span class="hljs-built_in">require</span>(<span class="hljs-string">'events'</span>);
<span class="hljs-keyword">var</span> myEmitter = <span class="hljs-keyword">new</span> event.EventEmitter();
myEmitter.on(<span class="hljs-string">'event'</span>, <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(a + b,<span class="hljs-built_in">this</span>);
  &#125;);
  myEmitter.emit(<span class="hljs-string">'event'</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果：<br>
<img alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-FA6pO5rg-1574234452733)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p39)]" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22cf32a0962641c899de6e7187a22494~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>当监听器被调用时，this指向的是EventEmitter对象</p>
</blockquote>
<h4 data-id="heading-13"><a href="https://juejin.cn/post/6943479411282804772"></a>文件系统 (读写 fs-FileSystem)</h4>
<ul>
<li>文件系统一般我们用到的都是一些读取、写入、别的一般很少会用到，node里面读取和写入文件也是一样的。</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">- 读取文件 （fs.readFile）
- 写入文件 （fs.writeFile）
- 流程：引入fs模块->调用方法->异常捕获
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>同步读写文件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@author <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@aim </span>演示文件读写
 * <span class="hljs-doctag">@param </span>myEmitter 创建eventemitter对象
 */</span>
<span class="hljs-comment">//引入fs</span>
<span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>); 
<span class="hljs-comment">//通过对象调方法     同步读取文件</span>
<span class="hljs-keyword">var</span> readme = fs.readFileSync(<span class="hljs-string">'readMe.txt'</span>,<span class="hljs-string">'utf-8'</span>);
<span class="hljs-built_in">console</span>.info(readme)
fs.writeFileSync(<span class="hljs-string">'writeMe.txt'</span>,readme)  <span class="hljs-comment">//同步写入文件  </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果：<br>
<img alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-iuXLQue7-1574234452733)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p40)]" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48662af0bcf14b1aaa44b90ff9be740b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
会发现写入文件的时候下面会多出一个我们刚刚写的文件<br>
<img alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-xK2QKb4V-1574234452734)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p41)]" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6a985676c4e4d93bc79b44eb8e465c3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>异步读写文件<br>
看代码：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@author <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@aim </span>演示文件读写
 */</span>
<span class="hljs-comment">//引入fs</span>
<span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);  
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@readMe</span>.txt 需要读的文件
 * <span class="hljs-doctag">@utf</span>-8 读的字符格式
 * <span class="hljs-doctag">@error </span>抛出异常
 * <span class="hljs-doctag">@data </span>读的内容
 */</span>
fs.readFile(__filename,<span class="hljs-string">'utf-8'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error,data</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(error) <span class="hljs-keyword">throw</span> error
    <span class="hljs-comment">//在我们读取结束后将自身的内容写入到新的文件中去</span>
    writeMeSync(data)
&#125;)
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@writeMeSync </span>写入一个文件
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>写入的参数 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">writeMeSync</span>(<span class="hljs-params">params</span>) </span>&#123;
    fs.writeFile(<span class="hljs-string">'SyncWriteMe.txt'</span>,params,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error,data</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(error) <span class="hljs-keyword">throw</span> error
&#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>-运行结果：<br>
<img alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-fHqGp2fG-1574234452735)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p44)]" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4126dff978864e23b08068431f4081a9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>创建文件和删除文件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> - 创建文件夹 fs.mkdir
 - 删除文件夹 fs.rmdir
 - 删除文件 fs.unlink
 流程：引入fs模块->调用方法->异常捕获
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
* <span class="hljs-doctag">@author <span class="hljs-variable">clearlove</span></span>
* <span class="hljs-doctag">@aim </span>演示删除文件以及文件夹
*/</span>
<span class="hljs-comment">//引入fs</span>
<span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>); 
fs.unlink(<span class="hljs-string">'SyncWriteMe.txt'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err</span>) </span>&#123;
   <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err
   <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'删除成功'</span>)
&#125;)
<span class="hljs-comment">//创建文件夹</span>
fs.mkdirSync(<span class="hljs-string">'views'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>)</span>&#123;
   <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err
   <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'创建成功'</span>)
&#125;)
<span class="hljs-comment">//删除文件夹</span>
fs.rmdirSync(<span class="hljs-string">'views'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>)</span>&#123;
   <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err
   <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'删除成功'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>你们自己运行吧</li>
<li>异步删除文件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@author <span class="hljs-variable">clearlove</span></span>
 * <span class="hljs-doctag">@aim </span>演示删除文件以及文件夹
 */</span>
<span class="hljs-comment">//引入fs</span>
<span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-comment">//异步操作文件夹   新建一个文件夹，读当前文件内容，将最新的文件内容写到一个新的文件里面</span>
fs.mkdir(<span class="hljs-string">'views'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    fs.readFile(__filename, <span class="hljs-string">'utf-8'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err, data</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err;
        fs.writeFile(<span class="hljs-string">'./views/new.js'</span>, data,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>)</span>&#123;
           <span class="hljs-keyword">if</span>(err) <span class="hljs-keyword">throw</span> err
            <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'创建成功'</span>)
        &#125;)
    &#125;)
&#125;)

<span class="hljs-comment">//异步删除文件夹 删除文件夹的前提是文件夹是空的，所以我们第一步是将文件夹里面的文件删除，成功以后删除文件夹</span>
fs.unlink(<span class="hljs-string">'./views/new.js'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(err) <span class="hljs-keyword">throw</span> err
    fs.mkdir(<span class="hljs-string">'vires'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err,data</span>) </span>&#123;
        <span class="hljs-keyword">if</span>(err) <span class="hljs-keyword">throw</span> err
        <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'文件夹删除成功'</span>)
    &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>运行结果：<br>
<img alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-La0F2vjq-1574234452735)(evernotecid://72A0867B-C2C9-4394-90F0-D1AD032DA4AC/appyinxiangcom/24072006/ENResource/p45)]" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be1d2bff71204d2190ee3f5f595876cb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<blockquote>
<p>ok，先写到这里吧，NodeJS还有很多需要学的，但是做事情不可以一蹴而就，循序渐进的来吧，下篇文章有时间的时候写一下剩下的一些关于NodeJS的知识，因为我是自学的，所以写的一些不规范或者有问题的地方可以提出来，我直接改掉，学习NodeJS注定是一条漫长的路，下一篇文章我会写一下本地怎么跑一个服务，将本地的html渲染出来，同时写一下关于buffer和stoream流的概念，共勉，感谢。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            