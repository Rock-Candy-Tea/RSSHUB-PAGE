
---
title: 'AJ-Report V0.9.2 发布，分享功能它来了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-afe6a9a4d28bb9cfd6557019a920113ba43.gif'
author: 开源中国
comments: false
date: Fri, 20 Aug 2021 15:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-afe6a9a4d28bb9cfd6557019a920113ba43.gif'
---

<div>   
<div class="content">
                                                                                            <p><em>AJ-Report V0.9.2已发布。</em></p> 
<p><strong><a href="https://gitee.com/anji-plus/report/releases/V0.9.2">V0.9.2</a>版本更新详情：</strong></p> 
<ol> 
 <li>新增大屏分享功能</li> 
 <li>大屏图表动态数据集支持数据集</li> 
 <li>大屏图表动态数据集字典进行分类管理</li> 
 <li>文件管理上传问题</li> 
 <li>文件管理添加复制url功能</li> 
 <li>优化数据集清洗功能</li> 
 <li>新增图表：堆叠图</li> 
</ol> 
<p><strong>近期计划：</strong></p> 
<ol> 
 <li>表格存在的问题，进行优化</li> 
 <li>编辑大屏数据集回显问题</li> 
 <li>大屏宽高动态适配问题</li> 
 <li>大屏导入导出功能</li> 
 <li>整体样式调整、优化</li> 
</ol> 
<p><span style="background-color:#ffffff; color:#40485b">AJ-Report由 </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.anji-plus.com%2F" target="_blank">安吉加加</a><span style="background-color:#ffffff; color:#40485b"> 开源的一个BI平台，酷炫大屏展示，能随时随地掌控业务动态，让每个决策都有数据支撑。</span></p> 
<p><span style="background-color:#ffffff; color:#40485b">多数据源支持，内置mysql、elasticsearch、kudu驱动，支持自定义数据集省去数据接口开发，支持17种大屏组件，不会开发，照着设计稿也可以制作大屏。</span></p> 
<p><span style="background-color:#ffffff; color:#40485b">三步轻松完成大屏设计：配置数据源---->写SQL配置数据集---->拖拽配置大屏---->保存发布。欢迎体验。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-afe6a9a4d28bb9cfd6557019a920113ba43.gif" referrerpolicy="no-referrer"></p> 
<p><strong>数据流程图</strong></p> 
<p><strong><img alt height="473" src="https://oscimg.oschina.net/oscnet/up-015ed57c8358d28f9f242ef88c9a519273c.png" width="757" referrerpolicy="no-referrer"></strong></p> 
<p><strong>核心技术</strong></p> 
<p>后端</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-boot%2F" target="_blank">Spring Boot 2.3.5.RELEASE</a>：Spring Boot是一款开箱即用框架，让我们的Spring应用变的更轻量化、更快的入门。 在主程序执行main函数就可以运行。你也可以打包你的应用为jar并通过使用java -jar来运行你的Web应用；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.baomidou.com%2F" target="_blank">Mybatis-plus3.3.2</a>：MyBatis-plus（简称 MP）是一个 MyBatis (opens new window) 的增强工具。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fflywaydb.org" target="_blank">flyway5.2.1</a>：MyBatis-plus（简称 MP）是一个 MyBatis (opens new window) 的增强工具。</li> 
</ul> 
<p>前端</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.npmjs.com%2F" target="_blank">npm</a>：node.js的包管理工具，用于统一管理我们前端项目中需要用到的包、插件、工具、命令等，便于开发和维护。。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwebpack.docschina.org%2F" target="_blank">webpack</a>：用于现代 JavaScript 应用程序的_静态模块打包工具。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fes6.ruanyifeng.com%2F" target="_blank">ES6</a>：Javascript的新版本，ECMAScript6的简称。利用ES6我们可以简化我们的JS代码，同时利用其提供的强大功能来快速实现JS逻辑。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcli.vuejs.org%2F" target="_blank">vue-cli</a>：Vue的脚手架工具，用于自动生成Vue项目的目录及文件。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frouter.vuejs.org%2F" target="_blank">vue-router</a>：Vue提供的前端路由工具，利用其我们实现页面的路由控制，局部刷新及按需加载，构建单页应用，实现前后端分离。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN" target="_blank">element-ui</a>：基于MVVM框架Vue开源出来的一套前端ui组件。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.avuejs.com%2F" target="_blank">avue</a>：用该组件包裹后可以变成拖拽组件,采用相对于父类绝对定位;用键盘的上下左右也可以控制移动。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvue-echartsg" target="_blank">vue-echarts</a>：vue-echarts是封装后的vue插件,基于 ECharts v4.0.1+ 开发。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvue-super-slider%2F" target="_blank">vue-superslide</a>：Vue-SuperSlide(Github) 是 SuperSlide 的 Vue 封装版本。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSortableJS%2FVue.Draggable%2F" target="_blank">vuedraggable</a>：是一款基于Sortable.js实现的vue拖拽插件。</li> 
</ul> 
<p><strong>在线体验</strong></p> 
<ul> 
 <li> 电脑在线体验: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freport.anji-plus.com%2Findex.html" target="_blank">https://report.anji-plus.com/index.html</a>  体验账号：guest  密码：guest</li> 
 <li> 在线文档: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freport.anji-plus.com%2Freport-doc%2F" target="_blank">https://report.anji-plus.com/report-doc/</a></li> 
 <li> 在线提问: <a href="https://gitee.com/anji-plus/report/issues">https://gitee.com/anji-plus/report/issues</a></li> 
</ul>
                                        </div>
                                      
</div>
            