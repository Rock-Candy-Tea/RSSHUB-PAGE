
---
title: '开源架构组件-varnish详解'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0227649303d4a368664b66b19cc2c31~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 02:30:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0227649303d4a368664b66b19cc2c31~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第9天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战 </a></p>
<h2 data-id="heading-0">varnish的介绍</h2>
<p>百度百科的概念：</p>
<p>Varnish是一款高性能的开源HTTP加速器，挪威最大的在线报纸 Verdens Gang (<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.vg.no" target="_blank" rel="nofollow noopener noreferrer" title="http://www.vg.no" ref="nofollow noopener noreferrer">www.vg.no</a>) 使用3台Varnish代替了原来的12台squid，性能居然比以前更好。</p>
<p>Varnish 的作者Poul-Henning Kamp是FreeBSD的内核开发者之一，他认为现在的计算机比起1975年已经复杂许多。在1975年时，储存媒介只有两种：内存与硬盘。但现在计算 机系统的内存除了主存外，还包括了cpu内的L1、L2，甚至有L3快取。硬盘上也有自己的快取装置，因此squid cache自行处理物件替换的架构不可能得知这些情况而做到最佳化，但操作系统可以得知这些情况，所以这部份的工作应该交给操作系统处理，这就是 Varnish cache设计架构。</p>
<p>varnish项目是2006年发布的第一个版本0.9.距今已经八年多了，此文档之前也提过varnish还不稳定，那是2007年时候编写的，经过varnish开发团队和网友们的辛苦耕耘，现在的varnish已经很健壮。很多门户网站已经部署了varnish，并且反应都很好，甚至反应比squid还稳定，且效率更高，资源占用更少。相信在反向代理，web加速方面，varnish已经有足够能力代替squid。</p>
<h2 data-id="heading-1">端口和官网</h2>
<p>varnish  的监听端口是6081       squid 的端口号3128</p>
<p>varnish 官网：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.varnish-cache.org" target="_blank" rel="nofollow noopener noreferrer" title="https://www.varnish-cache.org" ref="nofollow noopener noreferrer">varnish官方网站</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvarnish-cache.org%2Fdocs%2F6.3%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://varnish-cache.org/docs/6.3/" ref="nofollow noopener noreferrer">varish官方文档-6.3</a></p>
<h2 data-id="heading-2">varnish 特点：</h2>
<p>相比squid</p>
<p>1） 缓存方式：
varnish可以基于内存缓存，也可以在磁盘上缓存,可以利用虚拟内存缓存，支持设置0-60S精确缓存时间。
而squid 是将元数据缓存在内存，存储缓存在硬盘</p>
<p>2） ACL
varnish 配置是通过VAL语言来完成的，配置要先转换成C代码，所以使用VCL所写的配置要先转换C语言代码，因此要依赖于GCC临时编译VCL配置，编译完成后才能运行</p>
<h2 data-id="heading-3">varnish缓存数据的原理</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0227649303d4a368664b66b19cc2c31~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">varnish的安装</h2>
<h3 data-id="heading-5">1. 安装依赖包</h3>
<pre><code class="hljs language-bash copyable" lang="bash">yum install autoconf.noarch automake.noarch jemalloc-devel.x86_64 libedit-devel.x86_64 libtool.x86_64 ncurses-devel.x86_64 pcre-devel.x86_64 pkgconfig.x86_64 python-docutils.noarch python-sphinx.noarch graphviz.x86_64 -y

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2. 上传安装包并解压</h3>
<pre><code class="hljs language-bash copyable" lang="bash">[root@xinsz08-62 桌面]<span class="hljs-comment"># ls</span>
nethogs-0.8.5-1.el7.x86_64.rpm
 varnish-6.2.3.tgz

<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用file查看文件</p>
<pre><code class="hljs language-bash copyable" lang="bash">[root@xinsz08-62 桌面]<span class="hljs-comment"># file varnish-6.2.3.tgz </span>
varnish-6.2.3.tgz: gzip compressed data, from Unix, last modified: Fri Jan 31 20:18:02 2020, max compression

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash">
[root@xinsz08-62 ~]<span class="hljs-comment"># file varnish-6.2.3.tgz </span>
varnish-6.2.3.tgz: gzip compressed data, from Unix, last modified: Fri Jan 31 20:18:02 2020, max compression
[root@xinsz08-62 ~]<span class="hljs-comment"># gunzip varnish-6.2.3.tgz </span>
[root@xinsz08-62 ~]<span class="hljs-comment"># ls     </span>
  varnish-6.2.3.tar  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解压：</p>
<pre><code class="hljs language-bash copyable" lang="bash">[root@xinsz08-62 ~]<span class="hljs-comment"># tar xf varnish-6.2.3.tar </span>
[root@xinsz08-62 ~]<span class="hljs-comment"># ls</span>
  varnish-6.2.3      
  varnish-6.2.3.tar  
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">3. 进入目录并编译安装</h3>
<pre><code class="hljs language-bash copyable" lang="bash">[root@xinsz08-62 ~]<span class="hljs-comment"># cd varnish-6.2.3/</span>
[root@xinsz08-62 varnish-6.2.3]<span class="hljs-comment"># ls</span>
aclocal.m4   configure     lib          README.Packaging
autogen.sh   configure.ac  LICENSE      README.rst
bin          doc           m4           varnishapi.pc.in
build-aux    etc           Makefile.am  varnishapi-uninstalled.pc.in
ChangeLog    include       Makefile.in  varnish-legacy.m4
config.h.in  INSTALL       man          varnish.m4
[root@xinsz08-62 varnish-6.2.3]<span class="hljs-comment"># </span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译安装</p>
<pre><code class="hljs language-bash copyable" lang="bash">[root@xinsz08-62 varnish-6.2.3]<span class="hljs-comment"># ./autogen.sh </span>
[root@xinsz08-62 varnish-6.2.3]<span class="hljs-comment"># ./configure && make && make install </span>
[root@xinsz08-62 varnish-6.2.3]<span class="hljs-comment"># ldconfig</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>备注： ldconfig</p>
<p>ldconfig命令的用途:
在默认搜寻目录/lib和/usr/lib以及动态库配置文件/etc/ld.so.conf内所列的目录下，搜索出可共享的动态链接库（格式如lib*.so*）,进而创建出动态装入程序(ld.so)所需的连接和缓存文件。</p>
<p>缓存文件默认为/etc/ld.so.cache，此文件保存已排好序的动态链接库名字列表，为了让动态链接库为系统所共享，需运行动态链接库的管理命令ldconfig，此执行程序存放在/sbin目录下。</p>
<p>简而言之： ldconfig是一个动态链接库管理命令，其目的为了让动态链接库为系统所共享，而当用户安装了一个新的动态链接库时，就需要手工运行这个命令。</p>
<h3 data-id="heading-8">4. 检查版本及启动</h3>
<pre><code class="hljs language-bash copyable" lang="bash">[root@xinsz08-62 varnish-6.2.3]<span class="hljs-comment"># varnishd -V</span>
varnishd (varnish-6.2.3 revision 84d239c93e756ae255b6abb459c1052a36a409e9)
Copyright (c) 2006 Verdens Gang AS
Copyright (c) 2006-2019 Varnish Software AS

启动
[root@xinsz08-62 varnish-6.2.3]<span class="hljs-comment"># varnishd -a :6081 -T localhost:6802 -b localhost:8080</span>
<span class="hljs-comment"># </span>
[root@xinsz08-62 ~]<span class="hljs-comment"># ps -ef |grep varnish</span>
root      39814      1  0 11:35 ?        00:00:00 varnishd -a :6081 -T localhost:6082 -b localhost:8080
root      39825  39814  0 11:35 ?        00:00:00 varnishd -a :6081 -T localhost:6082 -b localhost:8080
root      43050  41288  0 12:05 pts/5    00:00:00 grep --color=auto varnish

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">总结</h2>
<p>varnish就给你介绍到这里了，在公司里用的比较多的还是varnish，建议跟着实验做一遍。</p></div>  
</div>
            