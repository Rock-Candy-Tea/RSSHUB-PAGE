
---
title: '国产开源 Http 服务器，smart-http 1.1.8 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=197'
author: 开源中国
comments: false
date: Sun, 15 Aug 2021 08:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=197'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">smart-http 是一款基于 smart-socket 的可编程式 http 应用微内核，同时还是为数不多的专注于服务器领域的国产开源项目。</p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">你可以将 smart-http 开发的程序部署在任何 Java 8 及以上版本的设备上。经过我们的不懈优化， 已经最大限度的降低程序运行期间对于内存和 GC 的开销。smart-http，是一款体现了作为开源人的工匠精神的作品。</span></p> 
<h1 style="text-align:left">开发示例</h1> 
<p style="text-align:left"><strong>服务端</strong></p> 
<pre style="text-align:left"><code class="language-java"><span style="color:#d73a49">public</span> <span style="color:#d73a49">class</span> <span style="color:#6f42c1">SimpleSmartHttp</span> &#123;
    <span style="color:#d73a49">public</span> <span style="color:#d73a49">static</span> <span style="color:#d73a49">void</span> <span style="color:#6f42c1">main</span>(String[] args) &#123;
        HttpBootstrap bootstrap = <span style="color:#d73a49">new</span> HttpBootstrap();
        bootstrap.pipeline(<span style="color:#d73a49">new</span> HttpServerHandler() &#123;
            <span style="color:#6a737d">@Override</span>
            <span style="color:#d73a49">public</span> <span style="color:#d73a49">void</span> <span style="color:#6f42c1">handle</span>(HttpRequest request, HttpResponse response) <span style="color:#d73a49">throws</span> IOException &#123;
                response.write(<span style="color:#032f62">"hello world<br/>"</span>.getBytes());
            &#125;
        &#125;);
        bootstrap.setPort(8080).start();
    &#125;
&#125;</code></pre> 
<p style="text-align:left"><strong>客户端 </strong></p> 
<pre style="text-align:left"><code class="language-java"><span style="color:#d73a49"><span style="color:#d73a49">public</span></span> <span style="color:#d73a49"><span style="color:#d73a49">class</span></span> <span style="color:#6f42c1"><span style="color:#6f42c1">HttpGetDemo</span></span> &#123;
    <span style="color:#d73a49"><span style="color:#d73a49">public</span></span> <span style="color:#d73a49"><span style="color:#d73a49">static</span></span> <span style="color:#d73a49"><span style="color:#d73a49">void</span></span> <span style="color:#6f42c1"><span style="color:#6f42c1">main</span></span>(String[] args) &#123;
        HttpClient httpClient = <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> HttpClient(<span style="color:#032f62"><span style="color:#032f62">"www.baidu.com"</span></span>, 80);
        httpClient.connect();
        httpClient.get(<span style="color:#032f62"><span style="color:#032f62">"/"</span></span>)
                .onSuccess(response -> System.out.println(response.body()))
                .onFailure(Throwable::printStackTrace)
                .send();
    &#125;
&#125;</code></pre> 
<h1 style="text-align:left">更新内容</h1> 
<ol> 
 <li style="text-align:left">升级 smart-socket 至 1.5.11。</li> 
 <li style="text-align:left">修复 HttpServerHandler 空实现时无法正常响应问题。</li> 
 <li style="text-align:left">修复 smart-http 在单核环境下默认线程数为 1 导致的启动报错问题。</li> 
 <li style="text-align:left">部分代码优化。</li> 
</ol> 
<h1 style="text-align:left">文档地址</h1> 
<p style="text-align:left">GiteePages：<a href="https://smartboot.gitee.io/book/smart-http/">https://smartboot.gitee.io/book/smart-http/</a></p> 
<h1 style="text-align:left">项目地址</h1> 
<p style="text-align:left">Gitee：<a href="https://gitee.com/smartboot/smart-http">https://gitee.com/smartboot/smart-http</a></p>
                                        </div>
                                      
</div>
            