
---
title: '源代码编译安装haproxy'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=1974'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 21:27:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=1974'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>可以去 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmirrors.huaweicloud.com%2Fhome" target="_blank" rel="nofollow noopener noreferrer" title="https://mirrors.huaweicloud.com/home" ref="nofollow noopener noreferrer">mirrors.huaweicloud.com/home</a> 查找相应的国内源 也可以使用其他源</p>
</blockquote>
<h1 data-id="heading-0">1 下载haproxy</h1>
<pre><code class="copyable">wget https://mirrors.huaweicloud.com/haproxy/2.4/src/haproxy-2.4.2.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">2 下载lua</h1>
<pre><code class="copyable"> wget https://www.lua.org/ftp/lua-5.4.3.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">3 安装依赖库</h1>
<pre><code class="copyable">yum -y install gcc gcc-c++ glibc glibc-devel pcre pcre-devel openssl openssl-devel systemd-devel net-tools vim iotop bc zip unzip zlib-devel lrzsz tree screen lsof tcpdump wget libevent-devel.x86_64  ncurses-devel.x86_64  readline-devel.x86_64    libtermcap-devel ntpdate
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意如果是centos 8 ntpdata被chrony替换了</p>
</blockquote>
<h1 data-id="heading-3">4 安装lua</h1>
<pre><code class="copyable">tar -xvf lua-5.4.3.tar.gz

cd lua-5.4.3/
make linux test
make install
lua -v #确认lua版本号
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">5 安装haproxy</h1>
<pre><code class="copyable">tar -xvf haproxy-2.4.2.tar.gz
mkdir /usr/local/haproxy
cd haproxy-2.4.2/
make ARCH=x86_64 TARGET=linux-glibc  USE_PCRE=1  USE_OPENSSL=1  USE_ZLIB=1  USE_SYSTEMD=1  USE_CPU_AFFINITY=1  USE_LUA=1  LUA_INC=/root/lua-5.4.3/src/  LUA_LIB=/root/lua-5.4.3/src/ PREFIX=/usr/local/haproxy LUA_LIB_NAME=lua
make install PREFIX=/usr/local/haproxy
ln -sv /usr/local/haproxy/sbin/haproxy /usr/sbin/
haproxy -v # 确认haproxy的版本号
mkdir -p /var/lib/haproxy  #用于存储 haproxy.pid文件
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">6 haproxy配置文件</h1>
<pre><code class="copyable">cat /etc/haproxy/haproxy.cfg
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文件内容</p>
<pre><code class="copyable">global
    #日志文件的输出定向
    log  127.0.0.1  local3 info
    #运行目录
    chroot      /usr/local/haproxy
    #将所有进程写入pid文件
    pidfile     /var/lib/haproxy/haproxy.pid
    #最大连接
    maxconn    4000
    #用户名
    user        haproxy
    #用户组
    group       haproxy
    #以后台形式运行haproxy
    daemon
    #开启多进程工作模式，推荐使用多进程单线程，除非服务器只有1核CPU，可以开启单进程多线程
    nbproc 2
    
    # turn on stats unix socket
    stats socket /var/lib/haproxy/haproxy.sock
defaults
    #工作模式，所处理的类别,默认采用http模式，可配置成tcp作4层消息转发
    mode    http
    log                     global
    #日志类别，记载http日志
    option                  httplog
    #不记录健康检查日志信息
    option                  dontlognull
    #每次请求完毕后主动关闭http通道,ha-proxy不支持keep-alive,只能模拟这种模式的实现
    option http-server-close
    #如果后端服务器需要获得客户端真实ip需要配置的参数，可以从Http Header中获得客户端ip
    #option forwardfor       except 127.0.0.0/8
    #是否允许重新分配在session 失败后
    option                  redispatch
    #3次连接失败就认为服务器不可用，主要通过后面的check检查
    retries    3
    #当服务器负载很高的时候，自动结束掉当前队列处理比较久的连接
    option abortonclose
    #默认http请求超时时间
    timeout http-request    10s
    #默认队列超时时间
    timeout queue    1m
    #连接超时时间
    timeout connect    10s
    #客户端连接超时时间
    timeout client    5m
    #服务器端连接超时时间
    timeout server    5m
    #默认持久连接超时时间
    timeout http-keep-alive    10s
    #设置心跳检查超时时间
    timeout check    10s
    #最大连接数
    maxconn                 3000
    #健康检测#注意实际工作中测试时，应该下载某一个页面来进行测试，因此这个页面应该是个小页面，而不要用首页面。这里是每隔一秒检查一次页面。
    #option  httpchk GET /index.html

listen admin_stats
  #开关
  mode http
  bind 0.0.0.0:10086
  stats enable
  stats uri /haproxy-stats
  stats realm HAProxy\ Statistics
  #认证账号密码
  stats auth admin:admin123
  #启用管理功能
  stats admin if TRUE
  #统计页面自动刷新时间
  stats refresh 30s
  #管理界面，如果认证成功了，可通过webui管理节点
  stats   admin if TRUE
  
#http-request set-header X-Forwarded-For req.hdr(X-Forwarded-For)
    
frontend myweb 
    bind 0.0.0.0:80
    mode http
    log global
    option httplog
    option httpclose
    default_backend myweb
    

backend myweb
    balance leastconn
    server web3 10.0.2.3:80 check  
    server web4 10.0.2.4:80 check  
    server web6 10.0.2.6:80 check  
    server web8 10.0.2.8:80 check  
    server web10 10.0.2.10:80 check  
    server web11 10.0.2.11:80 check  
    server web7 10.0.2.7:80 check  
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">7 安装 rsyslog</h1>
<pre><code class="copyable">yum install rsyslog -y
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置haproxy的日志通道</p>
<pre><code class="copyable">cd /etc/rsyslog.d/
vi haproxy.conf
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文件内容</p>
<pre><code class="copyable">$ModLoad imudp
$UDPServerRun 514
local3.*     /var/log/haproxy.log
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重启rsyslog</p>
<pre><code class="copyable">systemctl restart rsyslog
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">8 创建systemd启动服务</h1>
<pre><code class="copyable">vi /etc/systemd/system/haproxy.service
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文件内容</p>
<pre><code class="copyable"> [Unit]
 Description=HAProxy Load Balancer
 After=syslog.target network.target
 
 [Service]
 ExecStartPre=/usr/local/haproxy/sbin/haproxy -f /etc/haproxy/haproxy.cfg
 ExecStart=/usr/local/haproxy/sbin/haproxy -f /etc/haproxy/haproxy.cfg -p /var/lib/haproxy/haproxy.pid
 ExecReload=/bin/kill -USR2 $MAINPID
 
 [Install]
 WantedBy=multi-user.target
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">9 启动服务</h1>
<pre><code class="copyable"> systemctl  deamon-reload
 systemctl start  haproxy
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            