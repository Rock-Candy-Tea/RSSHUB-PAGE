
---
title: '学习了解PHP中的SeasLog日志扩展'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2213'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 16:49:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=2213'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第31天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>今天来学习的扩展是和日志相关的一个扩展，对于 PHP 的日志应用来说，除了本身自带的 error_log() 、 syslog() 之外，在大多数的框架中还会经常见到 monolog 的踪影。当然，我们今天讲的并不是 monolog ，而是需要自己安装的一个扩展日志组件。</p>
<h2 data-id="heading-0">关于 SeasLog</h2>
<p>首先要说明的是，SeasLog 这个扩展是我们国人开发的哦，Neeke 大佬。并且这个扩展也是收录在官方文档中的，下面是他的知乎主页的链接，大家可以去多多向大佬学习。</p>
<p>架构师 Neeke：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fpeople%2Fciogao" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/people/ciogao" ref="nofollow noopener noreferrer">www.zhihu.com/people/ciog…</a></p>
<p>对于 PHP 内置的那两个日志函数，也就是 error_log() 、 syslog() 来说，虽然功能强大并且性能极好，但是并没有错误级别的设置，也没有固定的格式，更分不了模块记录。而 monolog 、 log4php 这类的日志程序在性能上又多少略有缺憾。正因为这些各种各样的原因，Neeke 大佬就开发了这个 SeasLog 扩展，为的就是解决上面这些日志相关系统的问题。</p>
<p>因为是我们国人开发的，所以它的中文文档很友好，在 Gibhub 和官方文档中都有详细的中文文档说明，非常方便我们使用。安装过程也和普通的 PHP 扩展没有区别，并不需要什么别的特殊的软件支持。</p>
<h3 data-id="heading-1">日志记录格式</h3>
<p>我们先来了解一下 SeasLog 的日志记录格式。它的日志格式模板是在 php.ini 文件中配置的，无法动态修改，需要配置 seaslog.default_template 这个选项，默认值是 "%T | %L | %P | %Q | %t | %M" 。其中，%T 代表时间、%L 代表日志级别、%P 代表进程ID 、%Q 代表请求ID 、%t 代表时间戳、%M 代表日志信息。</p>
<p>当然，除了默认的这些参数之外 ，它还有一些别的参数，文档中说明得很详细，我们在下面的文章中也会再提到两个。具体的内容大家可以自行在官方文档中查阅，这里就不多说了。</p>
<h2 data-id="heading-2">相关属性参数设置</h2>
<p>除了一些需要在 php.ini 中配置的选项参数之外，SeasLog 还可以在程序运行时配置及获取一些配置信息。</p>
<h3 data-id="heading-3">日志根目录</h3>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-comment">// 获取设置日志根目录</span>
var_dump(SeasLog::getBasePath()); <span class="hljs-comment">// string(12) "/var/log/www"</span>
SeasLog::setBasePath(<span class="hljs-string">"./"</span>);
var_dump(SeasLog::getBasePath()); <span class="hljs-comment">// string(2) "./"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是日志所要记录到的文件目录信息，我们可以通过 getBasePath() 来获得当前配置的文件目录信息。默认情况下是 "/var/log/www" 这个目录，当然，我们也可以在 php.ini 中配置 seaslog.default_basepath 这个选项来修改这个默认的目录。而在代码中，我们可以通过 setBasePath() 函数来修改这个目录，比如我们在上面的测试代码中将日志的目录修改到当前目录下了。</p>
<h3 data-id="heading-4">Logger 信息</h3>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-comment">// 获取设置日志 Logger 名称</span>
var_dump(SeasLog::getLastLogger()); <span class="hljs-comment">// string(7) "default"</span>

SeasLog::info(<span class="hljs-string">"Test Logger Default"</span>);
<span class="hljs-comment">// ./default/20200106.log</span>
<span class="hljs-comment">// 2021-01-06 01:01:53 | INFO | 5038 | 5ff50c019ebe9 | 1609894913.650 | Test Logger Default</span>

