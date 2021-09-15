
---
title: '面试必备：Nginx 知识梳理'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/400f3b43dab991c262ca76a2532b7099.png'
author: Dockone
comments: false
date: 2021-09-15 03:08:28
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/400f3b43dab991c262ca76a2532b7099.png'
---

<div>   
<br><h3>Nginx概念</h3>Nginx 是一个<strong>高性能的 HTTP 和反向代理服务</strong>。其特点是占有内存少，并发能力强，事实上 Nginx 的并发能力在同类型的网页服务器中表现较好。<br>
<br>Nginx 专为性能优化而开发，性能是其最重要的考量指标，实现上非常注重效率，能经受住高负载的考验，有报告表明能支持高达 50000 个并发连接数。<br>
<br>在连接高并发的情况下，Nginx 是 Apache 服务不错的替代品：Nginx 在美国是做虚拟主机生意的老板们经常选择的软件平台之一。<br>
<h3>反向代理</h3>在说反向代理之前，先来说说什么是代理和正向代理。<br>
<h4>代理</h4>代理其实就是一个中介，A 和 B 本来可以直连，中间插入一个 C，C 就是中介。刚开始的时候，代理多数是帮助<strong>内网 client</strong>（局域网）访问<strong>外网 server</strong> 用的。 后来出现了反向代理，<code class="prettyprint">反向</code>这个词在这儿的意思其实是指方向相反，即代理将来自外网客户端的请求转发到内网服务器，从外到内。<br>
<h4>正向代理</h4>正向代理即是客户端代理，代理客户端，服务端不知道实际发起请求的客户端。<br>
<br>正向代理类似一个跳板机，代理访问外部资源。<br>
<br>比如我们国内访问谷歌，直接访问访问不到，我们可以通过一个正向代理服务器，请求发到代理服服务上，代理服务器能够访问谷歌，这样由代理去访问谷歌取到返回数据，再返回给我们，这样我们就能访问谷歌了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/400f3b43dab991c262ca76a2532b7099.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/400f3b43dab991c262ca76a2532b7099.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>反向代理</h4>反向代理即是服务端代理，代理服务端，客户端不知道实际提供服务的服务端。<br>
<br>客户端是感知不到代理服务器的存在。<br>
<br>是指以代理服务器来接受 Internet 上的连接请求，然后将请求转发给内部网络上的服务器，并将从服务器上得到的结果返回给 Internet 上请求连接的客户端，此时代理服务器对外就表现为一个反向代理服务器。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/3d77abff94ac1b165b692541916c88cb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/3d77abff94ac1b165b692541916c88cb.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>负载均衡</h3>关于负载均衡，先来举个例子：<br>
<br><blockquote><br>地铁大家应该都坐过吧，我们一般在早高峰乘地铁时候，总有那么一个地铁口人最拥挤，这时候，一般会有个地铁工作人员 A 拿个大喇叭在喊“着急的人员请走B口，B口人少车空”。而这个地铁工作人员A就是负责负载均衡的。<br>
  <br>
  <br>为了提升网站的各方面能力，我们一般会把多台机器组成一个集群对外提供服务。然而，我们的网站对外提供的访问入口都是一个的，比如 <code class="prettyprint">www.taobao.com</code>。那么当用户在浏览器输入 <code class="prettyprint">www.taobao.com</code> 的时候如何将用户的请求分发到集群中不同的机器上呢，这就是负载均衡在做的事情。</blockquote>负载均衡（Load Balance），意思是将负载（工作任务，访问请求）进行平衡、分摊到多个操作单元（服务器，组件）上进行执行。是解决高性能，单点故障（高可用），扩展性（水平伸缩）的终极解决方案。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/6979131521e61c256e7ae63318818150.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/6979131521e61c256e7ae63318818150.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
