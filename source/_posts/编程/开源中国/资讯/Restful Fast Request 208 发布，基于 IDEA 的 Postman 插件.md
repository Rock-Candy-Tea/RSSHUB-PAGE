
---
title: 'Restful Fast Request 2.0.8 发布，基于 IDEA 的 Postman 插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg'
author: 开源中国
comments: false
date: Tue, 07 Dec 2021 09:30:00 GMT
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
<h3 style="margin-left:0; margin-right:0; text-align:left">Restful Fast Request 2.0.8.1 正式发布,具体更新内容如下：</h3> 
<ul> 
 <li>修复初次添加项目或环境npe</li> 
 <li>json树响应字符渲染最大限制</li> 
 <li>添加Api navigate对methodType的支持</li> 
 <li>添加对忽略参数解析的支持</li> 
 <li>线程导致的EDT问题</li> 
 <li>send/sendDownload支持自定义快捷键</li> 
 <li>修复2021.3响应不显示</li> 
 <li>修复searchEveryWhere冲突警告</li> 
 <li>调整低版本idea工具栏操作按钮至工具栏顶部位置</li> 
 <li>移除多余依赖,插件从11.1M降至5.9M</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">send/sendDownload支持自定义快捷键</h3> 
<pre style="margin-left:.85rem; margin-right:.85rem; text-align:left"><code>快捷键在任意位置点击均可触发,不再需要聚焦到工具窗口
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="1126" src="https://oscimg.oschina.net/oscnet/up-e57045b930348760c68d09c0da476cd5acb.png" width="1468" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">添加Api navigate对methodType的支持</h3> 
<p><img height="768" src="https://oscimg.oschina.net/oscnet/up-7c387a8435d05eb7d56df77056a0e7f38fd.png" width="856" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c">支持</span></h2> 
<p><strong>2021开源软件投票支持已经开启，如果您觉得本软件对您的开发提效了许多，希望您帮忙投上宝贵的一票</strong></p> 
<p><strong>地址：<a href="https://www.oschina.net/project/top_cn_2021">https://www.oschina.net/project/top_cn_2021</a></strong></p> 
<p><strong>右上角搜索输入框输入 fast request</strong></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">文档</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://kings.gitee.io/restful-fast-request-doc/">https://kings.gitee.io/restful-fast-request-doc/</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">关于开源</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">欢迎各路好汉一起来参与完善 Restful Fast Request，我们期待你的 PR！</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>贡献代码：代码地址<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkings1990%2Ffast-request" target="_blank">Github</a><span> </span>|<span><span> </span></span><a href="https://gitee.com/kings/fast-request">Gitee</a>，欢迎提交 Issue 或者 Pull Requests</li> 
 <li>维护文档：文档地址<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkings1990%2Frestful-fast-request-doc" target="_blank">Document</a>，欢迎参与翻译和修订</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">下载及安装</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.网页端 :<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.jetbrains.com%2Fplugin%2F16988-fast-request" target="_blank">https://plugins.jetbrains.com/plugin/16988-fast-request</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.IDEA插件市场:打开setting->plugins->Marketplace 搜索Fast Request</p> 
<p> </p>
                                        </div>
                                      
</div>
            