
---
title: 'InfluxDB 2.0.8 发布，开源时序数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9530'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9530'
---

<div>   
<div class="content">
                                                                                            <p>InfluxDB 2.0.8 现已发布，具体更新内容如下：</p> 
<p><strong>WARNING：即将对 CLI 打包进行更改</strong></p> 
<p>从下一个次要版本开始，<code>influx</code>CLI 将不再被打包在<code>influxdb</code>来版本中发布。未来 CLI 的版本将从<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finflux-cli" target="_blank"><code>influx-cli</code></a>仓库中发布。</p> 
<p>希望采用新 CLI 的用户可以从 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finflux-cli%2Freleases%2Flatest" target="_blank">GitHub</a> 或 InfluxData <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fportal.influxdata.com%2Fdownloads%2F" target="_blank">Downloads Portal</a> 下载其最新版本。</p> 
<p><strong>Go Version</strong></p> 
<p>该版本将项目升级到 Go 1.16 版本。</p> 
<p><strong>Minimum macOS Version</strong></p> 
<p>由于版本的提升，这个版本的 macOS 构建至少需要 10.12 Sierra 版本才能运行。</p> 
<p><strong>Features</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21922" target="_blank">21922</a>：在<code>influxd</code>中添加<code>--ui-disabled</code>选项以允许在禁用 UI 的情况下运行。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21969" target="_blank">21969</a>：遥测改进：不记录不存在路径的遥测数据；用 slug 替换无效的静态资产路径。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F22098" target="_blank">22098</a>：将 Flux 升级到 v0.124.0。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F22101" target="_blank">22101</a>：将 UI 升级到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Fui%2Freleases%2Ftag%2FOSS-v2.0.8" target="_blank">v2.0.8</a>。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F22101" target="_blank">22101</a>：升级<code>flux-lsp-browser</code>到 v0.5.53。</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21748" target="_blank">21748</a>：使用 yum 兼容的名称重命名 arm rpm。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21859" target="_blank">21859</a>：避免<code>fields.idx</code>不必要的重写。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21860" target="_blank">21860</a>：不要在 DigestWithOptions 中两次关闭连接。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21866" target="_blank">21866</a>：删除不正确的 group-by 优化。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21867" target="_blank">21867</a>：当 InfluxQL 语句重写失败时，返回错误而不是 panicking。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21868" target="_blank">21868</a>：在使用之前将恢复的 KV 快照迁移到最新架构。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21869" target="_blank">21869</a>：指定在拒绝不完整的 onboarding 请求时缺少哪些字段。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Fpull%2F21941" target="_blank">21941</a>：升级到 golang-jwt 3.2.1。</li> 
 <li>......</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finfluxdata%2Finfluxdb%2Freleases%2Ftag%2Fv2.0.8" target="_blank">https://github.com/influxdata/influxdb/releases/tag/v2.0.8</a></p>
                                        </div>
                                      
</div>
            