
---
title: 'Nginx学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c6ea0122a91474c87a2d3cd4155e69f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 01:22:39 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c6ea0122a91474c87a2d3cd4155e69f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">一、Nginx简介</h4>
<p>1、<em>Nginx</em> (engine x) 是一个高性能的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2FHTTP" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/HTTP" ref="nofollow noopener noreferrer">HTTP</a>和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E5%258F%258D%25E5%2590%2591%25E4%25BB%25A3%25E7%2590%2586%2F7793488" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86/7793488" ref="nofollow noopener noreferrer">反向代理</a>web服务器，其特点是占有内存少，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E5%25B9%25B6%25E5%258F%2591%2F11024806" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E5%B9%B6%E5%8F%91/11024806" ref="nofollow noopener noreferrer">并发</a>能力强，事实上nginx的并发能力在同类型的网页服务器中表现较好</p>
<p>2、Nginx专为性能优化而开发，性能是其最重要的考量，能经受高负载的考验，有报告表明能支持高达50000个并发连接数</p>
<h4 data-id="heading-1">二、正向代理</h4>
<p>1、正向代理:是一个位于客户端和原始服务器(origin server)之间的服务器，为了从原始服务器取得内容，客户端向代理发送一个请求并指定目标(原始服务器)，然后代理向原始服务器转交请求并将获得的内容返回给客户端。客户端才能使用正向代理。正向代理的典型用途是为在防火墙内的局域网客户端提供访问Internet的途径。和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E5%258F%258D%25E5%2590%2591%25E4%25BB%25A3%25E7%2590%2586" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86" ref="nofollow noopener noreferrer">反向代理</a>不同之处在于，典型的正向代理是一种最终用户知道并主动使用的代理方式。例如Chrome浏览器中安装了switchysharp以后，通过switchysharp方便地进行代理转发服务。而为此用户必须要提前在switchysharp中做好设置才能达到相应的效果。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c6ea0122a91474c87a2d3cd4155e69f~tplv-k3u1fbpfcp-watermark.image" alt="正向代理.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">三、反向代理</h4>
<p>1、反向代理：反向代理服务器位于用户与目标服务器之间，但是对于用户而言，反向代理服务器就相当于目标服务器，即用户直接访问反向代理服务器就可以获得目标服务器的资源。同时，用户不需要知道目标服务器的地址，也无须在用户端作任何设定。反向代理服务器通常可用来作为Web加速，即使用反向代理作为Web服务器的前置机来降低网络和服务器的负载，提高访问效率。</p>
<h4 data-id="heading-3">四、负载均衡</h4>
<p>1、负载均衡（Load Balance）：其含义就是将负载（工作任务）进行平衡、分摊到多个操作单元上进行运行，例如FTP服务器、Web服务器、企业核心应用服务器和其它主要任务服务器等，从而协同完成工作任务。负载均衡构建在原有网络结构之上，它提供了一种透明且廉价有效的方法扩展服务器和网络设备的带宽、加强网络数据处理能力、增加吞吐量、提供网络的可用性和灵活性。</p>
<h4 data-id="heading-4">五、动静分离</h4>
<p>1、动静分离：动静分离是指在web服务器架构中，将静态页面与动态页面或者静态内容接口和动态内容接口分开不同系统访问的架构设计方法，进而提升整个服务访问性能和可维护性</p>
<h4 data-id="heading-5">六、linux虚拟机上安装Nginx</h4>
<p>1、安装编译工具及库文件</p>
<pre><code class="hljs language-shell copyable" lang="shell">yum -y install make zlib zlib-devel gcc-c++ libtool  openssl openssl-devel
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、安装 PCRE（PCRE 作用是让 Nginx 支持 Rewrite 功能）：大部分虚拟机使用的镜像是自带了PCRE的，则不需要额外安装</p>
<pre><code class="hljs language-shell copyable" lang="shell">// 切换目录
cd /usr/local/src/
// 下载pcre
wget http://downloads.sourceforge.net/project/pcre/pcre/8.35/pcre-8.35.tar.gz
// 解压安装包
tar zxvf pcre-8.35.tar.gz
// 进入安装包目录
cd pcre-8.35
// 编译安装
./configure
make &&　make install
// 查看pcre版本
pcre-config --version

