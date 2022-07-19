
---
title: 'Forest v1.5.25 发布，声明式 HTTP 客户端框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://forest.dtflyx.com/img/forest_logo.png'
author: 开源中国
comments: false
date: Tue, 19 Jul 2022 11:02:00 GMT
thumbnail: 'https://forest.dtflyx.com/img/forest_logo.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img alt height="496" src="https://forest.dtflyx.com/img/forest_logo.png" width="558" referrerpolicy="no-referrer"></p> 
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
<h3><strong>简单的例子</strong></h3> 
<p style="color:#00323c; text-align:start">创建一个<code>interface</code>，并用<code>@Get</code>注解修饰接口方法。</p> 
<div style="text-align:start"> 
 <pre style="margin-left:.85rem; margin-right:.85rem; text-align:left"><code><span style="color:#cc99cd">public</span> <span style="color:#cc99cd">interface</span> <span style="color:#f8c555">MyClient</span> <span style="color:#cccccc">&#123;</span>
    <span style="color:#cccccc">@Get</span><span style="color:#cccccc">(</span><span style="color:#7ec699">"http://localhost:8080/hello"</span><span style="color:#cccccc">)</span>
    <span style="color:#f8c555">String</span> <span style="color:#f08d49">hello</span><span style="color:#cccccc">(</span><span style="color:#cccccc">)</span><span style="color:#cccccc">;</span>
<span style="color:#cccccc">&#125;</span></code></pre> 
</div> 
<p style="color:#00323c; text-align:start">通过<code>@Get</code>注解，将上面的<code>MyClient</code>接口中的<code>simpleRequest()</code>方法绑定了一个 HTTP 请求， 其 URL 为<code>http://localhost:8080/hello</code><span> </span>，并默认使用<code>GET</code>方式，且将请求响应的数据以<code>String</code>的方式返回给调用者</p> 
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
             <div style="text-align:start"> 
              <h4 style="margin-left:0; margin-right:0">修复的问题</h4> 
              <ul> 
               <li>fix: 匹配验证secure cookie</li> 
               <li>fix: cookie携带请求不成功 (<a href="https://gitee.com/dromara/forest/issues/I5F8IY">#I5F8IY:cookie携带请求不成功</a>)</li> 
               <li>fix: OKHTTP 连接泄漏问题 (<a href="https://gitee.com/dromara/forest/issues/I5E613">#I5E613:OKHTTP 连接泄漏问题</a>)</li> 
               <li>fix: forest 支持springboot 1.5.14.realese 启动失败 (<a href="https://gitee.com/dromara/forest/issues/I5FDBG">#I5FDBG:forest 支持springboot 1.5.14.realese 启动失败</a>)</li> 
               <li>fix: 传的参数带有+号，但是服务接收时，获取的参数值中+号全部变成空格了 (<a href="https://gitee.com/dromara/forest/issues/I5EG9L">#I5EG9L:传的参数带有+号，但是服务接收时，获取的参数值中+号全部变成空格了</a>)</li> 
              </ul> 
              <h4 style="margin-left:0; margin-right:0">其它改动</h4> 
              <ul> 
               <li>add: OkHttp3Cookie</li> 
               <li>add: HttpclientCookie</li> 
               <li>update: 更新jackson版本到2.13.3</li> 
               <li>update: 更新jackson-databind版本到2.13.3</li> 
               <li>update: 更新jackson-annotations版本到2.13.3</li> 
               <li>update: 更新gson版本到2.8.9</li> 
               <li>update: 更新fastjson版本到1.2.83</li> 
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
            