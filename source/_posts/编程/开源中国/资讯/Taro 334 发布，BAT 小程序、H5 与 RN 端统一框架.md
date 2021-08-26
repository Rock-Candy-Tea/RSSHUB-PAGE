
---
title: 'Taro 3.3.4 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6337'
author: 开源中国
comments: false
date: Thu, 26 Aug 2021 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6337'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Taro 3.3.4 发布了。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信/京东/百度/支付宝/字节跳动/ QQ 小程序/H5 等应用。此版本更新内容包括：</p> 
<h4><strong>特性</strong></h4> 
<h4><strong>RN</strong></h4> 
<ul> 
 <li> <p>增加 <code>enableMergeStyle</code> 选项，对 JSX 标签 <code>style</code> 属性数组 (Array) 转换为对象 (Object)</p> </li> 
</ul> 
<h4><strong>修复</strong></h4> 
<h4><strong>小程序</strong></h4> 
<ul> 
 <li> <p>补全微信小程序的 <code>exitMiniProgram</code> API，fix <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10030" target="_blank">#10030</a> ，by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftu6ge" target="_blank">@tu6ge</a></p> </li> 
 <li>修复 <code>optimizeMainPackage</code> 配置在打包原生小程序页面时无法生效的问题</li> 
 <li>修复 Vue 2/3 不能正确使用端平台插件的问题，fix <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10098" target="_blank">#10098</a></li> 
 <li>修复多次调用 <code>innerHTML</code> 时旧节点没有正确卸载的问题，fix <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10108" target="_blank">#10108</a></li> 
 <li>修复 Vue3.2+ 版本静态节点渲染报错的问题，fix <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10077" target="_blank">#10077</a></li> 
 <li>修复使用 Vue <code>v-for</code> 指令时百度小程序 <code>swiper</code> 组件显示空白页的问题，fix <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9941" target="_blank">#9941</a></li> 
</ul> 
<p><strong>H5</strong></p> 
<ul> 
 <li>修复获取当前路由 <code>path</code> 未过滤 <code>basename</code> 的问题，by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhaomengfan" target="_blank">@zhaomengfan</a></li> 
</ul> 
<p><strong>RN</strong></p> 
<ul> 
 <li>修复打包后 <code>CheckBox</code> 和 <code>Radio</code> 报错的问题</li> 
 <li>修复 release 包 <code>child.type.name</code> 错误的问题</li> 
 <li>修复 <code>createRoute</code> 中关于 <code>tabbar</code>的判断</li> 
 <li>让 <code>npm scripts</code> 中的 <code>assets</code> 兼容 win 平台</li> 
 <li>增加对除 <code>page</code> 页面的组件的全局样式补充，npm 包支持需配置 <code>rn.resolve</code></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.3.4" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.3.4</a> </p>
                                        </div>
                                      
</div>
            