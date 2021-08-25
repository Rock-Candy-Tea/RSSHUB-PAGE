
---
title: 'noVNC 连 openstack'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6046'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 18:55:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=6046'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">添加 NoVNC 和 websokify 库</h2>
<p>要添加 noVNC 库，请在命令行中执行以下命令：</p>
<pre><code class="copyable">$ npm i @novnc/novnc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后转到<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnovnc%2Fwebsockify-js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/novnc/websockify-js" ref="nofollow noopener noreferrer"><strong>websockify-js</strong></a> github 页面并将库下载为 zip 文件。我将它解压到我的项目根文件夹 <strong>/vnc-client/tools/websockify-js/ 下</strong>。</p>
<pre><code class="copyable">➜  websockify-js
    ├── CHANGES.txt
    ├── LICENSE.txt
    ├── README.md
    ├── docs
    │   ├── LICENSE.GPL-3
    │   ├── LICENSE.LGPL-3
    │   ├── LICENSE.MPL-2.0
    │   ├── TODO
    │   ├── notes
    │   └── release.txt
    ├── include
    │   ├── VT100.js
    │   ├── keysym.js
    │   ├── util.js
    │   ├── websock.js
    │   ├── webutil.js
    │   ├── wsirc.js
    │   └── wstelnet.js
    ├── websockify
    │   ├── package.json
    │   └── websockify.js
    ├── wsirc.html
    └── wstelnet.html
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从这个位置执行这些命令来<strong>安装 websockify 依赖项</strong>：</p>
<pre><code class="copyable">$ cd websockify
$ npm install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们可以<strong>运行 websockify 服务器</strong>：</p>
<pre><code class="copyable">$ ./websockify.js [options] SOURCE_ADDR:PORT TARGET_ADDR:PORT
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例如，我将使用这些值运行命令，将<strong>websocket 流量</strong>从本地机器的端口<strong>5901</strong>（<em>vnc 服务器默认端口</em>）<strong>转发</strong>到端口<strong>6080</strong>：</p>
<pre><code class="copyable">$ ./websockify.js localhost:6080 localhost:5901

