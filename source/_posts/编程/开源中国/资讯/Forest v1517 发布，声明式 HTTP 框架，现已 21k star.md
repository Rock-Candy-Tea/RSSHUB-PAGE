
---
title: 'Forest v1.5.17 发布，声明式 HTTP 框架，现已 2.1k star'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e095709750cf803e835235b2f549ef278f6.png'
author: 开源中国
comments: false
date: Wed, 09 Feb 2022 14:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e095709750cf803e835235b2f549ef278f6.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="248" src="https://oscimg.oschina.net/oscnet/up-e095709750cf803e835235b2f549ef278f6.png" width="400" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>Forest介绍</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 是一个开源的 Java HTTP 客户端框架，它能够将 HTTP 的所有请求信息（包括 URL、Header 以及 Body 等信息）绑定到您自定义的 Interface 方法上，能够通过调用本地接口方法的方式发送 HTTP 请求</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">现已 2.1k star</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://chart.giteye.net/gitee/dromara/forest/NURRL346.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 如何使用</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 不需要您编写具体的 HTTP 调用过程，只需要您定义一个接口，然后通过 Forest 注解将 HTTP 请求的信息添加到接口的方法上即可。请求发送方通过调用您定义的接口便能自动发送请求和接受请求的响应</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 的工作原理</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 会将您定义好的接口通过动态代理的方式生成一个具体的实现类，然后组织、验证 HTTP 请求信息，绑定动态数据，转换数据形式，SSL 验证签名，调用后端 HTTP API(httpclient 等 API)执行实际请求，等待响应，失败重试，转换响应数据到 Java 类型等脏活累活都由这动态代理的实现类给包了。 请求发送方调用这个接口时，实际上就是在调用这个干脏活累活的实现类</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">文档和示例</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2F" target="_blank">项目官网</a></li> 
 <li><a href="https://apidoc.gitee.com/dt_flys/forest/">JavaDoc</a></li> 
 <li><a href="https://gitee.com/dt_flys/forest-example">Demo工程</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">重点更新内容</h2> 
<h4 style="margin-left:0; margin-right:0; text-align:start">动态正向代理来源</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">定义一个实现 HTTPProxySource 接口的类</p> 
<div style="text-align:start"> 
 <pre style="text-align:left"><code><em>// 自定义正向代理来源类</em>
<em>// 可以根据请求对象的信息来动态产生该请求所需的正向代理信息</em>
<strong style="color:#333333">public</strong> <span><strong style="color:#333333">class</strong> <strong style="color:#445588">MyHTTPProxySource</strong> <strong style="color:#333333">implements</strong> <strong style="color:#445588">HTTPProxySource</strong> </span>&#123;
    <span>@Override</span>
    <span><strong style="color:#333333">public</strong> ForestProxy <strong style="color:#990000">getProxy</strong><span>(ForestRequest request)</span> </span>&#123;
        <em>//  request.variableValue 方法可以获取全局或请求变量</em>
        <em>// 返回值将以 ForestProxy 类对象形式包装正向代理信息</em>
        <strong style="color:#333333">return</strong> <strong style="color:#333333">new</strong> ForestProxy(<span style="color:#dd1144">"127.0.0.1"</span>, (Integer) request.variableValue(<span style="color:#dd1144">"port"</span>));
    &#125;
&#125;
</code>
</pre> 
</div> 
<div style="text-align:start"> 
 <div style="text-align:center">
   
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">在接口中绑定</p> 
<div style="text-align:start"> 
 <pre style="text-align:left"><code><em>// 通过 HTTPProxy 注解的 source 属性指定自定义的正向代理来源类</em>
<span>@Post</span>(<span style="color:#dd1144">"/data"</span>)
<span>@HTTPProxy</span>(source = MyHTTPProxySource.class)
<span>ForestRequest<String> <strong style="color:#990000">sendData</strong><span>(@Var(<span style="color:#dd1144">"port"</span>)</span> <strong style="color:#333333">int</strong> port)</span>;
</code></pre> 
</div> 
<div style="text-align:start"> 
 <div style="text-align:left"> 
  <div style="text-align:start"> 
   <div style="text-align:left"> 
    <h3 style="margin-left:0; margin-right:0">本次更新</h3> 
    <blockquote> 
     <div style="text-align:start"> 
      <div style="text-align:start"> 
       <div style="text-align:start"> 
        <h4 style="margin-left:0; margin-right:0; text-align:start">新增特性</h4> 
        <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
         <li><span style="background-color:#ffffff; color:#40485b">feat: 动态正向代理来源信息 (</span><a href="https://gitee.com/dromara/forest/issues/I4SYM1">#I4SYM1:动态正向代理来源信息</a><span style="background-color:#ffffff; color:#40485b">)</span></li> 
        </ul> 
        <h4 style="margin-left:0; margin-right:0; text-align:start">修复问题</h4> 
        <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
         <li> <p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">fix: 异常：The file of SSL KeyStore is empty (<a href="https://gitee.com/dromara/forest/issues/I4SYGB">#I4SYGB:异常：The file of SSL KeyStore is empty</a>)</p> </li> 
         <li> <p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">fix: maxRetryInterval配置失效 (<a href="https://gitee.com/dromara/forest/issues/I4SV2P">#I4SV2P:maxRetryInterval配置失效</a>)</p> </li> 
         <li> <p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">fix: 主项目没有依赖lang3会报错的问题 (<a href="https://gitee.com/dromara/forest/issues/I4M9DE">#I4M9DE:主项目没有依赖lang3会报错的问题</a>)</p> </li> 
         <li> <p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">fix: 组合注解未生效 (<a href="https://gitee.com/dromara/forest/issues/I4N2HC">#I4N2HC:组合注解未生效</a>)</p> </li> 
        </ul> 
        <h4 style="margin-left:0; margin-right:0; text-align:start">其它更新</h4> 
        <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
         <li>refactor: 去掉 NameUtils 工具类中重复的if分支</li> 
        </ul> 
        <h2 style="margin-left:0; margin-right:0; text-align:start">特别鸣谢</h2> 
        <p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">本次更新有<span> </span><a href="https://gitee.com/chming">@chming</a> 参与贡献，万分感谢！</p> 
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
            