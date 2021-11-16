
---
title: 'Chrome 96 稳定版发布，启用桌面后退缓存'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6798'
author: 开源中国
comments: false
date: Tue, 16 Nov 2021 08:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6798'
---

<div>   
<div class="content">
                                                                                            <p>Chrome 96 稳定版发布了，稳定版增加了 15 个新特性，包含一些开发人员功能、用户体验改进和安全更新内容。</p> 
<p>新特性：</p> 
<h2 style="margin-left:0px">桌面后退缓存</h2> 
<p style="margin-left:0px">为访问的页面创建缓存，允许即时恢复到以前访问过的页面。</p> 
<h2 style="margin-left:0px">CSS @counter-style 描述符 ''speak-as''</h2> 
<p style="margin-left:0px">“speak-as” 描述符用于描述如何用给定的样式来合成计数器的语音形式。</p> 
<h2 style="margin-left:0px">媒体查询：首选对比功能</h2> 
<p style="margin-left:0px">添加“首选对比度”功能，允许开发者根据用户在操作系统中选择的对比度级别来调整 Web 的对比度。有效选项为“更多”、“更少”、“自定义”或“无偏好”。</p> 
<h2 style="margin-left:0px">剪贴板：保留 PNG 元数据</h2> 
<p style="margin-left:0px">现在将 PNG 复制到剪贴板会保留 PNG 元数据，而不是在读取时清理系统剪贴板中的图像数据，因为这种行为与其他浏览器供应商和其他形式的导入图像不一致，例如 <input type="file">。</p> 
<h2 style="margin-left:0px">WebAssembly 引用类型</h2> 
<p style="margin-left:0px">允许 WebAssembly 模块保存对 JS/DOM 对象的引用，将它们作为参数传递，将它们存储在局部变量和全局变量中，并将它们存储在 WebAssembly.Table 对象中。</p> 
<h2 style="margin-left:0px">被包含时，禁止将 body 的样式传播到视图</h2> 
<p style="margin-left:0px">在 root 元素或 body 元素中使用非 none 的值，会禁止从 body 中传播 CSS 属性，详情可参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdrafts.csswg.org%2Fcss-contain-1%2F%23c3" target="_blank">drafts.c​​sswg.org/css-contain-1/#c3</a></p> 
<h2 style="margin-left:0px">在只支持整数的地方添加 calc(number) 的 CSS </h2> 
<p style="margin-left:0px">解析为 <number> 的 CSS 数学函数：calc(number)  ，现在可以在只接受整型的地方使用，（四舍五入到最接近的整数。）</p> 
<h2 style="margin-left:0px">自动从 HTTP 到 HTTPS 重定向</h2> 
<p style="margin-left:0px">如果 Chrome 检测到网站部署了 HTTPS DNS 记录 ，将始终通过 HTTPS 连接到该网站。目前只涵盖了 HTTP->HTTPS 升级部分。</p> 
<h2 style="margin-left:0px">删除 FTP 支持</h2> 
<p style="margin-left:0px">FTP 支持在 Chrome 95 版本就已经移除了，这里是彻底删除掉。</p> 
<h2 style="margin-left:0px">新的数据属性</h2> 
<p style="margin-left:0px">新的用于测量实时通信 (RTC) 系统中的 A/V 同步和端到端延迟的数据属性，<code>captureTimestamp</code> 和 <code>senderCaptureTime</code>，被添加到 <code>RTCRtpContributingSource</code>，由<code>RTCRtpReceiver.getContributingSources()</code> 返回。详情可参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fw3c.github.io%2Fwebrtc-extensions%2F%23rtcrtpcontributingsource-dictionary." target="_blank">w3c.github.io/webrtc-extensions/#rtcrtpcontributingsource-dictionary。</a></p> 
<p style="margin-left:0px">除此之外，Chrome 96 稳定版还包含了一些安全更新，目前官方尚未推出更新公告，新特性发布在谷歌功能更新列表：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeatures%2F5656451751084032" target="_blank">https://chromestatus.com/features/5656451751084032</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            