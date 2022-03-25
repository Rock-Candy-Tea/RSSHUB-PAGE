
---
title: '精心伪造的微软客户支持和帮助文档实际上是窃取信息的Vidar恶意软件'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0325/b88edfb401dc1d7.jpg'
author: cnBeta
comments: false
date: Fri, 25 Mar 2022 09:18:44 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0325/b88edfb401dc1d7.jpg'
---

<div>   
网络安全公司Trustwave的安全团队SpiderLabs警告Windows用户，一个名为Vidar的新恶意软件活动将自己伪装成微软支持或帮助文件。因此，毫无戒心的用户可能很容易成为受害者，而Vidar是一个偷窃数据的恶意软件，可以窃取被利用者的信息。<br>
 <p>微软编译的HTML帮助（CHM）文件虽然现在已经不常见，但总是会有人希望寻求“帮助”，这个恶意的Vidar CHM恶意软件以ISO格式通过电子邮件散播，该ISO被伪装成一个"require.doc"文件。</p><p>在这个 request.doc ISO文件中包含几个恶意文件，一个被称为"pss10r.chm"的微软帮助文件（CHM）和一个被称为"app.exe"的可执行文件。一旦用户被骗提取这些文件，用户的系统就会被破坏。前者即"pss10r.chm"实际上是一个一般的合法文件，但附带的exe文件却是臭名昭著的Vidar，Vidar是偷窃者恶意软件，从浏览器等地方窃取信息和数据。该活动类似于我们在2月份了解到的RedLine恶意软件活动。</p><p><img src="https://static.cnbetacdn.com/article/2022/0325/b88edfb401dc1d7.jpg" title alt="1648195526_vidar_spam_msg_(source-_spiderlabs).jpg" referrerpolicy="no-referrer"></p><p>下面是一个合法的"pss10r.chm"与这个Vitar活动中使用的恶意文件的对比图片。</p><p><img src="https://static.cnbetacdn.com/article/2022/0325/4d8afc805fa1008.jpg" title alt="1648195521_vidar_malware_vs_real_ms_help_(source-_spider_labs).jpg" referrerpolicy="no-referrer"></p><p>恶意CHM的目的是运行另一个文件，即包含Vidar恶意软件的app.exe，以成功传递恶意软件载荷。</p><p>你可以在官方博客文章中找到更多技术细节：</p><p><a href="https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/vidar-malware-launcher-concealed-in-help-file/" _src="https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/vidar-malware-launcher-concealed-in-help-file/" target="_blank">https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/vidar-malware-launcher-concealed-in-help-file/</a><br></p>   
</div>
            