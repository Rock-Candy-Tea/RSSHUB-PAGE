
---
title: '声明式 HTTP 框架 Forest v1.5.24 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7176a890789deaf0dc6ec8695cc2bb8b13b.png'
author: 开源中国
comments: false
date: Mon, 27 Jun 2022 12:31:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7176a890789deaf0dc6ec8695cc2bb8b13b.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img alt height="384" src="https://oscimg.oschina.net/oscnet/up-7176a890789deaf0dc6ec8695cc2bb8b13b.png" width="420" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>Forest 介绍</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 是一个开源的声明式 Java HTTP 客户端框架，它能够将 HTTP 的所有请求信息（包括 URL、Header 以及 Body 等信息）绑定到您自定义的 Interface 方法上，能够通过调用本地接口方法的方式发送 HTTP 请求</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 如何使用</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 不需要您编写具体的 HTTP 调用过程，只需要您定义一个接口，然后通过 Forest 注解将 HTTP 请求的信息添加到接口的方法上即可。请求发送方通过调用您定义的接口便能自动发送请求和接受请求的响应</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 的工作原理</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 会将您定义好的接口通过动态代理的方式生成一个具体的实现类，然后组织、验证 HTTP 请求信息，绑定动态数据，转换数据形式，SSL 验证签名，调用后端 HTTP API (httpclient 等 API) 执行实际请求，等待响应，失败重试，转换响应数据到 Java 类型等脏活累活都由这动态代理的实现类给包了。 请求发送方调用这个接口时，实际上就是在调用这个干脏活累活的实现类</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">获得奖项</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2021 年度 OSC 中国开源项目评选<span style="background-color:#ffffff; color:#333333">「最受欢迎项目」</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/project/top_cn_2021">https://www.oschina.net/project/top_cn_2021</a></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">文档和示例</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2F" target="_blank">项目官网</a></li> 
 <li><a href="https://apidoc.gitee.com/dt_flys/forest/">JavaDoc</a></li> 
 <li><a href="https://gitee.com/dt_flys/forest-example">Demo 工程</a></li> 
</ul> 
<div style="text-align:start"> 
 <div style="text-align:left"> 
  <div style="text-align:start"> 
   <div style="text-align:left"> 
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
             <h4 style="margin-left:0; margin-right:0">BUG 修复:</h4> 
             <div style="text-align:start"> 
              <ul> 
               <li>fix: OKHTTP 连接泄漏问题 (<a href="https://gitee.com/dromara/forest/issues/I5E613">#I5E613:OKHTTP 连接泄漏问题</a>)</li> 
               <li>fix: 遇到无法解析的Cookie时会报空指针 (<a href="https://gitee.com/dromara/forest/issues/I5E27R">#I5E27R:遇到无法解析的Cookie时会报空指针</a>)</li> 
              </ul> 
             </div> 
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
 </div> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            