
---
title: 'React Native 0.69 发布，首个支持 React 18 的版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1709'
author: 开源中国
comments: false
date: Fri, 24 Jun 2022 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1709'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">React Native 0.69<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freactnative.dev%2Fblog%2F2022%2F06%2F21%2Fversion-069" target="_blank"><span> </span>已发布</a>。此版本对新架构和新特性进行了多项改进，其中包括支持 React 18，以及与 Hermes 绑定发布。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>React 18</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">React Native 0.69 是第一个支持 React 18 的版本。React 18 带来了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freactjs.org%2Fblog%2F2022%2F03%2F29%2Freact-v18.html" target="_blank">许多改进</a>，比如新 hook<code>useId</code>，以及新的并发特性：<code>useTransition</code>和完整的 Suspense 支持。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#1c1e21">React Native 0.69 已默认启用 React 18。但如果开发者尚未迁移到新架构，则无法使用并发渲染和其他并发特性。开发团队表示<strong>无法为旧架构添加对并发渲染的支持</strong>。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freactnative.dev%2Fdocs%2Fnext%2Freact-18-and-react-native" target="_blank"><span style="color:#1c1e21">点此查看详情</span></a><span style="color:#1c1e21">。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>与 Hermes 绑定发布</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">在 0.69 之前，Hermes 和 React Native 是分开发布的。这会导致开发者无法区分两者之间哪个版本是互相兼容的。为了解决这个问题，从 React Native 0.69 开始，开发团队将同时发布与对应版本兼容的 Hermes。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>新架构值得关注的变化</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>放弃对 iOS/tvOS SDK 11.0 的支持，现在要求 12.4 或更高版本</li> 
 <li>为使用 M1 的 Android 开发者提供<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact-native%2Fcommit%2Fc5babd993a2bed2994ecc4710fa9e424b3e6cfc2" target="_blank">更好的支持</a></li> 
 <li>添加新<code>.xcode.env</code>配置文件，以更确定地获取节点可执行文件</li> 
 <li>React Native <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact-native%2Fcommit%2F50c8e973f067d4ef1fc3c2eddd360a0709828968" target="_blank">现在使用</a>来自 Android 11 的最新状态栏 API</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact-native%2Fcommit%2Fc2e4ae39b8a5c6534a3fa4dae4130166eda15169" target="_blank">支持 C++17</a></li> 
 <li>在 iOS debug 菜单中引入<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact-native%2Fcommit%2F1a1a304ed2023d60547aef65b1a7bf56467edf08" target="_blank">新的<code>hotkeysEnabled</code>选项</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact-native%2Fblob%2Fmain%2FCHANGELOG.md%230690" target="_blank">Changelog</a></p>
                                        </div>
                                      
</div>
            