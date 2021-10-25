
---
title: 'Sequelize 6.8.0 发布，基于 Nodejs 的异步 ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1195'
author: 开源中国
comments: false
date: Mon, 25 Oct 2021 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1195'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Sequelize 6.8.0 发布了，Sequelize 是一款基于 Nodejs 的异步 ORM 框架，它同时支持 PostgreSQL、MySQL、SQLite 和 MSSQL 多种数据库，很适合作为 Nodejs 后端数据库的存储接口，为快速开发 Node.js 应用奠定扎实、安全的基础。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">本次更新内容如下：</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#333333">bug 修复</span></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>types:<span> </span></strong><code>isIn</code><span> </span>验证器允许<span style="color:#24292f">接受任何值。 (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F12962" target="_blank">#12962</a><span style="color:#24292f">)</span></li> 
 <li>允许插入带零的主键。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13458" target="_blank">#13458</a><span> </span>)</li> 
 <li><strong>model:</strong><span style="color:#24292f"><span> </span>为了避免出现 NaN ，只有当数值不为空时才允许转换数值。</span>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2F199b632b021830f9d09210fd7430045710638631" target="_blank"><u>199b632</u></a><span> </span>)</li> 
 <li><strong>fix(model.d):  </strong>在<span> </span><code>where</code><span> </span>中接受<span> </span><code>[Op.is]</code>（这功能在 TypeScript 4.4 中被破坏）。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13499" target="_blank">#13499</a>）</li> 
 <li><strong>postgres:<span> </span></strong>修复了<strong><span> </span></strong><span style="color:#24292f"><code>findCreateFind</code><span> </span>方法，让它能和<span> </span></span><code>postgres transactions</code><span> </span>一起工作。<span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13482" target="_blank">#13482</a><span style="color:#24292f">)</span></li> 
 <li><strong>select:</strong><span style="color:#24292f"><span> </span></span>不再强制设置<span> </span><code>subQuery</code><span> </span>为<span> </span><code>false</code><span> </span>。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13490" target="_blank">#13490</a>）</li> 
 <li><strong>sqlite:</strong><span style="color:#24292f"><span> </span> </span>修复了空字符串错误地覆盖存储的问题。<span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13376" target="_blank">#13376</a><span style="color:#24292f">) </span></li> 
 <li><strong>types:<span> </span></strong>加入了缺少的  <span style="color:#24292f">upsert hooks 。(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13394" target="_blank"><u>#13394</u></a><span style="color:#24292f">)</span></li> 
 <li><strong>types:<span> </span></strong><span style="color:#2e3033">通过<span> </span><code>SearchPathable</code><span> </span>来扩展<span> </span><code>BulkCreateOptions</code>。<span> </span></span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13469" target="_blank"><u>#13469</u></a><span style="color:#24292f">) </span></li> 
 <li><strong>types:<span> </span></strong><span style="color:#24292f">修正了<span> </span><code>model.d.ts</code><span> </span>中的错别字。(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13574" target="_blank"><u>#13574</u></a><span style="color:#24292f">) </span></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#24292f">新功能</span></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>postgres:</strong><span style="color:#24292f"><span> </span> 支持 query_timeout 选项。 (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13258" target="_blank">#13258</a><span style="color:#24292f">) (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2F3ca085db318201fa59422a2ce191bcf76e5f37dc" target="_blank">3ca085d</a><span style="color:#24292f">)</span></li> 
 <li><strong>typings:<span> </span></strong><span style="color:#24292f">添加<span> </span><code>UnknownConstraintError</code></span><span> </span> (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13461" target="_blank">#13461</a><span> </span>) (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2F69d899e27b733adb24e4300b48c9bae91455932f" target="_blank">69d899e</a><span> </span>)</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f">更新公告：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Freleases%2Ftag%2Fv6.8.0" target="_blank">https://github.com/sequelize/sequelize/releases/tag/v6.8.0</a></p>
                                        </div>
                                      
</div>
            