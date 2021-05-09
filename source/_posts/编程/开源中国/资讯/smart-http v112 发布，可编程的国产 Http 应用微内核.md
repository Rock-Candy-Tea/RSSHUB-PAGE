
---
title: 'smart-http v1.1.2 发布，可编程的国产 Http 应用微内核'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4190'
author: 开源中国
comments: false
date: Sun, 09 May 2021 08:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4190'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">smart-http 是一款可编程的 Http 应用微内核，用户可根据自身需求进行 </span><span style="color:#ffffff"><span style="background-color:#e67e22"> </span><strong><span style="background-color:#e67e22">Server </span> </strong></span><span style="background-color:#ffffff; color:#333333">或 </span><span style="color:#ffffff"><span style="background-color:#e67e22"> </span><strong><span style="background-color:#e67e22">Client </span> </strong></span><span style="background-color:#ffffff; color:#333333">的应用开发。</span></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">你可以基于它开发 HTTP 代理服务器、网关、静态服务器、http  client 工具、性能压测工具等。smart-http 依旧延续着作者一贯秉持的极简、易用、高性能风格，只提供高性能的运行能力和易用的接口设计。把更多的可能性交给开发者，由那些富有创造力的 Java 开发者打造更优秀的 Http 作品。</span></p> 
<p style="text-align:left"><strong>更新内容</strong></p> 
<ol> 
 <li>优化：升级 smart-socket 至 v1.5.7。</li> 
 <li>bugfix：修复 <span style="color:#000000">WebSocketDefaultHandle 中的方法名单词拼写错误问题（</span><span style="color:#000000">感谢 @wujiawei0926</span><span style="color:#000000">）。</span></li> 
 <li><span style="color:#000000">bugfix：修复客户端 URI 后仅跟一个问号时的解析错位问题。</span></li> 
</ol> 
<p style="text-align:left"><strong>使用示例</strong></p> 
<p style="text-align:left">1. Server 端</p> 
<pre style="text-align:left"><code class="language-java"><span style="color:#d73a49">public</span> <span style="color:#d73a49">class</span> <span style="color:#6f42c1">SimpleSmartHttp</span> &#123;
    <span style="color:#d73a49">public</span> <span style="color:#d73a49">static</span> <span style="color:#d73a49">void</span> <span style="color:#6f42c1">main</span>(String[] args) &#123;
        HttpBootstrap bootstrap = <span style="color:#d73a49">new</span> HttpBootstrap();
        <span style="color:#6a737d">// 普通http请求</span>
        bootstrap.pipeline().next(<span style="color:#d73a49">new</span> HttpHandle() &#123;
            <span style="color:#6a737d">@Override</span>
            <span style="color:#d73a49">public</span> <span style="color:#d73a49">void</span> <span style="color:#6f42c1">doHandle</span>(HttpRequest request, HttpResponse response) <span style="color:#d73a49">throws</span> IOException &#123;
                response.write(<span style="color:#032f62">"hello world<br/>"</span>.getBytes());
            &#125;
        &#125;);
        <span style="color:#6a737d">// websocket请求</span>
        bootstrap.wsPipeline().next(<span style="color:#d73a49">new</span> WebSocketDefaultHandle() &#123;
            <span style="color:#6a737d">@Override</span>
            <span style="color:#d73a49">public</span> <span style="color:#d73a49">void</span> <span style="color:#6f42c1">handleTextMessage</span>(WebSocketRequest request, WebSocketResponse response, String data) &#123;
                response.sendTextMessage(<span style="color:#032f62">"Hello World"</span>);
            &#125;
        &#125;);
        bootstrap.setPort(8080).start();
    &#125;
&#125;</code></pre> 
<p style="text-align:left">2. Client 端</p> 
<pre style="text-align:left"><code class="language-java"><span style="color:#d73a49">public</span> <span style="color:#d73a49">class</span> <span style="color:#6f42c1">HttpGetDemo</span> &#123;
    <span style="color:#d73a49">public</span> <span style="color:#d73a49">static</span> <span style="color:#d73a49">void</span> <span style="color:#6f42c1">main</span>(String[] args) &#123;
        HttpClient httpClient = <span style="color:#d73a49">new</span> HttpClient(<span style="color:#032f62">"www.baidu.com"</span>, 80);
        httpClient.connect();
        httpClient.get(<span style="color:#032f62">"/"</span>)
                .onSuccess(response -> System.out.println(response.body()))
                .onFailure(Throwable::printStackTrace)
                .send();
    &#125;
&#125;
</code></pre> 
<p style="text-align:left"><strong>最后</strong></p> 
<p style="text-align:left">如果觉得这个项目还不错，请给我们加个 Star。并且非常欢迎大家为这个项目贡献你的想法和代码，开源不易，且行且珍惜。</p>
                                        </div>
                                      
</div>
            