
---
title: '【得物技术】前端工程师要知道的Nginx知识'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/785d4058aafd4e23a7265863f1895e28~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 02 Apr 2021 02:16:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/785d4058aafd4e23a7265863f1895e28~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>平常我们在工作之中，遇到的许多问题其实都是与Nginx有关的问题，例如 跨域问题、请求过滤、配置gzip、负载均衡、或者与静态资源服务器有关等等的问题。</p>
<p>虽然nginx一般都由运维配置，我们不会直接配置，但是了解它在我们线上程序中所起到的作用，并且能够知道如何排查问题，也是非常重要的。</p>
<p>那么nginx到底是什么呢？</p>
<h1 data-id="heading-0">一、什么是Nginx</h1>
<p>Nginx是一款轻量级的Web服务器、反向代理服务器，由于它的内存占用少，启动极快，高并发能力强，在互联网项目中广泛应用。
<img alt="截屏2021-04-02 下午5.55.22.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/785d4058aafd4e23a7265863f1895e28~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>上图大概描述了Nginx在整个浏览访问中起到的作用，有一点像入口网关。Nginx其实就是一个高性能的反向代理服务器，那么什么是反向代理，什么是正向代理呢？</p>
<h2 data-id="heading-1">1. 正向代理</h2>
<p><img alt="截屏2021-04-02 下午5.55.48.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7fcf4ad9f884cc3a7dffc973c5ace55~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>由于防火墙的原因，我们不能直接访问www.google.com ,所以我们需要借助vpn来完成这次访问。通过这个例子，我们能发现，所谓的正向代理，代理的是客户端，客户端知道他访问的目标究竟是什么，但对于目标服务端来说，并不知道自己收到的是来自代理的访问还是来自真实客户端的访问。</p>
<p>官方解释如下：</p>
<blockquote>
<p>是一个位于客户端和原始服务器(origin server)之间的服务器，为了从原始服务器取得内容，客户端向代理发送一个请求并指定目标(原始服务器)，然后代理向原始服务器转交请求并将获得的内容返回给客户端。客户端才能使用正向代理。</p>
</blockquote>
<h2 data-id="heading-2">2. 反向代理</h2>
<p><img alt="截屏2021-04-02 下午5.56.51.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/356e7e59d3da433399a5ad4eaf4ea7cb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从图中我们可以看出，我们从外网访问www.baidu.com 的时候，会进行一个转发，代理到内网。因此反向代理其实代理的是服务器端，这一个过程对于客户端来说是透明的。</p>
<p>官方解释如下：</p>
<blockquote>
<p>反向代理服务器位于用户与目标服务器之间，但是对于用户而言，反向代理服务器就相当于目标服务器，即用户直接访问反向代理服务器就可以获得目标服务器的资源。</p>
</blockquote>
<h1 data-id="heading-3">二、Nginx的基本配置</h1>
<p>下图是nginx配置文件的基本结构：</p>
<p><img alt="截屏2021-04-02 下午5.57.34.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9528c00277ad410bb629c7cb3f79191e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>其中：</p>
<ul>
<li>main：nginx的全局配置，对全局生效</li>
<li>events：配置影响nginx服务器或与用户的网络连接</li>
<li>http：可以嵌套多个server，配置代理，缓存，日志定义等等功能，还能配置第三方模块的配置。</li>
<li>upstream：配置后端服务器的具体地址，与负载均衡息息相关</li>
<li>server：配置虚拟主机的相关参数，一个http中可以有多个server</li>
<li>location：配置请求的路由，以及各种页面的处理情况</li>
</ul>
<h2 data-id="heading-4">内置变量</h2>
<p><img alt="截屏2021-04-02 下午5.58.30.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/120e7e79923948969ffeb8682d91183e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">三、跨域问题</h1>
<h2 data-id="heading-6">1. 跨域的定义</h2>
<p>浏览器出于安全考虑，有同源策略。也就是说，如果协议、域名或者端口有一个不同就是跨域。</p>
<h2 data-id="heading-7">2. Nginx是怎么解决跨域</h2>
<p>eg.
• 前端server的域名：fast.dewu.com
• 后端server的域名：app.dewu.com</p>
<p>如果没有代理，那么在fast.dewu.com对app.dewu.com发起请求一定会产生跨域问题。</p>
<p>如果使Nginx用代理将serve_name设置成fast.dewu.com，然后设置相应的location拦截前端需要跨域的请求，最后将请求代理回app.dewu.com。配置如下：</p>
<pre><code class="copyable">&#123; 
    listen 80; 
    server_name fast.dewu.com; 
    location / &#123; 
        proxy_pass app.dewu.com; 
        &#125; 
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将这样fast.dewu.com访问nginx的fast.dewu.com属于同源访问，而nginx对服务端转发的请求不会触发浏览器的同源策略。</p>
<h1 data-id="heading-8">四、请求过滤</h1>
<h2 data-id="heading-9">1. 状态码过滤</h2>
<pre><code class="copyable">error_page 500 501 502 503 504 506 /50x.html; 
location = /50x.html &#123; 
  #将跟路径改编为存放html的路径。 
  root /root/static/html; 
