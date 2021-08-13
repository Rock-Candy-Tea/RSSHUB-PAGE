
---
title: 'Mozilla Firefox 92开始通过阻止不安全连接的下载项来增强安全性'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0813/940883100407380.jpg'
author: cnBeta
comments: false
date: Fri, 13 Aug 2021 00:04:28 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0813/940883100407380.jpg'
---

<div>   
<strong>最近发布的Firefox 91在私人浏览模式中启用了HTTPS-only模式。随着下一个Firefox
92版本的推出，Firefox可能会通过阻止混合不安全的下载来进一步提高安全性。</strong>此前因为提供了对Google安全浏览的支持，Firefox浏览器已经阻止了危险的、潜在的不需要的和不常见的下载。<br>
 <p>现在，Mozilla正在进一步扩大Firefox浏览器的下载保护，通过直接在下载面板上显示错误，检测并拒绝通过HTTPS网站的不安全连接下载文件，"文件没有下载。潜在的安全风险"，该错误写道。</p><p><img src="https://static.cnbetacdn.com/article/2021/0813/940883100407380.jpg" title alt="File-not-downloaded-potential-security-risk.jpg" referrerpolicy="no-referrer"></p><p>当用户点击它时，Firefox浏览器对错误细节的解释如下：</p><p><img src="https://static.cnbetacdn.com/article/2021/0813/543e68d7c8368cf.jpg" title alt="Firefox-says-the-file-uses-insecure-connection.jpg" referrerpolicy="no-referrer"></p><p>"该文件使用不安全的连接。它可能在下载过程中被损坏或篡改。你可以搜索其他的下载源，或稍后再试"</p><p>用户可以通过点击"允许下载"来获得该文件，风险自负，Firefox浏览器下载面板还提供了从设备上删除的选项，以保证您的安全。</p><p>现在大多数网站都使用HTTPS而不是HTTP，但HTTPS页面仍然可能提供HTTP的内容，这被称为混合内容。包括Firefox在内的大多数浏览器在检测到混合内容时都会发出警告。直到有一天，Mozilla把混合内容的下载阻止只限于Nightly，最近，Firefox 92 Beta中启用了该功能，它可能会随着最终版本的发布而被常态化。</p><p>Firefox浏览器开发人员声称，根据他们的遥测数据，该安全功能阻止了大约1.5%的下载。</p><p><strong>在Firefox 92测试版本中现在可以选择启用或禁用不安全的下载保护功能：</strong></p><p>访问about:config</p><p>点击"接受风险并继续"</p><p>在搜索框中输入"<strong>insecure</strong>"。</p><p>在列表中，找到并修改<strong>dom.block_download_insecure</strong>的预设值为true即可，相反的将预设值切换为false可以防止或阻止Firefox阻止不安全的下载，但为了你的安全，不建议做上述操作。</p>   
</div>
            