
---
title: 'Taro 3.3.10 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2650'
author: 开源中国
comments: false
date: Tue, 19 Oct 2021 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2650'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Taro 3.3.10 发布了。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信/京东/百度/支付宝/字节跳动/ QQ 小程序/H5 等应用。此版本更新内容包括：</span></p> 
<h4>特性</h4> 
<p style="text-align:start"><strong>RN</strong></p> 
<ul> 
 <li>React Native 版本升级到<span> </span><code>0.66</code>，升级相关<span> </span><code>metro</code>，<span> </span><code>expo</code>，<code>@unimodules</code>依赖</li> 
</ul> 
<p style="text-align:start"><strong>CLI</strong></p> 
<ul> 
 <li>新增<span> </span><code>onBuildComplete</code><span> </span>钩子</li> 
 <li><code>registerMethod</code><span> </span>支持注册多个同名钩子</li> 
</ul> 
<h4>修复</h4> 
<p style="text-align:start"><strong>小程序</strong></p> 
<ul> 
 <li>京东小程序<span> </span><code>Map</code><span> </span>组件补充<span> </span><code>bindRegionChange</code><span> </span>事件</li> 
</ul> 
<p style="text-align:start"><strong>H5</strong></p> 
<ul> 
 <li>修复切换<span> </span><code>tab</code><span> </span>栏时，无限增加 DOM 节点的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10200" target="_blank">#10200</a></li> 
 <li>web components 组件保留传入的<span> </span><code>attribute</code></li> 
</ul> 
<p style="text-align:start"><strong>RN</strong></p> 
<ul> 
 <li>补全和优化部分组件的<span> </span><code>ts</code><span> </span>类型推断，移除大部分<span> </span><code>ts-ignore</code></li> 
 <li>修复<span> </span><code>Button</code><span> </span>组件卸载时与 app 退到后台时的 warning</li> 
 <li>修复<span> </span><code>Taro.compressImage</code><span> </span>压缩图片时将透明色变为黑色的问题</li> 
 <li>修复获取系统信息的 API：<code>getSystemInfo</code>、<code>getSystemInfoSync</code></li> 
 <li>调整<span> </span><code>navigationStyle</code><span> </span>配置的优先级：<code>page</code><span> </span>><span> </span><code>window</code></li> 
 <li>解决样式文件里面引入 npm 包文件失效问题</li> 
</ul> 
<p style="text-align:start"><strong>@tarojs/plugin-html</strong></p> 
<ul> 
 <li>修复插件对部分组件属性<span> </span><code>key</code><span> </span>值的错误映射导致的问题</li> 
</ul> 
<h4>Types</h4> 
<ul> 
 <li>补全<span> </span><code>LivePusher</code><span> </span>组件的属性的类型</li> 
 <li>修复<span> </span><code>Swiper</code><span> </span>组件<span> </span><code>onChange</code><span> </span>事件的回调类型问题</li> 
 <li>修复了<span> </span><code>readFileSync</code><span> </span>方法<span> </span><code>encoding</code><span> </span>参数的顺序</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.3.10" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.3.10</a> </p>
                                        </div>
                                      
</div>
            