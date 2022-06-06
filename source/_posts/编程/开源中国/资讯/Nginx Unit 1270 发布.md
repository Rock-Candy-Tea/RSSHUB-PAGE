
---
title: 'Nginx Unit 1.27.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9233'
author: 开源中国
comments: false
date: Mon, 06 Jun 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9233'
---

<div>   
<div class="content">
                                                                                            <p>Nginx Unit 是一个动态应用服务器，能够与 Nginx Plus 和 Nginx 开源版并行或独立运行。Nginx Unit 支持 RESTful JSON API，可以在不中断服务的情况下更改配置，并可运行基于多种语言和架构的应用。Nginx Unit 生来就是为满足分布式应用的需求而设计的，可为您的服务网格奠定坚实的基础。</p> 
<p>Nginx Unit 1.27.0 正式发布，更新内容如下：</p> 
<h3>将 HTTP 请求重定向到 HTTPS</h3> 
<p>自从在 Unit 中加入了 TLS 支持和证书管理，就被要求简化将纯文本 HTTP 请求重定向到启用 TLS 的监听器。现在可以通过配置路由 action 的 <code>location</code> 值来实现这一功能。事实上，现在有一个新的变量， <code>$request_uri</code>，它包含了原始 URI 的路径和查询部分，完整的例子如下：</p> 
<pre><code class="language-json">&#123;
    "listeners": &#123;
        "*:443": &#123;
            "tls": &#123;
                "certificate": "example.com"
            &#125;,
            "pass": "routes"
        &#125;,
        "*:80": &#123;
            "pass": "routes"
        &#125;
     &#125;,

    "routes": [
        &#123;
            "match": &#123;
                "scheme": "http"
            &#125;,
            "action": &#123;
                "return": 301,
                "location": "<https://$>&#123;host&#125;$&#123;request_uri&#125;"
            &#125;
        &#125;
&#125;

</code></pre> 
<p>这种配置使 Unit 能够监听纯文本和启用 TLS 的端口，确保在纯文本端口收到的任何请求都会通知浏览器在启用 TLS 的端口重新提交。</p> 
<h3>为纯路径 URI 提供可配置的文件名</h3> 
<p>现在你可以通过为路由 action 指定索引来使用不同的默认文件名。下面提供了一个完整的例子：</p> 
<pre><code class="language-json">"routes": [
    &#123;
        "match": &#123;
            "uri": "/cms/*"
        &#125;,
        "action": &#123;
            "share": "/var/cms$uri",
            "index": "default.html"
        &#125;
    &#125;,
    &#123;
        "action": &#123;
            "share": "/var/www$uri"
        &#125;
    &#125;
]

</code></pre> 
<p>这个配置使 Unit 能够为指向 <code>/cms/*</code> 的纯路径 URI 提供 <code>default.html</code>，为所有其他纯路径的 URI 提供默认的 <code>index.html</code> 文件名。</p> 
<h3>其他</h3> 
<ul> 
 <li>与 GCC 12 兼容</li> 
 <li>错误修正：一些 Spring Boot 应用程序无法启动</li> 
 <li>错误修正：Python 协议的自动检测不正确</li> 
 <li>错误修正：ECMAScript 模块不能与最近的 Node.js 版本一起使用</li> 
</ul> 
<h3>平台更新</h3> 
<p>官方软件包现在可用于以下 Linux 发行版：</p> 
<ul> 
 <li>Fedora 36</li> 
 <li>RHEL 9</li> 
 <li>Ubuntu 22.04</li> 
</ul> 
<p>Docker 镜像已经更新，以使用最新的语言版本：</p> 
<ul> 
 <li>Go 1.18</li> 
 <li>PHP 8.1</li> 
 <li>Ruby 3.1</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Funit.nginx.org%2Fnews%2F2022%2Funit-1.27.0-released%2F" target="_blank">https://unit.nginx.org/news/2022/unit-1.27.0-released/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            