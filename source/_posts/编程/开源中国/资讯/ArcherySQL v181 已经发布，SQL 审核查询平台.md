
---
title: 'ArcherySQL v1.8.1 已经发布，SQL 审核查询平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3157'
author: 开源中国
comments: false
date: Sat, 27 Mar 2021 11:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3157'
---

<div>   
<div class="content">
                                                                                            <p>ArcherySQL v1.8.1 已经发布，这是一个 SQL 审核查询平台。</p> 
<p>此版本更新内容包括：</p> 
<h2>变更说明</h2> 
<ul> 
 <li>移除对 Inception 的审核支持，仅作为脱敏语句解析使用</li> 
 <li>在线查询，pg数据库增加会话超时设定，支持查询脱敏</li> 
 <li>慢查日志和明细列表支持按表头字段进行服务端排序</li> 
 <li>默认资源组、权限组支持多选，优化系统配置下拉选项</li> 
</ul> 
<h2>修复说明</h2> 
<ul> 
 <li>解决数据库区分大小写时查看事务信息报错的问题</li> 
 <li>解决 memoryview is not JSON serializable</li> 
 <li>PG脱敏-查询语句中带有别名脱敏处理</li> 
 <li>解决查询结果不展示json对象的问题</li> 
 <li>调整启动方式为wsgi，解决上版本出现访问阻塞的问题</li> 
 <li>企业微信消息推送,如果消息接受者ID为空,则不会调用企业微信官方API.</li> 
 <li>fix(sendmsg/feishu): fix #1016 支持新版飞书 webhook 接口 )</li> 
 <li>Bump django from 3.1.2 to 3.1.6</li> 
 <li>add pycryptodome to requirements</li> 
</ul> 
<h2>易用性调整</h2> 
<ul> 
 <li>手动执行按钮改名为“已手动完成”</li> 
</ul> 
<h2>安全性调整</h2> 
<ul> 
 <li>对接受入参的SQL拼接增加参数转义，规避注入风险</li> 
 <li>使用shlex.quote()对插件参数进行过滤，规避注入风险</li> 
</ul> 
<h2>升级步骤</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Farcherydms.com%2Finstallation%2Fupgrade%2F" target="_blank">https://archerydms.com/installation/upgrade/</a></li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/rtttte/Archery/releases/v1.8.1">https://gitee.com/rtttte/Archery/releases/v1.8.1</a></p>
                                        </div>
                                      
</div>
            