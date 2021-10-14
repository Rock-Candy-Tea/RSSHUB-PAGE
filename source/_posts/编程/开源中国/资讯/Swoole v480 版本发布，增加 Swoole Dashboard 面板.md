
---
title: 'Swoole v4.8.0 版本发布，增加 Swoole Dashboard 面板'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7708'
author: 开源中国
comments: false
date: Thu, 14 Oct 2021 10:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7708'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#212529; text-align:left">距离上个版本<code>v4.7.1</code>发布近两个月了，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Fenc%3DVHpeijz0vrSEcqiTCpNb9A%253D%253D.MCymYhUtUdfTICllCabiwyreChldQvY2hfbSJgddZJxmH32L91UFrVD8f9t%252FMNyw5IzzPZjdxJ3Leg3%252F%252FphWEA%253D%253D" target="_blank">v4.8.0</a><span> </span>版本终于发布了。</p> 
<p style="color:#212529; text-align:left">此版本包含了新功能、BUG 修复以及向下不兼容的改动。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">不兼容改动</h2> 
<p style="color:#212529; text-align:left">在 base 模式下，onStart 回调将始终在第一个工作进程 (worker id 为 0) 启动时回调，先于 onWorkerStart 执行。在 onStart 函数中始终可以使用协程 API，Worker-0 出现致命错误重启时，会再次回调 onStart</p> 
<p style="color:#212529; text-align:left">在之前的版本中，onStart 在只有一个工作进程时，会在 Worker-0 中回调。有多个工作进程时，在 Manager 进程中执行。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">admin_server</h2> 
<p style="color:#212529; text-align:left">在此版本中重要的功能就是增加了<code>admin_server</code>的选项，用于提供 API 服务，可以用于在 Swoole Dashboard 面板中查看当前服务的信息，例如 PHP 加载的扩展、文件、类、函数、常量，以及 Swoole 相关的进程、协程、连接信息等。</p> 
<pre style="text-align:left"><span style="color:#6a737d">//创建Server对象，监听 127.0.0.1:9501 端口</span>
<span style="color:#005cc5">$server</span> = <span style="color:#d73a49">new</span> Swoole\Server(<span style="color:#032f62">'127.0.0.1'</span>, <span style="color:#005cc5">9501</span>);

<span style="color:#005cc5">$server</span>->set([
    <span style="color:#032f62">'admin_server'</span> => <span style="color:#032f62">'0.0.0.0:9502'</span>, <span style="color:#6a737d">// 启用 admin_server 服务</span>
    <span style="color:#032f62">'worker_num'</span> => <span style="color:#005cc5">2</span>,
    <span style="color:#032f62">'task_worker_num'</span> => <span style="color:#005cc5">3</span>
]);

