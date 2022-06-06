
---
title: '亚马逊电子书退出国内市场 程序员开发Kindle助手：一键下载保存'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220606/672584cd-6723-4afb-b8e3-6445e6ff7ce5.png'
author: 快科技（原驱动之家）
comments: false
date: Mon, 06 Jun 2022 15:02:16 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220606/672584cd-6723-4afb-b8e3-6445e6ff7ce5.png'
---

<div>   
<p class="MsoNormal"><a class="f14_link" href="https://news.mydrivers.com/1/836/836656.htm" target="_blank">上周亚马逊中国突然宣布关停中国电子书业务</a>，明年<span lang="EN-US">6</span>月<span lang="EN-US">30</span>日就不能购买电子书了，而且<span lang="EN-US">Kindle</span>阅读器也开始提供非质量问题退货服务。</p>
<p class="MsoNormal">亚马逊这一波操作让很多喜欢用<span lang="EN-US">Kindle</span>阅读的网友措手不及，阅读器本身的影响不大，关键是已经购买的那些电子书，部分网友可能积攒了几百本甚至几千本亚马逊电子书，明年<span lang="EN-US">6</span>月份之后这会是个麻烦。</p>
<p class="MsoNormal">如何能够快速下载自己的电子书？<span style="color:#ff0000;"><strong>程序员<span lang="EN-US">yihong0618</span>开发了一个<a class="f14_link" href="https://github.com/yihong0618/Kindle_download_helper" target="_blank"><span lang="EN-US">Kindle_download_helper</span>的脚本</a>，目前已经开源，它可以让用户下载自己的亚马逊电子书。</strong></span></p>
<p class="MsoNormal">根据他的说法，这个脚本可以支持亚马逊中国及亚马逊全球，具体使用方法如下：</p>
<p class="MsoNormal"><strong>使用<span lang="EN-US"> amazon CN</span></strong></p>
<p class="MsoNormal">登陆<span lang="EN-US"> amazon.cn</span></p>
<p class="MsoNormal">访问<span lang="EN-US"> https://www.amazon.cn/hz/mycd/myx'>https://www.amazon.cn/hz/mycd/myx'>https://www.amazon.cn/hz/mycd/myx#/home/content/booksAll/dateDsc/</span></p>
<p class="MsoNormal">找到<span lang="EN-US"> cookie XHR </span>或者其他的方式</p>
<p class="MsoNormal">右键查看源码，搜索<span lang="EN-US"> csrfToken </span>复制后面的<span lang="EN-US"> value</span></p>
<p class="MsoNormal">执行<span lang="EN-US"> python3 kindle.py $&#123;cookie&#125; $&#123;csrfToken&#125; --is-cn</span></p>
<p class="MsoNormal"><strong><span lang="EN-US">how to amazon.com</span></strong></p>
<p class="MsoNormal"><span lang="EN-US">login amazon.com</span></p>
<p class="MsoNormal"><span lang="EN-US">visit https://www.amazon.cn/hz/mycd/myx#/home/content/booksAll/dateDsc/</span></p>
<p class="MsoNormal"><span lang="EN-US">find cookie F12 XHR or other ways</span></p>
<p class="MsoNormal"><span lang="EN-US">right click this page source then find csrfToken value copy</span></p>
<p class="MsoNormal"><span lang="EN-US">run: python3 kindle.py $&#123;cookie&#125; $&#123;csrfToken&#125;</span></p>
<p class="MsoNormal">不过这个脚本需要<span lang="EN-US">python3</span>，需要有一定的动手能力，不会用的也别着急，后面估计还会有程序员大神提供图形界面的<span lang="EN-US">Kindle</span>下载助手。</p>

<p class="MsoNormal" style="text-align: center;"><img alt="亚马逊电子书退出国内市场 程序员开发Kindle助手：一键下载保存" h="394" src="https://img1.mydrivers.com/img/20220606/672584cd-6723-4afb-b8e3-6445e6ff7ce5.png" style="text-align: center; border: 1px solid black;" w="600" referrerpolicy="no-referrer"></p>

           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
           <p class="zhuanzai"><strong>如需转载请务必注明出处：快科技</strong></p>  
          <p class="url"><span style="color:#666">责任编辑：宪瑞</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/yamaxun.htm">亚马逊</a><a href="https://news.mydrivers.com/tag/dianzishu.htm">电子书</a><a href="https://news.mydrivers.com/tag/chengxuyuan.htm">程序员</a>  </p>
        
</div>
            