
---
title: 'Forest v1.5.6 版本发布，轻量级 HTTP 客户端框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3983'
author: 开源中国
comments: false
date: Tue, 12 Oct 2021 15:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3983'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">Forest v1.5.6 版本发布了，此次更新主要修复一些BUG</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">项目介绍：</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Forest 是一个高层的、极简的轻量级 HTTP 调用 API 框架。<br> 相比于直接使用 Httpclient ，您不再用写一大堆重复的代码了，而是像调用本地方法一样去发送 HTTP 请求。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">文档和示例：</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2F" target="_blank">项目主页</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/dromara/forest">仓库地址</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2Fdocs%2F" target="_blank">中文文档</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://apidoc.gitee.com/dt_flys/forest/">JavaDoc</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/dt_flys/forest-example">Demo 工程</a></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 有哪些特性？</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>以 Httpclient 和 OkHttp 为后端框架</li> 
 <li>通过调用本地方法的方式去发送 Http 请求, 实现了业务逻辑与 Http 协议之间的解耦</li> 
 <li>因为针对第三方接口，所以不需要依赖 Spring Cloud 和任何注册中心</li> 
 <li>支持所有请求方法：GET 、HEAD 、OPTIONS 、TRACE 、POST 、DELETE 、PUT 、PATCH</li> 
 <li>支持文件上传和下载</li> 
 <li>支持灵活的模板表达式</li> 
 <li>支持拦截器处理请求的各个生命周期</li> 
 <li>支持自定义注解</li> 
 <li>支持 OAuth2 验证</li> 
 <li>支持过滤器来过滤传入的数据</li> 
 <li>基于注解、配置化的方式定义 Http 请求</li> 
 <li>支持 Spring 和 Springboot 集成</li> 
 <li>JSON 字符串到 Java 对象的自动化解析</li> 
 <li>XML 文本到 Java 对象的自动化解析</li> 
 <li>JSON、XML 或其他类型转换器可以随意扩展和替换</li> 
 <li>支持 JSON 转换框架: Fastjson 、Jackson 、Gson</li> 
 <li>支持 JAXB 形式的 XML 转换</li> 
 <li>可以通过 OnSuccess 和 OnError 接口参数实现请求结果的回调</li> 
 <li>配置简单，一般只需要 @Request 一个注解就能完成绝大多数请求的定义</li> 
 <li>支持异步请求调用</li> 
</ul> 
<div style="text-align:start"> 
 <h4 style="margin-left:0; margin-right:0; text-align:start">支持 Protobuf</h4> 
 <pre style="margin-left:0; margin-right:0; text-align:start"><code><span><span style="color:#032f62">@Post</span></span>(
    url = <span style="color:#dd1144"><span style="color:#032f62">"/proto"</span></span>,
    contentType = ContentType.APPLICATION_OCTET_STREAM)
ProtobufProto.<span>Data <strong style="color:#990000">sendProtobufData</strong><span>(<span style="color:#032f62">@ProtobufBody</span> ProtobufProto.Data data)</span></span>;
</code></pre> 
 <h4 style="margin-left:0; margin-right:0; text-align:start">后端切换的快捷注解</h4> 
 <pre style="margin-left:0; margin-right:0; text-align:start"><code><em><span style="color:#6a737d">// 切换到 okhttp3</span></em>
<span><span style="color:#032f62">@OkHttp</span></span><span style="color:#032f62">3</span>
<span><span style="color:#032f62">@Post</span></span>(<span style="color:#dd1144"><span style="color:#032f62">"/data1"</span></span>)
<span>String <strong style="color:#990000">sendData1</strong><span>(<span style="color:#032f62">@Body</span> MyUser user)</span></span>;

<em><span style="color:#6a737d">// 切换到 httpclient</span></em>
<span><span style="color:#032f62">@HttpClient</span></span>
<span><span style="color:#032f62">@Post</span></span>(<span style="color:#dd1144"><span style="color:#032f62">"/data2"</span></span>)
<span>String <strong style="color:#990000">sendData2</strong><span>(<span style="color:#032f62">@Body</span> MyUser user)</span></span>;
</code></pre> 
 <div style="text-align:start"> 
  <h4 style="margin-left:0; margin-right:0">新增特性:</h4> 
  <ul> 
   <li>feat: 将 timeout 细化为 connectTimeout 和 readTimeout  (<a href="https://gitee.com/dromara/forest/issues/I4DH21">#I4DH21:将timeout细化为connectTimeout和readTimeout</a>)</li> 
  </ul> 
  <h4 style="margin-left:0; margin-right:0">FIX 的 BUG:</h4> 
  <ul> 
   <li>fix: Google Protobuf 包依赖错误 (<a href="https://gitee.com/dromara/forest/issues/I4DDZY">#I4DDZY:Google Protobuf包依赖错误</a>)</li> 
   <li>fix: 配置 forest.connect-timeout 不生效 (<a href="https://gitee.com/dromara/forest/issues/I45298">#I45298:Spring Boot工程配置forest.connect-timeout不生效</a>)</li> 
  </ul> 
 </div> 
 <p> </p> 
</div>
                                        </div>
                                      
</div>
            