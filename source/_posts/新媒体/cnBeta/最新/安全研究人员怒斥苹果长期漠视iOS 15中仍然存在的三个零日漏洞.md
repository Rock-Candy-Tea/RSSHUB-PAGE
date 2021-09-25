
---
title: '安全研究人员怒斥苹果长期漠视iOS 15中仍然存在的三个零日漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0925/5ce096d03a7806b.png'
author: cnBeta
comments: false
date: Sat, 25 Sep 2021 02:38:06 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0925/5ce096d03a7806b.png'
---

<div>   
2019 年，苹果向公众开放了安全赏金计划，以鼓励研究人员向官方提交影响 iOS、iPadOS、macOS、tvOS 或 watchOS 的安全漏洞。通过高达百万美元的奖金，苹果希望此举能够确保自家软件平台的安全性。<strong>即便如此，还是有不少安全研究人员吐槽官方执行不力，比如近日 illusionofchaos 分享的一段“让人感到沮丧”的经历。</strong><br>
<p><img src="https://static.cnbetacdn.com/article/2021/0925/5ce096d03a7806b.png" alt="lockup-hero-large.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（图自：<a href="https://developer.apple.com/security-bounty/" target="_self">Apple Security Bounty</a>）</p><p>Kosta Eleftheriou 在一篇<a href="https://habr.com/en/post/579714/" target="_self">博客文章</a>中指出：这位不愿透露姓名的安全研究人员称，他们在今年 3~5 月期间向<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>上报了四个零日漏洞。</p><p>但除了已在 iOS 14.7 中修复的一个漏洞，其余三个仍存在于最新的 iOS 15.0 中。官方的这一敷衍态度，着实让他们感到信任丧失。</p><p><img src="https://static.cnbetacdn.com/article/2021/0925/6a42e0cfb69ef04.png" alt="1.png" referrerpolicy="no-referrer"></p><p>更让人无语的是，苹果并未在安全内容页面上列出，而是选择了掩盖其在 iOS 14.7 中修复的那个漏洞。</p><p>在与该公司对质时，对方曾表达歉意，同时保证会处理这方面的问题，并承诺在下一版更新时列出。</p><p>然而自那以后，该公司已经连续推送了三个更新，但每一次都食言了。</p><p><img src="https://static.cnbetacdn.com/article/2021/0925/920acbe0c7fc701.png" alt="2.png" referrerpolicy="no-referrer"></p><p>上周，忍无可忍的安全研究人员向苹果发出了警告 —— 如果再不给出正面回应，他们将公开披露相关安全漏洞 —— 结果引发了许多人的共鸣。</p><p>据悉，illusionofchaos 曝光的其中一个零日漏洞与游戏中心有关，可知其允许从 App Store 安装的任意应用访问某些用户数据：</p><blockquote><p>（1）Apple ID 电子邮件和与之关联的全名；</p><p>（2）允许代表用户访问 *.apple.com 上至少一个端点的 Apple ID 身份验证令牌；</p><p>（3）对 Core Duet 数据库的完整文件系统读取访问权限，涵盖邮件、短信、iMessage 消息、第三方 IM 的联系人列表、所有交互的元数据（包括时间戳和统计数据），以及 URL 和文本等部分附件。</p><p>（4）对快速拨号数据库和地址簿数据库的完整文件系统读取访问权限，包括联系人图片和其它元数据，比如创建和修改日期（似乎已在 iOS 15 上悄然修复）。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2021/0925/baef0f39715263d.png" alt="3.png" referrerpolicy="no-referrer"></p><p>最后，博客文章中还详细介绍了 iOS 15 中仍然存在的另外两个零日漏洞，以及 iOS 14.7 中修补的漏洞（Habr.com <a href="https://habr.com/en/post/579714/" target="_self">传送门</a>）。</p><p>遗憾的是，截止发稿时，苹果仍未就此事给予公开回应。</p>   
</div>
            