<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、安装并启动Nginx</p>
<pre><code class="hljs language-shell copyable" lang="shell">// 下载nginx
cd /usr/local/src/
wget http://nginx.org/download/nginx-1.6.2.tar.gz
// 解压安装包
tar zxvf nginx-1.6.2.tar.gz
// 进入安装包目录
cd nginx-1.6.2
// 编译安装
./configure
make &&　make install
// 查看nginx版本
/usr/local/nginx/sbin/nginx -v
// 启动nginx
cd /usr/local/nginx/sbin
./nginx
// 查看nginx进程
ps -ef|grep nginx
// 查看防火墙状态
systemctl status firewalld
// 关闭防火墙（不推荐）
systemctl stop firewalld
// 查看防火墙
firewall-cmd --list-all
// 临时开放端口80（reload之后消失）：不需要reload生效
firewall-cmd --add-port=80/tcp
// 永久开放端口80，reload之后生效
firewall-cmd --permanent --add-port=80/tcp
firewall-cmd --reload
// 永久删除开放的端口
firewall-cmd --permanent --remove-port=80/tcp
firewall-cmd --reload
// 查看所有放行的端口
firewall-cmd --list-ports
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">七、使用Nginx</h4>
<p>1、Nginx操作常用命令</p>
<p>(1)、使用nginx操作命令的前提是必须进入nginx的目录</p>
<pre><code class="hljs language-shell copyable" lang="shell">cd /usr/local/nginx/sbin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(2)、常用命令</p>
<pre><code class="hljs language-shell copyable" lang="shell">// 查看nginx版本号
./nginx -v
// 检查nginx配置文件nginx.conf是否正确
./nginx -t
// 停止nginx服务
./nginx -s stop
// 运行nginx服务
./nginx
// 更改nginx配置文件nginx.conf后重启nginx服务
./nginx -s reload
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、Nginx配置文件</p>
<p>（1）、Nginx配置文件位置</p>
<pre><code class="hljs language-shell copyable" lang="shell">// 配置文件是conf目录下的nginx.conf
cd /usr/local/nginx/conf
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）、配置文件内容组成：由三部分（全局块、events块、http块）组成</p>
<pre><code class="hljs language-shell copyable" lang="shell">// #表示当前行注释
<span class="hljs-meta">#</span><span class="bash">user  nobody;</span>
// Nginx服务器并发处理服务的关键配置，值越大，可以支持的并发处理量也越多，但是会受到硬件、软件等设备的制约
worker_processes  1;
<span class="hljs-meta">
#</span><span class="bash">error_log  logs/error.log;</span>
<span class="hljs-meta">#</span><span class="bash">error_log  logs/error.log  notice;</span>
<span class="hljs-meta">#</span><span class="bash">error_log  logs/error.log  info;</span>
<span class="hljs-meta">
#</span><span class="bash">pid        logs/nginx.pid;</span>


events &#123;
// 表示每个work process支持的最大连接数为1024，该配置对Nginx的性能影响较大，在实际中应该灵活配置
    worker_connections  1024;
&#125;

// http全局块
http &#123;
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

// server块
    server &#123;
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / &#123;
            root   html;
            index  index.html index.htm;
        &#125;

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html &#123;
            root   html;
        &#125;

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ &#123;
        #    proxy_pass   http://127.0.0.1;
        #&#125;

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ &#123;
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #&#125;

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht &#123;
        #    deny  all;
        #&#125;
    &#125;


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server &#123;
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / &#123;
    #        root   html;
    #        index  index.html index.htm;
    #    &#125;
    #&#125;


    # HTTPS server
    #
    #server &#123;
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / &#123;
    #        root   html;
    #        index  index.html index.htm;
    #    &#125;
    #&#125;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>全局块：从配置文件开始到events块之间的内容，主要会设置一些影响Nginx服务器整体运行的配置指令，主要包括配置运行Nginx服务器的用户（组）、允许生成的worker process数，进程PID存放路径、日志存放路径和类型以及配置文件的引入等</p>
