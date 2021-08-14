
---
title: '黑客可以利用管理DNS服务供应商的漏洞来监视公司和组织的内部流量'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/08/13d85279c8deaf4.gif'
author: cnBeta
comments: false
date: Sat, 14 Aug 2021 08:03:16 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/08/13d85279c8deaf4.gif'
---

<div>   
<strong>据《The Hacker News》报道，一种出现在DNSaaS（DNS即服务）的一类新漏洞可被黑客用来获取企业网络的敏感信息。</strong>基础设施安全公司Wiz的Ami
Luttwak和Shir
Tamari宣布，他们发现了一个简单的漏洞，允许拦截所有通过Google和亚马逊等管理的DNS供应商的互联网流量中的一部分动态DNS流量。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/08/13d85279c8deaf4.gif" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/08/13d85279c8deaf4.gif" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">他们进一步解释说，暴露的流量为威胁者提供了他们发动成功攻击所需的所有信息。令人不安的是，这使任何人都有能力看到公司和政府组织内部正在发生的事情。在某种程度上，它相当于国家级别的间谍活动能力，而且这些数据就像注册一个域名一样容易获得。<br></p><p style="text-align: left;">研究人员说："我们能够获取到的动态DNS流量来自15000多个组织，包括财富500强企业、45个美国政府机构和85个国际政府机构，这些数据包括大量有价值的情报，如内部和外部IP地址、计算机名称、员工姓名和办公地点。"</p><p style="text-align: left;">在Google云DNS或处理DNS解析服务的亚马逊Route53上进行的域名注册，创造了一个有效消除用户间的隔离并允许访问宝贵信息的场景。因此，如果一个组织在Route53平台上使用AWS名称服务器配置了一个新的域名，在托管区，他们将新的域名与内部网络相关联后，所有公司终端的动态DNS流量都可以被具有相同名称的欺诈性服务器所访问到。</p><p style="text-align: left;">幸运的是，由于Wiz Research团队开发了一个识别DNS信息泄漏的工具，这些漏洞已经被修补。简而言之，该工具发现了可以利用的DNS漏洞，以确定未经授权的内部DDNS更新是否被泄露给了DNS供应商或恶意行为者。</p><p><a href="https://static.cnbetacdn.com/article/2021/08/a57b40c78aa74fb.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/08/a57b40c78aa74fb.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;"><strong>您可以在这里测试并了解更多细节：</strong></p><p style="text-align: left;"><a href="https://dynamic-dns-checker.tools.wiz.io/" _src="https://dynamic-dns-checker.tools.wiz.io/" target="_blank">https://dynamic-dns-checker.tools.wiz.io/</a><br></p>   
</div>
            