
---
title: 'zorm 1.5.4 发布，保平安'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8389'
author: 开源中国
comments: false
date: Fri, 24 Dec 2021 10:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8389'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">zorm是</span><span style="background-color:#ffffff; color:#40485b">go(golang)轻量级ORM,零依赖,零侵入分布式事务,支持达梦(dm),金仓(kingbase),神通(shentong),南大通用(gbase),mysql,postgresql,oracle,mssql,sqlite,clickhouse数据库.</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">源码地址:<a href="https://gitee.com/chunanyong/zorm">https://gitee.com/chunanyong/zorm</a></p> 
<div style="text-align:start"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">go</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">get gitee.com/chunanyong/zorm </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></pre> 
 </div> 
</div> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>基于原生sql语句编写,是<a href="https://gitee.com/chunanyong/springrain">springrain</a>的精简和优化.</li> 
 <li><a href="https://gitee.com/zhou-a-xing/wsgt">自带代码生成器</a></li> 
 <li><span style="background-color:#ffffff; color:#40485b">代码精简,主体2500行,零依赖4000行,注释详细,方便定制修改</span></li> 
 <li><span style="color:#c0392b"><strong>支持事务传播,这是zorm诞生的主要原因</strong></span></li> 
 <li>支持mysql,postgresql,oracle,mssql,sqlite,<strong><span style="color:#c0392b">dm(达梦),kingbase(金仓),shentong(神通),gbase(南通),clickhouse</span></strong></li> 
 <li>支持多库和读写分离</li> 
 <li>更新性能zorm,gorm,xorm相当. 读取性能zorm比gorm,xorm快50%</li> 
 <li>不支持联合主键,变通认为无主键,业务控制实现(艰难取舍)</li> 
 <li>集成seata-golang,支持全局托管,不修改业务代码,零侵入分布式事务</li> 
 <li>支持clickhouse,更新,删除语句使用SQL92标准语法.clickhouse-go官方驱动不支持批量insert语法,建议使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmailru%2Fgo-clickhouse" target="_blank">https://github.com/mailru/go-clickhouse</a></li> 
 <li>测试用例即文档: <a href="https://gitee.com/chunanyong/readygo/blob/master/test/testzorm/BaseDao_test.go">https://gitee.com/chunanyong/readygo/blob/master/test/testzorm/BaseDao_test.go</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">生产使用参考 <a href="https://gitee.com/chunanyong/readygo/tree/master/permission/permservice">UserStructService.go</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>更新:</strong></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li style="text-align:start">QueryRow如果查询一个字段,而且这个字段数据库为null,会有异常,没有赋为默认值</li> 
 <li>reflect.Type 类型的参数,修改为 *reflect.Type 指针,包括CustomDriverValueConver接口的参数</li> 
 <li style="text-align:start"> 
  <div> 
   <div>
    <span style="color:#000000">完善文档,注释</span>
   </div> 
  </div> </li> 
</ol> 
<p> </p>
                                        </div>
                                      
</div>
            