
---
title: 'Taro 3.5.4 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1083'
author: 开源中国
comments: false
date: Wed, 24 Aug 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1083'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Taro 3.5.4 现已发布。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信 / 京东 / 百度 / 支付宝 / 字节跳动 / QQ 小程序 / H5 等应用。具体更新内容如下：</span></p> 
<h2>特性</h2> 
<h3>H5</h3> 
<ul> 
 <li>Swiper 组件 onChange 事件触发时机优化，对齐小程序平台<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10764" target="_blank">#10764</a></li> 
</ul> 
<h3>RN</h3> 
<ul> 
 <li>Windows 下使用大号二维码优化体验</li> 
</ul> 
<h2>修复</h2> 
<h3>小程序</h3> 
<ul> 
 <li>修复 prebundle 特性下，不必要的 splitChunks 配置<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12281" target="_blank">#12281</a></li> 
 <li><strong>tt:</strong><span> </span>优化原生组件重复 ID 问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12281" target="_blank">#12281</a></li> 
 <li><strong>tt:</strong><span> </span>补充字节小程序Video组件属性和事件</li> 
 <li>修复配置 enableSourceMap 后未在生产模式下产出 sourcemap</li> 
 <li><strong>shared:</strong><span> </span>修复在不同平台生成的模板不一致的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12320" target="_blank">#12320</a></li> 
</ul> 
<h3>H5</h3> 
<ul> 
 <li>Input 组件在 Safari 下，联想输入导致的事件触发问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12326" target="_blank">#12326</a></li> 
 <li>修复 prebundle 特性下，用户自定义 proxy 合并错误问题</li> 
 <li>修复 prebundle 特性下，生产环境的错误 chunkId 配置<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12279" target="_blank">#12279</a></li> 
</ul> 
<h3>RN</h3> 
<ul> 
 <li>页面为函数式组件时不再额外包裹 View<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12305" target="_blank">#12305</a></li> 
 <li><strong>taro-runtime-rn:</strong><span> </span>修复rn 函数式组件中hook多实例触发问题</li> 
</ul> 
<h3>Typing</h3> 
<ul> 
 <li>修正 Video 组件的 onWaiting 事件注释<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12329" target="_blank">#12329</a></li> 
 <li>补充 Video 组件相关配置，以及支持程度说明</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.5.4" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.5.4</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            