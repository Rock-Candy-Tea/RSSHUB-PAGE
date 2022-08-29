
---
title: 'Win11 SMB压缩获显著优化：大幅加快网络文件传输速度'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220829/s_ed6aad8221ce49aaa1c030a3dbcbec88.jpg'
author: 快科技（原驱动之家）
comments: false
date: Mon, 29 Aug 2022 18:18:15 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220829/s_ed6aad8221ce49aaa1c030a3dbcbec88.jpg'
---

<div>   
<p>近日，微软为Win11推送了KB5016691可选更新，<span style="color:#ff0000;"><strong>有用户发现，在此次更新中，微软对SMB（Server Message Block）压缩技术进行了优化改进，效果明显。</strong></span></p>
<p>据悉，SMB压缩允许管理员、用户或应用在传输文件时，将文件转为压缩形式发送，以小幅增加CPU占用率为代价，消耗更少的带宽，并减少传输时间，</p>
<p>但在很长一段时间里，<strong>微软的SMB压缩逻辑都非常奇怪，它会尝试先压缩文件的前500MiB（1MiB 为 1024KiB），如果可压缩的内容在100MiB以上，才会继续压缩并发送。</strong></p>
<p>而如果文件小于500MiB，或可压缩内容不到100MiB，那么即便文件压缩后的效果很好，或是体积很大，也不会进行任何压缩。</p>
<p>在更新后，这一限制终于被接触，<strong>SMB将压缩尽可能多的文件，这大幅提升了网络文件的传输速度。</strong></p>
<p>当然，新的逻辑也并不是没有缺点，它会无差别的压缩体积不大，且没有什么必要压缩的文件，对CPU造成额外负担。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220829/ed6aad8221ce49aaa1c030a3dbcbec88.jpg" target="_blank"><img alt="Win11 SMB压缩获显著优化：大幅加快网络文件传输速度" h="400" src="https://img1.mydrivers.com/img/20220829/s_ed6aad8221ce49aaa1c030a3dbcbec88.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

            
 <div style="overflow: hidden;font-size:14px;padding-top:30px;border-bottom:1px solid #eee;">
           <p class="zhuanzai">【本文结束】如需转载请务必注明出处：快科技</p>  
          <p class="url"><span style="color:#666">责任编辑：乃河</span></p>
        </div>
     
        
</div>
            