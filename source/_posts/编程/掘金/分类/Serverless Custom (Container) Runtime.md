
---
title: 'Serverless Custom (Container) Runtime'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 14:34:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这是第 106 篇不掺水的原创，想获取更多原创好文，请搜索公众号关注我们吧~ 本文首发于政采云前端博客：<a href="https://zoo.team/article/serverlesscustom" target="_blank" rel="nofollow noopener noreferrer">Serverless Custom (Container) Runtime</a></p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6a3993b411047628f072a647483f755~tplv-k3u1fbpfcp-watermark.image" alt="雪霁.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">背景</h3>
<p>我们知道 Serverless 可以理解为 <strong>Serverless = FaaS + BaaS</strong> 。Serverless 应用中，对于服务端业务逻辑代码，开发者是以<strong>函数</strong>的形式去实现的，即 <strong>FaaS</strong>（函数即服务）。( Serverless 相关文章可以看下团队<a href="https://juejin.cn/post/6892728697082609672" target="_blank">结合阿里云 FC 谈谈我对 FaaS 的理解</a>)</p>
<p>对于云厂商的 FaaS 平台，虽然他们支持多种编程语言及版本的标准运行环境，但毕竟还是<strong>有限</strong>的。所以，为了满足用户更多个性化开发语言及版本的函数实现需求，他们提供了 <strong>Custom Runtime 服务</strong>，即<strong>可定制化运行环境</strong>，支持用户用任何编程语言编写的函数。</p>
<p>以阿里云函数计算 FC 为例，这是它所支持的开发语言列表：</p>

































































<table><thead><tr><th>支持语言</th><th>运行环境</th></tr></thead><tbody><tr><td>Node.js</td><td>Node.js 6.10（runtime=nodejs6）、<br>Node.js 8.9.0（runtime=nodejs8）、<br>Node.js 10.15.3（runtime=nodejs10）<br>Node.js 12.16.1（runtime=nodejs12）</td></tr><tr><td>Python</td><td>Python 2.7（runtime = python2.7）<br>Python 3.6（runtime = python3）</td></tr><tr><td>PHP</td><td>PHP 7.2.7（Runtime=php7.2）</td></tr><tr><td>Java</td><td>Java OpenJDK 1.8.0（runtime=java8）</td></tr><tr><td>C#</td><td>.NET Core 2.1（runtime=dotnetcore 2.1）</td></tr><tr><td>Go</td><td>Go Custom Runtime</td></tr><tr><td>Ruby</td><td>Ruby Custom Runtime</td></tr><tr><td>PowerShell</td><td>PowerShell Custom Runtime</td></tr><tr><td>TypeScript</td><td>TypeScript Custom Runtime</td></tr><tr><td>F#</td><td>F# Custom Runtime</td></tr><tr><td>C++</td><td>C++ Custom Runtime</td></tr><tr><td>Lua</td><td>Lua Custom Runtime</td></tr><tr><td>Dart</td><td>Dart Custom Runtime</td></tr><tr><td>其他语言</td><td>Custom Runtime</td></tr></tbody></table>
<p>可以看出，对于我们前端工程师，如果想使用阿里云 FC 平台，并不能随心所欲的使用 Node.js 和 TypeScript 。因为 Node.js，只支持表格中的四种版本，而 TypeScript ，FC 平台自身完全不支持。所以要想使用 Node.js 的其它版本和 TypeScript，就需要自定义运行时。</p>
<p>那么什么是 Custom Runtime 呢？</p>
<h3 data-id="heading-1">概念</h3>
<p>运行时（ Runtime ）指函数代码在运行时所依赖的环境，包括任何库、代码包、框架或平台。Custom Runtime 就是完全由<strong>用户自定义函数的运行环</strong>境。</p>
<p>FaaS 平台通过开放实现自定义函数运行时，支持根据需求使用<strong>任意开发语言的任意版本</strong>来编写函数。</p>
<h3 data-id="heading-2">作用</h3>
<p>阿里云官方文档中说到，基于 Custom Runtime 我们可以实现这两件事：</p>
<ul>
<li>定制个性化语言（例如 Go、Lua、Ruby ）和各种语言的小版本（例如 Python 3.7、Node.js 14）的执行环境，打造属于您的运行环境。</li>
<li><strong>一键迁移</strong>现有的 Web 应用或基于传统开发的 Web 项目到函数计算平台，不用做任何改造。</li>
</ul>
<h2 data-id="heading-3">实现 Custom Runtime</h2>
<p>本文将以阿里云 FC 为例，实现一个 Custom Runtime。其它平台比如腾讯云 SCF 等，原理和过程也都大致相同。</p>
<h3 data-id="heading-4">工作原理</h3>
<p>Custom Runtime 本质上是一个 <strong>HTTP Server</strong>，代码里面包含一个名为 <strong>bootstrap 的启动文件</strong>，之后<strong>这个 HTTP Server 接管了函数计算平台的所有请求</strong>，包括事件调用或者 HTTP 函数调用等。</p>
<p>如今 <code>Typescript</code> 在 Node 中的应用已经越来越广泛，所以笔者将实现一个可以运行 TS 代码的 TypeScript 运行时。</p>
<h3 data-id="heading-5">操作步骤</h3>
<h4 data-id="heading-6">准备工作</h4>
<p>为了更快更好地玩转 Serverless 应用，需要先安装阿里云的一个 <a href="https://help.aliyun.com/document_detail/64204.html" target="_blank" rel="nofollow noopener noreferrer">Fun工具</a>，它是一个用于支持 Serverless 应用部署的工具，能帮助我们便捷地管理函数计算、API 网关、日志服务等资源。它通过一个资源配置文件（template.yml），协助我们进行<strong>开发、构建、部署</strong>操作。</p>
<p>安装配置过程如下：</p>
<p>（1）安装：</p>
<pre><code class="hljs language-bash copyable" lang="bash">// 安装命令
$ npm install @alicloud/fun -g

