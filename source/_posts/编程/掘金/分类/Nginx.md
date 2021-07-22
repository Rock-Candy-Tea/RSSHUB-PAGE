
---
title: 'Nginx'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2e1441a779d4e7bbf0172ef8767c3ec~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 22:15:14 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2e1441a779d4e7bbf0172ef8767c3ec~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">主要功能</h1>
<ol>
<li>负载均衡</li>
<li>反向代理</li>
<li>动静分离</li>
<li>配置https</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2e1441a779d4e7bbf0172ef8767c3ec~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">一、负载均衡</h2>
<p>负载均衡是一门计算机网络技术，主要用来优化资源使用、最大化吞吐率、最小化响应时间、同时避免过载的目的。<br>
如果一个网站只有一台服务器的话，如果这台服务器宕机了，那么整个网站将无法正常访问。当访问网站人数过多，并发量达到一定规模，超过服务器性能的极限，整个网站也将无法访问。而负载均衡就是用来解决这一类的问题。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cee3c940e4c4bc7b27b2cb72c820456~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
负载均衡是通过后端引入一个负载均衡器和至少一个额外的web服务器来缓解这类问题(增加的web服务器和原本的web服务器提供相同的内容)。用户访问的时候，先访问到负载均衡器，再通过负载均衡器将请求转发给后台服务器。
通过这种方法，当有一台服务器宕机时，负载均衡器就分配其他的服务器给用户，极大的增加的网站的稳定性。</p>
<p>负载均衡器主要可以转发http、https、tcp、udp四种请求规则<br>
负载均衡器如何给用户分配服务器？ 负载均衡器有多种负载均衡算法，基本就是给每台服务器一个不同的权重，通过权重来给用户分配服务器。<br>
负载均衡不需要前端进行配置，主要是服务端进行配置，前端稍作了解即可。</p>
<h4 data-id="heading-2">1.1 负载均衡的几种常用方式</h4>
<ul>
<li>轮询（默认）</li>
</ul>
<pre><code class="copyable">// nginx.config
upstream backserver &#123;
    server 192.168.0.1;
    server 192.168.0.2;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>权重weight</li>
</ul>
<blockquote>
<p>❝</p>
<p>指定不同ip的权重，权重与访问比成正相关，权重越高，访问越大，适用于不同性能的机器</p>
<p>❞</p>
</blockquote>
<pre><code class="copyable">// nginx.config
upstream backserver &#123;
    server 192.168.0.1 weight=2;
    server 192.168.0.2 weight=8;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>响应时间来分配</li>
</ul>
<blockquote>
<p>❝</p>
<p>公平竞争，谁相应快，谁处理，不过这种方式需要依赖到第三方插件nginx-upstream-fair，需要先安装</p>
<p>❞</p>
</blockquote>
<pre><code class="copyable">// nginx.config
upstream backserver &#123;
    server 192.168.0.1;
    server 192.168.0.2;
    fair;
&#125;

server &#123;
    listen 80;
    server_name localhost; 
    location / &#123;
      proxy_pass  http://backserver;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">1.2 健康检查</h4>
<blockquote>
<p>❝</p>
<p>Nginx 自带 ngx_http_upstream_module（健康检测模块）本质上服务器心跳的检查，通过定期轮询向集群里的服务器发送健康检查请求,来检查集群中是否有服务器处于异常状态</p>
<p>❞</p>
</blockquote>
<p>如果检测出其中某台服务器异常,那么在通过客户端请求nginx反向代理进来的都不会被发送到该服务器上（直至下次轮训健康检查正常）</p>
<p>基本例子如下👇</p>
<pre><code class="copyable">upstream backserver&#123;
    server 192.168.0.1  max_fails=1 fail_timeout=40s;
    server 192.168.0.2  max_fails=1 fail_timeout=40s;
&#125;

server &#123;
    listen 80;
    server_name localhost; 
    location / &#123;
      proxy_pass http://backend;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>涉及两个配置：</p>
