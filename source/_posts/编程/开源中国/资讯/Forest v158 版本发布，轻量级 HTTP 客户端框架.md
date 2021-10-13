
---
title: 'Forest v1.5.8 版本发布，轻量级 HTTP 客户端框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1009'
author: 开源中国
comments: false
date: Wed, 13 Oct 2021 11:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1009'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start"><strong>v1.5.8</strong> 版本发布，该版本主要解决以下BUG：</p> 
<div style="text-align:start"> 
 <ul> 
  <li>fix: 使用<code>@DownloadFile</code>下载文件时，在某些环境下会发送阻塞 (<a href="https://gitee.com/dromara/forest/issues/I4DLBI">#I4DLBI:使用@DownloadFile下载文件，在某些环境下会发送阻塞</a>)</li> 
 </ul> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li>fix: response对google protobuf包依赖 (<a href="https://gitee.com/dromara/forest/issues/I4DKQW">#I4DKQW:forest-spring-boot-starter 1.5.6缺少protobuf-java的jar包</a>)</li> 
 </ul> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目介绍：</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Forest是一个高层的、极简的轻量级HTTP调用API框架。<br> 相比于直接使用Httpclient您不再用写一大堆重复的代码了，而是像调用本地方法一样去发送HTTP请求。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">文档和示例：</h2> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2F" target="_blank">项目主页</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2Fdocs%2F" target="_blank">中文文档</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://apidoc.gitee.com/dt_flys/forest/">JavaDoc</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/dt_flys/forest-example">Demo工程</a></p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Forest有哪些特性？</h2> 
<ul> 
 <li>以Httpclient和OkHttp为后端框架</li> 
 <li>通过调用本地方法的方式去发送Http请求, 实现了业务逻辑与Http协议之间的解耦</li> 
 <li>因为针对第三方接口，所以不需要依赖Spring Cloud和任何注册中心</li> 
 <li>支持所有请求方法：GET, HEAD, OPTIONS, TRACE, POST, DELETE, PUT, PATCH</li> 
 <li>支持文件上传和下载</li> 
 <li>支持灵活的模板表达式</li> 
 <li>支持拦截器处理请求的各个生命周期</li> 
 <li>支持自定义注解</li> 
 <li>支持OAuth2验证</li> 
 <li>支持过滤器来过滤传入的数据</li> 
 <li>基于注解、配置化的方式定义Http请求</li> 
 <li>支持Spring和Springboot集成</li> 
 <li>JSON格式数据序列化和反序列化</li> 
 <li>XML格式数据序列化和反序列化</li> 
 <li>Protobuf格式数据序列化和反序列化</li> 
 <li>JSON、XML或其他类型转换器可以随意扩展和替换</li> 
 <li>支持JSON转换框架: Fastjson, Jackson, Gson</li> 
 <li>支持JAXB形式的XML转换</li> 
 <li>可以通过OnSuccess和OnError接口参数实现请求结果的回调</li> 
 <li>配置简单，一般只需要@Request一个注解就能完成绝大多数请求的定义</li> 
 <li>支持异步请求调用</li> 
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
<h2 style="margin-left:0; margin-right:0; text-align:left">文件上传</h2> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">/**</span></span>
<span><span style="color:#888888"> * 用@DataFile注解修饰要上传的参数对象</span></span>
<span><span style="color:#888888"> * OnProgress参数为监听上传进度的回调函数</span></span>
<span><span style="color:#888888"> */</span></span>
<span><span>@Post</span><span>(</span><span style="color:#dd2200">"/upload"</span><span>)</span></span>
<span><strong style="color:#445588">Map</strong> <strong style="color:#990000">upload</strong><span>(</span><span>@DataFile</span><span>(</span><span style="color:#dd2200">"file"</span><span>)</span> <strong style="color:#445588">String</strong> <span>filePath</span><span>,</span> <strong style="color:#445588">OnProgress</strong> <span>onProgress</span><span>);</span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">可以用一个方法加Lambda同时解决文件上传和上传的进度监听</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#445588">Map</strong> <span>result</span> <span>=</span> <span>myClient</span><span>.</span><span style="color:#008080">upload</span><span>(</span><span style="color:#dd2200">"D:\\TestUpload\\xxx.jpg"</span><span>,</span> <span>progress</span> <span>-></span> <span>&#123;</span></span>
<span>    <strong style="color:#445588">System</strong><span>.</span><span style="color:#008080">out</span><span>.</span><span style="color:#008080">println</span><span>(</span><span style="color:#dd2200">"progress: "</span> <span>+</span> <strong style="color:#445588">Math</strong><span>.</span><span style="color:#008080">round</span><span>(</span><span>progress</span><span>.</span><span style="color:#008080">getRate</span><span>()</span> <span>*</span> <span style="color:#009999">100</span><span>)</span> <span>+</span> <span style="color:#dd2200">"%"</span><span>);</span>  <span style="color:#888888">// 已上传百分比</span></span>
<span>    <strong style="color:#000000">if</strong> <span>(</span><span>progress</span><span>.</span><span style="color:#008080">isDone</span><span>())</span> <span>&#123;</span>   <span style="color:#888888">// 是否上传完成</span></span>
<span>        <strong style="color:#445588">System</strong><span>.</span><span style="color:#008080">out</span><span>.</span><span style="color:#008080">println</span><span>(</span><span style="color:#dd2200">"--------   Upload Completed!   --------"</span><span>);</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;);</span></span>
</pre> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">基本签名验证</h2> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>@Post</span><span>(</span><span style="color:#dd2200">"/hello/user?username=$&#123;username&#125;"</span><span>)</span></span>
<span><span>@BasicAuth</span><span>(</span><span>username</span> <span>=</span> <span style="color:#dd2200">"$&#123;username&#125;"</span><span>,</span> <span>password</span> <span>=</span> <span style="color:#dd2200">"bar"</span><span>)</span></span>
<span><strong style="color:#445588">String</strong> <strong style="color:#990000">send</strong><span>(</span><span>@DataVariable</span><span>(</span><span style="color:#dd2200">"username"</span><span>)</span> <strong style="color:#445588">String</strong> <span>username</span><span>);</span></span>
</pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            