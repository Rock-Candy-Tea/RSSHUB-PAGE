
---
title: '声明式 HTTP 框架 Forest v1.5.22 发布！支持 Kotlin'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7176a890789deaf0dc6ec8695cc2bb8b13b.png'
author: 开源中国
comments: false
date: Wed, 08 Jun 2022 11:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7176a890789deaf0dc6ec8695cc2bb8b13b.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0px; margin-right:0px; text-align:center"><img alt height="384" src="https://oscimg.oschina.net/oscnet/up-7176a890789deaf0dc6ec8695cc2bb8b13b.png" width="420" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>Forest 介绍</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 是一个开源的 Java HTTP 客户端框架，它能够将 HTTP 的所有请求信息（包括 URL、Header 以及 Body 等信息）绑定到您自定义的 Interface 方法上，能够通过调用本地接口方法的方式发送 HTTP 请求</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 如何使用</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 不需要您编写具体的 HTTP 调用过程，只需要您定义一个接口，然后通过 Forest 注解将 HTTP 请求的信息添加到接口的方法上即可。请求发送方通过调用您定义的接口便能自动发送请求和接受请求的响应</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 的工作原理</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 会将您定义好的接口通过动态代理的方式生成一个具体的实现类，然后组织、验证 HTTP 请求信息，绑定动态数据，转换数据形式，SSL 验证签名，调用后端 HTTP API (httpclient 等 API) 执行实际请求，等待响应，失败重试，转换响应数据到 Java 类型等脏活累活都由这动态代理的实现类给包了。 请求发送方调用这个接口时，实际上就是在调用这个干脏活累活的实现类</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">获得奖项</h4> 
<p>2021年度OSC中国开源项目评选<span style="background-color:#ffffff; color:#333333">「最受欢迎项目」</span></p> 
<p><a href="https://www.oschina.net/project/top_cn_2021">https://www.oschina.net/project/top_cn_2021</a></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">重点更新内容</h3> 
<h4><strong>统一连接池</strong></h4> 
<p style="margin-left:0; margin-right:0">不用再分别定义 OkHttp 和 Httpclient 的连接池了，也不用担心异步请求和同步请求不在同一个连接池的烦恼了</p> 
<p style="margin-left:0; margin-right:0">本次更新统一连接池，可以通过<code>max-connections</code><span> </span>和<span> </span><code>max-route-connections</code>属性统一管理 OkHttp 和 HttpClient 所有后端的所有请求的最大请求数和最大每路由请求数，同时也包括异步请求在内可以一同进行限制</p> 
<h4>参数定义返回类型</h4> 
<p style="margin-left:0; margin-right:0">当接口方法返回的是未知参数的泛型类型时，可以通过新增的@Return参数注解，来标识某个参数为返回类型</p> 
<pre style="text-align:start"><code><span>    // 通过 Class 类型参数来标识返回类型
</span>    <span>@Get</span>(<span style="color:#dd1144">"/user/info"</span>)
    <T> <span>T <strong style="color:#990000">getGenericClass</strong><span>(@Return Class clazz)</span></span>;

<span>    // 通过 Type 类型参数来标识返回类型
</span>    <span>@Get</span>(<span style="color:#dd1144">"/user/info"</span>)
    <T> <span>T <strong style="color:#990000">getGenericType</strong><span>(@Return Type type)</span></span>;

<span>    // 通过 TypeReference 类型参数来标识返回类型</span></code><code>    <span>@Get</span>(<span style="color:#dd1144">"/user/info"</span>)
    <T> <span>T <strong style="color:#990000">getGenericTypeReference</strong><span>(@Return TypeReference typeReference)</span></span>;

</code></pre> 
<h3 style="margin-left:0; margin-right:0; text-align:left">文档和示例</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2F" target="_blank">项目官网</a></li> 
 <li><a href="https://apidoc.gitee.com/dt_flys/forest/">JavaDoc</a></li> 
 <li><a href="https://gitee.com/dt_flys/forest-example">Demo 工程</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">本次更新</h4> 
<div style="text-align:start"> 
 <div style="text-align:left"> 
  <div style="text-align:start"> 
   <div style="text-align:left"> 
    <blockquote> 
     <div style="text-align:start"> 
      <div style="text-align:start"> 
       <div style="text-align:start"> 
        <div style="text-align:start"> 
         <h4 style="margin-left:0; margin-right:0">新增特性:</h4> 
         <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
          <li>feat: 统一连接池 (<a href="https://gitee.com/dromara/forest/issues/I5APJA">#I5APJA:统一连接池</a>)</li> 
          <li>feat: 可配置异步请求线程池队列大小 (<a href="https://gitee.com/dromara/forest/issues/I5B78X">#I5B78X:可配置异步请求线程池队列大小</a>)</li> 
          <li>feat: 支持通过参数定义返回类型 (<a href="https://gitee.com/dromara/forest/issues/I5ANZL">#I5ANZL:支持通过参数定义返回类型</a>)</li> 
         </ul> 
         <h4 style="margin-left:0; margin-right:0">修复的问题:</h4> 
         <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
          <li>fix: spring 5.1 以下的低版本启动失败</li> 
          <li>fix: 请求地址中包含#字符会被转义导致资源找不到 (<a href="https://gitee.com/dromara/forest/issues/I59O7M">#I59O7M:请求地址中包含#字符会被转义导致资源找不到</a>)</li> 
          <li>fix: 配置BaseRequest的baseURL属性后,完整请求路径中的默认端口号会被覆盖,导致请求失败 (<a href="https://gitee.com/dromara/forest/issues/I4YBDV">#I4YBDV:配置BaseRequest的baseURL属性后,完整请求路径中的默认端口号会被覆盖,导致请求失败</a>)</li> 
          <li>fix: 解决当@body注解在对象上标识以后，char&Character类型的属性无法从客户端传输至服务端问题</li> 
          <li>fix: kotlin项目启动异常 (<a href="https://gitee.com/dromara/forest/issues/I50PDZ">#I50PDZ:1.5.17及之后的版本kotlin项目启动异常</a>)</li> 
          <li>fix: RetryWhen重试条件接口在最后一次重试后会执行两次 (<a href="https://gitee.com/dromara/forest/issues/I599BT">#I599BT:RetryWhen重试条件接口在最后一次重试后会执行两次</a>)</li> 
         </ul> 
        </div> 
       </div> 
      </div> 
     </div> 
    </blockquote> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            