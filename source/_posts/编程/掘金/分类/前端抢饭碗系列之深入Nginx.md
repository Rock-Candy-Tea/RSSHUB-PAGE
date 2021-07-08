
---
title: '前端抢饭碗系列之深入Nginx'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/807dd346088b433b9db443a8a3196cc2~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 16:12:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/807dd346088b433b9db443a8a3196cc2~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>　　在大部分童鞋的印象里，Nginx应该都是属于后台工作的范畴，前端只要写好页面就好了；然后随着大前端范围的不断扩展，前端也在不断的进军服务器领域，而Nginx就是进军服务器领域必备的技能之一；以前我们都需要“低声下气”的让后端的同事给我们配置页面域名，但是学会了Nginx配置，域名配置、代理转发什么的完全就可以我们自己来了，这样抢来的饭碗它。。。。它难道不香吗？</p>
<blockquote>
<p>本文首发于公众号<code>【前端壹读】</code>，更多精彩内容敬请关注公众号最新消息。</p>
</blockquote>
<h1 data-id="heading-0">简介</h1>
<p>　　那么Nginx到底是什么，首先我们来看一下百度百科对Nginx的定义：</p>
<blockquote>
<p>Nginx是一个高性能的HTTP和反向代理web服务器，同时也提供了IMAP/POP3/SMTP服务。</p>
</blockquote>
<p>　　这里有三个词很关键，我们来拆解一下，分别是是高性能、反向代理和web服务器；首先这个web服务器自不用多说，像我们熟知的Apache、IIS、Tomcat等都是web服务器；然后是高性能，一个服务器的性能自然是网站开发者最为关心的，那么服务器的性能如何来进行衡量呢？一般可以通过CPU和内存的使用量来进行衡量。经过笔者简单的并发测试，在20000个并发链接时，CPU和内存占用也非常低，CPU仅占5%，内存占用也才2MB不到。</p>
<p>　　我们可以通过一个web压力测试工具<code>Apache Bench</code>，对Nginx进行简单的压力测试；通过在命令行<code>ab -n 20000 -c 10000 [url]</code>，我们对Nginx的首页发起请求总数为20000，并发数为10000的请求测试，测试结果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/807dd346088b433b9db443a8a3196cc2~tplv-k3u1fbpfcp-zoom-1.image" alt="压力测试结果" loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　我们看到总的请求时间（Time taken for tests）是25秒，平均每个请求耗时（Time per request）1.25毫秒，在这么高的并发量下面，服务器响应性能还是挺不错的。</p>
<p>　　然后是反向代理，与之对应的就是正向代理，这两者的区别也是面试中经常被问到的。我们先来看一下什么是正向代理，一个正向代理最典型的例子就是我们常用的“梯子”。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de862381eb184789b2924c419a2750ed~tplv-k3u1fbpfcp-zoom-1.image" alt="表情包" loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　我们直接访问Google，是访问不到的，但是如果我们使用了代理服务器，那么通过访问代理服务器就可以浏览Google，这里的代理服务器就属于<code>正向代理</code>；通过正向代理我们可以访问原来无法访问的资源。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a70f52c23a534e82a1ee7d88c6107ef2~tplv-k3u1fbpfcp-zoom-1.image" alt="正向代理" loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　那么什么是反向代理呢？反向代理最典型的例子就是我们的Nginx服务器了；比如我们在访问某个网站时，由代理服务器去目标服务器获取数据后返回给客户端，这样就能够隐藏真实服务器的IP地址，只对外开放代理服务器，以防止外网对内网服务器的恶性攻击。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dfa0c646fd343c190e87481d5f5fbea~tplv-k3u1fbpfcp-zoom-1.image" alt="反向代理" loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　理解了上面两个典型的案例，相信大家对正向反向代理也了解了，我们总结一下：</p>
<ul>
<li>正向代理，<strong>代理客户端</strong>，服务端不知道实际发起请求的客户端。</li>
<li>反向代理，<strong>代理服务端</strong>，客户端不知道实际提供服务的服务端。</li>
</ul>
<h1 data-id="heading-1">安装配置</h1>
<p>　　Nginx安装程序分为Linux版和Windows版，Windows版本的Nginx下载解压后就可以直接运行了，而Linux版本的需要make、configure等命令编译安装，好处是可以方便灵活的编译不同的模块到Nginx；网上也有很多的安装教程，这里就不再赘述了，可以从<a href="https://link.juejin.cn/?target=http%3A%2F%2Fnginx.org%2Fen%2Fdownload.html" target="_blank" rel="nofollow noopener noreferrer" title="http://nginx.org/en/download.html" ref="nofollow noopener noreferrer">官网</a>下载适合自己的版本，下载好后我们来看一下他的目录结构：</p>
<pre><code class="hljs language-bash copyable" lang="bash">├── conf            <span class="hljs-comment">#所有配置文件的目录</span>
    ├── nginx.conf  <span class="hljs-comment">#主配置文件</span>
    ├── mime.types  <span class="hljs-comment">#媒体类型控制文件</span>
