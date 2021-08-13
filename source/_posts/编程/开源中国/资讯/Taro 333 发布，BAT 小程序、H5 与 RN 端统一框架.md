
---
title: 'Taro 3.3.3 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2300'
author: 开源中国
comments: false
date: Fri, 13 Aug 2021 07:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2300'
---

<div>   
<div class="content">
                                                                                            <p>Taro 3.3.3 发布了。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信/京东/百度/支付宝/字节跳动/ QQ 小程序/H5 等应用。此版本更新内容包括：</p> 
<h3>特性</h3> 
<h4>CLI</h4> 
<ul> 
 <li>Taro 插件增加 <code>modifyRunnerOpts</code> 钩子，暴露 Taro 的编译配置。</li> 
</ul> 
<h4>RN</h4> 
<ul> 
 <li>新增 4 个 location 相关的 API：<code>startLocationUpdate</code> <code>stopLocationUpdate</code> <code>onLocationChange</code> <code>offLocationChange</code></li> 
 <li><code>Switch</code> 组件支持 <code>disabled</code> 属性</li> 
</ul> 
<h3>修复</h3> 
<h4>小程序</h4> 
<ul> 
 <li>修复 <code>innerHTML</code> API 对 <code><style></code> 标签的解析问题，fix <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9885" target="_blank">#9885</a></li> 
 <li>修复开发微信小程序插件时编译报错的问题，fix <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9610" target="_blank">#9610</a></li> 
 <li>修复微信小程序插件中调用 Taro 的 APIs 时报错的问题，fix <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9587" target="_blank">#9587</a></li> 
</ul> 
<h4>H5</h4> 
<ul> 
 <li>修复使用 Vue 开发时，<code>picker</code> 组件的 <code>rangeKey</code> 属性为 undefined 的问题，fix <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9475" target="_blank">#9475</a> ，by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPerfectPan" target="_blank">@PerfectPan</a></li> 
 <li>修复 <code>Taro.setClipboardData</code> API 在写入复制内容的时候对换行符解析失效的问题，by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHhpon" target="_blank">@Hhpon</a></li> 
 <li>修复设置 <code>router.basename</code> 失效的问题，by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhaomengfan" target="_blank">@zhaomengfan</a></li> 
 <li>修复频繁跳转时会导致多页面共存的问题</li> 
</ul> 
<h4>RN</h4> 
<ul> 
 <li>修复 <code>Button</code> 组件缺乏按压效果的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9974" target="_blank">#9974</a></li> 
 <li>修复 Android 端，<code>View</code> 组件不设置背景色时点击无效的问题</li> 
 <li>修复 Android 端 <code>Radio</code> 组件的样式错误，并统一 iOS 和 Android 端 <code>Radio</code> 的样式</li> 
 <li>优化 <code>Keyboard</code> 相关 API 的实现</li> 
</ul> 
<h3>Typings</h3> 
<ul> 
 <li>优化 <code>Keyboard</code> 相关 API 的类型</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.3.3" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.3.3</a></p>
                                        </div>
                                      
</div>
            