<p>events块：涉及的指令主要影响Nginx服务器与用户的网络连接，常用的设置包括是否开启对多work process下的网络连接进行序列化，是否允许同时接收多个网络连接，选取哪种事件驱动模型来处理连接请求，每个work process可以同时支持的最大连接数等</p>
<p>http块：代理、缓存和日志定义等绝大多数功能和第三方模块的配置都在这里，http块包含http全局块和server块。http全局块配置的指令包括文件引入、MIME-TYPE定义、日志自定义、连接超时时间、单链接请求数上限等。server块与虚拟主机有密切关系，虚拟主机从用户角度看，和一台独立的硬件主机是完全一样的，该技术的产生是为了节省互联网服务器硬件成本。每个http块可以包含多个server块，而每个server块就相当于是一个虚拟主机。每个server块分为全局server块和包含的多个location块。全局server块：最常见的配置是本虚拟机主机的监听配置和本虚拟机主机的名称或IP配置。location块：主要是基于Nginx服务器接收到的请求字符串（例如 server_name/uri-string），对虚拟主机名称（也可以是IP别名）之外的字符串（例如 前面的 /uri-string）进行匹配，对特定的请求进行处理。地址定向、数据缓存和应答控制等功能，还有许多第三方模块的配置也在这里进行。</p>
<p>3、nginx反向代理配置实例一</p>
<p>目标：在windows机器的浏览器上访问 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.123.com" target="_blank" rel="nofollow noopener noreferrer" title="http://www.123.com" ref="nofollow noopener noreferrer">www.123.com</a> ，能通过nginx做反向代理，访问到linux服务器中运行的tomcat首页</p>
<p>（1）、安装并配置JDK</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjingyan.baidu.com%2Farticle%2F0aa22375115f0088cc0d64b9.html" target="_blank" rel="nofollow noopener noreferrer" title="https://jingyan.baidu.com/article/0aa22375115f0088cc0d64b9.html" ref="nofollow noopener noreferrer">jingyan.baidu.com/article/0aa…</a></p>
<p>（2）、安装并运行tomcat：下载tomcat安装包并解压，完成后即可使用</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fsocketqiang%2Fp%2F10960218.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/socketqiang/p/10960218.html" ref="nofollow noopener noreferrer">www.cnblogs.com/socketqiang…</a></p>
<pre><code class="hljs language-shell copyable" lang="shell">// 将tomcat默认的端口8080开放
firewall-cmd --permanent --add-port=8080/tcp
firewall-cmd --reload
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(3)、在windows的hosts文件中配置 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.123.com" target="_blank" rel="nofollow noopener noreferrer" title="http://www.123.com" ref="nofollow noopener noreferrer">www.123.com</a> 域名映射到的ip地址。在浏览器上访问域名时，系统会先根据域名查找相对应的IP地址，再与目标ip进行通讯。域名相对应的IP地址系统会首先在hosts文件中进行查找，如果没有的话再通过dns服务器进行查询，如果在dns服务器上找不到的话，系统就会报错或者提示无法访问等。</p>
<pre><code class="hljs language-shell copyable" lang="shell">// hosts文件中加上域名映射ip配置(虚拟机ip 域名)，hosts文件的目录 C:\Windows\System32\drivers\etc
192.168.249.129 www.123.com
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(4)、在nginx里进行请求转发的配置（即反向代理）</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d88179cb93d45f7836bac1ba7116610~tplv-k3u1fbpfcp-watermark.image" alt="nginx反向代理转发配置.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此处配置表示当访问 192.168.249.129:80（80是默认端口，地址中不带端口时表示使用的就是默认端口80。location后面的只有一个斜杠，表示这条规则匹配的就是192.168.249.129:80）时，配置了proxy_pass 127.0.0.1:8080，表示代理转发到127.0.0.1:8080。到此反向代理已完成，重新启动nginx，在浏览器中访问www.123.com。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac2b1e5b0cf644a68c7583b9dcc343e3~tplv-k3u1fbpfcp-watermark.image" alt="nginx反向代理配置完效果.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解释说明：当在浏览器中访问www.123.com 时，相当于在访问 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.123.com%3A80" target="_blank" rel="nofollow noopener noreferrer" title="http://www.123.com:80" ref="nofollow noopener noreferrer">www.123.com:80</a> ，由于在hosts文件中配置了 192.168.249.129  <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.123.com" target="_blank" rel="nofollow noopener noreferrer" title="http://www.123.com" ref="nofollow noopener noreferrer">www.123.com</a> ，此时访问被代理到192.168.249.129:80，即代理到虚拟机的nginx服务上，由于nginx.conf中配置了请求转发，192.168.249.129:80的访问会转发到127.0.0.1:8080，即转发到虚拟机的tomcat服务上</p>
<p>4、nginx反向代理配置实例二</p>
<p>目标：使用Nginx反向代理，根据访问的路径跳转到不同端口的服务中，nginx监听端口9001，当访问<a href="https://link.juejin.cn/?target=http%3A%2F%2F127.0.0.1%3A9001%2Fedu%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://127.0.0.1:9001/edu/" ref="nofollow noopener noreferrer">http://127.0.0.1:9001/edu/</a> 直接跳转到127.0.0.1:8081，访问 <a href="https://link.juejin.cn/?target=http%3A%2F%2F127.0.0.1%3A9001%2Fvod%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://127.0.0.1:9001/vod/" ref="nofollow noopener noreferrer">http://127.0.0.1:9001/vod/</a> 直接跳转到127.0.0.1:8082</p>
<p>（1）、启动两个tomcat服务，新建文件夹tomcat8081和tomcat8082，把tomcat安装包放到两个文件夹中解压，在两个文件夹中的conf目录下的server.xml配置文件中分别配置tomcat启动端口为8081和8082，相应的tomcat服务关闭端口也做下修改</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f955b71dd0c3432099cc47c3ef39e552~tplv-k3u1fbpfcp-watermark.image" alt="修改tomcat的启动端口.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f22c888d00a34e39a8577849a5cc0585~tplv-k3u1fbpfcp-watermark.image" alt="修改tomcat关闭端口.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（2）、在tomcat8081中的tomcat的webapp目录下新建edu文件夹，在里面放一个a.html文件，html中内容为 8081!!!! ，相应的在tomcat8082中的webapp目录下新建vod文件夹，在里面放a.html文件，文件内容为 8082 ，使用tomcat中bin目录下的脚本 startup.sh分别启动两个tomcat服务</p>
<p>（3）、修改nginx配置，增加一个server全局块，完成后重新启动</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b85466873ea4580a34f3fa7dc909b88~tplv-k3u1fbpfcp-watermark.image" alt="nginx配置9001端口下的请求转发.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>location块后的符号说明：</p>
<p>=     等于号用于不含正则表达式的uri前，要求请求字符串与uri严格匹配，如果匹配成功，就停止继续向下搜索并立即处理该请求。</p>
<p>~     波浪号用于表示uri包含正则表达式，并且区分大小写。</p>
<p>~*    波浪号加上星号用于表示uri包含正则表达式，并且不区分大小写</p>
<p>^~    开始符号加上波浪号用于表示不含正则表达式的uri前，要求Nginx服务器找到标识uri和请求字符串匹配度最高的location后，立即使用此location处理请求，而不再使用location块中的正则uri和请求字符串做匹配</p>
<p>注意：如果uri包含正则表达式，则必须要有<del>或者</del>*标识</p>
<p>（4）最终效果：访问 <a href="https://link.juejin.cn/?target=http%3A%2F%2F192.168.249.129%3A9001%2Fedu%2Fa.html" target="_blank" rel="nofollow noopener noreferrer" title="http://192.168.249.129:9001/edu/a.html" ref="nofollow noopener noreferrer">http://192.168.249.129:9001/edu/a.html</a> 时，能转发到端口为8081的tomcat服务器上，找到edu文件夹下的a.html，显示里面的内容 8081!!!!，对于 <a href="https://link.juejin.cn/?target=http%3A%2F%2F192.168.249.129%3A9001%2Fvod%2Fa.html" target="_blank" rel="nofollow noopener noreferrer" title="http://192.168.249.129:9001/vod/a.html" ref="nofollow noopener noreferrer">http://192.168.249.129:9001/vod/a.html</a> 请求，能转发到端口为8082的tomcat服务器上，找到vod文件夹下的a.html，显示里面的内容8082</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70dfb7efb2734957847e15734cc505f3~tplv-k3u1fbpfcp-watermark.image" alt="转发到tomcat8081服务器上.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/697cfa90f34b4024bd2d13e71d4da519~tplv-k3u1fbpfcp-watermark.image" alt="转发到tomcat8082服务器上.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>5、Nginx负载均衡配置实例一</p>
<p>目标：启动两个tomcat服务器，端口分别为8081和8082，在两个服务器的webapp目录下均新建loadBalance文件夹，文件夹下均添加b.html文件，两个文件中内容分别为 负载均衡8081 和 负载均衡8082 ，当在浏览器上访问 <a href="https://link.juejin.cn/?target=http%3A%2F%2F192.168.249.129%3A9002%2FloadBalance%2Fb.html" target="_blank" rel="nofollow noopener noreferrer" title="http://192.168.249.129:9002/loadBalance/b.html" ref="nofollow noopener noreferrer">http://192.168.249.129:9002/loadBalance/b.html</a> 时，将请求负载均衡到8081和8082服务器上，采用轮询方式，即这次分发到8081服务器，下次就是分发到8082服务器，循环往复</p>
<p>（1）、准备好tomcat服务器，在两个tomcat服务器上新建b.html文件并启动tomcat服务器</p>
<p>（2）、nginx中配置负载均衡</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a93952da787148b0bc99aa40b221992c~tplv-k3u1fbpfcp-watermark.image" alt="负载均衡配置.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此处的配置表示当访问<a href="https://link.juejin.cn/?target=http%3A%2F%2F192.268.249.129%3A9002%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://192.268.249.129:9002/" ref="nofollow noopener noreferrer">http://192.268.249.129:9002/</a>  且后续路径中带有loadBalance时转发到配置的负载均衡myServer上，此处的负载均衡策略是往两个服务器上轮询分发。</p>
<p>（3）、结果展示</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bf6b89a8ba540188b1d7879c3734738~tplv-k3u1fbpfcp-watermark.image" alt="负载均衡分发到8081服务器.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ef6cb5a545e4f069f950e98963d85c1~tplv-k3u1fbpfcp-watermark.image" alt="负载均衡分发到8082服务器.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>负载均衡常用策略：</p>
<p>轮询（默认）：每个请求按时间顺序逐一分配到不同的后端服务器，如果后端服务器down掉，能自动剔除</p>
<p>weight：weight代表权重，默认为1，权重越高被分配的客户端越多，指定轮询几率，weight与访问比率成正比，用于后端服务器性能不均的情况。如下的配置，请求分发到8082服务器的概率是8081的2倍</p>
<pre><code class="hljs language-xml copyable" lang="xml">upstream server_pool &#123;
server 192.168.249.129:8081 weight=1;
server 192.168.249.129:8082 weight=2;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ip_hash：指定负载均衡器按照基于客户端IP的分配方式，这个方法确保了相同的客户端的请求一直发送到相同的服务器，以保证session会话。这样每个访客都固定访问一个后端服务器，可以解决session不能跨服务器的问题</p>
<pre><code class="hljs language-xml copyable" lang="xml">upstream server_pool &#123;
ip_hash;
server 192.168.249.129:8081;
server 192.168.249.129:8082;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>fair(第三方策略)：第三方的负载均衡策略的实现需要安装第三方插件。按后端服务器的响应时间来分配请求，请求响应时间短的服务器优先分配</p>
<pre><code class="hljs language-xml copyable" lang="xml">upstream server_pool &#123;
fair;
server 192.168.249.129:8081;
server 192.168.249.129:8082;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6、动静分离配置</p>
<p>（1）、Nginx动静分离简单来说就是把动态跟静态请求分开，不能理解成只是单纯的把动态页面和静态页面物理分离。严格意义上说应该是动态请求跟静态请求分开，可以理解成使用Nginx处理静态页面，Tomcat处理动态页面。动静分离从目前实现角度来讲大致分为两种，一种是纯粹把静态文件独立成单独的域名，放到独立的服务器上，也是目前主流推崇的方案；另外一种方法就是动态跟静态文件混合在一起发布，通过Nginx来分开。</p>
<p>​     方案1：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67928d0d9e5840fdb00ce0aa688524eb~tplv-k3u1fbpfcp-watermark.image" alt="动静分离示意图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（2）、Nginx中通过location指定不同的后缀名实现不同的请求转发。通过expires参数设置，可以设置浏览器缓存过期时间，减少与服务器之间的请求。具体Expires定义：给资源设置一个过期时间，在有效期内访问该URL时，会发送一个请求，比对服务器上资源与浏览器缓存中资源的更新时间是否一致，一致的话服务器返回状态码304，该资源就直接取浏览器缓存中的，否则从服务器重新请求。该方式适合变动很少的静态资源。</p>
<p>7、动静分离实例一</p>
<p>目标：通过location设置静态资源的访问路径</p>
<p>（1）、在根目录下新建data文件夹，data下新建img和html文件夹，在img文件夹下放置图片bluetooth.png，在html文件夹下放置a.html文件，在nginx配置文件中配置静态资源访问路径，autoindex:on 表示设置列出访问的目录</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e69fb6a2a53046aebff36bef9e7859d7~tplv-k3u1fbpfcp-watermark.image" alt="静态资源访问配置.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（2）、在浏览器中访问资源</p>
<p>​autoindex:on 列出访问的静态资源</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b0a673441da4a66954163561a36ca77~tplv-k3u1fbpfcp-watermark.image" alt="访问静态资源目录img.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​   访问静态图片资源</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3f54b999379436481c60cabad1c5eb9~tplv-k3u1fbpfcp-watermark.image" alt="访问静态资源图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​            访问静态文件资源</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/134e6aa5d5404f1eae4faf14298a333e~tplv-k3u1fbpfcp-watermark.image" alt="访问静态资源文件.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>8、Nginx配置高可用的集群</p>
<p>目标：配置两个Nginx服务器，在其中一个Nginx服务器不可用的时候能切换到另一个Nginx服务器继续提供服务。</p>
<p>（1）、高可用：高可用（High Availability）是分布式系统架构设计中必须考虑的因素之一，它通常是指，通过设计减少系统不能提供服务的时间</p>
<p>（2）、Keepalived：Keepalived的作用是检测服务器的状态，如果有一台web服务器宕机，或工作出现故障，Keepalived将检测到，并将有故障的服务器从系统中剔除，同时使用其他服务器代替该服务器的工作，当服务器工作正常后Keepalived自动将服务器加入到服务器群中，这些工作全部自动完成，不需要人工干涉，需要人工做的只是修复故障的服务器</p>
<p>（3）、准备两个linux服务器，ip分别为192.168.79.128（MASTER主服务器）、192.168.79.129（BACKUP备份服务器），在两台服务器上都安装nginx和keepalived，配置主服务器和备份服务器的keepalived.conf配置文件，配置文件在/etc/keepalived目录下，在两台服务器的/usr/local/src下都放在nginx是否运行的检测脚本，在两台nginx的服务器上都配上反向代理，代理9010端口的请求到服务器上的tomcat服务。主服务器与备份服务器的tomcat的webapps目录下都新增文件夹demo，demo文件夹下都放置index.html文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 主服务器keepalived.conf配置文件内容</span>
global_defs &#123;
   notification_email &#123;
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   &#125;
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server <span class="hljs-number">192.168</span><span class="hljs-number">.79</span><span class="hljs-number">.128</span>
   smtp_connect_timeout <span class="hljs-number">30</span>
   router_id MASTER  <span class="hljs-comment">// 主服务器域名</span>
   vrrp_skip_check_adv_addr
   vrrp_garp_interval <span class="hljs-number">0</span>
   vrrp_gna_interval <span class="hljs-number">0</span>
