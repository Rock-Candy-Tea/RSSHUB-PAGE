
---
title: 'Chrome 97 测试版发布，引入 WebTransport 协议框架等大量新特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1767'
author: 开源中国
comments: false
date: Fri, 19 Nov 2021 08:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1767'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">11 月 18日 ，谷歌公布了 Chrome 97 测试版的新特性，这些<span style="color:rgba(0, 0, 0, 0.87)">更改适用于适用于 Android、Chrome OS、Linux、macOS 和 Windows 的最新 Chrome 97 测试版本。</span><br> Chrome 97 测试版的新特性如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">自动展开详细信息元素</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">现在可以搜索封闭细节的元素，且可以链接到它们。使用页内查找（</span><code>find-in-page</code><span style="color:#2e3033">）、</span>滚动到文本片段（<span style="color:#2e3033"><code>ScrollToTextFragment</code>）和元素片段导航（</span><span style="color:rgba(0, 0, 0, 0.87)"><code>element fragment navigation</code></span><span style="color:#2e3033">）时，这些隐藏的元素也会自动展开。</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#2e3033">通过响应标头推送</span>传递内容安全策略</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:rgba(0, 0, 0, 0.87)">之前 Chrome 用了错误的所有者文档内容安全策略，现在</span>专职工作者由<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chromestatus.com%2Ffeature%2F5715844005888000" target="_blank">内容安全政策</a>管理。</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">CSS</h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新的 font-synthesis 属性</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><code>font-synthesis</code><span> </span><span style="color:#2e3033">CSS 属性控制当字体族在缺少斜面（</span><span style="color:rgba(0, 0, 0, 0.87)">oblique</span><span style="color:#2e3033">）、粗体（</span><span style="color:rgba(0, 0, 0, 0.87)"><span> </span>bold</span><span style="color:#2e3033">）和小型大写字母（</span><span style="color:rgba(0, 0, 0, 0.87)"><span> </span>small-caps</span><span style="color:#2e3033">）字体时，是否允许用户代理合成这三种字体。如果没有这个属性，一些没有必需变体的字体族的网页可能会有不自然的字体。</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">transform: perspective 支持 (none)参数</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033"><code>perspective()</code><span> </span>函数现在支持使用 'none' 作为参数，在动画的一个端点是单位矩阵的情况下，更容易使用perspective() 函数构建动画。</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#2e3033">新的键盘 API 特性策略</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Chrome 支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chromestatus.com%2Ffeature%2F5657965899022336" target="_blank">新的<code>dkeyboard-map</code>值，</a><code>Keyboard.getLayoutMap()</code><span> </span>与代码结合使用可以识别不同键盘布局（如英语和法语）的按键，此方法在 iframe 元素中不可用，某些无法使用键盘 API 的 Web 应用程序（Excel、Word 和 PowerPoint）的体系结构也现在可以使用。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新的 HTMLScriptElement.supports() 方法</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">HTMLScriptElement.supports() 方法提供了一种统一的方法来检测使用脚本元素的新特性。不过目前还没有决定好 HTMLScriptElement的type 的<span> </span></span><span style="color:rgba(0, 0, 0, 0.87)">type 属性</span><span style="color:#2e3033">可以使用哪些类型。关于此部分的内容可以参阅</span>以下几个使用脚本元素的新功能提案：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWICG%2Fimport-maps%2F" target="_blank">https://github.com/WICG/import-maps/ </a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeremyroman%2Falternate-loading-modes%2Fblob%2Fmain%2Ftriggers.md%23speculation-rules" target="_blank">https://github.com/jeremyroman/alternate-loading-modes/blob/main/triggers.md#speculation-rules<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWICG%2Fresource-bundles%2F" target="_blank">https://github.com/WICG /resource-bundles/</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">表单提交的换行规范化</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">表单条目中的换行符<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chromestatus.com%2Ffeature%2F5654547184746496" target="_blank">现在与 Gecko 和 WebKit 一样规范化</a>，解决了长期存在的互操作性问题，即 Gecko 和 WebKit 规范化换行符较晚，而 Chrome 较早进行。从 Chrome 97 开始，早期规范化被删除，后期规范化扩展到所有编码类型。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">标准化现有的客户端提示命名（Client Hint Naming）</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">Chrome 97 通过<span> </span></span><span style="color:rgba(0, 0, 0, 0.87)"><code>sec-ch-</code><span> </span>前缀来</span><span style="color:#2e3033">标准化客户端提示的名称，</span>受影响的客户端提示是<span> </span><code>dpr</code>、<code>width</code>、<code>viewport-width</code>、<code>device-memory</code>、<code>rtt</code>、<code>downlink</code>、和<code>ect</code>。Chrome 97 还在支持这些客户端提示。不过早晚会删除这个功能，建议开发人员做好准备。</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">WebTransport</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:rgba(0, 0, 0, 0.87)">WebTransport 是一个协议框架，它使受 Web 安全模型约束的客户端能够使用安全的多路复用传输与远程服务器进行通信。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前，Web 开发者有两个用于与远程服务器进行双向通信的 API：<code>WebSockets</code><span> </span>和<span> </span><code>RTCDataChannel</code>。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <code>WebSockets</code><span> </span>是基于 TCP 的，因此具有 TCP 的所有缺点（线头阻塞，缺乏对不可靠数据传输的支持），不适合对延迟敏感的应用程序。 </li> 
 <li><code>RTCDataChannel</code>基于流控制传输协议（SCTP），没有上述缺点；然而，它被设计用于对等环境，这导致它在客户端-服务器设置中的使用相当低。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> <code>WebTransport</code><span> </span>提供了一个客户端 - 服务器 API，支持不可靠和可靠数据的双向传输，使用类似 UDP 的数据报和可取消的流。<code>WebTransport</code><span> </span>调用在 DevTools 的 Network 面板中可见，并在 Type 列中标识。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">有关更多信息，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fweb.dev%2Fwebtransport%2F" target="_blank">使用 WebTransport 进行试验</a>。</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">JavaScript</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:rgba(0, 0, 0, 0.87)">Chrome 97 包含 V8 JavaScript 引擎最新的<span> </span></span><a href="https://www.oschina.net/news/169480/v8-release-9-7-released">9.7 版本</a>。可以在 V8 发行说明中找到<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv8.dev%2Fblog" target="_blank">最新功能</a>的完整列表。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><code>Array</code><span style="color:rgba(0, 0, 0, 0.87)"><span> </span>和<span> </span></span><code>TypedArray</code><span style="color:rgba(0, 0, 0, 0.87)"><span> </span>已支持<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeature%2F5693639729610752" target="_blank"><code>findLast()</code><span> </span>和<span> </span><code>fileLastIndex()</code></a><code>静态</code>方法。<span style="color:#2e3033">这些函数类似于<span> </span><code>find()</code><span> </span>和<span> </span><code>findIndex()</code>，不过从数组的末尾进行搜索，而不是开始。</span></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#2e3033">弃用和删除</span></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">删除 WebRTC 的 SDES 密钥交换</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:rgba(0, 0, 0, 0.87)">自 2013 年以来，WebRTC 的 SDES 密钥交换机制已在相关 IETF 标准中声明为“不支持”，</span>IETF 已宣布 SDES 规范具有历史意义。近年来，它在 Chrome 中的使用量显着下降，因此 Chrome 97 将它<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chromestatus.com%2Ffeature%2F5695324321480704" target="_blank">删除</a>。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">在第三方上下文中删除 WebSQL</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chromestatus.com%2Ffeature%2F5684870116278272" target="_blank">第三方上下文中的 WebSQL 现在已删除</a>。Web SQL 数据库标准于 2009 年 4 月首次提出，并于 2010 年 11 月放弃。Gecko<span> </span><strong>从未实现此功能</strong>，WebKit 在 2019 年就已经弃用了它。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">删除 SDP 的计划 B</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">用于在 WebRTC 中建立会话的会话描述协议 (SDP) ，在 Chromium 中使用两种不同的方言实现：统一计划和计划 B（<span style="color:rgba(0, 0, 0, 0.87)">Unified Plan and Plan B</span>）。计划 B 不能跨浏览器兼容，因此<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chromestatus.com%2Ffeatures%2F5823036655665152" target="_blank">删除</a>。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">公告原文：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.chromium.org%2F2021%2F11%2Fchrome-97-webtransport-new-array-static.html" target="_blank">https://blog.chromium.org/2021/11/chrome-97-webtransport-new-array-static.html</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            