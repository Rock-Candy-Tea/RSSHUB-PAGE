
---
title: 'Material UI 5.10.3 发布，Material Design React 组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4781'
author: 开源中国
comments: false
date: Wed, 31 Aug 2022 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4781'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">Material UI 是一组实现 Google Material Design 规范的 React 组件，它是一个前端 JS 框架，主要用在 web 端。 </span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">Material UI<span> </span></span>5.10.3<span style="color:#000000">现已发布，</span>具体更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/material@5.10.3</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[Autocomplete][material] 修复使用<span> </span><code>disableClearable</code>时值溢出的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F34053" target="_blank">#34053</a>）</li> 
 <li>[Slider] 从 d.ts 中移除 SliderInput 导出（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F34055" target="_blank">#34055</a>）</li> 
 <li>[TablePagination] 修复选择变体不起作用的问题 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F33974" target="_blank">#33974</a><span> </span>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/system@5.10.3</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[system] 修复打开多个会话时模式闪烁的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F33877" target="_blank">#33877</a>）</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/base@5.0.0-alpha.95</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[Button][base] 防止过多的 ref 更新 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F33882" target="_blank">#33882</a><span> </span>)</li> 
 <li>[Select][base] 修复列表框模糊事件处理程序中的拼写错误 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F34120" target="_blank">#34120</a><span> </span>)</li> 
 <li>[TrapFocus] 改进选项卡测试，并简化演示 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F34008" target="_blank">#34008</a><span> </span>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code><strong>@mui/joy@5.0.0-alpha.43</strong></code></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[Joy] 修复<span> </span><code>role</code><span> </span>proptypes (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F34119" target="_blank">#34119</a><span> </span>)</li> 
 <li>[Joy] 优化<span> </span><code>componentsProps</code><span> </span>的所有组件（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F34077" target="_blank">#34077</a>）</li> 
 <li>[Radio][joy] 支持<code>componentsProps</code>功能 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F34022" target="_blank">#34022</a><span> </span>)</li> 
 <li>[Select][joy] 改进 a11y 上的 select field demo (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F34073" target="_blank">#34073</a><span> </span>)</li> 
 <li>[Textarea][joy] 添加<code>Textarea</code>组件（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F33975" target="_blank">#33975</a>）</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>核心</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[核心] 提供<span> </span><code>OverridableComponent</code><span> </span>替代方案，通过模块增强获得更好的性能 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F32735" target="_blank">#32735</a><span> </span>)</li> 
 <li>[核心] 修复回归测试中的 prop-type 警告 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F34086" target="_blank">#34086</a><span> </span>)</li> 
 <li>[核心] 修复滚动恢复（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Fpull%2F34037" target="_blank">#34037</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmui%2Fmaterial-ui%2Freleases%2Ftag%2Fv5.10.3" target="_blank">https://github.com/mui/material-ui/releases/tag/v5.10.3</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            