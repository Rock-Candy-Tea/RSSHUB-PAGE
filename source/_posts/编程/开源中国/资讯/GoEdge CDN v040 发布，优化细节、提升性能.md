
---
title: 'GoEdge CDN v0.4.0 发布，优化细节、提升性能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7c41022488d86b883ffb7fdfdfa1c977fd9.png'
author: 开源中国
comments: false
date: Mon, 17 Jan 2022 09:30:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7c41022488d86b883ffb7fdfdfa1c977fd9.png'
---

<div>   
<div class="content">
                                                                                            <p><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333">是一款可以帮你快速构建 CDN & WAF 平台的工具，支持HTTP、HTTPS、TCP、TLS、UDP、PROXY Protocol、IPv6、WAF等特性。</span></p> 
<p><img alt height="352" src="https://oscimg.oschina.net/oscnet/up-7c41022488d86b883ffb7fdfdfa1c977fd9.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start">v0.4.0 细节优化，提升性能。</p> 
<h3 style="text-align:start">EdgeAdmin</h3> 
<ul> 
 <li>功能增强： 
  <ul> 
   <li>节点运行日志增加集群、节点、标签筛选</li> 
   <li>服务 
    <ul> 
     <li>创建服务时默认选中统计</li> 
     <li>改进服务访问日志、设置页在手机下的显示</li> 
     <li>可以使用集群、节点对访问日志进行筛选</li> 
    </ul> </li> 
   <li>集群 
    <ul> 
     <li>可以设置是否自动在firewalld中开放端口，默认为开启状态</li> 
    </ul> </li> 
   <li>IP名单 
    <ul> 
     <li>增加未读数字气泡显示，有未读的情况下可以根据未读筛选</li> 
    </ul> </li> 
   <li>WAF 
    <ul> 
     <li>WAF策略增加是否自动使用本地防火墙设置，开启后，可以自动使用本地防火墙（目前是firewalld）进行拦截防御</li> 
     <li>WAF规则增加描述信息</li> 
     <li>WAF策略增加自动SYNC Flood防护选项</li> 
     <li>可以使用集群搜索WAF策略</li> 
     <li>可以在IP名单、访问日志中跳到对应的WAF规则集</li> 
     <li>CAPTCHA增加最多失败次数和失败拦截时长</li> 
     <li>WAF动作中各个超时/有效秒数最大值从10位改成9位</li> 
     <li>WAF模板中特殊目录增加.env</li> 
     <li>WAF模板–爬虫工具增加白名单</li> 
     <li>WAF模板–爬虫工具默认不封禁搜索引擎</li> 
    </ul> </li> 
   <li>缓存 
    <ul> 
     <li>可以使用集群搜索缓存策略</li> 
     <li>增加Open File Cache选项，可以缓存文件句柄</li> 
    </ul> </li> 
   <li>反向代理 
    <ul> 
     <li>源站设置支持客户端证书</li> 
    </ul> </li> 
  </ul> </li> 
 <li>Bug修复 
  <ul> 
   <li>修复缓存策略不能直接回车保存的Bug</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<ul> 
 <li>功能增强： 
  <ul> 
   <li>缩短节点运行日志清理时间</li> 
   <li>缩短节点统计数据清理时间</li> 
   <li>WAF自动加入的IP不再生成更新任务</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeNode</h3> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">功能增强：</p> 
  <ul> 
   <li>如果没有设置节点CPU线程数，则默认为4倍的CPU线程数</li> 
   <li>优化User-Agent解析性能</li> 
   <li>增加地区（$&#123;geo.NAME&#125;）、ISP（$&#123;isp.NAME&#125;）、浏览器（$&#123;browser.NAME&#125;）、产品（$&#123;product.NAME&#125;）等变量</li> 
   <li>统计数据上传时如果遇到invalid utf-8，则自动过滤非法字符</li> 
   <li>提升WAF正则表达式性能</li> 
   <li>增加<code>edge-node [ip.drop|ip.reject|ip.remove] IP</code>命令</li> 
   <li>优化验证码在窄屏上的展示</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">Bug修复：</p> 
  <ul> 
   <li>删除缓存数据库版本切换时的错误提示</li> 
  </ul> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292f">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292f">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p>
                                        </div>
                                      
</div>
            