Nginx 提供的负载均衡主要有三种方式：轮询，加权轮询，Ip hash。<br>
<h4>轮询</h4>Nginx 默认就是轮询其权重都默认为 1，服务器处理请求的顺序：ABCABCABCABC……<br>
<pre class="prettyprint">upstream mysvr &#123; <br>
server 192.168.8.1:7070; <br>
server 192.168.8.2:7071;<br>
server 192.168.8.3:7072;<br>
&#125; <br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/d3feadb4e7fe9722c396ecf03ec7d0a1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/d3feadb4e7fe9722c396ecf03ec7d0a1.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>加权轮询</h4>根据配置的权重的大小而分发给不同服务器不同数量的请求。如果不设置，则默认为 1。下面服务器的请求顺序为：ABBCCCABBCCC……<br>
<pre class="prettyprint">upstream mysvr &#123; <br>
server 192.168.8.1:7070 weight=1; <br>
server 192.168.8.2:7071 weight=2;<br>
server 192.168.8.3:7072 weight=3;<br>
&#125; <br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/0147ae54c62df1c9cdab66518a9d25b1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/0147ae54c62df1c9cdab66518a9d25b1.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>ip_hash</h4>iphash 对客户端请求的 IP 进行 hash 操作，然后根据 hash 结果将同一个客户端 IP 的请求分发给同一台服务器进行处理，可以解决 session 不共享的问题。<br>
<pre class="prettyprint">upstream mysvr &#123; <br>
server 192.168.8.1:7070; <br>
server 192.168.8.2:7071;<br>
server 192.168.8.3:7072;<br>
ip_hash;<br>
&#125; <br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/b2a1f78906abf80f29e3524e9bf9e461.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/b2a1f78906abf80f29e3524e9bf9e461.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>动静分离</h3><h4>动态与静态页面区别</h4><ul><li>静态资源：当用户多次访问这个资源，资源的源代码永远不会改变的资源（如：HTML，JavaScript，CSS，img 等文件）。</li><li>动态资源：当用户多次访问这个资源，资源的源代码可能会发送改变（如：.jsp、servlet 等）。</li></ul><br>
<br><h4>什么是动静分离</h4><ul><li>动静分离是让动态网站里的动态网页根据一定规则把不变的资源和经常变的资源区分开来，动静资源做好了拆分以后，我们就可以根据静态资源的特点将其做缓存操作，这就是网站静态化处理的核心思路。</li><li>动静分离简单的概括是：动态文件与静态文件的分离。</li></ul><br>
<br><h4>为什么要用动静分离</h4>为了加快网站的解析速度，可以把动态资源和静态资源用不同的服务器来解析，加快解析速度。降低单个服务器的压力。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/b509ce810c916950df3d308c98edada3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/b509ce810c916950df3d308c98edada3.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Nginx 安装</h3><h4>Windows 下安装</h4><strong>1、下载 Nginx</strong><br>
<br><a href="http://nginx.org/en/download.html" rel="nofollow" target="_blank">http://nginx.org/en/download.html</a> 下载稳定版本。以 nginx/Windows-1.20.1 为例，直接下载 nginx-1.20.1.zip。 下载后解压，解压后如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/833af69b06135b0e43e7f2d3cf37eb3e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/833af69b06135b0e43e7f2d3cf37eb3e.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>2、启动 Nginx</strong><br>
<ul><li>直接双击 nginx.exe，双击后一个黑色的弹窗一闪而过</li><li>打开 cmd 命令窗口，切换到 Nginx 解压目录下，输入命令 <code class="prettyprint">nginx.exe</code>，回车即可</li></ul><br>
<br><strong>3、检查 Nginx 是否启动成功</strong><br>
<br>直接在浏览器地址栏输入网址 <a href="http://localhost/" rel="nofollow" target="_blank">http://localhost:80</a> 回车，出现以下页面说明启动成功！<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/b70b132bea851c2c957141182f15a548.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/b70b132bea851c2c957141182f15a548.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Docker 安装 Nnginx</h4>我之前的文章也讲过 Linux 下安装的步骤，我采用的是 Docker 安装的，很简单。<br>
<br>相关链接：<a href="https://juejin.cn/post/6937814934646423560" rel="nofollow" target="_blank">https://juejin.cn/post/6937814934646423560</a><br>
<br><strong>1、查看所有本地的主机上的镜像</strong>，使用命令 <code class="prettyprint">docker images</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/c8a975209cceb121378131419ef62cda.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/c8a975209cceb121378131419ef62cda.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>2、创建 Nginx 容器并启动容器</strong>，使用命令 <code class="prettyprint">docker run -d --name nginx01 -p 3344:80 nginx</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/ee6554543e138e5a64a230e97b3de652.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/ee6554543e138e5a64a230e97b3de652.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>3、查看已启动的容器</strong>，使用命令 <code class="prettyprint">docker ps</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/6b3e720a609dc7d377a5cb7fcdbdcdce.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/6b3e720a609dc7d377a5cb7fcdbdcdce.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
浏览器访问<code class="prettyprint">服务器ip:3344</code>，如下，说明安装启动成功。<br>
<br><code class="prettyprint">注意</code>：如何连接不上，检查阿里云安全组是否开放端口，或者服务器防火墙是否开放端口！<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/5fcf54c0f5885e3416fa78e6fcd03a95.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/5fcf54c0f5885e3416fa78e6fcd03a95.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Linux 下安装</h4><strong>1、安装 GCC</strong><br>
<br>安装 Nginx 需要先将官网下载的源码进行编译，编译依赖 GCC 环境，如果没有 GCC 环境，则需要安装：<br>
<pre class="prettyprint">yum install gcc-c++<br>
</pre><br>
<strong>2、PCRE pcre-devel 安装</strong><br>
<br>PCRE（Perl Compatible Regular Expressions）是一个 Perl 库，包括 Perl 兼容的正则表达式库。Nginx 的 http 模块使用 PCRE 来解析正则表达式，所以需要在 Linux 上安装 PCRE 库，pcre-devel 是使用 PCRE 开发的一个二次开发库。Nginx 也需要此库。命令：<br>
<pre class="prettyprint">yum install -y pcre pcre-devel<br>
</pre><br>
<strong>3、zlib 安装</strong><br>
<br>zlib 库提供了很多种压缩和解压缩的方式， Nginx 使用 zlib 对 http 包的内容进行 gzip ，所以需要在 CentOS 上安装 zlib 库。<br>
<pre class="prettyprint">yum install -y zlib zlib-devel<br>
</pre><br>
<strong>4、OpenSSL 安装</strong><br>
<br>OpenSSL 是一个强大的安全套接字层密码库，囊括主要的密码算法、常用的密钥和证书封装管理功能及 SSL 协议，并提供丰富的应用程序供测试或其它目的使用。Nginx 不仅支持 http 协议，还支持 https（即在 SSL 协议上传输http），所以需要在 CentOS 安装 OpenSSL 库。<br>
<pre class="prettyprint">yum install -y openssl openssl-devel<br>
</pre><br>
<strong>5、下载安装包</strong><br>
<br>手动下载 .tar.gz 安装包，地址：<a href="https://nginx.org/en/download.html" rel="nofollow" target="_blank">https://nginx.org/en/download.html</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/d6730e4b122328e50643dd3b2efb623a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/d6730e4b122328e50643dd3b2efb623a.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
下载完毕上传到服务器上 /root<br>
<br><strong>6、解压</strong><br>
<pre class="prettyprint">tar -zxvf nginx-1.20.1.tar.gz<br>
cd nginx-1.20.1<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/76d4d27ad5ba89079854165f9c4c4c8e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/76d4d27ad5ba89079854165f9c4c4c8e.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>7、配置</strong><br>
<br>使用默认配置，在 Nginx 根目录下执行<br>
<pre class="prettyprint">./configue<br>
make<br>
make install<br>
</pre><br>
查找安装路径：<code class="prettyprint">whereis nginx</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/12b53cafe8cfa0df8a627eea7cdd22b5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/12b53cafe8cfa0df8a627eea7cdd22b5.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>8、启动 Nginx</strong><br>
<pre class="prettyprint">./nginx<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/2c38b09c77f9f282ccf4d61eb7d09a60.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/2c38b09c77f9f282ccf4d61eb7d09a60.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
启动成功，访问页面：ip:80<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/72ed587c81547544205a8d10feae7d15.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/72ed587c81547544205a8d10feae7d15.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Nginx 常用命令</h3><code class="prettyprint">注意</code>：使用 Nginx 操作命令前提，必须进入到 Nginx 目录 <code class="prettyprint">/usr/local/nginx/sbin</code><br>
<br>1、查看Nginx版本号：<code class="prettyprint">./nginx -v</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/0ce596bfc48da881dcc5330f288df934.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/0ce596bfc48da881dcc5330f288df934.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
2、启动 Nginx：<code class="prettyprint">./nginx</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/e340ccf436c1563c60974a0e6602c684.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/e340ccf436c1563c60974a0e6602c684.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
3、停止 Nginx：<code class="prettyprint">./nginx -s stop</code> 或者 <code class="prettyprint">./nginx -s quit</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/7d53fb44f0e973a4b7845134243f4bf6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/7d53fb44f0e973a4b7845134243f4bf6.png" class="img-polaroid" title="21.png" alt="21.png" referrerpolicy="no-referrer"></a>
</div>
<br>
4、重新加载配置文件：<code class="prettyprint">./nginx -s reload</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/6ef3102260eceedcd4460387823e7cbd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/6ef3102260eceedcd4460387823e7cbd.png" class="img-polaroid" title="22.png" alt="22.png" referrerpolicy="no-referrer"></a>
</div>
<br>
5、查看 Nginx 进程：<code class="prettyprint">ps -ef|grep nginx</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/22988a12939a20faf2fdec2df88ecdfc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/22988a12939a20faf2fdec2df88ecdfc.png" class="img-polaroid" title="23.png" alt="23.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Nginx 配置文件</h3>Nginx 配置文件的位置：<code class="prettyprint">/usr/local/nginx/conf/nginx.conf</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/0c5c89d19edf2590730099dd91f34939.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/0c5c89d19edf2590730099dd91f34939.png" class="img-polaroid" title="24.png" alt="24.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Nginx 配置文件有3部分组成：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/ae2e29052070f2e0bced35f0836d72b2.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/ae2e29052070f2e0bced35f0836d72b2.jpg" class="img-polaroid" title="25.jpg" alt="25.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>1、全局块</strong><br>
<br>从配置文件开始到 events 块之间的内容，主要会设置一些影响 Nginx 服务器整体运行的配置指令，比如：<code class="prettyprint">worker_processes 1</code>。<br>
<br>这是 Nginx 服务器并发处理服务的关键配置，worker_processes 值越大，可以支持的并发处理量也越多，但是会受到硬件、软件等设备的制约。一般设置值和 CPU 核心数一致。<br>
<br><strong>2、events 块</strong><br>
<br>events 块涉及的指令主要影响 Nginx 服务器与用户的网络连接，比如：<code class="prettyprint">worker_connections 1024</code><br>
<br>表示每个 work process 支持的最大连接数为 1024，这部分的配置对 Nginx 的性能影响较大，在实际中应该灵活配置。<br>
<br><strong>3、http块</strong><br>
<pre class="prettyprint">http &#123;<br>
include       mime.types;<br>
<br>
default_type  application/octet-stream;<br>
<br>
sendfile        on;<br>
<br>
keepalive_timeout  65;<br>
<br>
server &#123;<br>
    listen       80;#监听端口<br>
    server_name  localhost;#域名<br>
