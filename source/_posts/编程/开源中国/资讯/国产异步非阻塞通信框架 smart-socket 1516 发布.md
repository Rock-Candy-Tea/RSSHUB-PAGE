
---
title: '国产异步非阻塞通信框架 smart-socket 1.5.16 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5204'
author: 开源中国
comments: false
date: Tue, 22 Mar 2022 11:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5204'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">smart-socket 是一款极简、易用、高性能的国产开源 AIO 通信框架，旨在帮助开发人员轻松打造企业级通信应用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>此版本主要变化</strong></p> 
<div> 
 <ul style="margin-left:0; margin-right:0"> 
  <li><span>修复并发场景下的内存异常问题。</span></li> 
  <li><span>修复特定并发场景下的 TCP 连接资源没有及时释放问题。</span></li> 
  <li><span>优化内存池的内存申请效率。</span></li> 
  <li><span>优化 AioQuickClient#shutdown0 ，支持网络连接断开后复用 client 对象进行TCP 重连。</span></li> 
  <li><span>适当缩小 WriteBuffer 的锁粒度。</span></li> 
  <li><span>其他一些细节优化。</span></li> 
 </ul> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>maven坐标</strong></p> 
<pre style="margin-left:0; margin-right:0; text-align:justify"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>org.smartboot.socket<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>aio-core<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.5.16<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">想要进一步了解 smart-socket，请移步以下链接不迷路：</p> 
<ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>文档</span></p> <p style="margin-left:0; margin-right:0"><a href="https://smartboot.gitee.io/book/smart-socket/">https://smartboot.gitee.io/book/smart-socket/</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Gitee仓库</span></p> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/smartboot/smart-socket">https://gitee.com/smartboot/smart-socket</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Github仓库</span></p> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsmartboot%2Fsmart-socket" target="_blank">https://github.com/smartboot/smart-socket</a></p> </li> 
</ul>
                                        </div>
                                      
</div>
            