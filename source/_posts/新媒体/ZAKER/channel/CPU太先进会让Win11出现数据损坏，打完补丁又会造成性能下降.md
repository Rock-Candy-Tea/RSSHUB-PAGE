
---
title: 'CPU太先进会让Win11出现数据损坏，打完补丁又会造成性能下降'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/62f3775e8e9f096903316e0a_1024.jpg'
author: ZAKER
comments: false
date: Wed, 10 Aug 2022 05:09:27 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/62f3775e8e9f096903316e0a_1024.jpg'
---

<div>   
<p>微软日前确认，Windows 11 和 Windows Server 2022 存在 BUG，在支持 VAES 指令集的环境下，可能到导致数据损坏。</p><p>Intel 从 10 代酷睿（Ice Lake ）和第三代至强可扩展处理器（IceLake-SP）开始才添加了对 VAES 的支持，AMD 这边则是 Zen 3 锐龙 5000，它也是 AVX-512 的组成部分。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202208/62f3775e8e9f096903316e0a_1024.jpg" data-height="349" data-width="612" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/62f3775e8e9f096903316e0a_1024.jpg" referrerpolicy="no-referrer"></div></div>没想到，因为处理器太先进，导致密码本算法模式不同，进而可能造成数据损毁。<p></p><p>不过，微软接着表示，早在 5 月（预览版）、6 月份（正式版），它们就推送了修复补丁。</p><p>本来遇到这样的 BUG 已经很无语了，没想到修复方案更令人尴尬。</p><p>可更尴尬的事情在于，打补丁后会造成性能下降，尤其是在 BitLocker、TLS、硬盘密集传输负载场景下时，调用 AES 指令集的任务可能因此慢两倍。</p><p>被炮轰后，微软现在建议用户再次安装 6 月 23 日和 7 月 12 日的最新补丁，这次通过修改 Windows 核心加密库的代码路径，减轻了性能下滑问题。</p><p>编辑：熊乐</p><p>· END<strong>·</strong></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            