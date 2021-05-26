
---
title: '【Clickhouse源码】（系列一）启动过程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17290de5d0aa4c40bd14854493128e82~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 25 May 2021 03:27:16 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17290de5d0aa4c40bd14854493128e82~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近学习ClickHouse相关的原理知识，基本了解了它的存储结构和设计，但是对在ClickHouse中执行一个SQL语句的过程不是很了解，所以就再次学习了一下。在这里做个总结。</p>
<p>准备出一个系列文章，通过源码阅读的方式，来逐步拆解<code>Clickhouse</code>的运行过程。今天，我们来看看<code>Clickhouse</code>是如何启动的。</p>
<h1 data-id="heading-0"><a href="https://pocoproject.org/slides/000-IntroAndOverview.pdf" target="_blank" rel="nofollow noopener noreferrer">Poco框架简介</a></h1>
<p>首先，大家需要知道一个名词：<code>Poco</code>。<a href="https://github.com/pocoproject/poco" target="_blank" rel="nofollow noopener noreferrer">Github</a> 这是<code>Clickhouse</code>选择的跨端网络编程框架。这里简单贴官方pdf中的几张图来介绍一下。</p>
<p>这是<code>Poco</code>的整体架构：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17290de5d0aa4c40bd14854493128e82~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>官方做的介绍：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cbed05d6ba54430b1df2ed8d6b81841~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>支持的平台：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6259b6f0cf7c4ea49ea88f55da5935f8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Server应用相关介绍：<a href="https://pocoproject.org/slides/190-Applications.pdf" target="_blank" rel="nofollow noopener noreferrer">阅读原文</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/955b9fac543b410ca7ee74b6ded9f528~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">入口</h1>
<p>大家都知道，在启动<code>Clickhouse</code>的时候，我们会执行<code>clickhouse-server ...</code>或<code>clickhouse server ...</code>或<code>clickhouse --server ...</code>命令。那么，执行后<code>Clickhouse</code>做了哪些事情呢？</p>
<p>首先我们需要找到入口。在最新的v18.14版本以后，<code>Clickhouse</code>的入口文件调整到<code>programs/main.cpp</code>，该文件为clickhouse入口文件：</p>
<p>我们直接来看看<code>main</code>函数的代码：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">(<span class="hljs-keyword">int</span> argc_, <span class="hljs-keyword">char</span> ** argv_)</span>
</span>&#123;
    inside_main = <span class="hljs-literal">true</span>;
    <span class="hljs-built_in">SCOPE_EXIT</span>(&#123; inside_main = <span class="hljs-literal">false</span>; &#125;);

    <span class="hljs-comment">/// Reset new handler to default (that throws std::bad_alloc)</span>
    <span class="hljs-comment">/// It is needed because LLVM library clobbers it.</span>
    std::<span class="hljs-built_in">set_new_handler</span>(<span class="hljs-literal">nullptr</span>);

    <span class="hljs-comment">/// PHDR cache is required for query profiler to work reliably</span>
    <span class="hljs-comment">/// It also speed up exception handling, but exceptions from dynamically loaded libraries (dlopen)</span>
    <span class="hljs-comment">///  will work only after additional call of this function.</span>
    <span class="hljs-built_in">updatePHDRCache</span>(); <span class="hljs-comment">// 共享库缓存</span>

    <span class="hljs-function">std::vector<<span class="hljs-keyword">char</span> *> <span class="hljs-title">argv</span><span class="hljs-params">(argv_, argv_ + argc_)</span></span>;

    <span class="hljs-comment">/// Print a basic help if nothing was matched</span>
    MainFunc main_func = printHelp;  <span class="hljs-comment">// 默认执行help函数</span>

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">auto</span> & application : clickhouse_applications)
    &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">isClickhouseApp</span>(application.first, argv)) <span class="hljs-comment">// 这里判断是不是clickhouse-xx </span>
                                                      <span class="hljs-comment">// 或 clickhous e --xx </span>
                                                      <span class="hljs-comment">// 或 clickhouse xx  命令</span>
                                                      <span class="hljs-comment">// 支持的命令看后面的说明</span>
        &#123;
            main_func = application.second; <span class="hljs-comment">// 当匹配到指定的命令后退出循环</span>
            <span class="hljs-keyword">break</span>;
        &#125;
    &#125;

    <span class="hljs-keyword">return</span> <span class="hljs-built_in">main_func</span>(<span class="hljs-keyword">static_cast</span><<span class="hljs-keyword">int</span>>(argv.<span class="hljs-built_in">size</span>()), argv.<span class="hljs-built_in">data</span>()); <span class="hljs-comment">// 执行响应的函数</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，<code>main</code>函数实际上是从<code>clickhouse_applications</code>中匹配指令，然后执行了响应的指令函数。</p>
<p>顺便看一下<code>clickhouse</code>支持的命令：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a00b406e976b47aaaa03b0336148e140~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>指令的声明源码如下：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-comment">/// Add an item here to register new application</span>
std::pair<<span class="hljs-keyword">const</span> <span class="hljs-keyword">char</span> *, MainFunc> clickhouse_applications[] =
&#123;
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> ENABLE_CLICKHOUSE_LOCAL</span>
    &#123;<span class="hljs-string">"local"</span>, mainEntryClickHouseLocal&#125;,  <span class="hljs-comment">// 启动本地服务</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> ENABLE_CLICKHOUSE_CLIENT</span>
    &#123;<span class="hljs-string">"client"</span>, mainEntryClickHouseClient&#125;, <span class="hljs-comment">// 启动clickhouse的内置客户端</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> ENABLE_CLICKHOUSE_BENCHMARK</span>
    &#123;<span class="hljs-string">"benchmark"</span>, mainEntryClickHouseBenchmark&#125;, 
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> ENABLE_CLICKHOUSE_SERVER</span>
    &#123;<span class="hljs-string">"server"</span>, mainEntryClickHouseServer&#125;, <span class="hljs-comment">// 启动clickhouse服务端</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> ENABLE_CLICKHOUSE_EXTRACT_FROM_CONFIG</span>
    &#123;<span class="hljs-string">"extract-from-config"</span>, mainEntryClickHouseExtractFromConfig&#125;,
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> ENABLE_CLICKHOUSE_COMPRESSOR</span>
    &#123;<span class="hljs-string">"compressor"</span>, mainEntryClickHouseCompressor&#125;,
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> ENABLE_CLICKHOUSE_FORMAT</span>
    &#123;<span class="hljs-string">"format"</span>, mainEntryClickHouseFormat&#125;,
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> ENABLE_CLICKHOUSE_COPIER</span>
    &#123;<span class="hljs-string">"copier"</span>, mainEntryClickHouseClusterCopier&#125;,
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> ENABLE_CLICKHOUSE_OBFUSCATOR</span>
    &#123;<span class="hljs-string">"obfuscator"</span>, mainEntryClickHouseObfuscator&#125;,
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> ENABLE_CLICKHOUSE_GIT_IMPORT</span>
    &#123;<span class="hljs-string">"git-import"</span>, mainEntryClickHouseGitImport&#125;,
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> ENABLE_CLICKHOUSE_INSTALL  <span class="hljs-comment">// clickhouse部署命令</span></span>
    &#123;<span class="hljs-string">"install"</span>, mainEntryClickHouseInstall&#125;,
    &#123;<span class="hljs-string">"start"</span>, mainEntryClickHouseStart&#125;,
    &#123;<span class="hljs-string">"stop"</span>, mainEntryClickHouseStop&#125;,
    &#123;<span class="hljs-string">"status"</span>, mainEntryClickHouseStatus&#125;,
    &#123;<span class="hljs-string">"restart"</span>, mainEntryClickHouseRestart&#125;,
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
    &#123;<span class="hljs-string">"hash-binary"</span>, mainEntryClickHouseHashBinary&#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，我们在执行<code>clickhouse-server ...</code>命令时，实际上运行了<code>mainEntryClickHouseServer</code>函数。接下来我们看看这个函数做了什么。</p>
<h1 data-id="heading-2">启动服务 Server</h1>
<p>我们从<code>main.cpp</code>中找到<code>mainEntryClickHouseServer</code>，该函数来自于<code>programs/server/Server.cpp</code>文件：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">mainEntryClickHouseServer</span><span class="hljs-params">(<span class="hljs-keyword">int</span> argc, <span class="hljs-keyword">char</span> ** argv)</span>
</span>&#123;
    DB::Server app;

    <span class="hljs-comment">// ...</span>

    <span class="hljs-keyword">try</span>
    &#123;
        <span class="hljs-keyword">return</span> app.<span class="hljs-built_in">run</span>(argc, argv); # 调用Pococ的run函数启动Server服务
    &#125;
    <span class="hljs-built_in"><span class="hljs-keyword">catch</span></span> (...)
    &#123;
        std::cerr << DB::<span class="hljs-built_in">getCurrentExceptionMessage</span>(<span class="hljs-literal">true</span>) << <span class="hljs-string">"\n"</span>;
        <span class="hljs-keyword">auto</span> code = DB::<span class="hljs-built_in">getCurrentExceptionCode</span>();
        <span class="hljs-keyword">return</span> code ? code : <span class="hljs-number">1</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，<code>Server</code>的启动最终是交给了<code>Poco</code>框架来完成的。那么我们是否到这里就结束了呢？让我们来看一下<code>Poco::Util::ServerApplication:run(int argc, char * * argv)</code>函数做了什么。这里我们找到<code>Poco</code>的<code>Poco/Util/src/ServerApplication.h</code>源码，可以很清楚的看到一段说明：</p>
<pre><code class="hljs language-c++ copyable" lang="c++">&#123;
<span class="hljs-keyword">public</span>:
<span class="hljs-built_in">ServerApplication</span>();
<span class="hljs-comment">/// Creates the ServerApplication.</span>

~<span class="hljs-built_in">ServerApplication</span>();
<span class="hljs-comment">/// Destroys the ServerApplication.</span>
                
        <span class="hljs-comment">// 就是这里：run方法执行的时候会调用当前Application类的main函数</span>
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">run</span><span class="hljs-params">(<span class="hljs-keyword">int</span> argc, <span class="hljs-keyword">char</span>** argv)</span></span>;
<span class="hljs-comment">/// Runs the application by performing additional initializations</span>
<span class="hljs-comment">/// and calling the main() method.</span>
                
        
        <span class="hljs-comment">// ...</span>
<span class="hljs-keyword">protected</span>:
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">run</span><span class="hljs-params">()</span></span>;
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">waitForTerminationRequest</span><span class="hljs-params">()</span></span>;
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> !defined(_WIN32_WCE)</span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">defineOptions</span><span class="hljs-params">(OptionSet& options)</span></span>;
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们再打开<code>Poco/Util/src/ServerApplication.cpp</code>看一下<code>run</code>函数的代码：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">ServerApplication::run</span><span class="hljs-params">(<span class="hljs-keyword">int</span> argc, <span class="hljs-keyword">char</span>** argv)</span>
</span>&#123;
<span class="hljs-keyword">if</span> (!<span class="hljs-built_in">hasConsole</span>() && <span class="hljs-built_in">isService</span>())
&#123;
<span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;
<span class="hljs-keyword">else</span>
&#123;
<span class="hljs-keyword">int</span> rc = EXIT_OK;
<span class="hljs-keyword">try</span>
&#123;
<span class="hljs-built_in">init</span>(argc, argv);
<span class="hljs-built_in"><span class="hljs-keyword">switch</span></span> (_action)
&#123;
<span class="hljs-keyword">case</span> SRV_REGISTER:
<span class="hljs-built_in">registerService</span>();
rc = EXIT_OK;
<span class="hljs-keyword">break</span>;
<span class="hljs-keyword">case</span> SRV_UNREGISTER:
<span class="hljs-built_in">unregisterService</span>();
rc = EXIT_OK;
<span class="hljs-keyword">break</span>;
<span class="hljs-keyword">default</span>:
rc = <span class="hljs-built_in">run</span>(); <span class="hljs-comment">// 这里会调用当前类的run()函数</span>
&#125;
&#125;
<span class="hljs-built_in"><span class="hljs-keyword">catch</span></span> (Exception& exc)
&#123;
<span class="hljs-built_in">logger</span>().<span class="hljs-built_in">log</span>(exc);
rc = EXIT_SOFTWARE;
&#125;
<span class="hljs-keyword">return</span> rc;
&#125;
&#125;

<span class="hljs-comment">//...</span>

<span class="hljs-comment">// run函数会直接调用Application的run方法</span>
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">ServerApplication::run</span><span class="hljs-params">()</span>
</span>&#123;
<span class="hljs-keyword">return</span> Application::<span class="hljs-built_in">run</span>();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么我们来打开<code>Poco/Util/src/Application.cpp</code>看一下<code>Application::run()</code>函数：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">Application::run</span><span class="hljs-params">()</span>
</span>&#123;
<span class="hljs-keyword">int</span> rc = EXIT_CONFIG;
<span class="hljs-built_in">initialize</span>(*<span class="hljs-keyword">this</span>);  <span class="hljs-comment">// 先调用initialize钩子</span>

<span class="hljs-keyword">try</span>
&#123;
rc = EXIT_SOFTWARE;
rc = <span class="hljs-built_in">main</span>(_unprocessedArgs); <span class="hljs-comment">// 然后这里会调用main函数</span>
&#125;
<span class="hljs-built_in"><span class="hljs-keyword">catch</span></span> (Poco::Exception& exc)
&#123;
<span class="hljs-built_in">logger</span>().<span class="hljs-built_in">log</span>(exc);
&#125;
<span class="hljs-comment">//...</span>
        
<span class="hljs-built_in">uninitialize</span>(); <span class="hljs-comment">// 最后调用uninitialize钩子</span>
<span class="hljs-keyword">return</span> rc;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>兜兜转转我们又要回到<code>Clickhouse</code>的<code>programs/server/Server.cpp</code>，我们直接看<code>Server::main()</code>函数吧，这个函数有点长。。。大致做了以下这些事吧。</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">Server::main</span><span class="hljs-params">(<span class="hljs-keyword">const</span> std::vector<std::string> & <span class="hljs-comment">/*args*/</span>)</span>
</span>&#123;
    Poco::Logger * log = &<span class="hljs-built_in">logger</span>();
    <span class="hljs-comment">// 1. RegisterXXX 注册一些基础的函数等</span>
    
    <span class="hljs-comment">// 2. 创建GlobalThreadPool</span>
    
    <span class="hljs-comment">// 3. 初始化全局上下文以及内容（配置等）</span>
    
    <span class="hljs-comment">// 4. 创建系统数据库(system、default等)、初始化内置表</span>
    
    <span class="hljs-comment">// 5. 注册不同协议的服务（http/https/tcp等）</span>
    
    <span class="hljs-comment">// 6. 启动所有服务（Poco::Net::TCPServer.start()）</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">auto</span> & server : *servers)
            server.<span class="hljs-built_in">start</span>();
    
    <span class="hljs-comment">// 最后等待结束</span>
    <span class="hljs-built_in">waitForTerminationRequest</span>();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里面创建http服务的关键代码为：</p>
<pre><code class="hljs language-c++ copyable" lang="c++">servers-><span class="hljs-built_in">emplace_back</span>(
                    port_name,
                    std::make_unique<HTTPServer>(
                        <span class="hljs-built_in">context</span>(), <span class="hljs-built_in">createHandlerFactory</span>(*<span class="hljs-keyword">this</span>, async_metrics, <span class="hljs-string">"HTTPHandler-factory"</span>), server_pool, socket, http_params));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到<code>servers</code>中添加了<code>HTTPServer</code>对象，这个<code>HTTPServer</code>对象是继承了<code>Poco::Net::TCPServer</code>的，所以实际上就是在<code>servers</code>向量表中加了一个<code>TCPServer</code>对象，等待后续的启动。</p>
<p>这里再进入到<code>createHandlerFactory</code>中看一下，发现会调用<code>Server/HTTPHandlerFactory.cpp</code>中的<code>addDefaultHandlersFactory</code>添加默认的一些处理器:</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">addDefaultHandlersFactory</span><span class="hljs-params">(HTTPRequestHandlerFactoryMain & factory, IServer & server, AsynchronousMetrics & async_metrics)</span>
</span>&#123;
    <span class="hljs-comment">// 1. 添加默认的处理器：</span>
    <span class="hljs-comment">//    a. / -> 静态资源。如.js\.css等</span>
    <span class="hljs-comment">//    b. /ping -> 处理ping消息</span>
    <span class="hljs-comment">//    c. /replicas_status -> 处理集群状态查询指令</span>
    <span class="hljs-comment">//    d. /play -> 内置的查询ui页面</span>
    <span class="hljs-built_in">addCommonDefaultHandlersFactory</span>(factory, server);

    <span class="hljs-keyword">auto</span> query_handler = std::make_shared<HandlingRuleHTTPHandlerFactory<DynamicQueryHandler>>(server, <span class="hljs-string">"query"</span>);
    query_handler-><span class="hljs-built_in">allowPostAndGetParamsRequest</span>();
    factory.<span class="hljs-built_in">addHandler</span>(query_handler);

    <span class="hljs-comment">/// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>题外话：贴一下<code>Clickhouse</code>内置的web客户端，丑归丑，估计大多数开发者都不知道这个地址：<code>http://192.168.1.xx:8123/play.html</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e6495aebadf4cebbc99bd559633ca58~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">总结</h1>
<p>到此，我们知道了整个<code>Clickhouse</code>的启动过程。最终通过<code>Poco</code>框架启动了一些个<code>TCPServer</code>服务来监听客户端连接和消息。后续文章会源码分析<code>Clickhouse</code>处理客户端的请求过程。后期有时间我也会跟大家唠唠<code>Poco</code>框架的基础和源码。咱们下期见~</p></div>  
</div>
            