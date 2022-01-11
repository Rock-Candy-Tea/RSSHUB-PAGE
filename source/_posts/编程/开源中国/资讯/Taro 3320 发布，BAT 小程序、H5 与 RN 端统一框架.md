
---
title: 'Taro 3.3.20 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7352'
author: 开源中国
comments: false
date: Tue, 11 Jan 2022 07:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7352'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Taro 3.3.20 发布了。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信/京东/百度/支付宝/字节跳动/ QQ 小程序/H5 等应用。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">此版本更新内容包括：</span></p> 
<h2>特性</h2> 
<h3>小程序</h3> 
<ul> 
 <li>编译为原生小程序组件时，支持配置原生组件的 Options，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9759" target="_blank">#9759</a><span> </span>，by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffengkx" target="_blank">@fengkx</a></li> 
</ul> 
<h3>H5</h3> 
<ul> 
 <li>支持<span> </span><code>NodesRef.node</code><span> </span>方法，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9461" target="_blank">#9461</a></li> 
 <li>支持<span> </span><code>NodesRef.context</code><span> </span>方法（video & canvas）</li> 
</ul> 
<h2>性能</h2> 
<h3>小程序</h3> 
<ul> 
 <li>修复<span> </span><code>CustomWrapper</code><span> </span>嵌套使用后失效的问题，by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCS-Tao" target="_blank">@CS-Tao</a></li> 
 <li>优化<span> </span><code>MiniSplitChunksPlugin</code><span> </span>的运行性能，by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frquanx" target="_blank">@rquanx</a></li> 
</ul> 
<h2>修复</h2> 
<h3>小程序</h3> 
<ul> 
 <li>修复<span> </span><code>window.setTimeout</code><span> </span>和<span> </span><code>window.clearTimeout</code><span> </span>缺少返回值的问题，by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fblade254353074" target="_blank">@blade254353074</a></li> 
</ul> 
<h3>H5</h3> 
<ul> 
 <li>修复<span> </span><code>Input</code><span> </span>组件<span> </span><code>autoFocus</code><span> </span>属性，by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaosiqing" target="_blank">@baosiqing</a></li> 
 <li>修复<span> </span><code>CanvasContext</code><span> </span>关联方法失效问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10931" target="_blank">#10931</a></li> 
 <li>修复<span> </span><code>SelectViewport</code><span> </span>失效问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F7553" target="_blank">#7553</a></li> 
 <li>修复<span> </span><code>createInnerAudioContext</code><span> </span>方法监听事件名，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11002" target="_blank">#11002</a></li> 
 <li>修复<span> </span><code>chooseLocation</code><span> </span>方法取消事件，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11006" target="_blank">#11006</a></li> 
 <li>修复<span> </span><code>browser</code><span> </span>模式下<span> </span><code>search</code><span> </span>参数丢失问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11004" target="_blank">#11004</a></li> 
 <li>修复 app 中<span> </span><code>onLaunch</code>与<code>componentDidMount</code><span> </span>事件无法获取启动参数问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F8730" target="_blank">#8730</a></li> 
 <li>修复<span> </span><code>TabBar</code><span> </span>导致的页面高度问题</li> 
 <li>修复<span> </span><code>query</code><span> </span>导致的<span> </span><code>pageId</code><span> </span>问题</li> 
</ul> 
<h3>RN</h3> 
<ul> 
 <li>修复 Android 下<span> </span><code>TextArea</code><span> </span>居中问题</li> 
 <li>修复<span> </span><code>Button</code><span> </span>下有<span> </span><code>icon</code><span> </span>但是没有其他子元素不居中问题</li> 
</ul> 
<h2>Typings</h2> 
<ul> 
 <li>添加<span> </span><code>openVideoEditor</code><span> </span>方法的类型定义，by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flblblong" target="_blank">@lblblong</a></li> 
 <li>修复取消监听事件回调类型不匹配问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10954" target="_blank">#10954</a></li> 
 <li>更新 app 中<span> </span><code>useDidShow</code><span> </span>方法类型</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.3.20" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.3.20</a></p>
                                        </div>
                                      
</div>
            