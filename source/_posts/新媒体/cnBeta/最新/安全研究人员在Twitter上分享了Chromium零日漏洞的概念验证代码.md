
---
title: '安全研究人员在Twitter上分享了Chromium零日漏洞的概念验证代码'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0415/78d2a0e02cc8aec.png'
author: cnBeta
comments: false
date: Thu, 15 Apr 2021 07:53:29 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0415/78d2a0e02cc8aec.png'
---

<div>   
<strong>印度安全研究人员 Rajvardhan Agarwal，刚刚在 Twitter 上分享了影响基于 Chromium 内核的诸多浏览器的零日漏洞。</strong>可知 Google Chrome、Microsoft Edge、Opera 和 Brave 等均受到影响，且 @r4j0x00 附上了 GitHub 的概念验证代码传送门。<br>
<p><img src="https://static.cnbetacdn.com/article/2021/0415/78d2a0e02cc8aec.png" referrerpolicy="no-referrer"></p><p>Rajvardhan Agarwal 在接受 <a href="https://therecord.media/security-researcher-drops-chrome-and-edge-zero-day-on-twitter/" target="_self">The Record</a> 采访时称，该漏洞源于一个 Chromium 中的 Bug，且有在上周举办的 Pwn2Own 黑客大赛中被使用。</p><p>当时 Dataflow Security 安全研究人员 Bruno Keith（@bkth_）和 Niklas Baumstark（@_niklasb）成功地利用了该漏洞，在 Chrome 和 Edge 上运行了恶意代码，并获得了 10 万美元的奖金。</p><p><img src="https://static.cnbetacdn.com/article/2021/0415/25792d2fb83adcc.png" referrerpolicy="no-referrer"></p><p>根据比赛规则，有关此漏洞的详情已经被提交给 Chrome 安全团队，因而有望尽快得到修补。虽然没有公开披露漏洞详情，但 Agarwal 宣称他在 V8 JavaScript 引擎的源代码中看到了端倪。</p><p>然后通过重现 Pwn2Own 比赛上的漏洞利用，Agarwal 在早些时候将概念验证代码上传到了 <a href="https://github.com/r4j0x00/exploits/tree/master/chrome-0day" target="_self">GitHub</a>，并在 Twitter 上进行了分享。</p><p>需要指出的是，尽管 Chromium 开发人员在上周修复了该 bug，但相关补丁尚未集成到采用 Chromium 内核的下游浏览器的正式版本中，意味着 Chrome 和 Edge 用户仍然很容易受到攻击。</p>   
</div>
            