<br>
    location / &#123;<br>
        root   html;<br>
        index  index.html index.htm;<br>
    &#125;<br>
<br>
    error_page   500 502 503 504  /50x.html;<br>
<br>
    location = /50x.html &#123;<br>
        root   html;<br>
    &#125;<br>
<br>
&#125;<br>
<br>
&#125; <br>
</pre><br>
这算是 Nginx 服务器配置中最频繁的部分。<br>
<h3>演示示例</h3><h4>反向代理/负载均衡</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/e7054d41f6a358918a065e1f04f4fdb3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/e7054d41f6a358918a065e1f04f4fdb3.png" class="img-polaroid" title="26.png" alt="26.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们在 Windows 下演示，首先我们创建两个 Spring Boot 项目，端口是 9001 和 9002，如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/913ffde28324de87a66a2c97f10d8f08.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/913ffde28324de87a66a2c97f10d8f08.png" class="img-polaroid" title="27.png" alt="27.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们要做的就是将 <code class="prettyprint">localhost:80</code> 代理 <code class="prettyprint">localhost:9001</code> 和 <code class="prettyprint">localhost:9002</code> 这两个服务，并且让轮询访问这两个服务。<br>
<br>Nginx 配置如下：<br>
<pre class="prettyprint">worker_processes  1;<br>
<br>
events &#123;<br>
worker_connections  1024;<br>
&#125;<br>
<br>
http &#123;<br>
include       mime.types;<br>
default_type  application/octet-stream;<br>
<br>
sendfile        on;<br>
keepalive_timeout  65;<br>
<br>
upstream jiangwang &#123;<br>
    server 127.0.0.1:9001 weight=1;//轮询其权重都默认为1<br>
    server 127.0.0.1:9002 weight=1;<br>