SeasLog::setLogger(<span class="hljs-string">"mylog"</span>);
var_dump(SeasLog::getLastLogger()); <span class="hljs-comment">// string(5) "mylog"</span>

SeasLog::info(<span class="hljs-string">"Test Logger MyLog"</span>);
<span class="hljs-comment">// ./mylog/20200106.log</span>
<span class="hljs-comment">// 2021-01-06 01:01:53 | INFO | 5038 | 5ff50c019ebe9 | 1609894913.650 | Test Logger MyLog</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Logger 信息可以看做是一个日志分类，它会把这个分类下的日志放到同一个文件夹中。比如我们在默认情况这个 Logger 是 default ，如果在默认情况下直接使用 info() 记录日志的话，就会在当前日志根目录生成一个 default 目录，并且创建一个以当前日期命名的日志文件。</p>
<p>如果我们使用 setLogger() 设置了一个新的 Logger ，那么两次记录日志的时候，就会生成创建一个新的 Logger 目录并将日志记录到这个目录中。</p>
<h3 data-id="heading-5">日期格式</h3>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-comment">// 获取设置日志日期格式</span>
var_dump(SeasLog::getDatetimeFormat()); <span class="hljs-comment">// string(11) "Y-m-d H:i:s"</span>

SeasLog::info(<span class="hljs-string">"Test Datetime Default"</span>);
<span class="hljs-comment">// 2021-01-06 01:04:44 …………</span>

SeasLog::setDatetimeFormat(<span class="hljs-string">"Y/m/d His"</span>);
var_dump(SeasLog::getDatetimeFormat()); <span class="hljs-comment">// string(9) "Y/m/d His"</span>

SeasLog::info(<span class="hljs-string">"Test Datetime New"</span>);
<span class="hljs-comment">// 2021/01/06 010444 …………</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>日期格式的修改其实就是针对的我们的日志格式中的 %T 这个参数。这个就不多解释了，代码中已经演示得很清晰了，使用 getDatetimeFormat() 可以获得当前设置的日期信息，而 setDatetimeFormat() 方法则是设置日期的格式。</p>
<h3 data-id="heading-6">请求 ID</h3>
<pre><code class="hljs language-php copyable" lang="php">var_dump(SeasLog::getRequestID()); <span class="hljs-comment">// string(13) "5ff50e4721a06"</span>
SeasLog::setRequestID(<span class="hljs-string">"new_request_id"</span> . uniqid());
var_dump(SeasLog::getRequestID()); <span class="hljs-comment">// string(27) "new_request_id5ff50e6519202"</span>
SeasLog::info(<span class="hljs-string">"Test New Request ID"</span>);
<span class="hljs-comment">// 2021/01/06 011216 | INFO | 5250 | new_request_id5ff50e70337b8 | 1609895536.210 | Test New Request ID</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请求ID 针对的是 %Q 这个参数的内容。默认情况下它就是调用 uniqid() 生成的一个唯一ID数据，我们可以通过 setRequestID() 来指定当前这条日志要生成的请求ID是什么内容。</p>
<h3 data-id="heading-7">其它日志变量</h3>
<p>除了上面的这些固定功能的函数外，我们还可以设置一些别的请求参数信息。</p>
<pre><code class="hljs language-php copyable" lang="php">ar_dump(SeasLog::getRequestVariable(SEASLOG_REQUEST_VARIABLE_DOMAIN_PORT));
var_dump(SeasLog::getRequestVariable(SEASLOG_REQUEST_VARIABLE_REQUEST_URI));
var_dump(SeasLog::getRequestVariable(SEASLOG_REQUEST_VARIABLE_REQUEST_METHOD));
var_dump(SeasLog::getRequestVariable(SEASLOG_REQUEST_VARIABLE_CLIENT_IP));
<span class="hljs-comment">// string(3) "cli"</span>
<span class="hljs-comment">// string(5) "1.php"</span>
<span class="hljs-comment">// string(9) "/bin/bash"</span>
<span class="hljs-comment">// string(5) "local"</span>

