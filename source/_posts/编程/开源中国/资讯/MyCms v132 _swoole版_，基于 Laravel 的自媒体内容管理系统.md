
---
title: 'MyCms v1.3.2 _swoole版_，基于 Laravel 的自媒体内容管理系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b30a3cef1b23ff0d16f6c6cb485ff245abe.png'
author: 开源中国
comments: false
date: Fri, 05 Nov 2021 06:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b30a3cef1b23ff0d16f6c6cb485ff245abe.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="600" src="https://oscimg.oschina.net/oscnet/up-b30a3cef1b23ff0d16f6c6cb485ff245abe.png" width="2000" referrerpolicy="no-referrer"></p> 
<p><strong>Swoole简介</strong></p> 
<p>Swoole 是为 PHP 开发的生产级异步编程框架。</p> 
<p>Swoole 使 PHP 开发人员可以编写高性能高并发的 TCP、UDP、Unix Socket、HTTP、 WebSocket 等服务，让 PHP 不再局限于 Web 领域。</p> 
<p><strong><span style="background-color:#ffffff; color:#333333">Laravel简介</span></strong></p> 
<p><span style="background-color:#ffffff; color:#333333">Laravel是当今最熟练，流行和广泛使用的开源框架之一。Laravel具有多种功能，例如模板引擎，MVC架构支持，安全性高，开发者工具，数据库迁移等。这些Laravel高级功能使它比其他PHP框架更好。</span></p> 
<p>但是，Laravel 有个最为人诟病的缺点就是：慢、笨重。</p> 
<p>这就是为什么我们需要尝试在 Swoole 上运行 Laravel。 Swoole 可以提供强大性能而 Laravel 则可以提供优雅代码结构使用。这俩儿真是完美组合！</p> 
<p><span style="background-color:#ffffff; color:#40485b"><strong>MyCms简介</strong></span></p> 
<p><span style="background-color:#ffffff; color:#40485b">MyCms是一款基于Laravel开发的开源免费的自媒体博客CMS系统，适用于个人网站及企业网站开发使用，软件著作权编号：2021SR1543432。</span></p> 
<p><span style="background-color:#ffffff; color:#40485b">MyCms基于Apache2.0开源协议发布，免费且不限制商业使用，欢迎持续关注我们。</span></p> 
<p><strong>MyCms v1.3.2 版本新增对swoole的支持。</strong></p> 
<p><span style="background-color:#ffffff; color:#40485b">使用新版本的用户直接安装后按以下配置即可。</span></p> 
<p><span style="background-color:#ffffff; color:#40485b">使用旧版本的用户则需要先安装<span> </span></span><code>composer require swooletw/laravel-swoole</code><span style="background-color:#ffffff; color:#40485b">。 在<span> </span></span><code>config/app.php</code><span style="background-color:#ffffff; color:#40485b"><span> </span>服务提供者数组添加该服务提供者。</span></p> 
<pre>[
    'providers' => [
        SwooleTW\Http\LaravelServiceProvider::class,
    ],
]</pre> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>Nginx配置</strong></p> 
<pre><span style="color:#808080">map $http_upgrade $connection_upgrade &#123;
</span><span style="color:#808080">    default upgrade;
</span><span style="color:#808080">    ''      close;
</span><span style="color:#808080">&#125;
</span><span style="color:#808080">server &#123;
</span><span style="color:#808080">    listen 80;
</span><span style="color:#808080">    server_name your.domain.com;
</span><span style="color:#808080">    root /path/to/laravel/public;
</span><span style="color:#808080">    index index.php;
</span>
<span style="color:#808080">    location = /index.php &#123;
</span><span style="color:#808080">        # Ensure that there is no such file named "not_exists"
</span><span style="color:#808080">        # in your "public" directory.
</span><span style="color:#808080">        try_files /not_exists @swoole;
</span><span style="color:#808080">    &#125;
</span><span style="color:#808080">    # any php files must not be accessed
</span><span style="color:#808080">    #location ~* \.php$ &#123;
</span><span style="color:#808080">    #    return 404;
</span><span style="color:#808080">    #&#125;
</span><span style="color:#808080">    location / &#123;
</span><span style="color:#808080">        try_files $uri $uri/ @swoole;
</span><span style="color:#808080">    &#125;
</span>
<span style="color:#808080">    location @swoole &#123;
</span><span style="color:#808080">        set $suffix "";
</span>
<span style="color:#808080">        if ($uri = /index.php) &#123;
</span><span style="color:#808080">            set $suffix ?$query_string;
</span><span style="color:#808080">        &#125;
</span>
<span style="color:#808080">        proxy_http_version 1.1;
</span><span style="color:#808080">        proxy_set_header Host $http_host;
</span><span style="color:#808080">        proxy_set_header Scheme $scheme;
</span><span style="color:#808080">        proxy_set_header SERVER_PORT $server_port;
</span><span style="color:#808080">        proxy_set_header REMOTE_ADDR $remote_addr;
</span><span style="color:#808080">        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
</span><span style="color:#808080">        proxy_set_header Upgrade $http_upgrade;
</span><span style="color:#808080">        proxy_set_header Connection $connection_upgrade;
</span>
<span style="color:#808080">        # IF https
</span><span style="color:#808080">        # proxy_set_header HTTPS "on";
</span>
<span style="color:#808080">        proxy_pass http://127.0.0.1:1215$suffix;
</span><span style="color:#808080">    &#125;
</span><span style="color:#808080">&#125;</span></pre> 
<p><strong>启动swoole</strong></p> 
<pre><span style="color:#808080">php artisan swoole:http start</span>
</pre> 
<p><strong>站点地址</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mycms.net.cn%2F%3Foschina" target="_blank">官方网站</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.mycms.net.cn%2Fsystem%2Flogin%3Foschina" target="_blank">演示后台</a></li> 
</ul> 
<p><strong>优秀案例</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zaixianjisuan.com%2F%3Foschina" target="_blank">在线计算网</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnav.mycms.net.cn%2F%3Foschina" target="_blank">程序员导航</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.gushici.top%2F%3Foschina" target="_blank">古诗词网</a></li> 
</ul>
                                        </div>
                                      
</div>
            