
---
title: '.NET Framework 2022 年 1 月累积更新预览已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4733'
author: 开源中国
comments: false
date: Mon, 31 Jan 2022 08:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4733'
---

<div>   
<div class="content">
                                                                                            <p>.NET Framework 2022 年 1 月累积更新预览已发布，.NET Framework 在 1 月带来以下改动：</p> 
<h3>质量和可靠性</h3> 
<p><strong>CLR（公共语言运行时）</strong></p> 
<ul> 
 <li>解决了在发生 GC 时可能出现的罕见崩溃和挂起，另一个线程位于用于从非共享通用上下文调用共享通用代码的特殊路径的中间。</li> 
</ul> 
<p><strong>WPF（Windows Presentation Foundation）</strong></p> 
<ul> 
 <li>解决了当下面这两个条件都存在时，滚动列表控件的挂起问题： 
  <ul> 
   <li>UseLayoutRounding 已启用</li> 
   <li>项目边距不是舍入量的倍数。（实际是 DPI 缩放的函数）</li> 
  </ul> </li> 
 <li>解决了将项目或组添加到 ItemsControl 时，显示的集合可能发生的 “高度必须为非负数” 异常。</li> 
 <li>解决了共享的 ContextMenu 在无法显示一次后停止显示的问题，因为它的所有者已从可视化树中删除。</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fnet-framework-january-2022-cumulative-update-preview%2F" target="_blank">https://devblogs.microsoft.com/dotnet/net-framework-january-2022-cumulative-update-preview/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            