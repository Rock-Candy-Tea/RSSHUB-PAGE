
---
title: '号外号外！DevUI Admin V1.0 发布啦！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202104/29122511_ZPSV.jpg'
author: 开源中国
comments: false
date: Thu, 29 Apr 2021 12:25:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202104/29122511_ZPSV.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p>4月是鸟儿的月份，是木棉花的月份，是 DevUI Admin 发布的月份。</p> 
<p>广受大家期待的 DevUI Admin 终于迎来了第一个开源 Angular 版本！</p> 
<p>DevUI Admin 是一个企业级中后台前端/设计解决方案，依据 DevUI Design 设计价值观，我们在自身的设计规范和基础组件的基础上，构建出了后台管理模板 DevUI Admin。</p> 
<p>数月的孵化，DevUI Admin 为你带来了搭建中后台前端系统的一套解决方案：</p> 
<ul> 
 <li>响应式：适应不同屏幕大小，为用户提供更舒适的界面与用户体验；</li> 
 <li>个性化主题：支持多种主题风格与个性化配置动态切换；</li> 
 <li>布局切换：页面布局可配置，灵活布局；</li> 
 <li>国际化：实现国际化功能，满足多语言业务诉求；</li> 
 <li>Mock 数据：本地数据调试方案，前后端分离；</li> 
 <li>页面模板：基于 DevUI 实践与沉淀，提炼了典型的业务场景并提供场景丰富的页面模板。</li> 
</ul> 
<p>你可以访问 devui.design 了解更多信息，或在 GitHub 上关注 DevUI Admin。</p> 
<ul> 
 <li>预览页：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fadmin%2F" target="_blank">https://devui.design/admin/</a></li> 
 <li>首页：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fadmin-page%2Fhome" target="_blank">https://devui.design/admin-page/home</a></li> 
 <li>GitHub仓库：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDevCloudFE%2Fng-devui-admin" target="_blank">https://github.com/DevCloudFE/ng-devui-admin</a></li> 
 <li>DevUI Design: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fhome" target="_blank">https://devui.design/home</a></li> 
</ul> 
<h1>响应式</h1> 
<p>DevUI Admin 提供了基于栅格的响应式解决方案，初始化一个 Admin 项目后即可获得页面响应式能力。更多地，我们也提供了 <code>da-grid</code> 作为公共组件，你可使用该组件进行响应式页面搭建。</p> 
<p><img alt="2.png" src="https://static.oschina.net/uploads/img/202104/29122511_ZPSV.jpg" referrerpolicy="no-referrer"></p> 
<h1>个性化主题</h1> 
<p>基于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Ftheme-guide" target="_blank">ng-devui</a> 基础能力，DevUI Admin 提供了多种用户可选择主题，除全局配色外，还支持字号、圆角大小可配置，用户可依据自我个性偏好选择对应的主题设置。</p> 
<p><img alt="3.gif" src="https://static.oschina.net/uploads/img/202104/29122512_PkMf.jpg" referrerpolicy="no-referrer"></p> 
<h1>布局切换</h1> 
<p>DevUI Admin 提供了多种布局支持，只需设置你的布局 config，即可进行自定义布局设置。更多地，我们提供了 <code>da-layout</code> 作为组件，你也可使用该组件扩展更多的布局配置。</p> 
<p><img alt="4.gif" src="https://static.oschina.net/uploads/img/202104/29122515_V9Y8.jpg" referrerpolicy="no-referrer"></p> 
<h1>国际化</h1> 
<p>DevUI Admin 通过 <code>@ngx-translate/core</code> 实现国际化功能，国际化相关词条支持模块化管理，在初始化你的 Admin 项目是即可选择对应国际化配置。</p> 
<p><img alt="5.png" src="https://static.oschina.net/uploads/img/202104/29122515_cTav.jpg" referrerpolicy="no-referrer"></p> 
<h1>Mock 数据</h1> 
<p>Mock 数据是做到前后端分离的关键之处，使得前端项目不受后端接口的影响。在 DevUI Admin 中我们已经为你提供了 Mock 数据的方法，你可在初始化你的 Admin 项目时默认选择数据 Mock 支持。</p> 
<h1>页面模板</h1> 
<p>在 DevUI Admin GitHub 代码仓中，我们默认为你提供了多个页面模板。</p> 
<p><img alt="6.png" src="https://static.oschina.net/uploads/img/202104/29122515_tUUM.jpg" referrerpolicy="no-referrer"></p> 
<pre><code>- Dashboard
  - 分析页
  - 监控页
  - 工作台
- 表单页
  - 基础表单
  - 表单布局
  - 高级表单
- 列表页
  - 基础列表
  - 卡片列表
  - 编辑列表
  - 高级列表
  - 树状列表
- 异常页
  - 403
  - 404
  - 500
- 个人页
  - 个人中心
  - 个人设置
</code></pre> 
<p>你可在拉取代码后进行参考。</p> 
<h1>Cli 支持</h1> 
<p>当前 DevUI Admin 支持使用 <code>angular cli</code> 初始化一个 admin 项目，使用 angular cli 即可快速创建并配置你的 admin 项目。</p> 
<pre><code># 初始化项目
$ ng new your-project && cd your-project
$ ng add devui-admin
</code></pre> 
<h1>结语</h1> 
<p>在未来我们将持续演进，关注 DevUI Admin 性能与易用性，持续优化 DevUI Admin 体验并降低开发者使用成本。期待你收到你的意见与建议（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDevCloudFE%2Fng-devui-admin%2Fissues" target="_blank">issue列表</a>），同时也期待你的参与和共建。</p>
                                        </div>
                                      
</div>
            