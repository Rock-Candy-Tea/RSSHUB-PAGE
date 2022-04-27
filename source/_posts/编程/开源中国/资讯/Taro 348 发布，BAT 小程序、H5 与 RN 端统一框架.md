
---
title: 'Taro 3.4.8 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=674'
author: 开源中国
comments: false
date: Wed, 27 Apr 2022 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=674'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信/京东/百度/支付宝/字节跳动/ QQ 小程序/H5 等应用。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Taro 3.4.8 现已发布，具体更新内容如下：</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>特性</strong></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>H5</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>支持播放 hls 视频</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>修复</strong></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>小程序</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 React 组件里使用动态 import 会报错的问题</li> 
 <li>修复调用<span> </span><code>Taro.request</code><span> </span>后<span> </span><code>onHeadersReceived</code><span> </span>未定义的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11224" target="_blank">#11224</a></li> 
 <li>修复支付宝部分 API 未正确获取返回值的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11703" target="_blank">#11703</a></li> 
 <li>Vue3 暴露 vue-loader 配置项</li> 
 <li>修复百度小程序的<span> </span><code>Button</code><span> </span>组件不支持<span> </span><code>onLogin</code><span> </span>事件的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11546" target="_blank">#11546</a></li> 
 <li>支持微信小程序<span> </span><code>Input</code><span> </span>组件的安全键盘属性，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11315" target="_blank">#11315</a></li> 
 <li>支持字节小程序的<span> </span><code>RtcRoom</code><span> </span>组件，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11460" target="_blank">#11460</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>H5</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复安卓系统的浏览器中调用罗盘 API 无法获得绝对方向的问题</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>RN</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复<span> </span><code>showToast</code><span> </span>图标错误</li> 
 <li>修复 css module 行内使用<span> </span><code>Object.assign</code><span> </span>等<span> </span><code>callExpression</code><span> </span>问题</li> 
 <li>修复生产环境下 iOS 后退 crash 的问题</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>CLI</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>删除 CLI 冗余依赖，加快安装速度，修复使用 React JSX 时的类型报错，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11097" target="_blank">#11097</a></li> 
 <li>修复<span> </span><code>taro init</code><span> </span>没有为项目安装 devDependencies 的问题</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Typings</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 Vue3 tsx 无事件属性类型的问题</li> 
 <li>修复<span> </span><code>page.animate</code><span> </span>方法的类型问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11700" target="_blank">#11700</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.4.8" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.4.8</a></p>
                                        </div>
                                      
</div>
            