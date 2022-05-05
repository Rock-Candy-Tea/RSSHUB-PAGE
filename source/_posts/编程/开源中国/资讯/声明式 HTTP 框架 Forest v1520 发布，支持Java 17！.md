
---
title: '声明式 HTTP 框架 Forest v1.5.20 发布，支持Java 17！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e095709750cf803e835235b2f549ef278f6.png'
author: 开源中国
comments: false
date: Thu, 05 May 2022 08:25:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e095709750cf803e835235b2f549ef278f6.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="248" src="https://oscimg.oschina.net/oscnet/up-e095709750cf803e835235b2f549ef278f6.png" width="400" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>Forest介绍</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 是一个开源的 Java HTTP 客户端框架，它能够将 HTTP 的所有请求信息（包括 URL、Header 以及 Body 等信息）绑定到您自定义的 Interface 方法上，能够通过调用本地接口方法的方式发送 HTTP 请求</p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>在Gitee上现已超过 2.3k star</strong></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 如何使用</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 不需要您编写具体的 HTTP 调用过程，只需要您定义一个接口，然后通过 Forest 注解将 HTTP 请求的信息添加到接口的方法上即可。请求发送方通过调用您定义的接口便能自动发送请求和接受请求的响应</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 的工作原理</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 会将您定义好的接口通过动态代理的方式生成一个具体的实现类，然后组织、验证 HTTP 请求信息，绑定动态数据，转换数据形式，SSL 验证签名，调用后端 HTTP API(httpclient 等 API)执行实际请求，等待响应，失败重试，转换响应数据到 Java 类型等脏活累活都由这动态代理的实现类给包了。 请求发送方调用这个接口时，实际上就是在调用这个干脏活累活的实现类</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">支持JDK 17</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">JDK 17这个坑已经挖了好一阵子了，这次终于把它填上了。此次新版本<code>1.5.20</code>兼容了从8到17所有JDK的版本，不会再出现新鱼与熊掌不能兼得的问题，也不再需要额外引入 jaxb 包就能在11以上版本正常运行</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">文档和示例</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2F" target="_blank">项目官网</a></li> 
 <li><a href="https://apidoc.gitee.com/dt_flys/forest/">JavaDoc</a></li> 
 <li><a href="https://gitee.com/dt_flys/forest-example">Demo工程</a></li> 
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
        <h4 style="margin-left:0; margin-right:0">修复的问题:</h4> 
        <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
         <li> <p style="margin-left:0; margin-right:0">feat: 支持JDK17，兼容从8、11到17所有JDK版本</p> </li> 
        </ul> 
        <h4 style="margin-left:0; margin-right:0">修复的问题:</h4> 
        <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
         <li> <p style="margin-left:0; margin-right:0">fix:  BaseRequest 设置connectTimeout和readTimeout没效果</p> </li> 
         <li> <p style="margin-left:0; margin-right:0">fix: 下载，内存溢出</p> </li> 
         <li> <p style="margin-left:0; margin-right:0">fix: AddressSource 里面配置 basePath 不生效</p> </li> 
        </ul> 
        <h4 style="margin-left:0; margin-right:0">特别鸣谢</h4> 
        <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
         <li><a href="https://gitee.com/chming">@chming</a></li> 
        </ul> 
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
            