// 执行 fun --version 检查安装是否成功
$ fun --version

3.6.21
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）安装好后，使用<code>fun config</code>命令配置账户信息（<a href="https://help.aliyun.com/document_detail/146702.html#section-h9e-864-bom" target="_blank" rel="nofollow noopener noreferrer">配置文档</a>），按照提示依次配置 Account ID、AccessKey ID、AccessKey Secret、Default Region Name。</p>
<p>配置完成后，先在本地创建一个 TypeScript 项目 custom-runtime-typescript，并安装相关依赖。</p>
<pre><code class="hljs language-$ copyable" lang="$">npm i typescript ts-node @types/node
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，开始 Custom Runtime 的开发流程，一步一步打造属于自己的自定义运行环境。</p>
<h4 data-id="heading-7">1.搭建一个具有监听端口的 HTTP Server</h4>
<ul>
<li>需要注意的是，这个服务一定要监听<code>0.0.0.0:CAPort</code>或<code>*:CAPort</code>端口，默认是 9000。如果使用<code>127.0.0.1:CAPort</code>端口，会导致请求超时</li>
</ul>
<p>用 TS 编写一个 HTTP Server 文件 server.ts 如下：</p>
<p>注意：在开发函数具体的逻辑之前，一般会确认开发的函数是事件函数还是 HTTP 函数</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> http <span class="hljs-keyword">from</span> <span class="hljs-string">'http'</span>;

