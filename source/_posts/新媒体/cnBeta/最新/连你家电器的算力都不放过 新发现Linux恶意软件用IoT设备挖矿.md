
---
title: '连你家电器的算力都不放过 新发现Linux恶意软件用IoT设备挖矿'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://pics5.baidu.com/feed/2e2eb9389b504fc264ec047eb715e61a91ef6d69.png@f_auto?token=1e208668e29ce4fbccf47cd3d3c8fd2f'
author: cnBeta
comments: false
date: Sun, 25 Sep 2022 08:53:07 GMT
thumbnail: 'https://pics5.baidu.com/feed/2e2eb9389b504fc264ec047eb715e61a91ef6d69.png@f_auto?token=1e208668e29ce4fbccf47cd3d3c8fd2f'
---

<div>   
继电脑和手机后，挖矿病毒也盯上了IoT设备。无论是智能冰箱、彩电还是洗衣机，但凡有点算力的（物联网和端侧）设备都可能被这种病毒感染，用于挖掘加密货币等。AT&T Alien Labs新发现的Linux恶意软件Shikitega就是一例。<br>
 <p>相比之前的一些IoT设备，Shikitega更加隐蔽，总共只有376字节，其中代码占了300字节。</p><p>那么，这个新型恶意软件究竟是如何感染设备的？</p><p>利用加壳技术“隐身”</p><p>具体来说，Shikitega核心是一个很小的ELF文件（Linux系统可执行文件格式）。</p><p><img src="https://pics5.baidu.com/feed/2e2eb9389b504fc264ec047eb715e61a91ef6d69.png@f_auto?token=1e208668e29ce4fbccf47cd3d3c8fd2f" width="640" referrerpolicy="no-referrer"><br></p><p>这个ELF文件加了动态壳，以规避一些安全防护软件的查杀。</p><p>加壳，指利用特殊算法压缩可执行文件中的资源，但压缩后的文件可以独立运行，且解压过程完全隐蔽，全部在内存中完成。</p><p>动态壳则是加壳里面更加强力的一种手段。</p><p>从整体过程来看，Shikitega会对端侧和IoT设备实施多阶段感染，控制系统并执行其他恶意活动，包括加密货币的挖掘（这里Shikitega的目标是门罗币）：</p><p><img src="https://pics6.baidu.com/feed/d50735fae6cd7b8961c384f156ec43acd8330e6c.png@f_auto?token=f8f375b3fe57828759471d03e3ed6270" width="640" referrerpolicy="no-referrer"><br></p><p>通过漏洞利用框架Metasploit中最流行的编码器Shikata Ga Nai（SGN），Shikitega会运行多个解码循环，每一个循环解码下一层。</p><p>最终，Shikitega中的有效载荷（恶意软件的核心部分，如执行恶意行为的蠕虫或病毒、删除数据、发送垃圾邮件等的代码）会被完全解码并执行。</p><p>这个恶意软件利用的是CVE-2021-4034和CVE-2021-3493两个Linux漏洞，虽然目前已经有修复补丁，但如果IoT设备上的旧版Linux系统没更新，就可能被感染。</p><p>事实上，像Shikitega这样感染IoT设备的恶意软件已经很常见了。</p><p>例如在今年三月，AT&T Alien Labs同样发现了一个用Go编写的恶意软件BotenaGo，用于创建在各种设备上运行的僵尸网络（Botnets）。</p><p>对此有不少网友吐槽，IoT设备的安全性堪忧：</p><p><img src="https://pics3.baidu.com/feed/80cb39dbb6fd52665bd0f1edf3d09620d60736a7.png@f_auto?token=c8e9a231f67ec61eb1f4de6ca84627e8" width="640" referrerpolicy="no-referrer"><br></p><p>也有网友认为，IoT设备应该搞WiFi隔离，不然就会给病毒“可乘之机”：</p><p><img src="https://pics7.baidu.com/feed/574e9258d109b3de64b3978cab776d8a810a4c1d.png@f_auto?token=e7c04aa29be40d88afe5b4e9dd2ed85b" width="640" referrerpolicy="no-referrer"><br></p><p>而除了IoT设备，更多人的关注点则放在了Linux系统的安全上。</p><p>Linux恶意软件数量飙升650%</p><p>这几年来，Linux恶意软件的多样性和数量都上升了。</p><p>根据AV-ATLAS团队提供的数据，新的Linux恶意软件的数量在2022年上半年达到了历史新高，发现了近170万个。</p><p>与去年同期（226324个恶意软件）相比，新的Linux恶意软件数量飙升了近650%。</p><p>除了Shikitega，近来发现的流行Linux恶意软件也变得更加多样，已知的包括BPFDoor、Symbiote、Syslogk、OrBit和Lightning Framework等。</p><p><img src="https://pics4.baidu.com/feed/50da81cb39dbb6fd12f190a653ecaa13952b37de.png@f_auto?token=5f568b2a055708e43164df33bb67a10c" width="640" referrerpolicy="no-referrer"><br></p><p>△图源AV-ATLAS</p><p>对此有网友提出疑惑，正因为Linux开源，它似乎无论如何都会面临病毒和恶意软件的泛滥？</p><p><img src="https://pics4.baidu.com/feed/83025aafa40f4bfb29f86f3a588779fbf6361883.png@f_auto?token=98d834705b79e9d52fd9aa46dd7626dc" width="640" referrerpolicy="no-referrer"><br></p><p>有网友回应称，一方面，虽然旧的Linux系统可能充满漏洞、成为病毒的“温床”，但它在经过升级、打了补丁之后就会变好。</p><p>另一方面，开发恶意软件本身也不是“有手就能做”的事情。</p><p>毕竟安全研究人员会不断修复并堵上所有漏洞，而恶意软件开发者必须在他们修复前找到漏洞、开发出恶意软件，还得让它们“大流行”，最终实现自己的目的。</p><p><img src="https://pics1.baidu.com/feed/9213b07eca806538016f6ff4cb15a04faf3482a7.png@f_auto?token=48352f107a7c27bab2282ee44ff3231b" width="640" referrerpolicy="no-referrer"><br></p><p>要是你家还有在用老旧Linux系统的设备，要注意及时升级or做好网络隔离等安全措施~</p>   
</div>
            