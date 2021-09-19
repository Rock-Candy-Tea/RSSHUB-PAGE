
---
title: 'Taro 3.3.9 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4262'
author: 开源中国
comments: false
date: Sun, 19 Sep 2021 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4262'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p><span style="color:#333333">Taro 3.3.9 发布了。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信/京东/百度/支付宝/字节跳动/ QQ 小程序/H5 等应用。此版本更新内容包括：</span></p> 
 <h4>特性</h4> 
 <p><strong>小程序</strong></p> 
 <ul> 
  <li>新增 Taro 小程序端构建后支持CI（持续集成）的插件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Fplugin-mini-ci" target="_blank">@taorjs/plugin-mini-ci</a>。支持构建完毕后自动打开小程序开发者工具、上传作为体验版、生成预览二维码（暂时仅支持微信、字节、百度、支付宝小程序）</li> 
 </ul> 
 <p><strong>H5</strong></p> 
 <ul> 
  <li>组件可以使用新增的 <code>nativeProps</code> 属性，透传非标准属性到 WebComponents 内部，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F8219" target="_blank">#8219</a></li> 
 </ul> 
 <p><strong>修复</strong></p> 
 <ul> 
  <li>修复潜在的 ReDoS 攻击漏洞</li> 
 </ul> 
 <p><strong>小程序</strong></p> 
 <ul> 
  <li>修复使用 <code>@tarojs/plugin-inject</code> 插件时，部分 API 错误的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10288" target="_blank">#10288</a></li> 
  <li>修复 <code>Illegal invocation</code> 报错，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9888" target="_blank">#9888</a></li> 
 </ul> 
 <p><strong>H5</strong></p> 
 <ul> 
  <li>修复 <code>babel-preset-taro</code> 配置设置 <code>useBuiltIns: usage</code> 后报错的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10201" target="_blank">#10201</a></li> 
  <li>修复 H5 模式打包页面后在安卓低端机上白屏报错的问题</li> 
 </ul> 
 <p><strong>@tarojs/plugin-html</strong></p> 
 <ul> 
  <li>不处理 HTML 的 <code><map></code> 标签，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10280" target="_blank">#10280</a></li> 
  <li>修复启动 CLI 命令报错的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10284" target="_blank">#10284</a></li> 
 </ul> 
 <h4>Typings</h4> 
 <ul> 
  <li>补全 Taro 插件的 <code>applyPlugins</code> 钩子的声明</li> 
 </ul> 
 <p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.3.9" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.3.9</a> </p> 
</div>
                                        </div>
                                      
</div>
            