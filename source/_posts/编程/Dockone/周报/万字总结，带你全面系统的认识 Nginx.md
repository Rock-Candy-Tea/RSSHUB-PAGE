
---
title: '万字总结，带你全面系统的认识 Nginx'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/01b58cad0947c5c9b929055940f8525d.png'
author: Dockone
comments: false
date: 2021-04-13 12:10:45
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/01b58cad0947c5c9b929055940f8525d.png'
---

<div>   
<br>作为一名前端开发人员，你是不是经常碰到领导让你上服务器去修改 <code class="prettyprint">Nginx</code> 配置，然而你会以“我是前端，这个我不会”为理由搪塞过去呢！今天就让我们一起告别这种尴尬，向“真正”的程序员迈进！<br>
<h3>Nginx 概述</h3>  <code class="prettyprint">Nginx</code> 是开源、高性能、高可靠的 <code class="prettyprint">Web</code> 和反向代理服务器，而且支持热部署，几乎可以做到 7 * 24 小时不间断运行，即使运行几个月也不需要重新启动，还能在不间断服务的情况下对软件版本进行热更新。性能是  <code class="prettyprint">Nginx</code> 最重要的考量，其占用内存少、并发能力强、能支持高达 5w 个并发连接数，最重要的是，  <code class="prettyprint">Nginx</code> 是免费的并可以商业化，配置使用也比较简单。<br><br>
<h3>Nginx 特点</h3><ul><li>高并发、高性能；</li><li>模块化架构使得它的扩展性非常好；</li><li>异步非阻塞的事件驱动模型这点和 <code class="prettyprint">Node.js</code> 相似；</li><li>相对于其它服务器来说它可以连续几个月甚至更长而不需要重启服务器使得它具有高可靠性；</li><li>热部署、平滑升级；</li><li>完全开源，生态繁荣；</li></ul><br>
<br><h3>Nginx 作用</h3>Nginx 的最重要的几个使用场景：<br>
<ol><li>静态资源服务，通过本地文件系统提供服务；</li><li>反向代理服务，延伸出包括缓存、负载均衡等；</li><li><code class="prettyprint">API</code> 服务，<code class="prettyprint">OpenResty</code> ；</li></ol><br>
<br>对于前端来说 <code class="prettyprint">Node.js</code> 并不陌生，<code class="prettyprint">Nginx</code> 和 <code class="prettyprint">Node.js</code> 的很多理念类似，<code class="prettyprint">HTTP</code> 服务器、事件驱动、异步非阻塞等，且 <code class="prettyprint">Nginx</code> 的大部分功能使用 <code class="prettyprint">Node.js</code> 也可以实现，但 <code class="prettyprint">Nginx</code> 和  <code class="prettyprint">Node.js</code> 并不冲突，都有自己擅长的领域。<code class="prettyprint">Nginx</code> 擅长于底层服务器端资源的处理（静态资源处理转发、反向代理，负载均衡等），<code class="prettyprint">Node.js</code> 更擅长上层具体业务逻辑的处理，两者可以完美组合。  <br>
<br>用一张图表示：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/01b58cad0947c5c9b929055940f8525d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/01b58cad0947c5c9b929055940f8525d.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Nginx 安装</h3>本文演示的是 <code class="prettyprint">Linux</code> <code class="prettyprint">CentOS 7.x</code> 的操作系统上安装 <code class="prettyprint">Nginx</code>，至于在其它操作系统上进行安装可以网上自行搜索，都非常简单的。  <br>
<br>使用 <code class="prettyprint">yum</code> 安装 <code class="prettyprint">Nginx</code> ：<br>
<pre class="prettyprint">yum install nginx -y<br>
</pre><br>
安装完成后，通过 <code class="prettyprint">rpm -ql nginx</code> 命令查看 <code class="prettyprint">Nginx</code> 的安装信息：<br>
<pre class="prettyprint"># Nginx 配置文件<br>
/etc/nginx/nginx.conf # Nginx 主配置文件<br>
/etc/nginx/nginx.conf.default<br>
<br>
# 可执行程序文件<br>
/usr/bin/nginx-upgrade<br>
/usr/sbin/nginx<br>
<br>
# Nginx 库文件<br>
/usr/lib/systemd/system/nginx.service # 用于配置系统守护进程<br>
/usr/lib64/nginx/modules # Nginx 模块目录<br>
<br>
# 帮助文档<br>
/usr/share/doc/nginx-1.16.1<br>
/usr/share/doc/nginx-1.16.1/CHANGES<br>
/usr/share/doc/nginx-1.16.1/README<br>
/usr/share/doc/nginx-1.16.1/README.dynamic<br>
/usr/share/doc/nginx-1.16.1/UPGRADE-NOTES-1.6-to-1.10<br>
<br>
# 静态资源目录<br>
/usr/share/nginx/html/404.html<br>
/usr/share/nginx/html/50x.html<br>
/usr/share/nginx/html/index.html<br>
<br>
# 存放 Nginx 日志文件<br>
/var/log/nginx<br>
</pre><br>
主要关注的文件夹有两个：<br>
<ol><li><code class="prettyprint">/etc/nginx/conf.d/</code> 是子配置项存放处，<code class="prettyprint">/etc/nginx/nginx.conf</code> 主配置文件会默认把这个文件夹中所有子配置项都引入；</li><li><code class="prettyprint">/usr/share/nginx/html/</code> 静态文件都放在这个文件夹，也可以根据你自己的习惯放在其他地方。</li></ol><br>
<br><h3>Nginx 常用命令</h3><code class="prettyprint">systemctl</code> 系统命令：<br>
<pre class="prettyprint"># 开机配置<br>
systemctl enable nginx # 开机自动启动<br>
systemctl disable nginx # 关闭开机自动启动<br>
<br>
# 启动 Nginx<br>
systemctl start nginx # 启动Nginx成功后，可以直接访问主机IP，此时会展示Nginx默认页面<br>
<br>
# 停止 Nginx<br>
systemctl stop nginx<br>
<br>
# 重启 Nginx<br>
systemctl restart nginx<br>
<br>
# 重新加载 Nginx<br>
systemctl reload nginx<br>
<br>
# 查看 Nginx 运行状态<br>
systemctl status nginx<br>
<br>
# 查看 Nginx 进程<br>
ps -ef | grep nginx<br>
<br>
# 杀死 Nginx 进程<br>
kill -9 pid # 根据上面查看到的 Nginx 进程号，杀死 Nginx 进程，-9 表示强制结束进程<br>
</pre><br>
<code class="prettyprint">Nginx</code> 应用程序命令：<br>
<pre class="prettyprint">nginx -s reload  # 向主进程发送信号，重新加载配置文件，热重启<br>
nginx -s reopen  # 重启 Nginx<br>
nginx -s stop    # 快速关闭<br>
nginx -s quit    # 等待工作进程处理完成后关闭<br>
nginx -T         # 查看当前 Nginx 最终的配置<br>
nginx -t         # 检查配置是否有问题<br>
</pre><br>
<h3>Nginx 核心配置</h3><h4>配置文件结构</h4><code class="prettyprint">Nginx</code> 的典型配置示例：<br>
<pre class="prettyprint"># main段配置信息<br>
user  nginx;                        # 运行用户，默认即是 Nginx，可以不进行设置<br>
worker_processes  auto;             # Nginx 进程数，一般设置为和 CPU 核数一样<br>
error_log  /var/log/nginx/error.log warn;   # Nginx 的错误日志存放目录<br>
pid        /var/run/nginx.pid;      # Nginx 服务启动时的 pid 存放位置<br>
<br>
# events段配置信息<br>
events &#123;<br>
use epoll;     # 使用 epoll 的 I/O 模型（如果你不知道 Nginx 该使用哪种轮询方法，会自动选择一个最适合你操作系统的）<br>
worker_connections 1024;   # 每个进程允许最大并发数<br>
&#125;<br>
<br>
# http 段配置信息<br>
# 配置使用最频繁的部分，代理、缓存、日志定义等绝大多数功能和第三方模块的配置都在这里设置<br>
http &#123; <br>
# 设置日志模式<br>
log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '<br>
                  '$status $body_bytes_sent "$http_referer" '<br>
                  '"$http_user_agent" "$http_x_forwarded_for"';<br>