&#125;
 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>50x就是错误状态码的显示页面，后面是存放具体html的地址。</p>
<h2 data-id="heading-10">2. 根据URL名称过滤</h2>
<pre><code class="copyable">location / &#123;
    rewrite  ^.*$ /index.html  redirect;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>rewrite的指令是这样的：</p>
<pre><code class="copyable">rewrite regex replacement [flag];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里使用了正则来匹配请求的url，如果匹配成功，则使用replacement来更改url。最后的redirect表示返回302临时重定向。</p>
<p>所以这里表示的是精准匹配URL，不匹配的URL全部重定向到主页。</p>
<h2 data-id="heading-11">3. 请求类型过滤</h2>
<pre><code class="copyable">if ( $request_method !~ ^(GET|POST|HEAD)$ ) &#123;
        return 403;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">五、配置gzip</h1>
<h2 data-id="heading-13">1. 什么是gzip</h2>
<p>gzip是GNUzip的缩写，最早用于UNIX系统的文件压缩。HTTP协议上的gzip编码是一种用来改进web应用程序性能的技术，web服务器和客户端（浏览器）必须共同支持gzip。目前主流的浏览器，Chrome,firefox,IE等都支持该协议。常见的服务器如Apache，Nginx，IIS同样支持gzip。</p>
<p>gzip压缩比率在3到10倍左右，可以大大节省服务器的网络带宽。而在实际应用中，并不是对所有文件进行压缩，通常只是压缩静态文件。</p>
<p><img alt="截屏2021-04-02 下午6.02.16.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92a3ceba526046059551f2b648708099~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">2. 开启gzip的表现</h2>
<p>请求头
<img alt="截屏2021-04-02 下午6.01.55.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a32276ad147f43f3a13ca8151a49cfac~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
响应头
<img alt="截屏2021-04-02 下午6.02.39.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aacecab24203450ba626fb2ac2d53437~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">3. nginx配置</h2>
<pre><code class="copyable">server&#123; 
gzip on; # 用于开启或 关闭gzip模块 
gzip_buffers 32 4K; # 设置系统获取几个单位的缓存用于存储gzip的压缩结果数据流。 
gzip_comp_level 6; # 压缩级别，1-10，数字越大压缩的越好，压缩级别越高压缩率越大，压缩时间越长。
gzip_min_length 100; # 设置允许压缩的页面最小字节数，页面字节数从相应消息头的Content-length中进行获取。
 
gzip_types application/javascript text/css text/xml; gzip_disable "MSIE [1-6]\."; # IE6对Gzip不友好，对Gzip（可以通过该指令对一些特定的User-Agent不使用压缩功能） 
gzip_proxied on: # 用于设置启用或禁用从代理服务器上收到相应内容gzip压缩。 
gzip_http_version 1.1; # 识别HTTP协议版本，其值可以是 1.1 或 1.0 
gzip_proxied : off; # 用于设置启用或禁用从代理服务器上收到相应内容gzip压缩。
gzip_vary on; # 用于在响应消息头中添加Vary：Accept-Encoding,使代理服务器根据请求头中的Accept-Encoding识别是否启用gzip压缩
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">六、负载均衡</h1>
<h2 data-id="heading-17">1. 什么是负载均衡</h2>
<p>负载均衡是高可用网络基础架构的关键组件，通常用于将工作负载分布到多个服务器来提高网站、应用、数据库或其他服务的性能和可靠性。</p>
<p>一个没有负载均衡的 web 架构类似下面这样：
<img alt="截屏2021-04-02 下午6.03.30.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d7c88a87eb84f18b5a961657de5052d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在这里用户是直连到 web 服务器，如果这个服务器宕机了，那么用户自然也就没办法访问了。另外，如果同时有很多用户试图访问服务器，超过了其能处理的极限，就会出现加载速度缓慢或根本无法连接的情况。</p>
<p>而通过在后端引入一个负载均衡器和至少一个额外的 web 服务器，可以缓解这个故障。通常情况下，所有的后端服务器会保证提供相同的内容，以便用户无论哪个服务器响应，都能收到一致的内容。</p>
<p><img alt="截屏2021-04-02 下午6.03.53.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a0cf710a85e45b698f250e69e060a6d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">2. nginx如何实现负载均衡</h2>
<p>Upstream指定后端服务器地址列表</p>
<pre><code class="copyable">upstream balanceServer &#123;
    server 10.1.22.33:12345;
    server 10.1.22.34:12345;
    server 10.1.22.35:12345;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在server中拦截响应请求，并将请求转发到Upstream中配置的服务器列表。</p>
