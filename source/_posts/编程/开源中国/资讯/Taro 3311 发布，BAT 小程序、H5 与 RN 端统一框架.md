
---
title: 'Taro 3.3.11 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=780'
author: 开源中国
comments: false
date: Wed, 27 Oct 2021 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=780'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Taro<span> </span></span>3.3.11<span> </span><span style="color:#333333">发布了。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信/京东/百度/支付宝/字节跳动/ QQ 小程序/H5 等应用。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">此版本更新内容包括：</span></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">新特性</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>小程序：</strong>新增对百度小程序<span> </span><code><Login></code><span> </span>组件的支持，fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10452" target="_blank">#10452</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">问题修复</h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">小程序</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>补充<code>Map</code><span> </span>组件的<span> </span><code>min-scale</code><span> </span>和<span> </span><code>max-scale</code><span> </span>属性，fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10239" target="_blank">#10239</a></li> 
 <li>修复当 import 引用<span> </span><code>@tarojs/taro/html5.css</code><span> </span>后报错的问题，fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10340" target="_blank">#10340</a></li> 
 <li>修复<span> </span><code>MiniSplitChunksPlugin</code><span> </span>对非微信小程序的小程序平台的支持，fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10478" target="_blank">#10478</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10439" target="_blank">#10439</a></li> 
 <li>修复设置<span> </span><code>style</code><span> </span>为<span> </span><code>pointer-events: none</code><span> </span>时失败的问题，fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10344" target="_blank">#10344</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">RN</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复<span> </span><code>componentDidShow</code>,<span> </span><code>componentDidHide</code>,<span> </span><code>useDidHide</code>,<span> </span><code>useDidShow</code><span> </span>的触发时机</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">CLI</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复在<span> </span><code>app.config.js</code><span> </span>使用<span> </span><code>fs</code><span> </span>或<span> </span><code>path</code><span> </span>依赖时报错的问题</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">Typing</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>补全、优化数据上报 API 的类型</li> 
 <li>补全音频播放 API 的类型</li> 
 <li>补充<span> </span><code>openSetting</code><span> </span>API 的参数类型，fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10032" target="_blank">#10032</a></li> 
 <li>补充<span> </span><code>openCustomerServiceChat</code><span> </span>的类型，fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10226" target="_blank">#10226</a></li> 
 <li>补充<span> </span><code>previewMedia</code><span> </span>API的类型，fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10232" target="_blank">#10232</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">其它</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>优化命令行输出</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.3.11" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.3.11</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            