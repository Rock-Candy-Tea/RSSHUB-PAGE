
---
title: 'Taro 3.4.14 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5112'
author: 开源中国
comments: false
date: Sun, 24 Jul 2022 07:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5112'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Taro 3.4.14 现已发布。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信 / 京东 / 百度 / 支付宝 / 字节跳动 / QQ 小程序 / H5 等应用。具体更新内容如下：</span></p> 
<h2 style="text-align:start">特性</h2> 
<h3 style="text-align:start">CLI</h3> 
<ul> 
 <li>支持使用包管理器的<span> </span><code>create</code><span> </span>命令创建 Taro 项目，如：<code>yarn create @tarojs/app</code></li> 
</ul> 
<h3 style="text-align:start">RN</h3> 
<ul> 
 <li>支持获取原生<span> </span><code>View</code><span> </span>组件的 ref 引用，将原生<span> </span><code>View</code><span> </span>组件的 ref 挂在<span> </span><code>ref.current.$ref</code><span> </span>属性上</li> 
 <li>支持在 style 文件中 (css, sass...)，使用<span> </span><code>vw</code>,<span> </span><code>vh</code><span> </span>等单位</li> 
</ul> 
<h2 style="text-align:start">修复</h2> 
<h3 style="text-align:start">小程序</h3> 
<ul> 
 <li>补充对淘宝小程序<span> </span><code>ArCamera</code><span> </span>组件的支持</li> 
</ul> 
<h3 style="text-align:start">H5</h3> 
<ul> 
 <li>优化<span> </span><code>Swiper</code><span> </span>组件的样式引入，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12034" target="_blank">#12034</a></li> 
</ul> 
<h3 style="text-align:start">CLI</h3> 
<ul> 
 <li>修复<span> </span><code>taro build</code><span> </span>命令设置<span> </span><code>port</code><span> </span>参数无效的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12024" target="_blank">#12024</a></li> 
</ul> 
<h3 style="text-align:start">@tarojs/plugin-react-devtools</h3> 
<ul> 
 <li>修复 react devtools 在 wsl2 下使用报错的问题</li> 
</ul> 
<h2 style="text-align:start">Typings</h2> 
<ul> 
 <li>补充<span> </span><code>getFuzzyLocation</code><span> </span>的类型</li> 
 <li>添加<span> </span><code>vibrateShort</code><span> </span>API震动参数类型</li> 
 <li>修复<span> </span><code>canvasToTempFilePath.Option.canvas</code><span> </span>类型错误问题</li> 
 <li>修复<span> </span><code>uploadFile/downloadFile</code><span> </span>返回结果类型不正确的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12048" target="_blank">#12048</a></li> 
 <li>补充<span> </span><code>RequestParams</code><span> </span>缺省类型，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12047" target="_blank">#12047</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.4.14" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.4.14</a></p>
                                        </div>
                                      
</div>
            