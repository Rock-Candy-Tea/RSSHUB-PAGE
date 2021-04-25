
---
title: '密码管理器Passwordstate被植入后门'
categories: 
 - 图片
 - 煎蛋
 - 首页
headimg: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/785ee9a64452fae8f99452d1a539c143.jpg!custom'
author: 煎蛋
comments: false
date: Sun, 25 Apr 2021 03:05:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/785ee9a64452fae8f99452d1a539c143.jpg!custom'
---

<div>   
<blockquote><p>打翻了装有全部鸡蛋的那个篮子</p></blockquote><img src="https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/785ee9a64452fae8f99452d1a539c143.jpg!custom" referrerpolicy="no-referrer"><p>密码管理器Passwordstate，有多达29000名用户下载到恶意更新。该更新从应用程序中提取数据并将其发送到攻击者控制的服务器。</p>
<p>在一封电子邮件中，Passwordstate的创建者Click Studios告诉客户，犯罪分子破坏了软件的更新机制，并利用漏洞在用户的电脑上安装恶意文件。根据安全公司CSIS Group的一份简短，恶意文件名为 "moserware.secretsplitter.dll"，包含一个名为SecretSplitter的应用程序的合法副本，以及名为 "Loader" 的恶意代码。</p>
<p>Loader代码试图检索位于https://passwordstate-18ed2.kxcdn[.]com/upgrade_service_upgrade.zip的文件档案，这样它就可以检索到加密过程第二阶段的有效载荷。一旦解密，该代码可直接在内存中执行。来自Click Studios的电子邮件说，该代码会 "提取有关计算机系统的信息，并选择Passwordstate数据，然后发布到不良行为者的CDN网络"。</p>
<p>Passwordstate更新泄露事件从4月20日上午8:33 UTC持续到4月22日上午12:30。攻击者的服务器于4月22日上午7:00(UTC)关闭。</p>
<p>安全从业人员经常推荐密码管理器，因为它们使人们很容易存储长而复杂的密码，这些密码对数百甚至数千个账户都是独一无二的。如果不使用密码管理器，许多人就会采用在多个账户中重复使用弱密码。</p>
<p>Passwordstate漏洞却揭示了密码管理器所带来的风险，因为它们代表了装有全部鸡蛋的那个篮子。如果启用双因素认证，风险就会大大降低，因为仅靠提取的密码不足以获得未经授权的访问。Click Studios表示，Passwordstate提供多种2FA选项。</p>
<p>这次漏洞特别令人担忧，因为Passwordstate的受众主要为企业客户，他们使用管理器来存储防火墙、VPN和其他企业应用程序的密码。Click Studios称，Passwordstate "受到全球29000多名客户和370000名安全和IT专业人士的信任，其安装基础从最大的企业，包括许多财富500强公司，到最小的IT商店"。</p>
<p>Passwordstate漏洞是最近几个月曝光的最新一次供应链攻击。12月，SolarWinds网络管理软件的一个恶意更新在18000名客户的网络中安装了后门。本月早些时候，名为Codecov Bash Uploader的开发者工具从受感染的机器中提取秘密认证令牌和其他敏感数据，并将它们发送到黑客控制的一个远程站点。</p>
<p>在这篇文章(原文)发布时，68个跟踪的端点保护程序中没有一个检测到该恶意软件。到目前为止，研究人员还无法获得后续有效载荷的样本。</p>
<p>任何使用Passwordstate的人都应该立即重置所有存储的密码，特别是防火墙、VPN、交换机、本地账户和服务器的密码。</p>
<p>参考 https://arstechnica.com/gadgets/2021/04/hackers-backdoor-corporate-password-manager-and-steal-customer-data/</p>  
</div>
            