&#125;<br>
<br>
server &#123;<br>
    listen       80;<br>
    server_name  localhost;<br>
<br>
    #charset koi8-r;<br>
<br>
    #access_log  logs/host.access.log  main;<br>
<br>
    location / &#123;<br>
        root   html;<br>
        index  index.html index.htm;<br>
        proxy_pass http://jiangwang;<br>
    &#125;<br>
&#125;<br>
<br>
&#125; <br>
</pre><br>
我们先将项目打成jar包，然后命令行启动项目，然后在浏览器上访问 <code class="prettyprint">localhost</code> 来访问这两个项目，我也在项目中打印了日志，操作一下来看看结果，是不是两个项目轮询被访问。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/d93fdbe71fe6e7844d145988431e7ace.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/d93fdbe71fe6e7844d145988431e7ace.png" class="img-polaroid" title="28.png" alt="28.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/987ca4087c6aa8c3edd223dedbea4717.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/987ca4087c6aa8c3edd223dedbea4717.jpg" class="img-polaroid" title="29.jpg" alt="29.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到，访问 <code class="prettyprint">localhost</code>，这两个项目轮询被访问。<br>
<br>接下来我们将权重改为如下设置：<br>
<pre class="prettyprint">upstream jiangwang &#123;<br>
server 127.0.0.1:9001 weight=1;<br>
server 127.0.0.1:9002 weight=3;<br>
&#125; <br>
</pre><br>
重新加载一个 Nginx 的配置文件：<code class="prettyprint">nginx -s reload</code><br>
<br>加载完毕，我们再访问其 <code class="prettyprint">localhost</code>，观察其访问的比例：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/c34ae931ff58d43cc48c484f6cd03588.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/c34ae931ff58d43cc48c484f6cd03588.png" class="img-polaroid" title="30.png" alt="30.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/3b635d7692c59637ca2774477947851d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/3b635d7692c59637ca2774477947851d.png" class="img-polaroid" title="31.png" alt="31.png" referrerpolicy="no-referrer"></a>
</div>
<br>
结果显示，9002 端口的访问次数与 9001 访问的次数基本上是 <code class="prettyprint">3:1</code>。<br>
<h4>动静分离</h4>1、将静态资源放入本地新建的文件里面，例如：在 D 盘新建一个文件 data，然后再 data 文件夹里面在新建两个文件夹，一个 img 文件夹，存放图片；一个 html 文件夹，存放 html 文件；如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/13f277ffc22c109b6c379012d76c792e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/13f277ffc22c109b6c379012d76c792e.png" class="img-polaroid" title="32.png" alt="32.png" referrerpolicy="no-referrer"></a>
</div>
<br>
2、在 html 文件夹里面新建一个 <code class="prettyprint">a.html</code> 文件，内容如下：<br>
<pre class="prettyprint"><!DOCTYPE html><br>
<html><br>
<head><br>
<meta charset="utf-8"><br>
<title>Html文件</title><br>
</head><br>
<body><br>
<p>Hello World</p><br>
</body><br>
</html><br>
</pre><br>
3、在 img 文件夹里面放入一张照片，如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/4cf3f8af5a8a3ded090750ad1ed0982c.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/4cf3f8af5a8a3ded090750ad1ed0982c.jpeg" class="img-polaroid" title="33.jpeg" alt="33.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
4、配置 Nginx 中 <code class="prettyprint">nginx.conf</code> 文件：<br>
<pre class="prettyprint">location /html/ &#123;<br>
root   D:/data/;<br>
index  index.html index.htm;<br>
&#125;<br>
<br>
location /img/ &#123;<br>
root   D:/data/;<br>
autoindex on;#表示列出当前文件夹中的所有内容<br>
&#125; <br>
</pre><br>
5、启动 Nginx，访问其文件路径，在浏览器输入 <code class="prettyprint">http://localhost/html/a.html</code>，如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/be3f586bc07d2e993c4db736170a74c3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/be3f586bc07d2e993c4db736170a74c3.png" class="img-polaroid" title="34.png" alt="34.png" referrerpolicy="no-referrer"></a>
</div>
<br>
6、在浏览器输入 <code class="prettyprint">http://localhost/img/</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/b534f9603724ec13f072d9c90035f2ea.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/b534f9603724ec13f072d9c90035f2ea.jpg" class="img-polaroid" title="35.jpg" alt="35.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Nginx 工作原理</h3><h4>mater&worker</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/750d5bcbfd61d930e8e2b38808e8c4ea.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/750d5bcbfd61d930e8e2b38808e8c4ea.png" class="img-polaroid" title="36.png" alt="36.png" referrerpolicy="no-referrer"></a>
</div>
<br>
master 接收信号后将任务分配给 worker 进行执行，worker 可有多个。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/94f63a469a3f66f4e217659526885fb6.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/94f63a469a3f66f4e217659526885fb6.jpg" class="img-polaroid" title="37.jpg" alt="37.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>worker 如何工作</h4>客户端发送一个请求到 master 后，worker 获取任务的机制不是直接分配也不是轮询，而是一种争抢的机制，“抢”到任务后再执行任务，即选择目标服务器 Tomcat 等，然后返回结果。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/c6c4bac01b0e93679e64addccc19da42.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/c6c4bac01b0e93679e64addccc19da42.jpg" class="img-polaroid" title="38.jpg" alt="38.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>worker_connection</h4>普通的静态访问最大并发数是：<code class="prettyprint">worker_connections * worker_processes/ 2</code>；若是 HTTP 作为反向代理来说，最大并发数量应该是 <code class="prettyprint">worker_connections * worker_processes/ 4</code>，因为作为反向代理服务器，每个并发会建立与客户端的连接和后端服务器的连接，会占用两个连接。<br>
<br>当然了，worker 数也不是越多越好，worker 数和服务器的 CPU 数相等时最适宜的。<br>
<h4>优点</h4>可以使用 <code class="prettyprint">nginx –s reload</code> 热部署，利用 Nginx 进行热部署操作每个 woker 是独立的进程，若其中一个 woker 出现问题，其他继续进行争抢，实现请求过程，不会造成服务中断。<br>
<h3>总结</h3>关于 Nginx 的基本概念、安装教程、配置、使用实例以及工作原理，本文都做了详细阐述。希望本文对你有所帮助。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/C54SRalfhE3c33voPb21v" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/C54SRalfhE3c33voPb21v</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            