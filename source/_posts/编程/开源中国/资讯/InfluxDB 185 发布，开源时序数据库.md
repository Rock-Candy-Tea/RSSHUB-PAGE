
---
title: 'InfluxDB 1.8.5 发布，开源时序数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8517'
author: 开源中国
comments: false
date: Thu, 22 Apr 2021 23:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8517'
---

<div>   
<div class="content">
                                                                    
                                                        <p>InfluxDB 1.8.5 现已发布，具体更新内容如下：</p> 
<p><strong>Features</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F20917" target="_blank">＃20917</a>：feat(inspect)：添加 report-disk 以衡量磁盘使用情况</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F20118" target="_blank">＃20118</a>：feat：优化只包含一个分片的组中的分片查询</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F20910" target="_blank">＃20910</a>：feat：使元查询 respect QueryTimeout 值</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F20989" target="_blank">＃20989</a>：feat：influx_inspect 导出到标准输出</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21021" target="_blank">＃21021</a>：feat：记录 POST 请求的查询文本</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21053" target="_blank">＃21053</a>：fix：influx_inspect 的帮助文本</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F20101" target="_blank">＃20101</a>：fix(write)：成功写入后，错误地增加了写入错误的统计数据</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F20276" target="_blank">＃20276</a>：fix(error)：不支持的值：+Inf" 错误未得到妥善处理</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F20277" target="_blank">＃20277</a>：fix(query)：Group By 查询的偏移量超过了 DST 边界，可能会失败</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F20295" target="_blank">＃20295</a>：fix：cp.Mux.Serve() 在发生错误时默默关闭所有 net.Listener 实例</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F19832" target="_blank">＃19832</a>：fix(prometheus)：正则表达式处理应符合 PromQL</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F20432" target="_blank">＃20432</a>：fix(error)：SELECT INTO 不返回不支持的值的错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F20033" target="_blank">＃20033</a>：fix(tsm1)：备份时出现“snapshot in progress”的错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F20909" target="_blank">＃20909</a>：fix(tsm1)：访问逻辑删除统计信息时的数据争用</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F20912" target="_blank">＃20912</a>：fix(tsdb)：在添加新字段或度量时最小化锁争用</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F20914" target="_blank">＃20914</a>：fix：无限递归错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F20862" target="_blank">＃20862</a>）</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Freleases%2Ftag%2Fv1.8.5" target="_blank">https://github.com/influxdata/influxdb/releases/tag/v1.8.5</a></p>
                                        </div>
                                      
</div>
            