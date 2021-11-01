
---
title: 'GoEdge CDN v0.3.3 发布，支持 Arm64、Gif 转 WebP、PROXY 协议'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-89e72fcb331226ca88db299c634f2c83b03.png'
author: 开源中国
comments: false
date: Mon, 01 Nov 2021 01:07:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-89e72fcb331226ca88db299c634f2c83b03.png'
---

<div>   
<div class="content">
                                                                                            <p><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333">是一款可以帮你快速构建 CDN & WAF 平台的工具，支持HTTP、HTTPS、TCP、TLS、UDP、IPv6、WAF等特性。</span></p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start"><img alt height="352" src="https://oscimg.oschina.net/oscnet/up-89e72fcb331226ca88db299c634f2c83b03.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start">v0.3.3 支持ARM64、Gif转WebP、PROXY Protocol协议、优化WAF。</p> 
<h3 style="text-align:start">EdgeAdmin</h3> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">功能</p> 
  <ul> 
   <li>WebP压缩支持.ico和.gif文件 <p><img height="322" src="https://oscimg.oschina.net/oscnet/up-14fb1257f764857f83f6a8f1010263925b9.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>各个网络协议支持使用PROXY Protocol访问源站，可以在”反向代理”–“更多设置”–“更多选项”–“PROXY Protocol”中启用 <p><img height="153" src="https://oscimg.oschina.net/oscnet/up-5ae93d5891ae3aa1af5bfe526d88cba6cdf.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>可以在集群中指定节点时区 <p><img height="153" src="https://oscimg.oschina.net/oscnet/up-0e34c8275e90dd67bce47222af0ae7514ac.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>选择线路的时候关键词可以搜索域名 <p><img height="134" src="https://oscimg.oschina.net/oscnet/up-7472eed956417142fd82e0499e462ee0817.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>运行日志显示未读的错误日志数量，可以查看未读的错误日志 <p><img height="224" src="https://oscimg.oschina.net/oscnet/up-523a00f83a7a509397dc41c25e5632bbb08.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>支持任意域名通过CNAME访问服务（开启选项后），可以重新生成服务CNAME <p><img height="177" src="https://oscimg.oschina.net/oscnet/up-b4d811f20195027454c683a1efaa126af92.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>增加使用Purge方法清除某个URL缓存的功能 <p><img height="133" src="https://oscimg.oschina.net/oscnet/up-264ba14c57e5c08a624a2c8be192bdc57f0.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>默认的内容压缩算法从gzip改为brotli <p><img height="61" src="https://oscimg.oschina.net/oscnet/up-270bd2e9d6126b69898e54a73d47ceea0d2.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>内容压缩支持对已压缩内容重新压缩 <p><img height="57" src="https://oscimg.oschina.net/oscnet/up-9a939c945779a8763a33fe1dc1cd575c429.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>WAF阻止动作增加封锁范围选项 <p><img height="253" src="https://oscimg.oschina.net/oscnet/up-15f917ada8de65ab837c4d45dddb9f69bcd.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>WAF增加防盗链规则参数 <p><img height="419" src="https://oscimg.oschina.net/oscnet/up-b2da90cab97162600e54f7a21188a8a26c8.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>WAF模板增加空Agent和随机URL规则集 <p><img height="59" src="https://oscimg.oschina.net/oscnet/up-18a8bfc11e39ca73c2f8c419259d80a2887.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>健康检查支持UserAgent和是否基础请求设置 <p><img height="122" src="https://oscimg.oschina.net/oscnet/up-babd62eabb0a65e1bfda7b3aa399f3708a8.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>可以在IP名单中搜索IP <p><img height="414" src="https://oscimg.oschina.net/oscnet/up-6df0120abae701d4c6943f317586671b71d.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>IP名单列表可以搜索关键词 <p><img height="305" src="https://oscimg.oschina.net/oscnet/up-860c1c614f4d9ff9730aeb244d75f222bbe.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>创建网站服务时增加缓存、WAF、从上级代理中读取IP等选项 <p><img height="127" src="https://oscimg.oschina.net/oscnet/up-c8689cdbff609eb0eed172f1e9208f81ea6.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>WAF模板中有新的规则时，可以在界面上收到提醒并点击加入 <p><img height="110" src="https://oscimg.oschina.net/oscnet/up-ca00544345f6ab5d135267d8b85be5da08a.png" width="600" referrerpolicy="no-referrer"></p> </li> 
   <li>WAF增加显示网页动作 <p><img height="304" src="https://oscimg.oschina.net/oscnet/up-e570733de3eeed134bf957536867142e9a8.png" width="600" referrerpolicy="no-referrer"></p> </li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">Bug修复</p> 
  <ul> 
   <li>修复编译脚本无法编译Arm64的Bug，官方提供的下载包将能直接在Arm64平台上运行</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">功能：</p> 
  <ul> 
   <li>将HTTP Header中Edge-改成X-Edge-</li> 
   <li>域名小时统计只保留7天</li> 
   <li>提供重新生成服务CNAME API</li> 
   <li>增加为WAF分组添加规则集的API</li> 
   <li>增加在IP名单中使用ipFrom和ipTo查找IP的API</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">Bug修复</p> 
  <ul> 
   <li>修复同属多集群下的节点无法删除线路的Bug</li> 
   <li>修复华为云DNS TXT记录值不加引号无法添加的问题</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeNode</h3> 
<ul> 
 <li>功能 
  <ul> 
   <li>WAF动作record_ip返回403</li> 
   <li>优化关闭连接方法</li> 
   <li>WebP支持源站gzip、deflate、br等压缩后的图片内容</li> 
   <li>优化节点日志记录，可以记录和上报panic错误</li> 
   <li>增大默认的源站的并发连接数</li> 
   <li>内容压缩支持对已压缩内容重新压缩</li> 
  </ul> </li> 
 <li>Bug修复 
  <ul> 
   <li>WebP无法解析原图时直接返回原图数据</li> 
   <li>修复特殊页面无法缓存的Bug</li> 
   <li>修复校验ACME证书时受自动跳转等设置的影响的问题</li> 
  </ul> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292f">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292f">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p>
                                        </div>
                                      
</div>
            