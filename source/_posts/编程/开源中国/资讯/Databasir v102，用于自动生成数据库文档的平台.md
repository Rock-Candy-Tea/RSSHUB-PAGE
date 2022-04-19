
---
title: 'Databasir v1.0.2，用于自动生成数据库文档的平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7c1870cc4ef30046f80189e104a3883dc64.png'
author: 开源中国
comments: false
date: Tue, 19 Apr 2022 08:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7c1870cc4ef30046f80189e104a3883dc64.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; text-align:start"><span>Hi，大家好，懒是第一生产力，项目的初衷就是为了能够自动生成数据库的模型文档，能够在数据库模型有变更时自动通知相关业务人员，让我专注于 coding（moyu）。</span></p> 
<p><span>上个版本 release 后收到了不少建议，90% 都已经在这个版本中完成了，尤其是大家反馈最多的的搜索与注释功能，话不多说，直接进入主题</span></p> 
<h2 style="margin-left:0.5em; margin-right:0px"><span>简介</span></h2> 
<p style="color:#333333; text-align:start"><span>如果懒得读可以直接看后面的<strong><span>功能展示</span></strong></span><span>，通过动图了解更直观。</span></p> 
<p style="color:#333333; text-align:start"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvran-dev%2Fdatabasir"><span>Databasir </span></a></span><span>是一款专注于</span><span><strong><span>数据库文档管理的开源平台</span></strong></span><span>，提供了自动化、版本化、团队化、个性化的文档管理特性。</span></p> 
<ul> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>自动化：表结构逆向生成文档，支持手动、定时同步，文档变更自动通知等</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>版本化：文档多版本记录，一键查看版本差异</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>团队化：扁平化的角色管理、系统日志审计、团队协作</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>个性化：文档模板自定义、</span><span><strong><span>理论支持任意拥有 JDBC 驱动的数据库</span></strong></span><span>、支持 Markdown、UML 导出</span></p> </li> 
</ul> 
<p><img height="31" src="https://oscimg.oschina.net/oscnet/up-7c1870cc4ef30046f80189e104a3883dc64.png" width="100" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:.5em; margin-right:0; text-align:start"><span>v1.0.2 发布内容</span></h2> 
<p style="color:#333333; text-align:start"><span>功能</span></p> 
<ol start> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feature；UML 图片导出支持 svg 格式</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feature；表目录列表支持按表名、注释名搜索</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feature；表文档页面新增注释展示</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feature；数据库扩展支持自动获取驱动类名</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feature：数据库元数据同步采用异步任务设计，解决大数据量同步超时问题</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feature：文档内容采用分组加载，解决大数据量加载超时问题</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feature：文档默认模板统一改为中文</span></p> </li> 
</ol> 
<p style="color:#333333; text-align:start"><span>安全</span></p> 
<ol start> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>security：对上传的驱动 jar 包新增规则校验</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>security：采用可配置（默认随机）的 jwt token secret</span></p> </li> 
</ol> 
<p style="color:#333333; text-align:start"><span><strong><span>Release 地址</span></strong></span><span>：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvran-dev%2Fdatabasir%2Freleases" target="_blank"><span>https://github.com/vran-dev/databasir/releases</span></a></span></p> 
<p style="color:#333333; text-align:start"><span><strong><span>文档地址</span></strong></span><span>：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.databasir.com" target="_blank"><span>https://doc.databasir.com</span></a></span></p> 
<p style="color:#333333; text-align:start"><span><strong><span>项目地址</span></strong></span><span>：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvran-dev%2Fdatabasir" target="_blank"><span>https://github.com/vran-dev/databasir</span></a></span></p> 
<p style="color:#333333; text-align:start"><span><strong><span>演示地址</span></strong></span><span>：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.databasir.com" target="_blank"><span>https://demo.databasir.com</span></a></span></p> 
<h2 style="margin-left:.5em; margin-right:0; text-align:start"><span>功能展示</span></h2> 
<ul> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>文档同步</span></p> </li> 
</ul> 
<p><img height="938" src="https://oscimg.oschina.net/oscnet/up-66dbc4a4b23bfc02c1cd50041adc0ae9a52.gif" width="1920" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>扩展受支持的数据库</span></p> </li> 
</ul> 
<p><img height="938" src="https://oscimg.oschina.net/oscnet/up-24e898e0281e91149c6a18381f37697f19f.gif" width="1920" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>导出 UML</span></p> </li> 
</ul> 
<p><img height="938" src="https://oscimg.oschina.net/oscnet/up-7f9a5753b607880805832de94bdc1374049.gif" width="1920" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>markdown 文档展示</span></p> </li> 
</ul> 
<p><img height="938" src="https://oscimg.oschina.net/oscnet/up-d0e70a4cb349460f2758adb38e81d83663b.gif" width="1920" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            