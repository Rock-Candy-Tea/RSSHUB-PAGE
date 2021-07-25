
---
title: 'nginx如何限流'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/472d1e9adbac4d0f9665cef5db3bb476~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 00:38:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/472d1e9adbac4d0f9665cef5db3bb476~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>流量限制(rate-limiting)，是Nginx中一个非常实用，却经常被错误理解和错误配置的功能。我们可以用来限制用户在给定时间内HTTP请求的数量。请求，可以是一个简单网站首页的GET请求，也可以是登录表单的POST请求。</p>
<p>流量限制可以用作安全目的，比如可以减慢暴力密码破解的速率。通过将传入请求的速率限制为真实用户的典型值，并标识目标URL地址(通过日志)，还可以用来抵御DDOS攻击。更常见的情况，该功能被用来保护上游应用服务器不被同时太多用户请求所压垮。</p>
<p>本篇文章将会介绍Nginx的 流量限制 的基础知识和高级配置，”流量限制”在Nginx Plus中也适用。</p>
<h3 data-id="heading-0">Nginx如何限流</h3>
<p>Nginx的”流量限制”使用漏桶算法(leaky bucket algorithm)，该算法在通讯和分组交换计算机网络中广泛使用，用以处理带宽有限时的突发情况。就好比，一个桶口在倒水，桶底在漏水的水桶。如果桶口倒水的速率大于桶底的漏水速率，桶里面的水将会溢出；同样，在请求处理方面，水代表来自客户端的请求，水桶代表根据”先进先出调度算法”(FIFO)等待被处理的请求队列，桶底漏出的水代表离开缓冲区被服务器处理的请求，桶口溢出的水代表被丢弃和不被处理的请求。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/472d1e9adbac4d0f9665cef5db3bb476~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">配置基本的限流</h3>
<p>“流量限制”配置两个主要的指令，limit_req_zone和limit_req，如下所示：
limit_req_zone $binary_remote_addr zone=mylimit:10m rate=10r/s;</p>
<p>server &#123;
location /login/ &#123;
limit_req zone=mylimit;</p>
<pre><code class="copyable">    proxy_pass http://my_upstream;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>limit_req_zone指令定义了流量限制相关的参数，而limit_req指令在出现的上下文中启用流量限制(示例中，对于”/login/”的所有请求)。limit_req_zone指令通常在HTTP块中定义，使其可在多个上下文中使用，它需要以下三个参数：</p>
<pre><code class="copyable">Key - 定义应用限制的请求特性。示例中的Nginx变量remote_addr，占用更少的空间)
Zone - 定义用于存储每个IP地址状态以及被限制请求URL访问频率的共享内存区域。保存在内存共享区域的信息，意味着可以在Nginx的worker进程之间共享。定义分为两个部分：通过zone=keyword标识区域的名字，以及冒号后面跟区域大小。16000个IP地址的状态信息，大约需要1MB，所以示例中区域可以存储160000个IP地址。
Rate - 定义最大请求速率。在示例中，速率不能超过每秒10个请求。Nginx实际上以毫秒的粒度来跟踪请求，所以速率限制相当于每100毫秒1个请求。因为不允许”突发情况”(见下一章节)，这意味着在前一个请求100毫秒内到达的请求将被拒绝。

