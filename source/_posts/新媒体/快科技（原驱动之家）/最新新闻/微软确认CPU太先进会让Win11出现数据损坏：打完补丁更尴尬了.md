
---
title: '微软确认CPU太先进会让Win11出现数据损坏：打完补丁更尴尬了'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220809/s_a4a23b2a490c47e0904a8bb52a24edc1.jpg'
author: 快科技（原驱动之家）
comments: false
date: Tue, 09 Aug 2022 18:01:08 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220809/s_a4a23b2a490c47e0904a8bb52a24edc1.jpg'
---

<div>   
<p>遇到这样的BUG已经很无语了，没想到修复方案更令人尴尬。</p>
<p>微软日前确认，Windows 11和Windows Server 2022存在BUG，在支持VAES指令集的环境下，可能到导致数据损坏。</p>
<p>Intel从10代酷睿（Ice Lake ）和第三代至强可扩展处理器（IceLake-SP）开始才添加了对VAES的支持，AMD这边则是Zen 3锐龙5000，它也是AVX-512的组成部分。</p>
<p>没想到，<strong>因为处理器太先进，导致密码本算法模式不同，进而可能造成数据损毁。</strong></p>
<p>不过，微软接着表示，早在5月（预览版）、6月份（正式版），它们就推送了修复补丁。</p>
<p>可更尴尬的事情在于，打补丁后会造成性能下降，尤其是在BitLocker、TLS、硬盘密集传输负载场景下时，调用AES指令集的任务可能因此慢两倍。</p>
<p>被炮轰后，微软现在建议用户再次安装6月23日和7月12日的最新补丁，这次通过修改Windows核心加密库的代码路径，减轻了性能下滑问题。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220809/a4a23b2a490c47e0904a8bb52a24edc1.jpg" target="_blank"><img alt="微软确认CPU太先进会让Win11出现数据损坏：打完补丁更尴尬了" h="337" src="https://img1.mydrivers.com/img/20220809/s_a4a23b2a490c47e0904a8bb52a24edc1.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
           <p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p>
<div style="overflow: hidden;font-size:14px;">
           <p class="zhuanzai"><strong>如需转载请务必注明出处：快科技</strong></p>  
          <p class="url"><span style="color:#666">责任编辑：万南</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/windows_11.htm">Windows 11</a><a href="https://news.mydrivers.com/tag/weiruan.htm">微软</a><a href="https://news.mydrivers.com/tag/zhilingji.htm">指令集</a>  </p>
        
</div>
            