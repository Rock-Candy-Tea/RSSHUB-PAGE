
---
title: 'Firefox 87正式发布：引入Smart Block以改善隐私浏览体验'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0324/30ee9893edce198.jpg'
author: cnBeta
comments: false
date: Wed, 24 Mar 2021 05:12:02 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0324/30ee9893edce198.jpg'
---

<div>   
Mozilla 刚刚发布了 Firefox 87.0 的正式版本，<strong>继续去年 12 月的 Firefox 85、以及今年 2 月份的 Firefox 86 之后，本月的 Firefox 87 主要引入了“智能拦截”（Smart Block）功能以改善隐私浏览体验。</strong>早些时候，我们已经介绍过 Firefox 87 即将默认修剪 HTTP Referrers 引荐来源标头中的路径和查询字符串等信息，以防止站点意外泄露了用户的敏感数据。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0324/30ee9893edce198.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0324/30ee9893edce198.jpg" alt="0-0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（动图对比：请戳<a href="https://cdn.arstechnica.net/wp-content/uploads/2021/03/firefox-smart-block.gif" target="_self">这里</a>）</p><p>作为 Mozilla 推出的开源浏览器的最新稳定版本，Firefox 87.0 还改进了引荐引荐来源（HTTP Referrers）网址政策，还可修剪 URL 中嵌入的脚本。</p><p>此前，Firefox 已默认阻止第三方追踪脚本有很长一段时间。在大都数情况下，这种体验都是相当无缝的。</p><p>不过在某些情况下，缺失的追踪脚本仍会对网页呈现造成一定的干扰，比如像下图一样，造成页面页面的永久破坏。</p><p><img src="https://static.cnbetacdn.com/article/2021/0324/01d55843de78e08.gif" alt="0-3.gif" referrerpolicy="no-referrer"></p><p>为此，智能拦截（Smart Block）采取了额外的步骤，来改善嵌入第三方跟踪器的页面上呈现。</p><p>它不会简单粗暴地去除追踪脚本，并在原位置留下一个空洞，而是将之替换成 Mozilla 所谓的“替代式”（stand-in）脚本。</p><p>替代脚本的功能与原追踪器类似，以尽可能复现原页面的呈现顺序和结果，而不会将实际数据泄露给第三方。</p><p><a href="https://static.cnbetacdn.com/article/2021/0323/48df1cee2bccef0.jpeg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0323/48df1cee2bccef0.jpeg" referrerpolicy="no-referrer"></a></p><p>最后，当你将其它网站的图像嵌入到自己的网站中时，有关该网站的查看着信息也会被泄露给其它网站的运营者。</p><p>举个例子，我们设置一个名叫 greatsearch.tld 的虚拟搜索引擎，然后借助 sheep-pictures.tld 运算符，以在每个页面结果页面上都嵌入一张绵羊图像。</p><blockquote><p>HTML 代码如下：</p><p><img src=https://sheep-pictures.tld/sheep1.jpg></p></blockquote><p>当用户使用该站点时，浏览器就会看到该标记，并在呈现页面上自动下载 https://sheep-pictures.tld/sheep1.jpg 这张图片。</p><p>传统做法会将引荐页的整个 URL 都包含在该 Web 请求中，意味着信息会通过 sheep-pictures.tld 泄露给网站运营者，且他们会在日志中看到如下内容：</p><blockquote><p>240.163.255.110 - - [15/Mar/2021:10:28:57 -0400] "GET /sheep1.jpg</p><p>HTTP/1.1" 200 11676 "http://greatsearch.tld/res</p><p>ults?really-embarrassing-medical-condition"</p></blockquote><p>但若你已将浏览器升级到 Firefox 87.0，则 sheep-pictures.tld 只会留下如下所示的操作日志：</p><blockquote><p>240.163.255.110 - - [15/Mar/2021:10:28:57 -0400] "GET /sheep1.jpg</p><p>HTTP/1.1" 200 11676 "http://greatsearch.tld/"</p></blockquote><p>最后，Firefox 87.0 还包含了其它修复和功能改进。</p><blockquote><p>● 网页查找时可启用高亮全选（Highlight All）；</p><p>● 全面支持 macOS 内置屏幕阅读器的旁白（VoiceOver）功能；</p><p>● 一些安全修复和常规调整（详见 Mozilla 的 Firefox 87.0 <a href="https://www.mozilla.org/en-US/firefox/87.0/releasenotes/" target="_self">发行说明</a>）。</p></blockquote><p>下载地址：</p><blockquote><p><a href="https://ftp.mozilla.org/pub/firefox/releases/87.0/" _src="https://ftp.mozilla.org/pub/firefox/releases/87.0/" target="_blank">https://ftp.mozilla.org/pub/firefox/releases/87.0/</a></p></blockquote><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1105343.htm" target="_blank">Firefox 87将默认修剪HTTP Referrers以保护用户隐私</a></p></div>   
</div>
            