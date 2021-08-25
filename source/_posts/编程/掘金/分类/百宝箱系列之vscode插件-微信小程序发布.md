
---
title: '百宝箱系列之vscode插件-微信小程序发布'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 15:20:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5683af50e01462c88e480d2b0451d47~tplv-k3u1fbpfcp-watermark.image" alt="1629709383643_毅轩.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这是第 112 篇不掺水的原创，想获取更多原创好文，请搜索公众号关注我们吧~ 本文首发于政采云前端博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzoo.team%2Farticle%2Fvscode-wechat" target="_blank" rel="nofollow noopener noreferrer" title="https://zoo.team/article/vscode-wechat" ref="nofollow noopener noreferrer">百宝箱系列之vscode插件-微信小程序发布</a></p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>开发当中我们会经常碰到很多觉得麻烦的事情，一些流程又臭又长，像老太太裹脚布一样的步骤。比如我们亲爱的小程序，那流程那步骤让我的 Mac 13 寸丐中丐版很是蛋疼。每次都得打开 N 多东西才能发布到预览。蓝瘦，真是个磨人的小妖精。</p>
<h2 data-id="heading-1">分析和拆解</h2>
<p><strong>关于 Vscode 插件开发基础教程<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcode.visualstudio.com%2Fapi" target="_blank" rel="nofollow noopener noreferrer" title="https://code.visualstudio.com/api" ref="nofollow noopener noreferrer">请移步官方文档</a>，这里就不过多赘述了，这边我们只把重心放到去实现小程序自动构建发布关键点的实现上。</strong></p>
<p>由于我们使用的是 uni-app 作为多端统一的方向，所以在每次开发或者提测小程序需要发到预览版上的时候都需要经历如下步骤：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/982554bcf52d40018a9c612a9123d117~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>ok，既然都已经大致理清楚流程了，那么拥有程序员严谨态度的我们，分析分析整个过程中需要用到的哪些能力？接下来我们只对每个环节关键的部分做一些分析和拆解，不做全盘 Vscode 插件代码的结构和代码分析。</p>
<ol>
<li>前置工作
<ul>
<li>选择构建分支，版本并填写描述
<ul>
<li>Vscode 插件 window 能力 - 输入描述，下拉框选择</li>
<li>Git 能力 - 拉取分支</li>
</ul>
</li>
<li>临时保存当前分支修改
<ul>
<li>Git 能力 - 保存当前分支</li>
</ul>
</li>
<li>切换到目标分支
<ul>
<li>Git 能力- 切换分支</li>
</ul>
</li>
</ul>
</li>
<li>本地构建
<ul>
<li>自动生成版本号
<ul>
<li>微信开发平台 api 能力- 获取当前 AppID 最近模板列表</li>
</ul>
</li>
<li>注入目标小程序 AppID
<ul>
<li>Shell 调用能力- 修改文件内容注入 AppID</li>
</ul>
</li>
<li>运行 uni-app 构建命令
<ul>
<li>Shell 调用能力 - 执行构建命令</li>
</ul>
</li>
<li>撤销发布临时修改文件
<ul>
<li>Git 调用能力- 使用 Git 来撤销修改文件</li>
</ul>
</li>
</ul>
</li>
<li>部署小程序
<ul>
<li>上传云端草稿箱
<ul>
<li>微信开发工具调用能力</li>
</ul>
</li>
<li>移动到模板库
<ul>
<li>微信开发平台 api 能力</li>
</ul>
</li>
<li>部署预览版
<ul>
<li>Dubbo 能力 - 由于后端已经存在微信开发平台 accessToken 能力，直接调用获取</li>
</ul>
</li>
</ul>
</li>
</ol>
<p>Vscode 插件的 window 能力是默认就带的不需要实现，所以就 Shell 调用，Git 调用，Dubbo调用，微信开发平台 api 调用，微信开发工具调用需要实现。</p>
<p>再归归类，其实 Git 调用，和微信开发工具调用都是命令行调用也就是 Shell 调用，微信开发平台 api 调用其实本质就是 http 请求，但是里面最最重要的 accessKey 呢是直接调用政采云后端 Dubbo 接口获取，所以才需要 Dubbo。下面看看大致怎么去做呢？</p>
<h4 data-id="heading-2">Shell 的调用</h4>
<p>听到 Shell 菊花一紧，不熟悉的人觉得天哪很复杂的样子，其实就是使用 <code>child_process</code> 去开一个子进程，然后你就快乐的玩耍吧。所以我们在项目中封装了一个 shell.ts 来做所有 Shell  脚本的执行动作。 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fapi%2Fchild_process.html" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/api/child_process.html" ref="nofollow noopener noreferrer">不熟悉<code>child_process</code>的请移步这里</a></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// shell.ts 部分核心代码</span>
<span class="hljs-keyword">import</span> &#123; execFile, ExecFileOptions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"child_process"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">namespace</span> Shell &#123;
  <span class="hljs-comment">// 在 shell 中直接调用 git 的执行文件执行原始命令</span>
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">exec</span><<span class="hljs-title">TOut</span> <span class="hljs-title">extends</span> <span class="hljs-title">string</span> | <span class="hljs-title">Buffer</span>>(<span class="hljs-params">
    args: <span class="hljs-built_in">any</span>[],
    options: ExecFileOptions = &#123;&#125;
  </span>): <span class="hljs-title">Promise</span><<span class="hljs-title">TOut</span>> </span>&#123;
    <span class="hljs-keyword">const</span> &#123; stdin, stdinEncoding, execFileNameOrPath, ...opts &#125;: <span class="hljs-built_in">any</span> = &#123;
      <span class="hljs-attr">maxBuffer</span>: <span class="hljs-number">100</span> * <span class="hljs-number">1024</span> * <span class="hljs-number">1024</span>,
      ...options,
    &#125;;

    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span><TOut>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (!execFileNameOrPath) &#123; reject(<span class="hljs-string">'error'</span>); &#125;
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> proc = execFile(
          execFileNameOrPath,
          args,
          opts,
          <span class="hljs-function">(<span class="hljs-params">error: <span class="hljs-built_in">any</span> | <span class="hljs-literal">null</span>, stdout, stderr</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (error != <span class="hljs-literal">null</span>) &#123;
              reject(error);
              <span class="hljs-keyword">return</span>;
            &#125;
            resolve(
              stdout <span class="hljs-keyword">as</span> TOut
            );
          &#125;
        );

        <span class="hljs-keyword">if</span> (stdin !== <span class="hljs-literal">null</span>) &#123;
          proc.stdin?.end(stdin, stdinEncoding ?? <span class="hljs-string">"utf8"</span>);
        &#125;
      &#125;
      <span class="hljs-keyword">catch</span> (e) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
    &#125;);
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就可以通过 Shell.exec 方法传入参数就能直接调用了</p>
<h4 data-id="heading-3">Git 的调用</h4>
<p>有了上一个 Shell 作为基础我们就可以开干 Git 的调用了，在 Shell 中第一个参数是命令的执行文件，所以我们需要得到当前的 Git 的执行文件的地址作为第一个参数，后面其实就是正常的 Git 命令的拼接就够了。那么怎么知道当前 Git  的执行文件路径呢？</p>
<p>通过 Vscode 插件中集成的 Git 能力去得到 <code>extensions.getExtension("vscode.git")</code>，如下方式</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 获取 Vscode 内置的 Git Api</span>
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">async</span> getBuiltInGitApi(): <span class="hljs-built_in">Promise</span><BuiltInGitApi | <span class="hljs-literal">undefined</span>> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">const</span> extension = extensions.getExtension(<span class="hljs-string">"vscode.git"</span>) <span class="hljs-keyword">as</span> Extension<
        GitExtension
      >;
      <span class="hljs-keyword">if</span> (extension !== <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">const</span> gitExtension = extension.isActive
          ? extension.exports
          : <span class="hljs-keyword">await</span> extension.activate();

        <span class="hljs-keyword">return</span> gitExtension.getAPI(<span class="hljs-number">1</span>);
      &#125;
    &#125; <span class="hljs-keyword">catch</span> &#123;&#125;

    <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在返回的对象中 <code>gitApi.git.path  </code> 就是 Git 的执行文件路径。为了更加方便的调用，我们也封装了一个 git.ts 作为 Git 最最核心最最基础的调用</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//git.ts 的部分核心代码</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">namespace</span> Git &#123;
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">namespace</span> Core &#123;
    <span class="hljs-comment">// 在 shell 中直接调用  git 的执行文件执行原始命令</span>
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">exec</span><<span class="hljs-title">TOut</span> <span class="hljs-title">extends</span> <span class="hljs-title">string</span> | <span class="hljs-title">Buffer</span>>(<span class="hljs-params">
      args: <span class="hljs-built_in">any</span>[],
      options: GitExecOptions = &#123;&#125;
    </span>): <span class="hljs-title">Promise</span><<span class="hljs-title">TOut</span>> </span>&#123;

      options.execFileNameOrPath = gitInfo.execPath || <span class="hljs-string">""</span>;

      args.splice(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-string">"-c"</span>, <span class="hljs-string">"core.quotepath=false"</span>, <span class="hljs-string">"-c"</span>, <span class="hljs-string">"color.ui=false"</span>);

      <span class="hljs-keyword">if</span> (process.platform === <span class="hljs-string">"win32"</span>) &#123;
        args.splice(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-string">"-c"</span>, <span class="hljs-string">"core.longpaths=true"</span>);
      &#125;
      <span class="hljs-keyword">return</span> Shell.exec(args, options);
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在外部我们直接用 Git.Core.exec 方法直接执行对应的 Git 命令</p>
<h4 data-id="heading-4">微信开发工具调用</h4>
<p>首选我们要先<strong>检查开发者工具设置：需要在开发者工具的设置 -> 安全设置中开启服务端口</strong>。这样我们才能直接唤起开发者然后做些我们要做的事情。</p>
<p>再者我们需要知道微信开发者工具的执行文件地址。 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fminiprogram%2Fdev%2Fdevtools%2Fcli.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/miniprogram/dev/devtools/cli.html" ref="nofollow noopener noreferrer">详细请移步文档</a></p>
<p>macOS: <code><安装路径>/Contents/MacOS/cli</code></p>
<p>windows: <code><安装路径>/cli.bat</code></p>
<p>正常来说 Mac 地址 <strong>/Applications/wechatwebdevtools.app/Contents/MacOS/cli</strong></p>
<p>最后通过我们以前提供的 Shell 命令能力去执行就搞定了。是不是很简单。我们也封装了miniProgram.ts 来做这个事情</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//miniProgram.ts 核心代码</span>
<span class="hljs-keyword">import</span> &#123; ExecFileOptions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"child_process"</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> vscode <span class="hljs-keyword">from</span> <span class="hljs-string">"vscode"</span>;
<span class="hljs-keyword">import</span> &#123; Shell &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../shell'</span>;

<span class="hljs-keyword">interface</span> MiniProgramExecOptions <span class="hljs-keyword">extends</span> ExecFileOptions &#123;
  <span class="hljs-attr">branchName</span>: <span class="hljs-built_in">string</span>;
  execFileNameOrPath: <span class="hljs-built_in">string</span>;
  projectPath: <span class="hljs-built_in">string</span>,
  <span class="hljs-attr">userVersion</span>: <span class="hljs-built_in">string</span>,
  <span class="hljs-attr">userDesc</span>: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">namespace</span> MiniProgram &#123;
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">namespace</span> Core &#123;
    <span class="hljs-comment">// 在 shell 中直接调用 git 的执行文件执行原始命令</span>
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">exec</span><<span class="hljs-title">TOut</span> <span class="hljs-title">extends</span> <span class="hljs-title">string</span> | <span class="hljs-title">Buffer</span>>(<span class="hljs-params">
      args: <span class="hljs-built_in">any</span>[],
      options: MiniProgramExecOptions
    </span>): <span class="hljs-title">Promise</span><<span class="hljs-title">TOut</span>> </span>&#123;
      vscode;
      options.execFileNameOrPath = <span class="hljs-string">"/Applications/wechatwebdevtools.app/Contents/MacOS/cli"</span>;
      <span class="hljs-keyword">return</span> Shell.exec(args, options);
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">Duddo 的调用</h4>
<p>不明觉厉，都直接调 Dubbo 了吊的不行，其实很简单，有一个 nodeJs 的库 <code>node-zookeeper-dubbo</code> 再配合 <code>js-to-java</code> 这两个库就能搞定，只不过一些配置比较麻烦，我就把代码大致的贴出来</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> nzd = <span class="hljs-built_in">require</span>(<span class="hljs-string">"node-zookeeper-dubbo"</span>);
<span class="hljs-keyword">const</span> j2j = <span class="hljs-built_in">require</span>(<span class="hljs-string">"js-to-java"</span>);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> DubboInstance &#123;
  <span class="hljs-attr">mp</span>: &#123;
    <span class="hljs-attr">getComponentToken</span>: <span class="hljs-built_in">Function</span>;
  &#125;;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DubboService</span> </span>&#123;
  <span class="hljs-keyword">private</span> _dubbo: DubboInstance;
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">get</span> <span class="hljs-title">dubbo</span>(): <span class="hljs-title">DubboInstance</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._dubbo;
  &#125;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> options = &#123;
      <span class="hljs-attr">application</span>: <span class="hljs-string">"你的项目名称"</span>, <span class="hljs-comment">//项目名称</span>
      <span class="hljs-attr">register</span>: <span class="hljs-string">"你的服务器地址"</span>, <span class="hljs-comment">// zookeeper 服务器地址，多个服务器之间使用逗号分割  </span>
      <span class="hljs-attr">dubboVer</span>: <span class="hljs-string">"你的版本"</span>, <span class="hljs-comment">//dubbo 的版本，询问后端得知是2.3.5</span>
      <span class="hljs-attr">root</span>: <span class="hljs-string">'你的根节点'</span>, <span class="hljs-comment">//注册到 zookeeper 上的根节点名称</span>
      <span class="hljs-attr">dependencies</span>: &#123;
        <span class="hljs-comment">//依赖的 dubbo 服务集,也就是你要调用的服务的配置集合</span>
        <span class="hljs-attr">mp</span>: &#123;
          <span class="hljs-comment">//服务的标识，自定义的，按自己喜好</span>
          <span class="hljs-attr">interface</span>: <span class="hljs-string">"你的后端 dubbo 服务地址"</span>, <span class="hljs-comment">//后端 dubbo 服务地址</span>
          <span class="hljs-attr">version</span>: <span class="hljs-string">"你的服务版本号"</span>, <span class="hljs-comment">//服务版本号</span>
          <span class="hljs-attr">timeout</span>: <span class="hljs-string">"30000"</span>, <span class="hljs-comment">//超时时间</span>
          <span class="hljs-attr">group</span>: <span class="hljs-string">'你的分组'</span>, <span class="hljs-comment">//分组的功能也没有使用</span>
          <span class="hljs-attr">methodSignature</span>: &#123;
            <span class="hljs-comment">//服务里暴露的方法的签名，可以省略</span>
            <span class="hljs-attr">getComponentToken</span>: <span class="hljs-function">() =></span> <span class="hljs-function">() =></span> [],
          &#125;,
        &#125;,
      &#125;,
      <span class="hljs-attr">java</span>: j2j, <span class="hljs-comment">//使用 js-to-java 库来简化传递给 java  后端的值的写法</span>
    &#125;;
    <span class="hljs-built_in">this</span>._dubbo = <span class="hljs-keyword">new</span> nzd(options);
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此一些基本能力已经封装的差不多了</p>
<p>Shell：Shell.exec 方法</p>
<p>Git：Git.Core.exec 方法</p>
<p>微信开发工具： MiniProgram.Core.exec 方法</p>
<p>Dubbo: DobboService.dubbo.mp 方法</p>
<h2 data-id="heading-6">搞起</h2>
<h3 data-id="heading-7">前置工作</h3>
<p>因为我们要构建一个预发版，所以很有可能我们需要构建的分支不是我们当前工作的分支，所以这步骤的话更多的是要做好一些构建前的一些准备工作，总不能因为人家测试要一个预览测试版然后一不小心把我们自己本地的辛辛苦苦开发的东西弄没了吧，那真的是 f**k 了。</p>
<p>根据流程我们先来分解下大致的技术动作</p>
<ul>
<li>临时保存当前分支修改
<ul>
<li>获取当前分支。</li>
<li>如果是在当前分支啥都不管，否则 stash 下</li>
</ul>
</li>
<li>切换到需要发布分支
<ul>
<li>切换下分支</li>
</ul>
</li>
</ul>
<p>再精简下： 获取<strong>当前分支</strong> ---> <strong>保存修改</strong> --> <strong>切换分支</strong>。 都是 Git 的一些动作。那么在 nodeJs 中怎么开始自己的 Git 表演呢？一个关键点：Shell 脚本和命令的调用，所以这里的本质是调用 Shell。我们在上个章节中已经实现的 Shell 和 Git 的基本能力了，我们直接调用就行了。</p>
<h4 data-id="heading-8">使用 symbolic-ref  获取当前分支</h4>
<p>其实 Git 的命令分为两种</p>
<ul>
<li>高层命令（porcelain commands）</li>
<li>底层命令（plumbing commands）</li>
</ul>
<p>常用的命令大家都很熟悉了，什么 branch 啊， init 啊，add 啊，commit 啊等等。底层命令又是什么鬼，其实所有的高层命令的本质都是会调用底层命令，可以类比为语言层面 Java，C#，Js 这些高级语言他的底层是使用 C 或者 C++ 是一个概念。 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgit-scm.com%2Fbook%2Fen%2Fv2%2FGit-Internals-Plumbing-and-Porcelain" target="_blank" rel="nofollow noopener noreferrer" title="https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain" ref="nofollow noopener noreferrer">有兴趣请移步</a></p>
<p>symbolic-ref 命令能干嘛呢？</p>
<p>给定一个参数，读取哪个分支头部给定的符号 ref 引用并输出其相对于 <code>.git/</code> 目录的路径。通常，<code>HEAD </code> 以  参数的形式提供您的工作树所在的分支。</p>
<p>有了上面 git.ts 支持基本能力那么现在我们就很简单多了，<code>Git.Core.exec<string>(["symbolic-ref", "--short", "HEAD"], options);</code></p>
<p>在 git.ts 中增加基本命令方法</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// git.ts 部分代码</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">symbolicRef</span>(<span class="hljs-params">options: GitExecOptions = &#123;&#125;</span>) </span>&#123;
     <span class="hljs-keyword">return</span> Core.exec<<span class="hljs-built_in">string</span>>([<span class="hljs-string">"symbolic-ref"</span>, <span class="hljs-string">"--short"</span>, <span class="hljs-string">"HEAD"</span>], options);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 gitService 中实现 getCurrentBranch 方法</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// gitService.ts 部分代码</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">async</span> getCurrentBranch(filePath: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">Promise</span><<span class="hljs-built_in">string</span>> &#123;
    <span class="hljs-keyword">const</span> branchName = <span class="hljs-keyword">await</span> Git.Cmd.symbolicRef(&#123; <span class="hljs-attr">cwd</span>: filePath &#125;);
    <span class="hljs-keyword">return</span> branchName.replace(<span class="hljs-regexp">/\n/g</span>, <span class="hljs-string">""</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">保存修改和切换分支</h4>
<p>当我们获取到当前分支之后，和我们目标分支进行比对如果一致的话直接跳过该步骤，否则就需要对当前分支保存并且切换了。</p>
<p>为了方便对于保存和切换我们直接用了Git 的 stash 和 checkout 命令，并且封装了两个方法。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// git.ts 部分代码</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkout</span>(<span class="hljs-params">options: GitExecOptions = &#123;&#125;</span>) </span>&#123;
      <span class="hljs-keyword">const</span> params = [
        <span class="hljs-string">"checkout"</span>
      ];
      <span class="hljs-keyword">if</span> (options.branchName) &#123;
        params.push(options.branchName);
      &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(options.fileName)&#123;
        params.push(<span class="hljs-string">'--'</span>,options.fileName);
      &#125;
      <span class="hljs-keyword">return</span> Core.exec<<span class="hljs-built_in">string</span>>(params, options);
    &#125;
    
    <span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">stash</span>(<span class="hljs-params">options: GitExecOptions = &#123;&#125;</span>) </span>&#123;
      <span class="hljs-keyword">const</span> params = [
        <span class="hljs-string">"stash"</span>
      ];
      <span class="hljs-keyword">if</span> (options.stashPop) &#123;
        params.push(<span class="hljs-string">'pop'</span>);
      &#125;
      <span class="hljs-keyword">return</span> Core.exec<<span class="hljs-built_in">string</span>>(params, options);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">本地构建</h3>
<p>继续分析下本地构建的基本流程</p>
<p>大致分以下几步</p>
<ul>
<li>自动生成版本号
<ul>
<li>得到当前 AppID 在微信模板库中版本号情况</li>
</ul>
</li>
<li>注入需要发布的小程序 AppID
<ul>
<li>需要修改 src/manifest.json 文件中 AppID，方便开发工具上传使用</li>
</ul>
</li>
<li>运行 uni-app 构建命令
<ul>
<li>run uniapp 命令</li>
</ul>
</li>
<li>撤销发布时候的临时文件修改
<ul>
<li>撤销文件修改</li>
</ul>
</li>
</ul>
<p>能力上来说有那么几个</p>
<ol>
<li>微信 api 调用</li>
<li>文件读取和修改能力</li>
<li>Shell 命令执行能力</li>
<li>撤销文件修改能力</li>
</ol>
<p>首先怎么调用微信的 api，由于那时候我们亲爱的后端同学啃次啃次的已经吧微信 token 鉴权的能力已经做掉了，所以我们直接接后端的微信鉴权能力就可以了。但是怎么接又是个问题，虽然人家已经有个 restful 接口可以用，但是接口都要登录的啊，让人家为了我这个小小的需求弄个匿名的不大现实也不安全，想来想去那就不要用 restful 了，直接调他后面提供的 Dobbo 服务好了，完美。</p>
<h4 data-id="heading-11">获取微信 accessToken</h4>
<p>在获取微信 api 调用前我们需要先得到 accessToken。</p>
<p>所以我们会先用一个公共方法先去获取当前 accessToken， 然后在去请求微信开发平台 api。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// miniProgramService.ts 部分代码  </span>
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">async</span> retrieveWxToken(): <span class="hljs-built_in">Promise</span><<span class="hljs-built_in">string</span>> &#123;
    <span class="hljs-keyword">if</span> (!Launcher.dobboService.dubbo.mp) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"dubbo初始化错误"</span>);
    &#125;
    <span class="hljs-keyword">const</span> &#123;
      <span class="hljs-attr">success</span>: dobboSuccess,
      error,
      <span class="hljs-attr">result</span>: wxToken,
    &#125; = <span class="hljs-keyword">await</span> Launcher.dobboService.dubbo.mp.getComponentToken();

    <span class="hljs-keyword">if</span> (!dobboSuccess) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`dubbo调用失败:<span class="hljs-subst">$&#123;error&#125;</span>`</span>);
    &#125;

    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"wxToken:"</span>, wxToken);
    <span class="hljs-keyword">return</span> wxToken;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果你们的后端没有支持微信开发平台的鉴权能力的话就需要自己用 nodejs 方式去实现了，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fminiprogram%2Fdev%2Fapi-backend%2Fopen-api%2Faccess-token%2Fauth.getAccessToken.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/access-token/auth.getAccessToken.html" ref="nofollow noopener noreferrer">具体的微信开放平台文案请移步</a></p>
</blockquote>
<h4 data-id="heading-12">微信开放平台 api 调用</h4>
<p>其实微信开放平台 api 调用就是正常的 http 调用即可。</p>
<p>微信提供了一系列方法，对于我们这次的场景来说有如下接口</p>
<ul>
<li>
<p>getTemplateList 获取模板列表</p>
<ul>
<li>
<pre><code class="hljs language-text copyable" lang="text">POST https://api.weixin.qq.com/wxa/gettemplatelist?access_token==ACCESS_TOKEN
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>addtotemplate 移动草稿到模板库</p>
<ul>
<li>
<pre><code class="copyable">POST https://api.weixin.qq.com/wxa/gettemplatelist?access_token=ACCESS_TOKEN
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>deleteTemplate 删除指定模板</p>
<ul>
<li>
<pre><code class="copyable">POST https://api.weixin.qq.com/wxa/deletetemplate?access_token=ACCESS_TOKEN
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>getTemplateDraftList 获取草稿箱列表</p>
<ul>
<li>
<pre><code class="copyable">https://api.weixin.qq.com/wxa/gettemplatedraftlist?access_token=ACCESS_TOKEN
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fminiprogram%2Fdev%2Fapi-backend%2Fopen-api%2Ftemplate-message%2FtemplateMessage.addTemplate.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/template-message/templateMessage.addTemplate.html" ref="nofollow noopener noreferrer">具体的微信开放平台文案请移步</a></p>
<p>版本号的自动生成主要是通过在你点击发布时候通过让用户选择发布的版本为“大版本”，“功能迭代”还是“补丁修复”，在结合这里提到的获取当前模板列表并用 AppID 找到当前最近的版本号再做自动计算累加的方式得到这次发布的版本号。</p>
<h4 data-id="heading-13">构建小程序</h4>
<p>构建小程序这边就直接沿用 uni-app 的能力直接做构建。封装了如下方法去构建小程序</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//miniProgramService.ts 部分代码</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">async</span> buildMPForLocal(env: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">Promise</span><<span class="hljs-built_in">string</span>> &#123;
    <span class="hljs-keyword">let</span> buildEnv;
    <span class="hljs-keyword">switch</span> (env.toUpperCase()) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"PROD"</span>:
        buildEnv = EnvEnum.prod;
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"STAGING"</span>:
        buildEnv = EnvEnum.staging;
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"TEST"</span>:
        buildEnv = EnvEnum.test;
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">default</span>:
        buildEnv = EnvEnum.dev;
        <span class="hljs-keyword">break</span>;
    &#125;

    <span class="hljs-keyword">const</span> args = <span class="hljs-string">`./node_modules/.bin/cross-env NODE_ENV=production DEPLOY_ENV=<span class="hljs-subst">$&#123;buildEnv&#125;</span> UNI_PLATFORM=mp-weixin ./node_modules/.bin/vue-cli-service uni-build`</span>.split(<span class="hljs-string">' '</span>);
    <span class="hljs-comment">//正常需要这样传入 shell 参数才行</span>
    <span class="hljs-comment">//[</span>
    <span class="hljs-comment">// 'NODE_ENV=production',</span>
    <span class="hljs-comment">// 'DEPLOY_ENV=staging',</span>
    <span class="hljs-comment">// 'UNI_PLATFORM=mp-weixin',</span>
    <span class="hljs-comment">// './node_modules/.bin/vue-cli-service',</span>
    <span class="hljs-comment">// 'uni-build'</span>
    <span class="hljs-comment">//]</span>

    <span class="hljs-keyword">const</span> options: MPExecOptions = &#123;
      <span class="hljs-attr">execFileNameOrPath</span>: <span class="hljs-string">'node'</span>,
      <span class="hljs-attr">cwd</span>: getWorkspacePath()
    &#125;;

    <span class="hljs-keyword">return</span> Shell.exec(args, options);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>其余的功能</p>
<ul>
<li>剩余文件读取就正常使用 fs 库的 readFileSync 方法去读取和修改</li>
<li>撤销修改文件则是通过调用 Git 的 checkout 命令的能力去做，也是要使用上一章节的 Git 的基本能力调用</li>
</ul>
</blockquote>
<h3 data-id="heading-14">部署小程序</h3>
<p>我们 build 完成了，怎么上传呢？微信小程序这块还是需要借助微信开发工具的能力来上传</p>
<h4 data-id="heading-15">微信开发工具上传</h4>
<p>首选我们要先<strong>检查开发者工具设置：需要在开发者工具的设置 -> 安全设置中开启服务端口</strong>。这样我们才能直接唤起开发者然后做些我们要做的事情。</p>
<p>再者我们需要知道微信开发者工具的执行文件地址。正常来说 Mac 地址</p>
<blockquote>
<p><strong>/Applications/wechatwebdevtools.app/Contents/MacOS/cli</strong></p>
</blockquote>
<p>最后通过我们以前提供的 Shell 命令能力去执行就搞定了。是不是很简单。我们也封装了miniProgram.ts 来做这个事情</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// miniProgram.ts 核心代码</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">namespace</span> Cmd &#123;
    <span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">uploadMP</span>(<span class="hljs-params">options: MiniProgramExecOptions</span>) </span>&#123;
      <span class="hljs-keyword">const</span> args = [
        <span class="hljs-string">'upload'</span>,
        <span class="hljs-string">'--project'</span>,
        options.projectPath,
        <span class="hljs-string">'-v'</span>,
        options.userVersion,
        <span class="hljs-string">'-d'</span>,
        options.userDesc,
      ];
      <span class="hljs-keyword">return</span> Core.exec<<span class="hljs-built_in">string</span>>(args, options);
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>其余的功能</p>
<ul>
<li>移动到模板库和部署预览版直接调用微信开放平台 api 即可</li>
</ul>
</blockquote>
<p><strong>效果预览图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ec1b2d1a55d4c1eb76da15def0bc044~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">尾声</h2>
<p>至此整个小程序部署的在 Vscode 插件中实现的几个关键的技术点已经逐一做了简要的说明，大家会不会觉得其实看下来不难，就是涉及的东西会比较多。其实还有其他的诸如整个构建流程步骤如何可视化，Vscode 插件里面的一些基础的能力等等在本文都没有详细提及。欢迎大家留言或者提问把自己想要知道的问题反馈给我们，也方便我们可以针对大家的问题再去做一篇更棒的关于 Vscode 插件开发的文章。</p>
<p>其实 Vscode 插件在整个开发提效场景中只是当中的一个环节，我们会以敦煌工作台为核心底座搭配 Chrome 插件，Vscode 插件，zoo-cli 形成一个开发提效的百宝箱。Vscode 插件更多的是想给开发者们带来<strong>沉浸式开发</strong>的体验。</p>
<p>最后送上我自己的座右铭- <strong>“懒”是人类进步的阶梯</strong>。为了更“懒”，我们不断的前进和探索。</p>
<h2 data-id="heading-17">推荐阅读</h2>
<p><a href="https://juejin.cn/post/6997536906967777316" target="_blank" title="https://juejin.cn/post/6997536906967777316">你需要知道的项目管理知识</a></p>
<p><a href="https://juejin.cn/post/6984547134062198791" target="_blank" title="https://juejin.cn/post/6984547134062198791">最熟悉的陌生人rc-form</a></p>
<p><a href="https://juejin.cn/post/6987140782595506189" target="_blank" title="https://juejin.cn/post/6987140782595506189">如何搭建适合自己团队的构建部署平台</a></p>
<p><a href="https://juejin.cn/post/6961201207964598286" target="_blank" title="https://juejin.cn/post/6961201207964598286">聊聊Deno的那些事</a></p>
<h2 data-id="heading-18">开源作品</h2>
<ul>
<li>政采云前端小报</li>
</ul>
<p><strong>开源地址 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zoo.team%2Fopenweekly%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zoo.team/openweekly/" ref="nofollow noopener noreferrer">www.zoo.team/openweekly/</a></strong> (小报官网首页有微信交流群)</p>
<h2 data-id="heading-19">招贤纳士</h2>
<p>政采云前端团队（ZooTeam），一个年轻富有激情和创造力的前端团队，隶属于政采云产品研发部，Base 在风景如画的杭州。团队现有 50 余个前端小伙伴，平均年龄 27 岁，近 3 成是全栈工程师，妥妥的青年风暴团。成员构成既有来自于阿里、网易的“老”兵，也有浙大、中科大、杭电等校的应届新人。团队在日常的业务对接之外，还在物料体系、工程平台、搭建平台、性能体验、云端应用、数据分析及可视化等方向进行技术探索和实战，推动并落地了一系列的内部技术产品，持续探索前端技术体系的新边界。</p>
<p>如果你想改变一直被事折腾，希望开始能折腾事；如果你想改变一直被告诫需要多些想法，却无从破局；如果你想改变你有能力去做成那个结果，却不需要你；如果你想改变你想做成的事需要一个团队去支撑，但没你带人的位置；如果你想改变既定的节奏，将会是“5 年工作时间 3 年工作经验”；如果你想改变本来悟性不错，但总是有那一层窗户纸的模糊… 如果你相信相信的力量，相信平凡人能成就非凡事，相信能遇到更好的自己。如果你希望参与到随着业务腾飞的过程，亲手推动一个有着深入的业务理解、完善的技术体系、技术创造价值、影响力外溢的前端团队的成长历程，我觉得我们该聊聊。任何时间，等着你写点什么，发给 <code>ZooTeam@cai-inc.com</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d3aa3d1f8646a8bcda8cfd9e335a4b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            