<span class="hljs-comment">// seaslog.default_template="%T | %L | %P | %Q | %t | %M | %H | %m"</span>

SeasLog::info(<span class="hljs-string">"Test Other Request Variable"</span>);
<span class="hljs-comment">// 2021/01/06 012512 | INFO | 5496 | new_request_id5ff5117888f86 | 1609896312.561 | Test Other Request Variable | localhost.localdomain | /bin/bash</span>

SeasLog::setRequestVariable(SEASLOG_REQUEST_VARIABLE_REQUEST_METHOD, <span class="hljs-string">"Get"</span>);
var_dump(SeasLog::getRequestVariable(SEASLOG_REQUEST_VARIABLE_REQUEST_METHOD)); <span class="hljs-comment">// string(3) "Get"</span>
SeasLog::info(<span class="hljs-string">"Test New Other Request Variable"</span>);
<span class="hljs-comment">// 2021/01/06 012625 | INFO | 5520 | new_request_id5ff511c1367c2 | 1609896385.223 | Test New Other Request Variable | localhost.localdomain | Get</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>getRequestVariable() 和 setRequestVariable() 方法就是用于获取和设置其它请求变量信息的方法。它们都只支持四个常量，也就是代码中演示的这些，分别代表请求的端口号、URI、方法和客户端IP。不过这些内容并没有配置在默认日志模板中，所以我们需要默认的日志模板来查看这些内容。</p>
<p>在这段代码中，我们测试的是给默认模板添加了 %H 和 %m 两个参数，%H 代表的是主机名，%m 代表的是请求的 method ，也就是请求方法。其中 %H 是无法设置修改的，这里只是测试一下格式的配置，而重点在于 %m 的内容。默认情况下，在日志中记录的这个请求方法是 /bin/bash ，其实就是因为我们使用的是命令行来运行的测试代码，它的请求方法就是命令环境 bash 了。这时，我们通过 setRequestVariable() 将请求方法的值修改为 "Get" ，在之后的日志记录中所有的 %m 参数中输出的就都是 Get 了。</p>
<h2 data-id="heading-8">日志记录</h2>
<p>通过上面的学习，我们已经看到了一个 info() 方法的使用。它就是记录普通的日志信息的一个函数，通过它记录的日志信息中的 %L 信息都会显示为 "info" 。后面还有其它的日志类型方法，我们先来看看这个 info() 方法还有什么可以深挖的东西。</p>
<pre><code class="hljs language-php copyable" lang="php">SeasLog::info(<span class="hljs-string">"Test Info Log"</span>);
<span class="hljs-comment">// 2021/01/06 013018 | INFO | 5583 | new_request_id5ff512aaafcde | 1609896618.720 | Test Info Log | localhost.localdomain | Get</span>

SeasLog::info(<span class="hljs-string">"Test &#123;name&#125; Log"</span>, [<span class="hljs-string">'name'</span>=><span class="hljs-string">'Info1'</span>]);
<span class="hljs-comment">// 2021/01/06 013018 | INFO | 5583 | new_request_id5ff512aaafcde | 1609896618.720 | Test Info1 Log | localhost.localdomain | Get</span>

SeasLog::info(<span class="hljs-string">"Test &#123;name&#125; Log"</span>, [<span class="hljs-string">'name'</span>=><span class="hljs-string">'Info1'</span>], <span class="hljs-string">'default'</span>);
<span class="hljs-comment">// ./default/20210106.log</span>
<span class="hljs-comment">// 2021/01/06 013140 | INFO | 5609 | new_request_id5ff512fc264f3 | 1609896700.156 | Test Info1 Log | localhost.localdomain | Get</span>

