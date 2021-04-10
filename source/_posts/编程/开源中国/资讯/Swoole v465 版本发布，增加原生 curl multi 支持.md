
---
title: 'Swoole v4.6.5 版本发布，增加原生 curl multi 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8754'
author: 开源中国
comments: false
date: Fri, 09 Apr 2021 19:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8754'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fswoole%2Fswoole-src%2Freleases%2Ftag%2Fv4.6.5" target="_blank">v4.6.5</a> 版本没有向下不兼容改动，主要对原生 curl hook 进行了一些增强，支持了 curl multi</p> 
<ul> 
 <li>支持原生 curl multi</li> 
</ul> 
<p style="text-align:left">使用原生 curl hook 的前提是在编译 Swoole 扩展时开启<code>--enable-swoole-curl</code>选项</p> 
<p style="text-align:left">可以使用以下代码进行测试：</p> 
<pre style="text-align:left"><code><strong>use</strong> <strong>Swoole</strong>\<strong>Runtime</strong>;
<strong>use</strong> <strong>function</strong> <strong>Swoole</strong>\<strong>Coroutine</strong>\<strong>run</strong>;

Runtime::enableCoroutine(SWOOLE_HOOK_NATIVE_CURL);
run(<strong>function</strong> () &#123;
    <span style="color:teal">$ch1</span> = curl_init();
    <span style="color:teal">$ch2</span> = curl_init();

    <em>// 设置URL和相应的选项</em>
    curl_setopt(<span style="color:teal">$ch1</span>, CURLOPT_URL, <span style="color:#dd1144">"http://www.baidu.com/"</span>);
    curl_setopt(<span style="color:teal">$ch1</span>, CURLOPT_HEADER, <span style="color:teal">0</span>);
    curl_setopt(<span style="color:teal">$ch1</span>, CURLOPT_RETURNTRANSFER, <span style="color:teal">1</span>);

    curl_setopt(<span style="color:teal">$ch2</span>, CURLOPT_URL, <span style="color:#dd1144">"http://www.gov.cn/"</span>);
    curl_setopt(<span style="color:teal">$ch2</span>, CURLOPT_HEADER, <span style="color:teal">0</span>);
    curl_setopt(<span style="color:teal">$ch2</span>, CURLOPT_RETURNTRANSFER, <span style="color:teal">1</span>);

    <span style="color:teal">$mh</span> = curl_multi_init();

    curl_multi_add_handle(<span style="color:teal">$mh</span>, <span style="color:teal">$ch1</span>);
    curl_multi_add_handle(<span style="color:teal">$mh</span>, <span style="color:teal">$ch2</span>);

    <span style="color:teal">$active</span> = <span style="color:teal">null</span>;
    <em>// 执行批处理句柄</em>
    <strong>do</strong> &#123;
        <span style="color:teal">$mrc</span> = curl_multi_exec(<span style="color:teal">$mh</span>, <span style="color:teal">$active</span>);
    &#125; <strong>while</strong> (<span style="color:teal">$mrc</span> == CURLM_CALL_MULTI_PERFORM);

    <strong>while</strong> (<span style="color:teal">$active</span> && <span style="color:teal">$mrc</span> == CURLM_OK) &#123;
        <span style="color:teal">$n</span> = curl_multi_select(<span style="color:teal">$mh</span>);
        <strong>if</strong> (<span style="color:teal">$n</span> != -<span style="color:teal">1</span>) &#123;
            <strong>do</strong> &#123;
                <span style="color:teal">$mrc</span> = curl_multi_exec(<span style="color:teal">$mh</span>, <span style="color:teal">$active</span>);
            &#125; <strong>while</strong> (<span style="color:teal">$mrc</span> == CURLM_CALL_MULTI_PERFORM);
        &#125;
    &#125;

    <span style="color:teal">$info1</span> = curl_multi_info_read(<span style="color:teal">$mh</span>);
    <span style="color:teal">$info2</span> = curl_multi_info_read(<span style="color:teal">$mh</span>);
    <span style="color:teal">$info3</span> = curl_multi_info_read(<span style="color:teal">$mh</span>);

    assert(<span style="color:teal">$info1</span>[<span style="color:#dd1144">'msg'</span>] === CURLMSG_DONE);
    assert(<span style="color:teal">$info2</span>[<span style="color:#dd1144">'msg'</span>] === CURLMSG_DONE);
    assert(<span style="color:teal">$info3</span> === <span style="color:teal">false</span>);

    assert(strpos(curl_multi_getcontent(<span style="color:teal">$ch1</span>),<span style="color:#dd1144">'baidu.com'</span>) !== <span style="color:teal">false</span>);
    assert(strpos(curl_multi_getcontent(<span style="color:teal">$ch2</span>),<span style="color:#dd1144">'中央人民政府门户网站'</span>) !== <span style="color:teal">false</span>);

    curl_multi_remove_handle(<span style="color:teal">$mh</span>, <span style="color:teal">$ch1</span>);
    curl_multi_remove_handle(<span style="color:teal">$mh</span>, <span style="color:teal">$ch2</span>);

    curl_multi_close(<span style="color:teal">$mh</span>);
&#125;);</code></pre> 
<p style="text-align:left">支持 curl multi 之后，也就间接的支持了 Guzzle，<strong>无需更改任何代码</strong>，即可支持。</p> 
<pre style="text-align:left"><code><strong>include</strong> <strong>__DIR__</strong> . <span style="color:#dd1144">'/vendor/autoload.php'</span>;

<strong>use</strong> <strong>Swoole</strong>\<strong>Coroutine</strong>\<strong>Barrier</strong>;
<strong>use</strong> <strong>Swoole</strong>\<strong>Runtime</strong>;
<strong>use</strong> <strong>GuzzleHttp</strong>\<strong>Client</strong>;
<strong>use</strong> <strong>GuzzleHttp</strong>\<strong>Promise</strong>;

<strong>use</strong> <strong>function</strong> <strong>Swoole</strong>\<strong>Coroutine</strong>\<strong>run</strong>;
<strong>use</strong> <strong>function</strong> <strong>Swoole</strong>\<strong>Coroutine</strong>\<strong>go</strong>;

Runtime::enableCoroutine(SWOOLE_HOOK_NATIVE_CURL);

<strong>const</strong> N = <span style="color:teal">4</span>;

run(<strong>function</strong> () &#123;
    <span style="color:teal">$barrier</span> = Barrier::make();
    <span style="color:teal">$result</span> = [];
    go(<strong>function</strong> () <strong>use</strong> (<span style="color:teal">$barrier</span>, &<span style="color:teal">$result</span>) &#123;
        <span style="color:teal">$client</span> = <strong>new</strong> Client();
        <span style="color:teal">$promises</span> = [
            <span style="color:#dd1144">'baidu'</span> => <span style="color:teal">$client</span>->getAsync(<span style="color:#dd1144">'http://www.baidu.com/'</span>),
            <span style="color:#dd1144">'qq'</span> => <span style="color:teal">$client</span>->getAsync(<span style="color:#dd1144">'https://www.qq.com/'</span>),
            <span style="color:#dd1144">'gov'</span> => <span style="color:teal">$client</span>->getAsync(<span style="color:#dd1144">'http://www.gov.cn/'</span>)
        ];
        <span style="color:teal">$responses</span> = Promise\Utils::unwrap(<span style="color:teal">$promises</span>);
        assert(strpos(<span style="color:teal">$responses</span>[<span style="color:#dd1144">'baidu'</span>]->getBody(),<span style="color:#dd1144">'百度'</span>) !== <span style="color:teal">false</span>);
        assert(strpos(iconv(<span style="color:#dd1144">'gbk'</span>, <span style="color:#dd1144">'utf-8'</span>, <span style="color:teal">$responses</span>[<span style="color:#dd1144">'qq'</span>]->getBody()),<span style="color:#dd1144">'腾讯'</span>) !== <span style="color:teal">false</span>);
        assert(strpos(<span style="color:teal">$responses</span>[<span style="color:#dd1144">'gov'</span>]->getBody(),<span style="color:#dd1144">'中华人民共和国'</span>) !== <span style="color:teal">false</span>);
        <span style="color:teal">$result</span>[<span style="color:#dd1144">'task_1'</span>] = <span style="color:#dd1144">'OK'</span>;
    &#125;);

    go(<strong>function</strong> () <strong>use</strong> (<span style="color:teal">$barrier</span>, &<span style="color:teal">$result</span>) &#123;
        <span style="color:teal">$client</span> = <strong>new</strong> Client([<span style="color:#dd1144">'base_uri'</span> => <span style="color:#dd1144">'http://httpbin.org/'</span>]);
        <span style="color:teal">$n</span> = N;
        <span style="color:teal">$data</span> = <span style="color:teal">$promises</span> = [];
        <strong>while</strong> (<span style="color:teal">$n</span>--) &#123;
            <span style="color:teal">$key</span> = <span style="color:#dd1144">'req_'</span> . <span style="color:teal">$n</span>;
            <span style="color:teal">$data</span>[<span style="color:teal">$key</span>] = uniqid(<span style="color:#dd1144">'swoole_test'</span>);
            <span style="color:teal">$promises</span>[<span style="color:teal">$key</span>] = <span style="color:teal">$client</span>->getAsync(<span style="color:#dd1144">'/base64/'</span> . base64_encode(<span style="color:teal">$data</span>[<span style="color:teal">$key</span>]));
        &#125;
        <span style="color:teal">$responses</span> = Promise\Utils::unwrap(<span style="color:teal">$promises</span>);

        <span style="color:teal">$n</span> = N;
        <strong>while</strong> (<span style="color:teal">$n</span>--) &#123;
            <span style="color:teal">$key</span> = <span style="color:#dd1144">'req_'</span> . <span style="color:teal">$n</span>;
            assert(<span style="color:teal">$responses</span>[<span style="color:teal">$key</span>]->getBody() === <span style="color:teal">$data</span>[<span style="color:teal">$key</span>]);
        &#125;
        <span style="color:teal">$result</span>[<span style="color:#dd1144">'task_2'</span>] = <span style="color:#dd1144">'OK'</span>;
    &#125;);

    Barrier::wait(<span style="color:teal">$barrier</span>);
    assert(<span style="color:teal">$result</span>[<span style="color:#dd1144">'task_1'</span>] === <span style="color:#dd1144">'OK'</span>);
    assert(<span style="color:teal">$result</span>[<span style="color:#dd1144">'task_2'</span>] === <span style="color:#dd1144">'OK'</span>);
    <strong>echo</strong> <span style="color:#dd1144">'Done'</span> . PHP_EOL;
&#125;);</code></pre> 
<p style="text-align:left">同时也还添加了一些 Guzzle 的单元测试。</p> 
<ul> 
 <li>允许在使用 HTTP/2 的 Response 中使用数组设置 headers</li> 
</ul> 
<p style="text-align:left">从 <code>v4.6.0</code> 版本开始 Swoole\Http\Response 支持重复设置相同 <code>$key</code> 的 <code>HTTP</code> 头，并且 <code>$value</code> 支持多种类型，如 <code>array</code>、<code>object</code>、<code>int</code>、<code>float</code>，底层会进行 <code>toString</code> 转换，并且会移除末尾的空格以及换行。</p> 
<p style="text-align:left">但是未支持 HTTP/2 的，详情见 issue <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fswoole%2Fswoole-src%2Fissues%2F4133" target="_blank">#4133</a></p> 
<p style="text-align:left">在此版本中也进行了支持：</p> 
<pre style="text-align:left"><code><span style="color:teal">$http</span> = <strong>new</strong> Swoole\Http\Server(<span style="color:#dd1144">'127.0.0.1'</span>, <span style="color:teal">9501</span>);
<span style="color:teal">$http</span>->set([<span style="color:#dd1144">'open_http2_protocol'</span> => <span style="color:teal">true</span>]);

<span style="color:teal">$http</span>->on(<span style="color:#dd1144">'request'</span>, <strong>function</strong> (<span style="color:teal">$request</span>, <span style="color:teal">$response</span>) &#123;
    <span style="color:teal">$response</span>->header(<span style="color:#dd1144">'Test-Value'</span>, [
        <span style="color:#dd1144">"a\r\n"</span>,
        <span style="color:#dd1144">'d5678'</span>,
        <span style="color:#dd1144">"e  \n "</span>,
        <span style="color:teal">null</span>,
        <span style="color:teal">5678</span>,
        <span style="color:teal">3.1415926</span>,
    ]);

    <span style="color:teal">$response</span>->end(<span style="color:#dd1144">"<h1>Hello Swoole. #"</span>.rand(<span style="color:teal">1000</span>, <span style="color:teal">9999</span>).<span style="color:#dd1144">"</h1>"</span>);
&#125;);
<span style="color:teal">$http</span>->start();</code></pre> 
<p style="text-align:left">可以使用以上代码进行测试，并使用 curl 命令进行测试结果</p> 
<pre style="text-align:left"><code>$ curl --http2-prior-knowledge -v http://localhost:9501
*   Trying ::1...
* TCP_NODELAY <span style="color:#0086b3">set</span>
* Connection failed
* connect to ::1 port 9501 failed: Connection refused
*   Trying 127.0.0.1...
* TCP_NODELAY <span style="color:#0086b3">set</span>
* Connected to localhost (127.0.0.1) port 9501 (<em>#0)</em>
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data <strong>in</strong> stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7fe9e9009200)
> GET / HTTP/2
> Host: localhost:9501
> User-Agent: curl/7.64.1
> Accept: */*
>
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
< HTTP/2 200
< test-value: a
< test-value: d5678
< test-value: e
< test-value: 5678
< test-value: 3.1415926
< server: swoole-http-server
< date: Fri, 09 Apr 2021 11:04:39 GMT
< content-type: text/html
< content-length: 28
<
* Connection <em>#0 to host localhost left intact</em>
<h1>Hello Swoole. <em>#6944</h1>* Closing connection 0</em></code></pre> 
<h2 style="text-align:left">更新日志</h2> 
<p style="text-align:left">下面是完整的更新日志：</p> 
<h3 style="text-align:left">新增 API</h3> 
<ul> 
 <li>在 WaitGroup 中增加 count 方法(swoole/library#100) (@sy-records) (@deminy)</li> 
</ul> 
<h3 style="text-align:left">增强</h3> 
<ul> 
 <li>支持原生 curl multi (#4093) (#4099) (#4101) (#4105) (#4113) (#4121) (#4147) (swoole/swoole-src@cd7f51c) (@matyhtf) (@sy-records) (@huanghantao)</li> 
 <li>允许在使用 HTTP/2 的 Response 中使用数组设置 headers</li> 
</ul> 
<h3 style="text-align:left">修复</h3> 
<ul> 
 <li>修复 NetBSD 构建 (#4080) (@devnexen)</li> 
 <li>修复 OpenBSD 构建 (#4108) (@devnexen)</li> 
 <li>修复 illumos/solaris 构建，只有成员别名 (#4109) (@devnexen)</li> 
 <li>修复握手未完成时，SSL 连接的心跳检测不生效 (#4114) (@matyhtf)</li> 
 <li>修复 Http\Client 使用代理时<code>host</code>中存在<code>host:port</code>产生的错误 (#4124) (@Yurunsoft)</li> 
 <li>修复 Swoole\Coroutine\Http::request 中 header 和 cookie 的设置 (swoole/library#103) (@leocavalcante) (@deminy)</li> 
</ul> 
<h3 style="text-align:left">内核</h3> 
<ul> 
 <li>支持 BSD 上的 asm context (#4082) (@devnexen)</li> 
 <li>在 FreeBSD 下使用 arc4random\_buf 来实现 getrandom (#4096) (@devnexen)</li> 
 <li>优化 darwin arm64 context：删除 workaround 使用 label (#4127) (@devnexen)</li> 
</ul> 
<h3 style="text-align:left">测试</h3> 
<ul> 
 <li>添加 alpine 的构建脚本 (#4104) (@limingxinleo)</li> 
</ul>
                                        </div>
                                      
</div>
            