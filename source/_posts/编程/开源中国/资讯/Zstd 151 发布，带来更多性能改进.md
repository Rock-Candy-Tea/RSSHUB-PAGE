
---
title: 'Zstd 1.5.1 发布，带来更多性能改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1222/073311_Lbzo_2720166.png'
author: 开源中国
comments: false
date: Wed, 22 Dec 2021 07:37:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1222/073311_Lbzo_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>Zstd 1.5.1 已发布，这是一个常规维护版本，更新内容除了小的改进外，在性能方面也带来了进一步的优化。</p> 
<ul> 
 <li><strong>提升 1-4 级的快速压缩 (fast compression) 速度</strong></li> 
 <li><strong>平衡 middle compression 的压缩级别</strong></li> 
</ul> 
<p><img src="https://static.oschina.net/uploads/space/2021/1222/073311_Lbzo_2720166.png" referrerpolicy="no-referrer"></p> 
<p><img src="https://static.oschina.net/uploads/space/2021/1222/073322_BRjc_2720166.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>改进霍夫曼代码，提升解码和编码速度</strong></li> 
</ul> 
<p>霍夫曼解码速度/编码速度的具体提升情况与场景紧密相关，对（解）压缩速度的总体影响取决于数据的可压缩性。</p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:max-content; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>Compiler</th> 
   <th>Scenario</th> 
   <th>v1.5.0 Speed</th> 
   <th>v1.5.1 Speed</th> 
   <th>Delta</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-style:solid; border-width:1px">gcc-11</td> 
   <td style="border-style:solid; border-width:1px">Literal compression - 128KB block</td> 
   <td style="border-style:solid; border-width:1px">748 MB/s</td> 
   <td style="border-style:solid; border-width:1px">927 MB/s</td> 
   <td style="border-style:solid; border-width:1px">+23.9%</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">clang-13</td> 
   <td style="border-style:solid; border-width:1px">Literal compression - 128KB block</td> 
   <td style="border-style:solid; border-width:1px">810 MB/s</td> 
   <td style="border-style:solid; border-width:1px">927 MB/s</td> 
   <td style="border-style:solid; border-width:1px">+14.4%</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">gcc-11</td> 
   <td style="border-style:solid; border-width:1px">Literal compression - 4KB block</td> 
   <td style="border-style:solid; border-width:1px">223 MB/s</td> 
   <td style="border-style:solid; border-width:1px">321 MB/s</td> 
   <td style="border-style:solid; border-width:1px">+44.0%</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">clang-13</td> 
   <td style="border-style:solid; border-width:1px">Literal compression - 4KB block</td> 
   <td style="border-style:solid; border-width:1px">224 MB/s</td> 
   <td style="border-style:solid; border-width:1px">310 MB/s</td> 
   <td style="border-style:solid; border-width:1px">+38.2%</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">gcc-11</td> 
   <td style="border-style:solid; border-width:1px">Literal decompression - 128KB block</td> 
   <td style="border-style:solid; border-width:1px">1164 MB/s</td> 
   <td style="border-style:solid; border-width:1px">1500 MB/s</td> 
   <td style="border-style:solid; border-width:1px">+28.8%</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">clang-13</td> 
   <td style="border-style:solid; border-width:1px">Literal decompression - 128KB block</td> 
   <td style="border-style:solid; border-width:1px">1006 MB/s</td> 
   <td style="border-style:solid; border-width:1px">1504 MB/s</td> 
   <td style="border-style:solid; border-width:1px">+49.5%</td> 
  </tr> 
 </tbody> 
</table> 
<ul> 
 <li style="text-align:start"><strong>优化二进制文件体积，提升构建速度</strong></li> 
</ul> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:max-content; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>Version</th> 
   <th>gcc-11 size</th> 
   <th>clang-13 size</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-style:solid; border-width:1px">v1.5.1</td> 
   <td style="border-style:solid; border-width:1px">1177 KB</td> 
   <td style="border-style:solid; border-width:1px">1167 KB</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">v1.5.0</td> 
   <td style="border-style:solid; border-width:1px">1338 KB</td> 
   <td style="border-style:solid; border-width:1px">1460 KB</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">v1.4.9</td> 
   <td style="border-style:solid; border-width:1px">1137 KB</td> 
   <td style="border-style:solid; border-width:1px">1151 KB</td> 
  </tr> 
 </tbody> 
</table> 
<p><span style="background-color:#ffffff; color:#333333">更多的细节和下载地址</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fzstd%2Freleases%2Ftag%2Fv1.5.1" target="_blank">查看发布公告</a><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            