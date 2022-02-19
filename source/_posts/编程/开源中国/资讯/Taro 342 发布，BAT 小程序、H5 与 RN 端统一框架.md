
---
title: 'Taro 3.4.2 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9794'
author: 开源中国
comments: false
date: Sat, 19 Feb 2022 07:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9794'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Taro 3.4.2 现已发布。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信/京东/百度/支付宝/字节跳动/ QQ 小程序/H5 等应用。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">此版本更新内容包括：</span></p> 
<h2>特性</h2> 
<h3>H5</h3> 
<ul> 
 <li>新增支持<span> </span><code>loadFontFace</code>、<code>getBatteryInfo</code>、<code>offNetworkStatusChange</code><span> </span>方法</li> 
 <li>新增支持<span> </span><code>getWindowInfo</code>、<code>getSystemSetting</code>、<code>getSystemInfoAsync</code>、<code>getDeviceInfo</code>、<code>getAppBaseInfo</code>、<code>getAppAuthorizeSetting</code><span> </span>方法</li> 
</ul> 
<h3>RN</h3> 
<ul> 
 <li>脚手架支持创建项目模板替换项目名<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11255" target="_blank">#11255</a></li> 
 <li>新增支持<span> </span><code>getFileSystemManager</code><span> </span>方法<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11277" target="_blank">#11277</a></li> 
 <li>支持 linaria<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11239" target="_blank">#11239</a></li> 
 <li>支持 border-[direction] 值简写<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11304" target="_blank">#11304</a></li> 
 <li>升级 react-native-root-siblings 并在app节点加入 RootSiblingParent<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11293" target="_blank">#11293</a></li> 
</ul> 
<h3>Harmony</h3> 
<ul> 
 <li>给 loaderMeta 增加 modifyInstantiate 配置</li> 
</ul> 
<h2>修复</h2> 
<h3>小程序</h3> 
<ul> 
 <li>修复小程序插件报错<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11278" target="_blank">#11278</a></li> 
 <li>修复 preact 小程序生命周期不触发的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11180" target="_blank">#11180</a></li> 
 <li>修复 preact 设置属性为<span> </span><code>false</code><span> </span>值时不生效的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11197" target="_blank">#11197</a></li> 
 <li>修复编译小程序插件时不能使用<span> </span><code>plugin-html</code><span> </span>的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10527" target="_blank">#10527</a></li> 
 <li>修复编译小程序插件时不能触发分享的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10105" target="_blank">#10105</a></li> 
 <li>开发小程序插件时暴露原生页面对象给开发者，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9889" target="_blank">#9889</a></li> 
 <li>更新默认模板的 stylelint 版本</li> 
</ul> 
<h3>H5</h3> 
<ul> 
 <li>修复监听方法指向错误问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11202" target="_blank">#11202</a></li> 
 <li>修复 Tabbar 默认高度问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11265" target="_blank">#11265</a></li> 
 <li>修复 Input 组件 target 绑定值问题，用以修复相关框架依赖的功能<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10836" target="_blank">#10836</a></li> 
 <li>优化 Input 组件输入法合成与复制事件时的返回值</li> 
 <li>移除 webpack-runner 不必要的依赖 fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11097" target="_blank">#11097</a><span> </span>fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11237" target="_blank">#11237</a></li> 
 <li>优化 scroll-container 获取方案<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11206" target="_blank">#11206</a></li> 
 <li>优化 pull-to-refresh 组件（页面遮挡 & Slot 导致的热更新问题）</li> 
</ul> 
<h3>RN</h3> 
<ul> 
 <li>修复 Picker 对日期格式的支持，Hermes 与 jsc 不一致，改为都支持的模式<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11191" target="_blank">#11191</a></li> 
 <li>修复 Android 11加载相册 loading 态问题 #111671</li> 
 <li>修复关闭 scalable value 有多个单位时只有第一个值不转换成 scalePx2dp<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11300" target="_blank">#11300</a></li> 
 <li>优化尺寸转换的计算方式，让 rem 表现与小程序一致<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11260" target="_blank">#11260</a></li> 
 <li>修复 View 包裹文案事件绑定时，点击有背景色<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11285" target="_blank">#11285</a></li> 
</ul> 
<h3>Harmony</h3> 
<ul> 
 <li>修改 TaroEvent 的 target 和 currentTarget 属性的实现</li> 
 <li>修复使用 preact 时 eslint 报错的问题</li> 
 <li>修复 Input 组件 onDestory时，取消键盘监听异常<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11252" target="_blank">#11252</a></li> 
</ul> 
<h2>Typings</h2> 
<ul> 
 <li>优化模板引用类型方式<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11222" target="_blank">#11222</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11223" target="_blank">#11223</a></li> 
 <li>优化类型 & 补充缺失方法<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fpull%2F11210" target="_blank">#11210</a></li> 
</ul> 
<h2>@tarojs/plugin-mini-ci</h2> 
<ul> 
 <li>向下兼容</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.4.2" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.4.2</a> </p>
                                        </div>
                                      
</div>
            