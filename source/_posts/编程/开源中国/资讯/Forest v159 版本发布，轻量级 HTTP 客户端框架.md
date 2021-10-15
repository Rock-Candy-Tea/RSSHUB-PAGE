
---
title: 'Forest v1.5.9 版本发布，轻量级 HTTP 客户端框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6486'
author: 开源中国
comments: false
date: Fri, 15 Oct 2021 15:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6486'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="text-align:start"> 
 <p style="margin-left:0em; margin-right:0em">v1.5.9 版本发布了，此次更新主要解决了URL Encoder在某些情况下不正确的问题</p> 
 <p style="margin-left:0; margin-right:0">为此自己重新实现了URL解析和URL编码，抛弃了原有的Java自带的URI对象解析和URLEncoder类</p> 
 <p style="margin-left:0; margin-right:0">实现了URL语义化的字符串模板</p> 
 <h4 style="margin-left:0; margin-right:0">自动区分模板参数属于URL的哪个部分</h4> 
 <pre><code><span>/**
 * 新版本能够识别 &#123;a&#125; 和 &#123;b&#125; 是一个URL的Query参数
 * 会按照查询参数的要求进行URL编码：会将'&'符号转义 
 * 而 &#123;path&#125; 会被识别URL路径的一部分
 * 会按照URL路径的要求来进行URL编码：会保留'&'符号，不做转义
 */</span>
<span>@Get</span>(<span style="color:#dd1144">"/data/&#123;path&#125;?a=&#123;a&#125;&b=&#123;b&#125;"</span>)
<span>String <strong style="color:#990000">getData</strong><span>(@Var(<span style="color:#dd1144">"path"</span>)</span> String path, @<strong style="color:#990000">Var</strong><span>(<span style="color:#dd1144">"a"</span>)</span> String a, @<strong style="color:#990000">Var</strong><span>(<span style="color:#dd1144">"b"</span>)</span> String b)</span>;
</code></pre> 
 <h4 style="margin-left:0; margin-right:0"><code>&#123;&#125;</code>与<code>$&#123;&#125;</code>的区别</h4> 
 <p><code>&#123;&#125;</code>代表一个Query参数</p> 
 <p style="margin-left:0; margin-right:0"><code>&#123;&#125;</code>模板参数，在<code>?a=&#123;a&#125;</code>的情况下，会被认为是一个Query参数，即便变量可能包含"1&x=10&y=20"这样多个参数的字符串，也会被转义成一个Query参数</p> 
 <pre><code><span>@Get</span>(<span style="color:#dd1144">"http://localhost/data?a=&#123;a&#125;&b=&#123;b&#125;"</span>)
<span>String <strong style="color:#990000">getData</strong><span>(@Var(<span style="color:#dd1144">"a"</span>)</span> String a, @<strong style="color:#990000">Var</strong><span>(<span style="color:#dd1144">"b"</span>)</span> String b)
</span></code></pre> 
 <pre><code><em>// 最终产生的URL是</em>
<em>// http://localhost/data?a=1%26x%3D10%26y%3D20&b=hello</em>
<em>// 也就是只会有 a 和 b 两个Query参数</em>
myClient.getData(<span style="color:#dd1144">"1&x=10&y=20"</span>, <span style="color:#dd1144">"hello"</span>);
</code></pre> 
 <p><code>$&#123;&#125;</code>可以包含多个Query参数</p> 
 <p style="margin-left:0; margin-right:0">而<span> </span><code>$&#123;&#125;</code>模板参数，可以认为是一种字符串替换，替换完再对URL参数进行解析，所以一个模板参数引用的变量中可能包含多个参数，也会被解析成多个参数</p> 
 <pre><code><span>@Get</span>(<span style="color:#dd1144">"http://localhost/data?a=$&#123;a&#125;&b=$&#123;b&#125;"</span>)
<span>String <strong style="color:#990000">getData</strong><span>(@Var(<span style="color:#dd1144">"a"</span>)</span> String a, @<strong style="color:#990000">Var</strong><span>(<span style="color:#dd1144">"b"</span>)</span> String b)
</span></code></pre> 
 <pre><code><em>// 最终产生的URL是</em>