<ul>
<li>fail_timeout : 设定服务器被认为不可用的时间段以及统计失败尝试次数的时间段，默认为10s</li>
<li>max_fails : 设定Nginx与服务器通信的尝试失败的次数，默认为：1次</li>
</ul>
<h2 data-id="heading-4">二、反向代理</h2>
<p>反向代理是前端经常会用到的一项功能，主要是为了解决浏览器跨域访问的问题。当协议、域名、端口号有一项或多项不同时，便违反了同源策略，需要跨域。前端跨域用的较多的有：</p>
<h4 data-id="heading-5">2.1 jsonp跨域：</h4>
<p>使用html的script标签可以引入第三方的js文件，所以我们可以通过</p>
<pre><code class="copyable"><script src="http://后台接口"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来绕过跨域的限制。但是需要注意的是，jsonp只支持get请求。</p>
<h4 data-id="heading-6">2.2 webpack反向代理：</h4>
<p>前端开发中，基于webpack配置环境的spa页面已经是一种趋势，webpack内置的proxy可以帮助我们在开发环境调试接口时将我们的地址代理到后台服务地址，解决跨域问题。配置如下</p>
<pre><code class="copyable">        proxyTable: &#123;
            '/api': &#123;
                target: 'http://192.168.xxx.xxx:8080',
                changeOrigin: true
            &#125;
        &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码的含义就是，当前端访问接口匹配到'/api'时，将代理到'<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttp%253A%252F%252F192.168.xxx.xxx" target="_blank" rel="nofollow noopener noreferrer" title="https://link.segmentfault.com/?url=http%3A%2F%2F192.168.xxx.xxx" ref="nofollow noopener noreferrer">192.168.xxx.xxx</a>:8080'服务端地址，如果前台的接口名为/api/restful，代理的请求路径将是'<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttp%253A%252F%252F192.168.xxx.xxx" target="_blank" rel="nofollow noopener noreferrer" title="https://link.segmentfault.com/?url=http%3A%2F%2F192.168.xxx.xxx" ref="nofollow noopener noreferrer">192.168.xxx.xxx</a>:8080/api/restful'。</p>
<h4 data-id="heading-7">2.3 使用nginx进行反向代理</h4>
<p>前端开发完成，对代码进行打包后，webpack就无法使用了。这个时候我们手里只有html、css、js等静态文件，后台接口地址都会访问不到。这个时候nginx就登场了，nginx反向代理配置和webpack大同小异，匹配到动态的地址时将请求转发到一个服务器地址实现跨域。</p>
<blockquote>
<p>反向代理指的是，当一个客户端发送的请求,想要访问服务器上的内容，但将被该请求先发送到一个代理服务器proxy,这个代理服务器（Nginx）将把请求代理到和自己属于同一个局域网下的内部服务器上,而用户通过客户端真正想获得的内容就存储在这些内部服务器上，此时Nginx代理服务器承担的角色就是一个中间人，起到分配和沟通的作用</p>
</blockquote>
<h5 data-id="heading-8">2.3.1 为什么需要反向代理</h5>
<p>反向代理的优势主要有以下两点</p>
<ul>
<li>防火墙作用</li>
</ul>
<p>当你的应用不想直接暴露给客户端（也就是客户端无法直接通过请求访问真正的服务器，只能通过Nginx），通过nginx过滤掉没有权限或者非法的请求，来保障内部服务器的安全</p>
<ul>
<li>负载均衡</li>
</ul>
<p>也就上一章提到负载均衡，本质上负载均衡就是反向代理的一种应用场景，可以通过nginx将接收到的客户端请求"均匀地"分配到这个集群中所有的服务器上(具体看负载均衡方式),从而实现服务器压力的负载均衡</p>
<h5 data-id="heading-9">2.3.2 如何使用反向代理</h5>
<blockquote>
<p>我们通过模拟内部服务器的端口启动的nodejs项目设置反向代理到80端口访问</p>
</blockquote>
<p>具体流程如下：</p>
<h6 data-id="heading-10">1) 访问<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttp%253A%252F%252Fnginx.org%252F" target="_blank" rel="nofollow noopener noreferrer" title="https://link.segmentfault.com/?url=http%3A%2F%2Fnginx.org%2F" ref="nofollow noopener noreferrer">nginx官网</a>，下载nginx到本地</h6>
<h6 data-id="heading-11">2) 将打包完成的代码放置在nginx的html目录下</h6>
<h6 data-id="heading-12">3) 打开conf文件夹下的nginx.conf文件，配置如下：</h6>
<pre><code class="copyable">server &#123;
    listen       3000;    //监听的本地端口
    server_name  localhost;    
                
    location /api &#123;         //匹配到/api开头的接口时，转发到下面的服务器地址
        root   html;  
        proxy_pass  http://192.168.xxx.xxx:8080;    //服务器地址      
    &#125;  
                        
    location =/ &#123;
        root html;
        index  index.htm  index.html;   //默认主页
    &#125;
                        
    # 所有静态请求都由nginx处理，存放目录为html  
    location ~ .(htm|html|js|css|jpg|png|gif|eot|svg|ttf|woff|woff2)$ &#123;  
        root    html;      //配置静态资源地址
    &#125;    
                
    error_page   500 502 503 504  /50x.html;
        location = /50x.html &#123;
        root   html;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Nginx 反向代理是，会通过 location 功能匹配指定的 URI，然后把接收到的符合匹配 URI的请求通过 proxy_pass 转移给之前定义好的 upstream 节点池</p>
