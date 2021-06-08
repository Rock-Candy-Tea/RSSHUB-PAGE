
---
title: '前端架构之Nginx （二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c3bf51319be4c239a6f19f5d0bce3d8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 23:19:03 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c3bf51319be4c239a6f19f5d0bce3d8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">Linux 版本安装</h3>
<p>关于 Nginx 的安装，分为在 Windows 平台和 Linux 平台安装，Windows 版本的 Nginx 服务器在效率上要比 Linux 版本的 Nginx 服务器差一些，而且实际使用的一般都是 Linux 平台的 Nginx 服务器。所以后期我们介绍时也会以 Linux 版本的为主。</p>
<h4 data-id="heading-1">1、安装gcc</h4>
<p>安装 nginx 需要先将官网下载的源码进行编译，编译依赖 gcc 环境，如果没有 gcc 环境，则需要安装：</p>
<pre><code class="hljs language-js copyable" lang="js">yum install gcc-c++
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">2、PCRE pcre-devel 安装</h4>
<p>对于 pcre，prce(Perl Compatible Regular Expressions)是一个Perl库，包括 perl 兼容的正则表达式库。nginx的http模块使用pcre来解析正则表达式，所以需要在linux上安装pcre库。</p>
<pre><code class="hljs language-js copyable" lang="js">yum install -y pcre pcre-devel
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">3、zlib 安装</h4>
<p>zlib 库提供了很多种压缩和解压缩的方式， nginx 使用 zlib 对 http 包的内容进行 gzip ，所以需要在 Centos 上安装 zlib 库。</p>
<pre><code class="hljs language-js copyable" lang="js">yum install -y zlib zlib-devel
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">4、OpenSSL 安装</h4>
<p>　对于 openssl，OpenSSL 是一个强大的安全套接字层密码库，囊括主要的密码算法、常用的密钥和证书封装管理功能及SSL协议，并提供丰富的应用程序供测试或其它目的使用。
OpenSSL 是一个强大的安全套接字层密码库，囊括主要的密码算法、常用的密钥和证书封装管理功能及 SSL 协议，并提供丰富的应用程序供测试或其它目的使用。
nginx 不仅支持 http 协议，还支持 https（即在ssl协议上传输http），所以需要在 Centos 安装 OpenSSL 库。</p>
<pre><code class="hljs language-js copyable" lang="js">yum install -y openssl openssl-devel
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">5、下载安装包</h4>
<p>手动下载.tar.gz安装包，地址：<a href="https://nginx.org/en/download.html" target="_blank" rel="nofollow noopener noreferrer">nginx.org/en/download…</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c3bf51319be4c239a6f19f5d0bce3d8~tplv-k3u1fbpfcp-watermark.image" alt="ng.png" loading="lazy" referrerpolicy="no-referrer">
下载完毕上传到服务器上 /root</p>
<h4 data-id="heading-6">6、解压</h4>
<p>　　首先将下载的 nginx-1.20.1.zip.gz 文件复制到 Linux 系统中，然后解压：</p>
<pre><code class="hljs language-js copyable" lang="js">tar -zxvf nginx-<span class="hljs-number">1.18</span><span class="hljs-number">.0</span>.tar.gz
cd nginx-<span class="hljs-number">1.18</span><span class="hljs-number">.0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着进入到解压之后的目录，进行编译安装。</p>
<pre><code class="hljs language-js copyable" lang="js">./configure --prefix=<span class="hljs-regexp">/usr/</span>local/nginx
 make
 make install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：指定 /usr/local/nginx 为nginx 服务安装的目录。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6cfb9b1aea54b86a1633f6092a93c49~tplv-k3u1fbpfcp-watermark.image" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>查找安装路径： whereis nginx</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c5674878b84410aa176a71f82231584~tplv-k3u1fbpfcp-watermark.image" alt="kuangstudyf80f8dc2-d5df-4bc2-933d-6ce11f388f6e.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">7、启动 nginx</h4>
<h4 data-id="heading-8"></h4>
<p>进入到 /usr/local/nginx 目录，文件目录显示如下：</p>
<p><strong><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3aa430e73654c5b8b6c4cb2e742b8c7~tplv-k3u1fbpfcp-watermark.image" alt="11111.png" loading="lazy" referrerpolicy="no-referrer"></strong></p>
<p>接着我们进入到 <strong>sbin 目录</strong>，通过如下命令启动 nginx：</p>
<pre><code class="hljs language-js copyable" lang="js">./nginx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　Linux 没有消息就好消息，不提示任何信息说明启动成功。</p>
<p>　或者也可以输入如下命令，查看 nginx 是否有服务正在运行：</p>
<pre><code class="hljs language-js copyable" lang="js">ps -ef | grep nginx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　然后我们在浏览器输入Linux系统的IP地址，出现windows安装成功的界面即可。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acf0781bb43344e7bfe75cebc04d9588~tplv-k3u1fbpfcp-watermark.image" alt="e8b4f1b858004a73ada811e5c47a7041_tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">8、关闭 nginx</h4>
<h5 data-id="heading-10">有两种方式：</h5>
<p>　　<strong>方式1：快速停止</strong></p>
<pre><code class="hljs language-js copyable" lang="js"> cd /usr/local/nginx/sbin
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">./nginx -s stop
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　此方式相当于先查出nginx进程id再使用kill命令强制杀掉进程。不太友好。</p>
<p>　<strong>方式2：平缓停止</strong></p>
<pre><code class="hljs language-js copyable" lang="js"> cd /usr/local/nginx/sbin
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">./nginx -s quit
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　此方式是指允许 nginx 服务将当前正在处理的网络请求处理完成，但不在接收新的请求，之后关闭连接，停止工作。</p>
<h4 data-id="heading-11">9、重启 nginx</h4>
<p><strong>方式1：先停止再启动</strong></p>
<pre><code class="hljs language-js copyable" lang="js">./nginx -s quit
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"> ./nginx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　相当于先执行停止命令再执行启动命令。</p>
<p><strong>方式2：重新加载配置文件</strong></p>
<pre><code class="hljs language-js copyable" lang="js"> ./nginx -s reload
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　通常我们使用nginx修改最多的便是其配置文件 nginx.conf。修改之后想要让配置文件生效而不用重启 nginx，便可以使用此命令。</p>
<h4 data-id="heading-12">10、检测配置文件语法是否正确</h4>
<p>　　<strong>方式1：通过如下命令，指定需要检查的配置文件</strong></p>
<pre><code class="hljs language-js copyable" lang="js"> nginx -t -c  /usr/local/nginx/conf/nginx.conf
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　<strong>方式2：通过如下命令，不加 -c 参数，默认检测nginx.conf 配置文件</strong>。</p>
<pre><code class="hljs language-js copyable" lang="js">nginx -t 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/727ef700f2584b2bae6149c63f15bd76~tplv-k3u1fbpfcp-watermark.image" alt="1120165-20180831144536534-484136202.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            