WebSocket settings:
    - proxying from localhost:6080 to localhost:5901
    - Running in unencrypted HTTP (ws://) mode
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们可以在<strong>package.json 中</strong>添加一个<strong>npm 脚本</strong>来启动<em>websockify 服务器</em>，转到<strong>脚本部分</strong>并添加以下行：
<code>"websockify": "node tools/websockify-js/websockify/websockify.js"</code></p>
<p>这在<strong>package.json 中</strong></p>
<pre><code class="copyable">&#123;
  "name": "vnc-client",
  "version": "0.0.0",
  "scripts": &#123;
    "ng": "ng",
    "start": "ng serve",
    "build": "ng build",
    "test": "ng test",
    "lint": "ng lint",
    "e2e": "ng e2e",
    "websockify": "node tools/websockify-js/websockify/websockify.js"
  &#125;,
  .
  .
  .
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以我们可以使用以下命令从<strong>项目主文件夹</strong>启动<em>websockify 服务器</em>：</p>
<pre><code class="copyable">$ npm run websockify localhost:6080 localhost:5901

> vnc-client@0.0.0 websockify ~/vnc-client
> node tools/websockify-js/websockify/websockify.js "localhost:6080" "localhost:5901"

WebSocket settings:
    - proxying from localhost:6080 to localhost:5901
    - Running in unencrypted HTTP (ws://) mode
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你在<strong>linux</strong>上<em>的 websockify Javascript 版本</em>有问题，从<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnovnc%2Fwebsockify" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/novnc/websockify" ref="nofollow noopener noreferrer"><strong>这里</strong></a>下载 python 版本，解压后你可以用这个命令运行它：</p>
<pre><code class="copyable">$ ./run localhost:6080 localhost:5901
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">在 Angular 组件中实现 NoVNC</h2>
<p>在这里，我们将在<strong>app.component 中</strong>实现 noVNC 。<br>
<br>
在<em>html 文件中</em>添加一个<code>div</code>以托管 Vnc 屏幕。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> ></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"screen"</span>></span>
      <span class="hljs-comment"><!-- This is where the remote screen will appear --></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<strong>app.component.ts</strong>如下所示：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@angular/core"</span>;

<span class="hljs-keyword">import</span> RFB <span class="hljs-keyword">from</span> <span class="hljs-string">"../../node_modules/@novnc/novnc/core/rfb.js"</span>;

<span class="hljs-meta">@Component</span>(&#123;
  <span class="hljs-attr">selector</span>: <span class="hljs-string">"app-root"</span>,
  <span class="hljs-attr">templateUrl</span>: <span class="hljs-string">"./app.component.html"</span>,
  <span class="hljs-attr">styleUrls</span>: [<span class="hljs-string">"./app.component.css"</span>],
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppComponent</span> </span>&#123;
  title = <span class="hljs-string">"vnc-client"</span>;

  <span class="hljs-keyword">public</span> rfb: RFB;

  <span class="hljs-function"><span class="hljs-title">startClient</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Starting !!!"</span>);

    <span class="hljs-comment">// Read parameters specified in the URL query string</span>
    <span class="hljs-comment">// By default, use the host and port of server that served this file</span>
    <span class="hljs-keyword">const</span> host = <span class="hljs-built_in">window</span>.location.hostname;
    <span class="hljs-keyword">const</span> port = <span class="hljs-string">"6080"</span>;
    <span class="hljs-keyword">const</span> password = <span class="hljs-string">"foobar"</span>; <span class="hljs-comment">// password of your vnc server</span>
    <span class="hljs-keyword">const</span> path = <span class="hljs-string">"websockify"</span>;
    <span class="hljs-comment">// Build the websocket URL used to connect</span>
    <span class="hljs-keyword">let</span> url = <span class="hljs-string">"ws"</span>;

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.location.protocol === <span class="hljs-string">"https:"</span>) &#123;
      url = <span class="hljs-string">"wss"</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      url = <span class="hljs-string">"ws"</span>;
    &#125;

    url += <span class="hljs-string">"://"</span> + host;
    <span class="hljs-keyword">if</span> (port) &#123;
      url += <span class="hljs-string">":"</span> + port;
    &#125;
    url += <span class="hljs-string">"/"</span> + path;

    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"URL: "</span>, url);

    <span class="hljs-comment">// Creating a new RFB object will start a new connection</span>
    <span class="hljs-built_in">this</span>.rfb = <span class="hljs-keyword">new</span> RFB(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"screen"</span>), url, &#123;
      <span class="hljs-attr">credentials</span>: &#123; <span class="hljs-attr">password</span>: password &#125;,
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后，在另一个命令行中重新启动 angular 应用程序</p>
<pre><code class="copyable">$ ng serve
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就是这样，您的 Vnc 客户端已启动并正在运行。</p>
<h2 data-id="heading-2">连接openstack</h2>
<p>首先从openstack获取vnc url</p>
<pre><code class="copyable">[root@hcloud-controller ~]# openstack console url show instance-b
+-------+--------------------------------------------------------------------------------------------------+
| Field | Value                                                                                            |
+-------+--------------------------------------------------------------------------------------------------+
| type  | novnc                                                                                            |
| url   | http://hcloud-controller:6080/vnc_auto.html?path=%3Ftoken%3Dcbbe83a2-f8d3-4520-affb-321fe41fa0d0 |
+-------+--------------------------------------------------------------------------------------------------+
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用这个url就可以直接访问vnc客户端, 需要将hcloud-controller 替换成openstack的ip地址。</p>
<h3 data-id="heading-3">我们也可以自己搭建客户端</h3>
<p>这里我们就不需要用<em>websockify</em>进行代理</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Component, OnInit &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>;
<span class="hljs-comment">// @ts-ignore</span>
<span class="hljs-keyword">import</span> RFB <span class="hljs-keyword">from</span> <span class="hljs-string">'../../node_modules/@novnc/novnc/core/rfb.js'</span>;

<span class="hljs-meta">@Component</span>(&#123;
  <span class="hljs-attr">selector</span>: <span class="hljs-string">'app-root'</span>,
  <span class="hljs-attr">templateUrl</span>: <span class="hljs-string">'./app.component.html'</span>,
  <span class="hljs-attr">styleUrls</span>: [<span class="hljs-string">'./app.component.scss'</span>]
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppComponent</span> <span class="hljs-title">implements</span> <span class="hljs-title">OnInit</span></span>&#123;
  title = <span class="hljs-string">'vnc-client'</span>;
  <span class="hljs-comment">// 直接用openstack生成的loken</span>
  url = <span class="hljs-string">'ws://hcloud-controller:6080/?token=cbbe83a2-f8d3-4520-affb-321fe41fa0d0'</span>;
  <span class="hljs-keyword">public</span> rfb: RFB;

  ngOnInit(): <span class="hljs-built_in">void</span> &#123;
    <span class="hljs-built_in">this</span>.startClient();
    <span class="hljs-comment">// @ts-ignore</span>
    <span class="hljs-built_in">window</span>.rfb = <span class="hljs-built_in">this</span>.rfb;
  &#125;

  startClient(): <span class="hljs-built_in">void</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'URL: '</span>, <span class="hljs-built_in">this</span>.url);

    <span class="hljs-comment">// Creating a new RFB object will start a new connection</span>
    <span class="hljs-built_in">this</span>.rfb = <span class="hljs-keyword">new</span> RFB(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'screen'</span>), <span class="hljs-built_in">this</span>.url, &#123;
      <span class="hljs-attr">credentials</span>: &#123;&#125;,
      <span class="hljs-attr">wsProtocols</span>: [<span class="hljs-string">'binary'</span>] <span class="hljs-comment">//协议</span>
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            