<h2 data-id="heading-13">三、配置https</h2>
<p>微信小程序现在越来越火，大批前端开发进军微信小程序，但是微信小程序只支持https请求，这是一个问题。</p>
<p>Nginx 常用来配置Https认证，主要有两个步骤：签署第三方可信任的 SSL 证书 和 配置 HTTPS。</p>
<h4 data-id="heading-14">配置https具体流程：</h4>
<h6 data-id="heading-15">1) 申请证书：</h6>
<p>配置 HTTPS 要用到私钥 example.key 文件和 example.crt 证书文件，而申请证书文件的时候要用到 example.csr 文件。对于想了解更多关于SSL证书的点这里 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fproduct%2Fssl%2Ffaqs" title="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fproduct%2Fssl%2Ffaqs" target="_blank">SSL证书介绍</a></p>
<h6 data-id="heading-16">2) 申请完成后下载nginx版本的证书至本地，一个crt文件一个key文件，crt为证书，key为密钥</h6>
<h6 data-id="heading-17">3) Nginx配置https</h6>
<pre><code class="copyable">server &#123;
    listen       443 ssl;    //监听443端口，因为443端口是https的默认端口。
                               80为http的默认端口
    server_name  www.domain.com;    //配置域名
    #证书文件    
    ssl_certificate      证书的绝对路径;
    #私钥文件
    ssl_certificate_key  密钥的绝对路径;
                
    # location / &#123;        //反向代理的服务器地址，视情况进行配置
    #    proxy_pass   http://112.35.xxx.xxx;
    # &#125;          
&#125;   
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">总结整个过程</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71d602236eff48919c186802cf8a40ae~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-19">1.用户输入<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttp%253A%252F%252F%2525E5%25259F%25259F%2525E5%252590%25258D" target="_blank" rel="nofollow noopener noreferrer" title="https://link.segmentfault.com/?url=http%3A%2F%2F%25E5%259F%259F%25E5%2590%258D" ref="nofollow noopener noreferrer">http://域名</a>，默认80端口</h6>
<h6 data-id="heading-20">2.nginx监听到80端口被访问，匹配到域名为www.dream.com，将服务代理到<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttp%253A%252F%252F192.168.3.10" target="_blank" rel="nofollow noopener noreferrer" title="https://link.segmentfault.com/?url=http%3A%2F%2F192.168.3.10" ref="nofollow noopener noreferrer">http://192.168.3.10</a>:8080</h6>
<h6 data-id="heading-21">3.服务器返回页面资源</h6>
<h6 data-id="heading-22">4.用户输入<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttps%253A%252F%252F%2525E4%2525BA%25258C%2525E7%2525BA%2525A7%2525E5%25259F%25259F%2525E5%252590%25258D%252C%2525E9%2525BB%252598%2525E8%2525AE%2525A4%2525E7%2525AB%2525AF%2525E5%25258F%2525A3%2525E4%2525B8%2525BA443" target="_blank" rel="nofollow noopener noreferrer" title="https://link.segmentfault.com/?url=https%3A%2F%2F%25E4%25BA%258C%25E7%25BA%25A7%25E5%259F%259F%25E5%2590%258D%2C%25E9%25BB%2598%25E8%25AE%25A4%25E7%25AB%25AF%25E5%258F%25A3%25E4%25B8%25BA443" ref="nofollow noopener noreferrer">https://二级域名,默认端口为443</a></h6>
<h6 data-id="heading-23">5.nginx监听443端口,匹配到相应域名，进行证书验证，将服务代理到指定服务器</h6>
<h2 data-id="heading-24">四、其他常用配置</h2>
<h4 data-id="heading-25">4.1 IP白名单</h4>
<p>可以配置nginx的白名单，规定有哪些ip可以访问你的服务器，防爬虫必备</p>
<ul>
<li>简单配置</li>
</ul>
<pre><code class="copyable"> server &#123;
        location / &#123;
                deny  192.168.0.1; // 禁止该ip访问
                deny  all; // 禁止所有
            &#125;
  &#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>白名单配置</li>
