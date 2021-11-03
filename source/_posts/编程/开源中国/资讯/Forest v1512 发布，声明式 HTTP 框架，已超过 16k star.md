
---
title: 'Forest v1.5.12 发布，声明式 HTTP 框架，已超过 1.6k star'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://chart.giteye.net/gitee/dromara/forest/NURRL346.png'
author: 开源中国
comments: false
date: Wed, 03 Nov 2021 05:45:00 GMT
thumbnail: 'https://chart.giteye.net/gitee/dromara/forest/NURRL346.png'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:start"> 
 <div style="text-align:left"> 
  <h2 style="margin-left:0; margin-right:0"><strong>Forest介绍</strong></h2> 
  <p style="margin-left:0; margin-right:0">Forest 是一个开源的 Java HTTP 客户端框架，它能够将 HTTP 的所有请求信息（包括 URL、Header 以及 Body 等信息）绑定到您自定义的 Interface 方法上，能够通过调用本地接口方法的方式发送 HTTP 请求</p> 
  <h3 style="margin-left:0; margin-right:0">现已超过 1600 star</h3> 
  <p style="margin-left:0; margin-right:0"><img alt="stars" height="300" src="https://chart.giteye.net/gitee/dromara/forest/NURRL346.png" width="910" referrerpolicy="no-referrer"></p> 
  <h3 style="margin-left:0; margin-right:0">Forest 如何使用</h3> 
  <p style="margin-left:0; margin-right:0">Forest 不需要您编写具体的 HTTP 调用过程，只需要您定义一个接口，然后通过 Forest 注解将 HTTP 请求的信息添加到接口的方法上即可。请求发送方通过调用您定义的接口便能自动发送请求和接受请求的响应。</p> 
  <h3 style="margin-left:0; margin-right:0">Forest 的工作原理</h3> 
  <p style="margin-left:0; margin-right:0">Forest 会将您定义好的接口通过动态代理的方式生成一个具体的实现类，然后组织、验证 HTTP 请求信息，绑定动态数据，转换数据形式，SSL 验证签名，调用后端 HTTP API(httpclient 等 API)执行实际请求，等待响应，失败重试，转换响应数据到 Java 类型等脏活累活都由这动态代理的实现类给包了。 请求发送方调用这个接口时，实际上就是在调用这个干脏活累活的实现类。</p> 
  <h3 style="margin-left:0; margin-right:0">文档和示例</h3> 
  <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2F" target="_blank">项目主页</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2Fdocs%2F" target="_blank">中文文档</a></li> 
   <li><a href="https://apidoc.gitee.com/dt_flys/forest/">JavaDoc</a></li> 
   <li><a href="https://gitee.com/dt_flys/forest-example">Demo工程</a></li> 
  </ul> 
  <h3 style="margin-left:0; margin-right:0">本次更新</h3> 
  <blockquote> 
   <div style="text-align:start"> 
    <h4 style="margin-left:0; margin-right:0">新增特性:</h4> 
    <ul> 
     <li>feat: getbody可以有key-value形式进行取值 (<a href="https://gitee.com/dromara/forest/issues/I4FUSB">#I4FUSB:建议改进下getbody可以有key -value形式进行取值</a>)</li> 
    </ul> 
    <h4 style="margin-left:0; margin-right:0">BUG FIX:</h4> 
    <ul> 
     <li>fix: URL参数会重复Encode (<a href="https://gitee.com/dromara/forest/issues/I4FDJC">#I4FDJC:URL参数会重复Encode</a>)</li> 
     <li>fix: &#123;变量名&#125;格式字符串模板在引用隐式变量时出错 (<a href="https://gitee.com/dromara/forest/issues/I4EP04">#I4EP04:&#123;变量名&#125;格式字符串模板在引用隐式变量时出错</a>)</li> 
     <li>fix: 对于<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%2Fxxx%3Ayyy%25E8%25BF%2599%25E7%25A7%258D%25E5%25BD%25A2%25E5%25BC%258F%25E7%259A%2584URL%25E8%25A7%25A3%25E6%259E%2590%25E9%2594%2599%25E8%25AF%25AF" target="_blank">http://localhost/xxx:yyy这种形式的URL解析错误</a><span> </span>(<a href="https://gitee.com/dromara/forest/issues/I4GC5M">#I4GC5M:对于http://localhost/xxx:yyy这种形式的URL解析错误</a>)</li> 
     <li>fix: httpclient和okhttp编码行为不一致 (<a href="https://gitee.com/dromara/forest/issues/I4FRR5">#I4FRR5:httpclient和okhttp编码行为不一致</a>)</li> 
     <li>fix: post请求的url为空的时候有bug (<a href="https://gitee.com/dromara/forest/issues/I4F3XS">#I4F3XS:post请求的url为空的时候有bug</a>)</li> 
     <li>fix: retrywhen中的异常被吃掉, 无法抛出. 且异常后仅触发一次重试 (<a href="https://gitee.com/dromara/forest/issues/I4E4X7">#I4E4X7:retrywhen中的异常被吃掉, 无法抛出. 且异常后仅触发一次重试</a>)</li> 
     <li>fix: Httpclient后端在连续异步发送请求后会出现I/IO报错 (<a href="https://gitee.com/dromara/forest/issues/I47FD7">#I47FD7:Httpclient后端在连续异步发送请求后会出现I/IO报错</a>)</li> 
    </ul> 
    <h4 style="margin-left:0; margin-right:0">代码重构:</h4> 
    <ul> 
     <li>refactor: 重构后端代码: 表单类型Body部分</li> 
     <li>refactor: 重构后端: okhttp3</li> 
     <li>refactor: 重构后端: httpclient</li> 
     <li>refactor: 重构后端: 重写异步请求逻辑</li> 
    </ul> 
    <h4 style="margin-left:0; margin-right:0">代码优化:</h4> 
    <ul> 
     <li>optimize: Forest对于一些错误的响应处理不友好 (<a href="https://gitee.com/dromara/forest/issues/I4EIDJ">#I4EIDJ:Forest对于一些错误的响应处理不友好</a>)</li> 
    </ul> 
    <h4 style="margin-left:0; margin-right:0">其它代码改动:</h4> 
    <ul> 
     <li>add: ForestBody类</li> 
     <li>add: Validations类</li> 
     <li>delete: OkHttp3不再使用的请求执行器类</li> 
    </ul> 
   </div> 
  </blockquote> 
 </div> 
</div>
                                        </div>
                                      
</div>
            