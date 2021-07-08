
---
title: 'Android端Chrome被指搜索引擎不公平竞争：仅对谷歌搜索进行优化'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0708/5178ba2ca349692.jpg'
author: cnBeta
comments: false
date: Thu, 08 Jul 2021 03:28:25 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0708/5178ba2ca349692.jpg'
---

<div>   
在 Android 端 Chrome 浏览器中，在搜索引擎竞争中 Google Search 存在天然的优势。这不仅在于 Google Search 是 Chrome 的默认搜索引擎，<strong>而且还专门为 Google Search 进行了性能优化</strong>。<strong>程序员 Daniel Aleksandersen 近日探究了 Chromium 项目的源代码，发现这个对其他搜索引擎不公平的地方。</strong><br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0708/5178ba2ca349692.jpg" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0708/3e74ffd52eaae25.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">Chromium 项目是由Google、其他企业及个人贡献者共同开发的，但是整个项目由Google管理和控制。Aleksandersen 在探究其他东西的时候，偶然在代码中发现了 PreconnectToSearch 功能。该功能在启用之后，会会预先打开并保持与默认搜索引擎的连接。</p><p style="text-align: left;">预连接功能会解析域名，并协商和设置了与服务器的安全连接。所有这些事情都需要时间，它们必须在搜索引擎能够接收用户的搜索查询之前发生。抢占这些步骤可以在缓慢的网络连接上节省十几秒，在快速连接上节省半秒。</p><p style="text-align: left;">这种优化可以为Google的客户带来不错的性能提升。当然，前提是连接只需要微不足道的处理能力和网络带宽。如果用户不打算搜索网络，提前设置连接可能会造成浪费，或减慢其他网页的加载速度。</p><p style="text-align: left;">不过这项功能有个小问题，那就是 Chromium 会检查默认的搜索引擎设置，只有当它被设置为 Google Search 时才会启用该功能。这种优惠待遇意味着没有其他搜索引擎能在加载搜索结果的时间上与Google搜索竞争。每个竞争者都必须等到用户开始输入搜索查询后，Chrome 才会建立连接。</p><p style="text-align: left;">与没有预连接的竞争对手相比，该功能使Google搜索在提供搜索结果方面拥有 80% 的领先优势。相关代码的 Chromium 变更日志照亮了一些关于为什么该功能以这种方式工作的原因。以下评论伴随着限制该功能只在Google域名上工作的评论：“这个功能允许我们在Google上进行实验，而不可能对非Google的DSE产生问题。这将有望防止与其他搜索引擎出现问题或倒退”。</p><p style="text-align: left;">Google担心，其他搜索引擎可能无法应对这一功能所导致的连接数量增加。这是一个合理的担忧。连接数的意外增加可能会使没有准备的接收者不知所措。这个潜在的问题并不能改变Google给自己带来不公平竞争优势的事实。</p><p style="text-align: left;">如果他们想，Chromium可以用更好的方式解决这个问题。其他搜索引擎可以通过对其OpenSearch Descriptions（OSD）的扩展来选择加入或退出。OSD是搜索引擎提供给网络浏览器的一个配置文件，告诉它们如何将它们设置为浏览器中的搜索提供者。Chrome 也可以使用 Well-Known URI（RFC 5785）来查询搜索引擎是否要选择加入或退出预连接。</p>   
</div>
            