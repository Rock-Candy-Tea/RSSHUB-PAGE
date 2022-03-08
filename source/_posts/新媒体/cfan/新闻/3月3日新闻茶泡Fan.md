
---
title: '3月3日新闻茶泡Fan'
categories: 
 - 新媒体
 - cfan
 - 新闻
headimg: 'https://upload.cfan.com.cn/2022/0303/1646274141899.jpg'
author: cfan
comments: false
date: Thu, 03 Mar 2022 10:23:00 GMT
thumbnail: 'https://upload.cfan.com.cn/2022/0303/1646274141899.jpg'
---

<div>   
<p><strong>Intel将物理封杀AVX512</strong></p>
<p>在12代酷睿Alder Lake处理器上，AVX512加速指令集一度引发了猫抓老鼠的游戏，Intel之前通过BIOS的方式封杀了AVX512，但主板厂商想办法破解并解锁AVX512，现在Intel发大招，将从物理级别封杀AVX512。</p>
<p>AVX512是Intel最新的AVX适量扩展指令集，可以大幅提升浮点性能，这一版指令集首发于2013年，主要是给至强处理器用的，这几年来在消费级酷睿上也有支持。</p>
<p>在最新的12代酷睿上，Intel从来提到过处理器支持AVX512，但实际使用中有用户发现可以开启AVX512支持，只需要禁用E-Core，也就是能效核，P-Core性能核就可以支持AVX512了。禁用E核，再加上AVX512加速指令集在部分应用有奇效，可大幅提升性能，所以很多玩家都很喜欢它，而主板厂商也为了满足消费者，开始绕过Intel的限制恢复AVX512支持，方法就是允许消费者切换新旧版BIOS。这种来回折腾也让Intel下定决心彻底封禁12代酷睿的AVX512支持，那就是将推出新版12代酷睿，直接物理层面上禁用AVX512。</p>
<p>TH网站得到Intel的确认，称早期的12代酷睿Alder Lake上没有禁用熔断器，但Intel计划在未来的Alder Lake上禁用AVX512。虽然还不确定新版12代酷睿什么时候上市，但是AVX512支持这件事很快就要终结了，Intel态度很坚定，需要AVX512的就去买更贵的至强处理器。</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0303/1646274141899.jpg" border="0" alt="1bcbed3a-af2a-4830-902f-89da43ecef26" referrerpolicy="no-referrer"></p>
<p><strong>NVIDIA RTX 40显卡暴力堆缓存</strong></p>
<p>看起来黑客们这次泄露的NVIDIA文件数据有太多真材实料，除了要命的DLSS源代码，还有未来显卡的诸多秘密。目前看，Hopper、Blackwell是未来两代一代计算卡，Ada Lovelace则是下一代游戏卡，也就是RTX 40系列。</p>
<p>根据最新挖掘到的信息，RTX 40系列将拥有“海量”的二级缓存，每16-bit显存位宽对应16MB。具体来说，顶级大核心AD102拥有384-bit位宽、96MB二级缓存，AD103 256-bit、64MB，AD104 192-bit 48MB，AD106、AD107则都是128-bit 32MB。</p>
<p>据说还有个超小核心AD10B(不是AD108)，暂时没看到缓存指标，估计64-bit、16MB？不过目前的RTX 30系列家族并没有如此小规模的核心，现在还不清楚AD10B这个名字都很特殊的核心，会有什么不一样。相比之下，Ampere RTX 40系列的二级缓存都非常小，GA102也不过区区6MB，GA103/GA104 4MB，GA106 3MB，GA107 2MB，两代整整16倍的差异！</p>
<p>有趣的是，AMD RDNA2架构引入了Infinity Cache无限缓存，最大容量128MB——NVIDIA这是要反击的节奏？</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0303/1646274151417.jpg" border="0" alt="s_1552547ab6574ad4ae7e80aaa04f35bb" referrerpolicy="no-referrer"></p>
<p><strong>美光发布世界最强176层SSD</strong></p>
<p>美光昨天宣布，已经试产全新的7450系列SSD。这是全球首个基于176层垂直堆叠NAND闪存的数据中心SSD，也是迄今最强悍的176层产品。早在2020年11月，美光就全球首发了176层TLC闪存，创造堆叠新纪录，此后陆续基于此发布了多款产品，包括3400/2450系列，旗下品牌英睿达的P5 Plus系列等。</p>
<p>最近，美光又量产了176层QLC闪存，并发布了2400系列SSD。以上产品都是面向消费级市场，最新的美光7450系列则针对服务器、数据中心，使用的是TLC闪存，平均故障间隔时间200万小时，五年质保。它细分为7450 PRO、7450 MAX两个子系列，并提供多种形态，包括U.3 15/7mm、E1.S 25/15/5.9mm、M.2 2280/22110。</p>
<p>7450 PRO系列面向读取密集型应用，支持每天1次全盘写入，容量方面U.3 960GB-15.36TB、E1.S 960GB-7.68TB、M.2 480GB-3.84TB，性能也各有不同，持续读写最高6.8GB/s、5.3GB/s，随机读写最高100万IOPS、21.5万IOPS。</p>
<p>7450 MAX锡类面向混合读写应用，支持每天3次全盘写入，容量方面U.3 800GB-12.8TB、E1.s 800-6.4TB、M.2 400-3.2TB(冗余空间更多)，性能最高持续读写也是6.8GB/s、5.3GB/s，随机读写则是100万IOPS、41万IOPS。</p>
<p>技术方面，支持PCIe 4.0、NVMe 1.4、掉电保护、数据路径保护、128命名空间、TYAA安全标准、SED加密、TCG Opal 2.01、IEEE1667、FIPS 140-3 Level 2等等。</p>
<p>最特别的是，它可以在99.9999% QoS下提供2ms的超低延迟，能够很好地满足SQL Server、Oracle、MySQL、RocksDB、Cassandra、Aerospike等应用环境的需求。</p>
<p>价格？那自然是没有的。</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0303/1646274160964.png" border="0" alt="s_6dde1918d831478c95d378133f86cf6d" referrerpolicy="no-referrer"></p>
<p><strong>Intel傲腾硬盘、内存有点悬</strong></p>
<p>在前几天的Intel投资者会议上，官方发布了酷睿、至强、GPU及先进工艺等路线图，一直畅想到2025年，然而这次会议上有个重要产品没了身影，那就是傲腾Optane，这让它的未来蒙上了一层阴影。</p>
<p>2020年Intel开始剥离存储芯片业务，以90亿美元的价格将闪存业务卖给了SK海力士，现在交易都已经完成了，但是Intel当时保留了傲腾业务，这种先进技术是打算掌握在自己手里的。</p>
<p>早在2015年7月份，Intel联合美光宣布推出革命性存储芯片3D Xpoint，号称速度是NAND闪存的1000倍，耐用性也是目前闪存的1000倍，密度是NAND的10倍，堪称25年最大存储芯片最大突破。基于3D Xpoint芯片的产品被Intel命名为傲腾，先后推出了多款产品，包括SSD及内存，速度、延迟及可靠性等核心指标上确实远超闪存，不过1000倍的差距倒是没有。</p>
<p>当初备受重视，现在的傲腾似乎被打入了冷宫，不仅路线图中没有看到未来的傲腾产品，就连CEO基辛格也不待见，德国Golem网站报道称基辛格表示从来没想到从事内存业务。</p>
<p>目前傲腾产品线最终的命运还没确定，但是它在过去几年中导致了巨额亏损，这肯定会影响Intel高层对它的看法，2020年亏损5.76亿美元，2021年预计亏损超过10亿美元，以致于傲腾业务负责人都被换掉了。</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0303/1646274169992.png" border="0" alt="a5d48270-e178-4aab-a28f-062afcd16d7e" referrerpolicy="no-referrer"></p>
<p><strong>OPPO Find X5系列开售</strong></p>
<p>前不久，OPPO举行新品发布会，正式发布OPPO Find X5系列，包括OPPO Find X5、OPPO Find X5 Pro和OPPO Find X5 Pro天玑版三款机型。经过多日等待，OPPO Find X5、OPPO Find X5 Pro于今日上午10:00正式开售，售价3999元起（Pro版 8+256GB、天玑9000版将在3月18日开售，水蓝12+256GB版4月1日开售）。</p>
<p>显示方面，OPPO Find X5 Pro配备6.7英寸AMOLED 2K 120Hz屏，支持智能动态刷新率技术，可实现1-120Hz的无感变频，峰值亮度1300nit，支持10.7亿色彩。而OPPO Find X5采用了一块6.55英寸1080P全面屏，支持120Hz刷新率，与Pro版相比，最大的区别就是没有了LTPO 2.0 2K屏。</p>
<p>核心配置上，OPPO Find X5 Pro搭载骁龙8处理器，前置3200万，后置5000万主摄、5000万超广角和1300万长焦，内置5000mAh电池，支持80W有线、50W无线闪充；OPPO Find X5搭载高通骁龙888旗舰处理器，前置3200万，后置5000万主摄、5000万超广角和1300万长焦三摄，内置4800mAh电池，支持80W有线、30W无线快充。</p>
<p>两款新机均首发搭载了OPPO自研芯片马里亚纳MariSilicon X，这是一颗由台积电代工的6nm影像专用NPU芯片。</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0303/1646274177430.png" border="0" alt="s_494b749de8ff44abab7c4089d3213a21" referrerpolicy="no-referrer"></p>
<p><strong>Chrome 99稳定版发布</strong></p>
<p>谷歌的Chrome已经成为使用最广泛的浏览器，版本号也刷得厉害，日前Chrome 99版的稳定版正式发布，这将是最后一个双位数的版本，Chrome 100版在开发版通道已经推出，月底就要正式版了。</p>
<p>Chrome 99的升级内容不多，功能性方面主要是将下载按钮从底部移动到了工具栏顶部，而且会有更好的提示，下载东西的时候是蓝色，下载完成后变成灰色按钮。其他方面，Chrome 99还可以为表单使用系统日期选择器，这个功能对一些开发者来说很重要。另外就是内置手写识别API，该功能从Chrome 91版就在测试，现在终于正式集成，开发者不需要第三方API了。</p>
<p>安全性方面，Chrome 99修复了28个安全漏洞，其中11个是高危险性漏洞，15个中等危险漏洞，还有2个低风险漏洞，具体信息不用管，升级就行了。</p>
<p>Chrome 99稳定版已经陆续开始推送，下一个版本是Chrome 100，开发版通道已经升级了，正式版预计在3月29日发布。Chrome 100是首次上三位数，有可能会给一些网站带来不兼容问题，不过影响也不大，谷歌也在解决这个问题。类似的还有FireFox 100、微软Edge 100，三位数的版本号多少都会有些问题，好在都能解决，不会影响使用。</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0303/1646274189915.jpg" border="0" alt="s_ae155e08706d4aaaaaf34b976a0b9c28" referrerpolicy="no-referrer"></p>
<p><strong>互联网弹窗不得推送恶意炒作娱乐八卦内容</strong></p>
<p>过去一年时间，国家网信办曾多次对APP弹窗进行专项整治，现在网信办又要进一步明确互联网弹窗的管理规定。</p>
<p>据网信办官网公告，为了进一步规范互联网弹窗信息推送服务管理，保障公民、法人和其他组织的合法权益，弘扬社会主义核心价值观，营造清朗网络空间，根据《中华人民共和国网络安全法》《中华人民共和国未成年人保护法》《中华人民共和国广告法》《互联网信息服务管理办法》《网络信息内容生态治理规定》等法律法规，我办起草了《互联网弹窗信息推送服务管理规定（征求意见稿）》，现向社会公开征求意见。</p>
<p>其中提到，互联网弹窗不得推送恶意炒作娱乐八卦、绯闻隐私、奢靡炫富、审丑扮丑等违背公序良俗内容；弹窗推送广告信息不得违反国家相关法律法规；应当具有可识别性，显著标明“广告”，明示用户；确保弹窗广告一键关闭。不得设置诱导用户沉迷、过度消费等违反法律法规或者违背伦理道德的算法模型。</p>
<p>同时，也不得设置诱导用户沉迷、过度消费等违反法律法规或者违背伦理道德的算法模型；不得滥用个性化弹窗服务，利用算法屏蔽信息、过度推荐等。不得滥用算法，针对未成年用户进行画像，向未成年用户推送可能影响其身心健康的信息等。</p>
<p>《互联网弹窗信息推送服务管理规定（征求意见稿）》原文如下：</p>
<p style="text-align: center; text-indent: 0;"><img src="https://upload.cfan.com.cn/2022/0303/1646274197600.png" border="0" alt="b054d6d2df174062aaf434c07ba95bb5" referrerpolicy="no-referrer"></p>　  
</div>
            