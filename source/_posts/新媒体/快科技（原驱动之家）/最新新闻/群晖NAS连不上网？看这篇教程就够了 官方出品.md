
---
title: '群晖NAS连不上网？看这篇教程就够了 官方出品'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220220/S2f567e07-0e3c-4cd0-92d9-773bf9e9605f.png'
author: 快科技（原驱动之家）
comments: false
date: Sun, 20 Feb 2022 14:08:35 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220220/S2f567e07-0e3c-4cd0-92d9-773bf9e9605f.png'
---

<div>   
<p>寒假归来，小部分小伙伴突然发现自己的NAS连不上了，群晖官方带来了网络诊断小教程，让你快速解决可能遇到的网络问题，一起来看看。</p>
<p><span style="color:#0000ff;"><strong>内网环境访问</strong></span></p>
<p>如果发现常用的内网 IP 地址无法访问 NAS 了，这时候可以先在电脑中下载一个Synology Assistant。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220220/2f567e07-0e3c-4cd0-92d9-773bf9e9605f.png" target="_blank"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="353" src="https://img1.mydrivers.com/img/20220220/S2f567e07-0e3c-4cd0-92d9-773bf9e9605f.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
找到自己的那台进行联机即可</p>
<p style="text-align: center"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="294" src="https://img1.mydrivers.com/img/20220220/d274f20a-75db-4123-a133-b42a95c51ede.png" style="border: black 1px solid" w="547" referrerpolicy="no-referrer"></p>
<p>如果你的 NAS 在 IP 状态中，显示的是 DHCP（自动获得 IP 地址），也建议你修改为固定 IP。</p>
<p>这样 IP 地址也不会随着路由器或 NAS 断电等原因发生变动，在家中或小型办公室中会比较方便，可以在【控制面板】>【网络】>【网络界面】中选择需要修改的网络进行【编辑】。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220220/7d371e67-f585-41aa-8505-d123d8c5d976.png" target="_blank"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="339" src="https://img1.mydrivers.com/img/20220220/S7d371e67-f585-41aa-8505-d123d8c5d976.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>大家可以根据自己家路由器的网段进行设置，务必要保证在同一网段中，最后一位地址可以尽量设置的大一些，避免和其他自动分配的设备冲突导致无法访问。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220220/a472d14e-deee-4dc8-be89-3144e908fc88.png" target="_blank"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="434" src="https://img1.mydrivers.com/img/20220220/Sa472d14e-deee-4dc8-be89-3144e908fc88.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>如果在 Synology Assistant 也无法搜到NAS，或是 NAS 的传输速度较慢，这时候就要尝试进行直连测试了。</p>
<p><strong>千兆环境中测试</strong></p>
<p>先将电脑的网络配置设为 DHCP，并关闭 Windows 网络防火墙</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220220/91b351ea-e9d9-4495-b78f-0f5662479f03.jpg" target="_blank"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="446" src="https://img1.mydrivers.com/img/20220220/S91b351ea-e9d9-4495-b78f-0f5662479f03.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>再将电脑与 NAS 用一根五类及以上的网线直接连接。同时，断开电脑的 WiFi 等其他网络连接，再次使用 Synology Assistant 进行搜索并联机，这时候你就可以在之前的 NAS【网络界面】查看 NAS 的网络状态是否为千兆。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220220/61fcb322-0e1c-4129-970e-52a32d35a38c.jpg" target="_blank"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="279" src="https://img1.mydrivers.com/img/20220220/S61fcb322-0e1c-4129-970e-52a32d35a38c.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>以及电脑的网络速度是否为 1Gbps</p>
<p style="text-align: center"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="563" src="https://img1.mydrivers.com/img/20220220/42130bb1-520a-4be1-b14e-bb594a3ef106.jpg" style="border: black 1px solid" w="407" referrerpolicy="no-referrer"></p>
<p>你还可以通过文件协议的形式，做一下传输文件测试（建议准备一个大于10G的ISO或压缩包进行测试），看看速度是否能达到千兆。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220220/72c1b77b-3105-4065-b6a6-e1cc1e324820.jpg" target="_blank"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="196" src="https://img1.mydrivers.com/img/20220220/S72c1b77b-3105-4065-b6a6-e1cc1e324820.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>万兆环境中测试</strong></p>
<p>要是你财力雄厚，拥有万兆环境，比如 DS1621+、DS1821+还配了万兆交换机和万兆网卡，那么在连接上 NAS 开始测试前还要记得三点：</p>
<p>1.测试用的网线最好换成六类及以上的网线</p>
<p>2.将网卡 MTU 调为 9000（万兆需要较高的MTU才能达到正常速度）</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220220/e1b5fe75-0bb5-4d04-aa1f-fba7a7c900e6.jpg" target="_blank"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="195" src="https://img1.mydrivers.com/img/20220220/Se1b5fe75-0bb5-4d04-aa1f-fba7a7c900e6.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>3.将电脑的网口 MTU 也调整为 9000，并开启电脑网卡的巨型帧</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220220/17b45b7f-178b-4aa6-bb3b-44dff5bda4f0.jpg" target="_blank"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="699" src="https://img1.mydrivers.com/img/20220220/S17b45b7f-178b-4aa6-bb3b-44dff5bda4f0.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="545" src="https://img1.mydrivers.com/img/20220220/b65335c4-2204-495a-995b-52a1f1f45135.jpg" style="border: black 1px solid" w="475" referrerpolicy="no-referrer"></p>
<p style="text-align: center"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="575" src="https://img1.mydrivers.com/img/20220220/72cdc918-9743-47d7-b64c-5fbc9d04d4a0.jpg" style="border: black 1px solid" w="459" referrerpolicy="no-referrer"></p>
<p>如果你是macOS，则可以参照下图设置：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220220/f27d8d1d-4d1e-4a72-a83f-57e7c3345473.jpg" target="_blank"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="500" src="https://img1.mydrivers.com/img/20220220/Sf27d8d1d-4d1e-4a72-a83f-57e7c3345473.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220220/55b66aac-b80c-4aa3-a8b9-b1e5450cbd5f.jpg" target="_blank"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="489" src="https://img1.mydrivers.com/img/20220220/S55b66aac-b80c-4aa3-a8b9-b1e5450cbd5f.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>随后就可以进行网络状态的查看，以及文件传输测试了。</p>
<p>需要注意的是，在直连测试中，如果你在直连过程中无法搜索到 NAS，或是完成上述操作后传输速度依旧不正常，建议你联系我们的售后技术支持，来解决问题。</p>
<p>如果直连测试一切正常，但是将 NAS 放回到正常网络环境中，又会出现问题。很有可能是路由器、交换机等其他网络设备出现了故障，需要联系对应的厂商进行排查。</p>
<p><span style="color:#0000ff;"><strong>外网环境</strong></span></p>
<p>如果出现 NAS 无法访问外网的情况比如：套件中心无法正常显示、套件无法正常下载等，但网络中的其他设备都能正常联网，可以尝试以下步骤进行排查：</p>
<p><strong>排除浏览器问题</strong></p>
<p>使用 Firefox 或 Chrome 浏览器登录 NAS可以避免浏览器不兼容导致的页面加载异常</p>
<p><strong>排除系统时间故障</strong></p>
<p>在【控制面板】>【区域选项】>【时间】中，选择【与 NTP 服务器同步】，并将服务器地址选为【pool.ntp.org】点击【立即更新】，以此来同步正确的系统时间如果无法自动同步，也可以手动指定正确的时间。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220220/b7a07d21-6450-4b95-bf11-67197cad3051.jpg" target="_blank"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="415" src="https://img1.mydrivers.com/img/20220220/Sb7a07d21-6450-4b95-bf11-67197cad3051.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>排除 DNS 故障</strong></p>
<p>在【控制面板】>【网络】中更改 DNS 为 223.5.5.5 或 180.76.76.76</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220220/9ab90296-3ee4-4b54-b47e-8e7075bc8d89.jpg" target="_blank"><img alt="群晖NAS连不上网？看这篇教程就够了 官方出品" h="325" src="https://img1.mydrivers.com/img/20220220/S9ab90296-3ee4-4b54-b47e-8e7075bc8d89.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>排除其他网络问题</strong></p>
<p>这点就比较多样化了，大家可以根据自己的网络环境检查，比较常见的有检查路由器或防火墙是否有开启安全性配置，例如 ARP 防护或流量过滤。</p>
<p>做完这些，如果还是存在外网访问问题那么依旧建议你联系售后工程师进行排查和解决~</p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/nas.htm"><i>#</i>NAS</a><a href="https://news.mydrivers.com/tag/qunhui.htm"><i>#</i>群晖</a></p>
<p class="url">
     
<span>责任编辑：随心</span>
</p>
        
</div>
            