
---
title: '【Nginx】实现负载均衡、限流、缓存、黑白名单和灰度发布，这是最全的一篇了！（建议收藏）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=3990'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 03:04:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=3990'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>大家好，我是冰河~~</strong></p>
<p>在《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg3MzE1NTIzNA%3D%3D%26mid%3D2247485388%26idx%3D1%26sn%3D0854d3f9b4527fd84af970261ec6e2e7%26chksm%3Dcee51801f992911732661cce665c967777e11d6ff53c82dbf2600382f37733a0982f60c47ea8%26token%3D515857896%26lang%3Dzh_CN%23rd" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=Mzg3MzE1NTIzNA==&mid=2247485388&idx=1&sn=0854d3f9b4527fd84af970261ec6e2e7&chksm=cee51801f992911732661cce665c967777e11d6ff53c82dbf2600382f37733a0982f60c47ea8&token=515857896&lang=zh_CN#rd" ref="nofollow noopener noreferrer">【高并发】面试官问我如何使用Nginx实现限流，我如此回答轻松拿到了Offer！</a>》一文中，我们主要介绍了如何使用Nginx进行限流，以避免系统被大流量压垮。除此之外，Nginx还有很多强大的功能，例如：负载均衡、缓存、黑白名单、灰度发布等。今天，我们就来一起探讨Nginx支持的这些强大的功能！</p>
<h2 data-id="heading-0">Nginx安装</h2>
<p><strong>注意：这里以CentOS 6.8服务器为例，以root用户身份来安装Nginx。</strong></p>
<h3 data-id="heading-1">1.安装依赖环境</h3>
<pre><code class="hljs language-bash copyable" lang="bash">yum -y install wget gcc-c++ ncurses ncurses-devel cmake make perl bison openssl openssl-devel gcc* libxml2 libxml2-devel curl-devel libjpeg* libpng* freetype* autoconf automake zlib* fiex* libxml* libmcrypt* libtool-ltdl-devel* libaio libaio-devel  bzr libtool
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">2.安装openssl</h3>
<pre><code class="hljs language-bash copyable" lang="bash">wget https://www.openssl.org/<span class="hljs-built_in">source</span>/openssl-1.0.2s.tar.gz
tar -zxvf openssl-1.0.2s.tar.gz
<span class="hljs-built_in">cd</span> /usr/<span class="hljs-built_in">local</span>/src/openssl-1.0.2s
./config --prefix=/usr/<span class="hljs-built_in">local</span>/openssl-1.0.2s
make
make install
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">3.安装pcre</h3>
<pre><code class="hljs language-bash copyable" lang="bash">wget https://ftp.pcre.org/pub/pcre/pcre-8.43.tar.gz
tar -zxvf pcre-8.43.tar.gz
<span class="hljs-built_in">cd</span> /usr/<span class="hljs-built_in">local</span>/src/pcre-8.43
./configure --prefix=/usr/<span class="hljs-built_in">local</span>/pcre-8.43
make
make install
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">4.安装zlib</h3>
<pre><code class="hljs language-bash copyable" lang="bash">wget https://sourceforge.net/projects/libpng/files/zlib/1.2.11/zlib-1.2.11.tar.gz
tar -zxvf zlib-1.2.11.tar.gz
<span class="hljs-built_in">cd</span> /usr/<span class="hljs-built_in">local</span>/src/zlib-1.2.11
./configure --prefix=/usr/<span class="hljs-built_in">local</span>/zlib-1.2.11
make
make
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">5.安装Nginx</h3>
<pre><code class="hljs language-bash copyable" lang="bash">wget http://nginx.org/download/nginx-1.17.2.tar.gz
tar -zxvf nginx-1.17.2.tar.gz
<span class="hljs-built_in">cd</span> /usr/<span class="hljs-built_in">local</span>/src/nginx-1.17.2
./configure --prefix=/usr/<span class="hljs-built_in">local</span>/nginx-1.17.2 --with-openssl=/usr/<span class="hljs-built_in">local</span>/src/openssl-1.0.2s --with-pcre=/usr/<span class="hljs-built_in">local</span>/src/pcre-8.43 --with-zlib=/usr/<span class="hljs-built_in">local</span>/src/zlib-1.2.11 --with-http_ssl_module
make
make install
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>这里需要注意的是：安装Nginx时，指定的是openssl、pcre和zlib的源码解压目录，安装完成后Nginx配置文件的完整路径为：/usr/local/nginx-1.17.2/conf/nginx.conf。</strong></p>
<h2 data-id="heading-6">Nginx负载均衡配置</h2>
<h3 data-id="heading-7">1.负载均衡配置</h3>
<pre><code class="hljs language-bash copyable" lang="bash">http &#123;
       ……
    upstream real_server &#123;
       server 192.168.103.100:2001 weight=1;  <span class="hljs-comment">#轮询服务器和访问权重</span>
       server 192.168.103.100:2002 weight=2;
    &#125;
 
    server &#123;
        listen  80;
 
        location / &#123;
            proxy_pass http://real_server;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2.失败重试配置</h3>
