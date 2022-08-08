
---
title: 'Forest v1.5.26 发布，简单高效的声明式 HTTP 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7176a890789deaf0dc6ec8695cc2bb8b13b.png'
author: 开源中国
comments: false
date: Mon, 08 Aug 2022 11:11:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7176a890789deaf0dc6ec8695cc2bb8b13b.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img alt height="365" src="https://oscimg.oschina.net/oscnet/up-7176a890789deaf0dc6ec8695cc2bb8b13b.png" width="400" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>Forest 介绍</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 是一个开源的声明式 Java HTTP 客户端框架，它能够将 HTTP 的所有请求信息（包括 URL、Header 以及 Body 等信息）绑定到您自定义的 Interface 方法上，能够通过调用本地接口方法的方式发送 HTTP 请求</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 如何使用</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 不需要您编写具体的 HTTP 调用过程，只需要您定义一个接口，然后通过 Forest 注解将 HTTP 请求的信息添加到接口的方法上即可。请求发送方通过调用您定义的接口便能自动发送请求和接受请求的响应</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 的工作原理</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 会将您定义好的接口通过动态代理的方式生成一个具体的实现类，然后组织、验证 HTTP 请求信息，绑定动态数据，转换数据形式，SSL 验证签名，调用后端 HTTP API (httpclient 等 API) 执行实际请求，等待响应，失败重试，转换响应数据到 Java 类型等脏活累活都由这动态代理的实现类给包了。 请求发送方调用这个接口时，实际上就是在调用这个干脏活累活的实现类</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">获得奖项</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2021 年度 OSC 中国开源项目评选<span style="background-color:#ffffff; color:#333333">「最受欢迎项目」</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/project/top_cn_2021">https://www.oschina.net/project/top_cn_2021</a></p> 
<h4 style="margin-left:0px; margin-right:0px; text-align:left">一个栗子</h4> 
<p>定义请求接口</p> 
<pre style="margin-left:.85rem; margin-right:.85rem; text-align:left"><code><span style="color:#cc99cd">public</span> <span style="color:#cc99cd">interface</span> <span style="color:#f8c555">MyClient</span> <span style="color:#cccccc">&#123;</span>

    <span style="color:#cccccc">@Get</span><span style="color:#cccccc">(</span><span style="color:#7ec699">"http://localhost:8080/hello"</span><span style="color:#cccccc">)</span>
    <span style="color:#f8c555">String</span> <span style="color:#f08d49">helloRequest</span><span style="color:#cccccc">(</span><span style="color:#cccccc">)</span><span style="color:#cccccc">;</span>

<span style="color:#cccccc">&#125;</span></code></pre> 
<p style="margin-left:0px; margin-right:0px; text-align:left">发送请求</p> 
<pre style="margin-left:.85rem; margin-right:.85rem; text-align:left"><code><span style="color:#999999">// 注入自定义的 Forest 接口实例</span>
<span style="color:#cccccc">@Resource</span>
<span style="color:#cc99cd">private</span> <span style="color:#f8c555">MyClient</span> myClient<span style="color:#cccccc">;</span>

<span style="color:#cc99cd">public</span> <span style="color:#cc99cd">void</span> <span style="color:#f08d49">testClient</span><span style="color:#cccccc">(</span><span style="color:#cccccc">)</span> <span style="color:#cccccc">&#123;</span>
    <span style="color:#999999">// 调用自定义的 MyClient 接口方法</span>
    <span style="color:#999999">// 等价于发送 HTTP 请求，请求地址和参数即为 helloRequest 方法上注解所标识的内容</span>
    <span style="color:#f8c555">String</span> result <span style="color:#67cdcc">=</span> myClient<span style="color:#cccccc">.</span><span style="color:#f08d49">helloRequest</span><span style="color:#cccccc">(</span><span style="color:#cccccc">)</span><span style="color:#cccccc">;</span>
    <span style="color:#999999">// result 即为 HTTP 请求响应后返回的字符串类型数据</span>
    <span style="color:#f8c555">System</span><span style="color:#cccccc">.</span>out<span style="color:#cccccc">.</span><span style="color:#f08d49">println</span><span style="color:#cccccc">(</span>result<span style="color:#cccccc">)</span><span style="color:#cccccc">;</span>
<span style="color:#cccccc">&#125;</span></code></pre> 
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
             <div style="margin-left:0; margin-right:0; text-align:start"> 
              <ul> 
               <li>[新增]: 在使用 OkHttp3 后端情况下，允许Query参数不转义大括号 (<a href="https://gitee.com/dromara/forest/issues/I5ITW9" target="_blank">#I5ITW9</a>)</li> 
               <li>[新增]: 在使用 OkHttp3 时绕过空 Multipart 错误 (<a href="https://gitee.com/dromara/forest/issues/I5I1AC" target="_blank">#I5I1AC</a>)</li> 
               <li>[修复]: 默认自动绕过SSL验证</li> 
               <li>[修复]: 声明的接口返回类型如果是String（或其他Charsequencel类型）导致自定义converter (<a href="https://gitee.com/dromara/forest/issues/I5L2P6" target="_blank">#I5L2P6</a>)</li> 
               <li>[修复]: okhttp后端自动将charset=UTF-8转成了小写 (<a href="https://gitee.com/dromara/forest/issues/I5L4AS" target="_blank">#I5L4AS</a>)</li> 
               <li>[修复]: url域名信息参数赋值会自动参数后添加”/“符号路径导致错误 (<a href="https://gitee.com/dromara/forest/issues/I5I62P" target="_blank">#I5I62P</a>)</li> 
               <li>[修复]: URL路径中的$字符会被转义</li> 
               <li>[修复]: 请求的ForestURL的ssl属性没有继承类里@BaseRequest的ssl信息 (<a href="https://gitee.com/dromara/forest/issues/I5HXHX" target="_blank">#I5HXHX</a>)</li> 
               <li>[更新]: spring 版本到<code>5.3.19</code></li> 
               <li>[更新]: spring boot 版本到<code>2.6.7</code></li> 
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
            