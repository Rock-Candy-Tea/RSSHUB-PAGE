
---
title: '声明式 HTTP 框架 Forest v1.5.21 发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e095709750cf803e835235b2f549ef278f6.png'
author: 开源中国
comments: false
date: Fri, 20 May 2022 07:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e095709750cf803e835235b2f549ef278f6.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="248" src="https://oscimg.oschina.net/oscnet/up-e095709750cf803e835235b2f549ef278f6.png" width="400" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>Forest 介绍</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 是一个开源的 Java HTTP 客户端框架，它能够将 HTTP 的所有请求信息（包括 URL、Header 以及 Body 等信息）绑定到您自定义的 Interface 方法上，能够通过调用本地接口方法的方式发送 HTTP 请求</p> 
<h4 style="margin-left:0px; margin-right:0px; text-align:left"><strong style="color:#333333">在 Gitee 上现已超过 2.4k star</strong></h4> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 如何使用</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 不需要您编写具体的 HTTP 调用过程，只需要您定义一个接口，然后通过 Forest 注解将 HTTP 请求的信息添加到接口的方法上即可。请求发送方通过调用您定义的接口便能自动发送请求和接受请求的响应</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 的工作原理</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 会将您定义好的接口通过动态代理的方式生成一个具体的实现类，然后组织、验证 HTTP 请求信息，绑定动态数据，转换数据形式，SSL 验证签名，调用后端 HTTP API (httpclient 等 API) 执行实际请求，等待响应，失败重试，转换响应数据到 Java 类型等脏活累活都由这动态代理的实现类给包了。 请求发送方调用这个接口时，实际上就是在调用这个干脏活累活的实现类</p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:left">重点更新内容</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">此次版本发布主要解决了URL在某些情况下的解析错误问题，以及对字符串模板进行手动URLEncode的支持</p> 
<div style="text-align:left"> 
 <div> 
  <p style="margin-left:0em; margin-right:0em">任何包含特殊字符的URL地址或Body中的表单信息要发送请求，都要进过一定程度的UREncode以符合HTTP相关标准，才能正常发出请求</p> 
  <p style="margin-left:0; margin-right:0">而HTTP请求中的不同部分对URLEncode强度要求是不同的，比如Body表单格式字符串的要求相对宽松，可以包含<code>&#123;</code>,<code>&#125;</code>,<code>空格</code>等字符串，而Query参数值部分则必须将其转义才能正常发送</p> 
  <p style="margin-left:0; margin-right:0">所以Forest在默认情况下为HTTP请求已经URL中的不同部分提供了各自合适的编码强度（最大限度宽松）的 URLEncode</p> 
  <p style="margin-left:0; margin-right:0">但有些情况默认的URLEncode也无法满足要求：</p> 
  <ol> 
   <li>不同服务端接口对编码的强度要求可能是不同的，比如要求Query参数必须是最严格的编码</li> 
   <li>已经如果在URL中大范围使用<span> </span><code>$&#123;变量名&#125;</code><span> </span>这样变量引用的时候，Forest也无法准备判断您引入的变量是URL中具体那个部分，从而也无法给出准确的编码强度</li> 
   <li>输入一个有歧义的字符串到字符串模板中</li> 
  </ol> 
  <p style="margin-left:0; margin-right:0">所以此时需要进行手动URLEncode，为此提供了在字符串模板中可供调用的内置函数:</p> 
  <ul> 
   <li><code>encode(str)</code>: 严格编码，最大的编码强度</li> 
   <li><code>encodeQuery(str)</code>: Query参数编码，对URL中的参数值部分字符串进行编码，强度适中以最大限度适应HTTP规范</li> 
   <li><code>encodePath(str)</code>: Path路径编码，对URL中域名+后端+<code>/</code><span> </span>后的路径部分字符串进行编码</li> 
   <li><code>encodeForm(str)</code>: Form表单编码，对Body中<code>x-www-form-urlencoded</code>格式的请求体字符串进行编码，强度最宽松</li> 
   <li><code>encodeUserInfo(str)</code>: UserInfo编码，对URL中用户名密码验证信息部分字符串进行编码</li> 
  </ul> 
  <p style="margin-left:0; margin-right:0">例子:</p> 
  <div> 
   <pre><code><em><em>// 在&#123;&#125;中调用encode函数对userInfo变量进行严格URLEncode编码</em></em>
<span><span>@Get</span></span>(<span style="color:#dd1144"><span style="color:#dd1144">"http://&#123;encode(userInfo)&#125;@localhost:8080/hello/user"</span></span>)
<span><span>ForestResponse<String> </span><strong style="color:#990000"><span><strong style="color:#990000">doGet</strong></span></strong><span><span><span>(@Var(</span></span><span style="color:#dd1144"><span><span><span style="color:#dd1144">"userInfo"</span></span></span></span><span><span>)</span></span></span><span> String userInfo)</span></span>;
</code></pre> 
   <div style="text-align:center">
     
   </div> 
  </div> 
  <p style="margin-left:0; margin-right:0">若调用该接口参数如下:</p> 
  <div> 
   <pre><code>client.doGet(<span style="color:#dd1144"><span style="color:#dd1144">"xxx/yyy/foo"</span></span>);
</code></pre> 
   <div style="text-align:center">
     
   </div> 
  </div> 
  <p style="margin-left:0; margin-right:0">则产生的请求为:</p> 
  <div> 
   <pre><code><strong style="color:#333333"><strong style="color:#333333">GET</strong></strong> <span><span>http://xxx%2Fyyy%2Ffoo</span><span style="color:#008080"><span><span style="color:#008080">@localhost</span></span></span><span>:8080/hello/user</span></span> HTTP
</code></pre> 
   <div style="text-align:center">
     
   </div> 
  </div> 
  <p style="margin-left:0; margin-right:0">如若不用<span> </span><code>encode</code><span> </span>函数的话，则请求会变成</p> 
  <div> 
   <pre><code><strong style="color:#333333"><strong style="color:#333333">GET</strong></strong> <span><span>http://xxx/yyy/foo</span><span style="color:#008080"><span><span style="color:#008080">@localhost</span></span></span><span>:8080/hello/user</span></span> HTTP
</code></pre> 
   <div style="text-align:center">
     
   </div> 
  </div> 
  <p style="margin-left:0em; margin-right:0em">此时<code>xxx/yyy/xxx</code>中的<code>/</code>会使地址产生歧义，将<code>xxx</code>错误地解析为域名，显然这样的地址是无法正常发送出去的</p> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <p> </p> 
  </div> 
 </div> 
</div> 
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
         <ul> 
          <li>feat: 字符串模板支持手动URLEncode (<a href="https://gitee.com/dromara/forest/issues/I58D1C">#I58D1C:字符串模板支持手动URLEncode</a>)</li> 
         </ul> 
         <h4 style="margin-left:0; margin-right:0">修复的问题:</h4> 
         <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
          <li>fix: url在某些场景下的解析错误 (<a href="https://gitee.com/dromara/forest/issues/I56XDM">#I56XDM:url在某些场景下的解析错误</a>)</li> 
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
            