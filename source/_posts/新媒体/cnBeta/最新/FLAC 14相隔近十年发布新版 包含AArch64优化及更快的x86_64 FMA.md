
---
title: 'FLAC 1.4相隔近十年发布新版 包含AArch64优化及更快的x86_64 FMA'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0911/559f6c9297d5b16.png'
author: cnBeta
comments: false
date: Sun, 11 Sep 2022 12:51:03 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0911/559f6c9297d5b16.png'
---

<div>   
FLAC 1.4于周五发布，作为"自由无损音频编解码器"，它以其强大可靠而无成本的数字音频无损压缩而闻名。自FLAC 1.3（2013年5月）发布以来已经有近十年的时间，周五带来的FLAC 1.4系列的发布引入了一系列改进。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0911/559f6c9297d5b16.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0911/559f6c9297d5b16.png" title alt="FLAC_logo_vector.svg.png" referrerpolicy="no-referrer"></a></p><p>随着FLAC 1.4的发布，现在的性能优化集中在具有NEON指令的ARMv8（AArch64）硬件上。从<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>M1/M2到Ampere Altra和其他各种硬件，在这个新的FLAC版本中，AArch64的性能应该会好很多。</p><p>在x86_64方面，FLAC 1.4为支持FMA指令的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>/<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>处理器下运行的表现带来了明显的提升。</p><p>FLAC 1.4中的一些其他改进包括编码/解码32位PCM，编码文件的采样率高达1048575Hz，还有编码预设的改进，FLAC格式文档的重写，CMake构建系统的改进，以及其他各种各样的补充和修复。</p><p><strong>您可以通过GitHub下载和了解更多关于FLAC 1.4更新的细节：</strong></p><p><a href="https://github.com/xiph/flac/releases/tag/1.4.0" _src="https://github.com/xiph/flac/releases/tag/1.4.0" target="_blank">https://github.com/xiph/flac/releases/tag/1.4.0</a><br></p>   
</div>
            