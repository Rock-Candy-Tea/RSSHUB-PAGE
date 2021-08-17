
---
title: 'PostgreSQL 14 Beta 3 发布、9.6 即将 EOL'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1320'
author: 开源中国
comments: false
date: Tue, 17 Aug 2021 07:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1320'
---

<div>   
<div class="content">
                                                                                            <p>PostgreSQL 全球开发组近日为所有受支持的版本发布了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fpostgresql-134-128-1113-1018-9623-and-14-beta-3-released-2277%2F" target="_blank">更新</a>，分别是 <span style="color:null"><span style="background-color:null">13.4、12.8、11.13、10.18、9.6.23 和 14 Beta 3。更新内容包括修复一个安全漏洞，以及修复过去三个月社区报告的超过 75 个错误。</span></span></p> 
<p><span style="color:null"><span style="background-color:null"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fdocs%2Frelease%2F" target="_blank">完整变更内容查看 release note</a>。</span></span></p> 
<h3><span style="color:null"><span style="background-color:null">安全漏洞</span></span></h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fsupport%2Fsecurity%2FCVE-2021-3677%2F" target="_blank"><span style="color:null"><span style="background-color:null">CVE-2021-3677</span></span></a><span style="color:null"><span style="background-color:null">：部分查询出现内存泄露</span></span></p> 
<p><span style="color:#0d0a0b"><span style="background-color:#ffffff">受影响的版本：11 - 13</span></span></p> 
<p style="text-align:left"><span style="color:#0d0a0b"><span style="background-color:#ffffff">漏洞描述：专门设计的查询可以读取服务器内存的任意字节。在默认配置下，任何经过身份验证的数据库用户都可以随意完成此攻击。攻击不需要创建对象的能力。如果服务器设置包括<code>max_worker_processes=0</code>，则无法对已知版本进行此攻击。但是，未被发现的攻击变体可能与该设置无关。</span></span></p> 
<h3 style="text-align:left">PostgreSQL 14 Beta 3</h3> 
<p style="text-align:left">PostgreSQL 14 Beta 3 为多域类型(multirange types)引入了<code>unnest</code>功能以及一些错误修复。</p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.postgresql.org%2Fwiki%2FPostgreSQL_14_Open_Items%23resolved_before_14beta3" target="_blank">完整变更点此查看</a>。</p> 
<p style="text-align:left"><span style="color:#0d0a0b"><span style="background-color:#ffffff">最后值得注意的是，PostgreSQL 9.6 将于 2021 年 11 月 11 日停止接收修复。如果用户在生产环境中使用的是 PostgreSQL 9.6，官方建议他们计划升级到更新的受支持的 PostgreSQL 版本。更多信息查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fsupport%2Fversioning%2F" target="_blank">版本控制政策</a>。</span></span></p>
                                        </div>
                                      
</div>
            