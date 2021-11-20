
---
title: 'Sequelize 6.10.0 发布，基于 Nodejs 的异步 ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5025'
author: 开源中国
comments: false
date: Sat, 20 Nov 2021 07:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5025'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Sequelize 6.10.0 发布了，Sequelize 是一款基于 Nodejs 的异步 ORM 框架，它同时支持 PostgreSQL、MySQL、SQLite 和 MSSQL 多种数据库，很适合作为 Nodejs 后端数据库的存储接口，为快速开发 Node.js 应用奠定扎实、安全的基础。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">本次更新内容如下：</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Bug Fixes</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>logger：</strong>将记录深度从 3 更改为 1（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F12879" target="_blank">#12879</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2Fddddc244c2019a765ad889226584b8fb07ff50da" target="_blank">ddddc24</a>）</li> 
 <li><strong>mariadb:</strong><span style="color:#24292f"><span> </span>修复了 MariaDB 10.5 的 JSON 字段处理。(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13633" target="_blank">#13633</a><span style="color:#24292f">) (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2Fcdd61ddbe83cbfe77dc04a32196dcc66e0052f51" target="_blank">cdd61dd</a><span style="color:#24292f">)</span></li> 
 <li><strong>model:</strong><span style="color:#24292f"><span> </span>现在会</span><span style="color:#2e3033">克隆选项对象，而不是直接修改它。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13589" target="_blank">#13589</a><span style="color:#24292f">) (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2F3be43deeb9a4e03cffb1d72ebc67a534a3c5dc19" target="_blank">3be43de</a><span style="color:#24292f">)</span></li> 
 <li><strong>mssql:</strong><span style="color:#24292f"><span> </span></span><span style="color:#2e3033">修正重命名主键字段时出现的子查询问题。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F12801" target="_blank">#12801</a><span style="color:#24292f">) (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2F73d99ab45c069119478d8ef39ff9391181d5578f" target="_blank">73d99ab</a><span style="color:#24292f">)</span></li> 
 <li><strong>mssql:<span> </span></strong><span style="color:#2e3033">Sqlserver 2008修复了使用偏移量和包含标准的问题。</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2F47c4494968422585bf265063925d1662ffcd4173" target="_blank">47c4494</a>)</li> 
 <li><strong>query:</strong><span> </span>现在<span style="color:#2e3033">堆栈跟踪会包含原始的调用代码。</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13347" target="_blank">#13347</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2Ff58154334d98038deafbecd017cf5719d1b13b7f" target="_blank">f581543</a>)</li> 
 <li><strong>types:</strong><span> </span><span style="color:#2e3033">在模型中添加缺失的类型定义。</span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13553" target="_blank">#13553</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2F73ecf6cf33628eca38973c0eeb5c798dbba177e9" target="_blank">73ecf6c</a>)</li> 
 <li><strong>types:</strong><span> </span><span style="color:#2e3033">在 model.d.ts 中添加 specifictojson 类型。</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13661" target="_blank">#13661</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2F5924be52152232fbd7a925d599c31cac9f90dc6d" target="_blank">5924be5</a>)</li> 
 <li><strong>types:</strong><span> </span>DataType.TEXT 重载定义。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13654" target="_blank">#13654</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2F1690801cda2ca15f32aaaf5e9ebd96e800808e36" target="_blank">1690801</a>)</li> 
 <li><strong>types:</strong><span style="color:#24292f"> </span><span style="color:#2e3033">在 IncludeThroughOptions 定义中</span>添加<span> </span><code>paranoid</code><span> </span>属性<span style="color:#2e3033">。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13625" target="_blank">#13625</a><span style="color:#24292f">) (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2Fb1fb1f32f7d66c013bbf015345a1076893ffd806" target="_blank">b1fb1f3</a><span style="color:#24292f">)</span></li> 
 <li><strong>types:</strong><span style="color:#24292f"> 修复<span> </span><code>Op.ne</code><span> </span>文档错误问题。(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13666" target="_blank">#13666</a><span style="color:#24292f">) (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2F98485dfcff501c565dbf453a54868a4dfe60a225" target="_blank">98485df</a><span style="color:#24292f">)</span></li> 
 <li><strong>types:</strong><span style="color:#24292f"><span> </span></span><span style="color:#2e3033">重命名类型并更新<span> </span><code>contributions</code><span> </span>文档。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13348" target="_blank">#13348</a><span style="color:#24292f">) (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2F1f2392423212ca9a4604772c1d0a2f008606695e" target="_blank">1f23924</a><span style="color:#24292f">)</span></li> 
 <li><span style="color:#2e3033">修复预期结果为 NULL ，但得到 0 的问题。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13637" target="_blank">#13637</a><span style="color:#24292f">) (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2Fda3ac091032856f8a74297eff9a9d89e7fc997e5" target="_blank">da3ac09</a><span style="color:#24292f">)</span></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新特性</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>definitions:</strong><span> </span><span style="color:#2e3033">添加 AbstractQuery 和前/后 query hook 定义。</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13635" target="_blank">#13635</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2F37a5858b1e635a28dee1da494f278753d489bbe8" target="_blank">37a5858</a>)</li> 
 <li><strong>postgresql:</strong><span> </span>现在有更简单的<span> </span><span style="color:#2e3033">SSL 配置和选项参数</span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13673" target="_blank">#13673</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2F95915739443f96996841dacfd6861e9d5ba35c1b" target="_blank">9591573</a>)</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Freleases%2Ftag%2Fv6.10.0" target="_blank">https://github.com/sequelize/sequelize/releases/tag/v6.10.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            