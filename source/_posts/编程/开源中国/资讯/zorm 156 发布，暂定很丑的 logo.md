
---
title: 'zorm 1.5.6 发布，暂定很丑的 logo'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b43253839b478bd3e367660e219cd77fdda.png'
author: 开源中国
comments: false
date: Tue, 12 Jul 2022 17:59:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b43253839b478bd3e367660e219cd77fdda.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="167" src="https://oscimg.oschina.net/oscnet/up-b43253839b478bd3e367660e219cd77fdda.png" width="150" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">zorm 是</span><span style="background-color:#ffffff; color:#40485b"><span> </span>go (golang) 轻量级 ORM, 零依赖，零侵入分布式事务，支持达梦 (dm), 金仓 (kingbase), 神通 (shentong), 南大通用 (gbase),mysql,postgresql,oracle,mssql,sqlite,clickhouse 数据库.</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">源码地址:<a href="https://gitee.com/chunanyong/zorm" target="_blank">https://gitee.com/chunanyong/zorm</a><br> 官网: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzorm.cn" target="_blank">https://zorm.cn</a></p> 
<div style="text-align:start"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">go</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">get gitee.com/chunanyong/zorm </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></pre> 
 </div> 
</div> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>基于原生 sql 语句编写，是<span> </span><a href="https://gitee.com/chunanyong/springrain">springrain</a><span> </span>的精简和优化.</li> 
 <li><a href="https://gitee.com/zhou-a-xing/wsgt">自带代码生成器</a></li> 
 <li><span style="background-color:#ffffff; color:#40485b">代码精简，主体 2500 行，零依赖 4000 行，注释详细，方便定制修改</span></li> 
 <li><span style="color:#c0392b"><strong>支持事务传播，这是 zorm 诞生的主要原因</strong></span></li> 
 <li>支持 mysql,postgresql,oracle,mssql,sqlite,<strong><span style="color:#c0392b">dm (达梦),kingbase (金仓),shentong (神通),gbase (南通),clickhouse</span></strong></li> 
 <li>支持多库和读写分离</li> 
 <li>更新性能 zorm,gorm,xorm 相当。读取性能 zorm 比 gorm,xorm 快 50%</li> 
 <li>不支持联合主键，变通认为无主键，业务控制实现 (艰难取舍)</li> 
 <li>集成 seata-golang, 支持全局托管，不修改业务代码，零侵入分布式事务</li> 
 <li>支持 clickhouse, 更新，删除语句使用 SQL92 标准语法.clickhouse-go 官方驱动不支持批量 insert 语法，建议使用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmailru%2Fgo-clickhouse" target="_blank">https://github.com/mailru/go-clickhouse</a></li> 
 <li>测试用例即文档: <a href="https://gitee.com/chunanyong/readygo/blob/master/test/testzorm/BaseDao_test.go">https://gitee.com/chunanyong/readygo/blob/master/test/testzorm/BaseDao_test.go</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">生产使用参考 <a href="https://gitee.com/chunanyong/readygo/tree/master/permission/permservice">UserStructService.go</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>更新:</strong></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> 
  <div> 
   <div>
    <span style="color:#000000">感谢@无泪发现Transaction方法返回值为nil的bug,已修复</span>
   </div> 
  </div> </li> 
 <li>感谢社区贡献,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzorm.cn" target="_blank">https://zorm.cn</a> 官网上线,很丑的logo上线 :)</li> 
 <li>支持已经存在的数据库连接</li> 
 <li>修改panic的异常记录和主键零值判断,用于支持基础类型扩展的主键</li> 
 <li><span style="color:#000000">完善文档，注释</span></li> 
</ol>
                                        </div>
                                      
</div>
            