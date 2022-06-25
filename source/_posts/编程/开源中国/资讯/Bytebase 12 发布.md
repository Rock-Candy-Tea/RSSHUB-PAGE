
---
title: 'Bytebase 1.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-124f3cfa97c294f87216e4b47a347e62543.gif'
author: 开源中国
comments: false
date: Sat, 25 Jun 2022 07:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-124f3cfa97c294f87216e4b47a347e62543.gif'
---

<div>   
<div class="content">
                                                                                            <p>Bytebase 是一个基于网络、零配置、无依赖的数据库 Schema 变更和版本控制管理工具，适用于开发人员和 DBA。</p> 
<p>Bytebase 1.2 发布，更新内容如下：</p> 
<h3><strong>支持 SQL 编辑器中的 Schema 审核</strong></h3> 
<p><img alt height="394" src="https://oscimg.oschina.net/oscnet/up-124f3cfa97c294f87216e4b47a347e62543.gif" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>配置完 Schema 审核规则后，在 SQL 编辑器中运行的语句如果违反了规则，Bytebase 会阻止语句执行并显示错误信息</li> 
 <li>可以把具体规则的警告等级从 「Error」 改为 「Warning」级别 
  <ul> 
   <li>如果语句违反了 Schema 审核规则，提示信息为 「Warning」，但 SQL 语句仍能正常运行</li> 
   <li>如果 Schema 审核通过，Bytebase 将正常运行 SQL 语句</li> 
  </ul> </li> 
</ul> 
<h3><strong>改进</strong></h3> 
<ul> 
 <li>改进了 SQL 编辑器的样式：</li> 
</ul> 
<p><img alt height="384" src="https://oscimg.oschina.net/oscnet/up-42bcb358d1f4c30ebbe74baf94674fbffce.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>改进了工单页面的 SQL 编辑器体验，提供了自动完成和代码格式化功能</li> 
 <li>支持为 ClickHouse 实例配置 SSL 连接参数</li> 
 <li>允许用户重试失败的表结构变更任务</li> 
 <li>在多租户模式下的工单中，支持 Approve / Run 一个 stage 下的所有 task</li> 
 <li>多租户项目不再强制相同数据库表结构版本号</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbytebase%2Fbytebase%2Freleases%2Ftag%2F1.2.0" target="_blank">https://github.com/bytebase/bytebase/releases/tag/1.2.0</a></p>
                                        </div>
                                      
</div>
            