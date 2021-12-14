
---
title: 'Metabase v0.41.4 发布，解决 log4j2 漏洞问题'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2703'
author: 开源中国
comments: false
date: Mon, 13 Dec 2021 23:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2703'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Metabase 发布了 v0.41.4 版本。Metabase 是一个简单的分析工具，通过给公司成员提问，从得到的数据中进行分析、学习。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此版本更新内容如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong style="color:#000000">Bug 修复</strong></p> 
<ul> 
 <li style="text-align:start">通过更新 log4j2 到 2.15.0 解决 CVE-2021-44228 安全漏洞</li> 
</ul> 
<p style="color:#000000; margin-left:0px; margin-right:0px; text-align:start">如果你不能马上升级，那么可通过设置 Java 属性<code>log4j2.formatMsgNoLookups=true</code>来增加缓解。JAR <span style="background-color:#ffffff; color:#24292f">示例</span>：<code>java ... -Dlog4j2.formatMsgNoLookups=true ... -jar metabase.jar</code>。Docker 示例：<code>docker run ... -e JAVA_OPTS="-Dlog4j2.formatMsgNoLookups=true" ...</code></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Upgrading</strong> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">用户可以下载该发行版的 .jar，或在 Docker 上获取最新版本。升级之前，请确保备份 Metabase 数据库。详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmetabase.com%2Fdocs%2Flatest%2Foperations-guide%2Fupgrading-metabase.html" target="_blank">升级说明</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Docker 镜像：<code>metabase/metabase:v0.41.4</code><br> 下载 JAR：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownloads.metabase.com%2Fv0.41.4%2Fmetabase.jar" target="_blank">https://downloads.metabase.com/v0.41.4/metabase.jar</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Notes</strong></p> 
<p style="color:#24292f; text-align:start">SHA-256 checksum for the 0.41.4 JAR:</p> 
<div style="text-align:start"> 
 <pre><code>8a14b5db169f2f66d8fcc0d9de597822e83a1f250c3cff57d4dddf384f2314f7</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Freleases%2Ftag%2Fv0.41.4" target="_blank">https://github.com/metabase/metabase/releases/tag/v0.41.4</a></p>
                                        </div>
                                      
</div>
            