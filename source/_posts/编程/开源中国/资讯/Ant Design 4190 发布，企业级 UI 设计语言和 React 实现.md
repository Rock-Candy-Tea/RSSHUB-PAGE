
---
title: 'Ant Design 4.19.0 发布，企业级 UI 设计语言和 React 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cc5a0bef5e2505ac8d2d0c2747cc95b7bd3.png'
author: 开源中国
comments: false
date: Wed, 09 Mar 2022 07:04:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cc5a0bef5e2505ac8d2d0c2747cc95b7bd3.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#000000">Ant Design 4.19.0 现已发布，主要变化如下：</span></p> 
<ul> 
 <li>优化部分组件箭头样式。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33710" target="_blank">#33710</a><br> <img alt height="300" src="https://oscimg.oschina.net/oscnet/up-cc5a0bef5e2505ac8d2d0c2747cc95b7bd3.png" width="374" referrerpolicy="no-referrer"></li> 
 <li>Input 
  <ul> 
   <li>引入 rc-input 重构 Input 组件为 function component。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34206" target="_blank">#34206</a> 
    <ul> 
     <li>注意：由于从 class component 变为 function component，Input 组件的<span> </span><code>ref</code><span> </span>类型及内容已经更新，可以通过<span> </span><code>import &#123; InputRef &#125; from 'antd'</code><span> </span>引入。其中的<span> </span><code>input</code><span> </span>属性作为获取 DOM 的途径被保留，同时支持<span> </span><code>focus</code><span> </span>和<span> </span><code>blur</code><span> </span>等文档中支持的方法。</li> 
    </ul> </li> 
   <li>新增<span> </span><code>clearIcon</code><span> </span>属性，支持自定义清除按钮。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34325" target="_blank">#34325</a></li> 
  </ul> </li> 
 <li>Table 
  <ul> 
   <li><code>column.filterSearch</code><span> </span>属性现在支持返回一个函数用于自定义搜索条件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34085" target="_blank">#34085</a></li> 
   <li><code>column.filterDropdown(&#123; clearFilters &#125;)</code><span> </span>支持参数<span> </span><code>clearFilters(&#123; confirm: false, closeDropdown: false &#125;)</code><span> </span>控制筛选。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34120" target="_blank">#34120</a></li> 
   <li>增加<span> </span><code>aria-sort</code><span> </span>属性以优化屏幕阅读器的使用体验。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33603" target="_blank">#33603</a></li> 
   <li>修复 Table 列筛选器中选择全部 Checkbox 状态问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34295" target="_blank">#34295</a></li> 
  </ul> </li> 
 <li>表单组件新增<span> </span><code>status</code><span> </span>属性以支持自定义状态。 
  <ul> 
   <li>Transfer<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34098" target="_blank">#34098</a></li> 
   <li>AutoComplete<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34096" target="_blank">#34096</a></li> 
   <li>TreeSelect<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34093" target="_blank">#34093</a></li> 
   <li>Cascader<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34086" target="_blank">#34086</a></li> 
   <li>Select<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34084" target="_blank">#34084</a></li> 
   <li>DatePicker 和 TimePicker<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34073" target="_blank">#34073</a></li> 
   <li>Mentions<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34071" target="_blank">#34071</a></li> 
   <li>InputNumber<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34042" target="_blank">#34042</a></li> 
   <li>Input<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33995" target="_blank">#33995</a><br> <img alt height="219" src="https://oscimg.oschina.net/oscnet/up-c3b6b7c8bd9e7587d951040275865cad3f6.png" width="500" referrerpolicy="no-referrer"></li> 
  </ul> </li> 
 <li>InputNumber 组件支持<span> </span><code>controls=&#123;&#123; upIcon, downIcon &#125;&#125;</code><span> </span>用于自定义上下图标。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33914" target="_blank">#33914</a></li> 
 <li>Notification 组件弹窗位置新增支持<span> </span><code>top</code><span> </span>/<span> </span><code>bottom</code>。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33871" target="_blank">#33871</a></li> 
 <li>Select、Cascader、DatePicker 等组件新增<span> </span><code>placement</code><span> </span>用于自定义弹层方向。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33541" target="_blank">#33641</a></li> 
 <li>Dropdown 组件支持<span> </span><code>arrow=&#123;&#123; pointAtCenter: true &#125;&#125;</code><span> </span>用于指向元素正中间，并且新增<span> </span><code>top</code><span> </span><code>bottom</code><span> </span>两种<span> </span><code>placement</code><span> </span>位置。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33658" target="_blank">#33658</a></li> 
 <li>Skeleton.Input 添加<span> </span><code>block</code><span> </span>属性。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33672" target="_blank">#33672</a></li> 
 <li>合并 TimePicker<span> </span><code>disabledHours</code>、<code>disabledMinutes</code>、<code>disabledSeconds</code><span> </span>至<span> </span><code>disabledTime</code><span> </span>以保持与 DatePicker 接口一致性。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33503" target="_blank">#33503</a></li> 
 <li>修改部分边框颜色和进度条的背景色为透明色以适应有色背景。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33506" target="_blank">#33506</a></li> 
 <li>Space 支持自定义 children 的<span> </span><code>key</code>。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33607" target="_blank">#33607</a></li> 
 <li>修复 Typography.Title 进入编辑模式时大小不一致的问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34169" target="_blank">#34169</a></li> 
 <li>修复 Form.Item 抛出<span> </span><code>React does not recognize the requiredMark prop on a DOM element</code><span> </span>的问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34323" target="_blank">#34323</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Freleases%2Ftag%2F4.19.0" target="_blank">https://github.com/ant-design/ant-design/releases/tag/4.19.0</a></p>
                                        </div>
                                      
</div>
            