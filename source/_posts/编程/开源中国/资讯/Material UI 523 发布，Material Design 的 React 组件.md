
---
title: 'Material UI 5.2.3 发布，Material Design 的 React 组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1208/064323_6Y0v_2744687.png'
author: 开源中国
comments: false
date: Wed, 08 Dec 2021 06:43:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1208/064323_6Y0v_2744687.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">Material UI 5.2.3 发布了，Material UI 是一组实现 Google Material Design 规范的 React 组件，它是一个前端 JS 框架，主要用在 web 领域。 更新内容如下：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033">在<span> </span></span><code>@mui/base</code><span style="color:#24292f">:<span> </span></span><code>TablePagination</code><span style="color:#2e3033"><span> </span>中引入了一个新的无样式组件：</span></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img alt height="600" src="https://static.oschina.net/uploads/space/2021/1208/064323_6Y0v_2744687.png" width="960" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">可以在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fissues%2F27170" target="_blank">#27170</a><span> </span>关注使用无样式组件的进展。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加了一个将 MUI 与<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fremix.run%2F" target="_blank">Remix</a><span> </span>结合使用的示例(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29952" target="_blank">#29952</a><span> </span>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/material@5.2.3</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f">​[Accordion]  </span>添加对<span> </span><code>square</code><span> </span>属性的测试(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29972" target="_blank">#29972</a><span> </span>) </li> 
 <li>[AvatarGroup] 允许指定 avatars 的总数（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29898" target="_blank">#29898</a>）</li> 
 <li>​[Button]<span> </span><span style="color:#2e3033">修复了从上下文 API 回归的问题<span> </span></span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29982" target="_blank">#29982</a>) </li> 
 <li>​[Grid]<span> </span><span style="color:#2e3033">复值为 objec t时为<span> </span></span><span style="color:#24292f"><code>spacing</code></span><span style="color:#2e3033"><span> </span>属性生成的类</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29880" target="_blank">#29880</a>) </li> 
 <li>​[Select] 修复启用<span> </span><code>multiple</code><span> </span>并传递空数组时的崩溃问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29957" target="_blank">#29957</a>) </li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/system@5.2.3</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>​[system] 修复<span> </span><code>createBox</code><span> </span>的返回类型 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29989" target="_blank">#29989</a>) </li> 
 <li>​[system] 在 typescript 中，<span> </span><code>sx</code><span> </span>属性作为数组使用的时候支持布尔值 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29911" target="_blank">#29911</a>) </li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/utils@5.2.3</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>​[utils] 为<span> </span><code>@mui-material/styles/cssUtils</code><span> </span>加入类型 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29621" target="_blank">#29621</a>) </li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/icons-material@5.2.1</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>​[icons]<span> </span><span style="color:#2e3033">合并被忽略的图标到一个列表中</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29843" target="_blank">#29843</a>) </li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/base@5.0.0-alpha.59</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>​[base]<span> </span><span style="color:#24292f">修复缺少的 ClickAwayListener 桶索引导出</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F30000" target="_blank">#30000</a>) </li> 
 <li>​[TablePaginationUnstyled] 引入新组件 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29759" target="_blank">#29759</a>) </li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/lab@5.0.0-alpha.59</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>​[DateRangePicker] 修复<span> </span><code>DateRangePickerDayProps</code><span> </span>界面 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29067" target="_blank">#29067</a>) </li> 
 <li>​[Pickers] 移除从自定义属性到<span> </span><code>MonthPicker</code><span> </span>组件 DOM 元素的传播(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F30021" target="_blank">#30021</a>) </li> 
 <li>​[StaticDatePicker] 将类名<span style="color:#24292f">和 slot 的根文件添加到 PickerStaticWrapper</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29619" target="_blank">#29619</a>) </li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/joy@5.0.0-alpha.5</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>​[Joy] 根据<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.notion.so%2Fmui-org%2FRFC-Theme-implementation-e15bc2ef11ba4f6f804434af27141afe" target="_blank">Notion</a><span> </span>设置默认主题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29846" target="_blank">#29846</a>) </li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">核心变更</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f">​[core]<span> </span></span>批量小改动<span> </span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F30042" target="_blank">#30042</a><span style="color:#24292f">)</span></li> 
 <li><span style="color:#24292f">​[core]<span> </span></span><span style="color:#2e3033">过渡到一个新的 StackOverflow 标签。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29967" target="_blank">#29967</a><span style="color:#24292f">) </span></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">除以上特性变更，此版本还包含一些文档变更，详情可查看</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Freleases%2Ftag%2Fv5.2.3" target="_blank">更新公告</a><span style="color:#000000">。</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            