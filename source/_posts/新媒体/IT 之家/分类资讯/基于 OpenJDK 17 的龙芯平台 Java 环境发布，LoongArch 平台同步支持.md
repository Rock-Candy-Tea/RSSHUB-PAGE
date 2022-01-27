
---
title: '基于 OpenJDK 17 的龙芯平台 Java 环境发布，LoongArch 平台同步支持'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/1/a27aa8fb-2c1d-4578-a60b-475d2a919722.png'
author: IT 之家
comments: false
date: Thu, 27 Jan 2022 06:41:44 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/1/a27aa8fb-2c1d-4578-a60b-475d2a919722.png'
---

<div>   
<p data-vmark="839d"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 1 月 27 日消息，龙芯中科今日于龙芯开源社区正式对外发布<span class="accentTextColor">基于 OpenJDK 17 的龙芯平台 Java 环境</span>。</p><p data-vmark="7439">Java 17 提供了数千种性能、稳定性和安全性更新，以及 14 个 JEP（JDK Enhancement Proposal，即 JDK 增强建议）来进一步优化 Java 语言和平台，从而帮助开发人员提高工作效率。</p><p data-vmark="4c88">IT之家了解到，此次新发布的版本，除了上述上游更新以外，龙芯团队针对龙芯平台特别是 LoongArch 平台进行了新功能开发和优化，具体如下：</p><h2 data-vmark="61b0">符合 TCK 标准：</h2><p data-vmark="c997">龙芯平台 Java 17 环境经过验证符合 Java SE 17，新应用程序和现有应用程序无需修改即可运行。</p><h2 data-vmark="f212">支持 C1 编译器和分层编译：</h2><p data-vmark="b2f9">C2 编译器（Server Compiler）主要满足了 Java 应用的峰值性能需求，此次发布的 LoongArch64 平台环境支持 C1 编译器（Client Compiler）和分层编译，可进一步满足对启动性能有要求的 Java 应用，比如桌面应用。</p><p data-vmark="e719">通过实测，龙芯平台开启 C1 和分层编译之后，部分应用得到了显著提升：Eclipse 启动时间减少 16.4%，NetBeans 启动时间减少 20.1%，SPECjvm2008 中的 startup 项提升 13.4%，Dacapo 中 luindex 和 fop 用时分别降低 31.9% 和 29.2%。</p><h2 data-vmark="f777">LoongArch 向量指令优化：</h2><p data-vmark="bc5e">此次版本通过使用 LoongArch 向量指令对 C2 编译器进行了自动向量化优化，同时还进行了 Vector API 的硬件支持。</p><p data-vmark="a278">通过实测，开启向量优化后，在 LoongArch64 平台上 SPECjvm2008 中的 scimark.lu.small 提升了 102.7%，JMH Microbenchmarks 含有 Vector 关键字的 168 项测试中，计时类测试中有 39 项用时降低 1/2 以上，吞吐量类测试中有 26 项提升 2 倍以上、其中最高项提升了 200 倍以上。</p><h2 data-vmark="a12b">支持 ZGC：</h2><p data-vmark="5f5d">ZGC（The Z Garbage Collector），是一款低延迟垃圾回收器，它的设计目标包括：</p><ul class=" list-paddingleft-2"><li><p data-vmark="2533">亚毫秒级最大停顿时间</p></li><li><p data-vmark="ce2f">暂停时间不随堆的大小、存活集及根集的大小的增加而增加</p></li><li><p data-vmark="e995">支持 8MB 至 16TB 级别的堆大小</p></li></ul><p data-vmark="681d">通过实测，龙芯平台（LoongArch64）开启 ZGC 后，在 3C5000L 双路上 SPECjbb2015 max-jOPS 提升 27.8%，critical-jOPS 提升 200% 以上。</p><p data-vmark="76f7"><img src="https://img.ithome.com/newsuploadfiles/2022/1/a27aa8fb-2c1d-4578-a60b-475d2a919722.png" w="800" h="470" alt="Specjbb2015-zgc.png" title="基于 OpenJDK 17 的龙芯平台 Java 环境发布，LoongArch 平台同步支持" width="800" height="470" referrerpolicy="no-referrer"></p><h2 data-vmark="7cec">加解密类优化：</h2><p data-vmark="b686">此次版本通过 Intrinsics 方式使用 LoongArch 基础指令对 SHA1、SHA256、AES、MD5 以及 CRC32 相关 API 进行优化。这些优化对 SPECjvm2008 中的 crypto 等项目有显著提升效果。</p><h2 data-vmark="8f22">数组拷贝优化：</h2><p data-vmark="a2cb">此次版本针对 LoongArch 进行了数组拷贝相关操作的重构和优化。</p><p data-vmark="d9dd">通过 JMH Microbenchmarks 测试显示，org.openjdk.bench.java.lang.ArrayCopy 相关测试用例优化后平均执行时间下降 33%，最多项下降了 76.77%，SPECjvm2008 中的 serial 项优化后提升了 6% 以上。</p><h2 data-vmark="c061">原子指令优化：</h2><p data-vmark="ee65">除了上述优化以外，此次发布的版本还包含针对龙芯平台的一些故障修复。这些优化和故障修复中的部分内容已集成至龙芯平台低版本 JDK 中，更多内容会根据情况陆续集成至低版本 JDK 中。</p><p data-vmark="0091"><strong>龙芯平台 Java 17 环境：</strong><a href="http://www.loongnix.cn/%20index.php/%20Java" target="_blank">点此下载</a></p>
          
</div>
            