<pre><code class="hljs language-bash copyable" lang="bash">upstream real_server &#123;
   server 192.168.103.100:2001 weight=1 max_fails=2 fail_timeout=60s;
   server 192.168.103.100:2002 weight=2 max_fails=2 fail_timeout=60s;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>意思是在fail_timeout时间内失败了max_fails次请求后，则认为该上游服务器不可用，然后将该服务地址踢除掉。fail_timeout时间后会再次将该服务器加入存活列表，进行重试。</p>
<h2 data-id="heading-9">Nginx限流配置</h2>
<h3 data-id="heading-10">1.配置参数</h3>
<p>limit_req_zone指令设置参数</p>
<pre><code class="hljs language-bash copyable" lang="bash">limit_req_zone <span class="hljs-variable">$binary_remote_addr</span> zone=mylimit:10m rate=10r/s;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>limit_req_zone定义在http块中，$binary_remote_addr表示保存客户端IP地址的二进制形式。</li>
<li>Zone定义IP状态及URL访问频率的共享内存区域。zone=keyword标识区域的名字，以及冒号后面跟区域大小。16000个IP地址的状态信息约1MB，所以示例中区域可以存储160000个IP地址。</li>
<li>Rate定义最大请求速率。示例中速率不能超过每秒10个请求。</li>
</ul>
<h3 data-id="heading-11">2.设置限流</h3>
<pre><code class="hljs language-bash copyable" lang="bash">location / &#123;
        limit_req zone=mylimit burst=20 nodelay;
        proxy_pass http://real_server;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>burst排队大小，nodelay不限制单个请求间的时间。</p>
<h3 data-id="heading-12">3.不限流白名单</h3>
<pre><code class="hljs language-bash copyable" lang="bash">geo <span class="hljs-variable">$limit</span> &#123;
default              1;
192.168.2.0/24  0;
&#125;
 
map <span class="hljs-variable">$limit</span> <span class="hljs-variable">$limit_key</span> &#123;
1 <span class="hljs-variable">$binary_remote_addr</span>;
0 <span class="hljs-string">""</span>;
&#125;
 
limit_req_zone <span class="hljs-variable">$limit_key</span> zone=mylimit:10m rate=1r/s;
 
location / &#123;
        limit_req zone=mylimit burst=1 nodelay;
        proxy_pass http://real_server;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述配置中，192.168.2.0/24网段的IP访问是不限流的，其他限流。</p>
<p>IP后面的数字含义：</p>
<ul>
<li>24表示子网掩码:255.255.255.0</li>
<li>16表示子网掩码:255.255.0.0</li>
<li>8表示子网掩码:255.0.0.0</li>
</ul>
<h2 data-id="heading-13">Nginx缓存配置</h2>
<h3 data-id="heading-14">1.浏览器缓存</h3>
<p>静态资源缓存用expire</p>
<pre><code class="hljs language-bash copyable" lang="bash">location ~*  .(jpg|jpeg|png|gif|ico|css|js)$ &#123;
   expires 2d;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Response Header中添加了Expires和Cache-Control,</p>
<p><strong>静态资源包括（一般缓存）</strong></p>
<ul>
<li>普通不变的图像，如logo，图标等</li>
<li>js、css静态文件</li>
<li>可下载的内容，媒体文件</li>
</ul>
<p><strong>协商缓存（add_header ETag/Last-Modified value）</strong></p>
<ul>
<li>HTML文件</li>
<li>经常替换的图片</li>
<li>经常修改的js、css文件</li>
<li>基本不变的API接口</li>
</ul>
<p><strong>不需要缓存</strong></p>
<ul>
<li>用户隐私等敏感数据</li>
<li>经常改变的api数据接口</li>
</ul>
<h3 data-id="heading-15">2.代理层缓存</h3>
<pre><code class="hljs language-bash copyable" lang="bash">//缓存路径，inactive表示缓存的时间，到期之后将会把缓存清理
proxy_cache_path /data/cache/nginx/ levels=1:2 keys_zone=cache:512m inactive = 1d max_size=8g;
 
