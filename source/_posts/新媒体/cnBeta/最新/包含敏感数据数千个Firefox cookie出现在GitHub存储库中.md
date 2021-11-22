
---
title: '包含敏感数据数千个Firefox cookie出现在GitHub存储库中'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1122/32d91c6ef758a20.png'
author: cnBeta
comments: false
date: Mon, 22 Nov 2021 03:02:56 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1122/32d91c6ef758a20.png'
---

<div>   
<strong>包含敏感数据的数千个 Firefox cookie 数据库目前出现在 GitHub 的存储库中，这些数据可能用于劫持经过身份验证的会话。</strong>这些 cookies.sqlite 数据库通常位于 Firefox 配置文件文件夹中。它们用于在浏览会话之间存储 cookie。现在可以通过使用特定查询参数搜索 GitHub 来找到它们，这就是所谓的搜索“dork”。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1122/32d91c6ef758a20.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1122/32d91c6ef758a20.png" alt="QQ截图20211122110231.png" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">总部位于伦敦的铁路旅行服务公司 Trainline 的安全工程师 Aidan Marlin 在通过 HackerOne 报告了他的发现，并被 GitHub 代表告知“我们用户暴露的凭据不在范围内后，提醒 The Register 这些文件的公开可用性。我们的漏洞赏金计划”。Marlin 然后问他是否可以公开他的发现，并被告知他可以自由这样做。</p><p style="text-align: left;">在发送给 The Register 的电子邮件中，Marlin 表示：“我很沮丧 GitHub 没有认真对待用户的安全和隐私。它至少可以防止这个 GitHub dork</p><p style="text-align: left;">的结果出现。如果上传这些 cookie 数据库的人知道他们做了什么，他们会尿裤子”。</p><p style="text-align: left;">Marlin 承认，受影响的 GitHub 用户在提交代码并将其推送到公共存储库时未能阻止他们的 cookies.sqlite 数据库被包含在内，因此应该受到一些指责。 “但是这个 dork 的点击量接近 4500 次，所以我认为 GitHub 也有注意的义务”。他说，并补充说他已经通知了英国信息专员办公室，因为个人信息处于危险之中。</p><p style="text-align: left;">Marlin 推测这种疏忽是从一个人的 Linux 主目录提交代码的结果。他解释说：“我想在大多数情况下，个人不知道他们已经上传了他们的 cookie 数据库，用户这样做的一个常见原因是跨多台机器的公共环境”。</p><p style="text-align: left;">Marlin 说，GitHub dorks 并不新鲜，但它们通常只影响单一服务，例如 AWS。这种特殊的失误令人不安，因为它可能允许攻击者访问任何面向互联网的网站，在提交 cookie 文件时，GitHub 用户已通过该网站进行身份验证。他补充说，可能也可以找到其他浏览器的傻瓜。</p>   
</div>
            