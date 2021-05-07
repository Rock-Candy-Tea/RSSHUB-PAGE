
---
title: 'Intel DG2独立显卡电路图泄露：PCIe 4.0 x12什么鬼？'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0507/5da749efe2162d8.jpg'
author: cnBeta
comments: false
date: Fri, 07 May 2021 11:03:48 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0507/5da749efe2162d8.jpg'
---

<div>   
Intel DG1正式回到了独立显卡的世界，但毕竟只是Xe LP低功耗架构，规格孱弱，跟核显没啥太大区别，掀不起什么波澜。更令人期待的还是Intel DG2，Xe HPG高性能架构，传闻甚至有希望和RTX 3070 Ti一较高下(保留意见)。<br>
<p>Igor's Lab今天泄露了Intel DG2独立显卡的系统结构图、板卡设计图，亮点多多。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0507/5da749efe2162d8.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/0507/5da749efe2162d8.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/0507/5da749efe2162d8.jpg" referrerpolicy="no-referrer"></a></p><p>这张移动平台的系统结构图据说有一段时间了，不能保证完全准确，确实也透露着一丝诡异，比如说<strong>DG2显卡和Tiger Lake-H处理器之间的通道，居然是PCIe 4.0 x12。</strong></p><p>正常的显卡通道都是x16，或者减半到x8，甚至是x4，但是从未见过x12这样不高不低的，当然如此设置理论上是完全没问题的。</p><p>只是不知道是因为Intel移动平台PCIe 4.0通道数量限制，还是一个纯粹的笔误？</p><p>另外，<strong>影音输出支持DisplayPort 2.0、HDMI 2.0</strong>——如果真是这样，<strong>它将是史上第一个DisplayPort 2.0 GPU，但却不支持同样最新的HDMI 2.1，很是奇怪。</strong></p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0507/0389ebcd5f0770c.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/0507/0389ebcd5f0770c.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/0507/0389ebcd5f0770c.jpg" referrerpolicy="no-referrer"></a></p><p>这是板卡电路设计图，<strong>左侧中间正方形是DG2 GPU(BGA1379封装)，右侧长方形是Tiger Lake-H CPU</strong>，上方六个小长方形是内存/显存，从布局看<strong>右侧四颗应该是DDR4/LPDDR4X内存，左侧两颗则是GDDR6显存。</strong></p><p>这颗DG2 GPU是最低端的版本，只有128个执行单元，搭配64-bit 4GB GDDR6显存，两颗2GB正好。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0507/73843dbfe381f81.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/0507/73843dbfe381f81.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/0507/73843dbfe381f81.jpg" referrerpolicy="no-referrer"></a></p><p>这是<strong>BGA1379封装的针脚图</strong>，但没有任何注释，看不出什么来。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0507/05b8f9bc12cea12.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/0507/05b8f9bc12cea12.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/0507/05b8f9bc12cea12.jpg" referrerpolicy="no-referrer"></a></p><p>之前也见过一次DG2 GPU的电路图，不过是更高端的384单元版本(BGA2660封装)，核心尺寸22.3×8.5毫米(这次的没有尺寸数据)，搭配六颗显存，总共192-bit 12GB。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0507/5d99699636079fa.png"><img data-original="https://static.cnbetacdn.com/article/2021/0507/5d99699636079fa.png" src="https://static.cnbetacdn.com/thumb/article/2021/0507/5d99699636079fa.png" referrerpolicy="no-referrer"></a></p><p>Intel DG2显卡一共五个型号，低端的128、196单元都是BGA1379封装，64-bit 4GB显存，高端的256、384、512单元则是BGA2660封装，分别对应128192/256--bit显存，芯片功耗100W，算上显存应该在125W左右，桌面卡最高可能突破200W。</p><p><strong>Intel DG2同时面向笔记本和桌面，但以前者为主，128/196单元版本10月底到11月中旬量产，256/384/512单元版本12月中旬量产，桌面卡得明年了。</strong></p><p>这个时间节点下，原本计划搭档Tiger Lake-H系列登场是不可能了，<strong>只能配合Alder Lake 12代酷睿平台</strong>，后者也新设计了Alder Lake-P版本，CPU和芯片组整合封装在一颗芯片内。</p><p><strong>Intel已经向<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://asus.jd.com/" target="_blank">华硕</a>、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">微星</a>等大厂介绍了DG2的相关情况，但目前还只是PPT</strong>，慢慢等吧。</p>   
</div>
            