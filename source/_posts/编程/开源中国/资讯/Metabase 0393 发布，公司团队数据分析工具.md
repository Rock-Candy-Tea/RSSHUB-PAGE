
---
title: 'Metabase 0.39.3 发布，公司团队数据分析工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2763'
author: 开源中国
comments: false
date: Mon, 07 Jun 2021 07:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2763'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Metabase 发布了 0.39.3 版本。Metabase 是一个简单的分析工具，通过给公司成员提问，从得到的数据中进行分析、学习。</p> 
<p>此版本更新内容如下：</p> 
<p><strong>Enhancements</strong> </p> 
<ul> 
 <li>LDAP settings form 在保存时点击错误的 API 端点（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16173" target="_blank">#16173</a>）</li> 
 <li>修复 Serialization P1s ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15756" target="_blank">#15756</a> )</li> 
 <li>保存前测试 LDAP 设置 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F11446" target="_blank">#11446</a> )</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li>Feature flag 会导致 Number 过滤器在 Native 查询中出现问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16218" target="_blank">#16218</a> )</li> 
 <li>撤销对多组用户的访问权限无法正确清理 GTAP ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16190" target="_blank">#16190</a> )</li> 
 <li>当用户调整浏览器窗口大小时，ExpressionEditor loses value ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16127" target="_blank">#16127</a> )</li> 
 <li>当字段具有 300 多个不同值时，过滤器下拉菜单不适用于非数据用户。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16112" target="_blank">#16112</a>）</li> 
 <li>当 X 轴为数字且样式为序数/直方图时，工具提示仅显示第一个 Y 轴值（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15998" target="_blank">#15998</a>）</li> 
 <li>小屏幕上的仪表可视化可能会导致悬停时前端刷新 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15980" target="_blank">#15980</a> )</li> 
 <li>Serialization：从 1.39.0 开始<code>field-literal</code>转换为<code>field</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15971" target="_blank">#15971</a>）</li> 
 <li>在 1.39.0 中用静态引用代替路径进行序列化转储（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15812" target="_blank">#15812</a>）</li> 
 <li>有些地方显示 &#123;0&#125;占位符，而不是预期值（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15694" target="_blank">#15694</a>）</li> 
 <li>......</li> 
</ul> 
<p><strong>Upgrading</strong></p> 
<p>用户可以下载该发行版的 .jar，或在 Docker 上获取最新版本。升级之前，请确保备份 Metabase 数据库。详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmetabase.com%2Fdocs%2Flatest%2Foperations-guide%2Fupgrading-metabase.html" target="_blank">升级说明</a>。</p> 
<p>Docker 镜像： metabase/metabase:v0.39.3<br> 下载 JAR：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownloads.metabase.com%2Fv0.39.3%2Fmetabase.jar" target="_blank">https://downloads.metabase.com/v0.39.3/metabase.jar</a></p> 
<p><strong>Notes</strong></p> 
<p>SHA-256 checksum for the 0.39.3 JAR:</p> 
<pre>81b26d7d9eb1385962a02c2133a2f82e95adeaf425fd329c7f02f98b1161282eg</pre> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Freleases%2Ftag%2Fv0.39.3" target="_blank">https://github.com/metabase/metabase/releases/tag/v0.39.3</a></p>
                                        </div>
                                      
</div>
            