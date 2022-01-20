
---
title: 'Intel 11_12代酷睿不再支持4K蓝光：SGX漏洞成筛子了'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220120/S48ada4b2-c11d-435e-aabd-824f05c82fc9.jpg'
author: 快科技（原驱动之家）
comments: false
date: Thu, 20 Jan 2022 16:09:46 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220120/S48ada4b2-c11d-435e-aabd-824f05c82fc9.jpg'
---

<div>   
<p>最近几天，Intel的11代、12代酷睿处理器无法播放4K蓝光（UHD BD）光碟的事闹得沸沸扬扬，<a class="f14_link" href="https://news.mydrivers.com/1/809/809267.htm" target="_blank">很多玩家不解Intel为什么要跟这个功能过不去</a>，现在可以确认Intel不是故意阉割功能，而是有苦衷，安全漏洞实在太多。</p>
<p>4K蓝光播放的要求很高，不仅对处理器有兼容性要求，还要支持更高级的数字版权管理DRM技术，包括AACS 2.0高级内容访问系统、HDCP 2.2高宽带数字内容保护等等，为此蓝光协会要求处理器支持SGX技术。</p>
<p>SGX指令集从6代酷睿开始支持，一直到10代酷睿，但最新的两代酷睿砍掉支持了。</p>
<p>在发现11代、12代酷睿不能播放4K蓝光之后，<strong>很多人以为Intel是故意的，而且不通知，这也是误解Intel了，实际上他们在12代酷睿的文档中已经明确了移除SGX指令集，</strong>如下所示：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220120/48ada4b2-c11d-435e-aabd-824f05c82fc9.jpg" target="_blank"><img alt="Intel 11/12代酷睿不再支持4K蓝光：SGX漏洞成筛子了" h="412" src="https://img1.mydrivers.com/img/20220120/S48ada4b2-c11d-435e-aabd-824f05c82fc9.jpg" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>一同被砍的还有其他一些技术或者指令集，包括TSX-NI、PAIR、MPX等等，只不过这些文档几乎没有谁去看，除了专业技术人员。</p>
<p>Intel砍掉SGX指令集也是迫不得已，因为问世7年来，SGX指令集虽然有助于保护版权，但安全漏洞实在太多，已经发现了至少7种基于SGX的攻击方式：</p>
<p>·2017年发现了Prime+Probe攻击</p>
<p>·2018年披露了类似Spectre的攻击</p>
<p>·2019年研究人员发现了Enclave 攻击</p>
<p>·MicroScope重放攻击</p>
<p>·所谓的“Plundervolt”注入攻击</p>
<p>·负载值注入 (LVI)攻击</p>
<p>·对CPU缓存的SGAxe攻击等</p>
<p>在这些攻击面前，<span style="color:#ff0000;"><strong>SGX已经被打成筛子了，相较于4K蓝光播放的功能，Intel更看重安全功能，所以才选择删除SGX指令集。</strong></span></p>
<p>另外，Intel显然也认为在PC上播放4K蓝光是非常小众的需求，可替代的方式太多了，综合影响确实不大，如果不是媒体报道，可能很多人都没注意到这个变化。</p>
<p style="text-align: center"><img alt="Intel 11/12代酷睿不再支持4K蓝光：SGX漏洞成筛子了" h="420" src="https://img1.mydrivers.com/img/20220120/bc055516-0400-436d-96f5-36cf1572aeeb.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/intel.htm"><i>#</i>Intel</a><a href="https://news.mydrivers.com/tag/cpuchuliqi.htm"><i>#</i>CPU处理器</a><a href="https://news.mydrivers.com/tag/languang.htm"><i>#</i>蓝光</a></p>
<p class="url">
     
<span>责任编辑：宪瑞</span>
</p>
        
</div>
            