
---
title: 'nginx+云服务器配置前端项目'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca16340faee4426c8f6434f506bb71e5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 00:06:23 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca16340faee4426c8f6434f506bb71e5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">打包前端项目</h2>
<p>以我自己的项目为例子</p>
<ol>
<li>在项目根路径下的<code>vue.config.js</code>里面配置部署应用包时的基本 URL <code>publicPath</code>，不配置的话默认是 <code>publickPath:"/"</code>；</li>
</ol>
<pre><code class="copyable">module.exports = &#123;
  publicPath: "/",
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>为了统一<code>vue-router</code>路由的<code>base</code>和<code>publickPath</code>，可以这样写：</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  <span class="hljs-attr">base</span>: process.env.BASE_URL,
  routes
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包完前端项目后需要将要打包好的dist里面的文件放到服务器上，然后再配置nginx</p>
<h2 data-id="heading-1">在服务器上（linux系统）配置nginx</h2>
<p>因为我的项目用的是腾讯云服务器(centos6.5)，所以我就以这个举例子了</p>
<h3 data-id="heading-2">下载安装nginx</h3>
<p>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Flinux%2Fnginx-install-setup.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/linux/nginx-install-setup.html" ref="nofollow noopener noreferrer">www.runoob.com/linux/nginx…</a></p>
<ol>
<li>安装编译工具及文库</li>
</ol>
<pre><code class="copyable">yum -y install make zlib zlib-devel gcc-c++ libtool  openssl openssl-devel
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>先要安装 PCRE</li>
</ol>
<p>PCRE 作用是让 Nginx 支持 Rewrite 功能。</p>
<pre><code class="copyable">[root@bogon src]# cd /usr/local/src/
[root@bogon src]# wget http://downloads.sourceforge.net/project/pcre/pcre/8.35/pcre-8.35.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>解压安装包</li>
</ol>
<pre><code class="copyable">[root@bogon src]# tar zxvf pcre-8.35.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>进入安装目录编译安装</li>
</ol>
<pre><code class="copyable">[root@bogon src]# cd pcre-8.35
[root@bogon pcre-8.35]# ./configure
[root@bogon pcre-8.35]# make && make install
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>查看pcre版本</li>
</ol>
<pre><code class="copyable">[root@bogon pcre-8.35]# pcre-config --version
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca16340faee4426c8f6434f506bb71e5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="6">
<li>下载、编译安装 nginx</li>
</ol>
<pre><code class="copyable">[root@bogon src]# cd /usr/local/src/
[root@bogon src]# wget http://nginx.org/download/nginx-1.18.0.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解压安装包</p>
<pre><code class="copyable">[root@bogon src]# tar zxvf nginx-1.18.0.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<p>进入安装目录</p>
<pre><code class="copyable">[root@bogon src]# cd nginx-1.18.0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译安装</p>
<pre><code class="copyable">[root@bogon nginx-1.18.0]# ./configure --prefix=/usr/local/webserver/nginx --with-http_stub_status_module --with-http_ssl_module --with-pcre=/usr/local/src/pcre-8.35
[root@bogon nginx-1.18.0]# make
[root@bogon nginx-1.18.0]# make install
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li>查看nginx版本，看是否安装成功</li>
</ol>
<pre><code class="copyable">[root@bogon nginx-1.18.0]# /usr/local/webserver/nginx/sbin/nginx -v
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99d35ed69b1f4e7d96adba001c109f75~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
安装成功！！！</p>
<h3 data-id="heading-3">配置nginx、设置云服务器</h3>
<ol>
<li>配置nginx</li>
</ol>
<p>将打包好的前端项目放到 nginx安装目录=>html下，然后找到nginx安装目录=>conf=>nginx.conf,编辑nginx.conf文件<code>vi nginx.conf</code><br>
把这段替换成这样：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d1ea0f922b84379a65a008286651996~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
改成这样：</p>
<pre><code class="copyable">    location / &#123;
        index  index.html index.htm;
        try_files $uri $uri/ /index.html;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>保存文件<code>:wq</code></p>
<p>注意：<strong><code>SPA</code>是一种网络应用程序或网站的模型，所有用户交互是通过动态重写当前页面，不管我们应用有多少页面，构建物都只会产出一个<code>index.html</code>，当我们进入到子路由时刷新页面，<code>web</code>容器没有相对应的页面此时会出现404，</strong><br></p>
<p>解决办法：<strong>只需要配置将任意页面都重定向到 <code>index.html</code>，把路由交由前端处理，对<code>nginx</code>配置文件<code>.conf</code>修改，添加<code>try_files $uri $uri/ /index.html;</code></strong></p>
<p>所以如果前端项目路由用的是 history 模式，如果用默认配置可能会刷新页面404的问题
详情可以参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Finterview%2Fvue%2F404.html%23%25E4%25BA%258C%25E3%2580%2581404%25E9%2597%25AE%25E9%25A2%2598" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/interview/vue/404.html#%E4%BA%8C%E3%80%81404%E9%97%AE%E9%A2%98" ref="nofollow noopener noreferrer">vue3js.cn/interview/v…</a></p>
<p>vue-cli官方文档: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2Fconfig%2F%23publicpath" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/zh/config/#publicpath" ref="nofollow noopener noreferrer">cli.vuejs.org/zh/config/#…</a></p>
<ol start="2">
<li>启动nginx</li>
</ol>
<pre><code class="copyable">/usr/local/webserver/nginx/sbin/nginx
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>设置云服务器安全组规则开放入口</li>
</ol>
<p>找到云服务器控制台安全组配置规则点击一键放通</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b67aa985ba824e9e80429304b96a14a9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>关闭防火墙：<code>chkconfig iptables off</code></p>
<p>输入公网id地址查看成果</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89a79fbc60a542a1a95c9d6ded8bc700~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
到这一步就大功告成了！！！</p>
<h3 data-id="heading-4">常用命令</h3>
<pre><code class="copyable">/usr/local/webserver/nginx/sbin/nginx -s reload            # 重新载入配置文件
/usr/local/webserver/nginx/sbin/nginx -s reopen            # 重启 Nginx
/usr/local/webserver/nginx/sbin/nginx -s stop              # 停止 Nginx
chkconfig iptables off                                     # 关闭防火墙
/usr/local/webserver/nginx/sbin/nginx -t                   # 检查配置文件nginx.conf的命令
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">写在最后</h3>
<p>我是<strong>AndyHu</strong>，目前暂时是一枚前端搬砖工程师。</p>
<p>文中如有错误，欢迎在评论区指正，如果这篇文章帮到了你，欢迎点赞和关注</p>
<p><strong>让灵魂控制自己的皮囊才是真正的自由！！！</strong></p></div>  
</div>
            