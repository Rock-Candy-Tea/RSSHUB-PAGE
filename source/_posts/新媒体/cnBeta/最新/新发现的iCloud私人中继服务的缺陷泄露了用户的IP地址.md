
---
title: '新发现的iCloud私人中继服务的缺陷泄露了用户的IP地址'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0925/087f16461df64bb.jpg'
author: cnBeta
comments: false
date: Sat, 25 Sep 2021 03:33:54 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0925/087f16461df64bb.jpg'
---

<div>   
苹果公司新推出的iCloud私人中继系统中被发现一个缺陷，在满足某些条件时暴露了用户的IP地址，从而破坏了该功能的基础价值。正如研究人员和开发人员Sergey
Mostsevenko在本周的一篇博文中所详述的那样，私人中继在处理WebRTC方面的一个缺陷会"泄露"用户的真实IP地址，其在FingerprintJS网站提供了一个概念证明。<br>
<p>在6月的全球开发者大会上宣布的Private Relay承诺通过将互联网请求路由到由两个不同实体运营的两个单独的中继站，来防止第三方对IP地址、用户位置和其他细节的跟踪。<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>公司说，配置为通过私人中继的互联网连接使用匿名的IP地址，映射到用户所在地区，但不透露他们的确切位置或身份。</p><p><a href="https://static.cnbetacdn.com/article/2021/0925/087f16461df64bb.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0925/087f16461df64bb.jpg" title alt="1.jpg" referrerpolicy="no-referrer"></a></p><p>理论上，网站应该只看到出口代理的IP地址，但用户的真实IP在某些WebRTC通信场景中会被保留，可以通过一些巧妙的代码来发现。</p><p>正如Mostsevenko所解释的，WebRTC API是用来促进网络上的直接通信，而不需要中间服务器。在大多数浏览器中部署，WebRTC依靠互动连接建立（ICE）框架来连接两个用户。一个浏览器收集ICE候选者，并使用潜在的连接方法来寻找并与第二个浏览器建立链接。</p><p>漏洞出现在服务器反射性候选，这是一个由NAT（STUN）服务器会话穿越工具使用的候选，用于连接到位于NAT后面的设备。网络地址转换（NAT）是一个协议，使多个设备能够通过一个IP地址访问互联网。重要的是，STUN服务器共享一个用户的公共IP地址和端口号。</p><p><a href="https://static.cnbetacdn.com/article/2021/0925/3765dca5c98b561.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0925/3765dca5c98b561.jpg" title alt="2.jpg" referrerpolicy="no-referrer"></a></p><p>"由于Safari不通过iCloud私人中继代理STUN请求，STUN服务器知道你的真实IP地址。这本身并不是一个问题，因为他们没有其他信息；然而，Safari将包含真实IP地址的ICE候选者传递给JavaScript环境，"Mostsevenko说。"然后完成去匿名化后，就变成了从ICE候选者中解析你的真实IP地址的问题--这一点很容易通过网络应用程序完成。</p><p>据该研究人员称，通过与STUN服务器建立连接对象，收集ICE候选者并分析其值，就可以收集到用户的IP地址。</p><p>FingerprintJS向苹果公司报告了这个漏洞，该公司在本周发布的最新macOS Monterey测试版中推送了一个修复程序。但该漏洞在iOS 15上仍未得到修补。</p><p>了解更多：</p><p><a href="https://fingerprintjs.com/blog/ios15-icloud-private-relay-vulnerability/" _src="https://fingerprintjs.com/blog/ios15-icloud-private-relay-vulnerability/" target="_blank">https://fingerprintjs.com/blog/ios15-icloud-private-relay-vulnerability/</a><br></p>   
</div>
            