├── contrib         <span class="hljs-comment">#存放一些实用工具</span>
├── docs            <span class="hljs-comment">#文档资料</span>
├── html            <span class="hljs-comment">#默认解析的静态文件目录</span>
├── logs            <span class="hljs-comment">#日志目录</span>
├── sbin            <span class="hljs-comment">#启动运行程序</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们经常用到的就是conf目录和html目录；而在根目录可以运行常用的一些命令对Nginx进行操作控制：</p>
<pre><code class="hljs language-bash copyable" lang="bash">nginx -s reopen <span class="hljs-comment">#重启Nginx</span>
nginx -s reload <span class="hljs-comment">#重新加载Nginx配置文件，然后以优雅的方式重启Nginx</span>
nginx -s stop   <span class="hljs-comment">#强制停止Nginx服务</span>
nginx -s quit   <span class="hljs-comment">#优雅地停止Nginx服务（即处理完所有请求后再停止服务）</span>
nginx -h     <span class="hljs-comment">#打开帮助信息</span>
nginx -v     <span class="hljs-comment">#显示版本信息并退出</span>
nginx -V    <span class="hljs-comment">#显示版本和配置选项信息，然后退出</span>
nginx -t    <span class="hljs-comment">#检测配置文件是否有语法错误，然后退出</span>
nginx -T     <span class="hljs-comment">#检测配置文件是否有语法错误，转储并退出</span>
nginx -q       <span class="hljs-comment">#在检测配置文件期间屏蔽非错误信息</span>
nginx -p prefix   <span class="hljs-comment">#设置前缀路径(默认是:/usr/share/nginx/)</span>
nginx -c filename<span class="hljs-comment">#设置配置文件(默认是:/etc/nginx/nginx.conf)</span>
nginx -g directives <span class="hljs-comment">#设置配置文件外的全局指令</span>
killall nginx<span class="hljs-comment">#杀死所有nginx进程</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们看前四个命令会发现，这四个命令可以分为两种，重启和停止Nginx，不过一种是强制的方式，另一种是优雅的方式；强制的方式就是让Nginx立即停止当前处理的所有请求，丢弃链接，停止工作；而优雅的方式是允许Nginx将当前正在处理的请求处理完成，但是不再接收新的请求，所有处理完成后再停止工作。</p>
<p>　　我们再来看一下主要配置文件nginx.conf的基本结构：</p>
<pre><code class="hljs language-conf copyable" lang="conf"># nginx进程数，建议设置为等于CPU总核心数
worker_processes  1;
# 进程文件
pid        logs/nginx.pid;
# 单个进程最大连接数
events &#123;
    worker_connections  1024;
&#125;
http &#123;
    # 文件扩展名与类型映射表
    include       mime.types;
    # 默认文件类型
    default_type  application/octet-stream;
    # 开启gzip压缩
    gzip  on;
    sendfile        on;
    keepalive_timeout  65;
    server &#123;
        # 监听端口
        listen       80;
        server_name  localhost;
        location / &#123;
            root   html;
            index  index.html index.htm;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　配置文件中主要可以分为以下几个块：</p>
<ul>
<li>全局模块：从配置文件开始到events块之间的内容，此处的配置影响nginx服务器整体的运⾏，⽐如worker进程的数量、错误⽇志的位置等</li>
<li>events：配置影响nginx服务器或与用户的网络连接。</li>
<li>http：<strong>可以嵌套多个server</strong>，配置代理，缓存，日志定义等绝大多数功能和第三方模块的配置。</li>
<li>server：配置虚拟主机的相关参数，一个http中可以有多个server。</li>
<li>location：配置请求的路由，以及各种页面的处理情况。</li>
</ul>
<p>　　很多时候，我们不会将所有的配置全都写在一个主配置文件，因为这样会显得冗长，也不知道每个模块是做什么用的；而是会根据项目来拆分多个配置文件，每个配置文件彼此独立，互不干扰，然后在主配置文件中引入；我们在conf目录下新建一个projects目录，然后可以新建多个.conf配置文件：</p>
<pre><code class="hljs language-conf copyable" lang="conf"># /conf/projects/home.conf
server &#123;
    listen       8080;
    server_name  localhost;
    location / &#123;
        root   html;
        index  index.html index.htm;
    &#125;
&#125;
server &#123;
    listen       8081;
    server_name  localhost;
    location / &#123;
        root   html;
        index  index.html index.htm;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　然后在主配置nginx.conf中将projects目录下的所有配置文件引入：</p>
