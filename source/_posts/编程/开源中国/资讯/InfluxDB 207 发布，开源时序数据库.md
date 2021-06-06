
---
title: 'InfluxDB 2.0.7 发布，开源时序数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9039'
author: 开源中国
comments: false
date: Sun, 06 Jun 2021 07:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9039'
---

<div>   
<div class="content">
                                                                    
                                                        <p>InfluxDB 2.0.7 现已发布，具体更新内容如下：</p> 
<p><strong>Features</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21519" target="_blank">21519</a>：将 Flux 升级到 v0.117.0</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21519" target="_blank">21519</a>：优化Flux 聚合窗口内的<code>table.fill()</code>执行。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21564" target="_blank">21564</a>：将 UI 升级到<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Fui%2Freleases%2Ftag%2FOSS-v2.0.7" target="_blank">v2.0.7</a></li> 
</ul> 
<p><strong>Bug Fixes</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21349" target="_blank">21349</a>：修复部分压缩数据的查询范围计算中的 off-by-one 错误。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21350" target="_blank">21350</a>：弃用不受支持的<code>PostSetupUser</code>API。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21376" target="_blank">21376</a>：添加限制到<code>/api/v2/delete</code>端点的开始和停止时间并带有错误消息。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21379" target="_blank">21379</a>：将 logging 添加到 NATS 流服务器以帮助调试启动失败。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21477" target="_blank">21479</a>：在<code>influx restore</code>中接受<code>--input</code>而不是位置参数。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21477" target="_blank">21479</a>：当<code>influx restore</code>无法找到备份清单时 print error 而不是 panicking。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21485" target="_blank">21485</a>：将空分片目录的最后修改时间设置为目录的 mod 时间而不是 Unix 纪元。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21499" target="_blank">21499</a>：删除对 istio 的错误依赖。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21501" target="_blank">21501</a>：当组织的成员超过 10 人时，不要在<code>influx org members list</code>中出现死锁。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21524" target="_blank">21524</a>：对于<code>ttf</code>，<code>woff</code>以及<code>eot</code>，用 slug 代替遥测文件名。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21549" target="_blank">21549</a>：在 Windows 上运行<code>influxd upgrade</code>时，允许启用<code>--upgrade-log</code>的绝对路径。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21548" target="_blank">21548</a>：使 InfluxQL 元查询 respect 查询超时。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Freleases%2Ftag%2Fv2.0.7" target="_blank">https://github.com/influxdata/influxdb/releases/tag/v2.0.7</a></p>
                                        </div>
                                      
</div>
            