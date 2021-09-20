
---
title: 'Web 服务软件 xmlweb 更新，添加 https 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3388'
author: 开源中国
comments: false
date: Sun, 19 Sep 2021 16:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3388'
---

<div>   
<div class="content">
                                                                                            <p><span>​ </span><span style="background-color:#ffffff; color:#333333">xmlweb 是一个基于状态机理论设计的 web 服务器，使用它可以设计出高可读性、高可维护性的 web 服务应用。你可以使用它作为 express 或者 koa 的一个替代。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">最近更新，添加 https 支持。使用方式类似 HTTP 组件，</span><span style="background-color:#f9f9f9; color:#333333">但使用时需要提供私钥以及证书文件路径。</span></p> 
<pre><code class="language-xml"><i:HTTPS listen='80' key='./privatekey.pem' cert='./certificate.pem' xmlns:i='//xmlweb'>
    <i:Router url='/index.html'/>
    <Hello id='hello'/>
</i:HTTPS></code></pre>
                                        </div>
                                      
</div>
            