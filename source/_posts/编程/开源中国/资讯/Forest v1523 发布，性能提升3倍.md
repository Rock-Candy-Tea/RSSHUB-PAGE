
---
title: 'Forest v1.5.23 发布，性能提升3倍'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7176a890789deaf0dc6ec8695cc2bb8b13b.png'
author: 开源中国
comments: false
date: Tue, 21 Jun 2022 13:31:00 GMT
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
<h4 style="margin-left:0; margin-right:0; text-align:start">重点优化内容</h4> 
<ol> 
 <li>引入了 ForestRoute 路由的概念，每个 Host + Port 的不同组合对应不同的路由</li> 
 <li>将 OkHttpClient 以及 HttpClient 后端 Client 对象归类到不同的路由，并进行缓存</li> 
 <li>可以从外部注入自定义的后端 Client 对象</li> 
 <li>默认都会缓存后端 Client 对象，同路由、同SSL、同超时间情况下都会复用同一个 Client 对象</li> 
 <li>如某个接口不想缓存 Client 对象，可通过<code>@BackendClient</code>注解进行配置 <p> </p> </li> 
</ol> 
<div style="text-align:start"> 
 <div style="text-align:left"> 
  <div style="text-align:start"> 
   <div style="text-align:left"> 
    <h4 style="margin-left:0; margin-right:0; text-align:start">优化结果</h4> 
    <p> </p> 
    <p style="text-align:center"><img height="454" src="https://oscimg.oschina.net/oscnet/up-35daac70f6d140d6e4f709c81b808183b49.png" width="800" referrerpolicy="no-referrer"></p> 
    <p>OkHttp后端QPS提升3倍，Httpclient后端QPS提升1倍</p> 
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
             <ul> 
              <li>feat: 快速接口支持快速下载文件</li> 
              <li>feat: 可配置注入OkHttpClient和HttpClient对象 (<a href="https://gitee.com/dromara/forest/issues/I5CWAL">#I5CWAL:可配置注入OkHttpClient和HttpClient对象</a>)</li> 
              <li>feat: 可配置接口的后端Client对象是否缓存 (<a href="https://gitee.com/dromara/forest/issues/I5D818">#I5D818:可配置接口的后端Client对象是否缓存</a>)</li> 
             </ul> 
             <h4 style="margin-left:0; margin-right:0">BUG修复:</h4> 
             <ul> 
              <li>fix: springboot配置binary转换器初始化失败 (<a href="https://gitee.com/dromara/forest/issues/I5D07S">#I5D07S:springboot配置binary转换器初始化失败</a>)</li> 
              <li>fix: ForestResponse.statusIs(xxx)会出现空指针 (<a href="https://gitee.com/dromara/forest/issues/I5CWQL">#I5CWQL:ForestResponse.statusIs(xxx)会出现空指针</a>)</li> 
              <li>fix: 在@Address注解的basePath中写的端口号会失效 (<a href="https://gitee.com/dromara/forest/issues/I5CR15">#I5CR15:在@Address注解的basePath中写的端口号会失效</a>)</li> 
              <li>fix: 使用@HTTPProxy注解对https请求设置http代理后出现java.lang.IllegalArgumentException:Socket may not be null</li> 
              <li>fix: 在不设置ContentType和BodyType的情况下无法正常发送请求 (<a href="https://gitee.com/dromara/forest/issues/I5CML4">#I5CML4:在不设置ContentType和BodyType的情况下无法正常发送请求</a>)</li> 
              <li>fix: ForestRequest.addBody(List) 循环中只执行一次</li> 
             </ul> 
             <h4 style="margin-left:0; margin-right:0; text-align:start">代码改动</h4> 
             <ul> 
              <li>refactor: 重构Cookie (<a href="https://gitee.com/dromara/forest/issues/I5C26U">#I5C26U:重构Cookie</a>)</li> 
              <li>refactor: 重构OkHttpClient</li> 
              <li>add: 添加拦截器到请求中方法ForestRequest#addInterceptor(Class<? extends Interceptor>)</li> 
              <li>add: HttpClientFactory</li> 
              <li>add: OkHttpClientFactory</li> 
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
 </div> 
</div> 
<div style="text-align:start"> 
 <div> 
  <div> 
   <p> </p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            