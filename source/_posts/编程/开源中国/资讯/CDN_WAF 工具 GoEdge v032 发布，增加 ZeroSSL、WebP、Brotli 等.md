
---
title: 'CDN_WAF 工具 GoEdge v0.3.2 发布，增加 ZeroSSL、WebP、Brotli 等'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5936f99437ada1a20b76cac97ce5ac7e78c.png'
author: 开源中国
comments: false
date: Mon, 11 Oct 2021 00:11:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5936f99437ada1a20b76cac97ce5ac7e78c.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333">是一款可以帮你快速构建 CDN & WAF 平台的工具，支持HTTP、HTTPS、TCP、TLS、UDP、IPv6、WAF等特性。</span></p> 
<p><span style="background-color:#ffffff; color:#333333"><img alt height="352" src="https://oscimg.oschina.net/oscnet/up-5936f99437ada1a20b76cac97ce5ac7e78c.png" width="600" referrerpolicy="no-referrer"></span></p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start">v0.3.2 主要增加ZeroSSL、WebP、Brotli等支持，优化IP名单性能。</p> 
<h3 style="text-align:start">EdgeAdmin</h3> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">功能</p> 
  <ul> 
   <li>内容压缩支持brotli和deflate</li> 
   <li>支持WebP自动转换</li> 
   <li>支持ZeroSSL免费证书申请</li> 
   <li>缓存条件增加可缓存的最小内容尺寸配置</li> 
   <li>看板增加离线节点数字</li> 
   <li>TCP、TLS、UDP支持端口范围</li> 
   <li>WAF策略增加防御模式、观察模式和通过模式</li> 
   <li>在WAF规则产生错误时给予提示</li> 
   <li>服务支持自定义访客IP地址获取方式</li> 
   <li>添加源站时自动去除专属域名中的末尾斜杠</li> 
   <li>证书上传时可以选择输入文本内容</li> 
   <li>特殊页面可以直接使用HTML</li> 
   <li>增加新的界面风格theme4, theme5</li> 
   <li>页面底部增加GoEdge官网和文档链接</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<ul> 
 <li>Bug修复 
  <ul> 
   <li>修复修改HTTP Header不会自动更新节点配置的Bug</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeNode</h3> 
<ul> 
 <li>功能 
  <ul> 
   <li>大幅优化IP名单查询速度，极大降低了内存使用</li> 
   <li>Block动作增加默认时间60秒</li> 
   <li>节点启动时如果加载的是本地配置则在网络恢复后重新加载配置</li> 
   <li>缓存内容也支持压缩</li> 
   <li>不把499状态码加入状态码统计</li> 
   <li>开启缓存后覆盖源站的ETag和Last-Modified</li> 
   <li>根据系统内存自动调节ttlcache的最大条目</li> 
   <li>WAF动作block和record_ip同时存在时，优先执行record_ip</li> 
   <li>服务支持自定义访客IP地址获取方式/对X-Real-IP等Header值进行有效性验证</li> 
   <li>缓存预热判断请求来源的时候增加IPv6回路地址判断</li> 
   <li>把tcp/udp的连接数记为访问量，增加tcp域名排名记录（需要SNI连接）</li> 
  </ul> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292e">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292e">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p>
                                        </div>
                                      
</div>
            