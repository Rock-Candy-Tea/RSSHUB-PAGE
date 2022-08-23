
---
title: '芋道 ruoyi-vue-pro v1.6.4 发布：新增 uniapp 管理后台、报表设计器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.iocoder.cn/images/ruoyi-vue-pro/%E7%99%BB%E5%BD%95.jpg?imageView2/2/format/webp/w/1280'
author: 开源中国
comments: false
date: Tue, 23 Aug 2022 08:54:00 GMT
thumbnail: 'https://static.iocoder.cn/images/ruoyi-vue-pro/%E7%99%BB%E5%BD%95.jpg?imageView2/2/format/webp/w/1280'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><span style="background-color:#ffffff">项目地址</span></span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro">https://gitee.com/zhijiantianya/ruoyi-vue-pro</a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>严肃声明：现在、未来都不会有商业版本，所有功能全部开源！</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>拒绝虚假开源，售卖商业版，程序员不骗程序员！！</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>「我喜欢写代码，乐此不疲」</strong><br> <strong>「我喜欢做开源，以此为乐」</strong></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">🐯<span style="color:#e74c3c"><span style="background-color:#ffffff">项目介绍</span></span></h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>芋道</strong>，一套<strong>全部开源</strong>的<strong>企业级</strong>的快速开发平台，毫无保留给个人及企业免费使用。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong style="color:#40485b">芋道</strong><span style="background-color:#ffffff; color:#40485b">，以开发者为中心，打造中国第一流的快速开发平台，</span><span style="color:#e74c3c"><span style="background-color:#ffffff"><strong>全部开源</strong></span></span><span style="background-color:#ffffff; color:#40485b">，</span><span style="color:#e74c3c"><span style="background-color:#ffffff"><u><strong>个人与企业可 100% 免费使用</strong></u></span></span></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">有任何问题，或者想要的功能，可以在<span> </span><em>Issues</em><span> </span>中提给艿艿。</p> 
</blockquote> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>管理后台的 Vue3 版本采用<span> </span><a href="https://gitee.com/kailong110120130/vue-element-plus-admin">vue-element-plus-admin</a><span> </span>，Vue2 版本采用<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FPanJiaChen%2Fvue-element-admin">vue-element-admin</a></li> 
 <li>管理后台的移动端采用<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdcloudio%2Funi-app">uni-app</a><span> </span>方案，一份代码多终端适配，同时支持 APP、小程序、H5！</li> 
 <li>后端采用 Spring Boot、MySQL + MyBatis Plus、Redis + Redisson</li> 
 <li>数据库可使用 MySQL、Oracle、PostgreSQL、SQL Server、MariaDB、国产达梦 DM、TiDB 等</li> 
 <li>权限认证使用 Spring Security & Token & Redis，支持多终端、多种用户的认证系统，支持 SSO 单点登录</li> 
 <li>支持加载动态权限菜单，按钮级别权限控制，本地缓存提升性能</li> 
 <li>支持 SaaS 多租户系统，可自定义每个租户的权限，提供透明化的多租户底层封装</li> 
 <li>工作流使用 Flowable，支持动态表单、在线设计流程、会签 / 或签、多种任务分配方式</li> 
 <li>高效率开发，使用代码生成器可以一键生成前后端代码 + 单元测试 + Swagger 接口文档 + Validator 参数校验</li> 
 <li>集成微信小程序、微信公众号、企业微信、钉钉等三方登陆，集成支付宝、微信等支付与退款</li> 
 <li>集成阿里云、腾讯云、云片等短信渠道，集成 MinIO、阿里云、腾讯云、七牛云等云存储服务</li> 
 <li>集成报表设计器，支持数据报表、图形报表、打印设计等</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">🐶 新手必读</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>演示地址：<a href="https://gitee.com/link?target=http%3A%2F%2Fdashboard.yudao.iocoder.cn">http://dashboard.yudao.iocoder.cn</a></li> 
 <li>启动文档：<a href="https://gitee.com/link?target=https%3A%2F%2Fdoc.iocoder.cn%2Fquick-start%2F">https://doc.iocoder.cn/quick-start/</a></li> 
 <li>视频教程：<a href="https://gitee.com/link?target=https%3A%2F%2Fdoc.iocoder.cn%2Fvideo%2F">https://doc.iocoder.cn/video/</a></li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><span style="background-color:#ffffff">更新说明</span></span></h1> 
<h3 style="text-align:start">📈<span> </span>Statistic</h3> 
<ul> 
 <li>总代码行数：87565</li> 
 <li>源码代码行数：54279</li> 
 <li>注释行数：19868</li> 
 <li>单元测试用例数：671</li> 
