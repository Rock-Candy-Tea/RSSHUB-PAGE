
---
title: 'View UI（iView）4.6.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1762'
author: 开源中国
comments: false
date: Fri, 11 Jun 2021 14:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1762'
---

<div>   
<div class="content">
                                                                    
                                                        <p>View UI（iView）4.6.0 版本已于 2021-06-11 日发布，版本代号：It Takes Two。</p> 
<h1>更新日志</h1> 
<blockquote> 
 <p>请到官网 www.iviewui.com 查看最新版。</p> 
</blockquote> 
<ul> 
 <li> <p>Modal 新增属性 <code>sticky</code> 和 <code>sticky-distance</code>，开启后，在拖拽时，将不会拖出屏幕边缘，并在极限距离时，自动吸附。</p> </li> 
 <li> <p>Modal 新增属性 <code>reset-drag-position</code>，开启后，Modal 再次打开时，将重置拖拽的位置。</p> </li> 
 <li> <p>Modal 的属性 <code>mask</code> 在 <code>draggable</code> 模式下，不再强制设置为 false。</p> </li> 
 <li> <p>Drawer 的属性 <code>placement</code> 新增值 <code>top</code> 和 <code>bottom</code>，支持顶部和底部方向。同时增加属性 <code>height</code>。顶部、底部暂不支持拖拽。</p> </li> 
 <li> <p>AutoComplete 新增属性 <code>capture</code>。</p> </li> 
 <li> <p>Dropdown、Select、DatePicker、TimePicker、Cascader、ColorPicker、Tooltip、Poptip、Page、AutoComplete 新增属性 <code>events-enabled</code>，开启后则会开启 Popper 的 eventsEnabled 属性，但可能会牺牲一定的性能。</p> </li> 
 <li> <p>修复 Row 组件在 4.5.0 版本时，有时产生无效 CSS 类名的问题。</p> </li> 
 <li> <p>修复 DatePicker 组件在 <code>daterange</code> 模式下，起始日期为31日时，切换上月面板，面板月份没有变化的问题。#418</p> </li> 
 <li> <p>修复 Select 组件使用 <code>label-in-value</code> 时，在多选、可搜索状态下出错的问题。</p> </li> 
 <li> <p>修复 Button 等组件同时设置 <code>target: _blank</code> 和 Object 类型的 <code>to</code> 属性时，跳转功能失效的问题。</p> </li> 
 <li> <p>修复带有下拉框的组件开启 transfer 时，有时滚动条抖动的问题。#911</p> </li> 
 <li> <p>修复 Divider 在 Chrome 91 版本错位的问题。#913</p> </li> 
 <li> <p>调整 Table 点击单元格事件 <code>@on-cell-click</code> 触发的位置。</p> </li> 
</ul> 
<h1>更新方法</h1> 
<p>1.修改 <code>package.jso</code>n 中 <code>view-design</code> 版本号：</p> 
<pre><code> "dependencies": &#123;
    "view-design": "^4.6.0"
  &#125;
</code></pre> 
<p>2.运行 <code>npm update view-design</code>。</p>
                                        </div>
                                      
</div>
            