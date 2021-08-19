
---
title: 'Swoole v4.7.1 版本发布，Bug 修复版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=81'
author: 开源中国
comments: false
date: Thu, 19 Aug 2021 09:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=81'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttps%253A%252F%252Fgithub.com%252Fswoole%252Fswoole-src%252Freleases%252Ftag%252Fv4.7.1" target="_blank">v4.7.1</a> 版本主要是一个 Bug 修复版本，没有向下不兼容改动。</p> 
<ul> 
 <li>兼容了 PHP 8.1 版本</li> 
 <li>为<code>SWOOLE_HOOK_CURL</code>支持了<code>CURLOPT_RESOLVE</code>选项</li> 
</ul> 
<p style="text-align:left">支持了形如<code>HOST:PORT:ADDRESS</code>、<code>[+]HOST:PORT:ADDRESS</code>、<code>[-]HOST:PORT:ADDRESS</code>和多地址的格式</p> 
<pre style="text-align:left"><span style="color:#d73a49">use</span> <span style="color:#6f42c1">Swoole</span>\<span style="color:#6f42c1">Coroutine</span>;
<span style="color:#d73a49">use</span> <span style="color:#6f42c1">Swoole</span>\<span style="color:#6f42c1">Runtime</span>;

Runtime::enableCoroutine(SWOOLE_HOOK_CURL);
Coroutine\run(<span style="color:#d73a49">function</span> () &#123;
    <span style="color:#005cc5">$host</span> = <span style="color:#032f62">'httpbin.org'</span>;
    <span style="color:#005cc5">$url</span> = <span style="color:#032f62">'https://httpbin.org/get'</span>;
    <span style="color:#005cc5">$ip</span> = Coroutine::gethostbyname(<span style="color:#005cc5">$host</span>);
    <span style="color:#005cc5">$ch</span> = curl_init();

    curl_setopt(<span style="color:#005cc5">$ch</span>, CURLOPT_URL, <span style="color:#005cc5">$url</span>);
    curl_setopt(<span style="color:#005cc5">$ch</span>, CURLOPT_RETURNTRANSFER, <span style="color:#005cc5">1</span>);
    curl_setopt(<span style="color:#005cc5">$ch</span>, CURLOPT_RESOLVE, [<span style="color:#032f62">"<span style="color:#24292e">&#123;$host&#125;</span>:443:127.0.0.1"</span>, <span style="color:#032f62">"<span style="color:#24292e">&#123;$host&#125;</span>:443:<span style="color:#24292e">&#123;$ip&#125;</span>"</span>]);

    <span style="color:#005cc5">$data</span> = curl_exec(<span style="color:#005cc5">$ch</span>);
    <span style="color:#005cc5">$httpPrimaryIp</span> = curl_getinfo(<span style="color:#005cc5">$ch</span>, CURLINFO_PRIMARY_IP);
    <span style="color:#005cc5">$body</span> = json_decode(<span style="color:#005cc5">$data</span>, <span style="color:#005cc5">true</span>);
    assert(<span style="color:#005cc5">$body</span>[<span style="color:#032f62">'headers'</span>][<span style="color:#032f62">'Host'</span>] === <span style="color:#032f62">'httpbin.org'</span>);
    assert(<span style="color:#005cc5">$body</span>[<span style="color:#032f62">'url'</span>] === <span style="color:#005cc5">$url</span>);
    assert(<span style="color:#005cc5">$ip</span> === <span style="color:#005cc5">$httpPrimaryIp</span>);
&#125;);</pre> 
<h2 style="text-align:left">更新日志</h2> 
<p style="text-align:left">下面是完整的更新日志：</p> 
<h3 style="text-align:left">增强</h3> 
<ul> 
 <li><code>System::dnsLookup</code> 支持查询 <code>/etc/hosts</code> (#4341) (#4349) (@zmyWL) (@NathanFreeman)</li> 
 <li>增加对 mips64 的 boost context 支持 (#4358) (@dixyes)</li> 
 <li><code>SWOOLE_HOOK_CURL</code> 支持 <code>CURLOPT_RESOLVE</code> 选项 (swoole/library#107) (@sy-records)</li> 
 <li><code>SWOOLE_HOOK_CURL</code> 支持 <code>CURLOPT_NOPROGRESS</code> 选项 (swoole/library#117) (@sy-records)</li> 
 <li>增加对 riscv64 的 boost context 支持 (#4375) (@dixyes)</li> 
</ul> 
<h3 style="text-align:left">修复</h3> 
<ul> 
 <li>修复 PHP-8.1 在 on shutdown 时产生的内存错误 (#4325) (@twose)</li> 
 <li>修复 8.1.0beta1 的不可序列化类 (#4335) (@remicollet)</li> 
 <li>修复多个协程递归创建目录失败的问题 (#4337) (@NathanFreeman)</li> 
 <li>修复 native curl 在外网发送大文件偶发超时的问题，以及在 CURL WRITEFUNCTION 中使用协程文件 API 出现 crash 的问题 (#4360) (@matyhtf)</li> 
 <li>修复 <code>PDOStatement::bindParam()</code> 期望参数 1 为字符串的问题 (swoole/library#116) (@sy-records)</li> 
</ul>
                                        </div>
                                      
</div>
            