
---
title: 'Taro 3.3.15 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3169'
author: 开源中国
comments: false
date: Wed, 24 Nov 2021 06:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3169'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Taro 3.3.15 发布了。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信/京东/百度/支付宝/字节跳动/ QQ 小程序/H5 等应用。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">此版本更新内容包括：</span></p> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>特性</strong></h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>H5</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">支持 <code>CoverView</code>、<code>CoverImage</code> 组件</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>RN</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>优化依赖，包括升级 <code>react-native-netinfo</code> ，删除 <code>expo-location</code> 依赖等，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F10690" target="_blank">#10690</a></li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>修复</strong></h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>小程序</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>增加对 <code>getLocalIPAddress</code> API 的支持，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10631" target="_blank">#10631</a></li> 
 <li>修复 Vue3 <code>Input</code> 组件设置自动聚焦失败的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10579" target="_blank">#10579</a></li> 
 <li>修复使用 <code>recoil</code> 报错的问题，fix <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10119" target="_blank">#10119</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>H5</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>支持使用<strong>相对路径</strong>地址跳转到新页面，by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaosiqing" target="_blank">@baosiqing</a></li> 
 <li>优化 <code>Input</code> 组件设置 <code>focus</code> 的时机，by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaosiqing" target="_blank">@baosiqing</a></li> 
 <li>修复浏览器多级后退造成的错误，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10616" target="_blank">#10616</a></li> 
 <li>修复快速切换 TabBar 时，页面展示错误的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10426" target="_blank">#10426</a></li> 
 <li>修复 <code>showTabBarRedDot</code>、<code>showTabBarBadge</code>、<code>setTabBarItem</code>、<code>setTabBarStyle</code> 等 <code>TabBar</code> 相关的 API，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9397" target="_blank">#9397</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F8580" target="_blank">#8580</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F8175" target="_blank">#8175</a></li> 
 <li>修复 Vue2 的组件使用 <code>nativeProps</code> 失效的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10689" target="_blank">#10689</a></li> 
 <li>修复 <code>Textarea</code> 组件 <code>onLineChange</code>、<code>autoHeight</code> 属性无效的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F7997" target="_blank">#7997</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F8003" target="_blank">#8003</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>RN</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 Windows 通过模板初始化 RN 报错的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10485" target="_blank">#10485</a></li> 
 <li>把 <code>networkType</code> 返回内容与小程序对齐</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>其它</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>增加对 <strong>nodejs 16 和 17</strong> 的支持</li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Typings</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li>优化类型实体写法，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10652" target="_blank">#10652</a></li> 
 <li>补充 <code>offMemoryWarning</code> API 的类型</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.3.15" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.3.15</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            