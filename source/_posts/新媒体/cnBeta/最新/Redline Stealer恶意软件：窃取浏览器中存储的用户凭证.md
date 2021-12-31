
---
title: 'Redline Stealer恶意软件：窃取浏览器中存储的用户凭证'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1231/fa4798e66863be8.webp'
author: cnBeta
comments: false
date: Fri, 31 Dec 2021 02:34:01 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1231/fa4798e66863be8.webp'
---

<div>   
<strong>在调查某公司最近发生的内部数据泄露事件时，<a href="https://asec.ahnlab.com/en/29885/" target="_blank">AhnLab ASEC</a> 分析小组确认用于访问公司网络的 VPN 账户是从某位在家工作的员工的电脑上泄露的。</strong>发生损失的公司为在家工作的员工提供 VPN 服务，让他们访问公司的内部网络，员工用提供的笔记本电脑或他们的 PC 通过 VPN 连接到公司内部网络。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1231/fa4798e66863be8.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">目标员工利用网络浏览器提供的密码管理功能，在网络浏览器上保存并使用 VPN 网站的账号和密码。在这样做的时候，个人电脑被感染了针对账户凭证的恶意软件，泄露了各个网站的账户和密码，其中也包括公司的 VPN 账户。三个月后，被泄露的 VPN 账户被用来入侵该公司的内部网络。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1231/946910fe564377c.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">为了方便用户，网络浏览器会储存用户访问网站时输入的账户和密码，并提供再次访问时自动输入的功能。在基于 Chromium 的网络浏览器（Edge、Chrome）上，密码管理功能是默认启用的。登录时输入的信息会通过密码管理功能保存到登录数据文件中。</p><p style="text-align: left;"><strong>网络浏览器文件路径</strong></p><p style="text-align: left;"><strong>Chrome</strong> C:\Users\<User name>\AppData\Local\Google\Chrome\User Data\Default\Login Data</p><p style="text-align: left;"><strong>Edge</strong> C:\Users\<User name>\AppData\Local\MicrosoftEdge\User\Default\Login Data</p><p style="text-align: left;"><strong>Opera</strong> C:\Users\<User name>\AppData\Roaming\Opera Software\Opera Stable\Login Data</p><p style="text-align: left;"><strong>Whale</strong> C:\Users\<User name>\AppData\Local\Naver\Naver Whale\User Data\Default\Login Data</p><p style="text-align: left;">登录数据是一个SQLite数据库文件，账户和密码信息被保存在logins表中。除了账户和密码之外，保存的时间、登录网站的URL以及访问次数也被保存在logins表中。如果用户拒绝保存某个网站的账号和密码信息，为了记住这一点，blacklisted_by_user 字段将被设置为1，用户名_value和密码_value字段将没有账号和密码，只有 origin_url 信息被保存到 logins 表中。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1231/1245bc1a9dcbf4e.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">发现目标员工的电脑是全家人在家里使用的，没有得到安全管理。它很早以前就已经感染了各种恶意软件，虽然安装了另一家公司的反恶意软件程序，但它未能正确检测和修复。</p><p style="text-align: left;">在被感染的恶意软件中，有一个叫 Redline Stealer 的恶意软件。Redline Stealer 是一种收集保存在网络浏览器中的账户凭证的信息窃取者，它于 2020 年 3 月首次出现在俄罗斯暗网上。一个名为 REDGlade 的用户上传了一个宣传帖子，解释了 Redline Stealer 包含的各种功能，并以 150-200 美元的价格出售该黑客工具。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1231/af4eb9d4989511f.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">由于 Redline Stealer 在暗网上被不加区分地卖给了不特定的人，因此很难将恶意软件的开发者与攻击者直接联系起来。除了恶意软件，使用Redline Stealer 泄露的凭证也在暗网中被出售。</p><p style="text-align: left;">在这个案例中，Redline Stealer 被伪装成 Soundshifter 的破解程序在网上传播，Soundshifter 是 Waves 公司的一个音调转换程序。用户输入带有破解、免费等字样的软件名称来搜索文件，下载并运行下载的文件，从而导致了恶意文件的感染。</p>   
</div>
            