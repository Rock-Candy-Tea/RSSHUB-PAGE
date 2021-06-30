
---
title: 'LAMP架构（宝，我重构了，输的是 LAMP 架构）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c386af90d404aec96c1362d3ecfc2c3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 24 Jun 2021 15:03:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c386af90d404aec96c1362d3ecfc2c3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 25 天，活动详情查看<a href="https://juejin.cn/post/6967194882926444557" target="_blank">：更文挑战</a></p>
<hr>
<blockquote>
<p>一名致力于在技术道路上的终身学习者、实践者、分享者，一位忙起来又偶尔偷懒的原创博主，一个偶尔无聊又偶尔幽默的少年。</p>
<p>欢迎各位掘友们微信搜索「<strong>杰哥的IT之旅</strong>」关注！</p>
<p>原文链接：<a href="https://mp.weixin.qq.com/s/Awi7lt7DJ9woTZBRRyuXTg" target="_blank" rel="nofollow noopener noreferrer">架构篇 | 带你轻松玩转 LAMP 网站架构平台（一）</a></p>
</blockquote>
<h3 data-id="heading-0">前言</h3>
<p>在前面的文章中，介绍了如何在 Linux 环境下搭建 HTTPD 服务、MySQL 数据库系统以及 HTTPD 服务的访问控制等等；相关文章可看文末推荐阅读系列，那么在今天的文章里，将介绍 <code>LAMP 架构</code>。</p>
<h3 data-id="heading-1">一、什么是 LAMP 架构？</h3>
<p>LAMP 架构是成熟的企业网站应用模式之一，能够协同工作的一套系统及相关软件，能够提供动态 Web 站点服务及其应用开发环境。</p>
<p>LAMP 是一个缩写词，<code>L</code>:<code>Linux操作系统</code>，<code>A</code>:<code>Apache网站服务器</code>，<code>M</code>:<code>MySQL数据库服务器</code>，<code>P</code>:<code>PHP、Python、Perl编程语言</code>;</p>
<h3 data-id="heading-2">二、LAMP 架构平台的构成组件</h3>
<ul>
<li>
<p><code>Linux操作系统</code>:是 LAMP 架构的基础，用于支撑 Web 站点的操作系统，具有良好的稳定性、兼容性；</p>
</li>
<li>
<p><code>Apache网站服务器</code>:是 LAMP 架构的前端，功能强大、稳定性好的 Web 服务器程序，面向用户提供网站访问、发送网页、文件、图片等内容；</p>
</li>
<li>
<p><code>MySQL数据库服务器</code>:是 LAMP 架构的后端，开源关系型数据库系统，数据用于存储在 MySQL 数据库中，可通过 SQL 语句来查询；</p>
</li>
<li>
<p><code>PHP、Python、Perl编程语言</code>:动态网页的编程语言，用于解释动态网页文件，提供 Web 应用程序的开发和运行环境。PHP 是一种被广泛应用的开放源代码的多用途脚本语言，可嵌入到 HTML 中，适用于 Web 应用开发。</p>
</li>
</ul>
<h3 data-id="heading-3">三、LAMP 架构平台的应用优势</h3>
<ul>
<li>
<p><code>成本低</code>：开放源代码的软件，可自由获得和免费使用，技术上和许可证上没有太严格的限制，大大降低企业的实施成本。</p>
</li>
<li>
<p><code>可定制</code>：拥有大量的额外组件和可扩展功能的模块，能够满足企业应用的定制需求，可自行开发、添加新的功能。</p>
</li>
<li>
<p><code>易开发</code>：基于 LAMP 平台的动态网站中，页面代码简洁，与 HTML 标记语言的结合度非常好，也能够轻松读懂及修改网页代码。</p>
</li>
<li>
<p><code>方便易用</code>：PHP 编程语言属于解释性语言，开发的各种 Web 程序不需要编译，方便移植使用，整套的网站项目程序，可通过复制到网站目录中，便可以访问。</p>
</li>
<li>
<p><code>安全稳定</code>：得益于开源的优势，</p>
</li>
</ul>
<h3 data-id="heading-4">四、构建 PHP 运行环境</h3>
<p><code>PHP：Hypertext Preprocessor，超文本预处理器的字母缩写</code>，是一种被广泛应用的开放源代码的多用途脚本语言，可嵌入到 HTML 中，适用于 Web 应用开发，且拥有更好的网页执行速度、支持绝大多数流行的数据库及多种操作系统。</p>
<h4 data-id="heading-5">安装 PHP 软件包</h4>
<p><strong>准备工作</strong></p>
<p>为避免发生程序冲突等现象，先以<code>rpm</code>的方式安装<code>php</code>及相关依赖包。</p>
<p>如果已经存在了，可根据实际情况可<code>卸载 php php-cli php-ldap php-common php-mysql</code>等，另外，需安装<code>zlib-devel</code>和<code>libxml2-devel</code>包。</p>
<pre><code class="copyable">[root@localhost lamp]# rpm -e php php-cli php-ldap php-common php-mysql --nodeps
[root@localhost lamp]# rpm -ivh /mnt/Packages/zlib-devel-1.2.3-29.el6.x86_64.rpm 
[root@localhost lamp]# rpm -ivh /mnt/Packages/libxml2-devel-2.7.6-14.el6.x86_64.rpm
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">安装扩展工具库</h4>
<p>在企业实际应用中，一部分基于<code>PHP</code>开发的<code>Web</code>应用系统会需要额外的扩展工具。</p>
<p>例如：<code>数据加密工具：libmcrypt、mhash、mcrypt</code>等，本篇文章所涉及到的安装包将一并打包放在<code>公众号后台</code>，大家可通过文末的<code>获取</code>方式进行获取<code>或</code>通过<code>站点：http://sourceforge.net</code>下载，在安装<code>PHP</code>软件包之前，需先安装好这些扩展工具。</p>
<p><strong>安装 libmcrypt</strong></p>
<pre><code class="copyable">[root@localhost lamp]# tar zxf libmcrypt-2.5.8.tar.gz -C /usr/src/
[root@localhost lamp]# cd /usr/src/libmcrypt-2.5.8/
[root@localhost libmcrypt-2.5.8]# ./configure
[root@localhost libmcrypt-2.5.8]# make && make install
[root@localhost libmcrypt-2.5.8]# ln -s /usr/local/lib/libmcrypt.* /usr/lib/
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>安装 mhash</strong></p>
<pre><code class="copyable">[root@localhost lamp]# tar zxf mhash-0.9.9.9.tar.gz -C /usr/src/
[root@localhost lamp]# cd /usr/src/mhash-0.9.9.9/
[root@localhost mhash-0.9.9.9]# ./configure
[root@localhost mhash-0.9.9.9]# make && make install
[root@localhost mhash-0.9.9.9]# ln -s /usr/local/lib/libmhash* /usr/lib/
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>安装 mcrypt</strong></p>
<pre><code class="copyable">[root@localhost lamp]# tar zxf mcrypt-2.6.8.tar.gz -C /usr/src/
[root@localhost lamp]# cd /usr/src/mcrypt-2.6.8/
[root@localhost mcrypt-2.6.8]# ./configure
[root@localhost mcrypt-2.6.8]# ln -s /usr/local/bin/libmcrypt-config /usr/bin/libmcrypt-config
[root@localhost mcrypt-2.6.8]# export LD_LIBRARY_PATH=/usr/local/lib: LD_LIBRARY_PATH     # 解决 configure 配置报错的现象
[root@localhost mcrypt-2.6.8]# ./configure
[root@localhost mcrypt-2.6.8]# make && make install
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">编译并安装 PHP</h4>
<p><strong>解包</strong></p>
<p>将下载的<code>PHP</code>源码包解压并释放到<code>/usr/src</code>目录下，且切换到该目录下。</p>
<pre><code class="copyable">[root@localhost lamp]# tar zxf php-5.3.28.tar.gz -C /usr/src/
[root@localhost lamp]# cd /usr/src/php-5.3.28/
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p>定制<code>PHP</code>的配置选项时，需指定<code>httpd</code>和<code>mysqld</code>的安装路径，便于添加相关支持设置，使<code>LAMP</code>各组件协同工作。还需指定<code>安装路径</code>、<code>启用多字节支持</code>、<code>加密扩展支持</code>等。</p>
<pre><code class="copyable">[root@localhost php-5.3.28]# ./configure --prefix=/usr/local/php5 --with-mcrypt --with-apxs2=/usr/local/httpd/bin/apxs --with-mysql=/usr/local/mysql --with-config-file-path=/usr/local/php5 --enable-mbstring
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">各参数选项所包含的含义：</h4>
<ul>
<li>
<p>--prefix：指定将<code>PHP</code>程序安装到哪个目录下；</p>
</li>
<li>
<p>--with-mcrypt：<code>加载数据加密等扩展工具</code>；</p>
</li>
<li>
<p>--with-apxs2：设置<code>apache http server</code>提供的 apxs 模块支持程序的文件位置；</p>
</li>
<li>
<p>--with-mysql：设置<code>MySQL 数据库</code>服务程序的安装位置；</p>
</li>
<li>
<p>--with-config-file-path：设置<code>PHP</code>的配置文件<code>php.ini</code>将要存放的位置；</p>
</li>
<li>
<p>--enable-mbstring：<code>启用多字节字符串功能，支持中文等代码</code>；</p>
</li>
</ul>
<p>如果在配置的过程中，出现如下报错，已导致编译不成功的现象时；</p>
<pre><code class="copyable">configure: error: Cannot find libmysqlclient under /usr.
Note that the MySQL client library is not bundled anymore!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过查找 libmysqlclient，发现是在 /usr/lib64/mysql/ 目录内的 libmysqlclient.so.16.0.0 做的软连接，PHP默认是去的 /usr/lib/ 搜索，所以没有找到，找到问题了就好解决了。</p>
<p><strong>解决办法</strong></p>
<p>执行如下命令即可；</p>
<pre><code class="copyable">cp -rp /usr/lib64/mysql/libmysqlclient.so.15.0.0 /usr/lib/libmysqlclient.so
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c386af90d404aec96c1362d3ecfc2c3~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>编译及安装</strong></p>
<p>编译过程较长，期间未出现错误，则说明<code>PHP</code>程序的安装过程基本就完成了。</p>
<pre><code class="copyable">[root@localhost php-5.3.28]# make && make install
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bf56fca1bc641d68188f2b0ddc76da9~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">五、设置 LAMP 组件环境</h3>
<p><strong>主要包括</strong></p>
<ul>
<li>
<p><code>PHP 的配置文件 php.ini</code>：确定 PHP 的运行参数；</p>
</li>
<li>
<p><code>Apache 的配置文件 httpd.conf</code>：加载 libphp5.so 模块，便于支持 PHP 网页；</p>
</li>
</ul>
<h4 data-id="heading-10">php.ini 配置调整</h4>
<p>php.ini 的建立及基本设置，安装好的 PHP 软件包，服务器不会自动创建 php.ini 文件，但在源码目录下分别有两个 <code>php.ini 开头的样例配置文件，分别用于开发环境和生产环境</code>。</p>
<pre><code class="copyable">[root@localhost php-5.3.28]# ll php.ini-*
-rw-r--r--. 1 501 games 69606 12月 11 2013 php.ini-development   # 开发样例文件
-rw-r--r--. 1 501 games 69627 12月 11 2013 php.ini-production   # 生产样例文件
<span class="copy-code-btn">复制代码</span></code></pre>
<p>选择其中一个样例文件，并复制到<code>PHP</code>的配置文件目录<code>/usr/local/php5</code>下，并改名为<code>php.ini</code>。</p>
<pre><code class="copyable">[root@localhost php-5.3.28]# cp /usr/src/php-5.3.28/php.ini-development /usr/local/php5/php.ini
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改<code>php.ini</code>文件中的配置内容，可控制<code>PHP</code>网页的执行特性。</p>
<p>是否允许用户上传文件、设置上传文件的大小限制、设置默认使用的字符集、加载额外的扩展模块等；</p>
<pre><code class="copyable">[root@localhost php-5.3.28]# vi /usr/local/php5/php.ini 
784 default_charset = "uft-8"               # 设置默认字符集:utf-8
882 file_uploads = On                       # 允许通过 PHP 网页上传文件
891 upload_max_filesize = 2M                # 允许上传的文件大小限制
894 max_file_uploads = 20                   # 每个 HTTP 最大允许请求上传的文件数
740 post_max_size = 8M                      # 每次通过表单 post 提交的数据量限制
226 short_open_tag = On                     # 允许识别 PHP 短语法标记
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>添加 ZendGuardLoader 优化模块</code>，来提高<code>PHP</code>程序的执行效率，优化页面加载速度。此优化模块适用于 PHP 5.3 系列版本，同时也可以从<code>官方站点：http://www.zend.com 下载</code>。</p>
<p>首先将下载的<code>ZendGuardLoader</code>包进行解压到<code>/usr/src</code>目录下，并将其中的<code>php-5.3.x</code>目录下的模块文件复制到<code>PHP</code>程序的模块文件夹。</p>
<pre><code class="copyable">[root@localhost lamp]# tar zxf ZendGuardLoader-php-5.3-linux-glibc23-x86_64.tar.gz -C /usr/src/
[root@localhost lamp]# cd /usr/src/ZendGuardLoader-php-5.3-linux-glibc23-x86_64/php-5.3.x/
[root@localhost php-5.3.x]# cp ZendGuardLoader.so /usr/local/php5/lib/php
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改<code>php.ini</code>配置文件，添加加载及启用<code>ZendGuardLoader.so</code>模块的配置语句。</p>
<pre><code class="copyable">[root@localhost php-5.3.x]# vi /usr/local/php5/php.ini
1919 zend_extension=/usr/local/php5/lib/php/ZendGuardLoader.so
1920 zend_loader.enable=1
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">httpd.conf 配置调整</h4>
<p>使<code>httpd服务器</code>支持<code>PHP</code>页面解析功能，需通过<code>LoadModule</code>配置项加载<code>PHP</code>程序的模块文件，然后添加<code>AddType</code>配置项并支持对<code>.php</code>类型的网页文件，还需要将<code>DirectoryIndex</code>配置行添加配置项<code>index.php</code>和<code>index.html</code>来进行识别常见的<code>PHP</code>首页文件。</p>
<p>重启<code>httpd</code>服务，并更新配置项；</p>
<pre><code class="copyable">[root@localhost php-5.3.x]# vi /usr/local/httpd/conf/httpd.conf
53 LoadModule php5_module        modules/libphp5.so
54 AddType application/x-httpd-php .php
170 DirectoryIndex index.php index.html
[root@localhost php-5.3.x]# /usr/local/httpd/bin/apachectl restart
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>上述各项配置的所包含的含义</strong></p>
<p>LoadModule 是安装<code>PHP</code>过程中自动添加的，AddType 需手动添加，DirectoryIndex 需在原有的基础上进行修改即可；</p>
<ul>
<li>
<p><code>php5_module</code>：模块名称；</p>
</li>
<li>
<p><code>modules/libphp5.so</code>：模块文件位置；</p>
</li>
</ul>
<h3 data-id="heading-12">六、测试 LAMP 是否已经搭建成功</h3>
<p>完成<code>PHP</code>相关扩展工具的安装及配置以后，便可以对相关功能进行测试验证<code>LAMP架构平台</code>并在网站的根目录下<code>/usr/local/httpd/htdocs/</code>创建相应的测试<code>PHP</code>网页，通过浏览器进行访问，来进行判断<code>LAMP</code>是否已经搭建成功，</p>
<p>通过两种方式来进行验证：</p>
<ul>
<li>
<p><code>PHP 网页解析是否成功；</code></p>
</li>
<li>
<p><code>访问 MySQL 数据库系统进行验证；</code></p>
</li>
</ul>
<h4 data-id="heading-13">测试 PHP 网页是否正常</h4>
<p>编写一个后缀名为<code>test1.php</code>格式的网页文件，结合<code>PHP</code>内建的<code>phpinfo( )</code>函数来显示服务器的<code>PHP</code>环境信息，文件中的代码应包括<code><?php···?></code>标记之间，并将该文件放在网站根目录下<code>/usr/local/httpd/htdocs/</code>。</p>
<pre><code class="copyable">[root@localhost php-5.3.x]# vi /usr/local/httpd/htdocs/test1.php
<?php
phpinfo( );
?>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过浏览器访问名为：<code>test1.php</code>的测试网页。</p>
<p>例如：<code>http://www.jacktiangjwan.com/test1.php</code></p>
<p>便可以看出<code>PHP</code>程序的版本号、配置命令、运行变量等信息；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b198bb607d04134849d4357c5bdde65~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">测试 PHP 网页是否能够正常访问 MySQL 数据库</h4>
<p>编写一个后缀名为<code>test2.php</code>格式的网页文件，<code>添加数据库的操作命令</code>，用于验证与<code>MySQL 数据库</code>的连接，查询等操作。</p>
<ul>
<li>
<p><code>mysql_connect()函数</code>：用于连接<code>MySQL数据库</code>，需指定目标主机地址、用户名、密码；</p>
</li>
<li>
<p><code>mysql_close</code>：断开数据库连接；</p>
</li>
</ul>
<pre><code class="copyable">[root@localhost mysql-5.5.22]# vi /usr/local/httpd/htdocs/test2.php 
<?php
$link=mysql_connect('127.0.0.1','root','666666');    # 连接 MySQL 数据库
if($link) echo "恭喜你，成功连接到 MySQL 数据库!";     # 连接成功时的返回信息
mysql_close();                                       # 断开数据库连接
?>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重启服务</p>
<pre><code class="copyable">[root@localhost mysql-5.5.22]# /usr/local/httpd/bin/apachectl restart
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过浏览器访问名为：<code>test2.php</code>的测试网页。</p>
<p>例如：<code>http://www.jacktiangjwan.com/test2.php</code></p>
<p>便可以看到成功连接<code>MySQL 数据库</code>的提示信息，当你的是错误用户名及密码时，或<code>mysql_connect()函数</code>未运行而导致连接数据库失败，将提示报错的页面。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9242cb57bdf5440f8fe0fb8fd095f5c3~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">推荐阅读</h3>
<p><a href="https://juejin.cn/post/6976006631028949022" target="_blank">手把手教你在 Linux 环境下部署 MySQL 数据库！</a></p>
<p><a href="https://juejin.cn/post/6976382902741237796" target="_blank">MySQL | MySQL 数据库系统（二）- SQL语句的基本操作</a></p>
<p><a href="https://juejin.cn/post/6976757259720196110" target="_blank">MySQL | MySQL 数据库系统（三）- 数据库的用户授权</a></p>
<p><a href="https://juejin.cn/post/6977124758378774536" target="_blank">MySQL | MySQL 数据库系统（四）- 数据库的备份与恢复</a></p>
<hr>
<p><strong>原创不易，如果你觉得这篇文章对你有点用的话，麻烦你为本文点个赞、评论或转发一下，因为这将是我输出更多优质文章的动力，感谢！</strong></p>
<p><strong>对了，掘友们记得给我点个免费的关注哟！防止你迷路下次就找不到我了。</strong></p>
<p><strong>我们下期再见！</strong></p></div>  
</div>
            