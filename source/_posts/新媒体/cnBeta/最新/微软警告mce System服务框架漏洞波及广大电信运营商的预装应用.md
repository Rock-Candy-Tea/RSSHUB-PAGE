
---
title: '微软警告mce System服务框架漏洞波及广大电信运营商的预装应用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0528/34ac1d4b9573be2.jpg'
author: cnBeta
comments: false
date: Sat, 28 May 2022 05:28:08 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0528/34ac1d4b9573be2.jpg'
---

<div>   
<strong>在 mce Systems 提供的 Android Apps 移动服务框架中，微软研究人员发现了一系列严重的漏洞。</strong>更糟糕的是，这批易受攻击 Android Apps，已在 Google Play 官方应用商店被下载了数百万次，让广大用户面临命令注入和权限提升攻击等重大风险。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0528/34ac1d4b9573be2.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：Microsoft <a href="https://www.microsoft.com/security/blog/2022/05/27/android-apps-with-millions-of-downloads-exposed-to-high-severity-vulnerabilities/" target="_self">Security</a>）</p><p>相关漏洞包括 CVE-2021-42598、  CVE-2021-42599、CVE-2021-42600 和 CVE-2021-42601，并且波及到了预装在电信运营商定制移动设备上的预装应用程序。</p><p>Microsoft 365 Defender 安全研究人员 Jonathan Bar Or、Sang Shin Jung、Michael
Peck、Joe Mansour 和 Apurva Kumar
表示：</p><blockquote><p>这些 Android Apps 被嵌入到了设备的系统镜像中，表明它们是原厂安装的默认应用程序。</p><p>受影响的运营商包括 AT&T、TELUS、Rogers Communications、Bell Canada、以及 Freedom Mobile 。</p></blockquote><p>尴尬的是，相关 Android Apps 都逃过了谷歌官方应用商店的自动安全检查（Google Play Protect）。</p><p>雪上加霜的是，在没有获得设备 root 访问权限的情况下，此类默认预装的应用是无法被彻底卸载或禁用的。</p><p><img src="https://static.cnbetacdn.com/article/2022/0528/19f8003b34d9143.gif" alt="4.gif" referrerpolicy="no-referrer"></p><p style="text-align: center;">（图自：<a href="https://mce.systems/" target="_self">mce System</a>）</p><p>虽然在微软今日公开披露相关安全漏洞之前，设备制造商已经修复了相关漏洞以保护其客户免受攻击。</p><p>但提供终端设备的一些电信企业 / 移动服务提供商，尚未彻底扫清使用了同一隐患服务框架的 Android 应用程序。</p><p>微软补充道：</p><blockquote><p>假如有别有用心的人在客户设备上部署了隐患 Android Apps（包名为 com.mce.mceiotraceagent），其它设备也有可能遭遇此类漏洞滥用和潜在攻击。</p><p>由于这些预装应用拥有广泛的系统权限，相关漏洞或成为攻击者访问系统配置和其它敏感信息的攻击媒介。</p><p>有鉴于此，研究人员建议发现其设备上被安装了相关 Android Apps 的用户即使清理，并及时打上最新的系统安全补丁。</p></blockquote><p>最后，当 BleepingComputer 于周五早些时候联系时，微软尚未披露受影响的 Android Apps 与移动运营商的完整列表。</p>   
</div>
            