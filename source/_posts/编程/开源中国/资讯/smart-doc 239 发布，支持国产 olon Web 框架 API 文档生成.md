
---
title: 'smart-doc 2.3.9 发布，支持国产 olon Web 框架 API 文档生成'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2020/1221/094844_KE7c_2720166.png'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 09:48:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2020/1221/094844_KE7c_2720166.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">smart-doc 是一款同时支持 java restful api 和 Apache Dubbo rpc 接口文档生成的工具，smart-doc 颠覆了传统类似 swagger 这种大量采用注解侵入来生成文档的实现方法。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">smart-doc 完全基于接口源码分析来生成接口文档，完全做到零注解侵入，你只需要按照 java 标准注释编写，smart-doc 就能帮你生成一个简易明了的 markdown 或是一个像 GitBook 样式的静态 html 文档。如果你已经厌倦了 swagger 等文档工具的无数注解和强侵入污染，那请拥抱 smart-doc 吧！</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">功能特性</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>支持接口 debug。</li> 
 <li>零注解、零学习成本、只需要写标准 java 注释。</li> 
 <li>基于源代码接口定义自动推导，强大的返回结构推导。</li> 
 <li>支持 Spring MVC,Spring Boot,Spring Boot Web Flux(controller 书写方式),JAX-RS规范。</li> 
 <li>支持 Callable,Future,CompletableFuture 等异步接口返回的推导。</li> 
 <li>支持 JavaBean 上的 JSR303 参数校验规范，支持分组验证。</li> 
 <li>对 json 请求参数的接口能够自动生成模拟 json 参数。</li> 
 <li>对一些常用字段定义能够生成有效的模拟值。</li> 
 <li>支持生成 json 返回值示例。</li> 
 <li>支持从项目外部加载源代码来生成字段注释(包括标准规范发布的 jar 包)。</li> 
 <li>支持生成多种格式文档：Markdown、HTML5、Asciidoctor、Postman collection、Open Api 3.0+。</li> 
 <li>轻易实现在 Spring Boot 服务上在线查看静态 HTML5 api 文档。</li> 
 <li>开放文档数据，可自由实现接入文档管理系统。</li> 
</ul> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>一款代码注释检测工具，不写注释的小伙伴逃不过法眼了。</li> 
 <li>插件式快速集成(支持 maven 和 gradle 插件)。</li> 
 <li>支持 Apache Dubbo rpc 文档生成。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Smart-doc 和其他工具的支持</p> 
<table border="1" cellpadding="1" cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:500px; word-break:keep-all; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">功能特性</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">smart-doc</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">swagger</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">代码侵入</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">无</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">注解侵入性严重</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">集成复杂度</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">简单，只需插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">偏复杂</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">插件支持</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">有gradle和maven插件</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">无插件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">openapi规范支持</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">支持openapi 3.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">完全支持openapi的版本</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">CI构建集成</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"> <p style="margin-left:0; margin-right:0">可在ci构建阶段使用</p> <p style="margin-left:0; margin-right:0">maven或者gradle命令</p> <p style="margin-left:0; margin-right:0">启动插件生成文档</p> <p style="margin-left:0; margin-right:0"> </p> </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">不支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">集中化文档中心集成</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"> <p style="margin-left:0; margin-right:0">已经和torna企业级接口文档管理平台对接</p> </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">不支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">维护持续性</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">值得信赖，开源后用户基础多，一直持续维护</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">全球用户多，开源维护值得信赖</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">接口debug</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">2.0.0版本开始已经支持debug，页面比swagger漂亮太多了。</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">支持</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Smart-doc 从 2.0.0 后几乎实现了 swagger ui 的功能，并且比 swagger ui 更简洁大方，也更符合国内开发者的诉求。当然 smart-doc 的功能也已经</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">超过了 swagger 为 java 开发者提供的功能。当然 smart-doc 本身是只支持扫描代码生成 openapi 3.0 的文档的，也可以将生成的 openapi 3.0 文档导入到其他ui中渲染展示。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">更新内容</h1> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>支持推送已过时的接口标记到torna。</li> 
 <li>rpc mock完善。</li> 
 <li>dubbo接口文档支持导出字典。</li> 
 <li>支持国产Solon，<a href="https://gitee.com/noear/solon">https://gitee.com/noear/solon</a></li> 
</ol> 
<h1 style="margin-left:0; margin-right:0; text-align:left">debug 页面效果</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/space/2020/1221/094844_KE7c_2720166.png" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">maven 或 gradle 插件</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">smart-doc 官方为了方便用户快速和无侵入的集成 smart-doc 的文档 api 生成能力，我们开发可相关的 maven 或者 gradle 插件。这里也推荐使用插件的方式来使用 smart-doc。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">https://gitee.com/smart-doc-team/smart-doc-maven-plugin</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong>官方推荐方案</strong></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">smart-doc + <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftorna.cn%2F" target="_blank">Torna</a> 组成行业领先的文档生成和管理解决方案，使用smart-doc无侵入完成Java源代码分析和提取注释生成API文档，自动将文档推送到Torna企业级接口文档管理平台。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="569" src="https://static.oschina.net/uploads/space/2022/0104/100051_aZiD_3820517.png" width="1405" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsmart-doc-group.github.io%2F%23%2Fzh-cn%2Ftorna%2FtornaIntegration" target="_blank">smart-doc+Torna文档自动化</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">smart-doc在国内很多企业中被用来替换了swagger，甚至是在国内Top 3内的大厂都有smart-doc的二次开发版本。Torna未来的目标是追赶和超越Yapi。smart-doc针对java spring技术栈的解析能力目前为业内最强(不服就拿工具来跑smart-doc的解析demo)。所以<a href="https://gitee.com/smart-doc-team/smart-doc/wikis/smart-doc%E4%B8%8Etorna%E5%AF%B9%E6%8E%A5?sort_id=3695028">smart-doc+Torna</a>的方案威力巨大，Torna目前处于高速迭代期，欢迎体验Torna，我们努力为社区提供高效好用的接口文档解决方案。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">升级建议</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> smart-doc 可基于以前的版本平滑升级，建议升级。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">DEMO</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/smart-doc-team/smart-doc-example-cn" target="_blank">使用demo</a>轻松玩转接口文档生成，其他用户案例文档效果展示：https://api.doubans.com/</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">知名用户</h1> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>科大讯飞</li> 
 <li>一加</li> 
 <li>小米</li> 
 <li>马蜂窝</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在今年2021年8月 smart-doc 也新增了一些外海的用户。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>非常感谢Solon作者在smart-doc上提供Solon支持的pr。</strong></p>
                                        </div>
                                      
</div>
            