<span class="hljs-comment">// 创建一个 HTTP Server</span>
<span class="hljs-keyword">const</span> server = http.createServer(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">req: http.IncomingMessage, res: http.ServerResponse</span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-keyword">var</span> rid = req.headers[<span class="hljs-string">"x-fc-request-id"</span>];
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`FC Invoke Start RequestId: <span class="hljs-subst">$&#123;rid&#125;</span>`</span>);
  
  <span class="hljs-keyword">var</span> rawData = <span class="hljs-string">""</span>;
  req.on(<span class="hljs-string">'data'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">chunk</span>) </span>&#123;
    rawData += chunk;
  &#125;);
  
  req.on(<span class="hljs-string">'end'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 处理业务逻辑 ……</span>
    <span class="hljs-built_in">console</span>.log(rawData);
    
    res.writeHead(<span class="hljs-number">200</span>);
    res.end(rawData);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`FC Invoke End RequestId: <span class="hljs-subst">$&#123;rid&#125;</span>`</span>);
  &#125;);
&#125;);

server.timeout = <span class="hljs-number">0</span>; <span class="hljs-comment">// never timeout</span>
server.keepAliveTimeout = <span class="hljs-number">0</span>; <span class="hljs-comment">// kee palive, never timeout</span>

<span class="hljs-comment">// 启动 HTTP 服务并监听 0.0.0.0:9000 端口</span>
server.listen(<span class="hljs-number">9000</span>, <span class="hljs-string">'0.0.0.0'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'FunctionCompute typescript runtime inited.'</span>);
&#125;);


<span class="copy-code-btn">复制代码</span></code></pre>
<p>编写完成后，可以先在本地测试该服务是否启动成功，通过安装在项目中的 ts-node 命令来运行上述代码：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 启动 HTTP 服务</span>

$ ./node_modules/.bin/ts-node server.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动后，在另一个终端中使用 curl 命令测试：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ curl 0.0.0.0:9000 -X POST -d <span class="hljs-string">"hello world"</span> -H <span class="hljs-string">"x-fc-request-id:123"</span> 

hello world
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若服务已正常启动，说明它可以在接收 HTTP 请求后处理业务逻辑，然后将处理结果再以 HTTP 响应的形式返回给 FaaS 平台。</p>
<h4 data-id="heading-8">2.创建一个启动目标 Server 的可执行文件 bootstrap</h4>
<p>函数计算冷启动 Custom Runtime 时，会默认调用 bootstrap 文件启动自定义的 HTTP Server。然后这个 HTTP Server 接管了函数计算系统的所有请求。</p>
<ul>
<li>bootstrap 是运行时入口引导程序文件，它会告诉 FaaS 如何启动你的自定义运行时。Custom Runtime 加载函数时会固定检索 bootstrap 同名文件，并执行该程序来启动 Custom Runtime 运行时。</li>
<li>bootstrap 需具备 777 或 755 可执行权限</li>
<li>如果是 shell 脚本，一定要添加<code>#!/bin/bash</code></li>
</ul>
<p>创建 bootstrap 文件如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-meta">#!/bin/bash</span>
./node_modules/.bin/ts-node server.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">3.编写资源配置文件 template.yaml</h4>
<p>在当前目录下编写一份用于部署到函数计算的资源配置文件 template.yaml：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">ROSTemplateFormatVersion:</span> <span class="hljs-string">'2015-09-01'</span>
<span class="hljs-attr">Transform:</span> <span class="hljs-string">'Aliyun::Serverless-2018-04-03'</span>
<span class="hljs-attr">Resources:</span>
  <span class="hljs-attr">custom-runtime:</span> <span class="hljs-comment"># 服务名称</span>
    <span class="hljs-attr">Type:</span> <span class="hljs-string">'Aliyun::Serverless::Service'</span> 
    <span class="hljs-attr">Properties:</span>
      <span class="hljs-attr">Description:</span> <span class="hljs-string">'helloworld'</span>
    <span class="hljs-attr">custom-runtime-ts:</span> <span class="hljs-comment"># 函数名称</span>
      <span class="hljs-attr">Type:</span> <span class="hljs-string">'Aliyun::Serverless::Function'</span> 
      <span class="hljs-attr">Properties:</span>
        <span class="hljs-attr">Handler:</span> <span class="hljs-string">index.handler</span> <span class="hljs-comment"># Handler 在此时没有实质意义，填写任意的一个满足函数计算 Handler 字符集约束的字符串即可， 例如 index.handler</span>
        <span class="hljs-attr">Runtime:</span> <span class="hljs-string">custom</span> <span class="hljs-comment"># custom 代表自定义运行时</span>
        <span class="hljs-attr">MemorySize:</span> <span class="hljs-number">512</span>
        <span class="hljs-attr">CodeUri:</span> <span class="hljs-string">'./'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">4.部署、调用测试、完成</h4>
<p>（1）使用<code>fun deploy -y </code> 命令将我们的自定义运行时和业务逻辑代码所有资源部署到阿里云。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55cc6d9b8bdb4a7cad3d8b9ae90ec662~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210505220309647" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（2）使用命令调用部署函数，验证</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ fun invoke -e <span class="hljs-string">"hello,my custom runtime"</span>  
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12d18e40cd0f4959b49b370eda7cacd4~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210505220520916" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到成功输出，就代表我们的 custom runtime 大功告成了！它可以直接运行我们写的 TS 代码了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14f8efab7cce43b4bab755921370b457~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210505223345696" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">实现 Custom Container Runtime</h2>
<p>TS 的运行环境问题可以用  Custom Runtime 解决，但是 Node 某些版本平台不支持的问题，就不能用同样的办法了。因为 Node 是全局安装的，依赖系统环境。</p>
<p>FC  平台已经为我们想好了此类问题的解决办法，为我们提供了 Custom Container Runtime （自定义容器运行环境）的能力。FaaS 平台有这种能力，是因为它的底层实现原理是 <strong>Docker 容器</strong>，所以它通过运用容器技术，<strong>把我们的应用代码和运行环境打包为 Docker 镜像</strong>，保持环境一致性。实现一次构建，到处运行。</p>
<h4 data-id="heading-12">工作原理</h4>
<p>Custom Container Runtime 工作原理与<a href="https://help.aliyun.com/document_detail/132044.htm#Task-2259898" target="_blank" rel="nofollow noopener noreferrer">Custom Runtime</a> 基本相同：</p>
<ul>
<li>函数计算系统初始化执行环境实例前会扮演该函数的服务角色，获得临时用户名和密码并<strong>拉取镜像</strong>。</li>
<li>拉取成功后根据指定的启动命令 Command、参数 Args 及 CAPort 端口（默认 9000 ）启动自定义的 HTTP Server。</li>
<li>然后这个 HTTP Server 接管了函数计算系统的所有请求，包括来自事件函数调用及 HTTP 函数调用。</li>
</ul>
<p>下面我们自定义一个 Node v16.1.0 版本的容器运行环境。</p>
<h4 data-id="heading-13">操作步骤</h4>
<h5 data-id="heading-14">1.自定义 HTTP Server</h5>
<p>这一步和 Custom Runtime 相同，使用 Node.js Express 自定义一个 Http 服务 server.js，GET 和 POST 方法分别路由至不同的 Handler:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// server.js 文件</span>
<span class="hljs-meta">'use strict'</span>;

<span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);

