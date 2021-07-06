
---
title: '让你 nodejs 水平暴增的 debugger 技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fd124fa151948b7a59649ea87f707ba~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 06:29:36 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fd124fa151948b7a59649ea87f707ba~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
</blockquote>
<p>学习 nodejs 最重要的是什么？可能每个人都有自己的答案。</p>
<p>我觉得学习 nodejs 除了要掌握基础的 api、常用的一些包外，最重要的能力是学会使用 debugger。因为当流程复杂的时候，断点调试能够帮你更好的理清逻辑，有 bug 的时候也能更快的定位问题。</p>
<p>狼叔说过，是否会使用 debugger 是区分一个程序员 nodejs 水平的重要标志。</p>
<p>本文分享一下 debugger 的原理和 vscode debugger 的使用技巧。</p>
<h2 data-id="heading-0">debugger 原理</h2>
<p>运行 nodejs 代码的时候，如果带上了 <code>--inspect</code>（可以打断点） 或者 <code>--inspect-brk</code>（可以打断点，并在首行断住） 的参数，那么就会以 debugger 的模式启动：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fd124fa151948b7a59649ea87f707ba~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，node 启动了一个 web socket 的 server，地址是：ws://127.0.0.1:9229/78637688-e8e0-4582-80cc-47655f4bff66</p>
<p><strong>为什么 debugger 要启动一个 websocket server 呢？</strong></p>
<p>debugger 的含义就是要在某个地方断住，可以单步运行、查看环境中的变量。那么怎么设置断点、怎么把当前上下文的变量暴露出去呢，就是通过启动一个 websocket server，这时候只要启动一个 websocket client 连接上这个 server 就可以调试 nodejs 代码了。</p>
<h3 data-id="heading-1">v8 debug protocol</h3>
<p>连上之后呢，debugger server 和 debugger client 怎么交流？这就涉及到了 v8 debug protocol。</p>
<p>通过两边都能识别的格式来交流，比如：</p>
<p>在 test.js 的 100 行 设置断点：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"seq"</span>:<span class="hljs-number">118</span>,
    <span class="hljs-string">"type"</span>:<span class="hljs-string">"request"</span>,
    <span class="hljs-string">"command"</span>:<span class="hljs-string">"setbreakpoint"</span>,
    <span class="hljs-string">"arguments"</span>:&#123;
        <span class="hljs-string">"type"</span>:<span class="hljs-string">"script"</span>,
        <span class="hljs-string">"target"</span>:<span class="hljs-string">"test.js"</span>,
        <span class="hljs-string">"line"</span>:<span class="hljs-number">100</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后查看当前作用域的变量：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"seq"</span>:<span class="hljs-number">117</span>,
    <span class="hljs-string">"type"</span>:<span class="hljs-string">"request"</span>,
    <span class="hljs-string">"command"</span>:<span class="hljs-string">"scope"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行一个表达式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"seq"</span>:<span class="hljs-number">118</span>,
    <span class="hljs-string">"type"</span>:<span class="hljs-string">"request"</span>,
    <span class="hljs-string">"command"</span>:<span class="hljs-string">"evaluate"</span>,
    <span class="hljs-string">"arguments"</span>:&#123;
        <span class="hljs-string">"expression"</span>:<span class="hljs-string">"a()"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后继续运行：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"seq"</span>:<span class="hljs-number">117</span>,
    <span class="hljs-string">"type"</span>:<span class="hljs-string">"request"</span>,
    <span class="hljs-string">"command"</span>:<span class="hljs-string">"continue"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这种方式，client 就可以告诉 debugger server 如何执行代码。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2cfd231896b4407bf6ecc0fa9f42312~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">debugger client</h3>