SeasLog::info(<span class="hljs-string">"Test &#123;name&#125; Log"</span>, [<span class="hljs-string">'name'</span>=><span class="hljs-string">'Info1'</span>], <span class="hljs-string">'defaultNew'</span>);
<span class="hljs-comment">// defaultNew/20210106.log</span>
<span class="hljs-comment">// 2021/01/06 013230 | INFO | 5631 | new_request_id5ff5132e3e143 | 1609896750.254 | Test Info1 Log | localhost.localdomain | Get</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没错，这个 info() 方法除了第一个参数是日志的内容信息之外，它还有两个参数。</p>
<p>第二个参数的作用是可以定义一个数组用来替换第一个参数中的一些占位符。是不是感觉和数据库中的预编译占位符很像。第三个参数则是可以直接指定一个 Logger ，也就是要记录的日志分类目录。这个参数可就方便了，我们当前测试环境是前面设置过的 "mysql" ，所以前两条日志都记录在 mysql 目录下的日志文件中了。而后面两条则是一条记录在 default 目录下，而另一条则是一个新的 defaultNew 目录下。这个新的 Logger 目录我们并没有通过 setLogger() 来创建，但这里也会直接和 setLogger() 一样去创建新的目录和日志文件，非常方便。</p>
<p>除了 info() 外，常见的日志类型还有 notice 、warning、error、alter、debug、critical、emergency 这些。相信只要是用过框架开发或者使用过 monolog 的同学都不会陌生。在 SeasLog 中，这些对应的方法函数也都是存在的，并且所有的参数和 info() 都是一样的。</p>
<pre><code class="hljs language-php copyable" lang="php">SeasLog::alert(<span class="hljs-string">"Test &#123;name&#125; Log"</span>, [<span class="hljs-string">'name'</span>=><span class="hljs-string">'Alert'</span>], <span class="hljs-string">'defaultNew'</span>);
SeasLog::error(<span class="hljs-string">"Test &#123;name&#125; Log"</span>, [<span class="hljs-string">'name'</span>=><span class="hljs-string">'Error'</span>], <span class="hljs-string">'defaultNew'</span>);
SeasLog::debug(<span class="hljs-string">"Test &#123;name&#125; Log"</span>, [<span class="hljs-string">'name'</span>=><span class="hljs-string">'Debug'</span>], <span class="hljs-string">'defaultNew'</span>);
SeasLog::critical(<span class="hljs-string">"Test &#123;name&#125; Log"</span>, [<span class="hljs-string">'name'</span>=><span class="hljs-string">'Critical'</span>], <span class="hljs-string">'defaultNew'</span>);
SeasLog::emergency(<span class="hljs-string">"Test &#123;name&#125; Log"</span>, [<span class="hljs-string">'name'</span>=><span class="hljs-string">'Emergency'</span>], <span class="hljs-string">'defaultNew'</span>);
SeasLog::notice(<span class="hljs-string">"Test &#123;name&#125; Log"</span>, [<span class="hljs-string">'name'</span>=><span class="hljs-string">'Notice'</span>], <span class="hljs-string">'defaultNew'</span>);
SeasLog::warning(<span class="hljs-string">"Test &#123;name&#125; Log"</span>, [<span class="hljs-string">'name'</span>=><span class="hljs-string">'Warning'</span>], <span class="hljs-string">'defaultNew'</span>);
<span class="hljs-comment">// 2021/01/06 014106 | ALERT | 5762 | new_request_id5ff5153200b30 | 1609897266.2 | Test Alert Log | localhost.localdomain | Get</span>
<span class="hljs-comment">// 2021/01/06 014106 | ERROR | 5762 | new_request_id5ff5153200b30 | 1609897266.2 | Test Error Log | localhost.localdomain | Get</span>
<span class="hljs-comment">// 2021/01/06 014106 | DEBUG | 5762 | new_request_id5ff5153200b30 | 1609897266.2 | Test Debug Log | localhost.localdomain | Get</span>
<span class="hljs-comment">// 2021/01/06 014106 | CRITICAL | 5762 | new_request_id5ff5153200b30 | 1609897266.2 | Test Critical Log | localhost.localdomain | Get</span>
<span class="hljs-comment">// 2021/01/06 014106 | EMERGENCY | 5762 | new_request_id5ff5153200b30 | 1609897266.2 | Test Emergency Log | localhost.localdomain | Get</span>
<span class="hljs-comment">// 2021/01/06 014106 | NOTICE | 5762 | new_request_id5ff5153200b30 | 1609897266.2 | Test Notice Log | localhost.localdomain | Get</span>
<span class="hljs-comment">// 2021/01/06 014106 | WARNING | 5762 | new_request_id5ff5153200b30 | 1609897266.2 | Test Warning Log | localhost.localdomain | Get</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，它们记录的日志信息中的 %L 内容都是和自身相对应的。当然，除了这些固定的方法函数之外，我们还有一个通用的记录日志的方法。</p>
<pre><code class="hljs language-php copyable" lang="php">SeasLog::log(SEASLOG_INFO, <span class="hljs-string">"Test log() &#123;name&#125; Log"</span>, [<span class="hljs-string">'name'</span>=><span class="hljs-string">"Info"</span>], <span class="hljs-string">'defaultNew'</span>);
<span class="hljs-comment">// 2021/01/06 014330 | INFO | 5809 | new_request_id5ff515c2ddd5d | 1609897410.908 | Test log() Info Log | localhost.localdomain | Get</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就是这个 log() 方法，它和上面的 info() 那些方法相比，就是多了一个需要指定当前日志类型的参数，而且这个参数也提供了常量。</p>
<h2 data-id="heading-9">日志信息查看</h2>
<p>接下来就是对日志信息的一些数据的查看了。就像上面的测试中我们来回测试其实已经记了不少日志数据了，有没有什么方法函数可以方便地查看这些日志信息内容呢？</p>
<pre><code class="hljs language-php copyable" lang="php">SeasLog::setLogger(<span class="hljs-string">'defaultNew'</span>);
var_dump(SeasLog::analyzerCount());
<span class="hljs-comment">// array(8) &#123;</span>
<span class="hljs-comment">//     ["DEBUG"]=></span>
<span class="hljs-comment">//     int(40)</span>
<span class="hljs-comment">//     ["INFO"]=></span>
<span class="hljs-comment">//     int(80)</span>
<span class="hljs-comment">//     ["NOTICE"]=></span>
<span class="hljs-comment">//     int(40)</span>
<span class="hljs-comment">//     ["WARNING"]=></span>
<span class="hljs-comment">//     int(40)</span>
<span class="hljs-comment">//     ["ERROR"]=></span>
<span class="hljs-comment">//     int(40)</span>
<span class="hljs-comment">//     ["CRITICAL"]=></span>
<span class="hljs-comment">//     int(40)</span>
<span class="hljs-comment">//     ["ALERT"]=></span>
<span class="hljs-comment">//     int(40)</span>
<span class="hljs-comment">//     ["EMERGENCY"]=></span>
<span class="hljs-comment">//     int(40)</span>
<span class="hljs-comment">//   &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先就是这个 analyzerCount() ，它用来统计日志的数量。可以看到在默认情况下它是返回一个数组并且显示的是所有日志类型记录的日志数量的。当然，它可以增加参数，但如果增加参数指定日志类型之后，它返回的就是一个普通的数字值了，也就是这个指定的日志类型的数量信息。</p>
<pre><code class="hljs language-php copyable" lang="php">var_dump(SeasLog::analyzerCount(SEASLOG_WARNING)); <span class="hljs-comment">// int(10)</span>
var_dump(SeasLog::analyzerCount(SEASLOG_ERROR, <span class="hljs-literal">null</span>)); <span class="hljs-comment">// int(10)</span>
var_dump(SeasLog::analyzerCount(SEASLOG_ERROR, <span class="hljs-literal">null</span>, <span class="hljs-string">"1609897995.939"</span>)); <span class="hljs-comment">// int(1)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，它还有另外两个参数，第二个参数是指定日志的路径信息，也就是在当前 Logger 目录下如果还有别的目录的话，可以通过这个参数指定，如果是设置为 null 则忽略这个函数。第三个参数则是过滤信息，就有点像模糊查找的概念，比如我们这里只查找指定的这个时间戳的日志，返回的结果就是只有一条。</p>
<pre><code class="hljs language-php copyable" lang="php">var_dump(SeasLog::analyzerDetail(SEASLOG_ALL, <span class="hljs-string">'secpath/'</span>, <span class="hljs-literal">null</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, SEASLOG_DETAIL_ORDER_DESC));
<span class="hljs-comment">// array(2) &#123;</span>
<span class="hljs-comment">//     [0]=></span>
<span class="hljs-comment">//     string(125) "2021/01/06 020212 | INFO | 6840 | new_request_id5ff51a248e1e2 | 1609898532.582 | Test Info1 Log | localhost.localdomain | Get"</span>
<span class="hljs-comment">//     [1]=></span>
<span class="hljs-comment">//     string(124) "2021/01/06 020212 | INFO | 6840 | new_request_id5ff51a248e1e2 | 1609898532.582 | Test Info Log | localhost.localdomain | Get"</span>
<span class="hljs-comment">//   &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>analyzerDetail() 是可以根据条件展示具体的日志信息。它也是可以指定日志类型、路径目录、关键词信息的，另外它还能够指定返回的条数、排序等，也就是自带范围查找及翻页功能。是不是非常地强悍。同 analyzerCount() 一样，它的参数也都可以设置为 null 表示当前这个参数不启用走默认的值。比如我们这个测试代码中的 null 就是关键字那个参数位置，表示的就是不用去模糊匹配关键字。</p>
<h2 data-id="heading-10">内存缓冲区日志</h2>
<p>除了可以直接记录文件日志外，SeasLog 还可以在 php.ini 中通过配置来将文件发送到指定的 tcp 或 ftp 服务器，这个大家可以自行了解下。而接下来要学习的是在内存中缓存日志的操作。通过这个配置，我们可以更进一步地提升 SeasLog 的性能表现。</p>
<p>如果每条日志都是实时地写入磁盘或者发送的外部，无疑都会带来额外的磁盘IO或者网络IO开销，为了进一步提升性能，SeasLog 中提供的内存缓冲能力就可以帮我们解决问题，它的意思其实就是先将日志保存在内存中，然后到达一定数量之后再一次性地写入到磁盘或者发送给外部。</p>
<pre><code class="hljs language-php copyable" lang="php">var_dump(SeasLog::getBufferEnabled()); <span class="hljs-comment">// bool(false)</span>