<br>
access_log  /var/log/nginx/access.log  main;   # Nginx 访问日志存放位置<br>
<br>
sendfile            on;   # 开启高效传输模式<br>
tcp_nopush          on;   # 减少网络报文段的数量<br>
tcp_nodelay         on;<br>
keepalive_timeout   65;   # 保持连接的时间，也叫超时时间，单位秒<br>
types_hash_max_size 2048;<br>
<br>
include             /etc/nginx/mime.types;      # 文件扩展名与类型映射表<br>
default_type        application/octet-stream;   # 默认文件类型<br>
<br>
include /etc/nginx/conf.d/*.conf;   # 加载子配置项<br>
<br>
# server段配置信息<br>
server &#123;<br>
    listen       80;       # 配置监听的端口<br>
    server_name  localhost;    # 配置的域名<br>
<br>
    # location段配置信息<br>
    location / &#123;<br>
        root   /usr/share/nginx/html;  # 网站根目录<br>
        index  index.html index.htm;   # 默认首页文件<br>
        deny 172.168.22.11;   # 禁止访问的 ip 地址，可以为 all<br>
        allow 172.168.33.44；# 允许访问的 ip 地址，可以为 all<br>
    &#125;<br>
<br>
    error_page 500 502 503 504 /50x.html;  # 默认 50x 对应的访问页面<br>
    error_page 400 404 error.html;   # 同上<br>
&#125;<br>
&#125; <br>
</pre><br>
<ul><li><code class="prettyprint">main</code> 全局配置，对全局生效；</li><li><code class="prettyprint">events</code> 配置影响 <code class="prettyprint">Nginx</code> 服务器与用户的网络连接；</li><li><code class="prettyprint">http</code> 配置代理，缓存，日志定义等绝大多数功能和第三方模块的配置；</li><li><code class="prettyprint">server</code> 配置虚拟主机的相关参数，一个 <code class="prettyprint">http</code> 块中可以有多个 <code class="prettyprint">server</code> 块；</li><li><code class="prettyprint">location</code> 用于配置匹配的 <code class="prettyprint">uri</code> ；</li><li><code class="prettyprint">upstream</code> 配置后端服务器具体地址，负载均衡配置不可或缺的部分。</li></ul><br>
<br>用一张图清晰的展示它的层级结构：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/daf9b95ca8db8b2218f9eba1585810fc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/daf9b95ca8db8b2218f9eba1585810fc.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>配置文件 main 段核心参数</h4><strong>user</strong><br>
<br>指定运行 <code class="prettyprint">Nginx</code> 的 <code class="prettyprint">woker</code> 子进程的属主和属组，其中组可以不指定。<br>
<pre class="prettyprint">user USERNAME [GROUP]<br>
<br>
user nginx lion; # 用户是 Nginx；组是 lion<br>
</pre><br>
<strong>pid</strong><br>
<br>指定运行 <code class="prettyprint">Nginx</code> <code class="prettyprint">master</code> 主进程的 <code class="prettyprint">pid</code> 文件存放路径。<br>
<pre class="prettyprint">pid /opt/nginx/logs/nginx.pid # master主进程的的 pid 存放在 nginx.pid 的文件<br>
</pre><br>
<strong>worker_rlimit_nofile_number</strong><br>
<br>指定 <code class="prettyprint">worker</code> 子进程可以打开的最大文件句柄数。<br>
<pre class="prettyprint">worker_rlimit_nofile 20480; # 可以理解成每个 worker 子进程的最大连接数量。<br>
</pre><br>
<strong>worker_rlimit_core</strong><br>
<br>指定 <code class="prettyprint">worker</code> 子进程异常终止后的 <code class="prettyprint">core</code> 文件，用于记录分析问题。<br>
<pre class="prettyprint">worker_rlimit_core 50M; # 存放大小限制<br>
working_directory /opt/nginx/tmp; # 存放目录<br>
</pre><br>
<strong>worker_processes_number</strong><br>
<br>指定 <code class="prettyprint">Nginx</code> 启动的 <code class="prettyprint">worker</code> 子进程数量。<br>
<pre class="prettyprint">worker_processes 4; # 指定具体子进程数量<br>
worker_processes auto; # 与当前 CPU 物理核心数一致<br>
</pre><br>
<strong>worker_cpu_affinity</strong><br>
<br>将每个 <code class="prettyprint">worker</code> 子进程与我们的 <code class="prettyprint">CPU</code> 物理核心绑定。<br>
<pre class="prettyprint">worker_cpu_affinity 0001 0010 0100 1000; # 4个物理核心，4个 worker 子进程<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/4536ed4c436a19d4ede21f3260df68b7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/4536ed4c436a19d4ede21f3260df68b7.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
将每个 <code class="prettyprint">worker</code> 子进程与特定 <code class="prettyprint">CPU</code> 物理核心绑定，优势在于，避免同一个 <code class="prettyprint">worker</code> 子进程在不同的 <code class="prettyprint">CPU</code> 核心上切换，缓存失效，降低性能。但其并不能真正的避免进程切换。  <br>
<br><strong>worker_priority</strong><br>
<br>指定 <code class="prettyprint">worker</code> 子进程的 <code class="prettyprint">nice</code> 值，以调整运行 <code class="prettyprint">Nginx</code> 的优先级，通常设定为负值，以优先调用 <code class="prettyprint">Nginx</code> 。<br>
<pre class="prettyprint">worker_priority -10; # 120-10=110，110 就是最终的优先级<br>
</pre><br>
<code class="prettyprint">Linux</code> 默认进程的优先级值是 120，值越小越优先；  <code class="prettyprint">nice</code> 定范围为 <code class="prettyprint">-20</code> 到 <code class="prettyprint">+19</code> 。  <br>
<br>[备注] 应用的默认优先级值是 120 加上 <code class="prettyprint">nice</code> 值等于它最终的值，这个值越小，优先级越高。  <br>
<br><strong>worker_shutdown_timeout</strong><br>
<br>指定 <code class="prettyprint">worker</code> 子进程优雅退出时的超时时间。<br>
<pre class="prettyprint">worker_shutdown_timeout 5s;<br>
</pre><br>
<strong>timer_resolution</strong><br>
<br><code class="prettyprint">worker</code> 子进程内部使用的计时器精度，调整时间间隔越大，系统调用越少，有利于性能提升；反之，系统调用越多，性能下降。<br>
<pre class="prettyprint">timer_resolution 100ms;<br>
</pre><br>
在 <code class="prettyprint">Linux</code> 系统中，用户需要获取计时器时需要向操作系统内核发送请求，有请求就必然会有开销，因此这个间隔越大开销就越小。  <br>
<br><strong>daemon</strong><br>
<br>指定 <code class="prettyprint">Nginx</code> 的运行方式，前台还是后台，前台用于调试，后台用于生产。<br>
<pre class="prettyprint">daemon off; # 默认是 on，后台运行模式<br>
</pre><br>
<h4>配置文件 events 段核心参数</h4><strong>use</strong><br>
<br><code class="prettyprint">Nginx</code> 使用何种事件驱动模型。<br>
<pre class="prettyprint">use method; # 不推荐配置它，让 Nginx 自己选择<br>
<br>
method 可选值为：select、poll、kqueue、epoll、/dev/poll、eventport<br>
</pre><br>
<strong>worker_connections</strong><br>
<br><code class="prettyprint">worker</code> 子进程能够处理的最大并发连接数。<br>
<pre class="prettyprint">worker_connections 1024 # 每个子进程的最大连接数为 1024<br>
</pre><br>
<strong>accept_mutex</strong><br>
<br>是否打开负载均衡互斥锁。<br>
<pre class="prettyprint">accept_mutex on # 默认是 off 关闭的，这里推荐打开<br>
</pre><br>
<h4>server_name 指令</h4>指定虚拟主机域名。<br>
<pre class="prettyprint">server_name name1 name2 name3<br>
<br>
# 示例：<br>
server_name www.nginx.com;<br>
</pre><br>
域名匹配的四种写法：<br>
<ul><li>精确匹配：<code class="prettyprint">server_name www.nginx.com</code> ;</li><li>左侧通配：<code class="prettyprint">server_name *.nginx.com</code> ;</li><li>右侧统配：<code class="prettyprint">server_name www.nginx.*</code> ;</li><li>正则匹配：<code class="prettyprint">server_name ~^www\.nginx\.*$</code> ;</li></ul><br>
<br>匹配优先级：<strong>精确匹配 > 左侧通配符匹配 > 右侧通配符匹配 > 正则表达式匹配</strong><br>
<br><code class="prettyprint">server_name</code> 配置实例：  <br>
<br>1、配置本地  <code class="prettyprint">DNS</code> 解析 <code class="prettyprint">vim /etc/hosts</code> （  <code class="prettyprint">macOS</code> 系统）<br>
<pre class="prettyprint"># 添加如下内容，其中 121.42.11.34 是阿里云服务器 IP 地址<br>
121.42.11.34 www.nginx-test.com<br>
121.42.11.34 mail.nginx-test.com<br>
121.42.11.34 www.nginx-test.org<br>
121.42.11.34 doc.nginx-test.com<br>
121.42.11.34 www.nginx-test.cn<br>
121.42.11.34 fe.nginx-test.club<br>
</pre><br>
[注意] 这里使用的是虚拟域名进行测试，因此需要配置本地 <code class="prettyprint">DNS</code> 解析，如果使用阿里云上购买的域名，则需要在阿里云上设置好域名解析。  <br>
<br>2、配置阿里云 <code class="prettyprint">Nginx</code> ，<code class="prettyprint">vim/etc/nginx/nginx.conf</code><br>
<pre class="prettyprint"># 这里只列举了 http 端中的 sever 端配置<br>
<br>
# 左匹配<br>
server &#123;<br>
listen  80;<br>
server_name *.nginx-test.com;<br>
root    /usr/share/nginx/html/nginx-test/left-match/;<br>
location / &#123;<br>
    index index.html;<br>
&#125;<br>
&#125;<br>
<br>
# 正则匹配<br>
server &#123;<br>
listen  80;<br>
server_name ~^.*\.nginx-test\..*$;<br>
root    /usr/share/nginx/html/nginx-test/reg-match/;<br>
location / &#123;<br>
    index index.html;<br>
&#125;<br>
&#125;<br>
<br>
# 右匹配<br>
server &#123;<br>
listen  80;<br>
server_name www.nginx-test.*;<br>
root    /usr/share/nginx/html/nginx-test/right-match/;<br>
location / &#123;<br>
    index index.html;<br>
&#125;<br>
&#125;<br>
<br>
# 完全匹配<br>
server &#123;<br>
listen  80;<br>
server_name www.nginx-test.com;<br>
root    /usr/share/nginx/html/nginx-test/all-match/;<br>
location / &#123;<br>
    index index.html;<br>
&#125;<br>
&#125; <br>
</pre><br>
3、访问分析<br>
<ul><li>当访问 <code class="prettyprint">www.nginx-test.com</code> 时，都可以被匹配上，因此选择优先级最高的“完全匹配”；</li><li>当访问 <code class="prettyprint">mail.nginx-test.com</code> 时，会进行“左匹配”；</li><li>当访问 <code class="prettyprint">www.nginx-test.org</code> 时，会进行“右匹配”；</li><li>当访问 <code class="prettyprint">doc.nginx-test.com</code> 时，会进行“左匹配”；</li><li>当访问 <code class="prettyprint">www.nginx-test.cn</code> 时，会进行“右匹配”；</li><li>当访问 <code class="prettyprint">fe.nginx-test.club</code> 时，会进行“正则匹配”；</li></ul><br>
<br><h4>root</h4>指定静态资源目录位置，它可以写在 <code class="prettyprint">http</code>、<code class="prettyprint">server</code>、<code class="prettyprint">location</code> 等配置中。<br>
<pre class="prettyprint">root path<br>
<br>
例如：<br>
location /image &#123;<br>
root /opt/nginx/static;<br>
&#125;<br>
<br>
当用户访问 www.test.com/image/1.png 时，实际在服务器找的路径是 /opt/nginx/static/image/1.png<br>
</pre><br>
[注意]  <code class="prettyprint">root</code> 会将定义路径与 <code class="prettyprint">URI</code> 叠加，<code class="prettyprint">alias</code> 则只取定义路径。<br><br>
<h4>alias</h4>它也是指定静态资源目录位置，它只能写在 <code class="prettyprint">location</code> 中。<br>
<pre class="prettyprint">location /image &#123;<br>
alias /opt/nginx/static/image/;<br>
&#125;<br>
<br>
当用户访问 www.test.com/image/1.png 时，实际在服务器找的路径是 /opt/nginx/static/image/1.png<br>
</pre><br>
[注意] 使用 alias 末尾一定要添加 <code class="prettyprint">/</code> ，并且它只能位于 <code class="prettyprint">location</code> 中。<br>
<h4>location</h4>配置路径。<br>
<pre class="prettyprint">location [ = | ~ | ~* | ^~ ] uri &#123;<br>
...<br>
&#125; <br>
</pre><br>
匹配规则：<br>
<ul><li><code class="prettyprint">=</code> 精确匹配；</li><li><code class="prettyprint">~</code> 正则匹配，区分大小写；</li><li><code class="prettyprint">~*</code> 正则匹配，不区分大小写；</li><li><code class="prettyprint">^~</code> 匹配到即停止搜索；</li></ul><br>
<br>匹配优先级：<code class="prettyprint">=</code> >  <code class="prettyprint">^~</code> >  <code class="prettyprint">~</code> >  <code class="prettyprint">~*</code> > 不带任何字符。  <br>
<br>实例：<br>
<pre class="prettyprint">server &#123;<br>
listen    80;<br>
server_name   www.nginx-test.com;<br>
<br>
# 只有当访问 www.nginx-test.com/match_all/ 时才会匹配到/usr/share/nginx/html/match_all/index.html<br>
location = /match_all/ &#123;<br>
  root  /usr/share/nginx/html<br>
  index index.html<br>
&#125;<br>
<br>
# 当访问 www.nginx-test.com/1.jpg 等路径时会去 /usr/share/nginx/images/1.jpg 找对应的资源<br>
location ~ \.(jpeg|jpg|png|svg)$ &#123;<br>
root /usr/share/nginx/images;<br>
&#125;<br>
<br>
# 当访问 www.nginx-test.com/bbs/ 时会匹配上 /usr/share/nginx/html/bbs/index.html<br>
location ^~ /bbs/ &#123;<br>
root /usr/share/nginx/html;<br>
index index.html index.htm;<br>
&#125;<br>
&#125; <br>
</pre><br>
<strong>location 中的反斜线</strong><br>
<pre class="prettyprint">location /test &#123;<br>
...<br>
&#125;<br>
<br>
location /test/ &#123;<br>
...<br>
&#125; <br>
</pre><br>
<ul><li>不带 <code class="prettyprint">/</code> 当访问 <code class="prettyprint">www.nginx-test.com/test</code> 时，  <code class="prettyprint">Nginx</code> 先找是否有 <code class="prettyprint">test</code> 目录，如果有则找 <code class="prettyprint">test</code> 目录下的 <code class="prettyprint">index.html</code>；如果没有 <code class="prettyprint">test</code> 目录，<code class="prettyprint">Nginx</code> 则会找是否有 <code class="prettyprint">test</code> 文件。</li><li>带 <code class="prettyprint">/</code> 当访问 <code class="prettyprint">www.nginx-test.com/test</code> 时，<code class="prettyprint">Nginx</code> 先找是否有 <code class="prettyprint">test</code> 目录，如果有则找 <code class="prettyprint">test</code> 目录下的 <code class="prettyprint">index.html</code>，如果没有它也不会去找是否存在 <code class="prettyprint">test</code> 文件。</li></ul><br>
<br><strong>return</strong><br>
<br>停止处理请求，直接返回响应码或重定向到其他 <code class="prettyprint">URL</code> ；执行 <code class="prettyprint">return</code> 指令后，<code class="prettyprint">location</code> 中后续指令将不会被执行。<br><br>
<pre class="prettyprint">return code [text];<br>
return code URL;<br>
return URL;<br>
<br>
例如：<br>
location / &#123;<br>
return 404; # 直接返回状态码<br>
&#125;<br>
<br>
location / &#123;<br>
return 404 "pages not found"; # 返回状态码 + 一段文本<br>
&#125;<br>
<br>
location / &#123;<br>
return 302 /bbs ; # 返回状态码 + 重定向地址<br>
&#125;<br>
<br>
location / &#123;<br>
return https://www.baidu.com ; # 返回重定向地址<br>
&#125; <br>
</pre><br>
<h4>rewrite</h4>根据指定正则表达式匹配规则，重写 <code class="prettyprint">URL</code> 。<br>
<pre class="prettyprint">语法：rewrite 正则表达式 要替换的内容 [flag];<br>
<br>
上下文：server、location、if<br>
<br>
示例：rewirte /images/(.*\.jpg)$ /pic/$1; # $1是前面括号(.*\.jpg)的反向引用<br>
</pre><br>
<code class="prettyprint">flag</code> 可选值的含义：<br>
<ul><li><code class="prettyprint">last</code> 重写后的 <code class="prettyprint">URL</code> 发起新请求，再次进入 <code class="prettyprint">server</code> 段，重试 <code class="prettyprint">location</code> 的中的匹配；</li><li><code class="prettyprint">break</code> 直接使用重写后的 <code class="prettyprint">URL</code> ，不再匹配其它 <code class="prettyprint">location</code> 中语句；</li><li><code class="prettyprint">redirect</code> 返回 302 临时重定向；</li><li><code class="prettyprint">permanent</code> 返回 301 永久重定向；</li></ul><br>
<br><pre class="prettyprint">server&#123;<br>
listen 80;<br>
server_name fe.lion.club; # 要在本地 hosts 文件进行配置<br>
root html;<br>
location /search &#123;<br>
rewrite ^/(.*) https://www.baidu.com redirect;<br>
&#125;<br>
<br>
location /images &#123;<br>
rewrite /images/(.*) /pics/$1;<br>
&#125;<br>
<br>
location /pics &#123;<br>
rewrite /pics/(.*) /photos/$1;<br>
&#125;<br>
<br>
location /photos &#123;<br>
<br>
&#125;<br>
&#125; <br>
</pre><br>
按照这个配置我们来分析：<br>
<ul><li>当访问 <code class="prettyprint">fe.lion.club/search</code> 时，会自动帮我们重定向到 <code class="prettyprint">https://www.baidu.com</code>。</li><li>当访问 <code class="prettyprint">fe.lion.club/images/1.jpg</code> 时，第一步重写 <code class="prettyprint">URL</code> 为 <code class="prettyprint">fe.lion.club/pics/1.jpg</code>，找到 <code class="prettyprint">pics</code> 的 <code class="prettyprint">location</code>，继续重写 <code class="prettyprint">URL</code> 为 <code class="prettyprint">fe.lion.club/photos/1.jpg</code>，找到 <code class="prettyprint">/photos</code> 的 <code class="prettyprint">location</code> 后，去 <code class="prettyprint">html/photos</code> 目录下寻找 <code class="prettyprint">1.jpg</code> 静态资源。</li></ul><br>
<br><h4>if 指令</h4><pre class="prettyprint">语法：if (condition) &#123;...&#125;<br>
<br>
上下文：server、location<br>
<br>
示例：<br>
if($http_user_agent ~ Chrome)&#123;<br>
rewrite /(.*)/browser/$1 break;<br>
&#125; <br>
</pre><br>
<code class="prettyprint">condition</code> 判断条件：<br>
<ul><li><code class="prettyprint">$variable</code> 仅为变量时，值为空或以 0 开头字符串都会被当做 <code class="prettyprint">false</code> 处理；</li><li><code class="prettyprint">=</code> 或 <code class="prettyprint">!=</code> 相等或不等；</li><li><code class="prettyprint">~</code> 正则匹配；</li><li><code class="prettyprint">! ~</code> 非正则匹配；</li><li><code class="prettyprint">~*</code> 正则匹配，不区分大小写；</li><li><code class="prettyprint">-f</code> 或 <code class="prettyprint">! -f</code> 检测文件存在或不存在；</li><li><code class="prettyprint">-d</code> 或 <code class="prettyprint">! -d</code> 检测目录存在或不存在；</li><li><code class="prettyprint">-e</code> 或 <code class="prettyprint">! -e</code> 检测文件、目录、符号链接等存在或不存在；</li><li><code class="prettyprint">-x</code> 或 <code class="prettyprint">! -x</code> 检测文件可以执行或不可执行；</li></ul><br>
<br>实例：<br>
<pre class="prettyprint">server &#123;<br>
listen 8080;<br>
server_name localhost;<br>
root html;<br>
<br>
location / &#123;<br>
if ( $uri = "/images/" )&#123;<br>
    rewrite (.*) /pics/ break;<br>
&#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
当访问 <code class="prettyprint">localhost:8080/images/</code> 时，会进入 <code class="prettyprint">if</code> 判断里面执行 <code class="prettyprint">rewrite</code> 命令。<br>
<h4>autoindex</h4>用户请求以 <code class="prettyprint">/</code> 结尾时，列出目录结构，可以用于快速搭建静态资源下载网站。  <br>
<br><code class="prettyprint">autoindex.conf</code> 配置信息：<br>
<pre class="prettyprint">server &#123;<br>
listen 80;<br>
server_name fe.lion-test.club;<br>
<br>
location /download/ &#123;<br>
root /opt/source;<br>
<br>
autoindex on; # 打开 autoindex，，可选参数有 on | off<br>
autoindex_exact_size on; # 修改为 off，以 KB、MB、GB 显示文件大小，默认为 on，以 bytes 显示出⽂件的确切⼤⼩<br>
autoindex_format html; # 以 html 的方式进行格式化，可选参数有 html | json | xml<br>
autoindex_localtime off; # 显示的⽂件时间为⽂件的服务器时间。默认为 off，显示的⽂件时间为GMT时间<br>
&#125;<br>
&#125; <br>
</pre><br>
当访问 <code class="prettyprint">fe.lion.com/download/</code> 时，会把服务器 <code class="prettyprint">/opt/source/download/</code> 路径下的文件展示出来，如下图所示：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/fcfdd55f0d10f345e0c1998dbe91b7f0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/fcfdd55f0d10f345e0c1998dbe91b7f0.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>变量</h4><code class="prettyprint">Nginx</code> 提供给使用者的变量非常多，但是终究是一个完整的请求过程所产生数据，  <code class="prettyprint">Nginx</code> 将这些数据以变量的形式提供给使用者。  <br>
<br>下面列举些项目中常用的变量：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/69f6d69a0e127c8ddaaf7065c96dfced.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/69f6d69a0e127c8ddaaf7065c96dfced.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
实例演示 <code class="prettyprint">var.conf</code> ：<br>
<pre class="prettyprint">server&#123;<br>
listen 8081;<br>
server_name var.lion-test.club;<br>
root /usr/share/nginx/html;<br>
location / &#123;<br>
    return 200 "<br>
remote_addr: $remote_addr<br>
remote_port: $remote_port<br>
server_addr: $server_addr<br>
server_port: $server_port<br>
server_protocol: $server_protocol<br>
binary_remote_addr: $binary_remote_addr<br>
connection: $connection<br>
uri: $uri<br>
request_uri: $request_uri<br>
scheme: $scheme<br>
request_method: $request_method<br>
request_length: $request_length<br>
args: $args<br>
arg_pid: $arg_pid<br>
is_args: $is_args<br>
query_string: $query_string<br>
host: $host<br>
http_user_agent: $http_user_agent<br>
http_referer: $http_referer<br>
http_via: $http_via<br>
request_time: $request_time<br>
https: $https<br>
request_filename: $request_filename<br>
document_root: $document_root<br>
";<br>
&#125;<br>
&#125; <br>
</pre><br>
当我们访问 <code class="prettyprint">http://var.lion-test.club:8081/test?pid=121414&amp;cid=sadasd</code> 时，由于 <code class="prettyprint">Nginx</code> 中写了 <code class="prettyprint">return</code> 方法，因此 <code class="prettyprint">chrome</code> 浏览器会默认为我们下载一个文件，下面展示的就是下载的文件内容：<br>
<pre class="prettyprint">remote_addr: 27.16.220.84<br>
remote_port: 56838<br>
server_addr: 172.17.0.2<br>
server_port: 8081<br>
server_protocol: HTTP/1.1<br>
binary_remote_addr: 茉<br>
connection: 126<br>
uri: /test/<br>
request_uri: /test/?pid=121414&cid=sadasd<br>
scheme: http<br>
request_method: GET<br>
request_length: 518<br>
args: pid=121414&cid=sadasd<br>
arg_pid: 121414<br>
is_args: ?<br>
query_string: pid=121414&cid=sadasd<br>
host: var.lion-test.club<br>
http_user_agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36<br>
http_referer: <br>
http_via: <br>
request_time: 0.000<br>
https: <br>
request_filename: /usr/share/nginx/html/test/<br>
document_root: /usr/share/nginx/html<br>
</pre><br>
<code class="prettyprint">Nginx</code> 的配置还有非常多，以上只是罗列了一些常用的配置，在实际项目中还是要学会查阅文档。<br><br>
<h3>Nginx 应用核心概念</h3>代理是在服务器和客户端之间假设的一层服务器，代理将接收客户端的请求并将它转发给服务器，然后将服务端的响应转发给客户端。  <br>
<br>不管是正向代理还是反向代理，实现的都是上面的功能。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/c4436f5cb76b4f5209c158fcaaf4f3e6.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/c4436f5cb76b4f5209c158fcaaf4f3e6.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>正向代理</h4>正向代理，意思是一个位于客户端和原始服务器（origin server）之间的服务器，为了从原始服务器取得内容，客户端向代理发送一个请求并指定目标（原始服务器），然后代理向原始服务器转交请求并将获得的内容返回给客户端。<br>
<br>正向代理是为我们服务的，即为客户端服务的，客户端可以根据正向代理访问到它本身无法访问到的服务器资源。  <br>
<br>正向代理对我们是透明的，对服务端是非透明的，即服务端并不知道自己收到的是来自代理的访问还是来自真实客户端的访问。<br><br>
<h4>反向代理</h4>反向代理（Reverse Proxy）方式是指以代理服务器来接受 internet 上的连接请求，然后将请求转发给内部网络上的服务器，并将从服务器上得到的结果返回给 internet 上请求连接的客户端，此时代理服务器对外就表现为一个反向代理服务器。<br>
<br>反向代理是为服务端服务的，反向代理可以帮助服务器接收来自客户端的请求，帮助服务器做请求转发，负载均衡等。  <br>
<br>反向代理对服务端是透明的，对我们是非透明的，即我们并不知道自己访问的是代理服务器，而服务器知道反向代理在为他服务。  <br>
<br>反向代理的优势：<br>
<ul><li>隐藏真实服务器；</li><li>负载均衡便于横向扩充后端动态服务；</li><li>动静分离，提升系统健壮性；</li></ul><br>
<br>那么“动静分离”是什么？负载均衡又是什么？<br><br>
<h4>动静分离</h4>动静分离是指在 <code class="prettyprint">web</code> 服务器架构中，将静态页面与动态页面或者静态内容接口和动态内容接口分开不同系统访问的架构设计方法，进而提示整个服务的访问性和可维护性。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/c1c73df37a799c7cfa03861e43984049.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/c1c73df37a799c7cfa03861e43984049.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
一般来说，都需要将动态资源和静态资源分开，由于 <code class="prettyprint">Nginx</code> 的高并发和静态资源缓存等特性，经常将静态资源部署在 <code class="prettyprint">Nginx</code> 上。如果请求的是静态资源，直接到静态资源目录获取资源，如果是动态资源的请求，则利用反向代理的原理，把请求转发给对应后台应用去处理，从而实现动静分离。  <br>
<br>使用前后端分离后，可以很大程度提升静态资源的访问速度，即使动态服务不可用，静态资源的访问也不会受到影响。<br><br>
<h4>负载均衡</h4>一般情况下，客户端发送多个请求到服务器，服务器处理请求，其中一部分可能要操作一些资源比如数据库、静态资源等，服务器处理完毕后，再将结果返回给客户端。  <br>
<br>这种模式对于早期的系统来说，功能要求不复杂，且并发请求相对较少的情况下还能胜任，成本也低。随着信息数量不断增长，访问量和数据量飞速增长，以及系统业务复杂度持续增加，这种做法已无法满足要求，并发量特别大时，服务器容易崩。  <br>
<br>很明显这是由于服务器性能的瓶颈造成的问题，除了堆机器之外，最重要的做法就是负载均衡。  <br>
<br>请求爆发式增长的情况下，单个机器性能再强劲也无法满足要求了，这个时候集群的概念产生了，单个服务器解决不了的问题，可以使用多个服务器，然后将请求分发到各个服务器上，将负载分发到不同的服务器，这就是负载均衡，核心是「分摊压力」。<code class="prettyprint">Nginx</code> 实现负载均衡，一般来说指的是将请求转发给服务器集群。  <br>
<br>举个具体的例子，晚高峰乘坐地铁的时候，入站口经常会有地铁工作人员大喇叭“请走 <code class="prettyprint">B</code> 口，  <code class="prettyprint">B</code> 口人少车空……”，这个工作人员的作用就是负载均衡。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/de52db9061b5f94d0c95f1a92efc368c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/de52db9061b5f94d0c95f1a92efc368c.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<code class="prettyprint">Nginx</code> 实现负载均衡的策略：<br>
<ul><li>轮询策略：默认情况下采用的策略，将所有客户端请求轮询分配给服务端。这种策略是可以正常工作的，但是如果其中某一台服务器压力太大，出现延迟，会影响所有分配在这台服务器下的用户。</li><li>最小连接数策略：将请求优先分配给压力较小的服务器，它可以平衡每个队列的长度，并避免向压力大的服务器添加更多的请求。</li><li>最快响应时间策略：优先分配给响应时间最短的服务器。</li><li>客户端 <code class="prettyprint">ip</code> 绑定策略：来自同一个 <code class="prettyprint">ip</code> 的请求永远只分配一台服务器，有效解决了动态网页存在的 <code class="prettyprint">session</code> 共享问题。</li></ul><br>
<br><h3>Nginx 实战配置</h3>在配置反向代理和负载均衡等等功能之前，有两个核心模块是我们必须要掌握的，这两个模块应该说是 <code class="prettyprint">Nginx</code> 应用配置中的核心，它们分别是： <code class="prettyprint">upstream</code>、<code class="prettyprint">proxy_pass</code>。<br>
<h4>upstream</h4>用于定义上游服务器（指的就是后台提供的应用服务器）的相关信息。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/6d1735743aa01631724894f7edd97855.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/6d1735743aa01631724894f7edd97855.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<pre class="prettyprint">语法：upstream name &#123;<br>
...<br>
&#125;<br>
<br>
上下文：http<br>
<br>
示例：<br>
upstream back_end_server&#123;<br>
server 192.168.100.33:8081<br>
&#125; <br>
</pre><br>
在 <code class="prettyprint">upstream</code> 内可使用的指令：<br>
<ul><li><code class="prettyprint">server</code> 定义上游服务器地址；</li><li><code class="prettyprint">zone</code> 定义共享内存，用于跨 <code class="prettyprint">worker</code> 子进程；</li><li><code class="prettyprint">keepalive</code> 对上游服务启用长连接；</li><li><code class="prettyprint">keepalive_requests</code> 一个长连接最多请求 <code class="prettyprint">HTTP</code> 的个数；</li><li><code class="prettyprint">keepalive_timeout</code> 空闲情形下，一个长连接的超时时长；</li><li><code class="prettyprint">hash</code> 哈希负载均衡算法；</li><li><code class="prettyprint">ip_hash</code> 依据  <code class="prettyprint">IP</code> 进行哈希计算的负载均衡算法；</li><li><code class="prettyprint">least_conn</code> 最少连接数负载均衡算法；</li><li><code class="prettyprint">least_time</code> 最短响应时间负载均衡算法；</li><li><code class="prettyprint">random</code> 随机负载均衡算法；</li></ul><br>
<br><strong>server</strong><br>
<br>定义上游服务器地址。<br>
<pre class="prettyprint">语法：server address [parameters]<br>
<br>
上下文：upstream<br>
</pre><br>
<code class="prettyprint">parameters</code> 可选值：<br>
<ul><li><code class="prettyprint">weight=number</code> 权重值，默认为 1；</li><li><code class="prettyprint">max_conns=number</code> 上游服务器的最大并发连接数；</li><li><code class="prettyprint">fail_timeout=time</code> 服务器不可用的判定时间；</li><li><code class="prettyprint">max_fails=numer</code> 服务器不可用的检查次数；</li><li><code class="prettyprint">backup</code> 备份服务器，仅当其他服务器都不可用时才会启用；</li><li><code class="prettyprint">down</code> 标记服务器长期不可用，离线维护；</li></ul><br>
<br><strong>keepalive</strong><br>
<br>限制每个 <code class="prettyprint">worker</code> 子进程与上游服务器空闲长连接的最大数量。<br>
<pre class="prettyprint">keepalive connections;<br>
<br>
上下文：upstream<br>
<br>
示例：keepalive 16;<br>
</pre><br>
<br><strong>keepalive_requests</strong><br>
<br>单个长连接可以处理的最多 <code class="prettyprint">HTTP</code> 请求个数。<br><br>
<pre class="prettyprint">语法：keepalive_requests number;<br>
<br>
默认值：keepalive_requests 100;<br>
<br>
上下文：upstream<br>
</pre><br>
<strong>keepalive_timeout</strong><br>
<br>空闲长连接的最长保持时间。<br><br>
<pre class="prettyprint">语法：keepalive_timeout time;<br>
<br>
默认值：keepalive_timeout 60s;<br>
<br>
上下文：upstream<br>
</pre><br>
<strong>配置实例</strong><br>
<pre class="prettyprint">upstream back_end&#123;<br>
server 127.0.0.1:8081 weight=3 max_conns=1000 fail_timeout=10s max_fails=2;<br>
keepalive 32;<br>
keepalive_requests 50;<br>
keepalive_timeout 30s;<br>
&#125; <br>
</pre><br>
<h4>proxy_pass</h4>用于配置代理服务器。<br>
<pre class="prettyprint">语法：proxy_pass URL;<br>
<br>
上下文：location、if、limit_except<br>
<br>
示例：<br>
proxy_pass http://127.0.0.1:8081<br>
proxy_pass http://127.0.0.1:8081/proxy<br>
</pre><br>
<code class="prettyprint">URL</code> 参数原则：<br>
<ol><li><code class="prettyprint">URL</code> 必须以 <code class="prettyprint">http</code> 或 <code class="prettyprint">https</code> 开头；</li><li><code class="prettyprint">URL</code> 中可以携带变量；</li><li><code class="prettyprint">URL</code> 中是否带 <code class="prettyprint">URI</code> ，会直接影响发往上游请求的 <code class="prettyprint">URL</code> ；</li></ol><br>
<br>接下来让我们来看看两种常见的 <code class="prettyprint">URL</code> 用法：<br>
<ol><li><code class="prettyprint">proxy_pass http://192.168.100.33:8081</code></li><li><code class="prettyprint">proxy_pass http://192.168.100.33:8081/</code></li></ol><br>
<br>这两种用法的区别就是带 <code class="prettyprint">/</code> 和不带 <code class="prettyprint">/</code> ，在配置代理时它们的区别可大了：<br>
<ul><li>不带 <code class="prettyprint">/</code> 意味着 <code class="prettyprint">Nginx</code> 不会修改用户 <code class="prettyprint">URL</code>，而是直接透传给上游的应用服务器；</li><li>带 <code class="prettyprint">/</code> 意味着 <code class="prettyprint">Nginx</code> 会修改用户 <code class="prettyprint">URL</code> ，修改方法是将 <code class="prettyprint">location</code> 后的 <code class="prettyprint">URL</code> 从用户 <code class="prettyprint">URL</code> 中删除；</li></ul><br>
<br>不带  <code class="prettyprint">/</code> 的用法：<br>
<pre class="prettyprint">location /bbs/&#123;<br>
proxy_pass http://127.0.0.1:8080;<br>
&#125; <br>
</pre><br>
分析：<br>
<ol><li>用户请求 <code class="prettyprint">URL</code>：<code class="prettyprint">/bbs/abc/test.html</code></li><li>请求到达 <code class="prettyprint">Nginx</code> 的  <code class="prettyprint">URL</code>：<code class="prettyprint">/bbs/abc/test.html</code></li><li>请求到达上游应用服务器的 <code class="prettyprint">URL</code> ：<code class="prettyprint">/bbs/abc/test.html</code></li></ol><br>
<br>带 <code class="prettyprint">/</code> 的用法：<br>
<pre class="prettyprint">location /bbs/&#123;<br>
proxy_pass http://127.0.0.1:8080/;<br>
&#125; <br>
</pre><br>
分析：<br>
<ol><li>用户请求 <code class="prettyprint">URL</code>：<code class="prettyprint">/bbs/abc/test.html</code></li><li>请求到达 <code class="prettyprint">Nginx</code> 的 <code class="prettyprint">URL</code>：<code class="prettyprint">/bbs/abc/test.html</code></li><li>请求到达上游应用服务器的 <code class="prettyprint">URL</code>：<code class="prettyprint">/abc/test.html</code></li></ol><br>
<br>并没有拼接上 <code class="prettyprint">/bbs</code>，这点和 <code class="prettyprint">root</code>与 <code class="prettyprint">alias</code> 之间的区别是保持一致的。<br>
<h4>配置反向代理</h4>这里为了演示更加接近实际，作者准备了两台云服务器，它们的公网 <code class="prettyprint">IP</code> 分别是：<code class="prettyprint">121.42.11.34</code> 与 <code class="prettyprint">121.5.180.193</code>。<br>
<br>我们把 <code class="prettyprint">121.42.11.34</code> 服务器作为上游服务器，做如下配置：<br>
<pre class="prettyprint"># /etc/nginx/conf.d/proxy.conf<br>
server&#123;<br>
listen 8080;<br>
server_name localhost;<br>
<br>
location /proxy/ &#123;<br>
root /usr/share/nginx/html/proxy;<br>
index index.html;<br>
&#125;<br>
&#125;<br>
<br>
# /usr/share/nginx/html/proxy/index.html<br>
<h1> 121.42.11.34 proxy html </h1><br>
</pre><br>
配置完成后重启 <code class="prettyprint">Nginx</code> 服务器 <code class="prettyprint">nginx -s reload</code>。  <br>
<br>把 <code class="prettyprint">121.5.180.193</code> 服务器作为代理服务器，做如下配置：<br>
<pre class="prettyprint"># /etc/nginx/conf.d/proxy.conf<br>
upstream back_end &#123;<br>
server 121.42.11.34:8080 weight=2 max_conns=1000 fail_timeout=10s max_fails=3;<br>
keepalive 32;<br>
keepalive_requests 80;<br>
keepalive_timeout 20s;<br>
&#125;<br>
<br>
server &#123;<br>
listen 80;<br>
server_name proxy.lion.club;<br>
location /proxy &#123;<br>
proxy_pass http://back_end/proxy;<br>
&#125;<br>
&#125; <br>
</pre><br>
本地机器要访问 <code class="prettyprint">proxy.lion.club</code> 域名，因此需要配置本地 <code class="prettyprint">hosts</code>，通过命令：<code class="prettyprint">vim /etc/hosts</code> 进入配置文件，添加如下内容：<br>
<pre class="prettyprint">121.5.180.193 proxy.lion.club<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/a4c024ac98d7de18490cf9ac4de93a78.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/a4c024ac98d7de18490cf9ac4de93a78.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
分析：<br>
<ol><li>当访问 <code class="prettyprint">proxy.lion.club/proxy</code> 时通过 <code class="prettyprint">upstream</code> 的配置找到 <code class="prettyprint">121.42.11.34:8080</code>；</li><li>因此访问地址变为 <code class="prettyprint">http://121.42.11.34:8080/proxy</code>；</li><li>连接到 <code class="prettyprint">121.42.11.34</code> 服务器，找到 <code class="prettyprint">8080</code> 端口提供的 <code class="prettyprint">server</code>；</li><li>通过 <code class="prettyprint">server</code> 找到 <code class="prettyprint">/usr/share/nginx/html/proxy/index.html</code> 资源，最终展示出来。</li></ol><br>
<br><h4>配置负载均衡</h4>配置负载均衡主要是要使用 <code class="prettyprint">upstream</code> 指令。<br>
<br>我们把 <code class="prettyprint">121.42.11.34</code> 服务器作为上游服务器，做如下配置（<code class="prettyprint">/etc/nginx/conf.d/balance.conf</code>）：<br>
<pre class="prettyprint">server&#123;<br>
listen 8020;<br>
location / &#123;<br>
return 200 'return 8020 \n';<br>
&#125;<br>
&#125;<br>
<br>
server&#123;<br>
listen 8030;<br>
location / &#123;<br>
return 200 'return 8030 \n';<br>
&#125;<br>
&#125;<br>
<br>
server&#123;<br>
listen 8040;<br>
location / &#123;<br>
return 200 'return 8040 \n';<br>
&#125;<br>
&#125; <br>
</pre><br>
配置完成后：<br>
<ol><li><code class="prettyprint">nginx -t</code> 检测配置是否正确；</li><li><code class="prettyprint">nginx -s reload</code> 重启 <code class="prettyprint">Nginx</code> 服务器；</li><li>执行 <code class="prettyprint">ss -nlt</code> 命令查看端口是否被占用，从而判断 <code class="prettyprint">Nginx</code> 服务是否正确启动。</li></ol><br>
<br>把 <code class="prettyprint">121.5.180.193</code> 服务器作为代理服务器，做如下配置（<code class="prettyprint">/etc/nginx/conf.d/balance.conf</code>）：<br>
<pre class="prettyprint">upstream demo_server &#123;<br>
server 121.42.11.34:8020;<br>
server 121.42.11.34:8030;<br>
server 121.42.11.34:8040;<br>
&#125;<br>
<br>
server &#123;<br>
listen 80;<br>
server_name balance.lion.club;<br>
<br>
location /balance/ &#123;<br>
proxy_pass http://demo_server;<br>
&#125;<br>
&#125; <br>
</pre><br>
配置完成后重启 <code class="prettyprint">Nginx</code> 服务器。并且在需要访问的客户端配置好 <code class="prettyprint">ip</code> 和域名的映射关系。<br>
<pre class="prettyprint"># /etc/hosts<br>
<br>
121.5.180.193 balance.lion.club<br>
</pre><br>
在客户端机器执行 <code class="prettyprint">curl http://balance.lion.club/balance/</code> 命令：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/36f74e6ade6751e4724edb175e0cd471.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/36f74e6ade6751e4724edb175e0cd471.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
不难看出，负载均衡的配置已经生效了，每次给我们分发的上游服务器都不一样。就是通过简单的轮询策略进行上游服务器分发。  <br>
<br>接下来，我们再来了解下 <code class="prettyprint">Nginx</code> 的其它分发策略。<br>
<br><strong>hash 算法</strong><br>
<br>通过制定关键字作为 <code class="prettyprint">hash key</code>，基于 <code class="prettyprint">hash</code> 算法映射到特定的上游服务器中。关键字可以包含有变量、字符串。<br>
<pre class="prettyprint">upstream demo_server &#123;<br>
hash $request_uri;<br>
server 121.42.11.34:8020;<br>
server 121.42.11.34:8030;<br>
server 121.42.11.34:8040;<br>
&#125;<br>
<br>
server &#123;<br>
listen 80;<br>
server_name balance.lion.club;<br>
<br>
location /balance/ &#123;<br>
proxy_pass http://demo_server;<br>
&#125;<br>
&#125; <br>
</pre><br>
<code class="prettyprint">hash $request_uri</code> 表示使用 <code class="prettyprint">request_uri</code> 变量作为 <code class="prettyprint">hash</code> 的 <code class="prettyprint">key</code> 值，只要访问的 <code class="prettyprint">URI</code> 保持不变，就会一直分发给同一台服务器。<br>
<br><strong>ip_hash</strong><br>
<br>根据客户端的请求 <code class="prettyprint">ip</code> 进行判断，只要 <code class="prettyprint">ip</code> 地址不变就永远分配到同一台主机。它可以有效解决后台服务器 <code class="prettyprint">session</code> 保持的问题。<br>
<pre class="prettyprint">upstream demo_server &#123;<br>
ip_hash;<br>
server 121.42.11.34:8020;<br>
server 121.42.11.34:8030;<br>
server 121.42.11.34:8040;<br>
&#125;<br>
<br>
server &#123;<br>
listen 80;<br>
server_name balance.lion.club;<br>
<br>
location /balance/ &#123;<br>
proxy_pass http://demo_server;<br>
&#125;<br>
&#125; <br>
</pre><br>
<strong>最少连接数算法</strong><br>
<br>各个 <code class="prettyprint">worker</code> 子进程通过读取共享内存的数据，来获取后端服务器的信息。来挑选一台当前已建立连接数最少的服务器进行分配请求。<br>
<pre class="prettyprint">语法：least_conn;<br>
<br>
上下文：upstream;<br>
</pre><br>
<br>示例：<br>
<pre class="prettyprint">upstream demo_server &#123;<br>
zone test 10M; # zone可以设置共享内存空间的名字和大小<br>
least_conn;<br>
server 121.42.11.34:8020;<br>
server 121.42.11.34:8030;<br>
server 121.42.11.34:8040;<br>
&#125;<br>
<br>
server &#123;<br>
listen 80;<br>
server_name balance.lion.club;<br>
<br>
location /balance/ &#123;<br>
proxy_pass http://demo_server;<br>
&#125;<br>
&#125; <br>
</pre><br>
最后你会发现，负载均衡的配置其实一点都不复杂。<br>
<h4>配置缓存</h4>缓存可以非常有效的提升性能，因此不论是客户端（浏览器），还是代理服务器（<code class="prettyprint">Nginx</code>），乃至上游服务器都多少会涉及到缓存。可见缓存在每个环节都是非常重要的。下面让我们来学习 <code class="prettyprint">Nginx</code> 中如何设置缓存策略。<br>
<br><strong>proxy_cache</strong><br>
<br>存储一些之前被访问过、而且可能将要被再次访问的资源，使用户可以直接从代理服务器获得，从而减少上游服务器的压力，加快整个访问速度。<br><br>
<pre class="prettyprint">语法：proxy_cache zone | off ; # zone 是共享内存的名称<br>
<br>
默认值：proxy_cache off;<br>
<br>
上下文：http、server、location<br>
</pre><br>
<strong>proxy_cache_path</strong><br>
<br>设置缓存文件的存放路径。<br>
<pre class="prettyprint">语法：proxy_cache_path path [level=levels] ...可选参数省略，下面会详细列举<br>
<br>
默认值：proxy_cache_path off<br>
<br>
上下文：http<br>
</pre><br>
参数含义：<br>
<ul><li><code class="prettyprint">path</code> 缓存文件的存放路径；</li><li><code class="prettyprint">level path</code> 的目录层级；</li><li><code class="prettyprint">keys_zone</code> 设置共享内存；</li><li><code class="prettyprint">inactive</code> 在指定时间内没有被访问，缓存会被清理，默认10分钟；</li></ul><br>
<br><strong>proxy_cache_key</strong><br>
<br>设置缓存文件的 <code class="prettyprint">key</code> 。<br>
<pre class="prettyprint">语法：proxy_cache_key<br>
<br>
默认值：proxy_cache_key $scheme$proxy_host$request_uri;<br>
<br>
上下文：http、server、location<br>
</pre><br>
<strong>proxy_cache_valid</strong><br>
<br>配置什么状态码可以被缓存，以及缓存时长。<br>
<pre class="prettyprint">语法：proxy_cache_valid [code...] time;<br>
<br>
上下文：http、server、location<br>
<br>
配置示例：proxy_cache_valid 200 304 2m;; # 说明对于状态为 200 和 304 的缓存文件的缓存时间是 2 分钟<br>
</pre><br>
<strong>proxy_no_cache</strong><br>
<br>定义相应保存到缓存的条件，如果字符串参数的至少一个值不为空且不等于“ 0”，则将不保存该响应到缓存。<br>
<pre class="prettyprint">语法：proxy_no_cache string;<br>
<br>
上下文：http、server、location<br>
<br>
示例：proxy_no_cache $http_pragma    $http_authorization;<br>
</pre><br>
<strong>proxy_cache_bypass</strong><br>
<br>定义条件，在该条件下将不会从缓存中获取响应。<br>
<pre class="prettyprint">语法：proxy_cache_bypass string;<br>
<br>
上下文：http、server、location<br>
<br>
示例：proxy_cache_bypass $http_pragma    $http_authorization;<br>
</pre><br>
<br><strong>upstream_cache_status 变量</strong><br>
<br>它存储了缓存是否命中的信息，会设置在响应头信息中，在调试中非常有用。<br>
<pre class="prettyprint">MISS：未命中缓存<br>
HIT：命中缓存<br>
EXPIRED：缓存过期<br>
STALE：命中了陈旧缓存<br>
REVALIDDATED：Nginx 验证陈旧缓存依然有效<br>
UPDATING：内容陈旧，但正在更新<br>
BYPASS：X响应从原始服务器获取<br>
</pre><br>
<strong>配置实例</strong><br>
<br>我们把 <code class="prettyprint">121.42.11.34</code> 服务器作为上游服务器，做如下配置（<code class="prettyprint">/etc/nginx/conf.d/cache.conf</code>）：<br>
<pre class="prettyprint">server &#123;<br>
listen 1010;<br>
root /usr/share/nginx/html/1010;<br>
location / &#123;<br>
index index.html;<br>
&#125;<br>
&#125;<br>
<br>
server &#123;<br>
listen 1020;<br>
root /usr/share/nginx/html/1020;<br>
location / &#123;<br>
index index.html;<br>
&#125;<br>
&#125; <br>
</pre><br>
把 <code class="prettyprint">121.5.180.193</code> 服务器作为代理服务器，做如下配置（<code class="prettyprint">/etc/nginx/conf.d/cache.conf</code>）：<br>
<pre class="prettyprint">proxy_cache_path /etc/nginx/cache_temp levels=2:2 keys_zone=cache_zone:30m max_size=2g inactive=60m use_temp_path=off;<br>
<br>
upstream cache_server&#123;<br>
server 121.42.11.34:1010;<br>
server 121.42.11.34:1020;<br>
&#125;<br>
<br>
server &#123;<br>
listen 80;<br>
server_name cache.lion.club;<br>
location / &#123;<br>
proxy_cache cache_zone; # 设置缓存内存，上面配置中已经定义好的<br>
proxy_cache_valid 200 5m; # 缓存状态为 200 的请求，缓存时长为 5 分钟<br>
proxy_cache_key $request_uri; # 缓存文件的 key 为请求的URI<br>
add_header Nginx-Cache-Status $upstream_cache_status # 把缓存状态设置为头部信息，响应给客户端<br>
proxy_pass http://cache_server; # 代理转发<br>
&#125;<br>
&#125; <br>
</pre><br>
缓存就是这样配置，我们可以在 <code class="prettyprint">/etc/nginx/cache_temp</code> 路径下找到相应的缓存文件。  <br>
<br><strong>对于一些实时性要求非常高的页面或数据来说，就不应该去设置缓存，下面来看看如何配置不缓存的内容。</strong><br><br>
<pre class="prettyprint">...<br>
<br>
server &#123;<br>
listen 80;<br>
server_name cache.lion.club;<br>
# URI 中后缀为 .txt 或 .text 的设置变量值为 "no cache"<br>
if ($request_uri ~ \.(txt|text)$) &#123;<br>
set $cache_name "no cache"<br>
&#125;<br>
<br>
location / &#123;<br>
proxy_no_cache $cache_name; # 判断该变量是否有值，如果有值则不进行缓存，如果没有值则进行缓存<br>
proxy_cache cache_zone; # 设置缓存内存<br>
proxy_cache_valid 200 5m; # 缓存状态为  200的请求，缓存时长为 5 分钟<br>
proxy_cache_key $request_uri; # 缓存文件的 key 为请求的 URI<br>
add_header Nginx-Cache-Status $upstream_cache_status # 把缓存状态设置为头部信息，响应给客户端<br>
proxy_pass http://cache_server; # 代理转发<br>
&#125;<br>
&#125; <br>
</pre><br>
<h4>HTTPS</h4>在学习如何配置 <code class="prettyprint">HTTPS</code> 之前，我们先来简单回顾下 <code class="prettyprint">HTTPS</code> 的工作流程是怎么样的？它是如何进行加密保证安全的？<br>
<br><strong>HTTPS 工作流程</strong><br>
<ol><li>客户端（浏览器）访问 <code class="prettyprint">https://www.baidu.com</code> 百度网站；</li><li>百度服务器返回 <code class="prettyprint">HTTPS</code> 使用的 <code class="prettyprint">CA</code> 证书；</li><li>浏览器验证 <code class="prettyprint">CA</code> 证书是否为合法证书；</li><li>验证通过，证书合法，生成一串随机数并使用公钥（证书中提供的）进行加密；</li><li>发送公钥加密后的随机数给百度服务器；</li><li>百度服务器拿到密文，通过私钥进行解密，获取到随机数（公钥加密，私钥解密，反之也可以）；</li><li>百度服务器把要发送给浏览器的内容，使用随机数进行加密后传输给浏览器；</li><li>此时浏览器可以使用随机数进行解密，获取到服务器的真实传输内容；</li></ol><br>
<br>这就是 <code class="prettyprint">HTTPS</code> 的基本运作原理，使用对称加密和非对称机密配合使用，保证传输内容的安全性。<br>
<br>关于HTTPS更多知识，可以查看作者的另外一篇文章《<a href="https://juejin.cn/post/6844904148601667598#heading-37">学习 HTTP 协议</a>》。<br>
<br><strong>配置证书</strong><br>
<br>下载证书的压缩文件，里面有个 <code class="prettyprint">Nginx</code> 文件夹，把 <code class="prettyprint">xxx.crt</code> 和 <code class="prettyprint">xxx.key</code> 文件拷贝到服务器目录，再进行如下配置：<br>
<pre class="prettyprint">server &#123;<br>
listen 443 ssl http2 default_server;   # SSL 访问端口号为 443<br>
server_name lion.club;         # 填写绑定证书的域名（我这里是随便写的）<br>
ssl_certificate /etc/nginx/https/lion.club_bundle.crt;   # 证书地址<br>
ssl_certificate_key /etc/nginx/https/lion.club.key;      # 私钥地址<br>
ssl_session_timeout 10m;<br>
ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # 支持ssl协议版本，默认为后三个，主流版本是[TLSv1.2]<br>
<br>
location / &#123;<br>
root         /usr/share/nginx/html;<br>
index        index.html index.htm;<br>
&#125;<br>
&#125; <br>
</pre><br>
如此配置后就能正常访问 <code class="prettyprint">HTTPS</code> 版的网站了。<br><br>
<h4>配置跨域 CORS</h4>先简单回顾下跨域究竟是怎么回事。<br>
<br><strong>跨域的定义</strong><br>
<br>同源策略限制了从同一个源加载的文档或脚本如何与来自另一个源的资源进行交互。这是一个用于隔离潜在恶意文件的重要安全机制。通常不允许不同源间的读操作。  <br>
<br><strong>同源的定义</strong><br>
<br>如果两个页面的协议，端口（如果有指定）和域名都相同，则两个页面具有相同的源。  <br>
<br>下面给出了与 URL <code class="prettyprint">http://store.company.com/dir/page.html</code> 的源进行对比的示例：<br>
<pre class="prettyprint">http://store.company.com/dir2/other.html 同源<br>
https://store.company.com/secure.html 不同源，协议不同<br>
http://store.company.com:81/dir/etc.html 不同源，端口不同<br>
http://news.company.com/dir/other.html 不同源，主机不同<br>
</pre><br>
<br>不同源会有如下限制：<br>
<ul><li><code class="prettyprint">Web</code> 数据层面，同源策略限制了不同源的站点读取当前站点的 <code class="prettyprint">Cookie</code>、<code class="prettyprint">IndexDB</code>、<code class="prettyprint">LocalStorage</code> 等数据。</li><li><code class="prettyprint">DOM</code> 层面，同源策略限制了来自不同源的 <code class="prettyprint">JavaScript</code> 脚本对当前 <code class="prettyprint">DOM</code> 对象读和写的操作。</li><li>网络层面，同源策略限制了通过 <code class="prettyprint">XMLHttpRequest</code> 等方式将站点的数据发送给不同源的站点。</li></ul><br>
<br><strong>Nginx 解决跨域的原理</strong><br>
<br>例如：<br>
<ul><li>前端 <code class="prettyprint">server</code> 的域名为：<code class="prettyprint">fe.server.com</code></li><li>后端服务的域名为：<code class="prettyprint">dev.server.com</code></li></ul><br>
<br>现在我在 <code class="prettyprint">fe.server.com</code> 对 <code class="prettyprint">dev.server.com</code> 发起请求一定会出现跨域。  <br>
<br>现在我们只需要启动一个 <code class="prettyprint">Nginx</code> 服务器，将 <code class="prettyprint">server_name</code> 设置为 <code class="prettyprint">fe.server.com</code> 然后设置相应的 <code class="prettyprint">location</code> 以拦截前端需要跨域的请求，最后将请求代理回 <code class="prettyprint">dev.server.com</code>。如下面的配置：<br>
<pre class="prettyprint">server &#123;<br>
listen           80;<br>
server_name  fe.server.com;<br>
location / &#123;<br>
    proxy_pass dev.server.com;<br>
&#125;<br>
&#125; <br>
</pre><br>
这样可以完美绕过浏览器的同源策略：<code class="prettyprint">fe.server.com</code> 访问 <code class="prettyprint">Nginx</code> 的 <code class="prettyprint">fe.server.com</code> 属于同源访问，而 <code class="prettyprint">Nginx</code> 对服务端转发的请求不会触发浏览器的同源策略。<br><br>
<h4>配置开启 gzip 压缩</h4><code class="prettyprint">GZIP</code> 是规定的三种标准 <code class="prettyprint">HTTP</code> 压缩格式之一。目前绝大多数的网站都在使用 <code class="prettyprint">GZIP</code> 传输 <code class="prettyprint">HTML</code>、<code class="prettyprint">CSS</code>、<code class="prettyprint">JavaScript</code> 等资源文件。  <br>
<br>对于文本文件，<code class="prettyprint">GZiP</code> 的效果非常明显，开启后传输所需流量大约会降至  <code class="prettyprint">1/4~1/3</code> 。  <br>
<br>并不是每个浏览器都支持  <code class="prettyprint">gzip</code> 的，如何知道客户端是否支持  <code class="prettyprint">gzip</code> 呢，请求头中的  <code class="prettyprint">Accept-Encoding</code> 来标识对压缩的支持。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/74864b13712510fefde149f4904575dc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/74864b13712510fefde149f4904575dc.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
启用 <code class="prettyprint">gzip</code> 同时需要客户端和服务端的支持，如果客户端支持 <code class="prettyprint">gzip</code> 的解析，那么只要服务端能够返回 <code class="prettyprint">gzip</code> 的文件就可以启用 <code class="prettyprint">gzip</code> 了，我们可以通过 <code class="prettyprint">Nginx</code> 的配置来让服务端支持 <code class="prettyprint">gzip</code>。下面的 <code class="prettyprint">respone</code> 中 <code class="prettyprint">content-encoding:gzip</code>，指服务端开启了 <code class="prettyprint">gzip</code> 的压缩方式。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/4da55cbded6eaca3fd8c33b975ba1bf4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/4da55cbded6eaca3fd8c33b975ba1bf4.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在 <code class="prettyprint">/etc/nginx/conf.d/</code> 文件夹中新建配置文件 <code class="prettyprint">gzip.conf</code> ：<br>
<pre class="prettyprint"># # 默认 off，是否开启 gzip<br>
gzip on; <br>
# 要采用 gzip 压缩的 MIME 文件类型，其中 text/html 被系统强制启用；<br>
gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;<br>
<br>
# ---- 以上两个参数开启就可以支持 Gzip 压缩了 ---- #<br>
<br>
# 默认 off，该模块启用后，Nginx 首先检查是否存在请求静态文件的 gz 结尾的文件，如果有则直接返回该 .gz 文件内容；<br>
gzip_static on;<br>
<br>
# 默认 off，Nginx 做为反向代理时启用，用于设置启用或禁用从代理服务器上收到相应内容 gzip 压缩；<br>
gzip_proxied any;<br>
<br>
# 用于在响应消息头中添加 Vary：Accept-Encoding，使代理服务器根据请求头中的 Accept-Encoding 识别是否启用 gzip 压缩；<br>
gzip_vary on;<br>
<br>
# gzip 压缩比，压缩级别是 1-9，1 压缩级别最低，9 最高，级别越高压缩率越大，压缩时间越长，建议 4-6；<br>
gzip_comp_level 6;<br>
<br>
# 获取多少内存用于缓存压缩结果，16 8k 表示以 8k*16 为单位获得；<br>
gzip_buffers 16 8k;<br>
<br>
# 允许压缩的页面最小字节数，页面字节数从 header 头中的 Content-Length 中进行获取。默认值是 0，不管页面多大都压缩。建议设置成大于 1k 的字节数，小于 1k 可能会越压越大；<br>
# gzip_min_length 1k;<br>
<br>
# 默认 1.1，启用 gzip 所需的 HTTP 最低版本；<br>
gzip_http_version 1.1;<br>
</pre><br>
其实也可以通过前端构建工具例如 <code class="prettyprint">webpack</code>、<code class="prettyprint">rollup</code> 等在打生产包时就做好 <code class="prettyprint">Gzip</code> 压缩，然后放到 <code class="prettyprint">Nginx</code> 服务器中，这样可以减少服务器的开销，加快访问速度。<br>
<br>关于 <code class="prettyprint">Nginx</code> 的实际应用就学习到这里，相信通过掌握了 <code class="prettyprint">Nginx</code> 核心配置以及实战配置，之后再遇到什么需求，我们也能轻松应对。接下来，让我们再深入一点学习下 <code class="prettyprint">Nginx</code> 的架构。<br>
<h3>Nginx 架构</h3><h4>进程结构</h4>多进程结构 <code class="prettyprint">Nginx</code> 的进程模型图：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/86385f828f5016fb625d39884401529b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/86385f828f5016fb625d39884401529b.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
多进程中的 <code class="prettyprint">Nginx</code> 进程架构如下图所示，会有一个父进程（<code class="prettyprint">Master Process</code>），它会有很多子进程（<code class="prettyprint">Child Processes</code>）。<br><br>
<ul><li><code class="prettyprint">Master Process</code> 用来管理子进程的，其本身并不真正处理用户请求。<br>
<ul><li>某个子进程 <code class="prettyprint">down</code> 掉的话，它会向 <code class="prettyprint">Master</code> 进程发送一条消息，表明自己不可用了，此时 <code class="prettyprint">Master</code> 进程会去新起一个子进程。</li>-   某个配置文件被修改了 `Master` 进程会去通知 `work` 进程获取新的配置信息，这也就是我们所说的热部署。</ul></li><li>子进程间是通过共享内存的方式进行通信的。</li></ul><br>
<br><h4>配置文件重载原理</h4><code class="prettyprint">reload</code> 重载配置文件的流程：<br>
<ol><li>向 <code class="prettyprint">master</code> 进程发送 <code class="prettyprint">HUP</code> 信号（<code class="prettyprint">reload</code> 命令）；</li><li><code class="prettyprint">master</code> 进程检查配置语法是否正确；</li><li><code class="prettyprint">master</code> 进程打开监听端口；</li><li><code class="prettyprint">master</code> 进程使用新的配置文件启动新的 <code class="prettyprint">worker</code> 子进程；</li><li><code class="prettyprint">master</code> 进程向老的 <code class="prettyprint">worker</code> 子进程发送 <code class="prettyprint">QUIT</code> 信号；</li><li>老的 <code class="prettyprint">worker</code> 进程关闭监听句柄，处理完当前连接后关闭进程；</li><li>整个过程 <code class="prettyprint">Nginx</code> 始终处于平稳运行中，实现了平滑升级，用户无感知；</li></ol><br>
<br><h4>Nginx 模块化管理机制</h4><code class="prettyprint">Nginx</code> 的内部结构是由核心部分和一系列的功能模块所组成。这样划分是为了使得每个模块的功能相对简单，便于开发，同时也便于对系统进行功能扩展。<code class="prettyprint">Nginx</code> 的模块是互相独立的,低耦合高内聚。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/56ba73727c61023170a3a62332ca5b02.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/56ba73727c61023170a3a62332ca5b02.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>总结</h3>相信通过本文的学习，你应该会对  <code class="prettyprint">Nginx</code>  有一个更加全面的认识。<br>
<br>原文链接：<a href="https://juejin.cn/post/6942607113118023710" rel="nofollow" target="_blank">https://juejin.cn/post/6942607113118023710</a>，作者：Lion
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            