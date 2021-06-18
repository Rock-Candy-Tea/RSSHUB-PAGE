
---
title: 'Metabase v0.39.4 发布，公司团队数据分析工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1930'
author: 开源中国
comments: false
date: Fri, 18 Jun 2021 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1930'
---

<div>   
<div class="content">
                                                                                            <p>Metabase 发布了 0.39.4 版本。Metabase 是一个简单的分析工具，通过给公司成员提问，从得到的数据中进行分析、学习。</p> 
<p>此版本更新内容如下：</p> 
<p><strong>Enhancements</strong> </p> 
<ul> 
 <li>当侧边栏已经打开时切换到 column settings ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fpull%2F16368" target="_blank">#16368</a> )</li> 
 <li>缺少用于共享单个问题的工具提示 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16108" target="_blank">#16108</a> )</li> 
 <li>当输入没有 in focus 时不显示自定义表达式助手 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15891" target="_blank">#15891</a> )</li> 
</ul> 
<p><strong>Bug修复</strong></p> 
<ul> 
 <li>启用 JWT 身份验证时出现 Javascript 错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16378" target="_blank">#16378</a> )</li> 
 <li>从 0.38.5 升级到 0.39.0 后，在对数组进行过滤时，MongoDB上的问题返回'No results!'  ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16299" target="_blank">#16299</a> )</li> 
 <li>如果 Metabase 无法访问 GeoJS API，登录将被阻止直到超时（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16169" target="_blank">#16169</a>）</li> 
 <li>直方图应该过滤掉空 x 值（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16049" target="_blank">#16049</a>）</li> 
 <li>沿 x 轴顺序移动图表值 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16002" target="_blank">#16002</a> )</li> 
 <li>仪表板过滤器下拉列表仅列出前 100 个值 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15695" target="_blank">#15695</a> )</li> 
 <li>在自定义表达式中不能在两个<code>case()</code>函数之间使用算术运算( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15107" target="_blank">#15107</a> )</li> 
 <li>当用户被分配到 1 个组时，LDAP 登录失败与 Group Sync ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15073" target="_blank">#15073</a> )</li> 
 <li>如果<code>givenName</code>或<code>sn</code>丢失，LDAP认证会出现"did not match stored password"的错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F14767" target="_blank">#14767</a>）</li> 
 <li>无法连接本身包含连接的 Saved Questions ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F12928" target="_blank">#12928</a> )</li> 
 <li>Human-reable numering 无法正常工作 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F12629" target="_blank">#12629</a> )</li> 
 <li>屏幕底部的时间序列过滤器和 granularity widgets 丢失 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F11183" target="_blank">#11183</a> )</li> 
 <li>LDAP group sync - 从映射组中删除用户后出现 LDAPException ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F11172" target="_blank">#11172</a> )</li> 
 <li>仪表板文本卡不滚动（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F8333" target="_blank">#8333</a>）</li> 
</ul> 
<p><strong>Upgrading</strong></p> 
<p>用户可以下载该发行版的 .jar，或在 Docker 上获取最新版本。升级之前，请确保备份 Metabase 数据库。详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmetabase.com%2Fdocs%2Flatest%2Foperations-guide%2Fupgrading-metabase.html" target="_blank">升级说明</a>。</p> 
<p>Docker 镜像：metabase/metabase:v0.39.4 <br> 下载 JAR：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownloads.metabase.com%2Fv0.39.4%2Fmetabase.jar" target="_blank">https://downloads.metabase.com/v0.39.4/metabase.jar</a></p> 
<p><strong>Notes</strong></p> 
<p>SHA-256 checksum for the 0.39.4 JAR:</p> 
<pre><code>f0fbb4c5b67d27b6e2b73f4794c45dc6a03f8b6a572a65c5e1e0cca9bf940894</code></pre> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Freleases%2Ftag%2Fv0.39.4" target="_blank">https://github.com/metabase/metabase/releases/tag/v0.39.4</a></p>
                                        </div>
                                      
</div>
            