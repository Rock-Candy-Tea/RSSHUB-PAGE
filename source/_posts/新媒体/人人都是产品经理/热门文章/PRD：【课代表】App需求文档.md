
---
title: 'PRD：【课代表】App需求文档'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/SM9P92vdU50FF1Hq030p.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 13 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/SM9P92vdU50FF1Hq030p.jpg'
---

<div>   
<blockquote><p>编辑导读：如果你是一个混迹各大视频网站的人，经常会在评论区前排看见课代表，他们用简单的几句话就总结了几分钟的视频内容。本文作者作者就结合当下互联网移动端发展趋势及各个平台上显现的“课代表”现象，提出了自己的软件设计方案，并写出了需求文档，与你分享。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4863222 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/SM9P92vdU50FF1Hq030p.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、前言</h2>
<p>本文是【课代表】产品的最终章，写需求文档的目的一是想锻炼一下自己写文档的能力，二是想将自己的小想法真正冷启动起来，尽管不一定成功，但有这篇文章在，总能证明一点为了“什么”的坚持。</p>
<h3>1.1 产品概述</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/dcntEMzi0GWnTr4ccXZ2.png" alt width="1677" height="809" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">课代表产品概述</p>
<h3>1.2 修订记录</h3>
<p style="text-align: center;"><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/B5wXlXqAyiwZy5LRkVnD.png" alt width="840" height="290" referrerpolicy="no-referrer">修订记录</p>
<h2 id="toc-2">二、项目概述</h2>
<h3>2.1 背景介绍+竞品分析</h3>
<p>（本章内容可查看账号其他文章：1.<a href="http://www.woshipm.com/pd/4478158.html" target="_blank" rel="noopener">总结类内容平台「课代表」：产品立项计划书</a></p>
<p>2.<a href="http://www.woshipm.com/user-research/4493139.html" target="_blank" rel="noopener">抖音用户分析向：论用户对总结类内容的偏好）</a></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/qQRyKZhl7oCjHq5cDmt3.jpg" alt width="1005" height="672" referrerpolicy="no-referrer">选中国互联网行业经历二十几年的发展，如今已步入相对成熟稳定的阶段，在此期间不断涌入出现新的选手，如抖音、今日头条、美团等，这意味着中国互联网发展依然充满巨大的潜力。然而，中国互联网已经形成规模，互联网应用走向多元化。</p>
<p>互联网越来越深刻的改变人们的学习、工作以及生活方式，甚至影响整个社会进程。过去的二十几年，推动互联网发展的重要力量就是用户需求，如搜索引擎、即时通讯、门户网站、电子商务等核心模式，都是为解决用户的需求而生的。</p>
<h3>2.2 阅读对象</h3>
<p>阅读权限：“KK课代表”产品线相关部门人员<br>
1） 产品部门-需求评审团队<br>
2） 技术部门-产品开发团队<br>
3） 测试部门-产品测试团队<br>
4） 设计团队-产品设计团队（根据版本权限开放：常规迭代及普通功能开发，核心特色复杂逻辑模块受控关闭）</p>
<h3>2.3 术语与缩写解释</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/TW8QO3dlJWfIj7EhLYfT.png" alt width="898" height="1097" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">术语与缩写解释</p>
<h2 id="toc-3">三、用户与需求</h2>
<h3>3.1 用户划分</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/t1LC3e6YouttdqSOQ82V.png" alt width="849" height="407" referrerpolicy="no-referrer"></p>
<h3>3.2 需求汇总与划分</h3>
<p>说明：该模块将展示原始数据源，但功能划分仍有重复，以最终需求分级列表为基准。</p>
<p>基础需求演化功能部分展示<br>
<img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/cxED6q9UFRtxNNEisF64.png" alt width="540" height="424" referrerpolicy="no-referrer"></p>
<p>优化型需求演化功能部分展示</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Ln6tbHiQd4zlFmbaxQqN.png" alt width="850" height="804" referrerpolicy="no-referrer"></p>
<p>兴奋需求演化功能部分展示</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/QYl2tphw7ySDR87KppPr.png" alt width="857" height="499" referrerpolicy="no-referrer"></p>
<p>需求汇总与分级</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/i5bak3DD0dATZya3jmN2.png" alt width="1157" height="967" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、产品结构</h2>
<h3>4.1  产品功能结构图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/wS55g9CcDtWrVAGbCxIR.png" alt width="2358" height="2724" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、全局说明</h2>
<h3>5.1 异常情况说明</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/FyxdvDkZzCCJOrEDmWHK.png" alt width="2332" height="930" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">加载页面</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/oLiDvDfGNsZtaT6A1zz4.png" alt width="2307" height="931" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">网络异常</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/R6ZC8hg1qF8tMy5Ikod6.png" alt width="878" height="912" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">其他异常</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/cVQREo9p4ghdVaYDt6bn.png" alt width="872" height="235" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">异常情况说明表</p>
<h3>5.2 功能详细说明</h3>
<p><strong>5.2.1 登录、注册页</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/X7ugogFQcp3t88MwuKp4.png" alt width="1402" height="837" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">登录、注册逻辑页</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/u1pM0eX01mjKDrR59845.png" alt width="845" height="704" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/BuFT9kBKcZhuKkKrOrZ3.png" alt width="817" height="697" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/RnIpVq8EkjihGCs5loCR.png" alt width="809" height="580" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/pmAeIzc5k7YfzANTB2Go.png" alt width="892" height="230" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">登录注册流程图</p>
<p><strong>5.2.2 主页面</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/E13p2dgncwZp6TIYGU1A.png" alt width="1716" height="2674" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">主页面逻辑页</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/KTWQMTbyWABN7xe027Au.png" alt width="1664" height="1740" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/dnECo0YTgnd8NvhRSrXX.png" alt width="1648" height="1743" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/AYgmLJO4oswM3j8dUJNH.png" alt width="871" height="780" referrerpolicy="no-referrer"></p>
<p><strong>5.2.3 创作页面</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/tNXXqOotcST0IItUxW2W.png" alt width="2762" height="2892" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">创作页面逻辑图</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/LdJq3MPqC0G7NWJHbfZk.png" alt width="1675" height="1724" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/looufvNtjpQmO9sX5oPI.png" alt width="1669" height="1725" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/5mFcEOev1fLYqqvOuMKi.png" alt width="1668" height="1031" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/ZufwzlEm3O1Gm5obJhu6.png" alt width="785" height="1106" referrerpolicy="no-referrer"></p>
<p><strong>5.2.4 活动页面</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/dk8gzVihgzdI3WTBf7V4.png" alt width="1798" height="2734" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">活动页面逻辑图</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/rriL6vE4mr0lczwYXtIp.png" alt width="1733" height="1026" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/lJ9CF4FmDdmqbp3kKTXh.png" alt width="1740" height="1038" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/JQ4qeIDBefNUGzT01cGT.png" alt width="871" height="1003" referrerpolicy="no-referrer"></p>
<p><strong>5.2.5 圈子页面</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/6jqC4rpKmnEJRi70wzKH.png" alt width="1315" height="1783" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">圈子页面逻辑图</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/8otGJQicx5sJi4yaaDYy.png" alt width="1683" height="1723" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/qFov8vqRizbKNWmCDgn8.png" alt width="871" height="1039" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、后记</h2>
<p>1.【课代表】App到这篇文章全部结束，从最开始的立项到这篇PRD文档经历了3个月的时间，期间包含了立项、竞品分析、用户调研、需求分级、产品设计和PRD文档全过程，也是自己第一次将自己的想法实现了从0到1冷启动的想法，也是对自己学习的另一种复盘方法。</p>
<p>2.这篇PRD文档因为篇幅和写作时间还有很多细节内容没有展示，有机会还会对其中的多个内容进行完善。</p>
<p>3.本文参考了很多人人网站上的文章，也照搬了知识星球Potti老师的PRD写作文档-登录注册部分，（因为感觉这部分写的很细致，所以照搬过来学习一下，向Potti老师表示感谢）。</p>
<p> </p>
<p>本文由@芭芭蘑菇 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4469730" data-author="1257275" data-avatar="http://image.woshipm.com/wp-files/2021/04/4yRYEr4FHemg8MdY5BMB.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">3人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602183025_4744.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602182900_2189.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602175327_5519.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            