<p>debugger client 一般都是有 ui 的（当然，在命令行里面通过命令来调试也可以，但一般不这么做）。常见的 js 的 debugger client 有 chrome devtools 和 vscode debugger 等。</p>
<p>我们写一个简单的 js 脚本，通过 node --inspect-brk 跑起来：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c6470d62cda44cb97cf8268a9ccebbf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到它启动在了 9229 端口，</p>
<p>然后，我们分别通过两种 client 连上它。</p>
<h4 data-id="heading-3">chrome devtools</h4>
<p>在 chrome 地址栏输入 chrome://inspect，然后点击 configure 来配置目标端口：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2590e76ebe04451b580c48d31a0640a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>把刚才的端口 9229 填上去：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0ca29859b8f43eaa8673bed5149aff3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后就可以看到 chrome 扫描到了这个 target，点击 inspect 就可以连上这个 debugger server。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a5f4342191c4fc8a10f9a048251cf16~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f92c17f12a34e5fbb1b4a83b83ba21b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>之后就可以设置断点、单步执行、执行表达式、查看作用域变量等，这些功能都是通过 v8 debug protocol 来实现的。</p>
<h4 data-id="heading-4">vscode debugger</h4>
<p>在 vscode 里面写代码，在 chrome devtools 里调试比较麻烦，vscode 也实现了 debugger 的支持，可以直接用 vscode 来调试。</p>
<p>使用vscode 调试能力的方式是修改项目根目录下的 .vscode/launch.json 配置。</p>
<h5 data-id="heading-5">attach</h5>
<p>点击右下角的按钮来添加一个配置项。这里选择 nodejs 的 attach：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c4512e763be4ced84b183379cfb60b5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为已经通过 node --inspect-brk 启动了 websocket 的 debugger server，那么只需要启动 websocket client，然后 attach 上 9229 端口就行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a08f6c47f38543a8846542593e2bbac2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击左侧的按钮，就可以连上 debugger server 开始调试：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd68ff4e05fd4e4db551af70fb782477~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-6">launch</h5>
<p>这样先通过 node --inspect-brk 启动 debugger server，然后再添加 vscode debug 配置来连接上太麻烦了，能不能把这两步合并呢？</p>
<p>当然可以，只要添加一个 launch 的配置：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef41e2b3038440ac8909d86af73e7efd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7594fb35747444eb562658266e77089~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里的 type 是 launch，就是启动 debgger server 并且启动一个 debugger client 连接上该 server。运行的程序是根目录下的 index2.js，还可以设置 stopOnEntry 来在首行断住。</p>
<p>点击调试，就可以看到能够成功的调试该 js 文件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/530a94d4b65d4038b8c1586d411bcbc4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>vscode 会启动 debugger server，然后启动 debugger client 自动连接上该 server，这些都不需要我们去关心。</p>
<p>这样我们就可以成功的使用 vscode debugger 来调试 nodejs 代码。</p>
<h2 data-id="heading-7">vscode debugger 进阶</h2>
<p>debugger client 中我们最常用的还是 vscode，这里着重讲一下 vscode debugger 的各种场景下的配置。</p>
<h3 data-id="heading-8">sourcemap</h3>
<p>如果调试 ts 代码，肯定不能调试编译后的代码，要能够映射回源码，这个是 sourcemap 做的事情。调试工具都支持 sourcemap，比如 chrome devtools 和 vscode debugger，都支持文件末尾的 sourcemap url 的解析：</p>
<pre><code class="copyable">//# sourceMappingURL=index.js.map
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样当调试 index.js的时候，如果它是 ts 编译的出来的，就会自动找到对应的 ts。</p>
<p>当然，如果调试配置里面直接指定了 ts，那么要能够调试需要再配置 outFiles，告诉 vscode 去哪里找 sourcemap。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7de612655fb147c4880e83198640e6ec~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样，在 ts 源码中打的断点和在编译出的 js 打的断点都能生效。</p>
<h3 data-id="heading-9">多进程调试</h3>
<p>当代码中有子进程的时候，就有了第二条控制流，需要再启动一个 debugger。</p>
<p>比如 vscode，它是基于 electron，需要启动一个主进程，一些渲染进程。主进程是通过 launch 启动的，而渲染进程则是后来 attach 的。</p>
<p>主进程启动的时候，通过 --remote-debugging-port 来指定子进程自动的时候的 debugger server 的端口。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d6b9b47c6e84c53961fa7fde4796acb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>outFiles 来指定 sourcemap 的位置，这样才可以直接调试 ts 源码。runtimeExecutable 是用 vscode 的运行时替代掉了 nodejs（一般不需要设置）。</p>
<p>然后渲染进程是后面启动的，我们通过参数配置了会启动在 9222 端口，那么只要 attach 到那个端口就可以调试该进程了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d91f9731dfb41e5bb801e1f5ecd6bf4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>vscode 支持多 target 调试，也就是可以在 vscode 里面同时启动 多个 debugger。可以切换不同的 debugger 来调试不同的进程。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06488cee74c94568ad97df513101e662~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">彩蛋</h2>
<p>debugger 只能打断点么，不是的，它还可以这么用，加日志，不污染源码。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/227bdaee3172484eb016f9d18334c573~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22e9aa616698444c9782f94684312e44~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50d64dd8156a4f3683f1b1b355746b3f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9657aa4ba5814e83bdb71483ff372810~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">总结</h2>
<p>debugger 的使用是一项很重要的能力，对于 nodejs 水平的提升很有帮助。</p>
<p>nodejs debugger 的原理是 js 引擎会启动 debugger server（websocket），等待客户端连接，我们可以通过各种 debugger client 连上来进行调试，比如 chrome devtools、vscode debugger。</p>
<p>调试 nodejs 代码更多还是使用 vscode debugger（当然有的时候也会使用 chrome devtools 调试，基于 chrome devtools 的 memory 来进行内存分析，定位内存泄漏问题的时候很有帮助）。</p>
<p>vscode debugger 的使用主要是在 .vscode/launch.json 里面添加调试配置。</p>
<p>调试配置分为 launch 和 attach 两种：</p>
<ul>
<li>launch 会启动 debugger server 并用 debugger client 连接上</li>
<li>attach 只是启动 debugger client 连接上已有的 debugger server，所以要指定端口</li>
</ul>
<p>具体的配置项常用的有：</p>
<ul>
<li>outFiles 指定 sourcemap 的位置，用来调试 ts 源码等需要编译的代码</li>
<li>stopOnEntry 在首行停住</li>
<li>args 来指定一些命令行参数</li>
<li>runtimeExecutable 当运行时不是 nodejs 的时候需要指定，比如 vscode 或者其他的一些运行时</li>
</ul>
<p>基于这些配置我们就可以调试各种场景下的 nodejs 代码，需要编译的，或者多个进程的。</p>
<p><strong>不夸张地说，如果你熟悉了 debugger 的使用，理解各种 nodejs 代码都会简单很多。</strong> 希望这篇文章能够帮助大家了解 debugger 的原理，并且能够使用 chrome devtools 或者 vscode debugger 来调试 nodejs 代码。知道有 sourcemap 以及多进程的情况下都怎么调试。</p></div>  
</div>
            