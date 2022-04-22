
---
title: '前后端分离后台管理系统 Gfast v3.0 全新发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://yxh-1301841944.cos.ap-chongqing.myqcloud.com/gfast/2022-04-19/gfastlogo.png'
author: 开源中国
comments: false
date: Fri, 22 Apr 2022 10:30:00 GMT
thumbnail: 'https://yxh-1301841944.cos.ap-chongqing.myqcloud.com/gfast/2022-04-19/gfastlogo.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p style="text-align:center"><img src="https://yxh-1301841944.cos.ap-chongqing.myqcloud.com/gfast/2022-04-19/gfastlogo.png" referrerpolicy="no-referrer"></p> 
 <p style="margin-left:0px; margin-right:0px; text-align:center"> </p> 
 <h1 style="margin-left:0px; margin-right:0px; text-align:center">GFast V3.0</h1> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">平台简介</h2> 
<ul> 
 <li>基于全新Go Frame 2.0+Vue3+Element Plus开发的全栈前后端分离的管理系统</li> 
 <li>前端采用vue-next-admin 、Vue、Element UI。</li> 
 <li>本项目由<a href="https://gitee.com/link?target=http%3A%2F%2Fwww.qjit.cn%2F" target="_blank"><strong>奇讯科技</strong></a>团队开发。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">特征</h2> 
<ul> 
 <li>高生产率：几分钟即可搭建一个后台管理系统</li> 
 <li>模块化：单应用多系统的模式，将一个完整的应用拆分为多个系统，后续扩展更加便捷，增加代码复用性。</li> 
 <li>插件化： 可通过插件的方式扩展系统功能</li> 
 <li>认证机制：采用gtoken的用户状态认证及casbin的权限认证</li> 
 <li>路由模式：得利于goframe2.0提供了规范化的路由注册方式,无需注解自动生成api文档</li> 
 <li>面向接口开发</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">内置功能</h2> 
<ol> 
 <li>用户管理：用户是系统操作者，该功能主要完成系统用户配置。</li> 
 <li>部门管理：配置系统组织机构（公司、部门、小组），树结构展现支持数据权限。</li> 
 <li>岗位管理：配置系统用户所属担任职务。</li> 
 <li>菜单管理：配置系统菜单，操作权限，按钮权限标识等。</li> 
 <li>角色管理：角色菜单权限分配、设置角色按机构进行数据范围权限划分。</li> 
 <li>字典管理：对系统中经常使用的一些较为固定的数据进行维护。</li> 
 <li>参数管理：对系统动态配置常用参数。</li> 
 <li>操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。</li> 
 <li>登录日志：系统登录日志记录查询包含登录异常。</li> 
 <li>在线用户：当前系统中活跃用户状态监控。</li> 
 <li>定时任务：在线（添加、修改、删除)任务调度包含执行结果日志。</li> 
 <li>代码生成：前后端代码的生成。</li> 
 <li>服务监控：监视当前系统CPU、内存、磁盘、堆栈等相关信息。</li> 
 <li>在线构建器：拖动表单元素生成相应的HTML代码。</li> 
 <li>文件上传,缓存标签等。</li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:left">演示地址</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=http%3A%2F%2Fv3.g-fast.cn%2Fsys">http://v3.g-fast.cn/sys</a><span> </span>账号：demo 密码：123456</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">配置</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">项目数据库文件<span> </span><code>resource/data/db.sql</code><span> </span>创建数据库导入后修改配置<span> </span><code>manifest/config/config.yaml.bak</code><span> </span>复制改为<code>manifest/config/config.yaml</code></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">其中gfToken配置</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#008080">gfToken</span><span>:</span></span>
<span>  <span style="color:#008080">cacheKey</span><span>:</span> <span style="color:#dd1144">"</span><span style="color:#dd2200">gfToken_"</span>   <span style="color:#888888">#缓存前缀</span></span>
<span>  <span style="color:#008080">timeOut</span><span>:</span> <strong style="color:#0000dd">10800</strong>         <span style="color:#888888">#token超时时间（秒）</span></span>
<span>  <span style="color:#008080">maxRefresh</span><span>:</span> <strong style="color:#0000dd">5400</strong>       <span style="color:#888888">#token自动刷新时间（秒）</span></span>
<span>  <span style="color:#008080">multiLogin</span><span>:</span> <span style="color:#008080">true</span>       <span style="color:#888888">#是否允许一个账号多人同时登录</span></span>
<span>  <span style="color:#008080">encryptKey</span><span>:</span> <span style="color:#dd1144">"</span><span style="color:#dd2200">49c54195e750b04e74a8429b17896586"</span>    <span style="color:#888888">#加密key (32位)</span></span>
<span>  <span style="color:#008080">cacheModel</span><span>:</span> <span style="color:#dd1144">"</span><span style="color:#dd2200">redis"</span>    <span style="color:#888888">#存储引擎 （memory使用内存|redis使用redis）</span></span>
<span>  <span style="color:#008080">excludePaths</span><span>:</span>          <span style="color:#888888">#排除不做登录验证的路由地址</span></span>
<span>    <span>-</span> <span style="color:#dd1144">"</span><span style="color:#dd2200">/api/v1/system/login"</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">项目为前后端分离，前端地址：</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">github地址：<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftiger1103%2Fgfast-ui">https://github.com/tiger1103/gfast-ui</a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">gitee地址：<a href="https://gitee.com/tiger1103/gfast-ui">https://gitee.com/tiger1103/gfast-ui</a></p> 
<p>(请切换：os-v3)</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">演示图</h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-indent:0px; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://yxh-1301841944.cos.ap-chongqing.myqcloud.com/gfast/2022-04-19/cje01e1blsg80hagzj.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://yxh-1301841944.cos.ap-chongqing.myqcloud.com/gfast/2022-04-19/cje01gckl91kjetl0d.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://yxh-1301841944.cos.ap-chongqing.myqcloud.com/gfast/2022-04-19/cje01gckl91ky1lm3d.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://yxh-1301841944.cos.ap-chongqing.myqcloud.com/gfast/2022-04-19/cje01kkmk7sc1txfvz.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://yxh-1301841944.cos.ap-chongqing.myqcloud.com/gfast/2022-04-19/cje01kkmkfi4syoydw.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://yxh-1301841944.cos.ap-chongqing.myqcloud.com/gfast/2022-04-19/cje01s04zq2470mx3r.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://yxh-1301841944.cos.ap-chongqing.myqcloud.com/gfast/2022-04-19/cje01kkmkfi4tquojj.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://yxh-1301841944.cos.ap-chongqing.myqcloud.com/gfast/2022-04-19/cje01s04zq245k17ta.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            