<em>// http://localhost/data?a=1&x=10&y=20&b=hello</em>
<em>// 也就是只会有 a、x、y、b 四个Query参数</em>
myClient.getData(<span style="color:#dd1144">"1&x=10&y=20"</span>, <span style="color:#dd1144">"hello"</span>);
</code></pre> 
 <h4 style="margin-left:0; margin-right:0">推荐使用<code>&#123;&#125;</code>作为模板参数</h4> 
 <p style="margin-left:0; margin-right:0">基于这两种模板参数各自的特性，都各有各的用处，但一般情况下，<strong>推荐使用<code>&#123;&#125;</code></strong></p> 
 <p style="margin-left:0; margin-right:0">因为它更结构化、更语义化，也更容易让人理解，不容易出错，尤其是在URL参数中传递另一个URL地址时的作用更为突出</p> 
 <p style="margin-left:0; margin-right:0">比如，要传一个带参数的子URL：<code>https://search.gitee.com/?type=repository&q=forest</code></p> 
 <p style="margin-left:0; margin-right:0">接到父URL后为<span> </span><code>http://localhost/data?call=&#123;url&#125;</code></p> 
 <p style="margin-left:0; margin-right:0">如果是用<code>$&#123;url&#125;</code>就会出问题</p> 
 <pre><code><span>@Get</span>(<span style="color:#dd1144">"/data?call=$&#123;url&#125;"</span>)
<span>String <strong style="color:#990000">getData</strong><span>(@Var(<span style="color:#dd1144">"url"</span>)</span> String url)</span>;

<em>// 最后产生的URL是</em>
<em>// http://localhost/data?call=https://search.gitee.com/?type=repository&q=forest</em>
</code></pre> 
 <p style="margin-left:0; margin-right:0">咋看起来没错，但最后那部分<code>&q=forest</code>会被认为是父URL的Query参数，但其实应该是子URL的</p> 
 <p style="margin-left:0; margin-right:0">如果用<span> </span><code>&#123;url&#125;</code><span> </span>就没关系，即使后来再有其它参数也毫无问题</p> 
 <pre><code><span>@Get</span>(<span style="color:#dd1144">"/data?call=&#123;url&#125;&x=&#123;x&#125;"</span>)
<span>String <strong style="color:#990000">getData</strong><span>(@Var(<span style="color:#dd1144">"url"</span>)</span> String url, @<strong style="color:#990000">Var</strong><span>(<span style="color:#dd1144">"x"</span>)</span> String x)</span>;

