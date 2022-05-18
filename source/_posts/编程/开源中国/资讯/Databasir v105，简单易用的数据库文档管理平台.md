
---
title: 'Databasir v1.0.5，简单易用的数据库文档管理平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-191f2e552a3bbc074892c540c7b9a4c47b2.gif'
author: 开源中国
comments: false
date: Wed, 18 May 2022 01:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-191f2e552a3bbc074892c540c7b9a4c47b2.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Hello，又到了发版的时候了，功能的迭代依旧稳步进行......</p> 
<h2>支持平台</h2> 
<p>由于使用了 JDBC 获取元数据，Databasir 能兼容市面绝大多数的数据库。</p> 
<p>除了我们熟知的 <strong>Mysql</strong>、<strong>Postgresql</strong>、<strong>Oracle、MariaDB </strong>以及<strong>达梦</strong>等传统数据库外，社区还有小伙伴接入了 <strong>Hive</strong>、<strong>Clickhouse </strong>等数仓，如果你接入了新的 DB ，欢迎反馈给我。</p> 
<h2>多图展示</h2> 
<p>> 更多功能请登录<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.databasir.com" target="_blank">演示地址</a>查看</p> 
<p>版本差异</p> 
<p><img height="1066" src="https://oscimg.oschina.net/oscnet/up-191f2e552a3bbc074892c540c7b9a4c47b2.gif" width="1948" referrerpolicy="no-referrer"></p> 
<p>全局搜索</p> 
<p><img height="961" src="https://oscimg.oschina.net/oscnet/up-3f5d44ca0603922ea69857522b8af8bdb10.gif" width="1440" referrerpolicy="no-referrer"></p> 
<h2>变更记录</h2> 
<p><img height="48" src="https://oscimg.oschina.net/oscnet/up-e9adcb60da03e94ce5b99d912f53304a3e1.png" width="48" referrerpolicy="no-referrer">Feature</p> 
<ol> 
 <li>feat：mysql、postgresql、mariaDB、oracle、sqlServer 支持生成触发器（trigger）文档信息</li> 
 <li>feat：支持全局搜索分组、项目、数据库、schema</li> 
 <li>feat：完善审计日志，新增文档描述更新、文档评论、文档导出等审计操作</li> 
 <li>feat：导出 markdown 内容中新增表注释</li> 
 <li>ui：优化分组列表卡片 UI 细节</li> 
 <li>ui：数据库扩展采用卡片式列表替换表格设计</li> 
</ol> 
<p><img height="48" src="https://oscimg.oschina.net/oscnet/up-6289cf23ab7fd7a817c5333dd73aebe1f0e.png" width="48" referrerpolicy="no-referrer"> Bug fix</p> 
<ol> 
 <li>fix：sql server 无法获取注释</li> 
 <li>fix：触发器名称没有显示</li> 
 <li>fix：文档页面表搜索框占位文案描述不清晰</li> 
 <li>fix：分组列表页的组长信息丢失</li> 
 <li>fix：组长查看项目日志时出现无权限</li> 
 <li>fix：注释内容过长会导致文档同步失败</li> 
</ol> 
<p><img height="48" src="https://oscimg.oschina.net/oscnet/up-fc9eab223c74d25aef6d1958345346130ea.png" width="48" referrerpolicy="no-referrer">Refactor</p> 
<ol> 
 <li>refactor：将 <code>plugin</code> 模块重命名为 <code>meta</code> 模块</li> 
 <li>refactor：重构 <code>MetaRepository</code> 为 <code>MetaProvider</code></li> 
 <li>refactor：API 接口增加 swagger 注解</li> 
</ol> 
<h2>更多</h2> 
<ul> 
 <li><strong>Github 地址</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvran-dev%2Fdatabasir" target="_blank">https://github.com/vran-dev/databasir</a></li> 
 <li><strong>文档地址</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.databasir.com" target="_blank">https://doc.databasir.com</a></li> 
 <li><strong>演示地址</strong>：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.databasir.com" target="_blank">http://demo.databasir.com</a>  // 请查看项目文档获取登录用户名和密码</li> 
 <li><strong>Release 地址</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvran-dev%2Fdatabasir%2Freleases%2Ftag%2Fv1.0.5" target="_blank">https://github.com/vran-dev/databasir/releases/tag/v1.0.5</a></li> 
</ul>
                                        </div>
                                      
</div>
            