<span class="hljs-comment">// Constants</span>
<span class="hljs-keyword">const</span> PORT = <span class="hljs-number">9000</span>;
<span class="hljs-keyword">const</span> HOST = <span class="hljs-string">'0.0.0.0'</span>;

<span class="hljs-comment">// HTTP 函数调用</span>
<span class="hljs-keyword">const</span> app = express();
app.get(<span class="hljs-string">'/*'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  res.send(<span class="hljs-string">`Hello FunctionCompute, http function, runtime is : Node <span class="hljs-subst">$&#123;process.version&#125;</span>\n`</span>);
&#125;);

<span class="hljs-comment">// 事件函数调用</span>
app.post(<span class="hljs-string">'/invoke'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  res.send(<span class="hljs-string">`Hello FunctionCompute, event function,runtime is : Node <span class="hljs-subst">$&#123;process.version&#125;</span>\n`</span>);
&#125;);

<span class="hljs-comment">// 启动 HTTP 服务并监听 9000 端口</span>
<span class="hljs-keyword">var</span> server = app.listen(PORT, HOST);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Running on http://<span class="hljs-subst">$&#123;HOST&#125;</span>:<span class="hljs-subst">$&#123;PORT&#125;</span>`</span>);

server.timeout = <span class="hljs-number">0</span>; <span class="hljs-comment">// never timeout</span>
server.keepAliveTimeout = <span class="hljs-number">0</span>; <span class="hljs-comment">// keepalive, never timeout</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动服务，本地测试一下：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 启动 HTTP 服务</span>
$ node server.js
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 新开一个终端，通过 curl 命令测试</span>
$ curl http://0.0.0.0:9000
Hello FunctionCompute, http GET, this runtime is : Node v11.5.0     <span class="hljs-comment"># 这是我本地的 Node 版本，后面在自定义容器中会输出 v16.1.0                 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>验证通过。</p>
<h5 data-id="heading-15">2.构建镜像并上传</h5>
<p>同样的，需要先做两个准备工作：</p>
<ul>
<li>
<p>1）安装启动 Docker</p>
</li>
<li>
<p>2）使用阿里云容器镜像服务<a href="https://cr.console.aliyun.com/" target="_blank" rel="nofollow noopener noreferrer">创建命名空间和镜像仓库</a>存放我们的自定义镜像</p>
</li>
</ul>
<p>接下来，先编写 Dockerfile，再构建包含我们 Node 指定版本运行环境和应用代码的镜像，最后上传到自己的镜像仓库。</p>
<p>（有需要的同学可以先看下这篇文章<a href="https://nodejs.org/zh-cn/docs/guides/nodejs-docker-webapp/" target="_blank" rel="nofollow noopener noreferrer">如何把一个 Node.js web 应用程序给 Docker 化</a> ）</p>
<p>(1) 编写 Dockerfile：</p>
<pre><code class="hljs language-dockerfile copyable" lang="dockerfile"><span class="hljs-comment"># 基于基础镜像 node:16.1.0-alpine3.11 构建我们自己的镜像</span>
<span class="hljs-keyword">FROM</span> node:<span class="hljs-number">16.1</span>.<span class="hljs-number">0</span>-alpine3.<span class="hljs-number">11</span>

<span class="hljs-comment"># 设置容器工作目录</span>
<span class="hljs-keyword">WORKDIR</span><span class="bash"> /usr/src/app</span>

<span class="hljs-comment"># 将 package.json 和 package-lock.json 都拷贝到工作目录</span>
<span class="hljs-keyword">COPY</span><span class="bash"> package*.json ./</span>

<span class="hljs-comment"># 安装依赖</span>
<span class="hljs-keyword">RUN</span><span class="bash"> npm install</span>

<span class="hljs-comment"># 将当前目录下的所有文件拷贝到容器工作目录中</span>
<span class="hljs-keyword">COPY</span><span class="bash"> . .</span>

<span class="hljs-comment"># 暴露容器 8080 端口</span>
<span class="hljs-keyword">EXPOSE</span> <span class="hljs-number">8080</span>

<span class="hljs-comment"># 在容器中启动应用程序</span>
<span class="hljs-keyword">ENTRYPOINT</span><span class="bash"> [ <span class="hljs-string">"node"</span>, <span class="hljs-string">"server.js"</span> ]</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）安装启动 Docker，登录阿里云镜像服务，构建并上传：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 登录</span>
$ sudo docker login --username=xxx registry.cn-hangzhou.aliyuncs.com
<span class="copy-code-btn">复制代码</span></code></pre>
<p>登录成功后，先构建 Docker 镜像：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 指定ACR镜像地址：其中 my_serverless 为你自己的容器命名空间；nodejs 为你自己的镜像仓库名称；v16.1.0 为镜像版本号</span>
$ <span class="hljs-built_in">export</span> IMAGE_NAME=<span class="hljs-string">"registry.cnhangzhou.aliyuncs.com/my_serverless/nodejs:v16.1.0"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash">
<span class="hljs-comment"># 构建镜像</span>
<span class="hljs-comment"># -t 给镜像取名字打标签，通常 name:tag 或者 name 格式</span>
$ docker build -t <span class="hljs-variable">$IMAGE_NAME</span> .
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再启动容器，本地打开浏览器 <a href="http://localhost:9000/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:9000/</a> 看是否可以正常响应，来验证我们的自定义镜像是否可以运行成功：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 启动容器： 将容器的 9000 端口映射到主机的 9000 端口</span>
$ docker run -p 9000:9000 -d <span class="hljs-variable">$IMAGE_NAME</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6acbfc32153e48f9a7df5e377e43bbd8~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210514150709489" loading="lazy" referrerpolicy="no-referrer">
<p>验证通过后，最后上传镜像：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 上传镜像</span>
$ docker push <span class="hljs-variable">$IMAGE_NAME</span>  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上传成功后，可以在阿里云镜像服务中看到我们的镜像。后面就可以使用它啦！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a32a2ed92de4f389269184a14c3d3be~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210509153919228" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-16">3.定义 template.yaml</h5>
<p>创建一个 <code>template.yaml</code>文件如下：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">ROSTemplateFormatVersion:</span> <span class="hljs-string">'2015-09-01'</span>
<span class="hljs-attr">Transform:</span> <span class="hljs-string">'Aliyun::Serverless-2018-04-03'</span>
<span class="hljs-attr">Resources:</span>
  <span class="hljs-attr">CustomContainerRuntime:</span> <span class="hljs-comment"># 服务名称</span>
    <span class="hljs-attr">Type:</span> <span class="hljs-string">'Aliyun::Serverless::Service'</span>
    <span class="hljs-attr">Properties:</span>
      <span class="hljs-attr">Policies:</span>
        <span class="hljs-bullet">-</span> <span class="hljs-string">AliyunContainerRegistryReadOnlyAccess</span>
      <span class="hljs-attr">InternetAccess:</span> <span class="hljs-literal">true</span>
    <span class="hljs-attr">nodejs-express-http:</span> <span class="hljs-comment"># 函数名称</span>
      <span class="hljs-attr">Type:</span> <span class="hljs-string">'Aliyun::Serverless::Function'</span>
      <span class="hljs-attr">Properties:</span>
        <span class="hljs-attr">Description:</span> <span class="hljs-string">'HTTP function powered by nodejs express'</span>
        <span class="hljs-attr">Runtime:</span> <span class="hljs-string">custom-container</span> <span class="hljs-comment"># 表示自定义容器</span>
        <span class="hljs-attr">Timeout:</span> <span class="hljs-number">60</span>
        <span class="hljs-attr">CAPort:</span> <span class="hljs-number">9000</span> <span class="hljs-comment"># 注意！这里Custom Container Runtime使用的监听端口一定要和HTTP Server监听的端口保持一致，否则会出现错误</span>
        <span class="hljs-attr">Handler:</span> <span class="hljs-string">not-used</span>
        <span class="hljs-attr">MemorySize:</span> <span class="hljs-number">1024</span>
        <span class="hljs-attr">CodeUri:</span> <span class="hljs-string">./</span>   <span class="hljs-comment"># Root directory for the function or the Dockerfile path</span>
        <span class="hljs-attr">CustomContainerConfig:</span> <span class="hljs-comment"># 容器镜像配置</span>
          <span class="hljs-comment"># Sample image value: registry-vpc.cn-shenzhen.aliyuncs.com/fc-demo/nodejs-express:v0.1  使用同地域的VPC镜像地址加速</span>
          <span class="hljs-attr">Image:</span> <span class="hljs-string">'registry.cn-hangzhou.aliyuncs.com/my_serverless/nodejs:v16.1.0'</span>
          <span class="hljs-attr">Command:</span> <span class="hljs-string">'[ "node"]'</span>
          <span class="hljs-attr">Args:</span> <span class="hljs-string">'["server.js"]'</span>
      <span class="hljs-attr">Events:</span>
        <span class="hljs-attr">http-trigger-test:</span>
          <span class="hljs-attr">Type:</span> <span class="hljs-string">HTTP</span>
          <span class="hljs-attr">Properties:</span>
              <span class="hljs-attr">AuthType:</span> <span class="hljs-string">ANONYMOUS</span>
              <span class="hljs-attr">Methods:</span> [<span class="hljs-string">'GET'</span>, <span class="hljs-string">'POST'</span>, <span class="hljs-string">'PUT'</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">4.部署测试</h5>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 使用命令部署到 FC </span>
$ fun deploy -y
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/319556a34c8b4ad5bc861a3b432f7ab9~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210509163842880" loading="lazy" referrerpolicy="no-referrer">
<p>部署成功后，我们去 FC 平台上进行测试。</p>
<p>因为我们在<code>template.yaml</code> 中配置的触发器是 http 触发器，所以我们点击“执行”按钮进行调试，发现正常运行,返回结果为  runtime is : Node v16.1.0，说明我们的自定义容器运行环境也成功实现了！</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3553a89ace54a618a85304ca32d5d5b~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210509163945647" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-18">小结</h2>
<p>Custom Runtime 为我们打破了 FaaS 平台对语言的限制；Custom Container Runtime 让开发者可以将应用代码和运行环境打包成容器镜像作为函数的交付物，优化开发者体验、提升开发和交付效率。</p>
<p>自定义（容器）运行时让我们开发者使用 Serverless 的自由度更高，通过它们可以让我们无需代码改造，一键迁移我们的 Web 应用。</p>
<h2 data-id="heading-19">参考资料</h2>
<p><a href="https://stackoverflow.com/questions/3900549/what-is-runtime" target="_blank" rel="nofollow noopener noreferrer">what-is-runtime</a></p>
<p><a href="https://zhuanlan.zhihu.com/p/137204273" target="_blank" rel="nofollow noopener noreferrer">为阿里云 serverless 打造 Deno 运行时</a></p>
<p><a href="https://cloud.tencent.com/document/product/583/47274" target="_blank" rel="nofollow noopener noreferrer">Custom Runtime 说明</a></p>
<p><a href="https://help.aliyun.com/document_detail/64204.html" target="_blank" rel="nofollow noopener noreferrer">fun 工具</a></p>
<p><a href="https://developer.aliyun.com/article/772788" target="_blank" rel="nofollow noopener noreferrer">函数计算支持容器镜像-加速应用 Serverless 进程</a></p>
<p><a href="https://cloud.tencent.com/developer/article/1690709" target="_blank" rel="nofollow noopener noreferrer">Custom Runtime - 打破云函数语言限制</a></p>
<h2 data-id="heading-20">推荐阅读</h2>
<p><a href="https://zoo.team/article/about-vite" target="_blank" rel="nofollow noopener noreferrer">Vite 特性和部分源码解析</a></p>
<p><a href="https://juejin.cn/post/6974184935804534815" target="_blank">我在工作中是如何使用 git 的</a></p>
<p><a href="https://juejin.cn/post/6976798974757830687" target="_blank">15 分钟学会 Immutable</a></p>
<h2 data-id="heading-21">开源作品</h2>
<ul>
<li>政采云前端小报</li>
</ul>
<p><strong>开源地址 <a href="https://www.zoo.team/openweekly/" target="_blank" rel="nofollow noopener noreferrer">www.zoo.team/openweekly/</a></strong> (小报官网首页有微信交流群)</p>
<h2 data-id="heading-22">招贤纳士</h2>
<p>政采云前端团队（ZooTeam），一个年轻富有激情和创造力的前端团队，隶属于政采云产品研发部，Base 在风景如画的杭州。团队现有 40 余个前端小伙伴，平均年龄 27 岁，近 3 成是全栈工程师，妥妥的青年风暴团。成员构成既有来自于阿里、网易的“老”兵，也有浙大、中科大、杭电等校的应届新人。团队在日常的业务对接之外，还在物料体系、工程平台、搭建平台、性能体验、云端应用、数据分析及可视化等方向进行技术探索和实战，推动并落地了一系列的内部技术产品，持续探索前端技术体系的新边界。</p>
<p>如果你想改变一直被事折腾，希望开始能折腾事；如果你想改变一直被告诫需要多些想法，却无从破局；如果你想改变你有能力去做成那个结果，却不需要你；如果你想改变你想做成的事需要一个团队去支撑，但没你带人的位置；如果你想改变既定的节奏，将会是“5 年工作时间 3 年工作经验”；如果你想改变本来悟性不错，但总是有那一层窗户纸的模糊… 如果你相信相信的力量，相信平凡人能成就非凡事，相信能遇到更好的自己。如果你希望参与到随着业务腾飞的过程，亲手推动一个有着深入的业务理解、完善的技术体系、技术创造价值、影响力外溢的前端团队的成长历程，我觉得我们该聊聊。任何时间，等着你写点什么，发给 <code>ZooTeam@cai-inc.com</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d3aa3d1f8646a8bcda8cfd9e335a4b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            