
---
title: 'Golang 实现的远程桌面 Vnc 代理组件 Vprix-VncProxy 发布 v2.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9521'
author: 开源中国
comments: false
date: Thu, 30 Jun 2022 17:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9521'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:start"> 
 <h3 style="margin-left:0; margin-right:0">本次更新内容</h3> 
 <p>1.  重构代码结构，更优雅的作为依赖库被引入到其他项目中。</p> 
 <p>2. 完善了vnc文档，让有意向了解vnc协议的朋友能更方便的学习。</p> 
 <p>3. 修复了tight编码格式的bug。</p> 
 <h3 style="margin-left:0; margin-right:0">软件简介</h3> 
</div> 
<div style="text-align:start"> 
 <div> 
  <div> 
   <div style="text-align:left"> 
    <p style="margin-left:0; margin-right:0">VprixVncProxy 是 Golang 实现的 Vnc 远程桌面代理组件，完全解析 rfb 协议，支持远程桌面代理，rbs 文件录屏，rbs 文件回放，截图，录制视频。</p> 
    <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
     <li>全协议支持的 VncProxy。 
      <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
       <li>支持 Tcp 代理</li> 
       <li>支持 WebSocket 代理</li> 
      </ul> </li> 
     <li>支持远程桌面操作保存为<span> </span><strong>rbs</strong><span> </span>文件。</li> 
     <li>支持使用<span> </span><strong>rbs</strong><span> </span>文件作为重播服务，通过 vnc 客户端连接 player 服务，回放远程桌面的操作。</li> 
     <li> <p style="margin-left:0; margin-right:0">支持实时录制视频。</p> </li> 
     <li> <p style="margin-left:0; margin-right:0">支持通过<span> </span><strong>rbs</strong><span> </span>文件录制视频</p> </li> 
     <li> <p style="margin-left:0; margin-right:0">支持屏幕截图</p> </li> 
    </ul> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            