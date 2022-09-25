
---
title: 'smart-socket 1.5.21 发布，单机百万长连接背后的故事'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-776fbd52374ee1f5706ad3e2c1b0bbfe053.png'
author: 开源中国
comments: false
date: Sun, 25 Sep 2022 00:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-776fbd52374ee1f5706ad3e2c1b0bbfe053.png'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <div> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">smart-socket 是一款极简、易用、高性能的国产开源 AIO 通信框架，旨在帮助开发人员轻松打造企业级通信应用。</p> 
  <h2 style="margin-left:0; margin-right:0"><span>更新内容</span>🎉</h2> 
  <ol style="margin-left:0; margin-right:0"> 
   <li><span>支持低内存运行模式，实现低配内存服务器运行百万长连接。</span></li> 
   <li><span>增加对 DelimiterFrameDecoder 的入参校验。（感谢@乾坤摄 提交的PR ）</span></li> 
   <li><span>添加benchmark测试工具</span></li> 
  </ol> 
  <h2 style="margin-left:0; margin-right:0"><span>Maven坐标</span>🎈</h2> 
  <pre><dependency>
    <groupId>org.smartboot.socket</groupId>
    <artifactId>aio-core</artifactId>
    <version>1.5.21</version>
</dependency></pre> 
  <h2 style="margin-left:0; margin-right:0"><span>走进百万长连接背后的故事</span>📓</h2> 
  <p style="margin-left:0; margin-right:0"><span>smart-socket 自2017年开源以来，一直秉承着匠心精神，力求打造出极简、易用、高性能的国产开源通信框架。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>然而，在网上各类未经验证的信息误导下， 大众对于Java 始终存在一些偏见。认定只有 C、C++，以及新晋之秀 Golang 才适合支撑海量连接、高流量的通信服务 。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>事实上，用 Java 语言编写的 smart-socket 早已在性能排行榜上取得了不错的成绩（见下图）。并且，我们也终于在2022年9月23日成功验证了 smart-socket 的百万级长连接。</span></p> 
  <p><img height="962" src="https://oscimg.oschina.net/oscnet/up-776fbd52374ee1f5706ad3e2c1b0bbfe053.png" width="1500" referrerpolicy="no-referrer"></p> 
  <p style="margin-left:0; margin-right:0"><span>在过往的项目推广中，smart-socket 从未以“百万长连接”作为宣传噱头。因为在没有经过实际验证的情况下，无法说服自己在宣传文案中出现“百万级长连接”之类不负责的字眼。况且，百万长连接的是操作系统和硬件本身便具备的能力。能做到，不代表我们的通信框架多优秀；若做不到，才当反思一下我们的项目质量。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>而困扰我无法开展验证工作的主要原因，在于不具备硬件条件。我所用的开发电脑为 Mac Pro，先天不具备百万级长连接的测试条件（上限约26W）。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>并且长期以来陷入某种思维误区，以为这种级别的测试必须搭配多台测试机。或者至少是一台高配服务器，再创建至少20个以上的虚拟机或容器。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>尽管身处困境，但我却还产生了一个更疯狂的想法：</span><strong><span>能否用一台普通配置的服务器（4核8G）实现百万长连接。</span></strong></p> 
  <p style="margin-left:0; margin-right:0"><span>在将验证方案构思完成，并做好充分准备后，便开始在社群中寻求帮助。</span></p> 
  <p><img height="392" src="https://oscimg.oschina.net/oscnet/up-8e50def7029715671a63375502948858a27.png" width="1416" referrerpolicy="no-referrer"></p> 
  <p style="margin-left:0; margin-right:0"><span>很快便得到了响应和支持，在次特别感谢这位老朋友。</span></p> 
  <p><img height="912" src="https://oscimg.oschina.net/oscnet/up-2c02d37e99eb834ced4af2be4c31b70df07.png" width="1362" referrerpolicy="no-referrer"></p> 
  <p style="margin-left:0; margin-right:0"><span>最终，我们顺利的完成了百万级长连接的测试。</span></p> 
  <p><img height="580" src="https://oscimg.oschina.net/oscnet/up-ee0b3dd500e3dccab9e3d726247bb48d258.png" width="1370" referrerpolicy="no-referrer"></p> 
  <p style="margin-left:0; margin-right:0"><span>当 TCP 总连接数定格在101万的时候，服务端仅消耗内存 3.1G，每个客户端维持在 120~170MB 左右。（PS：内存开销还有进一步优化空间）</span></p> 
  <p><img height="1084" src="https://oscimg.oschina.net/oscnet/up-f09fc9da7f4651d923939801b8e10826dfd.png" width="1482" referrerpolicy="no-referrer"></p> 
 </div> 
</div> 
<h2>最后</h2> 
<p>开源不易，支持这款国产开源项目的朋友帮忙点点Star。想要体验的百万长连接的，也可通过项目仓库Readme.md入口获取实战教程。</p>
                                        </div>
                                      
</div>
            