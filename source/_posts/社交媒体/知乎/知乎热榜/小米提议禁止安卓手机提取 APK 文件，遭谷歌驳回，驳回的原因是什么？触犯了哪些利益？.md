
---
title: '小米提议禁止安卓手机提取 APK 文件，遭谷歌驳回，驳回的原因是什么？触犯了哪些利益？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=8862'
author: 知乎
comments: false
date: Wed, 25 May 2022 09:38:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=8862'
---

<div>   
Wearone的回答<br><br><p></p><p data-pid="yU5pqVKb">看了一下小米这个工程师提交的patch，发现这个提问就不太对。 </p><p data-pid="14CtPjtg">并不是“禁止安卓手机提取 APK 文件”，而是“限制 adb shell 提取 APK 文件”，这其中的区别是非常大的。 </p><p data-pid="aWZVWIFy">小米的patch对普通用户没有影响。 </p><p data-pid="NS1_J2fQ">说白了，即使 Google 同意将这段代码合入 AOSP ，Android 用户依然可以通过各种方式提取 APK，只是在使用 adb shell 提取的时候多了一些限制，仅此而已。这个 patch Google是否通过，都对普通用户没有影响。 </p><p data-pid="ZBepML_8">像“彻底阻止 Android 设备所有者从手机中复制 APK 文件”这是错误的解读。这个 patch 并不阻止用户从手机中复制 APK 文件，也完全不阻止用户从各种非官方渠道安装 APK ，也不会让 Android 走向闭源。像小米互传这种支持直接分享 APK 的功能，就完全不会受到什么影响。 </p><h3>什么是 adb shell ？ </h3><p data-pid="dqvRUP72">简单来说，adb shell 是 Android 工程师在调试应用时使用的命令行开发工具，adb 工具是在电脑上使用的，所以对于普通的手机用户来说，adb 工具怎么改都不会影响他们的日常操作。 </p><h3>小米为什么要这么改（限制 adb shell 提取 APK 文件）？ </h3><p data-pid="yQZ7Y0x_">小米的所提交的这个改动，最有可能影响到的场景，是用户将手机插到电脑上（当然无线调试也行），然后电脑在用户不知情的情况下将用户安装的 APK 都提取到本地。可能是小米在历史上曾经监测到相关的情况，所以提出了这种改进措施。 </p><p data-pid="u9UqB8lY">另一种可能是小米为了保护自己的系统App，防止用户胡乱提取安装，造成一些不兼容的问题。</p><p data-pid="WB0b7Gxx">（这种可能我也问下了小米同学有没有案例，得到的答案是肯定的，他们说：去年有一个发烧友提取了安全中心的一个测试版，然后发给别人，导致一堆人升级MIUI13之后无限重启，小米内部自查原因，查了好久才发现。） </p><h3>Google 为什么没同意？ </h3><p data-pid="3hGLA1In">核心原因是这个 patch 在 Google 看来没用，并没有实现小米的这个工程师想达到的目的。Google 工程师的意思是，用户有非常多的方式去绕过这个限制，你只是稍微提高了门槛，意义不大。 </p><p data-pid="SQ-e81mG">Google 的观点可以说是：对，也不对。 </p><p data-pid="UwbfnR78">Google 想的是，我们都是开发者，绕过这个限制还不简单，稍微抬高点门槛就是多此一举。Google 没想到的是，有很多恶意软件或者普通用户，其实并不是开发者，稍微抬高点门槛就足以把他们挡在外面了。 </p><p data-pid="Sn3nq2qQ">Google 在做决策的时候，并不会考虑中国市场的特殊性，跟小米所处的环境完全不同，所以对同样的问题有完全不同的考虑角度，再正常不过了。</p><p data-pid="LNfNxz1U">这也让我想到了当初小米MIX的时候，小米团队多次拜访谷歌团队才打开了屏幕比例限制，让现在全面屏遍地开花</p>  
</div>
            