&#125;

vrrp_script check_nginx &#123;
   script <span class="hljs-string">"/usr/local/src/nginx_check.sh"</span>  <span class="hljs-comment">// 检测nginx是否正常运行的脚本</span>
   interval <span class="hljs-number">2</span>
   weight <span class="hljs-number">2</span>
&#125;

vrrp_instance VI_1 &#123;
    state MASTER
    interface ens33
    virtual_router_id <span class="hljs-number">51</span>
    priority <span class="hljs-number">100</span>
    advert_int <span class="hljs-number">1</span>
    authentication &#123;
        auth_type PASS
        auth_pass <span class="hljs-number">1111</span>
    &#125;
    virtual_ipaddress &#123;
        <span class="hljs-number">192.168</span><span class="hljs-number">.79</span><span class="hljs-number">.100</span>  <span class="hljs-comment">// 虚拟ip</span>
    &#125;
    #定义实例中需要使用的脚本
    track_script &#123;
        #需要检测的脚本
        check_nginx
    &#125;
&#125;

<span class="hljs-comment">// 备份服务器keepalived.conf配置文件</span>
global_defs &#123;
   notification_email &#123;
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   &#125;
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server <span class="hljs-number">192.168</span><span class="hljs-number">.79</span><span class="hljs-number">.129</span>
   smtp_connect_timeout <span class="hljs-number">30</span>
   router_id BACKUP
   vrrp_skip_check_adv_addr
   vrrp_garp_interval <span class="hljs-number">0</span>
   vrrp_gna_interval <span class="hljs-number">0</span>
