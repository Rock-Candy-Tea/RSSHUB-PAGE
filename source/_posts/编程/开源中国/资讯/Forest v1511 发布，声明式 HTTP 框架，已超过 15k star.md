
---
title: 'Forest v1.5.11 发布，声明式 HTTP 框架，已超过 1.5k star'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-94aefb6f67d856d48916ee678e0e1239ab8.png'
author: 开源中国
comments: false
date: Tue, 19 Oct 2021 03:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-94aefb6f67d856d48916ee678e0e1239ab8.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2><strong>Forest介绍</strong></h2> 
<p>Forest 是一个开源的 Java HTTP 客户端框架，它能够将 HTTP 的所有请求信息（包括 URL、Header 以及 Body 等信息）绑定到您自定义的 Interface 方法上，能够通过调用本地接口方法的方式发送 HTTP 请求</p> 
<h3>现已超过 1500 star</h3> 
<p><img height="300" src="https://oscimg.oschina.net/oscnet/up-94aefb6f67d856d48916ee678e0e1239ab8.png" width="910" referrerpolicy="no-referrer"></p> 
<h3>Forest 如何使用</h3> 
<p>Forest 不需要您编写具体的 HTTP 调用过程，只需要您定义一个接口，然后通过 Forest 注解将 HTTP 请求的信息添加到接口的方法上即可。请求发送方通过调用您定义的接口便能自动发送请求和接受请求的响应。</p> 
<h3>Forest 的工作原理</h3> 
<p>Forest 会将您定义好的接口通过动态代理的方式生成一个具体的实现类，然后组织、验证 HTTP 请求信息，绑定动态数据，转换数据形式，SSL 验证签名，调用后端 HTTP API(httpclient 等 API)执行实际请求，等待响应，失败重试，转换响应数据到 Java 类型等脏活累活都由这动态代理的实现类给包了。 请求发送方调用这个接口时，实际上就是在调用这个干脏活累活的实现类。</p> 
<h3>文档和示例</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2F" target="_blank">项目主页</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2Fdocs%2F" target="_blank">中文文档</a></li> 
 <li><a href="https://apidoc.gitee.com/dt_flys/forest/">JavaDoc</a></li> 
 <li><a href="https://gitee.com/dt_flys/forest-example">Demo工程</a></li> 
</ul> 
<h3>本次更新</h3> 
<blockquote> 
 <p><strong>FIX的BUG</strong></p> 
 <ul> 
  <li>fix: connect-timeout配置在springboot 1.x 版本下无法解析 (#I4ECR3)</li> 
 </ul> 
 <p><strong>优化改进</strong></p> 
 <ul> 
  <li>optimize: 增强字符串模板报错信息 (#I4EC9V)</li> 
 </ul> 
</blockquote>
                                        </div>
                                      
</div>
            