
---
title: 'smart-http v1.1.11发布，QPS 高达 703W 的 Http 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-75f4fddb6983a0d9370e4a73b6df8abe86b.png'
author: 开源中国
comments: false
date: Fri, 11 Feb 2022 09:48:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-75f4fddb6983a0d9370e4a73b6df8abe86b.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p style="margin-left:0; margin-right:0"><span>smart-http 是一款基于 smart-socket 通信框架，支持 HTTP/1.0、HTTP/1.1 以及 Websocket 协议的可编程式 HTTP 微内核。</span></p> 
 <h3 style="margin-left:0; margin-right:0"><span>此版本主要变化</span></h3> 
 <ol style="margin-left:0; margin-right:0"> 
  <li><span>新增 ByteTree 数据结构，提升解码和路由性能。</span></li> 
  <li><span>新增 </span><span style="color:#000000">TimerUtils 用于维护系统时钟。</span></li> 
  <li><span style="color:#000000">优化 Http 响应逻辑，减少空header的判断。</span></li> 
  <li><span>优化 chunked 响应的判定逻辑。</span></li> 
  <li><span>升级 smart-socket 至 1.5.15。</span></li> 
  <li><span style="color:#000000">移除 「HEAD 请求禁止 body 响应」的约束。</span></li> 
  <li><span>移除 HttpRouteHandler 中的缓存映射。</span></li> 
  <li><span style="color:#000000">移除 MessageProcessor 的代理设计。</span></li> 
  <li><span style="color:#000000">Http Body 解码器绑定至 RequestAttachment。</span></li> 
  <li><span style="color:#000000">支持集成 smart-socket 插件。</span></li> 
  <li><span>支持 MaxFormContentSize 配置化。</span></li> 
  <li><span>解码过程指定默认字符集：StandardCharsets.US_ASCII。</span></li> 
  <li><span>补充 https 的应用 demo。</span></li> 
 </ol> 
 <h3 style="margin-left:0; margin-right:0"><span>Maven 坐标</span></h3> 
 <pre><code class="language-xml"><dependency>
    <groupId>org.smartboot.http</groupId>
    <artifactId>smart-http-server</artifactId>
    <version>1.1.11</version>
</dependency></code></pre> 
 <h3 style="margin-left:0; margin-right:0"><span>示例代码</span></h3> 
 <pre><code class="language-java">public class SimpleSmartHttp &#123;
    public static void main(String[] args) &#123;
        HttpBootstrap bootstrap = new HttpBootstrap();
        bootstrap.httpHandler(new HttpServerHandler() &#123;
            @Override
            public void handle(HttpRequest request, HttpResponse response) throws IOException &#123;
                response.write("hello smart-http<br/>".getBytes());
            &#125;
        &#125;).setPort(8080).start();
    &#125;
&#125;</code></pre> 
 <h3 style="margin-left:0; margin-right:0"><span>性能评测</span></h3> 
 <p style="margin-left:0; margin-right:0"><span>历经三个多月的优化，该版本性能提升幅度约10%~15%，并于近期的 TFB 评测中以 703W 的QPS位居榜单第一位。</span></p> 
 <p><img height="1446" src="https://oscimg.oschina.net/oscnet/up-75f4fddb6983a0d9370e4a73b6df8abe86b.png" width="2340" referrerpolicy="no-referrer"></p> 
</div>
                                        </div>
                                      
</div>
            