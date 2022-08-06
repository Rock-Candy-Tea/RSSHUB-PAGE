
---
title: 'Taro 3.5.2 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2250'
author: 开源中国
comments: false
date: Sat, 06 Aug 2022 08:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2250'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Taro 3.5.2 现已发布。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信 / 京东 / 百度 / 支付宝 / 字节跳动 / QQ 小程序 / H5 等应用。具体更新内容如下：</span></p> 
<h2>特性</h2> 
<h3>H5</h3> 
<ul> 
 <li>新增支持 movable 组件 fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10767" target="_blank">#10767</a></li> 
 <li><strong>prebundle:</strong><span> </span>默认继承 webpack 配置，并支持开发者自定义拓展 fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12160" target="_blank">#12160</a></li> 
</ul> 
<h3>RN</h3> 
<ul> 
 <li><strong>taro-runtime-rn:</strong><span> </span>实现 useLoad 钩子 fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F12177" target="_blank">#12177</a></li> 
 <li><strong>taro-runtime-rn:</strong><span> </span>实现 useUnload 钩子 fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F12173" target="_blank">#12173</a></li> 
 <li>依赖版本升级，by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhiqingchen" target="_blank">@zhiqingchen</a></li> 
</ul> 
<h2>修复</h2> 
<h3>小程序</h3> 
<ul> 
 <li>优化主入口引用样式文件编译问题，by @顾一峰</li> 
</ul> 
<h3>H5</h3> 
<ul> 
 <li><strong>prebundle:</strong><span> </span>支持新版本 prefresh 热更新 fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12138" target="_blank">#12138</a></li> 
 <li><strong>prebundle:</strong><span> </span>react 框架默认排除 mobx 依赖预编译 fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12175" target="_blank">#12175</a></li> 
 <li><strong>router:</strong><span> </span>优化自定义路由入口判断 fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12214" target="_blank">#12214</a></li> 
</ul> 
<h3>RN</h3> 
<ul> 
 <li>修复 window 平台下编译报错问题 fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F12197" target="_blank">#12197</a></li> 
 <li><strong>rn-runner/rn-style:</strong><span> </span>修复 rollupTransform 参数格式化、丢失问题，并调整相关类型声明文件</li> 
 <li><strong>rn-style-transformer:</strong><span> </span>修复 scss nest importer 不执行问题</li> 
 <li><strong>rn-support/rn-runner:</strong><span> </span>支持 ios/android 文件读取 fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F12200" target="_blank">#12200</a></li> 
 <li><strong>rn:</strong><span> </span>编译组件时移除 clear dist 操作 fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12183" target="_blank">#12183</a></li> 
</ul> 
<h3>ELSE</h3> 
<ul> 
 <li><strong>postcss:</strong><span> </span>pxtransform 语法优化</li> 
 <li><strong>helper:</strong><span> </span>debug 依赖升级</li> 
</ul> 
<h2>Typings</h2> 
<ul> 
 <li>更新 video 组件类型</li> 
 <li>更新 JSX 组件类型缺失</li> 
 <li>更新组件 props 类型导出</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.5.2" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.5.2</a></p>
                                        </div>
                                      
</div>
            