</ul> 
<h3 style="text-align:start">⭐<span> </span>New Features</h3> 
<ul> 
 <li>【新增】完善 Vue3 管理后台的工作流实现，由<span> </span><a href="https://gitee.com/xingyu4j">@xingyu4j</a><span> </span>贡献 #238</li> 
 <li>【新增】管理后台的移动端<span> </span><code>yudao-ui-admin-uniapp</code><span> </span>项目，采用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdcloudio%2Funi-app" target="_blank">uni-app</a><span> </span>方案，一份代码多终端适配，同时支持 APP、小程序、H5！<a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/247">#247</a></li> 
 <li>【新增】集成积木报表，提供低代码报表设计器，由<span> </span><a href="https://gitee.com/jiangqiang1996">@jiangqiang1996</a><span> </span>贡献<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/237">#237</a></li> 
 <li>【新增】接入支付宝 PC 网站支付，由<span> </span><a href="https://gitee.com/jiangqiang1996">@jiangqiang1996</a><span> </span>贡献<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/240">#240</a></li> 
 <li>【优化】项目的启动速度，控制在 30 秒左右，默认不启动 bpm、visualization 模块</li> 
 <li>【优化】管理后台的弹窗支持滚动、拖拽，并点击背景布关闭，避免误操作，由<span> </span><a href="https://gitee.com/ycak47">@颗粒</a><span> </span>贡献<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/253">#253</a></li> 
 <li>【优化】一键改包，如果目标目录已存在，则不进行生成，由<span> </span><a href="https://gitee.com/cksspk">@C</a><span> </span>贡献<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/229">#229</a></li> 
</ul> 
<h3 style="text-align:start">🐞<span> </span>Bug Fixes</h3> 
<ul> 
 <li>【修复】Redis 7.0 监控查询 calls 数值超过 Integer 范围的异常，由<span> </span><a href="https://gitee.com/lanyue52011">@lanyue52011</a><span> </span>贡献<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/239">#239</a></li> 
 <li>【修复】前端表单设计器中动态数据，不能正常获取和更深层级的赋值错误的情况，由<span> </span><a href="https://gitee.com/hdzxhl">@CorrectRoadH</a><span> </span>贡献<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/256">#256</a></li> 
 <li>【修复】代码生成功能中，点击同步，会清除已添加并存在的字段，由<span> </span><a href="https://gitee.com/xiruicode">@xrcoder</a><span> </span>贡献<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/249/">#249</a></li> 
 <li>【修复】工作流与积木报表的依赖冲突，将 xercesImpl 升级到<span> </span><code>2.12.0</code><span> </span>版本，由<span> </span><a href="https://gitee.com/shihaiyang">@shihy</a><span> </span>贡献<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/254/">#254</a></li> 
