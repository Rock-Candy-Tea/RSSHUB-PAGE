
---
title: '致力于实现 Http 服务器国产化，smart-http 1.1.5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4e330148f8519b413a6a74742e21fec732d.png'
author: 开源中国
comments: false
date: Wed, 09 Jun 2021 01:31:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4e330148f8519b413a6a74742e21fec732d.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>smart-http 是一款基于 smart-socket 的可编程式 http 应用微内核，同时还是为数不多的专注于服务器领域的国产开源项目。</p> 
<p>smart-http 采用了基于状态驱动的算法进行 Http 协议解码，这是一种对初中级开发人员极为友好的算法，以结构化的形式展示完整的 Http 解码过程。与此同时，在 smart-socket 强大通信能力的加持下，smart-http 的性能表现已属于业内顶尖水准。</p> 
<p><img height="1198" src="https://oscimg.oschina.net/oscnet/up-4e330148f8519b413a6a74742e21fec732d.png" width="1438" referrerpolicy="no-referrer"></p> 
<p>你可以将 smart-http 开发的程序部署在任何 Java 8 及以上版本的设备上。经过我们的不懈优化， 已经最大限度的降低程序运行期间对于内存和 GC 的开销。smart-http，是一款体现了作为开源人的工匠精神的作品。</p> 
<h1>开发示例</h1> 
<p><strong>服务端</strong></p> 
<pre><code class="language-java">public class SimpleSmartHttp &#123;
    public static void main(String[] args) &#123;
        HttpBootstrap bootstrap = new HttpBootstrap();
        bootstrap.pipeline(new HttpServerHandle() &#123;
            @Override
            public void doHandle(HttpRequest request, HttpResponse response) throws IOException &#123;
                response.write("hello world<br/>".getBytes());
            &#125;
        &#125;);
        bootstrap.setPort(8080).start();
    &#125;
&#125;</code></pre> 
<p><strong>客户端 </strong></p> 
<pre><code class="language-java">public class HttpGetDemo &#123;
    public static void main(String[] args) &#123;
        HttpClient httpClient = new HttpClient("www.baidu.com", 80);
        httpClient.connect();
        httpClient.get("/")
                .onSuccess(response -> System.out.println(response.body()))
                .onFailure(Throwable::printStackTrace)
                .send();
    &#125;
&#125;</code></pre> 
<h1>更新内容</h1> 
<ol> 
 <li>优化：引入跳跃式解码算法， 提升Http数据帧遍历效率。</li> 
 <li>优化：引入字符串常量池，提升解码效率并缓解 GC。</li> 
 <li>优化：提升 HttpRouteHandle 对于精准路径的路由匹配速度。</li> 
 <li>优化：升级 smart-socket 至最新版 1.5.9。</li> 
 <li>新特性：新增单元测试模块。</li> 
</ol> 
<h1>文档地址</h1> 
<p>GiteePages：<a href="https://smartboot.gitee.io/book/smart-http/">https://smartboot.gitee.io/book/smart-http/</a></p> 
<h1>项目地址</h1> 
<p>Gitee：<a href="https://gitee.com/smartboot/smart-http">https://gitee.com/smartboot/smart-http</a></p>
                                        </div>
                                      
</div>
            