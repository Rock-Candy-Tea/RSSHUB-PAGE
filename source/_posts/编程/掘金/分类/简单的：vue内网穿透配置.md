
---
title: '简单的：vue内网穿透配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1327'
author: 掘金
comments: false
date: Mon, 24 May 2021 01:26:55 GMT
thumbnail: 'https://picsum.photos/400/300?random=1327'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">什么是内网穿透：</h1>
<p><strong>一般来说我们在本地运行项目，都是通过</strong></p>
<pre><code class="hljs language-js copyable" lang="js">http:<span class="hljs-comment">//localhost:8082/ </span>

http:<span class="hljs-comment">//10.0.10.27:8082/</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>这样来访问本地运行的项目，不知道大家有没有遇到过这样访问本地项目的</strong>：</p>
<pre><code class="hljs language-js copyable" lang="js">http:<span class="hljs-comment">//dev.xxxxxxxx.cn:8080/618</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>通过一个域名地址来访问本地项目；</strong></p>
<h3 data-id="heading-1">为什么要这样访问呢？</h3>
<ul>
<li>
<p>提供内网穿透服务</p>
</li>
<li>
<p>连接内网服务器，在外网演示内网web站点</p>
</li>
<li>
<p>无需服务器部署，快速调试本地程序，方便快速开发微信公众号和微信小程序</p>
</li>
<li>
<p>支持http、https协议站点，省去证书中间件复杂配置，http协议站点直接升级为https站点</p>
</li>
<li>
<p>支持TCP，UDP协议端口转发。支持数据库、SSH、远程桌面、网络摄像头等等开放到外网。</p>
</li>
</ul>
<h1 data-id="heading-2">简单实现：</h1>
<h3 data-id="heading-3">怎么实现呢?（vue为例）</h3>
<p>第一步，修改vue的配置 <strong>disableHostCheck</strong></p>
<p><em>disableHostCheck是webpack中webpack-dev-server的一个配置项；
感兴趣大家可以自己去看一下；</em></p>
<pre><code class="hljs language-js copyable" lang="js">vue-cli版本<span class="hljs-number">3.0</span>的情况下修改vue.config.js的配置

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">disableHostCheck</span>: <span class="hljs-literal">true</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一步是让vue <strong>本地服务</strong> 能被<strong>外部IP</strong>访问；</p>
<p>接着就是修改本地电脑的 host配置：</p>
<p>一般来说window的host文件路径为：</p>
<p><strong>C:\WINDOWS\system32\drivers\etc</strong></p>
<p>host文件内容：</p>
<pre><code class="hljs language-js copyable" lang="js"># Copyright (c) <span class="hljs-number">1993</span>-<span class="hljs-number">2009</span> Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP <span class="hljs-keyword">for</span> Windows.
#
# This file contains the mappings <span class="hljs-keyword">of</span> IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed <span class="hljs-keyword">in</span> the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such <span class="hljs-keyword">as</span> these) may be inserted on individual
# lines or following the machine name denoted by a <span class="hljs-string">'#'</span> symbol.
#
# For example:
#
#      <span class="hljs-number">102.54</span><span class="hljs-number">.94</span><span class="hljs-number">.97</span>     rhino.acme.com          # source server
#       <span class="hljs-number">38.25</span><span class="hljs-number">.63</span><span class="hljs-number">.10</span>     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#<span class="hljs-number">127.0</span><span class="hljs-number">.0</span><span class="hljs-number">.1</span>       localhost
#::<span class="hljs-number">1</span>             localhost

<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加我们的域名地址：</p>
<pre><code class="hljs language-js copyable" lang="js">    增加这一句
    
       <span class="hljs-number">127.0</span><span class="hljs-number">.0</span><span class="hljs-number">.1</span>  你的域名
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后：</p>
<pre><code class="hljs language-js copyable" lang="js"># Copyright (c) <span class="hljs-number">1993</span>-<span class="hljs-number">2009</span> Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP <span class="hljs-keyword">for</span> Windows.
#
# This file contains the mappings <span class="hljs-keyword">of</span> IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed <span class="hljs-keyword">in</span> the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such <span class="hljs-keyword">as</span> these) may be inserted on individual
# lines or following the machine name denoted by a <span class="hljs-string">'#'</span> symbol.
#
# For example:
#
#      <span class="hljs-number">102.54</span><span class="hljs-number">.94</span><span class="hljs-number">.97</span>     rhino.acme.com          # source server
#       <span class="hljs-number">38.25</span><span class="hljs-number">.63</span><span class="hljs-number">.10</span>     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#<span class="hljs-number">127.0</span><span class="hljs-number">.0</span><span class="hljs-number">.1</span>       localhost
#::<span class="hljs-number">1</span>             localhost


       <span class="hljs-number">127.0</span><span class="hljs-number">.0</span><span class="hljs-number">.1</span>     dev.xxxxxxx.cn

<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后大功告成：</p>
<p>我们就可以 这样<strong><a href="http://dev.xxxxxxxx.cn:8080/618" target="_blank" rel="nofollow noopener noreferrer">dev.xxxxxxxx.cn:8080/618</a></strong> 访问本地的项目了；</p></div>  
</div>
            