</ul> 
<h3 style="text-align:start">🔨<span> </span>Dependency Upgrades</h3> 
<p style="color:#c9d1d9; text-align:start">暂无</p> 
<p>-----------------------------------------------------------------------------------------------------------------------------------</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">🐷 演示图</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">系统功能</h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,"system-ui","Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>模块</th> 
   <th>biu</th> 
   <th>biu</th> 
   <th>biu</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">登录 & 首页</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="登录" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E7%99%BB%E5%BD%95.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="首页" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E9%A6%96%E9%A1%B5.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="个人中心" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E4%B8%AA%E4%BA%BA%E4%B8%AD%E5%BF%83.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">用户 & 应用</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="用户管理" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="令牌管理" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E4%BB%A4%E7%89%8C%E7%AE%A1%E7%90%86.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="应用管理" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E5%BA%94%E7%94%A8%E7%AE%A1%E7%90%86.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">租户 & 套餐</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="租户管理" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E7%A7%9F%E6%88%B7%E7%AE%A1%E7%90%86.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="租户套餐" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E7%A7%9F%E6%88%B7%E5%A5%97%E9%A4%90.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">部门 & 岗位</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="部门管理" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E9%83%A8%E9%97%A8%E7%AE%A1%E7%90%86.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="岗位管理" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E5%B2%97%E4%BD%8D%E7%AE%A1%E7%90%86.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">菜单 & 角色</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="菜单管理" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E8%8F%9C%E5%8D%95%E7%AE%A1%E7%90%86.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="角色管理" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E8%A7%92%E8%89%B2%E7%AE%A1%E7%90%86.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">审计日志</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="操作日志" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%93%8D%E4%BD%9C%E6%97%A5%E5%BF%97.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="登录日志" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E7%99%BB%E5%BD%95%E6%97%A5%E5%BF%97.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">短信</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="短信渠道" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E7%9F%AD%E4%BF%A1%E6%B8%A0%E9%81%93.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="短信模板" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E7%9F%AD%E4%BF%A1%E6%A8%A1%E6%9D%BF.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="短信日志" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E7%9F%AD%E4%BF%A1%E6%97%A5%E5%BF%97.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">字典 & 敏感词</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="字典类型" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E5%AD%97%E5%85%B8%E7%B1%BB%E5%9E%8B.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="字典数据" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E5%AD%97%E5%85%B8%E6%95%B0%E6%8D%AE.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="敏感词" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%95%8F%E6%84%9F%E8%AF%8D.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">错误码 & 通知</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="错误码管理" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E9%94%99%E8%AF%AF%E7%A0%81%E7%AE%A1%E7%90%86.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="通知公告" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E9%80%9A%E7%9F%A5%E5%85%AC%E5%91%8A.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="margin-left:0; margin-right:0; text-align:left">工作流程</h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,"system-ui","Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>模块</th> 
   <th>biu</th> 
   <th>biu</th> 
   <th>biu</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">流程模型</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="流程模型-列表" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%B5%81%E7%A8%8B%E6%A8%A1%E5%9E%8B-%E5%88%97%E8%A1%A8.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="流程模型-设计" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%B5%81%E7%A8%8B%E6%A8%A1%E5%9E%8B-%E8%AE%BE%E8%AE%A1.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="流程模型-定义" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%B5%81%E7%A8%8B%E6%A8%A1%E5%9E%8B-%E5%AE%9A%E4%B9%89.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">表单 & 分组</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="流程表单" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%B5%81%E7%A8%8B%E8%A1%A8%E5%8D%95.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="用户分组" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E7%94%A8%E6%88%B7%E5%88%86%E7%BB%84.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">我的流程</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="我的流程-列表" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%88%91%E7%9A%84%E6%B5%81%E7%A8%8B-%E5%88%97%E8%A1%A8.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="我的流程-发起" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%88%91%E7%9A%84%E6%B5%81%E7%A8%8B-%E5%8F%91%E8%B5%B7.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="我的流程-详情" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%88%91%E7%9A%84%E6%B5%81%E7%A8%8B-%E8%AF%A6%E6%83%85.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">待办 & 已办</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="任务列表-审批" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E4%BB%BB%E5%8A%A1%E5%88%97%E8%A1%A8-%E5%AE%A1%E6%89%B9.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="任务列表-待办" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E4%BB%BB%E5%8A%A1%E5%88%97%E8%A1%A8-%E5%BE%85%E5%8A%9E.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="任务列表-已办" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E4%BB%BB%E5%8A%A1%E5%88%97%E8%A1%A8-%E5%B7%B2%E5%8A%9E.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">OA 请假</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="OA请假-列表" src="https://static.iocoder.cn/images/ruoyi-vue-pro/OA%E8%AF%B7%E5%81%87-%E5%88%97%E8%A1%A8.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="OA请假-发起" src="https://static.iocoder.cn/images/ruoyi-vue-pro/OA%E8%AF%B7%E5%81%87-%E5%8F%91%E8%B5%B7.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="OA请假-详情" src="https://static.iocoder.cn/images/ruoyi-vue-pro/OA%E8%AF%B7%E5%81%87-%E8%AF%A6%E6%83%85.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="margin-left:0; margin-right:0; text-align:left">基础设施</h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,"system-ui","Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>模块</th> 
   <th>biu</th> 
   <th>biu</th> 
   <th>biu</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">代码生成</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="代码生成" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E4%BB%A3%E7%A0%81%E7%94%9F%E6%88%90.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="生成效果" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E7%94%9F%E6%88%90%E6%95%88%E6%9E%9C.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">文档</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="系统接口" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E7%B3%BB%E7%BB%9F%E6%8E%A5%E5%8F%A3.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="数据库文档" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%95%B0%E6%8D%AE%E5%BA%93%E6%96%87%E6%A1%A3.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">文件 & 配置</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="文件配置" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%96%87%E4%BB%B6%E9%85%8D%E7%BD%AE.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="文件管理" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%862.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="配置管理" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E9%85%8D%E7%BD%AE%E7%AE%A1%E7%90%86.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">定时任务</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="定时任务" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="任务日志" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E4%BB%BB%E5%8A%A1%E6%97%A5%E5%BF%97.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">API 日志</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="访问日志" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E8%AE%BF%E9%97%AE%E6%97%A5%E5%BF%97.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="错误日志" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E9%94%99%E8%AF%AF%E6%97%A5%E5%BF%97.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">MySQL & Redis</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="MySQL" src="https://static.iocoder.cn/images/ruoyi-vue-pro/MySQL.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="Redis" src="https://static.iocoder.cn/images/ruoyi-vue-pro/Redis.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">监控平台</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="Java监控" src="https://static.iocoder.cn/images/ruoyi-vue-pro/Java%E7%9B%91%E6%8E%A7.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="链路追踪" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E9%93%BE%E8%B7%AF%E8%BF%BD%E8%B8%AA.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="日志中心" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%97%A5%E5%BF%97%E4%B8%AD%E5%BF%83.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="margin-left:0; margin-right:0; text-align:left">支付系统</h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,"system-ui","Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>模块</th> 
   <th>biu</th> 
   <th>biu</th> 
   <th>biu</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">商家 & 应用</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="商户信息" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E5%95%86%E6%88%B7%E4%BF%A1%E6%81%AF.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="应用信息-列表" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E5%BA%94%E7%94%A8%E4%BF%A1%E6%81%AF-%E5%88%97%E8%A1%A8.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="应用信息-编辑" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E5%BA%94%E7%94%A8%E4%BF%A1%E6%81%AF-%E7%BC%96%E8%BE%91.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">支付 & 退款</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="支付订单" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%94%AF%E4%BB%98%E8%AE%A2%E5%8D%95.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="退款订单" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E9%80%80%E6%AC%BE%E8%AE%A2%E5%8D%95.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">---</td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="margin-left:0; margin-right:0; text-align:left">数据报表</h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,"system-ui","Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>模块</th> 
   <th>biu</th> 
   <th>biu</th> 
   <th>biu</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">报表设计器</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="数据报表" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%8A%A5%E8%A1%A8%E8%AE%BE%E8%AE%A1%E5%99%A8-%E6%95%B0%E6%8D%AE%E6%8A%A5%E8%A1%A8.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="图形报表" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%8A%A5%E8%A1%A8%E8%AE%BE%E8%AE%A1%E5%99%A8-%E5%9B%BE%E5%BD%A2%E6%8A%A5%E8%A1%A8.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="报表设计器-打印设计" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%8A%A5%E8%A1%A8%E8%AE%BE%E8%AE%A1%E5%99%A8-%E6%89%93%E5%8D%B0%E8%AE%BE%E8%AE%A1.jpg?imageView2/2/format/webp/w/1280" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="margin-left:0; margin-right:0; text-align:left">移动端（管理后台）</h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,"system-ui","Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>biu</th> 
   <th>biu</th> 
   <th>biu</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt src="https://static.iocoder.cn/images/ruoyi-vue-pro/admin-uniapp/01.png?imageView2/2/format/webp" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt src="https://static.iocoder.cn/images/ruoyi-vue-pro/admin-uniapp/02.png?imageView2/2/format/webp" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt src="https://static.iocoder.cn/images/ruoyi-vue-pro/admin-uniapp/03.png?imageView2/2/format/webp" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt src="https://static.iocoder.cn/images/ruoyi-vue-pro/admin-uniapp/04.png?imageView2/2/format/webp" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt src="https://static.iocoder.cn/images/ruoyi-vue-pro/admin-uniapp/05.png?imageView2/2/format/webp" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt src="https://static.iocoder.cn/images/ruoyi-vue-pro/admin-uniapp/06.png?imageView2/2/format/webp" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt src="https://static.iocoder.cn/images/ruoyi-vue-pro/admin-uniapp/07.png?imageView2/2/format/webp" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt src="https://static.iocoder.cn/images/ruoyi-vue-pro/admin-uniapp/08.png?imageView2/2/format/webp" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt src="https://static.iocoder.cn/images/ruoyi-vue-pro/admin-uniapp/09.png?imageView2/2/format/webp" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="margin-left:0; margin-right:0; text-align:left">商城系统</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">建设中...</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="功能图" src="http://static.iocoder.cn/mall%20%E5%8A%9F%E8%83%BD%E5%9B%BE-min.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="GIF 图-耐心等待" src="https://raw.githubusercontent.com/YunaiV/Blog/master/Mall/onemall-admin-min.gif" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="GIF 图-耐心等待" src="https://raw.githubusercontent.com/YunaiV/Blog/master/Mall/onemall-h5-min.gif" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            