
---
title: 'Swoole v4.6.7 版本发布，Bug 修复版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1062'
author: 开源中国
comments: false
date: Fri, 14 May 2021 18:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1062'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fswoole%2Fswoole-src%2Freleases%2Ftag%2Fv4.6.7" target="_blank">v4.6.7</a> 版本主要是一个 Bug 修复版本，没有向下不兼容改动。</p> 
<p style="text-align:left">此版本中修复了<code>Http\Response::end()</code>方法总是返回 <code>true</code> 的问题，同时修改了 <code>output_buffer_size</code> 的默认值</p> 
<p style="text-align:left">在之前的版本中 <code>output_buffer_size</code> 的默认值为<code>2M</code>，由于受到 <code>output_buffer_size</code> 的限制，如果在调用<code>end</code>时，需要发送的内容大于这个限制则会响应失败，并抛出如下错误：</p> 
<pre style="text-align:left"><code><strong>use</strong> <strong>Swoole</strong>\<strong>Http</strong>\<strong>Server</strong>;
<strong>use</strong> <strong>Swoole</strong>\<strong>Http</strong>\<strong>Request</strong>;
<strong>use</strong> <strong>Swoole</strong>\<strong>Http</strong>\<strong>Response</strong>;

<span style="color:teal">$http</span> = <strong>new</strong> Server(<span style="color:#dd1144">'127.0.0.1'</span>, <span style="color:teal">9501</span>);

<span style="color:teal">$http</span>->set([
    <span style="color:#dd1144">'http_compression'</span> => <span style="color:teal">false</span>,
    <span style="color:#dd1144">'buffer_output_size'</span> => <span style="color:teal">128</span> * <span style="color:teal">1024</span>,
]);

<span style="color:teal">$http</span>->on(<span style="color:#dd1144">'request'</span>, <strong>function</strong> (Request <span style="color:teal">$request</span>, Response <span style="color:teal">$response</span>) &#123;
    assert(<span style="color:teal">$response</span>->end(str_repeat(<span style="color:#dd1144">'A'</span>, <span style="color:teal">256</span> * <span style="color:teal">1024</span>)) === <span style="color:teal">false</span>);
    assert(swoole_last_error() === SWOOLE_ERROR_DATA_LENGTH_TOO_LARGE);
&#125;);

<span style="color:teal">$http</span>->start();</code></pre> 
<blockquote>
 使用以上代码即可复现该错误
</blockquote> 
<pre style="text-align:left"><code>WARNING finish (ERRNO 1203): The length of data [262144] exceeds the output buffer size[131072], please use the sendfile, chunked transfer mode or adjust the output_buffer_size</code></pre> 
<p style="text-align:left">以前的解决方法为：使用 <code>sendfile</code>、<code>write</code> 或调整 <code>output_buffer_size</code>，而此版本中将<code>output_buffer_size</code>的默认值提高到了无符号 INT 最大值(<code>UINT_MAX</code>)</p> 
<p style="text-align:left">从 4.5 版本开始去掉了 Worker 进程共享内存的使用，改为了全部使用 <code>UnixSocket</code> 管道，所以不再需要预先分配内存。<code>output_buffer_size</code> 参数只是一个限制，设置为比较大的参数也不会导致额外占用内存。</p> 
<p style="text-align:left">同时还修复了<code>end</code>的返回值一直是<code>true</code>的问题，以上代码中产生错误后未成功响应，返回值为<code>false</code></p> 
<h2 style="text-align:left">更新日志</h2> 
<p style="text-align:left">下面是完整的更新日志：</p> 
<h3 style="text-align:left">增强</h3> 
<ul> 
 <li>Manager 进程和 Task 同步进程支持调用<code>Process::signal()</code>函数 (#4190) (@matyhtf)</li> 
</ul> 
<h3 style="text-align:left">修复</h3> 
<ul> 
 <li>修复信号不能被重复注册的问题 (#4170) (@matyhtf)</li> 
 <li>修复在 OpenBSD/NetBSD 上编译失败的问题 (#4188) (#4194) (@devnexen)</li> 
 <li>修复监听可写事件时特殊情况 onClose 事件丢失 (#4204) (@matyhtf)</li> 
 <li>修复 Symfony HttpClient 使用 native curl 的问题 (#4204) (@matyhtf)</li> 
 <li>修复<code>Http\Response::end()</code>方法总是返回 true 的问题 (swoole/swoole-src@66fcc35) (@matyhtf)</li> 
 <li>修复 PDOStatementProxy 产生的 PDOException (swoole/library#104) (@twose)</li> 
</ul> 
<h3 style="text-align:left">内核</h3> 
<ul> 
 <li>重构 worker buffer，给 event data 加上 msg id 标志 (#4163) (@matyhtf)</li> 
 <li>修改 Request Entity Too Large 日志等级为 warning 级别 (#4175) (@sy-records)</li> 
 <li>替换 inet_ntoa and inet_aton 函数 (#4199) (@remicollet)</li> 
 <li>修改 output_buffer_size 默认值为 UINT_MAX (swoole/swoole-src@46ab345) (@matyhtf)</li> 
</ul>
                                        </div>
                                      
</div>
            