<span style="color:#6a737d">//监听连接进入事件</span>
<span style="color:#005cc5">$server</span>->on(<span style="color:#032f62">'Connect'</span>, <span><span style="color:#d73a49">function</span> (<span><span style="color:#005cc5">$server</span>, <span style="color:#005cc5">$fd</span></span>) </span>&#123;
    <span style="color:#d73a49">echo</span> <span style="color:#032f62">"Client: Connect.\n"</span>;
&#125;);

<span style="color:#6a737d">//监听数据接收事件</span>
<span style="color:#005cc5">$server</span>->on(<span style="color:#032f62">'Receive'</span>, <span><span style="color:#d73a49">function</span> (<span><span style="color:#005cc5">$server</span>, <span style="color:#005cc5">$fd</span>, <span style="color:#005cc5">$reactor_id</span>, <span style="color:#005cc5">$data</span></span>) </span>&#123;
    <span style="color:#005cc5">$server</span>->send(<span style="color:#005cc5">$fd</span>, <span style="color:#032f62">"Server: <span style="color:#24292e">&#123;$data&#125;</span>"</span>);
&#125;);

<span style="color:#6a737d">//监听连接关闭事件</span>
<span style="color:#005cc5">$server</span>->on(<span style="color:#032f62">'Close'</span>, <span><span style="color:#d73a49">function</span> (<span><span style="color:#005cc5">$server</span>, <span style="color:#005cc5">$fd</span></span>) </span>&#123;
    <span style="color:#d73a49">echo</span> <span style="color:#032f62">"Client: Close.\n"</span>;
&#125;);

<span style="color:#6a737d">//启动服务器</span>
<span style="color:#005cc5">$server</span>->start();</pre> 
<p style="color:#212529; text-align:left">可以在更新 Swoole v4.8.0 版本后，前往<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Fenc%3DT8hCes7tTrikgstxQRQWNA%253D%253D.eDabFXqJJqQJ%252Fxcd%252BAK0VC4uPJc7pEwIuT%252BAvjKYtHM%253D" target="_blank">https://dashboard.swoole.com/</a><span> </span>进行体验。</p> 
<p style="color:#212529; text-align:left">在登录时配置本地的<code>admin_server</code>地址或者云端的地址，形如：<code>http://127.0.0.1:9502/</code><span> </span>，登录后也可以在右上角配置其他地址。</p> 
<blockquote>
 注：少数功能受限，需要安装
 <code>ext-swoole_plus</code>
</blockquote> 
<p style="color:#212529; text-align:left">另外还增加了一些新的 API：<code>Table::stats</code>、<code>Coroutine::join</code>等，下面来具体看一下：</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Coroutine::join</h2> 
<p style="color:#212529; text-align:left">并发执行多个协程。</p> 
<pre style="text-align:left">Swoole\Coroutine::join(<span style="color:#d73a49">array</span> <span style="color:#005cc5">$cid_array</span>, <span style="color:#d73a49">float</span> <span style="color:#005cc5">$timeout</span> = -<span style="color:#005cc5">1</span>): <span style="color:#d73a49">bool</span></pre> 
<p style="color:#212529; text-align:left"><code>$timeout</code>为总的超时时间，超时后会立即返回。但正在运行的协程会继续执行完毕，而不会中止</p> 
<pre style="text-align:left"><span style="color:#d73a49">use</span> <span style="color:#6f42c1">Swoole</span>\<span style="color:#6f42c1">Coroutine</span>;
<span style="color:#d73a49">use</span> <span style="color:#6f42c1">function</span> <span style="color:#6f42c1">Swoole</span>\<span style="color:#6f42c1">Coroutine</span>\<span style="color:#6f42c1">go</span>;
<span style="color:#d73a49">use</span> <span style="color:#6f42c1">function</span> <span style="color:#6f42c1">Swoole</span>\<span style="color:#6f42c1">Coroutine</span>\<span style="color:#6f42c1">run</span>;

run(<span><span style="color:#d73a49">function</span> () </span>&#123;
    <span style="color:#005cc5">$status</span> = Coroutine::join([
        go(<span><span style="color:#d73a49">function</span> () <span style="color:#d73a49">use</span> (<span>&<span style="color:#005cc5">$result</span></span>) </span>&#123;
            <span style="color:#005cc5">$result</span>[<span style="color:#032f62">'baidu'</span>] = strlen(file_get_contents(<span style="color:#032f62">'https://www.baidu.com/'</span>));
        &#125;),
        go(<span><span style="color:#d73a49">function</span> () <span style="color:#d73a49">use</span> (<span>&<span style="color:#005cc5">$result</span></span>) </span>&#123;
            <span style="color:#005cc5">$result</span>[<span style="color:#032f62">'zhihu'</span>] = strlen(file_get_contents(<span style="color:#032f62">'https://www.zhihu.com/'</span>));
        &#125;)
    ], <span style="color:#005cc5">1</span>);
    var_dump(<span style="color:#005cc5">$result</span>, <span style="color:#005cc5">$status</span>);
&#125;);</pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">addCommand/command</h2> 
<p style="color:#212529; text-align:left">Swoole Dashboard 的 API 就是基于<code>addCommand</code>提供的，代码位于<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Fenc%3DLNDCF9ttrrZu57DE48iySw%253D%253D.4sKzgr6PKHosmV0NFhvrjliWU8YTu5eencWEjtqvdUmDZhXEU1%252Fu54R%252FarBOFTRmEfRS0u2tn%252BUfitHs%252BGsFGP696BKm9WUiPJTO%252B1WSX9E%253D" target="_blank">library</a><span> </span>中，除了 library 中提供的<code>command</code>，swoole 扩展中也有一些。</p> 
<p style="color:#212529; text-align:left">当然也可以自定义：</p> 
<pre style="text-align:left">Swoole\Server->addCommand(<span style="color:#d73a49">string</span> <span style="color:#005cc5">$name</span>, <span style="color:#d73a49">int</span> <span style="color:#005cc5">$accepted_process_types</span>, <span style="color:#d73a49">callable</span> <span style="color:#005cc5">$callback</span>)

<span style="color:#005cc5">$server</span>->addCommand(<span style="color:#032f62">'test_getpid'</span>, SWOOLE_SERVER_COMMAND_MASTER | SWOOLE_SERVER_COMMAND_EVENT_WORKER,
    <span><span style="color:#d73a49">function</span> (<span><span style="color:#005cc5">$server</span></span>) </span>&#123;
        <span style="color:#d73a49">return</span> json_encode([<span style="color:#032f62">'pid'</span> => posix_getpid()]);
&#125;);</pre> 
<p style="color:#212529; text-align:left"><code>command</code>方法用于在 server 中调用定义的接口：</p> 
<pre style="text-align:left">Swoole\Server->command(<span style="color:#d73a49">string</span> <span style="color:#005cc5">$name</span>, <span style="color:#d73a49">int</span> <span style="color:#005cc5">$process_id</span>, <span style="color:#d73a49">int</span> <span style="color:#005cc5">$process_type</span>, <span style="color:#005cc5">$data</span>, <span style="color:#d73a49">bool</span> <span style="color:#005cc5">$json_decode</span> = <span style="color:#005cc5">true</span>)

<span style="color:#005cc5">$server</span>->command(<span style="color:#032f62">'test_getpid'</span>, <span style="color:#005cc5">0</span>, SWOOLE_SERVER_COMMAND_MASTER, [<span style="color:#032f62">'type'</span> => <span style="color:#032f62">'master'</span>]);</pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">onBeforeShutdown</h2> 
<p style="color:#212529; text-align:left">新增<code>onBeforeShutdown</code>事件回调，在此回调中可以使用协程 API。</p> 
<ul> 
 <li><strong>安全提示</strong></li> 
</ul> 
<p style="color:#212529; text-align:left">在<code>onStart</code>回调中可以使用异步和协程的 API，但需要注意这可能会与<code>dispatch_func</code>和<code>package_length_func</code>存在冲突，<strong>请勿同时使用</strong>。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Coroutine::getStackUsage()</h2> 
<p style="color:#212529; text-align:left">获取当前 PHP 栈的内存使用量。</p> 
<pre style="text-align:left">Swoole\Coroutine::getStackUsage([<span style="color:#005cc5">$cid</span>]): <span style="color:#d73a49">int</span></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Table::stats</h2> 
<p style="color:#212529; text-align:left">用来获取<span> </span><code>Swoole\Table</code><span> </span>状态。</p> 
<pre style="text-align:left"><span style="color:#d73a49">use</span> <span style="color:#6f42c1">Swoole</span>\<span style="color:#6f42c1">Table</span>;

<span style="color:#005cc5">$table</span> = <span style="color:#d73a49">new</span> Table(<span style="color:#005cc5">1024</span>);
<span style="color:#005cc5">$table</span>->column(<span style="color:#032f62">'string'</span>, Table::TYPE_STRING, <span style="color:#005cc5">256</span>);
<span style="color:#005cc5">$table</span>->create();

<span style="color:#005cc5">$table</span>->set(<span style="color:#032f62">'swoole'</span>, [<span style="color:#032f62">'string'</span> => <span style="color:#032f62">'www.swoole.com'</span>]);
var_dump(<span style="color:#005cc5">$table</span>->stats());

<span style="color:#6a737d">//array(8) &#123;</span>
<span style="color:#6a737d">//  ["num"]=></span>
<span style="color:#6a737d">//  int(1)</span>
<span style="color:#6a737d">//  ["conflict_count"]=></span>
<span style="color:#6a737d">//  int(0)</span>
<span style="color:#6a737d">//  ["conflict_max_level"]=></span>
<span style="color:#6a737d">//  int(0)</span>
<span style="color:#6a737d">//  ["insert_count"]=></span>
<span style="color:#6a737d">//  int(1)</span>
<span style="color:#6a737d">//  ["update_count"]=></span>
<span style="color:#6a737d">//  int(0)</span>
<span style="color:#6a737d">//  ["delete_count"]=></span>
<span style="color:#6a737d">//  int(0)</span>
<span style="color:#6a737d">//  ["available_slice_num"]=></span>
<span style="color:#6a737d">//  int(204)</span>
<span style="color:#6a737d">//  ["total_slice_num"]=></span>
<span style="color:#6a737d">//  int(204)</span>
<span style="color:#6a737d">//&#125;</span></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更新日志</h2> 
<p style="color:#212529; text-align:left">下面是完整的更新日志：</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">向下不兼容改动</h3> 
<ul> 
 <li>在 base 模式下，onStart 回调将始终在第一个工作进程 (worker id 为 0) 启动时回调，先于 onWorkerStart 执行 (#4389) (@matyhtf)</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">新增 API</h3> 
<ul> 
 <li>新增<span> </span><code>Coroutine::getStackUsage()</code><span> </span>方法 (#4398) (@matyhtf) (@twose)</li> 
 <li>新增<span> </span><code>Coroutine\Redis</code><span> </span>的一些 API (#4390) (@chrysanthemum)</li> 
 <li>新增<span> </span><code>Table::stats()</code><span> </span>方法 (#4405) (@matyhtf)</li> 
 <li>新增<span> </span><code>Coroutine::join()</code><span> </span>方法 (#4406) (@matyhtf)</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">新增功能</h3> 
<ul> 
 <li>支持 server command (#4389) (@matyhtf)</li> 
 <li>支持<span> </span><code>Server::onBeforeShutdown</code><span> </span>事件回调 (#4415) (@matyhtf)</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">增强</h3> 
<ul> 
 <li>当 Websocket pack 失败时设置错误码 (swoole/swoole-src@d27c5a5) (@matyhtf)</li> 
 <li>新增<span> </span><code>Timer::exec_count</code><span> </span>字段 (#4402) (@matyhtf)</li> 
 <li>hook mkdir 支持使用 open_basedir ini 配置 (#4407) (@NathanFreeman)</li> 
 <li>library 新增 vendor_init.php 脚本 (swoole/library@6c40b02) (@matyhtf)</li> 
 <li>SWOOLE_HOOK_CURL 支持 CURLOPT_UNIX_SOCKET_PATH (swoole/library#121) (@sy-records)</li> 
 <li>Client 支持设置 ssl_ciphers 配置项 (#4432) (@amuluowin)</li> 
 <li>为<span> </span><code>Server::stats()</code><span> </span>添加了一些新的信息 (#4410) (#4412) (@matyhtf)</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">修复</h3> 
<ul> 
 <li>修复文件上传时，对文件名字进行不必要的 URL decode (swoole/swoole-src@a73780e) (@matyhtf)</li> 
 <li>修复 HTTP2 max_frame_size 问题 (#4394) (@twose)</li> 
 <li>修复 curl_multi_select bug #4393 (#4418) (@matyhtf)</li> 
 <li>修复丢失的 coroutine options (#4425) (@sy-records)</li> 
 <li>修复当发送缓冲区满的时候，连接无法被 close 的问题 (swoole/swoole-src@2198378) (@matyhtf)</li> 
</ul>
                                        </div>
                                      
</div>
            