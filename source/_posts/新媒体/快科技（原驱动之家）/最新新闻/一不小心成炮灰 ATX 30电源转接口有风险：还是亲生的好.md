
---
title: '一不小心成炮灰 ATX 3.0电源转接口有风险：还是亲生的好'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220911/d45324d7-b44d-4cae-b690-54c4c546dc86.png'
author: 快科技（原驱动之家）
comments: false
date: Sun, 11 Sep 2022 22:59:08 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220911/d45324d7-b44d-4cae-b690-54c4c546dc86.png'
---

<div>   
<p>在ATX 2.3版电源规范问世19年后，今年Intel终于联合多家厂商制定了ATX 3.0电源，其一大变化就是带来了适应PCIe 5.0的显卡供电设计，功耗可达600W。</p>
<p>600W功耗还只是一部分，ATX 3.0电源需要在短时间内应付2倍的过载，因此瞬时功耗可达1800W，这对电源的供电设计要求很高，因此ATX 3.0中设计了新的12VHPWR 16针接口。</p>
<p>然而现实中还没有PCIe 5.0供电要求的显卡上市，主板及电源也没有准备好，NVIDIA上半年推出的RTX 3090 Ti是首个支持新规范的显卡，<strong>但它实际上是附赠了3个8pin电源转接口，并不是原生支持的。</strong></p>
<p>现在的问题来了，通过8pin接口转接支持ATX 3.0会不会有问题？这事还真值得说说，<span style="color:#ff0000;"><strong>PCI-SIG组织已经发出警告，支持了2路8pin或者3路8pin转接口可能带来的风险。</strong></span></p>
<p>根据测试，在2个8pin转接口时，供电负载可以均分，但400W及600W功耗下已经超标2倍了。</p>
<p>如果是3个8pin接口转接，负载就不容易均衡了，有1个接口负载能到300W，另外的2个接口则低于150W。</p>
<p>这样的结果会有什么危害？简单来说，这样转接出来的接口很难控制在规范内，<strong>要知道电源线质量本来就有不同，超过负载很容易过热甚至烧毁，</strong>这种转接口方案显然是不如12VHPWR 16针接口原生设计的好。</p>
<p>这也是ATX 3.0新规范全面普及前的阵痛，彻底解决这个问题需要电源、显卡、主板及CPU厂商全面支持新接口新规范。</p>
<p style="text-align: center"><img alt="一不小心成炮灰 ATX 3.0电源转接口有风险：还是亲生的好" h="596" src="https://img1.mydrivers.com/img/20220911/d45324d7-b44d-4cae-b690-54c4c546dc86.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>

            
 <div style="overflow: hidden;font-size:14px;padding-top:30px;border-bottom:1px solid #eee;">
           <p class="zhuanzai">【本文结束】如需转载请务必注明出处：快科技</p>  
          <p class="url"><span style="color:#666">责任编辑：宪瑞</span></p>
        </div>
     
        
</div>
            