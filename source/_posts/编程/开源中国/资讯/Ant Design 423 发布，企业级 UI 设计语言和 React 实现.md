
---
title: 'Ant Design 4.23 发布，企业级 UI 设计语言和 React 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9239'
author: 开源中国
comments: false
date: Mon, 05 Sep 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9239'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Ant Design 4.23 现已发布，主要变化如下：</span></p> 
<ul> 
 <li>Tooltip 支持 Fragment 子节点展示气泡。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F37045" target="_blank">#37045</a></li> 
 <li>Dropdown.Button 支持<span> </span><code>danger</code><span> </span>样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36810" target="_blank">#36810</a></li> 
 <li>Input.TextArea 组件<span> </span><code>showCount.formatter</code><span> </span>API 添加<span> </span><code>value</code><span> </span>参数。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36793" target="_blank">#36793</a></li> 
 <li>Table 新增<span> </span><code>expandable.columnTitle</code><span> </span>属性以支持自定义展开列表头。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36794" target="_blank">#36794</a></li> 
 <li>废弃所有弹窗组件的<span> </span><code>visible</code><span> </span>属性，统一为<span> </span><code>open</code>。 
  <ul> 
   <li>Dropdown 的<span> </span><code>visible</code><span> </span>改为<span> </span><code>open</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F37232" target="_blank">#37232</a></li> 
   <li>Modal 组件的<span> </span><code>visible</code><span> </span>改为<span> </span><code>open</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F37084" target="_blank">#37084</a></li> 
   <li>Drawer 的<span> </span><code>visible</code><span> </span>改为<span> </span><code>open</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F37047" target="_blank">#37047</a></li> 
   <li>Table 组件<span> </span><code>columns</code><span> </span>中的<span> </span><code>filterDropdownVisible</code><span> </span>改为<span> </span><code>filterDropdownOpen</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F37026" target="_blank">#37026</a></li> 
   <li>Tooltip, Popover 和 Popconfirm 中的<span> </span><code>visible</code><span> </span>改为<span> </span><code>open</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F37241" target="_blank">#37241</a></li> 
   <li>Slider 的<span> </span><code>tooltip</code><span> </span>相关属性合并到<span> </span><code>tooltip</code><span> </span>属性中。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F37000" target="_blank">#37000</a></li> 
   <li>移除 Tag 组件的<span> </span><code>visible</code><span> </span>属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36934" target="_blank">#36934</a></li> 
  </ul> </li> 
 <li>废弃所有组件的<span> </span><code>dropdownClassName</code>，统一为<span> </span><code>popupClassName</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36880" target="_blank">#36880</a></li> 
 <li>Tabs 支持<span> </span><code>items</code><span> </span>属性，并且废弃原 jsx 语法糖用法。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36889" target="_blank">#36889</a></li> 
 <li>修复 css 变量与 less 变量不一致的问题。 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F37064" target="_blank">#37064</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F37304" target="_blank">#37304</a></li> 
  </ul> </li> 
 <li>修复 Menu 禁用项依然有 focus 样式的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F37332" target="_blank">#37332</a></li> 
 <li><code>@border-radius-sm</code><span> </span>变量默认值不与<span> </span><code>@border-radius-base</code><span> </span>关联，以修复 Checkbox 等组件圆角样式异常。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F37309" target="_blank">#37309</a></li> 
 <li>支持使用<span> </span><code>@slider-handle-margin-left</code><span> </span>定制样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F37001" target="_blank">#37001</a></li> 
 <li>替换 Tabs 切换样式为渐隐过渡，以提升在切换时的体验。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36943" target="_blank">#36943</a></li> 
 <li>改进 Form 校验无障碍体验。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36762" target="_blank">#36762</a></li> 
 <li>补全<span> </span><code>ru_RU</code><span> </span>中<span> </span><code>filterCheckall</code><span> </span>的翻译。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F37311" target="_blank">#37311</a></li> 
 <li>补全<span> </span><code>cs_CZ</code><span> </span>的翻译。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F37388" target="_blank">#37388</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Freleases%2Ftag%2F4.23.0" target="_blank">https://github.com/ant-design/ant-design/releases/tag/4.23.0</a></p>
                                        </div>
                                      
</div>
            