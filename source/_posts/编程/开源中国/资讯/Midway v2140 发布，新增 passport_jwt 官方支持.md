
---
title: 'Midway v2.14.0 发布，新增 passport_jwt 官方支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8855'
author: 开源中国
comments: false
date: Mon, 06 Dec 2021 14:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8855'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <div> 
  <div> 
   <div> 
    <div> 
     <div> 
      <p style="margin-left:0; margin-right:0"><span>正式发版节奏将于 12.12 之后回归。</span></p> 
      <h2 style="margin-left:0; margin-right:0"><span>Features</span></h2> 
      <h3 style="margin-left:0; margin-right:0"><span>1、支持 passport 和 jwt</span></h3> 
      <p style="margin-left:0; margin-right:0"><span>感谢社区 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNawbc" target="_blank"><span>@Nawbc</span></a><span> 提供 passport 和 jwt 组件。</span></p> 
      <p style="margin-left:0; margin-right:0"><span>身份验证是大多数 Web 应用程序的重要组成部分，Passport 也是现今 Node.js 中较为流行的鉴权验证库。</span></p> 
      <p style="margin-left:0; margin-right:0"><span>Passport 通过策略的可扩展插件进行身份验证请求，同时通过中间件的方式来接入全局或者特定的路由，这最大限度地提高了灵活性并允许开发人员做出应用程序级别的决策。</span></p> 
      <p style="margin-left:0; margin-right:0"><span>可以访问 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmidwayjs.org%2Fdocs%2Fpassport" target="_blank"><span>https://midwayjs.org/docs/passport</span></a><span> 来查看如何使用。</span></p> 
      <h3 style="margin-left:0; margin-right:0"><span>2、validate 增加自定义错误状态码</span></h3> 
      <p style="margin-left:0; margin-right:0"><span>感谢社区 @</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fghostoy" target="_blank"><span>ghostoy</span></a><span> 提供该 PR。</span></p> 
      <p style="margin-left:0; margin-right:0"><span>现在你可以通过 @Validate 装饰器的参数来修改 http 返回的状态码。</span></p> 
      <p style="margin-left:0; margin-right:0"><span>同时在 v3 版本，我们提供了全局的错误码配置，校验失败，默认返回码将变为 422。</span></p> 
      <h2 style="margin-left:0; margin-right:0"><span>Bugfix</span></h2> 
      <h3 style="margin-left:0; margin-right:0"><span>1、express 路由中间件作用域的问题</span></h3> 
      <p style="margin-left:0; margin-right:0"><span>之前的版本，单个路由中间件配置后，整个 controller 下的路由都会被生效，新版本修复了该问题。</span></p> 
      <h3 style="margin-left:0; margin-right:0"><span>2、移除 redis 的 db/username/password 检查选项</span></h3> 
      <p style="margin-left:0; margin-right:0"><span>和用户，ioredis作者核对之后，原有的 db/username/password 选项为可选参数，不应该提供必选校验，新版本中已移除。</span></p> 
      <h3 style="margin-left:0; margin-right:0"><span>3、修复 mongoose/typegoose 中无法使用异步配置覆盖的问题</span></h3> 
      <p style="margin-left:0; margin-right:0"><span>原有的 mongoose 初始化服务生命周期过于提前，导致使用 onConfigLoad 的方式无法正确的覆盖配置，导致初始化错误的实例。</span></p> 
      <p style="margin-left:0; margin-right:0"><span>新版本调整了这一时机，使得异步配置覆盖正确。</span></p> 
      <p style="margin-left:0; margin-right:0"><span>感谢 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdeveloperyvan" target="_blank"><span>@developeryvan</span></a><span> 发现此问题并提供 3.x 的 PR。</span></p> 
      <h3 style="margin-left:0; margin-right:0"><span>4、修复多连接下 @EntityView 装饰器无法判断 connectionName 的问题 </span></h3> 
      <p style="margin-left:0; margin-right:0"><span>之前的版本，@EntityView 漏了多实例的支持，新版本补回。</span></p> 
      <h3 style="margin-left:0; margin-right:0"><span>5、修复在特定场景下的路由排序的问题</span></h3> 
      <p style="margin-left:0; margin-right:0"><span>有用户提出，在某些路由下，排序出现了错误，新版本进行了修复处理。</span></p> 
      <pre>'/detail/:id.html'
'/:typeid/:area/'</pre> 
      <p style="margin-left:0; margin-right:0"><span>PS：Midway 3.x 已经发布到 beta.7，欢迎试用反馈。</span></p> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            