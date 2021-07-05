
---
title: 'nginx配置静态资源'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=2166'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 06:24:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=2166'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p> <strong>业务场景：</strong></p>
<p>app端的同事想要隐私协议和用户协议的h5静态资源，以方便用户点进去查看。</p>
<p><strong>解决办法：</strong></p>
<p>当时我有两个想法，一个是用web服务器配置静态资源，另外一个用nginx配置静态资源。</p>
<p>评估了一下，因当前项目用的技术架构前后端分离，用nginx做的反向代理和webpack打包的前端静态页面，并没有用到web服务器。所以最后选择了用nginx。</p>
<p>具体的操作：</p>
<p>进入nginx软件目录下，找到nginx.conf 文件，</p>
<p>vi命令打开此文件。</p>
<p>添加如下信息：</p>
<pre><code class="copyable">server &#123;
        listen       8091;
        server_name  localhost;

        location /private &#123;
            alias   html;
            index  index.html index.htm;
        &#125;

        location /user &#123;
            alias  test;
            index  index.html index.htm;
        &#125;
        error_page   500 502 503 504  /50x.html;
        location = /50x.html &#123;
            root   html;
        &#125;

     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里解释一下，上面配置的含义：</p>
<p>listen 代表监听的端口</p>
<p>server_name 代表监听的域名，没有的话一般默认localhost</p>
<p>location /private 代表拦截url为<a href="http://10.0.23.214:8091/private/" target="_blank" rel="nofollow noopener noreferrer">http://ip:8091/private/</a>的请求</p>
<p>alias 为别名 也可以设置为root其区别是root相当于default</p>
<p>alias 后面的html代表与nginx.conf 同一级别的静态资源目录</p>
<p>index 代表html文件的index.html作为首页。</p>
<p>location /use同理</p>
<p><strong>重启nginx的坑：</strong></p>
<p>部署时，先停止nginx进程再进行启动nginx。若直接执行./sbin/nginx -s reload 进行重启，亲测一般不会有效果</p>
<p>先执行停止nginx进程，再进行启动:</p>
<p>ps -ef|grep nginx    查询nginx的进程号，一般有两条，选以maste开头的那条。</p>
<p>kill -TERM xxx   杀死进程xxx，比暴力的命令“kill -9”稍微好些。</p>
<p>./sbin/nginx -c /usr/local/nginx/nginx.conf    启动nginx的命令。</p></div>  
</div>
            