&#125;

vrrp_script check_nginx &#123;
   script <span class="hljs-string">"/usr/local/src/nginx_check.sh"</span>
   interval <span class="hljs-number">2</span>
   weight <span class="hljs-number">2</span>
&#125;

vrrp_instance VI_1 &#123;
    state BACKUP
    interface ens33
    virtual_router_id <span class="hljs-number">51</span>
    priority <span class="hljs-number">80</span>
    advert_int <span class="hljs-number">1</span>
    authentication &#123;
        auth_type PASS
        auth_pass <span class="hljs-number">1111</span>
    &#125;
    virtual_ipaddress &#123;
        <span class="hljs-number">192.168</span><span class="hljs-number">.79</span><span class="hljs-number">.100</span>
    &#125;
    #定义实例中需要使用的脚本
    track_script &#123;
        #需要检测的脚本
        check_nginx
    &#125;
&#125;

<span class="hljs-comment">// nginx_check.sh脚本内容，此处需要注意，如果是从windows系统中粘贴这段文字到linux系统中，需要运行 sed -i 's/\r$//' nginx_check.sh 命名将Windows下每一行结尾的 \n\r 替换成Linux下的 \n， https://blog.csdn.net/ouyang_peng/article/details/86488451</span>
#!<span class="hljs-regexp">/bin/</span>bash
#获取nginx进程的数量
counter=$(ps -C nginx --no-heading|wc -l)
#如果nginx进程数量为<span class="hljs-number">0</span>(没有启动或挂掉)
echo <span class="hljs-string">"monitor running"</span>
#查询nginx进程数量
counter=$(ps -C nginx --no-heading|wc -l)
#如果nginx进程数仍然为<span class="hljs-number">0</span>
<span class="hljs-keyword">if</span> [ <span class="hljs-string">"$&#123;counter&#125;"</span> = <span class="hljs-string">"0"</span> ]; then
    #则停止keepalived进程，迫使虚拟IP转移到备机上，完成故障转移（该命令需要根据实际情况修改）
    systemctl stop keepalived.service
