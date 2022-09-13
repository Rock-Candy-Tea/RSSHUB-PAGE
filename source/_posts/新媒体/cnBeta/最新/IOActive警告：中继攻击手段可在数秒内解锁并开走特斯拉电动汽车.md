
---
title: 'IOActive警告：中继攻击手段可在数秒内解锁并开走特斯拉电动汽车'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0913/3ba716f69316d12.jpg'
author: cnBeta
comments: false
date: Tue, 13 Sep 2022 08:49:29 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0913/3ba716f69316d12.jpg'
---

<div>   
尽管特斯拉已经在网络安全保障上付出了相当大的心力，但其精心设计的系统，还是难以应付层出不穷的攻击类型。<strong>比如近日，IOActive 首席安全顾问 Josep Pi Rodriguez 就发现了所谓的“NFC 中继攻击”。</strong>尽管需要团伙中的两个人协作，但只需几秒钟就能窃取权限的这一手段，还是给特斯拉和 Model Y 的车主们敲响了警钟。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0913/3ba716f69316d12.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://act-on.ioactive.com/acton/attachment/34793/f-6460b49e-1afe-41c3-8f73-17dc14916847/1/-/-/-/-/NFC-relay-TESlA_JRoriguez.pdf" target="_self">IOActive</a>）</p><p>具体说来是，一名窃贼需要靠近汽车、而团伙中的另一人需要贴近车主 —— 以中继 NFC 卡片，或<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>、口袋、钱包里的虚拟钥匙信号。</p><blockquote><p>● NFC 是‘近场通讯’的简称，而特斯拉车主们可以贴近 B 柱的读卡器来解锁并发动其车辆。</p><p>● 此外尽管车主们可使用手机遥控 / 虚拟钥匙来解锁，但为防万一（丢失钥匙或手机没电），官方手册还是建议他们随身携带 NFC 卡片作为备用钥匙。</p></blockquote><p>而在 Rodriguez 的演示场景中，攻击者只需靠近带有 NFC 卡片、或手机虚拟钥匙大约 2 英寸范围内 —— 比如在路上贴身走过、或在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C752%2C761" target="_blank">咖啡</a>馆 / 餐厅里排队之时。</p><p><img src="https://static.cnbetacdn.com/article/2022/0913/48c0b70f05931d3.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>演示期间，第一名黑客利用 Proxmark RDV4.0 设备，启动司机侧门柱中的 NFC 读卡器的通信。正常状况下，此时车载系统会向车主的 NFC 卡发送问答信号。</p><blockquote><p>但在中继攻击中，Proxmark 设备可通过 Wi-Fi 或蓝牙，将询问信号传输到同伙那边的移动设备 —— 通过贴近车主的口袋或钱包，与钥匙卡取得通信并回传信号。</p><p>即使 Wi-Fi 和蓝牙信号限制了两个同谋之间的作案距离，但若使用树莓派来中继信号，范围就可以扩展到数英尺、甚至通过互联网而实现更遥远的攻击。</p></blockquote><p>当然这套方案也不是无懈可击，比如一旦停好车，他们就无法重新启动。但若同伙需要多花一些时间才能靠近车主，Proxmark 还是可以向汽车不断发起问询。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=382781260&autoplay=false&disablePlaylist=true" width="420" height="700" frameborder="0"></iframe></p><p style="text-align: center;">IOActive NFC Relay Attack Tesla Y（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMzgyNzgxMjYwLnNodG1s.html" target="_self">via</a>）</p><p>其实直到去年，使用 NFC 钥匙卡解锁的特斯拉车主，还是需要将卡片留在前排座椅中间的控制台上，以激活换挡和驾驶功能。</p><p>但出于体验优化的考虑，官方又于去年的软件更新中取消了这一额外步骤 —— 现只需在解锁后两分钟内踩下制动踏板，即可操控特斯拉电动汽车汽车。</p><p>作为应对，安全研究人员建议车主们设置 PIN 码，那样就可以在启动车子前加上一道安全保障（当然车内贵重物品还是可能被窃取）。遗憾的是，许多人甚至不知道这项功能的存在。</p>   
</div>
            