<span class="hljs-comment">// seaslog.use_buffer=1</span>
<span class="hljs-comment">// seaslog.buffer_disabled_in_cli=0</span>
<span class="hljs-comment">// seaslog.buffer_size=100</span>
var_dump(SeasLog::getBufferEnabled()); <span class="hljs-comment">// bool(true)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们需要在 php.ini 中配置 seaslog.use_buffer 为 1 ，也就是开启内存缓冲的功能。如果是命令行脚本运行的话，还需要将 seaslog.buffer_disabled_in_cli 设置为 0 ，关闭“内存缓冲在cli环境下不启用”的功能。最后，设置一下 seaslog.buffer_size ，也就是缓冲区保存多少条数据。当这些设置完成之后，使用 getBufferEnabled() 就可以看到返回的内容是 true 了，也就是我们已经开启了内存缓冲的能力。</p>
<p>接下来，使用 getBuffer() 方法就可以看到目前在内存缓冲区中的所有日志信息了。</p>
<pre><code class="hljs language-php copyable" lang="php">var_dump(SeasLog::getBuffer());
<span class="hljs-comment">// array(3) &#123;</span>
<span class="hljs-comment">//     [".//default/20210106.log"]=></span>
<span class="hljs-comment">//     array(2) &#123;</span>
<span class="hljs-comment">//       [0]=></span>
<span class="hljs-comment">//       string(125) "2021-01-06 02:21:43 | INFO | 8006 | 5ff51eb7e1a54 | 1609899703.924 | Test Logger Default | localhost.localdomain | /bin/bash</span>
<span class="hljs-comment">//   "</span>
<span class="hljs-comment">//     ……………………</span>
<span class="hljs-comment">//     &#125;</span>
<span class="hljs-comment">//     [".//mylog/20210106.log"]=></span>
<span class="hljs-comment">//     array(8) &#123;</span>
<span class="hljs-comment">//       [0]=></span>
<span class="hljs-comment">//       string(123) "2021-01-06 02:21:43 | INFO | 8006 | 5ff51eb7e1a54 | 1609899703.924 | Test Logger MyLog | localhost.localdomain | /bin/bash</span>
<span class="hljs-comment">//   "</span>
<span class="hljs-comment">//       ……………………</span>
<span class="hljs-comment">//     &#125;</span>
<span class="hljs-comment">//     [".//defaultNew/20210106.log"]=></span>
<span class="hljs-comment">//     array(9) &#123;</span>
<span class="hljs-comment">//       [0]=></span>
<span class="hljs-comment">//       string(126) "2021/01/06 022143 | INFO | 8006 | new_request_id5ff51eb7e1b30 | 1609899703.924 | Test Info1 Log | localhost.localdomain | Get</span>
<span class="hljs-comment">//   "</span>
<span class="hljs-comment">//       ……………………</span>
<span class="hljs-comment">//     &#125;</span>
<span class="hljs-comment">//   &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当开启了内存缓冲的功能之后，我们前面的测试代码中的所有记录日志的操作都会将日志记录在内存中了，所以 getBuffer() 方法返回的数组中会有非常多的数据。当脚本结束运行或者请求终止的时候，这些内存中的数据就会写入磁盘或者发送走。当然，我们也可以手动地将这些数据刷新到磁盘上。</p>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-comment">// 刷新内存缓冲区</span>
SeasLog::flushBuffer();
var_dump(SeasLog::getBuffer());
<span class="hljs-comment">// array(0) &#123;</span>
<span class="hljs-comment">// &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用 flushBuffer() 方法就可以手动地将内存数据刷新掉，这时再调用 getBuffer() 就没有任何数据了。同时我们的测试文件中也一次性地写入了所有的日志数据。</p>
<h2 data-id="heading-11">总结</h2>
<p>不得不说，通过这个扩展的学习貌似又发现了一个大宝藏。这种日志系统在底层扩展上进行操作，效率肯定是没有问题，但是麻烦的也是需要安装底层的扩展，而不像 monolog 之类的可以直接使用 Composer 就完成安装使用。事物总有利弊，具体合适哪种还是要根据我们的业务场景来深入分析判断。</p>
<p>测试代码：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzhangyue0503%2Fdev-blog%2Fblob%2Fmaster%2Fphp%2F2021%2F01%2Fsource%2F2.%25E5%25AD%25A6%25E4%25B9%25A0%25E4%25BA%2586%25E8%25A7%25A3PHP%25E4%25B8%25AD%25E7%259A%2584SeasLog%25E6%2597%25A5%25E5%25BF%2597%25E6%2589%25A9%25E5%25B1%2595.php" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zhangyue0503/dev-blog/blob/master/php/2021/01/source/2.%E5%AD%A6%E4%B9%A0%E4%BA%86%E8%A7%A3PHP%E4%B8%AD%E7%9A%84SeasLog%E6%97%A5%E5%BF%97%E6%89%A9%E5%B1%95.php" ref="nofollow noopener noreferrer">github.com/zhangyue050…</a></p>
<p>参考文档：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.php.net%2Fmanual%2Fzh%2Fbook.seaslog.php" target="_blank" rel="nofollow noopener noreferrer" title="https://www.php.net/manual/zh/book.seaslog.php" ref="nofollow noopener noreferrer">www.php.net/manual/zh/b…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSeasX%2FSeasLog%2Fblob%2Fmaster%2FREADME_zh.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SeasX/SeasLog/blob/master/README_zh.md" ref="nofollow noopener noreferrer">Github文档</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSeasX%2FSeasLog%2Fblob%2Fmaster%2FREADME_zh.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SeasX/SeasLog/blob/master/README_zh.md" ref="nofollow noopener noreferrer">github.com/SeasX/SeasL…</a></p></div>  
</div>
            