fi

<span class="hljs-comment">// 主服务器etc目录下的hosts文件加上一下这行</span>
<span class="hljs-number">127.0</span><span class="hljs-number">.0</span><span class="hljs-number">.1</span>   MASTER

<span class="hljs-comment">// 备份服务器etc目录下的hosts文件加上一下这行</span>
<span class="hljs-number">127.0</span><span class="hljs-number">.0</span><span class="hljs-number">.1</span>   BACKUP

<span class="hljs-comment">// 主服务器与备份服务器nginx配置文件中均加上一下这段转发配置</span>
server &#123;
    listen <span class="hljs-number">9010</span>;
    server_name <span class="hljs-number">127.0</span><span class="hljs-number">.0</span><span class="hljs-number">.1</span>;

    location ~ <span class="hljs-regexp">/demo/</span> &#123;
        proxy_pass http:<span class="hljs-comment">//127.0.0.1:8080;</span>
    &#125;
&#125;

<span class="hljs-comment">// 主服务器下tomcat中webapps下的demo文件中index.html内容</span>
<html>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">head</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>高可用keepalived分发的主nginx服务器192.168.79.128转发到tomcat服务器上<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span></span>
    
<span class="hljs-comment">// 备份服务器下tomcat中webapps下的demo文件中index.html内容</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>高可用keepalived分发的备份nginx服务器192.168.79.129转发到tomcat服务器上<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>（4）、启动主和备份服务器上的nginx和keepalived服务，启动keepalived的命名为 systemctl start keepalived.service</p>
<p>（5）、访问虚拟ip <a href="https://link.juejin.cn/?target=http%3A%2F%2F192.168.79.100%3A9010%2Fdemo%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="http://192.168.79.100:9010/demo/index.html" ref="nofollow noopener noreferrer">http://192.168.79.100:9010/demo/index.html</a> ，可以看到访问到的是主服务上的nginx转发到的tomcat服务器</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e47ffa93be6149c6b4847990777022c7~tplv-k3u1fbpfcp-watermark.image" alt="keepalived访问主服务器的nginx.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​        在主服务器192.168.79.128中运行ip addr，可以看到虚拟ip当前指向的是主服务器ip</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff96da6eeec94eb49adf8f287a38d09d~tplv-k3u1fbpfcp-watermark.image" alt="查看虚拟ip绑定的真实服务器ip.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（6）、停掉主服务器的nginx服务，nginx_check脚本将会去停止掉keepalived，再次访问虚拟ip  192.168.79.100，访问ip会漂移到备份服务器192.168.79.129上</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/415dad5907f54fd3ad65306904d9601b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210713162735969.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在备份服务器上运行 ip addr 可以看到虚拟ip此时绑定的是备份服务器的ip</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abf47c78503740408a94bc8048b0aaa4~tplv-k3u1fbpfcp-watermark.image" alt="主服务器nginx停止服务keepalived会将请求漂移到备份服务器上.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">八、Nginx原理解析</h4>
<p>1、<strong>Nginx架构</strong>：Nginx 启动之后，在 Linux 系统中有两个进程，一个为 master，一个为 worker。master 作为管理员不参与任何工作，只负责给多个 worker 分配不同的任务(worker 一般有多个)。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1350d4a59f14ed385aee8163af11e90~tplv-k3u1fbpfcp-watermark.image" alt="Nginx架构.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2、<strong>worker 是如何工作的?</strong></p>
<p>客户端发送一个请求首先要经过 master，管理员收到请求后会将请求通知给 worker，多个 worker 以争抢的机制来抢夺任务，得到任务的 worker 会将请求经由 tomcat 等做请求转发、反向代理、访问数据库等(nginx 本身是不直接支持 java 的)。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1e70971eb3947549342e10f567adc3a~tplv-k3u1fbpfcp-watermark.image" alt="work工作过程.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>3、<strong>一个 master 和多个 worker 的好处</strong></p>
<p>（1）、可以使用 nginx -s reload 进行热部署，重启时正在工作的worker会继续完成工作，其他worker重新加载。</p>
<p>（2）、每个 worker 是独立的进程，如果其中一个 worker 出现问题，其它 worker 是独立运行的，会继续争抢任务，实现客户端的请求过程，而不会造成服务中断。</p>
<p>4、<strong>设置多少个 worker 合适</strong></p>
<p>Nginx 和 redis 类似，都采用了 io 多路复用机制（所以一般在linux服务器上部署Nginx和redis），每个 worker 都是一个独立的进程，每个进程里只有一个主线程，通过异步非阻塞的方式来处理请求，每个 worker 的线程可以把一个 cpu 的性能发挥到极致，因此，worker 数和服务器的 cpu 数相等是最为适宜的。</p></div>  
</div>
            