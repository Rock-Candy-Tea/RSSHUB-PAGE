
---
title: '微软设法让第三方更难改变Windows 11中的默认浏览器'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1112/a8d7f30a570d31a.gif'
author: cnBeta
comments: false
date: Fri, 12 Nov 2021 12:01:38 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1112/a8d7f30a570d31a.gif'
---

<div>   
<strong>微软再次转移了目标，使终端用户更难选择Edge以外的默认浏览器。处理来自Windows 11
microsoft-edge://类型的网页链接的URI方案不能再被EdgeDeflector等工具覆盖。</strong>这意味着Mozilla为其Firefox浏览器以及Brave浏览器（基于Chromium）所做的相同实现不再有效。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1112/a8d7f30a570d31a.gif" title alt="1636708981_ezgif-4-7b4963d33a25.gif" referrerpolicy="no-referrer"></p><p>EdgeDeflector的开发者Daniel Aleksandersen注意到，在GitHub上报告了一个问题之后，这个变化是随着Windows 11 build 22494的发布而出现的，该版本的Windows 11是在一周半之前发布给在开发频道注册的Windows Insiders的。Windows 11现在已经阻止了第三方截取microsoft-edge://链接，目前没有任何非破坏性的解决方法。基本上，这使得Edge不可能被用于操作系统级别的链接而改变。</p><p>Windows虽然没有阻止第三方注册协议处理程序，但拒绝在UI中显示它们，即便在系统注册表中改变默认值，它也会忽略这个设置，因此选择仅限于Edge、Edge Beta和Edge Dev。</p><p>这一点在进入应用程序>默认应用程序>按链接类型选择默认值，然后试图改变microsoft-edge链接类型时很明显，只能选择Edge。</p><p><img src="https://static.cnbetacdn.com/article/2021/1112/5dff1d8b9971900.jpg" title alt="1636711096_snag-0003.jpg" referrerpolicy="no-referrer"></p><p>Aleksandersen在一篇博文中对这一变化进行了更详细的说明：</p><blockquote><p>这将使终端用户除了手动改变每个文件类型外没有其他选择。我写这篇文章的机器运行的是Windows 10 21H2 (19044.1348)，仍然可以对microsoft-edge://协议使用EdgeDeflector，它可以强制操作系统级别的网页链接在默认浏览器中打开。</p><p>虽然仍然可以在Windows 10中换掉Edge，但人们不得不怀疑Mozilla等公司是否会挑战<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>的反竞争措施，因为微软正在Windowx系统中进行默认浏览器大战的战火升级。</p><p>之前声称突破了限制的Mozilla方面表示，人们应该有选择权，他们应该有能力简单和容易地设置默认值，他们对默认浏览器的选择应该得到尊重。因此之前Mozilla特别为Windows系统定制了代码，当使用microsoft-edge协议时，可以为那些已经选择Firefox作为其默认浏览器的用户启动Firefox，但微软在最近对Windows 11的改变之后，这个计划的实施将不再可能了。</p></blockquote><p>Aleksandersen在上个月的一篇博文中进一步指出，在Google为其移动应用引入googlechrome://方案后，供应商特定的URI方案在2014年2月开始兴起，以此来对抗<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>反竞争的坚持，即Safari应该处理iOS设备上的某些链接。</p><p>当然，在Windows 11中更难选择默认应用程序的决定完全有可能在其最终于2022年某个时候向公众发布之前发生变化，因为据称Windows Insiders对Windows开发的过程和结果有发言权。</p>   
</div>
            