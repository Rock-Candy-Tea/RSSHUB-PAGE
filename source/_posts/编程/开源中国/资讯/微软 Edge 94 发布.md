
---
title: '微软 Edge 94 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4988'
author: 开源中国
comments: false
date: Mon, 27 Sep 2021 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4988'
---

<div>   
<div class="content">
                                                                                            <p>微软正式推出 Edge 94 稳定版本，这是微软向所有用户发布的首个以四周为周期的更新，而不是此前的六周周期，该版本带来的变化包括：</p> 
<ul> 
 <li>微软 Edge 已经完成了向四周更新周期的转变。自此微软将为主要版本采用了新的发布周期</li> 
 <li>提供新的扩展稳定选项。微软正在向管理的企业客户提供一个新的扩展稳定选项，扩展稳定选项将每隔八周更新一次，每两周会有一次安全更新。</li> 
 <li>改进了打开 MHTML 文件的默认行为。如果启用了 IE 模式，MHTML 文件将继续以 IE 模式打开，除非 MHTML 文件是从 Edge 中保存的（使用 Edge 中的另存为选项）。如果该文件是从 Edge 保存的，它现在将在 Edge 中打开。这一变化将修复从 Edge 保存的 MHTML 文件在 IE 模式下打开时出现的渲染问题。</li> 
 <li>将私人网络请求限制在安全范围内。从互联网上的页面访问本地（内网）网络上的资源，需要这些页面通过 HTTPS 交付。这一变化发生在 Chromium 项目中，而 Edge 基于该项目。有两种兼容性策略可用（InsecurePrivateNetworkRequestAllowed 和 InsecurePrivateNetworkRequestAllowedForUrls），以支持需要保留与非安全页面的兼容性的情况。</li> 
 <li>阻止混合内容的下载。安全页面将只下载托管在其他安全页面上的文件，如果从安全页面启动，托管在非安全（非 HTTPS）页面上的下载将被阻止。</li> 
 <li>为本地账户启用隐式登录。通过启用 OnlyOnPremisesImplicitSigninEnabled 策略，只有本地账户将被启用隐式登录。Microsoft Edge 不会尝试隐式登录到 MSA 或 AAD 账户。</li> 
 <li>新的可访问性设置页面。微软把与可访问性有关的设置集中在一个页面上。你可以在主设置列表下找到新的 edge://settings/accessibility 页面。在未来的 Microsoft Edge 版本中，将继续在这里添加新的设置。</li> 
</ul> 
<h3>新策略</h3> 
<ul> 
 <li>ApplicationGuardPassiveModeEnabled 忽略 Application Guard 站点列表配置，正常浏览 Edge</li> 
 <li>OnlyOnPremisesImplicitSigninEnabled 只有本地账户启用隐式登录功能</li> 
 <li>WebRtcRespectOsRoutingTableEnabled 在通过 WebRTC 进行点对点连接时启用对 Windows 操作系统路由表规则的支持。</li> 
</ul> 
<h3>废弃的策略</h3> 
<ul> 
 <li>UserAgentClientHintsEnabled 启用用户代理客户端提示功能</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fdeployedge%2Fmicrosoft-edge-relnote-stable-channel" target="_blank">https://docs.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel</a></p> 
<p> </p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            