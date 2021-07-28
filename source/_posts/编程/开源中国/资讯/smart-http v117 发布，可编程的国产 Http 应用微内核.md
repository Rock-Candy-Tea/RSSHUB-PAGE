
---
title: 'smart-http v1.1.7 发布，可编程的国产 Http 应用微内核'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6977'
author: 开源中国
comments: false
date: Wed, 28 Jul 2021 09:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6977'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">smart-http 是一款基于 smart-socket 的可编程式 http 应用微内核。</p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">你可以将 smart-http 开发的程序部署在任何 Java 8 及以上版本的设备上。经过我们的不懈优化， 已经最大限度的降低程序运行期间对于内存和 GC 的开销。smart-http，是一款体现了作为开源人的工匠精神的作品。</span></p> 
<h1 style="text-align:left">开发示例</h1> 
<p style="text-align:left"><strong>服务端</strong></p> 
<pre><code class="language-java">public class SimpleSmartHttp &#123;
    public static void main(String[] args) &#123;
        HttpBootstrap bootstrap = new HttpBootstrap();
        bootstrap.httpHandler(new HttpServerHandler() &#123;
            @Override
            public void handle(HttpRequest request, HttpResponse response) throws IOException &#123;
                response.write("hello smart-http<br/>".getBytes());
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
 <li>smart-http-server 默认启用 aio-enhance。</li> 
 <li>client 支持通过代理服务器转发 http 请求。</li> 
 <li>Http Body 采用响应式解析。</li> 
 <li>支持自定义 Http 响应码和描述。</li> 
 <li>client 支持指定超时时间。</li> 
 <li>client 支持启用内存池。</li> 
 <li>client 支持解压 gzip 响应内容。</li> 
 <li>优化异常码流可能导致的死循环问题。</li> 
 <li>移除 pipeline 的设计。</li> 
 <li>优化 Http 协议解析算法。</li> 
</ol> 
<h1 style="text-align:left">文档地址</h1> 
<p style="text-align:left">GiteePages：<a href="https://smartboot.gitee.io/book/smart-http/">https://smartboot.gitee.io/book/smart-http/</a></p> 
<h1 style="text-align:left">项目地址</h1> 
<p style="text-align:left">Gitee：<a href="https://gitee.com/smartboot/smart-http">https://gitee.com/smartboot/smart-http</a></p>
                                        </div>
                                      
</div>
            