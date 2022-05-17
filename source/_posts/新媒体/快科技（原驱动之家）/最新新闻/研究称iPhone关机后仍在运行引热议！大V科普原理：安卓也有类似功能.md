
---
title: '研究称iPhone关机后仍在运行引热议！大V科普原理：安卓也有类似功能'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220517/s_cb6c9880c123458f8e81ae41848f535e.jpg'
author: 快科技（原驱动之家）
comments: false
date: Tue, 17 May 2022 21:52:36 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220517/s_cb6c9880c123458f8e81ae41848f535e.jpg'
---

<div>   
<p>5月17日，一则关于#研究称iPhone关机后仍在运行#的话题登上了各大平台热搜，被网友还广泛讨论。</p>
<p><strong>据介绍，iPhone上的查找手机等功能会让手机在关机时，仍然以低功耗模式（LPM）运行，以便帮助用户寻找丢失的手机。</strong></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220517/cb6c9880c123458f8e81ae41848f535e.jpg" target="_blank"><img alt="研究称iPhone关机后仍在运行引热议！大V科普原理：安卓也有类似功能" h="399" src="https://img1.mydrivers.com/img/20220517/s_cb6c9880c123458f8e81ae41848f535e.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p><span style="color:#ff0000;"><strong>而最近有研究人员基于这一机制设计出一种恶意软件，在用户关闭iPhone时也能运行，甚至可以通过这种功能侵入关机的iPhone，</strong></span>或在手机关闭时运行恶意功能。</p>
<p>对此，博主@<a class="f14_link" href="https://weibo.com/6198648442/LtsUR3zC0?from=page_1005056198648442_profile&wvr=6&mod=weibotime" target="_blank">好大的奕</a> 发文浅谈解析了实现原理。</p>
<p>首先，这个功能原本的使用场景是：多台iPhone设备使用同一个ID时，当其中一台处于关机状态下，只要是打开“Find My”功能，那么手持的设备可以让其发出定位或者声响。</p>
<p>而这个功能实现便是通过Always-on Processor处理器。</p>
<p>实现的框架便是在手机自动进入low-power-mode时（关机状态），由另一端的手持设备通过ID给指令至需要寻找的设备当中内置的app，而后app再下达指令给交互软件，而后再到传递给用户访问硬件环境与软件。</p>
<p>而这个指令会发送到一个单独的硬件上，这个硬件则是Always-on Processor。<strong>它在iPhone中可以控制相当一部分IC的电源，也就是说只要IC能够有电源就能运行，这是这一功能实现的原因。</strong></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220517/11434d69f269409a9a183ce10e3412b2.png" target="_blank"><img alt="研究称iPhone关机后仍在运行引热议！大V科普原理：安卓也有类似功能" h="865" src="https://img1.mydrivers.com/img/20220517/s_11434d69f269409a9a183ce10e3412b2.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p><span style="color:#ff0000;"><strong>目前三星等多种安卓品牌也能实现类似关机查找手机的功能，同样不排除会被侵入的可能。</strong></span></p>
<p>但相比之下用户可能更愿意它的存在，能在手机丢失之后有找回来的可能，属于一种为了能够给用户实现更多的方便，而牺牲掉一小部分的隐私和安全性功能。</p>
<p>而这种功能究竟可取不可取还是在于个人，有人支持也有人反对，只能说是仁者见仁，智者见智了。</p>
<p><strong>你觉得关机查找手机的功能应该保留吗？</strong></p>

           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
           <p class="zhuanzai"><strong>如需转载请务必注明出处：快科技</strong></p>  
          <p class="url"><span style="color:#666">责任编辑：建嘉</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/iphoneshouji.htm">iPhone手机</a><a href="https://news.mydrivers.com/tag/pingguo.htm">苹果</a><a href="https://news.mydrivers.com/tag/anzhuo.htm">安卓</a>  </p>
        
</div>
            