
---
title: 'process常用api整理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8111'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 04:58:34 GMT
thumbnail: 'https://picsum.photos/400/300?random=8111'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>process是一个全局的变量，所以使用的时候是不需要执行require操作，可以直接使用。</p>
<p>这里分两部分来说明，第一个就是可以借助它去获取进程信息，比如进程工作的时候本地是一个什么样的环境，通过process可以获取。第二个通过process可以对当前的进程做一些操作，比如说可以监听进程执行过程中内置的事件，创建子进程完成更多的操作。</p>
<p>process在node开发中是一个重要的全局变量。</p>
<p>内存相关获取</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 查看内存消耗</span>
<span class="hljs-built_in">console</span>.log(process.memoryUsage());
<span class="hljs-comment">/**
* rss： 常驻内存
* heapToal: 总内存大小
* heapUsed: 已使用内存
* external: 扩展内存 - 底层模块占用的C/C++核心模块
* arrayBuffers: 缓冲区大小
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CPU相关信息获取</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(process.cpuUsage());
<span class="hljs-comment">/**
* user: 用户占用的时间片段
* system: 系统占用的时间片段
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行时可以通过process查看运行目录，node环境，cpu架构，用户环境，系统平台。</p>
<pre><code class="hljs language-js copyable" lang="js">process.cwd(); <span class="hljs-comment">// 运行目录</span>
process.version; <span class="hljs-comment">// node版本</span>
process.versions; <span class="hljs-comment">// 运行环境版本</span>
process.arch; <span class="hljs-comment">// cpu架构</span>
process.env.NODE_ENV; <span class="hljs-comment">// 环境 需要先设置</span>
process.env.PATH; <span class="hljs-comment">// 环境变量</span>
process.env.USERPROFILE; <span class="hljs-comment">// 管理员目录路径 不同环境方式不一样 process.env.HOME</span>
process.platform; <span class="hljs-comment">// 平台 win32 macos</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行时可以获取启动参数，PID，运行时间，</p>
<pre><code class="hljs language-js copyable" lang="js">process.argv; <span class="hljs-comment">// 获取运行参数，空格分隔可在数组中获取到，默认会存在node目录和执行脚本的目录两个值。</span>
process.argv0; <span class="hljs-comment">// 获取第一个值, 只有这一个api</span>
process.pid; <span class="hljs-comment">// 获取运行的pid</span>
process.ppid; 
process.uptime; <span class="hljs-comment">// 脚本运行时间</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>事件监听在process中提供的内容。这里不会着重说明process里面到底有哪些事件，主要还是看一看在nodejs里面熟悉一下事件驱动编程以及发布订阅的模式。</p>
<p>process是实现了emit接口的。可以使用on监听事件，内部提供了很多的事件，比如exit，程序退出的时候执行。这里绑定的事件只能执行同步代码，是不可以执行异步代码的，这里要注意。</p>
<pre><code class="hljs language-js copyable" lang="js">process.on(<span class="hljs-string">'exit'</span>, <span class="hljs-function">(<span class="hljs-params">code</span>) =></span> &#123; <span class="hljs-comment">// 退出时</span>
    <span class="hljs-built_in">console</span>.log(code); <span class="hljs-comment">// 0</span>
&#125;)

process.on(<span class="hljs-string">'beforeExit'</span>, <span class="hljs-function">(<span class="hljs-params">code</span>) =></span> &#123; <span class="hljs-comment">// 退出之前</span>
    <span class="hljs-built_in">console</span>.log(code); <span class="hljs-comment">// 0</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>手动退出，这种退出不会执行beforeExit，而且exit后面的代码也不会执行，因为执行exit就已经退出了。</p>
<pre><code class="hljs language-js copyable" lang="js">process.exit();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>标准输出，输入，错误</p>
<pre><code class="hljs language-js copyable" lang="js">process.stdout; <span class="hljs-comment">// 是一个流，可以对他进行读写操作。</span>

process.stdout.write(<span class="hljs-string">'123'</span>); <span class="hljs-comment">// 123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);

fs.createReadStream(<span class="hljs-string">'text.txt'</span>).pipi(process.stdout); <span class="hljs-comment">// 读取文件输出。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">process.stdin; <span class="hljs-comment">// 可以拿到控制台输入的内容</span>
process.stdin.pipe(process.stdout); <span class="hljs-comment">// 输入之后输出</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 设置字符编码</span>
process.stdin.setEncoding(<span class="hljs-string">'utf-8'</span>);
<span class="hljs-comment">// 监听readable事件，是否可读也就是有无内容</span>
process.stdin.on(<span class="hljs-string">'readable'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 获取输入的内容</span>
    <span class="hljs-keyword">let</span> chunk = process.stdin.read();
    <span class="hljs-keyword">if</span> (chunk !== <span class="hljs-literal">null</span>) &#123;
        process.stdout.write(chunk);
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            