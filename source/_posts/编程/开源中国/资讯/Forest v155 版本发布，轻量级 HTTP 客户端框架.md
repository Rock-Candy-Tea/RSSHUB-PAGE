
---
title: 'Forest v1.5.5 版本发布，轻量级 HTTP 客户端框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3490'
author: 开源中国
comments: false
date: Sat, 09 Oct 2021 17:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3490'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Forest v1.5.5 版本发布了，此版本主要支持了Protobuf，以及修改了若干Bug</p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:left">项目介绍：</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Forest是一个高层的、极简的轻量级HTTP调用API框架。<br> 相比于直接使用Httpclient您不再用写一大堆重复的代码了，而是像调用本地方法一样去发送HTTP请求。</p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:left">文档和示例：</h3> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2F" target="_blank">项目主页</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/dromara/forest">仓库地址</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2Fdocs%2F" target="_blank">中文文档</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://apidoc.gitee.com/dt_flys/forest/">JavaDoc</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/dt_flys/forest-example">Demo工程</a></p> </li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0px; text-align:left">Forest有哪些特性？</h3> 
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
 <li>JSON字符串到Java对象的自动化解析</li> 
 <li>XML文本到Java对象的自动化解析</li> 
 <li>JSON、XML或其他类型转换器可以随意扩展和替换</li> 
 <li>支持JSON转换框架: Fastjson, Jackson, Gson</li> 
 <li>支持JAXB形式的XML转换</li> 
 <li>可以通过OnSuccess和OnError接口参数实现请求结果的回调</li> 
 <li>配置简单，一般只需要@Request一个注解就能完成绝大多数请求的定义</li> 
 <li>支持异步请求调用</li> 
</ul> 
<div style="text-align:start"> 
 <h4 style="margin-left:0; margin-right:0">支持Protobuf</h4> 
 <pre><code><span>@Post</span>(
    url = <span style="color:#dd1144">"/proto"</span>,
    contentType = ContentType.APPLICATION_OCTET_STREAM)
ProtobufProto.<span>Data <strong style="color:#990000">sendProtobufData</strong><span>(@ProtobufBody ProtobufProto.Data data)</span></span>;
</code></pre> 
 <h4 style="margin-left:0; margin-right:0">后端切换的快捷注解</h4> 
 <pre><code><em>// 切换到 okhttp3</em>
<span>@OkHttp</span>3
<span>@Post</span>(<span style="color:#dd1144">"/data1"</span>)
<span>String <strong style="color:#990000">sendData1</strong><span>(@Body MyUser user)</span></span>;

<em>// 切换到 httpclient</em>
<span>@HttpClient</span>
<span>@Post</span>(<span style="color:#dd1144">"/data2"</span>)
<span>String <strong style="color:#990000">sendData2</strong><span>(@Body MyUser user)</span></span>;
</code></pre> 
 <h4 style="margin-left:0; margin-right:0">新特性:</h4> 
 <ul> 
  <li>feat: 支持每个请求都可自定义序列化转换器 (<a href="https://gitee.com/dromara/forest/issues/I4CLV8">#I4CLV8:支持每个请求都可自定义序列化转换器</a>)</li> 
  <li>feat: 二进制类型请求体 (<a href="https://gitee.com/dromara/forest/issues/I4D4GY">#I4D4GY:二进制类型请求体</a>)</li> 
  <li>feat: Protobuf请求体 (<a href="https://gitee.com/dromara/forest/issues/I4D4JT">#I4D4JT:Protobuf请求体</a>)</li> 
  <li>feat: 转换器对应包依赖 需要时获取 (<a href="https://gitee.com/dromara/forest/issues/I29XE0">#I29XE0:处理Protobuf的序列化和反序列化的转换器</a>)</li> 
 </ul> 
 <h4 style="margin-left:0; margin-right:0">Fix的Bug:</h4> 
 <ul> 
  <li>fix: getAttribute方法在多线程情况下取值会串 (<a href="https://gitee.com/dromara/forest/issues/I4D5KS">#I4D5KS:getAttribute在多线程情况下返回值会串</a>)</li> 
  <li>fix: 在onRetry方法中，调用 addQuery 或 addBody 能API无效 (<a href="https://gitee.com/dromara/forest/issues/I4CZS5">#I4CZS5:在onRetry方法中，调用 addQuery 或 addBody 能API无效</a>)</li> 
 </ul> 
 <h4 style="margin-left:0; margin-right:0">代码改动:</h4> 
 <ul> 
  <li>add:<span> </span><a href="https://gitee.com/okhttp3">@okhttp<span> </span></a>注解</li> 
  <li>add: @HttpClient 注解</li> 
  <li>add: ForestRequest.type(ForestRequestType type) 方法</li> 
  <li>add: ForestLogHandler.logContent(String content) 方法</li> 
 </ul> 
 <h4 style="margin-left:0; margin-right:0">特别鸣谢:</h4> 
 <p style="margin-left:0em; margin-right:0em"><a href="https://gitee.com/yakax">@yakax</a></p> 
</div>
                                        </div>
                                      
</div>
            