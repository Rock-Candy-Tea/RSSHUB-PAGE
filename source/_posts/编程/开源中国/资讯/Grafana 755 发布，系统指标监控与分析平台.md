
---
title: 'Grafana 7.5.5 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9635'
author: 开源中国
comments: false
date: Fri, 30 Apr 2021 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9635'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Grafana 7.5.5 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</p> 
<p>具体更新内容如下：</p> 
<p><strong>Features and enhancements</strong></p> 
<ul> 
 <li><strong>Explore</strong>：当提供的 source 不存在时，在 Explore 中加载 default data source。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F32992" target="_blank">＃32992</a></li> 
 <li><strong>Instrumentation</strong>：添加电子邮件通知的成功率指标。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F33359" target="_blank">＃33359</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbergquist" target="_blank">@bergquist</a></li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li><strong>Alerting</strong>：从 Slack 通知中删除字段限制。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F33113" target="_blank">＃33113</a></li> 
 <li><strong>Auth</strong>：令牌查找失败时，请勿清除身份验证令牌 cookie。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F32999" target="_blank">＃32999</a></li> 
 <li><strong>Bug</strong>：将 git 命令添加到 Dockerfile.ubuntu 文件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F33247" target="_blank">＃33247</a></li> 
 <li><strong>Explore</strong>：将时间调整为选定的时区。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F33315" target="_blank">＃33315</a></li> 
 <li><strong>GraphNG</strong>：修复示例窗口位置。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F33427" target="_blank">＃33427</a></li> 
 <li><strong>Loki</strong>：将跳过 TLS 验证的设置传递给警报查询。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F33025" target="_blank">＃33025</a></li> 
 <li><strong>Postgres</strong>：在启用 TimescaleDB 且间隔小于一秒时，修复 time group macro。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F33153" target="_blank">＃33153</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv7.5.5" target="_blank">https://github.com/grafana/grafana/releases/tag/v7.5.5</a></p>
                                        </div>
                                      
</div>
            