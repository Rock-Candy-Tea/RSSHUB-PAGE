
---
title: 'Taro 3.3.17 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8727'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 07:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8727'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Taro 3.3.17 发布了。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信/京东/百度/支付宝/字节跳动/ QQ 小程序/H5 等应用。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">此版本更新内容包括：</span></p> 
<h2 style="text-align:start">特性</h2> 
<h3 style="text-align:start">H5</h3> 
<ul> 
 <li>支持全局配置<span> </span><code>entryPagePath</code></li> 
 <li>支持多路由自定义配，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9289" target="_blank">#9289</a></li> 
</ul> 
<h3 style="text-align:start">RN</h3> 
<ul> 
 <li>支持 SVG 文件的引入</li> 
 <li>支持使用 playground 预览本地 bundle，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10867" target="_blank">#10867</a></li> 
</ul> 
<h2 style="text-align:start">修复</h2> 
<h3 style="text-align:start">小程序</h3> 
<ul> 
 <li>修复<span> </span><code>Textarea</code><span> </span>设置<span> </span><code>autoFocus</code><span> </span>属性时报错的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10870" target="_blank">#10870</a></li> 
 <li>优化 HTML 解析器对 CSS 属性选择器的解析</li> 
 <li>修复 Vue3 首次进入页面会触发两次<span> </span><code>onShow</code><span> </span>的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10728" target="_blank">#10728</a></li> 
 <li>修复支付宝小程序使用 v2.0 构建时使用<span> </span><code>Slot</code><span> </span>会报错的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10162" target="_blank">#10162</a></li> 
 <li>修复百度小程序<span> </span><code>Text</code><span> </span>嵌套不显示的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10829" target="_blank">#10829</a></li> 
 <li>修复微信小程序热重载报错的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10722" target="_blank">#10722</a></li> 
 <li>支持字节小程序<span> </span><code>Canvas</code><span> </span>v2.0，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10882" target="_blank">#10882</a></li> 
 <li>修复 Vue2<span> </span><code>video</code><span> </span>组件不能设置<span> </span><code>muted</code><span> </span>的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9550" target="_blank">#9550</a></li> 
 <li>优化对 vant weapp 的兼容，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10337" target="_blank">#10337</a></li> 
</ul> 
<h3 style="text-align:start">H5</h3> 
<ul> 
 <li>修复配置<span> </span><code>basename</code><span> </span>后没有设置上页面标题的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10862" target="_blank">#10862</a></li> 
 <li>修复使用<span> </span><code>Block</code><span> </span>组件会创建真实节点的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10285" target="_blank">#10285</a></li> 
 <li>修复页面滚动条共享的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F7974" target="_blank">#7974</a></li> 
 <li>修复 reLaunch 未清空路由栈和页面问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F9724" target="_blank">#9724</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F8347" target="_blank">#8347</a></li> 
 <li>修复上页索引计算错误，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10903" target="_blank">#10903</a></li> 
 <li>改变构建方式，使 H5 API 可以直接使用已有类型</li> 
 <li>修改 H5 目录结构，梳理当前缺失 API 并补充部分</li> 
 <li>修复 Taro-H5 Tree Shaking 问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10466" target="_blank">#10466</a></li> 
 <li>修复 API 关联 Issue<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10823" target="_blank">#10823</a></li> 
</ul> 
<h3 style="text-align:start">RN</h3> 
<ul> 
 <li>修复<span> </span><code>Picker</code><span> </span>日期和时间属性当初始化值为空时无法变更值的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10405" target="_blank">#10405</a></li> 
 <li>修复 ReLaunch 到 Tabbar 页错误的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10801" target="_blank">#10801</a></li> 
</ul> 
<h3 style="text-align:start">@tarojs/plugin-html</h3> 
<ul> 
 <li>修复错误过滤样式中<span> </span><code>*</code><span> </span>的问题</li> 
</ul> 
<h2 style="text-align:start">Typings</h2> 
<ul> 
 <li>优化<span> </span><code>showActionSheet</code><span> </span>的类型</li> 
 <li>修复没有导出 Events 类型的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10880" target="_blank">#10880</a></li> 
 <li>修改 Button OpenType 类型</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.3.17" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.3.17</a></p>
                                        </div>
                                      
</div>
            