<pre><code class="copyable">server &#123; 
      server_name fe.server.com; 
      listen 80; 
      location /api &#123; 
          proxy_pass http://balanceServer; 
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">3. 负载均衡的策略</h2>
<h3 data-id="heading-20">（1）轮询策略（默认）</h3>
<p>将所有客户端请求轮询分配给服务端。这种策略是可以正常工作的，但是如果其中某一台服务器压力太大，出现延迟，会影响所有分配在这台服务器下的用户。
代码如上。</p>
<p><img alt="截屏2021-04-02 下午6.04.54.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89b0d5d61f0a414fbca16129d7f34e25~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">(2) 最小连接数策略</h3>
<p>将请求优先分配给压力较小的服务器，它可以平衡每个队列的长度，并避免向压力大的服务器添加更多的请求。</p>
<pre><code class="copyable">upstream balanceServer &#123; 
  least_conn; 
  server 10.1.22.33:12345; 
  server 10.1.22.34:12345; 
  server 10.1.22.35:12345; 
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="截屏2021-04-02 下午6.05.28.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d635a392d24e412db9a422b2c1c184b7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-22">(3) 权重策略</h3>
<p>指定不同ip的权重，权重与访问比成正相关，权重越高，访问越大，适用于不同性能的机器。</p>
<pre><code class="copyable">upstream balanceServer &#123;
    server 192.168.0.1 weight=2;
    server 192.168.0.2 weight=8;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">(4) 客户端ip绑定 ip_hash</h3>
<p>来自同一个ip的请求永远只分配一台服务器，有效解决了动态网页存在的session共享问题。</p>
<pre><code class="copyable">upstream balanceServer &#123;
    ip_hash;
    server 10.1.22.33:12345;
    server 10.1.22.34:12345;
    server 10.1.22.35:12345;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">(5) 最快响应时间策略 fair（第三方）</h3>
<p>会将请求优先分配给相应最快的服务器，这种方式需要依赖到第三方插件 nginx-upstream-fair</p>
<pre><code class="copyable">upstream balanceServer &#123;
    fair;
    server 10.1.22.33:12345;
    server 10.1.22.34:12345;
    server 10.1.22.35:12345;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">(6) url_hash（第三方）</h3>
<p>按访问url的hash结果来分配请求，使每个url定向到同一个后端服务器，后端服务器为缓存时比较有效。</p>
<pre><code class="copyable">upstream balanceServer &#123; 
  hash $request_uri; 
  server 192.168.244.1:8080; 
  server 192.168.244.2:8080; 
  server 192.168.244.3:8080; 
  server 192.168.244.4:8080; 
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-26">4. 健康检查</h2>
<p>Nginx 自带 ngx_http_upstream_module（健康检测模块）本质上服务器心跳的检查，通过定期轮询向集群里的服务器发送健康检查请求,来检查集群中是否有服务器处于异常状态。</p>
<p>如果检测出其中某台服务器异常,那么在通过客户端请求nginx反向代理进来的都不会被发送到该服务器上（直至下次轮训健康检查正常）。</p>
<pre><code class="copyable">upstream balanceServer&#123; 
  server 192.168.0.1 max_fails=1 fail_timeout=40s; 
  server 192.168.0.2 max_fails=1 fail_timeout=40s; 
  &#125; 
  
server &#123;  
  listen 80; 
  server_name localhost; 
  location / &#123; 
    proxy_pass http://balanceServer; 
  &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>涉及两个配置： fail_timeout : 设定服务器被认为不可用的时间段以及统计失败尝试次数的时间段，默认为10s max_fails : 设定Nginx与服务器通信的尝试失败的次数，默认为：1次。</p>
<h1 data-id="heading-27">七、静态资源服务器</h1>
<pre><code class="copyable">location ~* \.(png|gif|jpg|jpeg)$ &#123; 
  root  /root/static/; 
  autoindex on; 
  access_log off; 
  expires 10h;# 设置过期时间为10小时 
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>匹配以png|gif|jpg|jpeg为结尾的请求，并将请求转发到本地路径，root中指定的路径即nginx本地路径。同时也可以进行一些缓存的设置。</p>
<h1 data-id="heading-28">八、访问权限控制</h1>
<p>可以配置 nginx 白名单，规定哪些ip可以访问服务器。</p>
<pre><code class="copyable">location / &#123;
        allow  192.168.0.1;  # 允许该ip访问
        deny   all;  # 禁止所有
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文｜衠灵</p>
<p>关注得物技术，携手走向技术的云端</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            