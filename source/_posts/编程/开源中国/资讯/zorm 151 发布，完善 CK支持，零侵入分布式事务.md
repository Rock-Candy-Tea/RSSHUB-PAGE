
---
title: 'zorm 1.5.1 发布，完善 CK支持，零侵入分布式事务'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7195'
author: 开源中国
comments: false
date: Tue, 20 Jul 2021 17:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7195'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><span style="background-color:#ffffff; color:#40485b">zorm是</span><span style="background-color:#ffffff; color:#40485b">go(golang)轻量级ORM,零依赖,零侵入分布式事务,支持达梦(dm),金仓(kingbase),神通(shentong),南大通用(gbase),mysql,postgresql,oracle,mssql,sqlite,clickhouse数据库.</span></p> 
<p style="text-align:start">源码地址:<a href="https://gitee.com/chunanyong/zorm">https://gitee.com/chunanyong/zorm</a></p> 
<div style="text-align:start"> 
 <div> 
  <pre><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">go</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">get gitee.com/chunanyong/zorm </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></pre> 
 </div> 
</div> 
<ul> 
 <li>基于原生sql语句编写,是<a href="https://gitee.com/chunanyong/springrain">springrain</a>的精简和优化.</li> 
 <li><a href="https://gitee.com/zhou-a-xing/wsgt">自带代码生成器</a></li> 
 <li><span style="background-color:#ffffff; color:#40485b">代码精简,主体2500行,零依赖4000行,注释详细,方便定制修改</span></li> 
 <li><span style="color:#c0392b"><strong>支持事务传播,这是zorm诞生的主要原因</strong></span></li> 
 <li>支持mysql,postgresql,oracle,mssql,sqlite,<strong><span style="color:#c0392b">dm(达梦),kingbase(金仓),shentong(神通),gbase(南通),clickhouse</span></strong></li> 
 <li>支持多库和读写分离</li> 
 <li>更新性能zorm,gorm,xorm相当. 读取性能zorm比gorm,xorm快一倍</li> 
 <li>不支持联合主键,变通认为无主键,业务控制实现(艰难取舍)</li> 
 <li>集成seata-golang,支持全局托管,不修改业务代码,零侵入分布式事务</li> 
 <li>支持clickhouse,更新,删除语句使用SQL92标准语法.clickhouse-go官方驱动不支持批量insert语法,建议使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmailru%2Fgo-clickhouse" target="_blank">https://github.com/mailru/go-clickhouse</a></li> 
 <li>测试用例即文档: <a href="https://gitee.com/chunanyong/readygo/blob/master/test/testzorm/BaseDao_test.go">https://gitee.com/chunanyong/readygo/blob/master/test/testzorm/BaseDao_test.go</a></li> 
</ul> 
<p style="text-align:start">生产使用参考 <a href="https://gitee.com/chunanyong/readygo/tree/master/permission/permservice">UserStructService.go</a></p> 
<p style="text-align:start"><strong>更新:</strong></p> 
<ol> 
 <li style="text-align:start">完善文档,注释</li> 
 <li><span style="color:#000000">注释未使用的代码</span></li> 
 <li><span style="color:#000000">先判断error,再执行defer rows.Close()</span></li> 
 <li style="text-align:start">优化SQL提取的正则表达式</li> 
 <li><span style="color:#000000">增加社区支持微信号[</span><span style="color:#a31515">LAUV927</span><span style="color:#000000">](负责人是八块腹肌的单身小伙 @zhou-a-xing)</span></li> 
</ol>
                                        </div>
                                      
</div>
            