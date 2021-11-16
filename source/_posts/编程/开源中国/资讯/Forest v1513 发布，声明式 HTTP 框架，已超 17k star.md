
---
title: 'Forest v1.5.13 发布，声明式 HTTP 框架，已超 1.7k star'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b145353508a4482d04c55d25104d1e8bb21.png'
author: 开源中国
comments: false
date: Tue, 16 Nov 2021 05:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b145353508a4482d04c55d25104d1e8bb21.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left"><strong>Forest介绍</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 是一个开源的 Java HTTP 客户端框架，它能够将 HTTP 的所有请求信息（包括 URL、Header 以及 Body 等信息）绑定到您自定义的 Interface 方法上，能够通过调用本地接口方法的方式发送 HTTP 请求</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">现已超过 1700 star</h3> 
<p><img height="300" src="https://oscimg.oschina.net/oscnet/up-b145353508a4482d04c55d25104d1e8bb21.png" width="910" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 如何使用</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 不需要您编写具体的 HTTP 调用过程，只需要您定义一个接口，然后通过 Forest 注解将 HTTP 请求的信息添加到接口的方法上即可。请求发送方通过调用您定义的接口便能自动发送请求和接受请求的响应。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 的工作原理</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 会将您定义好的接口通过动态代理的方式生成一个具体的实现类，然后组织、验证 HTTP 请求信息，绑定动态数据，转换数据形式，SSL 验证签名，调用后端 HTTP API(httpclient 等 API)执行实际请求，等待响应，失败重试，转换响应数据到 Java 类型等脏活累活都由这动态代理的实现类给包了。 请求发送方调用这个接口时，实际上就是在调用这个干脏活累活的实现类。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">文档和示例</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2F" target="_blank">项目主页</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2Fdocs%2F" target="_blank">中文文档</a></li> 
 <li><a href="https://apidoc.gitee.com/dt_flys/forest/">JavaDoc</a></li> 
 <li><a href="https://gitee.com/dt_flys/forest-example">Demo工程</a></li> 
</ul> 
<div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <div style="text-align:start"> 
    <div style="text-align:left"> 
     <h3 style="margin-left:0; margin-right:0">本次更新</h3> 
     <blockquote> 
      <div style="text-align:start"> 
       <div style="text-align:start"> 
        <h4 style="margin-left:0; margin-right:0">新增特性</h4> 
        <ul> 
         <li>feat: 指定请求体类型的@BodyType注解 (<a href="https://gitee.com/dromara/forest/issues/I4IF3N">#I4IF3N:指定请求体类型的@BodyType注解</a>)</li> 
         <li>feat: 新增获取全部请求体中键值对参数的方法 (<a href="https://gitee.com/dromara/forest/issues/I4GWO7">#I4GWO7:新增一个获取全部key vlaue参数的方法，便于加签</a>)</li> 
        </ul> 
        <h4 style="margin-left:0; margin-right:0">修复的BUG</h4> 
        <ul> 
         <li>fix: 在请求中设置自定义Encoder无效 (<a href="https://gitee.com/dromara/forest/issues/I4HNZF">#I4HNZF:在请求中设置自定义Encoder无效</a>)</li> 
         <li>fix: url解析问题，如果包含@符@会去掉 (<a href="https://gitee.com/dromara/forest/issues/I4GQWW">#I4GQWW:在url中包含一个@符，例如http://aaa/bbb/sip:123456@aaa.com，@会去去掉</a>)</li> 
        </ul> 
        <h4 style="margin-left:0; margin-right:0">其它改动</h4> 
        <ul> 
         <li>add: BodyType注解</li> 
         <li>add: FastjsonEncoder注解</li> 
         <li>add: GsonEncoder注解</li> 
         <li>add: JacksonEncoder注解</li> 
        </ul> 
        <h4 style="margin-left:0; margin-right:0">不兼容改动</h4> 
        <ul> 
         <li>delete: com.dtflys.forest.http.ForestBodyType类</li> 
         <li>update:<span> </span><code>ForestRequest</code>类的<code>setBodyType</code>方法和<code>bodyType</code>方法的参数类型改为<code>ForestDatType</code></li> 
        </ul> 
       </div> 
      </div> 
     </blockquote> 
     <div style="text-align:start"> 
      <div style="text-align:start"> 
       <ul> 
       </ul> 
      </div> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            