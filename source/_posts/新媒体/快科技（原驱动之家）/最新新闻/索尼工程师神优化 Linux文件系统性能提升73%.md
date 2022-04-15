
---
title: '索尼工程师神优化 Linux文件系统性能提升73%'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220415/s_c92d75b8e71145448c08da3bde5f1fa7.jpg'
author: 快科技（原驱动之家）
comments: false
date: Fri, 15 Apr 2022 19:39:31 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220415/s_c92d75b8e71145448c08da3bde5f1fa7.jpg'
---

<div>   
<p class="MsoNormal">在<span lang="EN-US">Linux</span>系统中，索尼工程师最近立大功了，他们提交的代码使得<span lang="EN-US">exFAT</span>文件系统的性能大涨<span lang="EN-US">73%</span>甚至更多，极大地缩短了文件创建时间。</p>
<p class="MsoNormal">据报道，索尼工程师<span lang="EN-US">Yuezhang Mo</span>提交的代码解决了<span lang="EN-US">eXFAT</span>文件系统的一个问题，<span style="color:#ff0000;"><strong>在“目录同步“模式下挂载时，这些代码改进了在清零集簇时的<span lang="EN-US">block</span>区块请求，在<span lang="EN-US">ARM</span>平台上的<span lang="EN-US">SD</span>卡存储测试中，文件系统性能大涨<span lang="EN-US">73%</span>，甚至更多。</strong></span></p>
<p class="MsoNormal">实测下来，创建<span lang="EN-US">256KB</span>簇大小的文件时间从<span lang="EN-US">11</span>分<span lang="EN-US">22</span>秒降低到了<span lang="EN-US">1</span>分<span lang="EN-US">39</span>秒，如果是<span lang="EN-US">64KB</span>簇，创建<span lang="EN-US">1000</span>个目录的时间从<span lang="EN-US">3</span>分<span lang="EN-US">34</span>秒缩短到了<span lang="EN-US">56</span>秒。</p>
<p class="MsoNormal">目前索尼工程师提交的代码将在本周排队等待<span lang="EN-US">Linux exFAT</span>系统驱动程序代码合并，<strong>预计会在今年夏天发布的<span lang="EN-US">Linux 5.19</span>内核中实装。</strong></p>

<p align="center"><a href="https://img1.mydrivers.com/img/20220415/c92d75b8e71145448c08da3bde5f1fa7.jpg" target="_blank"><img alt="索尼工程师神优化 Linux文件系统性能提升73%" h="371" src="https://img1.mydrivers.com/img/20220415/s_c92d75b8e71145448c08da3bde5f1fa7.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
           <p class="zhuanzai"><strong>如需转载请务必注明出处：快科技</strong></p>  
          <p class="url"><span style="color:#666">责任编辑：宪瑞</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/caozuoxitong.htm">操作系统</a><a href="https://news.mydrivers.com/tag/linux.htm">Linux</a><a href="https://news.mydrivers.com/tag/suoni.htm">索尼</a>  </p>
        
</div>
            