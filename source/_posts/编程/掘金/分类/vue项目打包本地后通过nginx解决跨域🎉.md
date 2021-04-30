
---
title: 'vue项目打包本地后通过nginx解决跨域🎉'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfc0f24d71974879bd26eacb0079fb4f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 29 Apr 2021 18:41:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfc0f24d71974879bd26eacb0079fb4f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言☀️</h2>
<ul>
<li>有时候我们打包好<code>vue</code>项目让后端人员部署项目时可能会有小插曲，为了不麻烦后端人员和避免尴尬，最好的办法就是在本地自己先测一下，而在本地运行打包后的项目会遇到接口跨域的问题。我平时经常用的方法就是配置<code>nginx</code>设置反向代理解决跨域问题。</li>
</ul>
<h2 data-id="heading-1">准备过程🚴</h2>
<ul>
<li>安装<code>nginx</code>，具体怎么安装部署可以参考 <a href="https://blog.csdn.net/qq_33454884/article/details/89212702" target="_blank" rel="nofollow noopener noreferrer">传送门</a></li>
<li>准备打包后的<code>vue</code>项目</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfc0f24d71974879bd26eacb0079fb4f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">配置nginx🏂</h2>
<ul>
<li>编辑<code>nginx.conf</code> 配置文件</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df48e9cb95374438b8995a1d7089886f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/233387455172428ea3321bd80d720a42~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在配置文件中新增一个<code>server</code></li>
</ul>
<pre><code class="copyable">#新增一个服务
    server &#123;
        listen       8088; # 监听的端口
        server_name  localhost;

        location / &#123;
            root D://Thello/Project/kcgl; # vue 打包后静态文件存放的地址 如果/后面是t开头则要加多一个'/'
            index  index.html; # 默认主页地址
        &#125;

        
        location /kc &#123;
            proxy_pass http://ip地址/kc; # 代理接口地址（此处ip地址根据自己情况更换）
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">启动nginx</h2>
<blockquote>
<p>有两种方法启动<code>nginx</code></p>
</blockquote>
<ul>
<li>双击目录下的nginx.exe</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6b7340b6de047ec97645cecd7016dbb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>命令行进入该文件夹，执行<code>start nginx</code>命令，也会直接启动<code>nginx</code>服务器</li>
</ul>
<blockquote>
<p>启动后会出现一个小的黑色屏幕然后马上关闭</p>
</blockquote>
<h2 data-id="heading-4">验证</h2>
<p>输入在<code>http://localhost</code>会出现以下页面，表示已经访问成功！
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a771b0eea7141249f88bf6e9f8e6400~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>改为上方自己设置的端口号
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18143d605280442aadc01f8a8a01dfca~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
项目就已经运行起来了！！就可以愉快的测试了。</p>
<h2 data-id="heading-5">更多的nginx指令</h2>
<ul>
<li>启动服务：<code>start nginx</code></li>
<li>退出服务：<code>nginx -s quit</code></li>
<li>强制关闭服务：<code>nginx -s stop</code></li>
<li>重载服务：<code>nginx -s reload</code>　　（重启，服务不会中止）</li>
<li>验证配置文件：<code>nginx -t</code></li>
<li>使用配置文件：<code>nginx -c</code></li>
<li>使用帮助：<code>nginx -h</code></li>
</ul>
<blockquote>
<p>在操作中如果发现运行不了<code>nginx</code>则先通过命令行终止再打开即可</p>
</blockquote></div>  
</div>
            