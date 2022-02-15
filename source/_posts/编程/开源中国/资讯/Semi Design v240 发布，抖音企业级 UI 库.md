
---
title: 'Semi Design v2.4.0 发布，抖音企业级 UI 库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=107'
author: 开源中国
comments: false
date: Tue, 15 Feb 2022 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=107'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Semi Design 是现代、全面、灵活的设计系统和 UI 库，由字节跳动抖音前端与 UED 团队设计、开发并维护，是一款包含设计语言、React 组件、主题等开箱即用的中后台解决方案，可用于快速搭建美观的 React 应用。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">目前 Semi Design 发布了 v2.4.0 版本，此版本带来以下变化：</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">【Fix】</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>TimePicker 崩溃问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDouyinFE%2Fsemi-design%2Fissues%2F585" target="_blank">#585</a></li> 
 <li>修复 Nav limitIndent 在折叠态后，子菜单通过 dropdown 形式展示时，也被消费，从而导致了多余的空白间隔的问题</li> 
 <li>修复 Typography 组件截断错误，当设置 whiteSpace 为 'pre-line' 且 expandable</li> 
 <li>修复 TreeSelect 当 treeData 较大时，由于多余的转化为 Set 的操作，造成 update 变得很慢<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDouyinFE%2Fsemi-design%2Fissues%2F521" target="_blank">#521</a></li> 
 <li>修复 TreeSelect 在单选且非受控时，treeData 更新后，已选值会被异常清空的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDouyinFE%2Fsemi-design%2Fissues%2F515" target="_blank">#515</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">【Style】</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>更新了 Button、Input、Modal、Select、ScrollList、TreeSelect 的部分 Sass 变量，抽取了部分默认样式为 Sass 变量以方便 DSM 修改组件默认样式<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDouyinFE%2Fsemi-design%2Fpull%2F570" target="_blank">#570</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDouyinFE%2Fsemi-design%2Freleases%2Ftag%2Fv2.4.0" target="_blank">https://github.com/DouyinFE/semi-design/releases/tag/v2.4.0</a></p>
                                        </div>
                                      
</div>
            