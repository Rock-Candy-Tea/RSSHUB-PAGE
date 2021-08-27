
---
title: 'OpenResty - 高性能应用服务器框架'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=3034'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 15:05:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=3034'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;color:rgba(46,36,36,.87);overflow-x:hidden&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;margin-bottom:5px;font-size:30px;font-weight:500&#125;.markdown-body h1:before&#123;content:"#";margin-right:10px;color:#1976d2&#125;.markdown-body h2&#123;font-size:28px;font-weight:400;border-left:5px solid #454545;margin-top:20px;padding-left:10px;transition:all .3s ease-in-out&#125;.markdown-body h2:hover&#123;border-color:#1976d2&#125;.markdown-body h3&#123;font-size:24px;font-weight:400;margin-top:15px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:20px;font-weight:500&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body h2:first-letter,.markdown-body h3:first-letter,.markdown-body p:first-letter&#123;text-transform:capitalize&#125;.markdown-body em&#123;text-emphasis:dot;text-emphasis-position:under&#125;.markdown-body img&#123;display:block;margin:0 auto!important;max-width:100%;border-radius:2px;box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)!important&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#ddd,#999,#ddd);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;font-weight:900;word-break:break-word;border-radius:2px;overflow-x:auto;font-size:.87em;padding:.065em .4em;background-color:#fbe5e1;color:#c0341d&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:0 4px&#125;.markdown-body pre>code&#123;font-weight:400;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#027fff;transition:all .3s ease-in-out;padding-bottom:4px;border-bottom:2px solid transparent&#125;.markdown-body a:after&#123;content:"";display:inline-block;width:18px;height:18px;margin-left:4px;vertical-align:middle;background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMiIgaGVpZ2h0PSIyMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiMwMjdGRkYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PHBhdGggZD0iTTkuODE1IDYuNDQ4bDEuOTM2LTEuOTM2YzEuMzM3LTEuMzM2IDMuNTgtMS4yNTkgNS4wMTMuMTczIDEuNDMyIDEuNDMyIDEuNTEgMy42NzYuMTczIDUuMDEzbC0xLjQ1MiAxLjQ1Mi0uOTY4Ljk2OGMtMS4zMzcgMS4zMzYtMy41ODEgMS4yNTktNS4wMTMtLjE3MyIvPjxwYXRoIGQ9Ik0xMS4yNjcgMTUuMzY3bC0xLjkzNiAxLjkzNmMtMS4zMzYgMS4zMzctMy41OCAxLjI2LTUuMDEyLS4xNzMtMS40MzItMS40MzItMS41MS0zLjY3Ni0uMTczLTUuMDEybDEuNDUyLTEuNDUyLjk2OC0uOTY4YzEuMzM2LTEuMzM3IDMuNTgtMS4yNiA1LjAxMi4xNzMiLz48L2c+PC9zdmc+);background-size:cover;background-repeat:no-repeat&#125;.markdown-body a:hover&#123;border-color:#027fff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body a.footnote-backref:after,.markdown-body a.footnote-ref:after,.markdown-body sup a:after&#123;display:none!important&#125;.markdown-body table&#123;margin:0 auto 10px;font-size:12px;width:auto;max-width:100%;overflow:auto;border:2px solid #c6c6c6&#125;.markdown-body table img&#123;box-shadow:none!important&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body del&#123;color:rgba(0,0,0,.6)&#125;.markdown-body blockquote&#123;position:relative;color:#666;padding:5px 23px 1px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:hsla(0,0%,78.4%,.12);transition:all .2s ease-in-out&#125;.markdown-body blockquote:hover&#123;border-color:#1976d2&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;font-size:24px;font-weight:800;line-height:24px;color:#cbcbcb;opacity:.6&#125;.markdown-body blockquote:before&#123;content:"“";top:4px;left:6px&#125;.markdown-body blockquote:after&#123;content:"”";right:8px;bottom:-8px&#125;.markdown-body blockquote>p,.markdown-body blockquote blockquote&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #1976d2;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary:hover::-webkit-details-marker&#123;color:#1976d2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第27天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p>基于Nginx的模块化设计，衍生出了很多第三方模块以扩展Nginx的能力。其中，有一个<code>有趣</code>且影响深远的模块，即<code>lua-nginx-module</code>。它把Lua解析器内嵌到了Nginx中，从而可以使用Lua语言编程，极大增强了Nginx的能力。</p>
<blockquote>
<p>Lua是一种轻量，小巧的脚本语言，用标准的c语言编写并以源代码，其设计目的是   饿了嵌入应用程序中，从而为应用程序提供灵活的扩展和定制功能</p>
</blockquote>
<p>OpenResty(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fopenresty.org%2Fcn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://openresty.org/cn/" ref="nofollow noopener noreferrer">openresty.org/cn/</a>) 正是基于Nginx与Lua的高性能Web平台，其内部集成了大量精良的Lua库，第三方模块以及大多数依赖项，用于方便地搭建能够处理超高并发和扩展性极高的动态Web应用，Web服务和动态网关。</p>
<p>下面以Ubuntu 1604（LTS）为例，详细介绍了OpenResty的安装和使用</p>
<ol>
<li>安装相关依赖库，命令如下：</li>
</ol>
<pre><code class="copyable">sudo apt install -y libpcre3-dev libssl-dev perl make build-essential curl
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>从OpenResty官方(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fopenresty.org%2Fcn%2Fdownload.html)%25E4%25B8%258B%25E8%25BD%25BD%25E6%259C%2580%25E6%2596%25B0%25E7%259A%2584%25E6%25BA%2590%25E7%25A0%2581%25E5%258C%2585%25EF%25BC%258C%25E5%25B9%25B6%25E8%25A7%25A3%25E5%258E%258B%25EF%25BC%258C%25E7%25BC%2596%25E8%25AF%2591%25E5%2592%258C%25E5%25AE%2589%25E8%25A3%2585%25EF%25BC%258C%25E5%2591%25BD%25E4%25BB%25A4%25E5%25A6%2582%25E4%25B8%258B%25EF%25BC%259A" target="_blank" rel="nofollow noopener noreferrer" title="https://openresty.org/cn/download.html)%E4%B8%8B%E8%BD%BD%E6%9C%80%E6%96%B0%E7%9A%84%E6%BA%90%E7%A0%81%E5%8C%85%EF%BC%8C%E5%B9%B6%E8%A7%A3%E5%8E%8B%EF%BC%8C%E7%BC%96%E8%AF%91%E5%92%8C%E5%AE%89%E8%A3%85%EF%BC%8C%E5%91%BD%E4%BB%A4%E5%A6%82%E4%B8%8B%EF%BC%9A" ref="nofollow noopener noreferrer">openresty.org/cn/download…</a></li>
</ol>
<pre><code class="copyable">wget https://openresty.org/download/openresty-1.13.6.1.tar.gztar -xvf openresty-1.13.6.1.tar.gz
cd openresty-1.13.6.1
./configure -j2
make -j2
sudo make install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认情况下程序会被安装到"/usr/local/openresty"目录下，也可以使用"./configuure --help"查看更多的配置选项</p>
<ol start="3">
<li>安装成功后，在开始使用OpenResty前，新建Nginx配置文件<code>confgi/nginx.conf</code>, 代码如下：</li>
</ol>
<pre><code class="copyable">worker_processes 1;
error_log logs/error.log;
events &#123;
    worker_connections 1024
&#125;
http &#123;
    server &#123;
        listen 9000;
        location / &#123;
            default_type text/html;
            content_by_lua '
                ngx.say("<p>Hello, World!<p>")
                ';
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>tips: 关于lua语言的介绍和使用，请参考lua官方文档：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.lua.org%2Fdocs.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.lua.org/docs.html" ref="nofollow noopener noreferrer">www.lua.org/docs.html</a></p>
</blockquote>
<ol start="4">
<li>启动OpenResty服务，命令如下：</li>
</ol>
<pre><code class="copyable">/usr/local/openresty/nginx/sbin/nginx -p `pwd`/ -c conf/nginx.conf
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没有任何输出，说明启动成功，其中参数-p指定项目目录：参数-c指定配置文件</p>
<ol start="5">
<li>使用cURL来访问该服务，命令如下：</li>
</ol>
<pre><code class="copyable">curl http://localhost:8080/
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>输出结果如下：</li>
</ol>
<pre><code class="copyable"><p>Hello, World!<p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单来说，OpenResty是基于Nginx的扩展，并且开发语言不在是Nginx的C语言实现，而是更简单，易用的lua语言</p>
<h2 data-id="heading-0">最后</h2>
<blockquote>
<p>公众号：小何成长，佛系更文，都是自己曾经踩过的坑或者是学到的东西</p>
<p>有兴趣的小伙伴欢迎关注我哦，我是：<code>何小玍</code>。大家一起进步鸭</p>
</blockquote></div>  
</div>
            