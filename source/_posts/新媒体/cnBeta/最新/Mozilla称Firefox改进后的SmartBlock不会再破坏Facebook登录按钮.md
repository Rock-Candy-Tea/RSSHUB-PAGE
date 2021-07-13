
---
title: 'Mozilla称Firefox改进后的SmartBlock不会再破坏Facebook登录按钮'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/07/3ab05d26c286188.gif'
author: cnBeta
comments: false
date: Tue, 13 Jul 2021 13:11:00 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/07/3ab05d26c286188.gif'
---

<div>   
<strong>Mozilla Firefox
90引入了SmartBlock的下一个版本，该浏览器的跟踪器阻止机制内置于其私人浏览和严格模式中，现在它有了改进，旨在防止使用Facebook账户登录网站的按钮被破坏，Mozilla在星期二宣布了这一消息。</strong>SmartBlock于3月随Firefox
87首次推出，主要用于智能修复那些被追踪保护措施破坏的网页，而同时不损害用户的隐私。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/07/3ab05d26c286188.gif" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/07/3ab05d26c286188.gif" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">SmartBlock通过为被阻止的第三方跟踪脚本提供本地替身来做到这一点，这些替身脚本的行为与原始脚本一样，足以确保网站正常运行，且允许依赖原始脚本的破损网站在其功能完好的情况下加载。</p><p style="text-align: left;">但有时，该功能会破坏Facebook的登录按钮。在一篇新的博文中，Mozilla的汤姆·维斯涅夫斯基和亚瑟-爱德斯坦用一个试图登录Etsy的例子解释了为什么会发生这种情况。</p><p><a href="https://static.cnbetacdn.com/article/2021/07/0955f66018f60af.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/07/0955f66018f60af.png" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">在Firefox 90之前，如果使用私人浏览窗口，当点击'继续使用Facebook'按钮登录时，'登录'将无法进行，因为所需的第三方Facebook脚本已经被Firefox屏蔽。</p><p><a href="https://static.cnbetacdn.com/article/2021/07/810b1e346e41263.gif" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/07/810b1e346e41263.gif" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">不过，有了Firefox 90和SmartBlock 2.0，Facebook的登录按钮可以重新使用，而SmartBlock 2.0仍然可以阻止跨网站追踪。这是因为最初Facebook的脚本都被阻止了，但在新版当中，当点击'继续使用Facebook'按钮进行登录时，SmartBlock会做出反应，迅速解除对Facebook登录脚本的封锁，使登录顺利进行。"</p><p style="text-align: left;">Mozilla Firefox 90现在已经在Mozilla的FTP提供下载。<br style="text-align: left;"></p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1152099.htm" target="_blank">Mozilla Firefox 90发布：引入后台升级特性 终止FTP支持并加强了安全性</a></p><p><a href="https://www.cnbeta.com/articles/tech/1152389.htm" target="_blank">抵御跨站攻击：Mozilla为Firefox 90引入元数据请求标头功能</a></p></div>   
</div>
            