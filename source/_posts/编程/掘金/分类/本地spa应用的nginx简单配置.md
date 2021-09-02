
---
title: '本地spa应用的nginx简单配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50f2f1d8c64347308bc5ed39ba674cd5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 01:00:58 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50f2f1d8c64347308bc5ed39ba674cd5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>最近碰到一个棘手的问题，开发打包都没问题，发到线上页面不出来报错：<code>Uncaught SyntaxError: Invalid or unexpected token</code>，为了方便调试于是使用<code>nginx</code>起本地服务，记录一下<code>nginx</code>的简单配置</p>
</blockquote>
<ul>
<li>常用命令放在前面(windows没有配置<code>nginx</code>全局环境变量的话需要到<code>nginx</code>的解压目录下运行命令)</li>
</ul>
<ol>
<li>启动：<code>start nginx</code>、<code>nginx</code></li>
<li>停止：<code>nginx -s stop</code>、<code>nginx -s quit</code></li>
<li>重启：<code>nginx -s reload</code></li>
<li>创建<code>nginx.pid</code>文件：<code>nginx -c conf/nginx.conf</code>。这条命令在使用停止启动命令报<code>nginx报错[error] CreateFile()</code>使用</li>
</ol>
<ul>
<li>下载与启动</li>
</ul>
<ol>
<li>下载地址<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnginx.org%2Fen%2Fdownload.html" target="_blank" rel="nofollow noopener noreferrer" title="https://nginx.org/en/download.html" ref="nofollow noopener noreferrer">nginx.org/en/download…</a>，页面有<code>Mainline version</code>(主版本)、<code>Stable version</code>(稳定版本)、<code>Legacy versions</code>(旧版本)可以下载。文章下载是稳定版，版本是<code>nginx-1.20.1</code></li>
<li>将下载的压缩包解压到某个文件夹下</li>
<li>启动
<ul>
<li>直接双击<code>nginx.exe</code>启动</li>
<li>打开<code>cmd</code>命令窗口，切到<code>nginx</code>解压目录下使用<code>nginx</code>、<code>start nginx</code>启动</li>
</ul>
</li>
<li>检查<code>nginx</code>是否启动成功
<ul>
<li>在浏览器地址栏输入网址<code>http://localhost:80</code>，出现<code>Welcome to nginx!</code>欢迎页面说明启动成功</li>
</ul>
</li>
</ol>
<ul>
<li>配置一个简单的<code>spa</code>项目的<code>server</code></li>
</ul>
<ol>
<li>编辑器打开<code>nginx</code>解压目录下<code>/conf/nginx.conf</code>配置文件，默认只有一个<code>server</code>配置内容<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50f2f1d8c64347308bc5ed39ba674cd5~tplv-k3u1fbpfcp-watermark.image" alt="nginx" loading="lazy" referrerpolicy="no-referrer">，这也是启动时欢迎页面的<code>server</code>配置</li>
<li>在现有的<code>server</code>配置下添加新的<code>server</code>
<ul>
<li><code>spa</code>应用没有基路径的<code>server</code>配置，前端文件地址结构为<code>项目地址/dist/index.html</code></li>
</ul>
<pre><code class="copyable">    server &#123;
        ... // 这是当前默认server内容
    &#125;
    server &#123;
        listen 8888; // 监听的端口号
        server_name localhost;
        root ../[项目地址]/dist; // 前端包地址（这里基于解压后的nginx.exe所在地址使用的相对路径）
        location / &#123;
            index /index.html;
            try_files $uri $uri/ /index.html; // spa应用的关键配置
        &#125;
        location ^~ /api/ &#123;
            # proxy_pass [接口代理地址]; // 接口代理地址
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>spa</code>应用有基路径的<code>server</code>配置，如最后访问页面地址是<code>localhost:8888/app/[route]</code>，前端文件地址结构为<code>项目地址/dist/index.html</code></li>
</ul>
<pre><code class="copyable">    server &#123;
        listen 8888; // 注意端口号不能重复
        server_name localhost;
        root ../[项目地址]/dist;

        location ^~ /app &#123; // 添加访问地址的基路径
            index /index.html;
            try_files $uri $uri/ /index.html;
        &#125;
        location ^~ /api/ &#123;
            # proxy_pass [接口代理地址];
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>添加新的<code>server</code>配置后保存<code>nginx.conf</code>文件</li>
<li>使用<code>nginx -s reload</code>命令重启<code>nginx</code>，这时候就能访问<code>http://localhost:8888/</code>或<code>http://localhost:8888/app/[route]</code>查看对应的<code>spa</code>应用了</li>
</ol></div>  
</div>
            