location / &#123;
    location ~ \.(htm|html)?$ &#123;
        proxy_cache cache;
        proxy_cache_key    $uri$is_args<span class="hljs-variable">$args</span>;     //以此变量值做HASH，作为KEY
        //HTTP响应首部可以看到X-Cache字段，内容可以有HIT,MISS,EXPIRES等等
        add_header X-Cache <span class="hljs-variable">$upstream_cache_status</span>;
        proxy_cache_valid 200 10m;
        proxy_cache_valid any 1m;
        proxy_pass  http://real_server;
        proxy_redirect     off;
    &#125;
    location ~ .*\.(gif|jpg|jpeg|bmp|png|ico|txt|js|css)$ &#123;
        root /data/webapps/edc;
        expires      3d;
        add_header Static Nginx-Proxy;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在本地磁盘创建一个文件目录，根据设置，将请求的资源以K-V形式缓存在此目录当中，KEY需要自己定义（这里用的是url的hash值），同时可以根据需要指定某内容的缓存时长，比如状态码为200缓存10分钟，状态码为301，302的缓存5分钟，其他所有内容缓存1分钟等等。
可以通过purger的功能清理缓存。</p>
<p>AB测试/个性化需求时应禁用掉浏览器缓存。</p>
<h2 data-id="heading-16">Nginx黑名单</h2>
<h3 data-id="heading-17">1.一般配置</h3>
<pre><code class="hljs language-bash copyable" lang="bash">location / &#123;
    deny  192.168.1.1;
    deny 192.168.1.0/24;
    allow 10.1.1.0/16;
    allow 2001:0db8::/32;
    deny  all;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">2. Lua+Redis动态黑名单(OpenResty)</h3>
<p><strong>安装运行</strong></p>
<pre><code class="hljs language-bash copyable" lang="bash">yum install yum-utils
yum-config-manager --add-repo https://openresty.org/package/centos/openresty.repo
yum install openresty
yum install openresty-resty
查看
yum --disablerepo=<span class="hljs-string">"*"</span> --enablerepo=<span class="hljs-string">"openresty"</span> list available
运行
service openresty start
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置(/usr/local/openresty/nginx/conf/nginx.conf)</strong></p>
<pre><code class="hljs language-bash copyable" lang="bash">lua_shared_dict ip_blacklist 1m;
 
server &#123;
    listen  80;
 
    location / &#123;
        access_by_lua_file lua/ip_blacklist.lua;
        proxy_pass http://real_server;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>lua脚本（ip_blacklist.lua）</strong></p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">local</span> redis_host    = <span class="hljs-string">"192.168.1.132"</span>
<span class="hljs-built_in">local</span> redis_port    = 6379
<span class="hljs-built_in">local</span> redis_pwd     = 123456
<span class="hljs-built_in">local</span> redis_db = 2
 
-- connection timeout <span class="hljs-keyword">for</span> redis <span class="hljs-keyword">in</span> ms.
<span class="hljs-built_in">local</span> redis_connection_timeout = 100
 
-- a <span class="hljs-built_in">set</span> key <span class="hljs-keyword">for</span> blacklist entries
<span class="hljs-built_in">local</span> redis_key     = <span class="hljs-string">"ip_blacklist"</span>
 
-- cache lookups <span class="hljs-keyword">for</span> this many seconds
<span class="hljs-built_in">local</span> cache_ttl     = 60
 
-- end configuration
 
<span class="hljs-built_in">local</span> ip                = ngx.var.remote_addr
<span class="hljs-built_in">local</span> ip_blacklist      = ngx.shared.ip_blacklist
<span class="hljs-built_in">local</span> last_update_time  = ip_blacklist:get(<span class="hljs-string">"last_update_time"</span>);
 
