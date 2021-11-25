
---
title: 'Material UI 5.2.0 发布，Material Design 组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7851'
author: 开源中国
comments: false
date: Thu, 25 Nov 2021 06:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7851'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Material UI 5.2.0 发布了，Material UI 是一组实现 Google Material Design 规范的 React 组件，它是一个前端 JS 框架，主要用在 web 领域。 更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/material@5.2.0</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[IconButton] 设置<span> </span><code>disableRipple</code><span> </span>时，移除悬停效果(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29298" target="_blank">#29298</a><span> </span>)</li> 
 <li>[i18n] 添加阿姆哈拉语 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29153" target="_blank">#29153</a><span> </span>)</li> 
 <li>[material] 修复<span> </span><code>variants.style</code><span> </span>接受回调的类型（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29610" target="_blank">#29610</a>）</li> 
 <li>[Popper] 简化 prop 类型（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29680" target="_blank">#29680</a>）</li> 
 <li>[选择] 选项未被选中时，默认<span> </span><code>aria-selected = false</code><span> </span>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29695" target="_blank">#29695</a><span> </span>)</li> 
 <li>[useMediaQuery] 修复 Safari 14 以下版本 和 IE 11 中的崩溃问题。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29776" target="_blank">#29776</a><span> </span>)</li> 
 <li>[useMediaQuery] 确保在 React 18 没有撕裂和串联更新。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F28491" target="_blank">#28491</a><span> </span>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/codemod@5.2.0</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[codemod] 修复<span> </span><code>jss-to-styled</code><span> </span>，以支持多个 withStyles (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29824" target="_blank">#29824</a><span> </span>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/icons-material@5.2.0</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[图标] 同步新的 Google Material Icons (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29818" target="_blank">#29818</a><span> </span>)</li> 
 <li>[图标] 同步最近来自 Google 的 Material Icons (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29328" target="_blank">#29328</a><span> </span>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/system@5.2.0</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[Box] 在<span> </span><code>sx</code><span> </span>用作函数时，修复 prop 的运行时问题 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29830" target="_blank">#29830</a><span> </span>)</li> 
 <li>[系统] 修复<span> </span><code>sx</code><span> </span>值为<span> </span><code>null</code><span> </span>或<span> </span><code>undefined</code><span> </span>时报错的问题 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29756" target="_blank">#29756</a><span> </span>)</li> 
 <li>[系统] 修复轻微的 CssVars 问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29747" target="_blank">#29747</a>）</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/styled-engine@5.2.0</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[styled-engine] 修复 styled-engine 的 prop 推断  (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29739" target="_blank">#29739</a><span> </span>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/base@5.0.0-alpha.56</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[FormControlUnstyled]<span> </span><code>focused</code><span> </span>始终为 false，除非明确设置为<span> </span><code>true</code></li> 
 <li>[TabsUnstyled] 引入新组件 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29597" target="_blank">#29597</a><span> </span>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/lab@5.0.0-alpha.56</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[DatePicker][timepicker] 添加缺少的组件声明 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29517" target="_blank">#29517</a><span> </span>)</li> 
 <li>[Masonry] 从 root 包导出 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29754" target="_blank">#29754</a><span> </span>)</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29761" target="_blank">pickers</a><span> </span>] 扩大接受的<span> </span><code>luxon</code><span> </span>版本范围 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29761" target="_blank">#29761</a><span> </span>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Core</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[测试] 允许使用 Chrome 和 VSCode 检查器进行调试 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29777" target="_blank">#29777</a><span> </span>)</li> 
 <li>[测试] 使用渲染器时钟而不是自定义 useFakeTimers 调用（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29778" target="_blank">#29778</a>）</li> 
 <li>[测试] 仅在回归测试中模拟日期 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29763" target="_blank">#29763</a><span> </span>)</li> 
 <li>[测试] 在<span> </span><code>next</code><span> </span>分支上禁用 nightly 集成测试(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29748" target="_blank">#29748</a><span> </span>)</li> 
 <li>[测试] 允许直接从<span> </span><code>createRenderer</code><span> </span>配置时钟（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29684" target="_blank">#29684</a>）</li> 
 <li>[测试] 在测试 CLI  接受反斜杠作为路径分隔符 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F29694" target="_blank">#29694</a><span> </span>)</li> 
 <li>[utils] 在 useId 可用时使用内置 hooks (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Fpull%2F26489" target="_blank">#26489</a><span> </span>)</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">除以上特性变更，此版本还包含一些文档变更，详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui-org%2Fmaterial-ui%2Freleases%2Ftag%2Fv5.2.0" target="_blank">更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            