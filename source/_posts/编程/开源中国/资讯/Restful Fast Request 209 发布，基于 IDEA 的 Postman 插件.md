
---
title: 'Restful Fast Request 2.0.9 发布，基于 IDEA 的 Postman 插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg'
author: 开源中国
comments: false
date: Tue, 14 Dec 2021 08:34:00 GMT
thumbnail: 'https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="margin-left:0; margin-right:0; text-align:left">简介</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com" target="_blank"><img alt height="80" src="https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg" width="80" referrerpolicy="no-referrer"></a><a href="https://gitee.com/kings/fast-request" target="_blank"><img alt height="80" src="https://resources.jetbrains.com/storage/products/company/brand/logos/IntelliJ_IDEA_icon.svg" width="80" referrerpolicy="no-referrer"> <img alt src="https://gitee.com/kings/fast-request/widgets/widget_3.svg" referrerpolicy="no-referrer"></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.jetbrains.com%2Fplugin%2F16988-fast-request" target="_blank">Restful Fast Request</a><span> </span>是一个强大的 restful api 工具包插件(Http Client)，可以根据已有的方法帮助您快速生成 url和 params。Restful Fast Request = API 调试工具+API 管理工具，它有一个漂亮的界面来完成请求、检查服务器响应、存储你的 api 请求和导出 api 请求，同时基于 idea 原生，调试代码更加快速、方便、简捷。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支持 Spring 体系 (Spring MVC / Spring Boot)</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支持JAX-RS</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong>对标及优势</strong></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">对比与 HTTP Client，Restful Fast Request不仅拥有 HTTP Client 内置的功能，还提供了友好易懂直观的界面，让使用者调试 API 的时候能够更加方便、简捷，同时各种类型参数也提供了不同的定制方式，更加灵活。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong>宗旨</strong></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#2c3e50">插件的宗旨是为</span><span style="color:#16a085"><span style="background-color:#ffffff"><strong>简化开发、提高效率</strong></span></span><span style="background-color:#ffffff; color:#2c3e50">而生，</span>我们的愿景是<span style="color:#c0392b"><strong>成为 IDEA 最好的搭档</strong></span>，就像魂斗罗中的 1P、2P，<span style="color:#c0392b"><strong>基友</strong></span>搭配，效率翻倍。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Restful Fast Request 2.0.9正式发布,具体更新内容如下：</h3> 
<ul> 
 <li>2021.3+版本修复"Slow operations are prohibited on EDT"</li> 
 <li>修复快速从response添加Headers</li> 
 <li>添加项目级别的配置,切换项目env和project不受变化</li> 
 <li>文本编辑器添加了快捷格式化按钮</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">从response添加Headers</h3> 
<pre style="margin-left:.85rem; margin-right:.85rem; text-align:left"><code>如果你的api需要再header里面塞入token,你可以像这样子从响应里面快速加参数塞入headers

1.访问登录接口
2.从登录接口响应中加需要加入headers的token信息通过点击+快如加入headers</code></pre> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9fbe66e866b8067d975cdb214f819e9a426.gif" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">文本编辑器添加了快捷格式化按钮</h3> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5fcb4a262924266b001215c1f374b8cab68.gif" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<h1 style="margin-left:0px; margin-right:0px; text-align:left"><span style="color:#e74c3c">投票支持</span></h1> 
<p><span style="color:#c0392b">《2021优秀开源软件投票》支持已经开启，Fast Request本是个人为了方便调试API所开发，后面觉得好用便开源，目前是单人开发，开源不易，如果各位develop觉得好用请一定要为Fast Request投票，谢谢</span><br> 投票地址：<a href="https://www.oschina.net/project/top_cn_2021/?id=589">https://www.oschina.net/project/top_cn_2021/?id=589</a></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>点击链接即可到达投票界面</strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"> </p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">文档</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://kings.gitee.io/restful-fast-request-doc/">https://kings.gitee.io/restful-fast-request-doc/</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">关于开源</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">欢迎各路好汉一起来参与完善 Restful Fast Request，我们期待你的 PR！</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>贡献代码：代码地址<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkings1990%2Ffast-request" target="_blank">Github</a><span> </span>|<span><span> </span></span><a href="https://gitee.com/kings/fast-request">Gitee</a>，欢迎提交 Issue 或者 Pull Requests</li> 
 <li>维护文档：文档地址<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkings1990%2Ffast-request%2Fdocs" target="_blank">Document</a>，欢迎参与翻译和修订</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">下载及安装</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.网页端 :<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.jetbrains.com%2Fplugin%2F16988-fast-request" target="_blank">https://plugins.jetbrains.com/plugin/16988-fast-request</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.IDEA插件市场:打开setting->plugins->Marketplace  搜索 Fast Request</p>
                                        </div>
                                      
</div>
            