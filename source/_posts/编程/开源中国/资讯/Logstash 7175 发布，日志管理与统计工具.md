
---
title: 'Logstash 7.17.5 发布，日志管理与统计工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1504'
author: 开源中国
comments: false
date: Thu, 30 Jun 2022 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1504'
---

<div>   
<div class="content">
                                                                                            <p>Logstash 是一个应用程序日志、事件的传输、处理、管理和搜索的平台，可用于对应用程序日志进行收集管理，提供 Web 接口用于查询和统计。</p> 
<p>目前 Logstash 发布了 7.17.5 版本，带来如下变更：</p> 
<h3 style="margin-left:0px"><strong>已修复的问题</strong></h3> 
<ul> 
 <li>修复 Logstash 进程崩溃期间， Persistent Queue 可能损坏的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Flogstash%2Fpull%2F14147" target="_blank">#14147</a></li> 
 <li>将 PQ 可用磁盘空间不足的检查更改为警告，而不是错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Flogstash%2Fpull%2F14267" target="_blank">#14267</a></li> 
 <li>当使用不推荐的设置配置 Logstash 时， 修复 <code>logstash-keystore</code> util 中的异常 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Flogstash%2Fpull%2F14246" target="_blank">#14246</a> </li> 
</ul> 
<h3 style="margin-left:0px"><strong>依赖项的更新</strong></h3> 
<ul> 
 <li>捆绑的 JDK 11 已更新至 11.0.15+10 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Flogstash%2Fpull%2F14152" target="_blank">#14152</a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Flogstash%2F7.17%2Flogstash-7-17-5.html" target="_blank">https://www.elastic.co/guide/en/logstash/7.17/logstash-7-17-5.html</a></p>
                                        </div>
                                      
</div>
            