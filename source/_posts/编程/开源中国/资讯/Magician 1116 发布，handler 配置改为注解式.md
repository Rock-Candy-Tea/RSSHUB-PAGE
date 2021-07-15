
---
title: 'Magician 1.1.16 发布，handler 配置改为注解式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7c098ebc21648557147fadf843f2efae80b.png'
author: 开源中国
comments: false
date: Thu, 15 Jul 2021 01:36:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7c098ebc21648557147fadf843f2efae80b.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>考虑到三方集成的方便性，所以将 handler的 配置 全部改成了注解式，只需要在类上加一个注解即可创建一个handler，让创建handler和创建服务 这两个步骤的耦合性降到了最低。</p> 
<p>这样如果有三方项目集成了Magician，就不用为handler的增减 而发愁了。</p> 
<h2>更新后的使用方式如下</h2> 
<p><strong>创建服务，指定一个扫描的范围即可</strong></p> 
<pre><code class="language-java">Magician.createTCPServer()
                    .scan("The package name of the handler")
                    .bind(8080);</code></pre> 
<p><strong>创建Handler，加个注解即可，不需要去改动 创建服务的代码</strong></p> 
<pre><code class="language-java">@TCPHandler(path="/")
public class DemoHandler implements TCPBaseHandler<MagicianRequest> &#123;

    @Override
    public void request(MagicianRequest magicianRequest) &#123;
        // response data
        magicianRequest.getResponse()
                .sendJson(200, "&#123;'status':'ok'&#125;");
    &#125;
&#125;</code></pre> 
<p><strong>增加websocket，只需要新建handler即可，一样不需要再去改动 创建服务的代码</strong></p> 
<pre><code class="language-java">@WebSocketHandler(path = "/websocket")
public class DemoSocketHandler implements WebSocketBaseHandler &#123;
   
    @Override
    public void onOpen(WebSocketSession webSocketSession) &#123;
     
    &#125;
   
    @Override
    public void onClose(WebSocketSession webSocketSession) &#123;
        
    &#125;

    @Override
    public void onMessage(String message, WebSocketSession webSocketSession) &#123;

    &#125;
&#125;</code></pre> 
<p>如果有三方项目集成了Magician，由于被集成的Magician 基本都会被二次封装，频繁改动这块代码不仅麻烦，还会有一定的隐患。现在改成了注解式 可以有效规避这个问题。</p> 
<h2>跟Magician一起升级的还有</h2> 
<p>Magician-Web组件，Martian组件。 这两个组件的升级点，主要是配合Magician的改动而改动。 而且给Martian带来了一个新特性：可以很方便的支持WebWocket了。</p> 
<p>--------------------------------</p> 
<p>Magician是一个异步非阻塞的网络编程包，支持TCP和UDP协议，内置了http和websocket解码器，使用方便简单。</p> 
<p>TFB测试结果 达到了每秒可以完成15万次请求。</p> 
<p><img alt height="415" src="https://oscimg.oschina.net/oscnet/up-7c098ebc21648557147fadf843f2efae80b.png" width="700" referrerpolicy="no-referrer"></p> 
<p>想了解更多可以关注官网：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmagician-io.com%2F" target="_blank">http://magician-io.com</a></p>
                                        </div>
                                      
</div>
            