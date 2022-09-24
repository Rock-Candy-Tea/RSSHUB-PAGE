
---
title: 'ATX 3.0迷思'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220924/s_c634eb2e934a4d17a556b02a978f2e91.jpg'
author: 快科技（原驱动之家）
comments: false
date: Sat, 24 Sep 2022 16:57:11 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220924/s_c634eb2e934a4d17a556b02a978f2e91.jpg'
---

<div>   
<p>近来有网红主播声称，4090用户若沿用现有ATX 2.0电源，最坏的情况是把房子点着。想求稳就要早做打算，抓紧时间抢购ATX 3.0电源，<strike>所以EVGA才转行卖电源</strike>。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20220924/c634eb2e934a4d17a556b02a978f2e91.jpg" target="_blank"><img alt="ATX 3.0迷思" h="337" src="https://img1.mydrivers.com/img/20220924/s_c634eb2e934a4d17a556b02a978f2e91.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>他们的主张是，ATX 3.0电源带有原生12VHPWR连接器，支持600瓦功率输送，不仅能满足额定450瓦的4090，还能战未来（比如4090Ti）。</p>
<p>原生12VHPWR当然好，根据Intel的ATX 3.0规范可知，除12个电源触点外，还额外设计4个信号触点供显卡与电源通信，告知对方需要多少功率。即便玩家购入一块4090之类的电老虎，也不至于因电源功率不足无法启动PC。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20220924/2fe23c2837b347489136c0818dc6869d.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="ATX 3.0迷思" h="227" src="https://img1.mydrivers.com/img/20220924/s_2fe23c2837b347489136c0818dc6869d.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>根据上表可知，若显卡未监听到电源信号（Sense0与Sense1开路），则以最低档功率运行，确保用户能亮机并进入系统，然后显卡驱动程序会告诉用户GPU正处于低功率运行状态。</p>
<p>现在的问题是，旧电源显然不支持这套握手信号，即便<strong>每一块4系显卡都附送了12VHPWR转接线</strong>，也只是负责将旧电源的8Pin PCIE转接成显卡端的12VHPWR——按坊间流传已久的说法，单路8Pin可提供150瓦功率，四根8Pin正好达成12VHPWR的上限，即4x150=600瓦。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20220924/cb5e378b742d43f5a78da4ca6cd1351b.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="ATX 3.0迷思" h="353" src="https://img1.mydrivers.com/img/20220924/s_cb5e378b742d43f5a78da4ca6cd1351b.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>为解决握手信号问题，12VHPWR转接线会将信号0与信号1接地，受欺骗的显卡处于全情投入状态，不会顾及电源是否扛得住。有主播声称，由于无法做到多路均流，其中一路8Pin必然会超过其150瓦功率上限，最危险的情况便是火灾。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220924/06d83d38fd844c168079e9b874ee5177.jpg" target="_blank"><img alt="ATX 3.0迷思" h="316" src="https://img1.mydrivers.com/img/20220924/s_06d83d38fd844c168079e9b874ee5177.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>有识之士指出，所谓单根8Pin线最多150瓦是都市传言，合格的12VHPWR转接线使用16AWG线材（截面积1.3平方毫米），端子可承受至少300瓦功率——按照厂家的说法，使用18AWG线材的8Pin可提供306瓦功率，16AWG线材可到468瓦。</p>
<p>如果使用四路8Pin转12VHPWR且线材合格，连接端子没有氧化现象（接触电阻足够小），而你的老电源是下血本购入的，就不必去赞助EVGA的新业务（其实EVGA现在还无法提供ATX 3.0电源）。</p>
<p>唯一的问题是插拔次数，一份由索泰提供的宣传单指出，附赠的12VHPWR转接线最好不要超过30次插拔，否则就要考虑更换全新转接线。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220924/77895f4913704e7d96487c5f5e140ad4.jpg" target="_blank"><img alt="ATX 3.0迷思" h="414" src="https://img1.mydrivers.com/img/20220924/s_77895f4913704e7d96487c5f5e140ad4.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220924/edca3794e7bf4569af6c8ed2aa088e71.jpg" target="_blank"><img alt="ATX 3.0迷思" h="377" src="https://img1.mydrivers.com/img/20220924/s_edca3794e7bf4569af6c8ed2aa088e71.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

            
 <div style="overflow: hidden;font-size:14px;padding-top:30px;border-bottom:1px solid #eee;">
           <p class="zhuanzai">【本文结束】如需转载请务必注明出处：快科技</p>  
          <p class="url"><span style="color:#666">责任编辑：Zhengogo</span></p>
        </div>
     
        
</div>
            