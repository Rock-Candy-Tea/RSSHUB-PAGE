
---
title: 'WiFiDemon – iOS WiFi RCE 0-Day漏洞利用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f47974c894ec4273bfc82884cbfedd92~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 03:12:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f47974c894ec4273bfc82884cbfedd92~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f47974c894ec4273bfc82884cbfedd92~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>近日，ZecOps安全研究人员发现了iOS WiFi命名漏洞的零交互攻击利用方式，可以用来远程劫持iPhone设备。</p>
<h1 data-id="heading-0"><strong>Wi-Fi-Demon</strong></h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/303c523872d644c7b6bb335e1878f3a1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Wifid 是处理与WiFi连接相关的协议的系统daemon。Wifid是以root 权限运行的。大多数处理函数都在CoreWiFi 框架中定义，而且这些服务无法在沙箱中访问。</p>
<p>6月，研究人员Carl Schou发现wifid在处理SSID 时存在格式字符串问题。攻击者利用该wifid漏洞可以引发DoS攻击，禁用iPhone的WiFi功能和热点功能。引发DoS 攻击的原因是wifid 会将已知的WiFi SSID写入硬盘中的以下文件：</p>
<p>/var/preferences/com.apple.wifi.known-networks.plist</p>
<p>/var/preferences/SystemConfiguration/com.apple.wifi-networks.plist.backup</p>
<p>/var/preferences/SystemConfiguration/com.apple.wifi-private-mac-networks.plist</p>
<p>Wifid每次启动后，就会从文件中读取SSID并引发奔溃。及时重启也无法解决该问题。</p>
<h1 data-id="heading-1"><strong>WiFiDemon 技术分析：零点击远程漏洞利用</strong></h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1eb6d4a770f04cbbaf742cfb1646f4cd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>研究人员进一步分析发现：</p>
<p>攻击者无法强迫用户连接。该漏洞可以以零点击的非交互形式启动。受害者只需要将WiFi开启就会触发有漏洞的代码。</p>
<p>研究人员在测试格式字符串bug时，注意到WiFid在无法连接到WiFi时会生成日志。这些日志中包含SSID，表明其中可能受到相同的格式字符串bug影响。该日志与智能设备的一个常见行为有关：自动扫描和加入已知的网络。</p>
<p>当用户使用手机时，iPhone每3秒会扫描WiFi网络。此外，如果用户的手机屏幕关闭了，仍然会扫描WiFi网络，但是扫描频率会变低一点，扫描的时间从10秒到1分钟左右。</p>
<p>如果用户连接到已有的WiFi 网络，攻击者可以启动其他攻击来断开设备的WiFi连接，然后启动0点击攻击。</p>
<p>零点击攻击：如果恶意AP有密码保护，且用户从未加入WiFi网络，硬盘中不会保存任何内容。在关闭恶意AP后，用户的WiFi功能就会正常。用户不会注意到是否受到攻击。</p>
<p> </p>
<p>【<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fdocs.qq.com%252Fdoc%252FDVFNpaGJvRFJiQ2Ro" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.qq.com%2Fdoc%2FDVFNpaGJvRFJiQ2Ro" ref="nofollow noopener noreferrer">网络安全学习资料免费分享</a>】</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abdac60a531f4f9290fbe781a9b0f54e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            