</ul>
<p>建立白名单</p>
<pre><code class="copyable">vim /etc/nginx/white_ip.conf
 ...
192.168.0.1 1; 
 ...
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改nginx配置(nginx.conf)</p>
<pre><code class="copyable">geo $remote_addr $ip_whitelist&#123;
    default 0;
    include ip.conf;
&#125;
// geo 指令主要是可以根据指定变量的值映射出一个新变量。 如果不指定变量，默认为$remote_addr
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为匹配项做白名单设置</p>
<pre><code class="copyable">server &#123;
    location / &#123;
        if ( $ip_whitelist = 0 )&#123;
            return 403; //不在白名单返回 403
        &#125;
        index index.html;
        root /tmp;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">4.2 适配PC与移动环境</h4>
<p>当用户从移动端打开PC端baidu.com的场景时，将自动跳转指移动端m.baidu.com，本质上是Nginx可以通过内置变量$http_user_agent，获取到请求客户端的userAgent，从而知道当前用户当前终端是移动端还是PC，进而重定向到H5站还是PC站</p>
<pre><code class="copyable">server &#123;
 location / &#123;
        //移动、pc设备agent获取
        if ($http_user_agent ~* '(Android|webOS|iPhone)') &#123;
            set $mobile_request '1';
        &#125;
        if ($mobile_request = '1') &#123;
            rewrite ^.+ http://m.baidu.com;
        &#125;
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">4.3 配置gzip</h4>
<p>开启Nginx gzip，压缩后,静态资源的大小会大大的减少,从而可以节约大量的带宽,提高传输效率,带来更好的响应和体验</p>
<pre><code class="copyable">server&#123;
    gzip on; //启动
    gzip_buffers 32 4K;
    gzip_comp_level 6; //压缩级别，1-10，数字越大压缩的越好
    gzip_min_length 100; //不压缩临界值，大于100的才压缩，一般不用改
    gzip_types application/javascript text/css text/xml;
    gzip_disable "MSIE [1-6]\."; // IE6对Gzip不友好，对Gzip
    gzip_vary on;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">4.4 Nginx配置跨域请求</h4>
<p>当出现403跨域错误的时候，还有 No 'Access-Control-Allow-Origin' header is present on the requested resource报错等，需要给Nginx服务器配置响应的header参数：</p>
<pre><code class="copyable">location / &#123;  
    add_header Access-Control-Allow-Origin *;
    add_header Access-Control-Allow-Methods 'GET, POST, OPTIONS';
    add_header Access-Control-Allow-Headers 'DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization';

    if ($request_method = 'OPTIONS') &#123;
        return 204;
    &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">五、如何使用Nginx</h2>
<p>通过在本地使用Nginx，从启动、更改、重启等环节来介绍Nginx的基本使用</p>
<ul>
<li>
<p>如何启动 <code>sudo nginx</code></p>
</li>
<li>
<p>修改nginx.conf 配置 (具体看你配置位置) <code>vim /usr/local/etc/nginx/nginx.conf</code></p>
</li>
<li>
<p>检查语法是否正常 <code>sudo nginx -t</code></p>
</li>
<li>
<p>重启nginx <code>sudo nginx -s reload</code></p>
</li>
<li>
<p>创建软链接(便于管理多应用nginx)</p>
</li>
</ul>
<blockquote>
<p>当我们需要管理多个网站的nginx，nginx文件放在一起是最好的管理方式，一般都存在/nginx/conf.d/，我们需要把配置文件丢到 /etc/nginx/conf.d/ 文件夹下，怎样才能使这个配置文件既在程序文件夹下，又在 /etc/nginx/conf.d/文件夹下呢？</p>
</blockquote>
<p>假如我们在程序文件夹下有一个 ngxin 配置文件：/home/app/app.nginx.conf 我们需要给这个文件创建一个软链接到 /etc/nginx/conf.d/ 下：<br>
<code>ln -s /home/app/app.example.com.nginx.conf /etc/nginx/conf.d/app.nginx.conf</code><br>
这样操作之后，当我们改应用配置文件，/etc/nginx/conf.d/ 下与之对应的配置文件也会被修改，修改后重启 nginx 就能够使新的 ngxin 配置生效了。</p></div>  
</div>
            