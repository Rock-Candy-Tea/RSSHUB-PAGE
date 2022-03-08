
---
title: 'Win10_11下锐龙处理器出现卡顿、死机bug AMD确认5月发新BIOS'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202203/6226bc9cb15ec03f5a72e20a_1024.jpg'
author: ZAKER
comments: false
date: Mon, 07 Mar 2022 21:10:44 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202203/6226bc9cb15ec03f5a72e20a_1024.jpg'
---

<div>   
<p>前不久我们报道过 AMD 的锐龙处理器在微软 Win11 系统下会出现卡顿、死机等 bug，Win10 下也有类似的问题，现在几个月过去了 AMD 官方已经调查出根源了，跟主板的 SPI ROM 有关，5 月份会发新版 BIOS 解决。</p><p>此前这个问题被认为与 fTPM 有关，AMD 平台开启 fTPM 就有可能出现周期性死机、卡顿、系统不稳定、声音播放出现噼啪声及屏幕鼠标乱窜等问题，禁用 fTPM 之后问题就会消失。</p><p>AMD 调查之后确认，问题的根源在于锐龙平台的主板上的 SPI ROM 闪存，锐龙的配置可能会让它间歇性执行与 fTPM 相关的扩展内存事务，这可能会导致系统交互及响应暂停。</p><p>AMD 提供了一种临时解决办法，那就是将系统的 fTPM 设置切换到 dTPM，后者使用的是 NVROM 与 TPM 交互，不过前提是用户的设备支持 dTPM 功能，而且切换 TPM 意味着加密要换，需要确保自己的数据备份没问题。</p><p>最终的解决办法需要升级 BIOS，AMD 表示今年 5 月上旬会推出新的补丁升级，可能会基于 AGESA 1207 或者更高版本的微代码，具体的计划要等主板厂商的测试和升级结果。</p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202203/6226bc9cb15ec03f5a72e20a_1024.jpg" data-height="397" data-width="600" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202203/6226bc9cb15ec03f5a72e20a_1024.jpg" referrerpolicy="no-referrer"></div></div><p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            