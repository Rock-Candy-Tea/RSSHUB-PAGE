
---
title: 'fastrx v3 版本发布——精简版极速 rxjs 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6437'
author: 开源中国
comments: false
date: Wed, 15 Sep 2021 10:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6437'
---

<div>   
<div class="content">
                                                                                            <p>fastrx是一款api和rxjs十分近似的js库，拥有极为精简的实现，并提供极速的性能。与官方的RxJS相比有部分功能删减（不常用）。</p> 
<p>特性：同时支持链式编程方式和管道编程方式</p> 
<p>性能方面：</p> 
<div> 
 <table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,system-ui,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:max-content; word-spacing:0px"> 
  <tbody> 
   <tr> 
    <td style="border-style:solid; border-width:1px">fastrx</td> 
    <td style="border-style:solid; border-width:1px">22.56 op/s ± 1.77%</td> 
    <td style="border-style:solid; border-width:1px">(57 samples)</td> 
   </tr> 
   <tr> 
    <td style="border-style:solid; border-width:1px">cb-basics</td> 
    <td style="border-style:solid; border-width:1px">9.56 op/s ± 1.73%</td> 
    <td style="border-style:solid; border-width:1px">(49 samples)</td> 
   </tr> 
   <tr> 
    <td style="border-style:solid; border-width:1px">xstream</td> 
    <td style="border-style:solid; border-width:1px">5.37 op/s ± 0.68%</td> 
    <td style="border-style:solid; border-width:1px">(30 samples)</td> 
   </tr> 
   <tr> 
    <td style="border-style:solid; border-width:1px">most</td> 
    <td style="border-style:solid; border-width:1px">17.32 op/s ± 1.93%</td> 
    <td style="border-style:solid; border-width:1px">(82 samples)</td> 
   </tr> 
   <tr> 
    <td style="border-style:solid; border-width:1px">rx 6</td> 
    <td style="border-style:solid; border-width:1px">6.28 op/s ± 3.10%</td> 
    <td style="border-style:solid; border-width:1px">(35 samples)</td> 
   </tr> 
  </tbody> 
 </table> 
</div> 
<p>v3版本更新内容： </p> 
<p>采用TypeScript重写，并优化部分逻辑、进一步精简代码（通过类继承实现）</p> 
<p>支持Tree-shaking，（仅在使用pipe编程方式时）</p> 
<p>使用npm i fastrx@next 安装</p>
                                        </div>
                                      
</div>
            