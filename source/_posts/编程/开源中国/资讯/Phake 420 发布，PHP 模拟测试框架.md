
---
title: 'Phake 4.2.0 发布，PHP 模拟测试框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8914'
author: 开源中国
comments: false
date: Tue, 14 Dec 2021 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8914'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="margin-left:.6em; margin-right:0; text-align:start">新功能</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fphake%2Fphake%2Fissues%2F304" target="_blank">#304</a><span> </span>- 增加对 PHP 8.1 初始化器中新功能的支持 
  <ul style="margin-left:0; margin-right:0"> 
   <li>PHP 8.1 在初始化器中引入了新功能，Phake 4.2 现在可以使用此功能创建对象的模拟。</li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fphake%2Fphake%2Fpull%2F303" target="_blank">#303</a><span> </span>- 增加对 PHP 8.1 交集类型和<span> </span><code>never</code><span> </span>返回类型的支持 
  <ul style="margin-left:0; margin-right:0"> 
   <li>PHP 8.1 引入了交集类型和 never 返回类型，Phake 4.2 支持这些新类型。当一个模拟的方法返回的<span> </span><code>never</code><span> </span>被调用时，Phake 默认会抛出一个<span> </span><code>Phake\\Exception\\NeverReturnMethodCalledException</code><span> </span>异常。调用<span> </span><code>Phake::when($mock)->thenReturn($x)</code><span> </span>将对这个方法的结果没有影响。</li> 
  </ul> </li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">变化</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fphake%2Fphake%2Fissues%2F301" target="_blank">#301</a><span> </span>- 在 PHP 8.1+ 的模拟内部方法上增加<span> </span><code>#[\\ReturnTypeWillChange]</code>。 
  <ul style="margin-left:0; margin-right:0"> 
   <li>所有在 PHP 8.1+ 下的内部模拟方法都将有<span> </span><code>#[\\ReturnTypeWillChange]</code><span> </span>属性，以避免任何弃用警告。</li> 
  </ul> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fphake%2Fphake%2Freleases%2Ftag%2Fv4.2.0" target="_blank">https://github.com/phake/phake/releases/tag/v4.2.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            