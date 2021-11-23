
---
title: 'Restful Fast Request 2.0.7 发布，基于 IDEA 的 Postman 插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg'
author: 开源中国
comments: false
date: Tue, 23 Nov 2021 08:38:00 GMT
thumbnail: 'https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="margin-left:0; margin-right:0; text-align:left">简介</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com" target="_blank"><img alt height="80" src="https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg" width="80" referrerpolicy="no-referrer"></a><a href="https://gitee.com/kings/fast-request" target="_blank"><img alt height="80" src="https://resources.jetbrains.com/storage/products/company/brand/logos/IntelliJ_IDEA_icon.svg" width="80" referrerpolicy="no-referrer"> <img alt src="https://gitee.com/kings/fast-request/widgets/widget_3.svg" referrerpolicy="no-referrer"></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.jetbrains.com%2Fplugin%2F16988-fast-request" target="_blank">Restful Fast Request</a><span> </span>是一个强大的restful api工具包插件(Http Client)，可以根据已有的方法帮助您快速生成url和params。Restful Fast Request = API调试工具+API管理工具，它有一个漂亮的界面来完成请求、检查服务器响应、存储你的api请求和导出api请求，同时基于idea原生，调试代码更加快速、方便、简捷。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支持 Spring 体系 (Spring MVC / Spring Boot)</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong>对标及优势</strong></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">对比与HTTP Client，Restful Fast Request不仅拥有HTTP Client内置的功能，还提供了友好易懂直观的界面，让使用者调试API的时候能够更加方便、简捷，同时各种类型参数也提供了不同的定制方式，更加灵活。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong>宗旨</strong></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#2c3e50">插件的宗旨是为</span><span style="color:#16a085"><span style="background-color:#ffffff"><strong>简化开发、提高效率</strong></span></span><span style="background-color:#ffffff; color:#2c3e50">而生，</span>我们的愿景是<span style="color:#c0392b"><strong>成为 IDEA 最好的搭档</strong></span>，就像魂斗罗中的 1P、2P，<span style="color:#c0392b"><strong>基友</strong></span>搭配，效率翻倍。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Restful Fast Request 2.0.7正式发布,具体更新内容如下：</h3> 
<ul> 
 <li style="text-align:left">添加API导航树</li> 
 <li style="text-align:left">添加Headers随项目和环境切换自动切换的支持</li> 
 <li style="text-align:left"><span style="color:#e74c3c">优化windows系统某些情况下下载文件无法弹出目录</span></li> 
 <li style="text-align:left">优化@RequestParam的参数解析</li> 
 <li style="text-align:left">优化工具窗口project和env下拉组件及布局</li> 
 <li style="text-align:left">curl拷贝提示优化</li> 
 <li style="text-align:left">regenerate提示优化</li> 
 <li style="text-align:left">删除project和env配置增加确认操作</li> 
 <li style="text-align:left">修复json字段输出循序被打乱</li> 
 <li style="text-align:left">将发送请求按钮至工具栏同时支持快捷键</li> 
</ul> 
<h3>API导航树</h3> 
<pre><span style="color:#808080">选中树输入关键字,再按回车或者鼠标左键双击即可定位到API
</span>
<span style="color:#808080">悬浮鼠标显示api的doc</span>
</pre> 
<p><img align="left" alt height="744" src="https://oscimg.oschina.net/oscnet/up-4bc0c760c53e9416b7c7735024d884c4355.gif" width="1425" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<h3>Headers自动切换</h3> 
<pre><span style="color:#808080">场景:SpringBoot等多模块项目不同项目、不同环境下头参数不同,为了快速自动切换headers,引入了header分组
</span><span style="color:#808080">操作方式：
</span><span style="color:#808080">1.在headers group里修改约束:输入的值必须是标准json格式
</span><span style="color:#808080">2.直接切换环境,然后再headers表格中输入对应的key、value值</span></pre> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9a772e3dfa343766b3346c37d02da6dbfbc.gif" width="1425" referrerpolicy="no-referrer"></p> 
<p> </p> 
<h3>将发送请求按钮至工具栏同时支持快捷键</h3> 
<pre><span style="color:#808080">send request: alt =
</span><span style="color:#808080">send and download: alt -
</span><span style="color:#808080">前提条件:工具窗口需要被聚焦</span>
</pre> 
<p><img height="818" src="https://oscimg.oschina.net/oscnet/up-fbc0986d8a4ea86c23505f3090f30056a87.png" width="1262" referrerpolicy="no-referrer"></p> 
<h3>优化工具窗口project和env下拉组件及布局</h3> 
<p>界面布局极简优化</p> 
<pre><span style="color:#808080">图标p代表project
</span><span style="color:#808080">图标e代表environment  </span>
</pre> 
<p><img height="684" src="https://oscimg.oschina.net/oscnet/up-c01238da49ce5f0013f0f2c01f81339ffb2.png" width="1264" referrerpolicy="no-referrer"></p> 
<p><img height="612" src="https://oscimg.oschina.net/oscnet/up-03e7139d8b84000f1e974985917f182279f.png" width="1260" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">文档</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://kings.gitee.io/restful-fast-request-doc/">https://kings.gitee.io/restful-fast-request-doc/</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">关于开源</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">欢迎各路好汉一起来参与完善 Restful Fast Request，我们期待你的 PR！</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>贡献代码：代码地址<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkings1990%2Ffast-request" target="_blank">Github</a><span> </span>|<span><span> </span></span><a href="https://gitee.com/kings/fast-request">Gitee</a>，欢迎提交 Issue 或者 Pull Requests</li> 
 <li>维护文档：文档地址<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkings1990%2Frestful-fast-request-doc" target="_blank">Document</a>，欢迎参与翻译和修订</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">下载及安装</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.网页端:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.jetbrains.com%2Fplugin%2F16988-fast-request" target="_blank">https://plugins.jetbrains.com/plugin/16988-fast-request</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.IDEA插件市场:打开setting->plugins->Marketplace 搜索Fast Request</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3.idea版本:建议升级到2020.3+(不用担心入狱，<a href="https://gitee.com/pengzhile/ide-eval-resetter">idea无限试用</a>)</p>
                                        </div>
                                      
</div>
            