当Nginx需要添加新条目时存储空间不足，将会删除旧条目。如果释放的空间仍不够容纳新记录，Nginx将会返回 503状态码(Service Temporarily Unavailable)。另外，为了防止内存被耗尽，Nginx每次创建新条目时，最多删除两条60秒内未使用的条目。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>limit_req_zone指令设置流量限制和共享内存区域的参数，但实际上并不限制请求速率。所以需要通过添加limit_req指令，将流量限制应用在特定的location或者server块。在上面示例中，我们对/login/请求进行流量限制。</p>
<p>现在每个IP地址被限制为每秒只能请求10次/login/，更准确地说，在前一个请求的100毫秒内不能请求该URL。
处理突发</p>
<p>如果我们在100毫秒内接收到2个请求，怎么办？对于第二个请求，Nginx将给客户端返回状态码503。这可能并不是我们想要的结果，因为应用本质上趋向于突发性。相反地，我们希望缓冲任何超额的请求，然后及时地处理它们。我们更新下配置，在limit_req中使用burst参数：</p>
<p>location /login/ &#123;
limit_req zone=mylimit burst=20;
proxy_pass http://my_upstream;
&#125;</p>
<p>burst参数定义了超出zone指定速率的情况下(示例中的mylimit区域，速率限制在每秒10个请求，或每100毫秒一个请求)，客户端还能发起多少请求。上一个请求100毫秒内到达的请求将会被放入队列，我们将队列大小设置为20。</p>
<p>这意味着，如果从一个给定IP地址发送21个请求，Nginx会立即将第一个请求发送到上游服务器群，然后将余下20个请求放在队列中。然后每100毫秒转发一个排队的请求，只有当传入请求使队列中排队的请求数超过20时，Nginx才会向客户端返回503。
无延迟的排队</p>
<p>配置burst参数将会使通讯更流畅，但是可能会不太实用，因为该配置会使站点看起来很慢。在上面的示例中，队列中的第20个包需要等待2秒才能被转发，此时返回给客户端的响应可能不再有用。要解决这个情况，可以在burst参数后添加nodelay参数：</p>
<p>location /login/ &#123;
limit_req zone=mylimit burst=20 nodelay;</p>
<pre><code class="copyable">proxy_pass http://my_upstream;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>使用nodelay参数，Nginx仍将根据burst参数分配队列中的位置，并应用已配置的速率限制，而不是清理队列中等待转发的请求。相反地，当一个请求到达“太早”时，只要在队列中能分配位置，Nginx将立即转发这个请求。将队列中的该位置标记为”taken”(占据)，并且不会被释放以供另一个请求使用，直到一段时间后才会被释放(在这个示例中是，100毫秒后)。</p>
<p>假设如前所述，队列中有20个空位，从给定的IP地址发出的21个请求同时到达。Nginx会立即转发这个21个请求，并且标记队列中占据的20个位置，然后每100毫秒释放一个位置。如果是25个请求同时到达，Nginx将会立即转发其中的21个请求，标记队列中占据的20个位置，并且返回503状态码来拒绝剩下的4个请求。</p>
<p>现在假设，第一组请求被转发后101毫秒，另20个请求同时到达。队列中只会有一个位置被释放，所以Nginx转发一个请求并返回503状态码来拒绝其他19个请求。如果在20个新请求到达之前已经过去了501毫秒，5个位置被释放，所以Nginx立即转发5个请求并拒绝另外15个。</p>
<p>效果相当于每秒10个请求的“流量限制”。如果希望不限制两个请求间允许间隔的情况下实施“流量限制”，nodelay参数是很实用的。</p>
<p>注意：对于大部分部署，我们建议使用burst和nodelay参数来配置limit_req指令。
高级配置示例</p>
<p>通过将基本的“流量限制”与其他Nginx功能配合使用，我们可以实现更细粒度的流量限制。</p>
<p>白名单</p>
<p>下面这个例子将展示，如何对任何不在白名单内的请求强制执行“流量限制”：</p>
<p>geo $limit &#123;
default         1;
10.0.0.0/8         0;
192.168.0.0/64     0;
&#125;</p>
<p>map <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>l</mi><mi>i</mi><mi>m</mi><mi>i</mi><mi>t</mi></mrow><annotation encoding="application/x-tex">limit </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">i</span><span class="mord mathnormal">m</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span></span></span></span></span>limit_key &#123;
0 "";
1 $binary_remote_addr;
&#125;</p>
<p>limit_req_zone $limit_key zone=req_zone:10m rate=5r/s;</p>
<p>server &#123;
location / &#123;
limit_req zone=req_zone burst=10 nodelay;</p>
<pre><code class="copyable">    # ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>这个例子同时使用了geo和map指令。geo块将给在白名单中的IP地址对应的$limit变量分配一个值0，给其它不在白名单中的分配一个值1。然后我们使用一个映射将这些值转为key，如下：</p>
<pre><code class="copyable">如果
<span class="copy-code-btn">复制代码</span></code></pre>
<p>变量的值是
，limit_key变量将被赋值为空字符串
如果
变量的值是</p>
<pre><code class="copyable">，limit_key变量将被赋值为客户端二进制形式的IP地址 两个指令配合使用，白名单内IP地址的$limit_key变量被赋值为空字符串，不在白名单内的被赋值为客户端的IP地址。当limit_req_zone后的第一个参数是空字符串时，不会应用“流量限制”，所以白名单内的IP地址(10.0.0.0/8和192.168.0.0/24 网段内)不会被限制。其它所有IP地址都会被限制到每秒5个请求。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>limit_req指令将限制应用到/的location块，允许在配置的限制上最多超过10个数据包的突发，并且不会延迟转发。
location包含多limit_req指令</p>
<p>我们可以在一个location块中配置多个limit_req指令。符合给定请求的所有限制都被应用时，意味着将采用最严格的那个限制。例如，多个指令都制定了延迟，将采用最长的那个延迟。同样，请求受部分指令影响被拒绝，即使其他指令允许通过也无济于事。</p>
<p>扩展前面将“流量限制”应用到白名单内IP地址的例子：</p>
<p>http &#123;
# ...</p>
<pre><code class="copyable">limit_req_zone $limit_key zone=req_zone:10m rate=5r/s;
limit_req_zone $binary_remote_addr zone=req_zone_wl:10m rate=15r/s;