-- update ip_blacklist from Redis every cache_ttl seconds:
<span class="hljs-keyword">if</span> last_update_time == nil or last_update_time < ( ngx.now() - cache_ttl ) <span class="hljs-keyword">then</span>
 
  <span class="hljs-built_in">local</span> redis = require <span class="hljs-string">"resty.redis"</span>;
  <span class="hljs-built_in">local</span> red = redis:new();
 
  red:set_timeout(redis_connect_timeout);
 
  <span class="hljs-built_in">local</span> ok, err = red:connect(redis_host, redis_port);
  <span class="hljs-keyword">if</span> not ok <span class="hljs-keyword">then</span>
    ngx.log(ngx.ERR, <span class="hljs-string">"Redis connection error while connect: "</span> .. err);
  <span class="hljs-keyword">else</span>
    <span class="hljs-built_in">local</span> ok, err = red:auth(redis_pwd)
    <span class="hljs-keyword">if</span> not ok <span class="hljs-keyword">then</span>
      ngx.log(ngx.ERR, <span class="hljs-string">"Redis password error while auth: "</span> .. err);
    <span class="hljs-keyword">else</span>
        <span class="hljs-built_in">local</span> new_ip_blacklist, err = red:smembers(redis_key);
        <span class="hljs-keyword">if</span> err <span class="hljs-keyword">then</span>
            ngx.log(ngx.ERR, <span class="hljs-string">"Redis read error while retrieving ip_blacklist: "</span> .. err);
        <span class="hljs-keyword">else</span>
        ngx.log(ngx.ERR, <span class="hljs-string">"Get data success:"</span> .. new_ip_blacklist)
          -- replace the locally stored ip_blacklist with the updated values:
            ip_blacklist:flush_all();
          <span class="hljs-keyword">for</span> index, banned_ip <span class="hljs-keyword">in</span> ipairs(new_ip_blacklist) <span class="hljs-keyword">do</span>
            ip_blacklist:<span class="hljs-built_in">set</span>(banned_ip, <span class="hljs-literal">true</span>);
          end
          -- update time
          ip_blacklist:<span class="hljs-built_in">set</span>(<span class="hljs-string">"last_update_time"</span>, ngx.now());
      end
    end
  end
end
 
<span class="hljs-keyword">if</span> ip_blacklist:get(ip) <span class="hljs-keyword">then</span>
  ngx.log(ngx.ERR, <span class="hljs-string">"Banned IP detected and refused access: "</span> .. ip);
  <span class="hljs-built_in">return</span> ngx.exit(ngx.HTTP_FORBIDDEN);
end
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">Nginx灰度发布</h2>
<h3 data-id="heading-20">1.根据Cookie实现灰度发布</h3>
<p>根据Cookie查询version值，如果该version值为v1转发到host1，为v2转发到host2，都不匹配的情况下转发到默认配置。</p>
<pre><code class="hljs language-bash copyable" lang="bash">upstream host1 &#123;
   server 192.168.2.46:2001 weight=1;  <span class="hljs-comment">#轮询服务器和访问权重</span>
   server 192.168.2.46:2002 weight=2;
&#125;
 
upstream host2 &#123;
   server 192.168.1.155:1111  max_fails=1 fail_timeout=60;
&#125;
 
upstream default &#123;
   server 192.168.1.153:1111  max_fails=1 fail_timeout=60;
&#125;
 
map <span class="hljs-variable">$COOKIE_version</span> <span class="hljs-variable">$group</span> &#123;
   ~*v1$ host1;
   ~*v2$ host2;
   default default;
&#125;
 
lua_shared_dict ip_blacklist 1m;
 
server &#123;
    listen  80;
 
    <span class="hljs-comment">#set $group "default";</span>
    <span class="hljs-comment">#if ($http_cookie ~* "version=v1")&#123;</span>
    <span class="hljs-comment">#    set $group host1;</span>
    <span class="hljs-comment">#&#125;</span>
    <span class="hljs-comment">#if ($http_cookie ~* "version=v2")&#123;</span>
    <span class="hljs-comment">#    set $group host2;</span>
    <span class="hljs-comment">#&#125;</span>
 
    location / &#123;
        access_by_lua_file lua/ip_blacklist.lua;
        proxy_pass http://<span class="hljs-variable">$group</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">2.根据来路IP实现灰度发布</h3>
<pre><code class="hljs language-bash copyable" lang="bash">server &#123;
  ……………
  <span class="hljs-built_in">set</span> <span class="hljs-variable">$group</span> default;
  <span class="hljs-keyword">if</span> (<span class="hljs-variable">$remote_addr</span> ~ <span class="hljs-string">"192.168.119.1"</span>) &#123;
      <span class="hljs-built_in">set</span> <span class="hljs-variable">$group</span> host1;
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-variable">$remote_addr</span> ~ <span class="hljs-string">"192.168.119.2"</span>) &#123;
      <span class="hljs-built_in">set</span> <span class="hljs-variable">$group</span> host2;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">3.更细粒度灰度发布</h3>
<p>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsunshinelyz%2FABTestingGateway" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sunshinelyz/ABTestingGateway" ref="nofollow noopener noreferrer">github.com/sunshinelyz…</a></p>
<p><strong>好了，今天就到这儿吧，我是冰河，我们下期见~~</strong></p></div>  
</div>
            