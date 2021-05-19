
---
title: 'Metabase 0.39.2 发布，公司团队数据分析工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=797'
author: 开源中国
comments: false
date: Wed, 19 May 2021 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=797'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Metabase 发布了 0.39.2 版本。Metabase 是一个简单的分析工具，通过给公司成员提问，从得到的数据中进行分析、学习。</p> 
<p>此版本更新内容如下：</p> 
<p><strong>Enhancements</strong> </p> 
<ul> 
 <li>在企业自定义构建中显示正确的版本（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15677" target="_blank">＃15677</a>）</li> 
 <li>无法使用复选框选择 pinned collection item（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15338" target="_blank">＃15338</a>）</li> 
 <li>Collection tree loader 导致 UI jump（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F14603" target="_blank">＃14603</a>）</li> 
 <li>需要更好的说明来设置 Google Auth（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F9744" target="_blank">＃9744</a>）</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li>将 Druid 日期过滤器与维度过滤器相结合的回归（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15903" target="_blank">＃15903</a>）</li> 
 <li>升级后的变量字段类型“输入到 parse-value-to-field-type 与模式不匹配”​​（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15901" target="_blank">＃15901</a>）</li> 
 <li>Whitelabel favicon 在所有浏览器中都不能正常工作（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15711" target="_blank">＃15711</a>）</li> 
 <li>字段值查询的新“contains”行为在 dashboards 之外无法工作（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15240" target="_blank">＃15240</a>）</li> 
 <li>当数据库停机时，无法恢复数据模型中的表的可见性（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15165" target="_blank">＃15165</a>）</li> 
 <li>当用户没有数据权限时，难以使用某些过滤器[FE-如果 API 端点返回 403，则过滤器小部件将停止工作]（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15119" target="_blank">＃15119</a>）</li> 
 <li>带下拉列表的过滤器使用数据库查询（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F13832" target="_blank">＃13832</a>）</li> 
 <li>如果用户电子邮件不是小写，则 LDAP 登录失败（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F13739" target="_blank">＃13739</a>）</li> 
 <li>有关不支持的类的启动警告将影响性能（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F13625" target="_blank">＃13625</a>）</li> 
 <li>在提交错误的验证时，Auth 返回 400 错误请求而不是 401 未授权（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F13140" target="_blank">＃13140</a>）</li> 
 <li>......</li> 
</ul> 
<p><strong>Upgrading</strong></p> 
<p>用户可以下载该发行版的 .jar，或在 Docker 上获取最新版本。升级之前，请确保备份 Metabase 数据库。详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmetabase.com%2Fdocs%2Flatest%2Foperations-guide%2Fupgrading-metabase.html" target="_blank">升级说明</a>。</p> 
<p>Docker 镜像：<code>metabase/metabase:v0.39.2</code><br> 下载 JAR：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownloads.metabase.com%2Fv0.39.2%2Fmetabase.jar" target="_blank">https://downloads.metabase.com/v0.39.2/metabase.jar</a></p> 
<p><strong>Notes</strong></p> 
<p>SHA-256 checksum for the 0.39.2 JAR:</p> 
<pre>51b4d1d45a9e3929ff96e9dec4c2b55663e5d08c5de25dbb5ed16f9dd2e4faff</pre> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Freleases%2Ftag%2Fv0.39.2" target="_blank">https://github.com/metabase/metabase/releases/tag/v0.39.2</a></p>
                                        </div>
                                      
</div>
            