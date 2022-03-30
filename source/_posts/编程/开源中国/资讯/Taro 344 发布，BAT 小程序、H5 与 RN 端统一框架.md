
---
title: 'Taro 3.4.4 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6981'
author: 开源中国
comments: false
date: Wed, 30 Mar 2022 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6981'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="color:#333333">Taro 3.4.4 现已发布。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信/京东/百度/支付宝/字节跳动/ QQ 小程序/H5 等应用。</span></p> 
<h2><strong>特性</strong></h2> 
<h3 style="margin-right:0; text-align:start"><strong>小程序</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>支持 Vue3 Class Component，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11392" target="_blank">#11392</a></li> 
 <li>新增对微信小程序<span> </span><code>ShareElement</code><span> </span>组件的支持，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11466" target="_blank">#11466</a></li> 
 <li>让微信小程序的<span> </span><code>Input</code><span> </span>组件支持使用<span> </span><code>KeyboardAccessory</code><span> </span>组件，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11510" target="_blank">#11510</a></li> 
</ul> 
<h3 style="margin-right:0; text-align:start"><strong>RN</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>升级<span> </span><code>@react-native-community/cli</code><span> </span>为<span> </span><code>^6.0.0</code>，与 react native 0.67 保持一致</li> 
 <li>当<span> </span><code>style</code><span> </span>为 array 类型时转换为 object 类型，保持各端操作的一致性</li> 
</ul> 
<h3 style="margin-right:0; text-align:start"><strong>@tarojs/plugin-inject</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>支持自定义以<span> </span><code>bind</code><span> </span>或<span> </span><code>catch</code><span> </span>绑定事件</li> 
</ul> 
<h2 style="margin-left:0em; margin-right:0; text-align:start"><strong>修复</strong></h2> 
<h3 style="margin-left:0em; margin-right:0; text-align:start"><strong>小程序</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复编译支付宝小程序插件时，生成的<span> </span><code>plugin.json</code><span> </span>缺少<span> </span><code>pages</code><span> </span>配置的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11361" target="_blank">#11361</a></li> 
 <li>修复小程序插件无法使用 Taro hooks 的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11373" target="_blank">#11373</a>，</li> 
 <li>修复编译小程序插件时配合使用 devtools 插件会报错的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11438" target="_blank">#11438</a>，</li> 
 <li>修复使用<span> </span><code>@tarojs/plugin-html</code><span> </span>时引入的 HTML 样式权重问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11487" target="_blank">#11487</a>，</li> 
 <li>修复使用原生写法的自定义<span> </span><code>Tabbar</code><span> </span>失败的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11437" target="_blank">#11437</a></li> 
 <li>修复开启 Vue3 的<span> </span><code>__VUE_OPTIONS_API__</code><span> </span>配置会让 Taro composition API 失效的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11393" target="_blank">#11393</a></li> 
 <li>修复 Vue3 使用原生组件时事件触发失败的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9794" target="_blank">#9794</a></li> 
 <li>让<span> </span><code>Slot</code><span> </span>组件支持设置 style 属性，借此支持<span> </span><code>ScrollView</code><span> </span>自定义下拉刷新组件，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11495" target="_blank">#11495</a></li> 
</ul> 
<h3 style="margin-left:0em; margin-right:0; text-align:start"><strong>H5</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>路由不对 query 进行 decode，与小程序保持一致</li> 
</ul> 
<h3 style="margin-left:0em; margin-right:0; text-align:start"><strong>RN</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复<span> </span><code>request</code><span> </span>对<span> </span><code>header content-type</code><span> </span>的处理，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11505" target="_blank">#11505</a><span> </span>，</li> 
 <li>修复<span> </span><code>Form</code><span> </span>组件包含 image 的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11456" target="_blank">#11456</a></li> 
 <li>修复<span> </span><code>framework</code><span> </span>配置为<span> </span><code>preact</code><span> </span>时报错的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11490" target="_blank">#11490</a></li> 
 <li>修复当<span> </span><code>Input</code><span> </span>组件未设置 value 时，<code>Form</code><span> </span>重复提交会重置<span> </span><code>Input</code><span> </span>等组件的值的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11473" target="_blank">#11473</a></li> 
</ul> 
<h3 style="margin-left:0em; margin-right:0; text-align:start"><strong>CLI</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复<span> </span><code>taro-doctor</code><span> </span>命令，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10648" target="_blank">#10648</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11253" target="_blank">#11253</a></li> 
</ul> 
<h2 style="margin-left:0em; margin-right:0; text-align:start"><strong>Typings</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>为<span> </span><code>Button</code><span> </span>组件完善<span> </span><code>getPhoneNumber</code><span> </span>的类型，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11454" target="_blank">#11454</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.4.4" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.4.4</a></p>
                                        </div>
                                      
</div>
            