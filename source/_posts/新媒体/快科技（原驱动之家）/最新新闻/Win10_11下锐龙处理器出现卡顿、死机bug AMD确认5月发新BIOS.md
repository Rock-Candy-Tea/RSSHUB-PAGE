
---
title: 'Win10_11下锐龙处理器出现卡顿、死机bug AMD确认5月发新BIOS'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220308/f425c1c3-3ecc-44b3-b54e-abc9bb2b5e0a.png'
author: 快科技（原驱动之家）
comments: false
date: Tue, 08 Mar 2022 06:53:40 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220308/f425c1c3-3ecc-44b3-b54e-abc9bb2b5e0a.png'
---

<div>   
<p class="MsoNormal">前不久我们报道过<span lang="EN-US">AMD</span>的锐龙处理器在微软<span lang="EN-US">Win11</span>系统下会出现卡顿、死机等<span lang="EN-US">bug</span>，<span lang="EN-US">Win10</span>下也有类似的问题，现在几个月过去了<span lang="EN-US">AMD</span>官方已经调查出根源了，跟主板的<span lang="EN-US">SPI ROM</span>有关，<span lang="EN-US">5</span>月份会发新版<span lang="EN-US">BIOS</span>解决。</p>
<p class="MsoNormal">此前这个问题被认为与<span lang="EN-US">fTPM</span>有关，<span lang="EN-US">AMD</span>平台开启<span lang="EN-US">fTPM</span>就有可能出现周期性死机、卡顿、系统不稳定、声音播放出现噼啪声及屏幕鼠标乱窜等问题，禁用<span lang="EN-US">fTPM</span>之后问题就会消失。</p>
<p class="MsoNormal"><span lang="EN-US">AMD</span>调查之后确认，<span style="color:#ff0000;"><strong>问题的根源在于锐龙平台的主板上的<span lang="EN-US">SPI ROM</span>闪存，锐龙的配置可能会让它间歇性执行与<span lang="EN-US">fTPM</span>相关的扩展内存事务，这可能会导致系统交互及响应暂停。</strong></span></p>
<p class="MsoNormal"><span lang="EN-US">AMD</span>提供了一种临时解决办法，<strong>那就是将系统的<span lang="EN-US">fTPM</span>设置切换到<span lang="EN-US">dTPM</span>，</strong>后者使用的是<span lang="EN-US">NVROM</span>与<span lang="EN-US">TPM</span>交互，不过前提是用户的设备支持<span lang="EN-US">dTPM</span>功能，而且切换<span lang="EN-US">TPM</span>意味着加密要换，需要确保自己的数据备份没问题。</p>
<p class="MsoNormal">最终的解决办法需要升级<span lang="EN-US">BIOS</span>，<strong><span lang="EN-US">AMD</span>表示今年<span lang="EN-US">5</span>月上旬会推出新的补丁升级，</strong>可能会基于<span lang="EN-US">AGESA 1207</span>或者更高版本的微代码，具体的计划要等主板厂商的测试和升级结果。</p>

<p class="MsoNormal" style="text-align: center;"><img alt="Win10/11下锐龙处理器出现卡顿、死机bug AMD确认5月发新BIOS" h="397" src="https://img1.mydrivers.com/img/20220308/f425c1c3-3ecc-44b3-b54e-abc9bb2b5e0a.png" style="text-align: center; border: 1px solid black;" w="600" referrerpolicy="no-referrer"></p>

           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
           <p class="zhuanzai"><strong>如需转载请务必注明出处：快科技</strong></p>  
          <p class="url"><span style="color:#666">责任编辑：宪瑞</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/amd.htm">AMD</a><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm">Windows操作系统</a><a href="https://news.mydrivers.com/tag/cpuchuliqi.htm">CPU处理器</a>  </p>
        
</div>
            