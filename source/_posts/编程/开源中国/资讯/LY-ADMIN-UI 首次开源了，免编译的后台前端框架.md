
---
title: 'LY-ADMIN-UI 首次开源了，免编译的后台前端框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/tengzhinei/ly-admin-ui/raw/master/images/1.jpeg'
author: 开源中国
comments: false
date: Thu, 09 Jun 2022 09:55:00 GMT
thumbnail: 'https://gitee.com/tengzhinei/ly-admin-ui/raw/master/images/1.jpeg'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0; margin-right:0; text-align:left"><br> 介绍</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">三年磨一剑,Ly-Admin-ui是我们经过多年内部维护和使用的ui框架,现在决定开源了</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Ly-Admin-ui 好用超全的管理后台前端框架，它基于 vue + element-ui+vue-rap 技术栈。 它使用了最新的前端技术栈，项目在element-ui基础上又添加了超多实用组件和布局; 项目整体使用了最新的vue-rap流应用技术,项目可以不需要构建的情况下直接部署,边使用边下载。</p> 
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
<h3 style="margin-left:0; margin-right:0; text-align:left">安装方式</h3> 
<hr> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">下载文件<span> </span><a href="https://gitee.com/link?target=http%3A%2F%2Flyadminui.magcloud.net%2Flyadminui.zip">LyAdminUI</a></p> 
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:left">目录结构</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span>├─portal                       前端跟目录</span>
<span>│  ├─comp                      项目特用的组件,且不会抽取为公共的组件</span>
<span>│  ├─utils                     工具文件</span>
<span>│  │   ├─area.json             地区数据(请勿移动)</span>
<span>│  │   ├─state.js              状态量管理</span>
<span>│  │   ├─menus.json            这里是你的菜单配置文件</span>
<span>│  ├─ly                        LYUI 框架目录(请勿移动)</span>
<span>│  ├─其他自定义模块              其他自定义模块</span>
<span>│  ├─global.js                 入口js文件</span>
<span>│  ├─index.html                入口html,正常会由后端渲染返回</span>
<span>├─static                       前端静态文件</span>
<span>│  ├─ly                     LYUI 需要使用到的静态文件(请勿移动)</span>
<span>│  ├─imgs                   静态图片</span>
<span>│  ├─libs                   引用的三方js 库</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">拉取后的目录结构为推荐的目录结构,可以根据实际情况进行调整</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">标志为请勿移动的目录为 LyUI 框架文件,请勿随意修改或在目录内放入其他项目文件</p> 
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:left">框架更新</h3> 
<hr> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">重新拉取项目,覆盖<span> </span><code>/portal/ly</code>,<code>/static/ly</code>三个目录</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">项目截图</h3> 
<div>
 <img src="https://gitee.com/tengzhinei/ly-admin-ui/raw/master/images/1.jpeg" width="92%" referrerpolicy="no-referrer">
 <span> </span>
 <img src="https://gitee.com/tengzhinei/ly-admin-ui/raw/master/images/2.jpeg" width="92%" referrerpolicy="no-referrer">
 <span> </span>
 <img src="https://gitee.com/tengzhinei/ly-admin-ui/raw/master/images/3.jpeg" width="92%" referrerpolicy="no-referrer">
 <span> </span>
 <img src="https://gitee.com/tengzhinei/ly-admin-ui/raw/master/images/4.jpeg" width="92%" referrerpolicy="no-referrer">
</div> 
<p> </p>
                                        </div>
                                      
</div>
            