<pre><code class="hljs language-conf copyable" lang="conf">http &#123;
    include       mime.types;
    default_type  application/octet-stream;
    gzip  on;
    sendfile        on;
    keepalive_timeout  65;
    ## 引入projects目录下所有的配置文件
    include       projects/*.conf;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这样我们可以直接在projects目录下新增.conf后缀的配置文件，而不用修改主配置文件；但是我们修改完还不能确定是否会有错误，可以通过命令对配置文件进行检测：</p>
<pre><code class="hljs language-bash copyable" lang="bash">nginx -t
<span class="hljs-comment">#nginx: the configuration file nginx/conf/nginx.conf syntax is ok</span>
<span class="hljs-comment">#nginx: configuration file nginx/conf/nginx.conf test is successful</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　通过检测发现没有任何报错，就可以优雅的重启服务器了：</p>
<pre><code class="hljs language-bash copyable" lang="bash">nginx -s reload
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">静态服务器</h1>
<p>　　作为一个web服务器，最重要的就是能够对静态资源提供访问服务，我们的Nginx服务器可以用来托管一些静态的资源，比如js、css、图片等，访问某一特定的静态资源路径时会转发到本地目录文件上；那么我们就来看Nginx是如何一步一步的通过域名配置、URI配置以及目录配置来命中请求的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/697ac5223df94493ad8d6bbd041299b1~tplv-k3u1fbpfcp-zoom-1.image" alt="Nginx首页" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">server_name配置</h2>
<p>　　在上面的配置中，我们主要是将<code>server_name</code>设置为<code>localhost</code>，但是这样仅能让局域网内的主机访问到；我们想要让广域网上的其他主机访问，可以将<code>server_name</code>匹配域名，它的参数值可以是以下几种：</p>
<ul>
<li>精确的域名，如www.my.com</li>
<li>通配符名称，但通配符只能用在由三段字符串组成的名称的首段或尾段，如<code>*.my.com或者www.my.*</code></li>
<li>正则表达式，使用波浪号<code>~</code>作为正则表达式字符串的开始标记，如<code>~^www\d+\.my\.com$</code></li>
<li>ip地址</li>
</ul>
<p>　　在上面正则表达式中，<code>^</code>表示以www开头，紧跟一个或多个数字（\d+），然后跟上域名my.com，最后以<code>$</code>结尾；因此上面的表达式可以匹配的域名比如www1.my.com，但是www.my.com就不行。</p>
<p>　　正则表达式还支持字符串捕获功能，即将正则表达式匹配成功的名称中的一部分字符串截取出来，放在变量中供后面使用；比如将server_name进行如下设置：</p>
<pre><code class="hljs language-conf copyable" lang="conf">server &#123;
  listen       80;
  server_name  ~^(.+)?\.my\.com$;
  location / &#123;
    root   /usr/share/nginx/html/$1;
    index  index.html index.htm;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这样，通过二级域名home.my.com到达Nginx时，被<code>server_name</code>正则表达式捕获，将其中的<code>home</code>字符串存入<code>$1</code>变量中，我们在<code>/usr/share/nginx/html/home</code>目录下的静态资源就能通过home.my.com域名来访问了；我们服务器的目录就可以是这样的：</p>
<pre><code class="hljs language-file copyable" lang="file">/usr/share/nginx/html/
    |- home
        |- index.html
    |- blog
        |- index.html
    |- mail
        |- index.html
    |- photo
        |- index.html
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这样就只需要一个server块来完成多个站点的配置。</p>
<p>　　nginx允许一个虚拟主机有多个域名，因此我们可以给server_name同时配置多个域名，多个之间以空格分隔：</p>
<pre><code class="hljs language-conf copyable" lang="conf">server &#123;
  listen       80;
  server_name  a.com b.com c.com;
  # ...其他配置
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　由于server_name支持以上三种配置方式，如果出现多个server块同时匹配了相同的域名，那么这个请求交给哪个server呢？因此优先级顺序如下：</p>
<ol>
<li>精确匹配server_name</li>
<li>通配符在开始时匹配server_name</li>
<li>通配符在结尾时匹配server_name</li>
<li>正则表达式匹配server_name</li>
</ol>
<p>　　如果我们想让局域网内的设备访问nginx，可以将<code>server_name</code>设置ip地址的方式：</p>
<pre><code class="hljs language-conf copyable" lang="conf">server &#123;
  listen       80;
  server_name  localhost 192.168.1.101;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　如果还不能访问，可以查看下是否是防火墙的原因，在防火墙允许通过的应用中将Nginx勾选（没有找到Nginx可以点击<code>允许其他应用</code>进行新增）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f19e92ce712649968e668752554db5c4~tplv-k3u1fbpfcp-zoom-1.image" alt="Windows防火墙" loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　有时候我们还会见到将server_name设置为<code>_</code>（下划线），意味着server_name为空，即匹配全部的主机；我们可以配置host，将a.com、b.com和c.com都指向本机，然后配置nginx：</p>
<pre><code class="hljs language-conf copyable" lang="conf">server &#123;
  listen       80;
  server_name  _;
  location / &#123;
    root   html;
    index  index.html index.htm;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这样我们不仅可以通过域名a.com、b.com、c.com来访问，也能通过ip的方式。</p>
<h2 data-id="heading-4">location配置</h2>
<p>　　location用于匹配不同的URI请求，它的语法如下：</p>
<pre><code class="hljs language-conf copyable" lang="conf">location [ = | ~ | ~* | ^~ ] uri &#123; ... &#125;
location @/name/ &#123; … &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这里的<code>uri</code>就是待匹配的请求字符串，可以是不含正则的字符串，比如<code>/home</code>，称为<code>标准URI</code>；也可以是包含正则的字符串，比如<code>\.html$</code>（表示以.html结尾），称为<code>正则URI</code>。而方括号中的四种匹配符都是可选的，用来改变请求字符串与URI的匹配方式，我们来看下四种匹配符的解释：</p>

































<table><thead><tr><th>匹配符</th><th>解释</th></tr></thead><tbody><tr><td>不填</td><td>location后没有参数，直接跟着标准URI，表示前缀匹配，代表跟请求中的URI从头开始匹配</td></tr><tr><td>=</td><td>用于标准URI前，要求请求字符串与其精准匹配，成功则立即处理，nginx停止搜索其他匹配</td></tr><tr><td>^~</td><td>用于标准URI前，要求一旦匹配就会立即处理，不再去匹配其他正则URI，一般用来匹配目录</td></tr><tr><td>~</td><td>用于正则URI前，表示URI包含正则表达式，<code>区分大小写</code></td></tr><tr><td>~*</td><td>用于正则URI前，表示URI包含正则表达式，<code>不区分大小写</code></td></tr><tr><td>@</td><td>定义一个命名的location，@定义的location名字一般用在内部定向</td></tr></tbody></table>
<p>　　我们来看下每种匹配规则能匹配的url，首先不填代表的话表示前缀匹配，如果我们有多个相似的前缀匹配：</p>
<pre><code class="hljs language-conf copyable" lang="conf">location /pre/fix &#123;
  # ...
&#125;
location /pre &#123;
  # ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　对于请求<code>/pre/fix/home</code>，根据最大匹配原则，匹配第一个location。</p>
<p>　　然后是<code>=</code>，要求路径完全匹配：</p>
<pre><code class="hljs language-conf copyable" lang="conf">location = /abc &#123;
  # ...
&#125;

# /abc    匹配
# /abcde  不匹配
# /abc/   不匹配，带有结尾的/
# /cde/abc不匹配
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　其次是<code>^~</code>最佳匹配，它的优先级高于正则表达式：</p>
<pre><code class="hljs language-conf copyable" lang="conf">location ^~ /login &#123;
  # ...
&#125;

# /login      匹配
# /loginss    匹配
# /login/     匹配
# /home/login 不匹配
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　接着是<code>~</code>正则表达式匹配，它区分大小写匹配（注意：windows版本nginx不区分）：</p>
<pre><code class="hljs language-conf copyable" lang="conf">location ~ \.(gif|jpg|png|js|css)$ &#123;
  # ...
&#125;
# /bg.png     匹配
# /bg.PNG     不匹配 
# /bg.png?a=1 匹配
# /bg.jpeg    不匹配
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　<code>~*</code>同样也是正则匹配，只不过它不区分大小写，这里就不再演示。</p>
<p>　　如果我们的URI匹配到了多个location，其并不完全按照在配置文件中出现的顺序来进行匹配，URI会按照如下规则进行匹配：</p>
<ol>
<li>= 精确匹配会第一个被处理。如果发现精确匹配，nginx停止搜索其他匹配。</li>
<li>普通字符匹配，正则表达式规则和长的块规则将被优先和查询匹配，也就是说如果该项匹配还需去看有没有正则表达式匹配和更长的匹配。</li>
<li>^~ 则只匹配该规则，nginx停止搜索其他匹配，否则nginx会继续处理其他location指令。</li>
<li>最后匹配理带有<code>~</code>和<code>~*</code>的指令，如果找到相应的匹配，则nginx停止搜索其他匹配；当没有正则表达式或者没有正则表达式被匹配的情况下，那么匹配程度最高的逐字匹配指令会被使用。</li>
</ol>
<h2 data-id="heading-5">请求目录配置</h2>
<p>　　在location匹配URI后，就需要在服务器指定的目录中寻找请求资源，而<code>root</code>和<code>alias</code>就是用来指定目录的两种指令，两者主要的区别在于如何解析location后面的路径；我们首先来看下root的用法，假如我们需要将<code>/data/</code>下面的所有路径转发到<code>html/roottest</code>下面：</p>
<pre><code class="hljs language-conf copyable" lang="conf">location /data/ &#123;
  root html/roottest;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　当location接收到<code>/data/index.html</code>的请求时，会在<code>html/roottest/data/</code>目录下找到index.html文件并进行相应，root会将root路径和location路径进行拼接。</p>
<p>　　而alias指令则改变location接收到的请求路径，假如我们需要将<code>/data1/</code>下面的所有路径转发到<code>html/aliastest</code>下面：</p>
<pre><code class="hljs language-conf copyable" lang="conf">location /data1/ &#123;
  alias html/aliastes/;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　当location接收到<code>/data1/index.html</code>的请求时，会在<code>html/aliastes/</code>目录下查找index.html文件并响应。</p>
<blockquote>
<p>需要注意的是：alias指令后面的路径<code>必须以/结束</code>，否则会找不到文件，而root则可有可无。</p>
</blockquote>
<h2 data-id="heading-6">访问权限控制</h2>
<p>　　针对一些静态资源，我们可能会设置一些用户访问权限，比如和js一起打包产出的<code>.map</code>文件，会对源码进行映射；但是我们想让它只能针对公司的ip进行开放，对外网的ip禁止访问，这时就需要用到<code>allow</code>和<code>deny</code>命令了。</p>
<p>　　假如局域网还有两个设备，我们只能让这两个设备的ip通过访问：</p>
<pre><code class="hljs language-conf copyable" lang="conf">location / &#123;
  alias html/aliastes/;
  allow 192.168.1.102;
  allow 192.168.1.103;
  deny all;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　deny和allow指令是由ngx_http_access_module模块提供，Windows版本的Nginx并不包含该模块。</p>
<p>　　还可以对前端的.map文件进行访问权限控制，打包后的map文件一般会放在服务器上，但是如果能对所有人开放，别人就能查看到对应源码；因此我们可以控制只有公司的ip才有访问权限：</p>
<h2 data-id="heading-7">try_files</h2>
<p>　　前端在配置路由时经常会用到history路由模式，因此后台就需要映射对应的路由到index.html；但是如果我们给每个路由都配置一个location就会比较繁琐，因此可以通过<code>try_files</code>指令来进行尝试解析；<code>try_files</code>的语法规则如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 格式1：</span>
try_files file ... uri;  
<span class="hljs-comment"># 格式2：</span>
try_files file ... =code;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　假设我们打包出来的单页面位于<code>/html/my/index.html</code>，我们想要将/login、/regisrer等路由指向index.html，我们可以配置try_files：</p>
<pre><code class="hljs language-conf copyable" lang="conf">server &#123;
    listen       8080;
    server_name  localhost;
    location / &#123;
        try_files $uri /my/index.html;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　对于多页面的应用，假设我们的页面都放在<code>/html/pages/</code>目录下，我们想要访问<code>/login</code>时响应<code>/html/pages/login.html</code>页面，可以通过<code>$uri</code>：</p>
<pre><code class="hljs language-conf copyable" lang="conf">server &#123;
    listen       8080;
    server_name  localhost;
    location / &#123;
        index  index.html index.htm;
        root html/pages;
        try_files $uri /$uri.html $uri/index.html /index.html;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这里我们设置root目录为html/pages，当我们访问<code>/login</code>路由时，这里的$uri就是/login，try_files会去尝试在根目录下找<code>/login.html</code>；如果找不到就尝试<code>/login/index.html</code>，最后找不到则会默认返回index.html。</p>
<h2 data-id="heading-8">gzip</h2>
<p>　　我们都知道在服务端开启gzip压缩能够使得js、css、html等文件在传输时大幅提高访问速度，优化网站性能；gzip压缩后的文件大小可以变为原来的30%甚至更小；而对于图片、视频、音频等其他多媒体文件，因为压缩效果不好，所以不会开启压缩。</p>
<p>　　gzip压缩本质上是服务器端压缩，传输到浏览器后解压解析，我们来看下gzip的原理示意：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcb7bc3f21a54a04ae74e610239ebbc1~tplv-k3u1fbpfcp-zoom-1.image" alt="Gzip原理" loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　可以看到在请求和相应头上分别加了accept-encoding和content-encoding来进行传输；我们可以通过一个js的请求数据来查看：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/580052fa553445cba1c0cd60dc23ab51~tplv-k3u1fbpfcp-zoom-1.image" alt="Gzip请求响应头" loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　既然gzip有这么多的好处，我们来看下nginx如何进行配置，gzip的配置可以在http块或者server块中：</p>
<pre><code class="hljs language-conf copyable" lang="conf"># 开启gzip
gzip        on;
# 设置gzip申请内存的大小
gzip_buffers 32 4K;
# 设置gzip压缩等级
# 压缩级别 1-9，级别越高压缩率越大但耗CPU
gzip_comp_level 6;
# 正则匹配User-Agent中的值，匹配上则不进行gzip
gzip_disable "MSIE [1-6]\.(?!.*SV1)";
# 设置允许压缩的页面最小字节数
gzip_min_length 1024;
# 设定进行gzip压缩的最小http版本
gzip_http_version 1.0;
# 需要压缩哪些响应类型的资源
gzip_types application/javascript text/css text/xml;
# 添加“Vary: Accept-Encoding”响应头
gzip_vary on;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">密码控制</h2>
<p>　　对于一些简单的页面，我们想要通过密码来限制其他用户的访问，但是又不想接入复杂的账号体系，Nginx提供了简单的账号密码控制；首先我们通过Linux的工具创建一个密码本存放账号密码：</p>
<pre><code class="hljs language-bash copyable" lang="bash">sudo yum install httpd-tools -y
sudo htpasswd -c passwd/passwd admin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　<code>passwd/passwd</code>文件就是生成的密码文件，运行后会要求连续两次输入密码，成功后为admin用户添加了密码；然后我们就修改nginx的配置文件，对站点开启密码验证：</p>
<pre><code class="hljs language-conf copyable" lang="conf">server &#123;
  listen 8000;
server_name localhost;
auth_basic "请输入账号密码";
auth_basic_user_file /etc/nginx/conf/passwd/passwd;
location / &#123;
    # .....
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　重启nginx，再次访问站点就会出现需要身份验证的弹框了。</p>
<h1 data-id="heading-10">反向代理</h1>
<p>　　上面我们介绍了正向代理和反向代理的区别，反向代理功能是nginx的三大主要功能之一（静态web服务器、反向代理、负载均衡）。反向代理不需要额外的模块，默认自带proxy_pass和fastcgi_pass指令，通过在location块中配置即可实现：</p>
<pre><code class="hljs language-conf copyable" lang="conf">server &#123;
  listen 80;
  server_name a.com;
  location / &#123;
    proxy_pass http://192.168.1.102:8080;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　在配置proxy_pass时，我们需要注意url后面的<code>/`；当我们通过下面几种情况访问</code>/proxy/home.html``时：</p>
<pre><code class="hljs language-conf copyable" lang="conf">location /proxy/ &#123;
  proxy_pass http://192.168.1.102:8080/;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　第一种情况url后面带上/，则会被代理到<code>http://192.168.1.102:8080/home.html</code>。</p>
<pre><code class="hljs language-conf copyable" lang="conf">location /proxy/ &#123;
  proxy_pass http://192.168.1.102:8080;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　第二种情况url后不带/，则会被代理到<code>http://192.168.1.102:8080/proxy/home.html</code></p>
<pre><code class="hljs language-conf copyable" lang="conf">location /proxy/ &#123;
  proxy_pass http://192.168.1.102:8080/doc/;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　第三种情况代理/doc/，则会被代理到<code>http://192.168.1.102:8080/doc/home.html</code></p>
<pre><code class="hljs language-conf copyable" lang="conf">location /proxy/ &#123;
  proxy_pass http://192.168.1.102:8080/doc;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　第四种情况代理/doc，则会被代理到<code>http://192.168.1.102:8080/dochome.html</code></p>
<p>　　在配置反向代理时，我们还可以修改代理请求的请求参数：</p>
<pre><code class="hljs language-conf copyable" lang="conf">location /proxy/ &#123;
  proxy_pass http://192.168.1.102:8080/;
  # 修改请求的method
  proxy_method GET;
  # 修改请求的http协议版本
  proxy_http_version 1.1;
  # 将原来host字段放到转发请求中
  proxy_set_header Host $host;
  #获取真实ip
  proxy_set_header X-Real-IP $remote_addr;
  # 代理服务器每成功收到一个请求，就把请求来源IP地址添加到右边
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  proxy_redirect  off;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　经过反向代理后，由于客户端和web服务器之间增加了一个代理层，因此web服务器无法拿到客户端请求的host和真实ip，我们通过proxy_set_header指令修改代理请求的头部；<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>h</mi><mi>o</mi><mi>s</mi><mi>t</mi><mtext>和</mtext></mrow><annotation encoding="application/x-tex">host和</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">h</span><span class="mord mathnormal">o</span><span class="mord mathnormal">s</span><span class="mord mathnormal">t</span><span class="mord cjk_fallback">和</span></span></span></span></span>remote_addr是用户真实的host和ip，这里作为变量传入Host和X-Real-IP字段，因此我们在客户端服务器想要获取真实ip就可以通过request.getAttribute("X-real-ip")的方式。</p>
<h1 data-id="heading-11">负载均衡</h1>
<p>　　随着互联网的发展，用户规模的增加，服务器的压力也越来越大，如果只使用一台服务器有时候不能承受流量的压力，这时我们就需要将部分流量分散到多台服务器上，使得每台服务器都均衡的承担压力。</p>
<p>　　nginx负载均衡目前支持六种策略：轮询策略、加权轮询策略、ip_hash策略、url_hash策略、fair策略和sticky策略；六种策略可以分为两大类，内置策略（轮询、加权轮询、ip_hash）和扩展策略（url_hash、fair、sticky）；默认情况下内置策略自动编译在Nginx中，而扩展策略需要额外安装。</p>
<p>　　既然是负载，那么我们需要启用多台服务器；这里为了方便演示，我们在一台电脑上运行node脚本来模拟3台服务器；同时为了方便看到每台服务器有多少流量，每访问一次就计数一次：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">"express"</span>);
<span class="hljs-keyword">const</span> app = express();
<span class="hljs-keyword">const</span> PORT = <span class="hljs-number">8080</span>;
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);
<span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
app.get(<span class="hljs-string">"*"</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  count++;
  res.sendFile(path.resolve(__dirname, <span class="hljs-string">"./index.html"</span>));
&#125;);
app.listen(PORT);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　然后我们修改端口号，这样我们就有8080、8081、8082三个服务器了。</p>
<h2 data-id="heading-12">轮询策略</h2>
<p>　　轮询策略，顾名思义，就是按照请求顺序，逐一分配到不同的服务器节点；如果某台服务器出现问题，会自动剔除。</p>
<pre><code class="hljs language-conf copyable" lang="conf">upstream myserver &#123;
    server 192.168.1.101:8080;
    server 192.168.1.101:8081;
    server 192.168.1.101:8082;
&#125;
server &#123;
    listen      8070;
    server_name _;
    location / &#123;
        proxy_pass http://myserver;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们还是通过测试工具<code>Apache Bench</code>来并发100个请求到Nginx：</p>
<pre><code class="hljs language-bash copyable" lang="bash">ab -n 100 -c 10 http://localhost:8070/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　最后统计每台服务器的结果，每台服务器的请求还是很平均的：</p>
<pre><code class="hljs language-text copyable" lang="text">8080：34个请求
8081：33个请求
8082：33个请求
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">加权轮询策略</h2>
<p>　　加权轮询在基本轮询策略上考虑各服务器节点接受请求的权重，指定服务器节点被轮询的权重，主要用于服务器节点性能不均的情况。</p>
<p>　　通过在server节点后配置weight来设置权重，weight的大小和访问比率成正比（weight的默认值为1）；我们给三台服务器设置访问比是<code>1:3:2</code>。</p>
<pre><code class="hljs language-conf copyable" lang="conf">upstream myserver &#123;
    server 192.168.1.101:8080;
    server 192.168.1.101:8081 weight=3;
    server 192.168.1.101:8082 weight=2;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　压力测试后统计服务器的请求结果，和我们配置的比率还是几乎相同的：</p>
<pre><code class="copyable">8080：16个请求
8081：51个请求
8082：33个请求
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注：由于weight是内置，所以可以直接和其他策略配合使用。</p>
</blockquote>
<h2 data-id="heading-14">ip_hash策略</h2>
<p>　　ip_hash策略是将前端访问的ip进行hash操作后，然后根据hash的结果将请求分配到不同的节点上，这样使得每个ip都会固定访问服务节点；这样做的好处是用户的session只在一个后端服务器节点上，不必考虑一个session存在多台服务器节点出现session共享问题。</p>
<pre><code class="hljs language-conf copyable" lang="conf">upstream myserver &#123;
    ip_hash;
    server 192.168.1.101:8080;
    server 192.168.1.101:8081 weight=3;
    server 192.168.1.101:8082 weight=2;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　压力测试后统计服务器的请求结果，我们发现所有的请求都到固定一台服务器上了：</p>
<pre><code class="copyable">8080：0个请求
8081：0个请求
8082：100个请求
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">url_hash策略</h2>
<p>　　url_hash策略是将url地址进行hash操作，根据hash结果请求定向到同一服务器节点上；url_hash的优点是能够提高后端缓存服务器的效率。</p>
<pre><code class="hljs language-conf copyable" lang="conf">upstream myserver &#123;
    hash $request_uri;
    server 192.168.1.101:8080;
    server 192.168.1.101:8081;
    server 192.168.1.101:8082;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　压力测试后统计服务器的请求结果：</p>
<pre><code class="copyable">8080：0个请求
8081：0个请求
8082：100个请求
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　如果我们切换不同的url，/home、/list等，都会分配到不同的服务器节点。</p>
<h2 data-id="heading-16">fair策略</h2>
<p>　　fair策略请求转发到负载最小的后端服务器节点上。Nginx通过服务器节点对响应时间来判断负载情况，响应时间最短的节点负载就相对较轻，Nginx就会将前端请求转发到此服务器节点上。</p>
<blockquote>
<p>注：fair策略默认不被编译进nginx内核，需要额外安装</p>
</blockquote>
<pre><code class="hljs language-conf copyable" lang="conf">upstream myserver &#123;
    fair;
    server 192.168.1.101:8080;
    server 192.168.1.101:8081;
    server 192.168.1.101:8082;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　压力测试后统计服务器的请求结果：</p>
<pre><code class="copyable">8080：33个请求
8081：33个请求
8082：34个请求
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">sticky策略</h2>
<p>　　sticky策略是基于cookie的一种负载均衡解决方案，通过分发和识别cookie，使来自同一个客户端的请求落在同一台服务器上，默认cookie标识名为route。</p>
<p>　　sticky策略看起来和ip_hash策略类似，但是又有一定区别。假设在一个局域网内有3台电脑，他们有3个内网IP，但是他们发起请求时，却只有一个外网IP，如果使用ip_hash方式，则Nginx会将请求分配到同一服务器；如果使用sticky策略，则会把请求分配到不同服务器上，这是ip_hash无法做到的。</p>
<blockquote>
<p>注：sticky策略默认不被编译进nginx内核，需要额外安装</p>
</blockquote>
<pre><code class="hljs language-conf copyable" lang="conf">upstream myserver &#123;
    sticky name=sticky_cookie expires=6h;
    server 192.168.1.101:8080;
    server 192.168.1.101:8081;
    server 192.168.1.101:8082;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　sticky默认的cookie的名称是<code>route</code>，我们可以通过name修改，还有一些其他的cookie参数可以进行修改：</p>
<ul>
<li>[name=route]　　　　　　　设置用来记录会话的cookie名称</li>
<li>[domain=.foo.bar]　　　　设置cookie作用的域名</li>
<li>[path=/]　　　　　　　　  设置cookie作用的URL路径，默认根目录</li>
<li>[expires=1h] 　　　　　　 设置cookie的生存期，默认不设置，浏览器关闭即失效</li>
<li>[hash=index|md5|sha1]   设置cookie中服务器的标识是用明文还是使用md5值，默认使用md5</li>
<li>[no_fallback]　　　　　　 设置该项，当sticky的后端机器挂了以后，nginx返回502 (Bad Gateway or Proxy Error) ，而不转发到其他服务器，不建议设置</li>
<li>[secure]　　　　　　　　  设置启用安全的cookie，需要HTTPS支持</li>
<li>[httponly]　　　　　　　  允许cookie不通过JS泄漏，没用过</li>
</ul>
<p>　　我们通过浏览器来访问，在cookie中可以看到sticky下发的cookie</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/715099cbfac040e89a010525afc94357~tplv-k3u1fbpfcp-zoom-1.image" alt="sticky策略cookie" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注：由于cookie最初由服务器端下发，如果客户端禁用cookie，则cookie不会生效。</p>
</blockquote>
<h2 data-id="heading-18">其他参数</h2>
<p>　　upstream还有一些参数我们可以配合负载均衡：</p>

































<table><thead><tr><th>参数</th><th>描述</th></tr></thead><tbody><tr><td>fail_timeout</td><td>与max_fails结合使用</td></tr><tr><td>max_fails</td><td>设置在fail_timeout参数设置的时间内最大失败次数，如果在这个时间内，所有针对该服务器的请求都失败了，那么认为该服务器会被认为是停机了</td></tr><tr><td>fail_time</td><td>服务器会被认为停机的时间长度,默认为10s。</td></tr><tr><td>backup</td><td>标记该服务器为备用服务器。当主服务器停止时，请求会被发送到它这里。</td></tr><tr><td>down</td><td>标记服务器永久停机了。</td></tr><tr><td>keepalive</td><td>连接数（keepalive的值）指定了每个工作进程中保留的持续连接到nginx负载均衡器缓存的最大值。如果超过这个设置值的闲置进程想链接到nginx负载均衡器组，最先连接的将被关闭。</td></tr></tbody></table>
<pre><code class="hljs language-conf copyable" lang="conf">upstream backserver&#123; 
  ip_hash;
  # down 表示单前的server暂时不参与负载 
  server 192.168.1.101:8080 down; 
  server 192.168.1.101:8081;
  # max_fails允许请求失败的次数默认为1，此处允许失败的次数为3。每次失败后暂停的时间为30s
  server 192.168.1.101:8082 max_fails=3 fail_timeout=30s; 
  # 其它所有的非backup机器down或者忙的时候，请求backup机器
  server 192.168.1.101:8083 backup;
  # 连接到nginx负载均衡器的最大
  keepalive 16;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Nginx你学会了吗？更多前端资料请关注公众号<code>【前端壹读】</code>。</p>
<p>如果觉得写得还不错，请关注我的<a href="https://juejin.im/user/580038cebf22ec0064bd0b2d" target="_blank" title="//juejin.im/user/580038cebf22ec0064bd0b2d">掘金主页</a>。更多文章请访问<a href="https://link.juejin.cn/?target=http%3A%2F%2Fxieyufei.com" target="_blank" rel="nofollow noopener noreferrer" title="http://xieyufei.com" ref="nofollow noopener noreferrer">谢小飞的博客</a></p></div>  
</div>
            