<em>// 最后产生的URL是</em>
<em>// http://localhost/data?call=https://search.gitee.com/?type=repository%26q=forest&x=xxx</em>
</code></pre> 
 <p style="margin-left:0; margin-right:0">可以看到，子URL中Query参数的连接符<code>&</code>被转义了，这样就解决了子URL参数和父URL参数(如后面的<code>x</code>)之间产生的歧义</p> 
 <h4 style="margin-left:0; margin-right:0">FIX的BUG</h4> 
 <ul> 
  <li>fix: URI路径的URLEncoder编码结果不正确 (<a href="https://gitee.com/dromara/forest/issues/I4DUFG">#I4DUFG:URI路径的URLEncoder编码结果不正确</a>)</li> 
 </ul> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目介绍</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Forest是一个高层的、极简的轻量级HTTP调用API框架。<br> 相比于直接使用Httpclient您不再用写一大堆重复的代码了，而是像调用本地方法一样去发送HTTP请求。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">文档和示例</h2> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2F" target="_blank">项目主页</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2Fdocs%2F" target="_blank">中文文档</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://apidoc.gitee.com/dt_flys/forest/">JavaDoc</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/dt_flys/forest-example">Demo工程</a></p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">发送JSON数据</h2> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">/**</span></span>
<span><span style="color:#888888"> * 将对象参数解析为JSON字符串，并放在请求的Body进行传输</span></span>
<span><span style="color:#888888"> */</span></span>
<span><span>@Post</span><span>(</span><span style="color:#dd2200">"/register"</span><span>)</span></span>
<span><strong style="color:#445588">String</strong> <strong style="color:#990000">registerUser</strong><span>(</span><span>@JSONBody</span> <strong style="color:#445588">MyUser</strong> <span>user</span><span>);</span></span>

<span><span style="color:#888888">/**</span></span>
<span><span style="color:#888888"> * 将Map类型参数解析为JSON字符串，并放在请求的Body进行传输</span></span>
<span><span style="color:#888888"> */</span></span>
<span><span>@Post</span><span>(</span><span style="color:#dd2200">"/test/json"</span><span>)</span></span>
<span><strong style="color:#445588">String</strong> <strong style="color:#990000">postJsonMap</strong><span>(</span><span>@JSONBody</span> <strong style="color:#445588">Map</strong> <span>mapObj</span><span>);</span></span>

<span><span style="color:#888888">/**</span></span>
<span><span style="color:#888888"> * 直接传入一个JSON字符串，并放在请求的Body进行传输</span></span>
<span><span style="color:#888888"> */</span></span>
<span><span>@Post</span><span>(</span><span style="color:#dd2200">"/test/json"</span><span>)</span></span>
<span><strong style="color:#445588">String</strong> <strong style="color:#990000">postJsonText</strong><span>(</span><span>@JSONBody</span> <strong style="color:#445588">String</strong> <span>jsonText</span><span>);</span></span></pre> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">发送XML数据</h2> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">/**</span></span>
<span><span style="color:#888888"> * 将一个通过JAXB注解修饰过的类型对象解析为XML字符串</span></span>
<span><span style="color:#888888"> * 并放在请求的Body进行传输</span></span>
<span><span style="color:#888888"> */</span></span>
<span><span>@Post</span><span>(</span><span style="color:#dd2200">"/message"</span><span>)</span></span>
<span><strong style="color:#445588">String</strong> <strong style="color:#990000">sendXmlMessage</strong><span>(</span><span>@XMLBody</span> <strong style="color:#445588">MyMessage</strong> <span>message</span><span>);</span></span>

<span><span style="color:#888888">/**</span></span>
<span><span style="color:#888888"> * 直接传入一个XML字符串，并放在请求的Body进行传输</span></span>
<span><span style="color:#888888"> */</span></span>
<span><span>@Post</span><span>(</span><span style="color:#dd2200">"/test/xml"</span><span>)</span></span>
<span><strong style="color:#445588">String</strong> <strong style="color:#990000">postXmlBodyString</strong><span>(</span><span>@XMLBody</span> <strong style="color:#445588">String</strong> <span>xml</span><span>);</span></span></pre> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">发送Protobuf数据</h2> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">/**</span></span>
<span><span style="color:#888888"> * ProtobufProto.MyMessage 为 Protobuf 生成的数据类</span></span>
<span><span style="color:#888888"> * 将 Protobuf 生成的数据对象转换为 Protobuf 格式的字节流</span></span>
<span><span style="color:#888888"> * 并放在请求的Body进行传输</span></span>
<span><span style="color:#888888"> * </span></span>
<span><span style="color:#888888"> * 注: 需要引入 google protobuf 依赖</span></span>
<span><span style="color:#888888"> */</span></span>
<span><span>@Post</span><span>(</span><span>url</span> <span>=</span> <span style="color:#dd2200">"/message"</span><span>,</span> <span>contentType</span> <span>=</span> <span style="color:#dd2200">"application/octet-stream"</span><span>)</span></span>
<span><strong style="color:#445588">String</strong> <strong style="color:#990000">sendProtobufMessage</strong><span>(</span><span>@ProtobufBody</span> <strong style="color:#445588">ProtobufProto</strong><span>.</span><span style="color:#008080">MyMessage</span> <span>message</span><span>);</span></span></pre> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">详细文档请看：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2F" target="_blank">http://forest.dtflyx.com</a></h2>
                                        </div>
                                      
</div>
            