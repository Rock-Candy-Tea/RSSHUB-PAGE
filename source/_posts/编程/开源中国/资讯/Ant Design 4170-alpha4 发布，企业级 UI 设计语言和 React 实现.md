
---
title: 'Ant Design 4.17.0-alpha.4 发布，企业级 UI 设计语言和 React 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=601'
author: 开源中国
comments: false
date: Mon, 27 Sep 2021 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=601'
---

<div>   
<div class="content">
                                                                                            <p>Ant Design 4.17.0-alpha.4 <span style="background-color:#ffffff; color:#000000">现</span><span style="background-color:#ffffff; color:#333333">已发布，主要变化如下：</span></p> 
<ul> 
 <li>修复英文国际化文案<span> </span><code>Ok</code><span> </span>为<span> </span><code>OK</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32259" target="_blank">#32259</a></li> 
 <li>修复<span> </span><code>antd.variable.less</code><span> </span>编译时会混入默认主题配置的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32279" target="_blank">#32279</a></li> 
 <li>Button 
  <ul> 
   <li>修复 Button<span> </span><code>ghost</code><span> </span>鼠标悬停样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32289" target="_blank">#32289</a></li> 
   <li>修复 Button 配置<span> </span><code>loading</code><span> </span>时，无法触发 Tooltip 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32158" target="_blank">#32158</a></li> 
  </ul> </li> 
 <li>Table 
  <ul> 
   <li>修复 Table 不支持<span> </span><code>ref</code><span> </span>的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32136" target="_blank">#32136</a></li> 
   <li>Table 移除 IE11 下<span> </span><code>sticky</code><span> </span>的相关样式以解决布局问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32177" target="_blank">#32177</a></li> 
   <li>优化 Table 排序图标边距问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32172" target="_blank">#32172</a></li> 
  </ul> </li> 
 <li>修复 Switch<span> </span><code>loading</code><span> </span>按钮位置不正确的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32216" target="_blank">#32216</a></li> 
 <li>修复 Grid Col<span> </span><code>flex</code><span> </span>在内容过长的时候缩放失效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32160" target="_blank">#32160</a></li> 
 <li>RTL 
  <ul> 
   <li>优化 Alert 关闭按钮在 RTL 模式下的显示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32286" target="_blank">#32286</a></li> 
   <li>优化 Table 表头操作按钮在 RTL 模式下显示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32283" target="_blank">#32283</a></li> 
   <li>优化 Collapse 按钮在 RTL 模式下位置显示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32282" target="_blank">#32282</a></li> 
   <li>优化 Badge 数字在 RTL 模式下显示和动画。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32281" target="_blank">#32281</a></li> 
   <li>优化 InputNumber 操作栏 RTL 模式下边框样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32272" target="_blank">#32272</a></li> 
   <li>优化 Dropdown RTL 模式下 icon 显示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32271" target="_blank">#32271</a></li> 
  </ul> </li> 
 <li>TypeScript 
  <ul> 
   <li>修复 Switch<span> </span><code>id</code><span> </span>属性定义。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32237" target="_blank">#32237</a></li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Freleases%2Ftag%2F4.17.0-alpha.4" target="_blank">https://github.com/ant-design/ant-design/releases/tag/4.17.0-alpha.4</a> </p>
                                        </div>
                                      
</div>
            