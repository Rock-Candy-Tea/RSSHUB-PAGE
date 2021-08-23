
---
title: '获取 NodeJS 程序退出码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=619'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 05:33:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=619'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第23天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>想要退出正在运行的 NodeJS 程序，我们既可以通过 <code>Ctrl + C </code>  的方式，也可以通过<code> process.exit()</code>来执行退出。</p>
<p>这两种操作都将强制进程尽快退出，即使仍有未完全完成的异步操作挂起，包括对 <code>process.stdout</code> 和 <code>process.stderr</code> 的 I/O 操作。</p>
<p>如果由于错误情况需要终止 Node.js 进程，则抛出未捕获的错误并允许进程相应地终止比调用 <code>process.exit()</code> 更安全，比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> process <span class="hljs-keyword">from</span> <span class="hljs-string">'process'</span>;

<span class="hljs-comment">// 如何正确设置退出码，同时让进程正常退出。</span>
<span class="hljs-keyword">if</span> (someConditionNotMet()) &#123;
  printUsageToStdout();
  process.exitCode = <span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>Worker</code> 线程中，该函数停止当前线程而不是当前进程。</p>
<p>那么对于一些意外退出的 NodeJS 程序，如何来获取 exitCode ？每一个退出码又代表什么？今天我们就来学习一下。</p>
<h2 data-id="heading-1">通过 NodeJS 的 child_process 子进程获取退出码</h2>
<p>child_process.fork() 方法是 child_process.spawn() 的特例，专门用于衍生新的 NodeJS 进程。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fork = <span class="hljs-built_in">require</span>(<span class="hljs-string">"child_process"</span>).fork;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"main "</span>, process.argv);

<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

<span class="hljs-keyword">const</span> fd = fs.openSync(<span class="hljs-string">"./a.log"</span>, <span class="hljs-string">"a"</span>);

