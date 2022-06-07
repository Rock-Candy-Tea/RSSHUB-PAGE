
---
title: 'vue-rap 2.1.0 发布了，第一个免编译的 vue 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7766'
author: 开源中国
comments: false
date: Tue, 07 Jun 2022 13:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7766'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0; margin-right:0; text-align:start">概述</h3> 
<hr> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">Vue-rap 可以在不使用大量前端工具(如npm,webpack,Browserify等)的情况下快速构建基于 Vue的秒速打开边用边下载的流应用(单页面应用);</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">优点</h3> 
<hr> 
<ul style="margin-left:0; margin-right:0"> 
 <li>依赖小(只需要引用 vue 就可以了),学习成本低,上手快</li> 
 <li>vue-rap拥有类似 .vue 的单页面组件;</li> 
 <li>vue-rap拥有可以方便使用的路由系统,路由秉承约定大约配置,可以快速路由,无限拓展;</li> 
 <li>vue-rap拥有强大的缓存机制,应用支持秒级打开,边使用边下载,可以使用 vue-rap 构建流应用;</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">最新更新</h3> 
<hr> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">修改指令 v-link为 v-jump<br> Rap.go 和 Rap.replace 方法修改为 Rap.navigateTo 和 Rap.redirectTo<br> 防止加载 .js 文件产生缓存</p> 
<hr> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">路由支持 history 和 hash 模式<br> Rap.define 支持定义,和导入模块<br> 添加Rap.require方法<br> 缓存存放到 indexedDb里 如果不支持会向下降级<br> 支持 keep ,能做到列表进详情,后退后列表位置不变<br> 添加 Rap.showPopup 弹框<br> 支持判定环境 android,ios 微信等<br> 支持自定义路由别名 Rap.router</p> 
<h3>Ly-Admin-UI内部基于 vue-rap的后台管理前端组件库也开源了</h3> 
<p>开源地址:https://gitee.com/tengzhinei/ly-admin-ui</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">ly-admin-ui为公司内部使用多年的前端组件库,已陆续更新 3 年多，它基于 vue + element-ui+vue-rap 技术栈。 它使用了最新的前端技术栈，项目在element-ui基础上又添加了超多实用组件和布局; 项目整体使用了最新的vue-rap流应用技术,项目可以不需要构建的情况下直接部署,边使用边下载。</p> 
<ul> 
 <li>演示地址<span> </span><a href="https://gitee.com/link?target=http%3A%2F%2Flyadminui.magcloud.net%2F">http://lyadminui.magcloud.net/</a></li> 
 <li>登录地址<span> </span><a href="https://gitee.com/link?target=http%3A%2F%2Flyadminui.magcloud.net%2Fportal%2Flogin">http://lyadminui.magcloud.net/portal/login</a></li> 
 <li>文档地址<span> </span><a href="https://gitee.com/link?target=http%3A%2F%2Flyadminui.magcloud.net%2F">http://lyadminui.magcloud.net/</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">特色功能组件</h3> 
<ul> 
 <li>N种主布局只有搭配</li> 
 <li>支持菜单,配置项,文档搜索的全局搜索能力</li> 
 <li>支持拖动验证,文字点选等多种行为验证方式</li> 
 <li>好看的操作指引</li> 
 <li>支持drop,剪贴板等使用简单的文件上传</li> 
 <li>懒加载方式的弹出框,不需要将弹出框内的代码写到当前页面</li> 
 <li>一行代码的图表展示</li> 
 <li>超级强大的 table 组件和 table 相关的组件</li> 
 <li>完备的权限验证能力</li> 
 <li>还有很多,太多了...</li> 
</ul> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            