server &#123;
    # ...
    location / &#123;
        limit_req zone=req_zone burst=10 nodelay;
        limit_req zone=req_zone_wl burst=20 nodelay;
        # ...
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>白名单内的IP地址不会匹配到第一个“流量限制”，而是会匹配到第二个req_zone_wl，并且被限制到每秒15个请求。不在白名单内的IP地址两个限制能匹配到，所以应用限制更强的那个：每秒5个请求。
配置相关功能</p>
<p>日志记录 默认情况下，Nginx会在日志中记录由于流量限制而延迟或丢弃的请求，如下所示：</p>
<p>2015/06/13 04:20:00 [error] 120315#0: *32086 limiting requests, excess: 1.000 by zone "mylimit", client: 192.168.1.2, server: nginx.com, <br>request: "GET / HTTP/1.0", host: "nginx.com"</p>
<p>日志条目中包含的字段：</p>
<pre><code class="copyable">limiting requests - 表明日志条目记录的是被“流量限制”请求
excess - 每毫秒超过对应“流量限制”配置的请求数量
zone - 定义实施“流量限制”的区域
client - 发起请求的客户端IP地址
server - 服务器IP地址或主机名
request - 客户端发起的实际HTTP请求
host - HTTP报头中host的值
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认情况下，Nginx以error级别来记录被拒绝的请求，如上面示例中的[error]所示(Ngin以较低级别记录延时请求，一般是info级别)。如要更改Nginx的日志记录级别，需要使用limit_req_log_level指令。这里，我们将被拒绝请求的日志记录级别设置为warn：</p>
<p>location /login/ &#123;
limit_req zone=mylimit burst=20 nodelay;
limit_req_log_level warn;</p>
<pre><code class="copyable">proxy_pass http://my_upstream;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>发送到客户端的错误代码</p>
<p>一般情况下，客户端超过配置的流量限制时，Nginx响应状态码为503(Service Temporarily Unavailable)。可以使用limit_req_status指令来设置为其它状态码(例如下面的444状态码):</p>
<p>location /login/ &#123;
limit_req zone=mylimit burst=20 nodelay;
limit_req_status 444;
&#125;</p>
<p>指定location拒绝所有请求</p>
<p>如果你想拒绝某个指定URL地址的所有请求，而不是仅仅对其限速，只需要在location块中配置deny all指令：</p>
<p>location /foo.php &#123;
deny all;
&#125;</p>
<p>总结</p>
<p>前文已经涵盖了Nginx和Nginx Plus提供的“流量限制”的很多功能，包括为HTTP请求的不同loation设置请求速率，给“流量限制”配置burst和nodelay参数。还涵盖了针对客户端IP地址的白名单和黑名单应用不同“流量限制”的高级配置，阐述了如何去日志记录被拒绝和延时的请求。</p>
<p>END</p></div>  
</div>
            