<span class="hljs-keyword">const</span> child = fork(<span class="hljs-string">"./index.js"</span>, &#123;
    <span class="hljs-attr">stdio</span>: [<span class="hljs-string">"ipc"</span>, <span class="hljs-string">"pipe"</span>, fd]
&#125;);

child.on(<span class="hljs-string">"error"</span>, <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> info = <span class="hljs-string">`child process error <span class="hljs-subst">$&#123;error&#125;</span>`</span>;
    fs.writeSync(fd, info);
    <span class="hljs-built_in">console</span>.log(info);
&#125;);

child.on(<span class="hljs-string">"exit"</span>, <span class="hljs-function">(<span class="hljs-params">code</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> info = <span class="hljs-string">`child process exited with code <span class="hljs-subst">$&#123;code&#125;</span>`</span>;
    fs.writeSync(fd, info);
    <span class="hljs-built_in">console</span>.log(info);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>子程序执行参数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fork = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>).fork;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'main '</span>,process.argv);

<span class="hljs-keyword">const</span> fs=<span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);

<span class="hljs-keyword">const</span> fd = fs.openSync(<span class="hljs-string">'./a.log'</span>,<span class="hljs-string">'a'</span>);

<span class="hljs-comment">// 子程序参数</span>
<span class="hljs-keyword">let</span> args = [];
args[<span class="hljs-number">0</span>] = <span class="hljs-string">'test'</span>;

<span class="hljs-keyword">const</span> child = fork(<span class="hljs-string">'./index.js'</span>,args,&#123;
    <span class="hljs-attr">stdio</span>:[<span class="hljs-string">'ipc'</span>,<span class="hljs-string">'pipe'</span>,fd]
&#125;);

child.on(<span class="hljs-string">'error'</span>, <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> info = <span class="hljs-string">`child process error <span class="hljs-subst">$&#123;error&#125;</span>`</span>;
    fs.writeSync(fd,info);
    <span class="hljs-built_in">console</span>.log(info);
&#125;);

child.on(<span class="hljs-string">'exit'</span>, <span class="hljs-function">(<span class="hljs-params">code</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> info = <span class="hljs-string">`child process exited with code <span class="hljs-subst">$&#123;code&#125;</span>`</span>;
    fs.writeSync(fd,info);
    <span class="hljs-built_in">console</span>.log(info);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">NodeJS退出码</h2>
<p>当没有更多异步操作挂起时，NodeJS 通常会以 <code>0</code> 状态代码退出。 在其他情况下使用以下状态代码：</p>
<ul>
<li><code>1</code> <strong>未捕获的致命异常</strong>：存在未捕获的异常，并且其没有被域或 <code>'uncaughtException'</code> 事件句柄处理。</li>
<li><code>2</code>: 未使用（由 Bash 保留用于内置误用）</li>
<li><code>3</code> <strong>内部 JavaScript 解析错误</strong>：NodeJS 引导过程中的内部 JavaScript 源代码导致解析错误。 这是极其罕见的，通常只能在 NodeJS 本身的开发过程中发生。</li>
<li><code>4</code> <strong>内部 JavaScript 评估失败</strong>：NodeJS 引导过程中的内部 JavaScript 源代码在评估时未能返回函数值。 这是极其罕见的，通常只能在 NodeJS 本身的开发过程中发生。</li>
<li><code>5</code> <strong>致命错误</strong>：V8 中存在不可恢复的致命错误。 通常将打印带有前缀 <code>FATAL ERROR</code> 的消息到标准错误。</li>
<li><code>6</code> <strong>非函数的内部异常句柄</strong>：存在未捕获的异常，但内部致命异常句柄不知何故设置为非函数，无法调用。</li>
<li><code>7</code> <strong>内部异常句柄运行时失败</strong>：存在未捕获的异常，并且内部致命异常句柄函数本身在尝试处理时抛出错误。 例如，如果 <code>'uncaughtException'</code> 或 <code>domain.on('error')</code> 句柄抛出错误，就会发生这种情况。</li>
<li><code>8</code>: 未使用。 在以前版本的 NodeJS 中，退出码 8 有时表示未捕获的异常。</li>
<li><code>9</code> <strong>无效参数</strong>：指定了未知选项，或者提供了需要值的选项而没有值。</li>
<li><code>10</code> <strong>内部 JavaScript 运行时失败</strong>：NodeJS 引导过程中的内部 JavaScript 源代码在调用引导函数时抛出错误。 这是极其罕见的，通常只能在 NodeJS 本身的开发过程中发生。</li>
<li><code>12</code> <strong>无效的调试参数</strong>：设置了 <code>--inspect</code> 和/或 <code>--inspect-brk</code> 选项，但选择的端口号无效或不可用。</li>
<li><code>13</code> <strong>未完成的顶层等待</strong>：在顶层代码中的函数外使用了 <code>await</code>，但传入的 <code>Promise</code> 从未解决。</li>
<li><code>>128</code> <strong>信号退出</strong>：如果 NodeJS 收到致命的信号，例如 <code>SIGKILL</code> 或 <code>SIGHUP</code>，则其退出码将是 <code>128</code> 加上信号代码的值。 这是标准的 POSIX 实践，因为退出码被定义为 7 位整数，并且信号退出设置高位，然后包含信号代码的值。 例如，信号 <code>SIGABRT</code> 的值是 <code>6</code>，因此预期的退出码将是 <code>128</code> + <code>6</code> 或 <code>134</code>。</li>
</ul>
<h2 data-id="heading-3">总结</h2>
<p>以上就是获取 NodeJS 程序退出码的方法以及退出码枚举。</p>
<p>~</p>
<p>~本文完，感谢阅读！</p>
<p>~</p>
<blockquote>
<p>学习有趣的知识，结识有趣的朋友，塑造有趣的灵魂！</p>
<p>大家好，我是〖<a href="https://juejin.cn/user/2893570333750744/posts" target="_blank" title="https://juejin.cn/user/2893570333750744/posts">编程三昧</a>〗的作者 <strong>隐逸王</strong>，我的公众号是『<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fyinyiwang%2FblogImages%2Fraw%2Fmaster%2Fimages%2F20210604%2520%2F19-26-03-txvEvM.png" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/yinyiwang/blogImages/raw/master/images/20210604%20/19-26-03-txvEvM.png" ref="nofollow noopener noreferrer">编程三昧</a>』，欢迎关注，希望大家多多指教！</p>
<p>你来，怀揣期望，我有墨香相迎！ 你归，无论得失，唯以余韵相赠！</p>
<p>知识与技能并重，内力和外功兼修，理论和实践两手都要抓、两手都要硬！</p>
</blockquote></div>  
</div>
            