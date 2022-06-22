
---
title: 'Semi Design v2.13.0 发布，抖音企业级 UI 库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4302'
author: 开源中国
comments: false
date: Wed, 22 Jun 2022 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4302'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Semi Design 是现代、全面、灵活的设计系统和 UI 库，由字节跳动抖音前端与 UED 团队设计、开发并维护，是一款包含设计语言、React 组件、主题等开箱即用的中后台解决方案，可用于快速搭建美观的 React 应用。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前 Semi Design 发布了 v2.13.0 版本，此版本带来如下更新内容：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>【Fix】 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复当设置onChangeWithObject，mutiple后，value传入的值为undefined时时，Cascader 崩溃的问题。（影响范围 v2.0.4 - v 2.12.0）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDouyinFE%2Fsemi-design%2Fissues%2F905" target="_blank">#905</a></li> 
   <li>修复 esm / cjs 构建产物，滚动条样式部分场景失效的问题</li> 
  </ul> </li> 
 <li>【Style】 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Modal、TanPane、Upload 增加 color text 声明，解决暗色模式下，当未在 body 容器统一声明 color时，文本颜色对比度不足的问题</li> 
   <li>解决 TimePicker range 模式，在暗色模式下 border-radius 显示不正确的问题</li> 
   <li>disabled的TagInput可以显示+N部分popover的内容</li> 
  </ul> </li> 
 <li>【Design Token】 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Tabs 增加 $color-tabs_tab-pane-text-default，Upload 增加 $color-upload_drag_area_main-text 等若干Token</li> 
  </ul> </li> 
 <li>【Docs】 
  <ul style="margin-left:0; margin-right:0"> 
   <li>增加searchRender API 和 search方法的示例</li> 
  </ul> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDouyinFE%2Fsemi-design%2Freleases%2Ftag%2Fv2.13.0" target="_blank">https://github.com/DouyinFE/semi-design/releases/tag/v2.13.0</a></p>
                                        </div>
                                      
</div>
            