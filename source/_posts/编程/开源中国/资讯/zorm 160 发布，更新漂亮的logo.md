
---
title: 'zorm 1.6.0 发布，更新漂亮的logo'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2402'
author: 开源中国
comments: false
date: Mon, 29 Aug 2022 10:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2402'
---

<div>   
<div class="content">
                                                                                            <p><span>Go轻量ORM,零依赖,零侵入分布式事务,支持达梦(dm),金仓(kingbase),神通(shentong),南通(gbase),TDengine,mysql,postgresql,oracle,mssql,sqlite,db2,clickhouse数据库.</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">源码地址:<a href="https://gitee.com/chunanyong/zorm" target="_blank">https://gitee.com/chunanyong/zorm</a><br> 官网:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzorm.cn" target="_blank">https://zorm.cn</a><br> 测试用例 <a href="https://gitee.com/wuxiangege/zorm-examples" target="_blank">zorm-examples</a></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>基于原生 sql 语句，是<span> </span><a href="https://gitee.com/chunanyong/springrain">springrain</a><span> </span>的精简和优化.</li> 
 <li><a href="https://gitee.com/zhou-a-xing/wsgt">自带代码生成器</a></li> 
 <li><span style="background-color:#ffffff; color:#40485b">代码精简，主体 2500 行，零依赖 4000 行，注释详细，方便定制修改</span></li> 
 <li><span style="color:#c0392b"><strong>支持事务传播，这是 zorm 诞生的主要原因</strong></span></li> 
 <li>支持 mysql,postgresql,oracle,mssql,sqlite,db2,<strong><span style="color:#c0392b">dm (达梦),kingbase (金仓),shentong (神通),gbase (南通),TDengine,clickhouse</span></strong></li> 
 <li>支持多库和读写分离</li> 
 <li>更新性能 zorm,gorm,xorm 相当。读取性能 zorm 比 gorm,xorm 快 50%</li> 
 <li>不支持联合主键，变通认为无主键，业务控制实现 (艰难取舍)</li> 
 <li>集成 seata-golang,hptx,dbpack 支持全局托管，不修改业务代码，零侵入分布式事务</li> 
 <li>支持 clickhouse, 更新，删除语句使用 SQL92 标准语法.clickhouse-go 官方驱动不支持批量 insert 语法，建议使用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmailru%2Fgo-clickhouse" target="_blank">https://github.com/mailru/go-clickhouse</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>更新:</strong></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> 
  <div> 
   <div> 
    <div> 
     <div>
      <span style="color:#000000">更新漂亮的logo</span>
     </div> 
    </div> 
   </div> 
  </div> </li> 
 <li> 
  <div> 
   <div> 
    <div> 
     <div>
      <span style="color:#000000">增加db2数据支持,依赖Limit分页语法</span>
     </div> 
    </div> 
   </div> 
  </div> </li> 
 <li> 
  <div> 
   <div> 
    <div> 
     <div>
      <span style="color:#000000">DBType即将废弃,更名为Dialect,方便gorm和xorm迁移</span>
     </div> 
    </div> 
   </div> 
  </div> </li> 
 <li> 
  <div>
   <span style="color:#000000">FuncReadWriteStrategy和GetGTXID函数增加error返回值</span>
  </div> </li> 
 <li> 
  <div>
   <span style="color:#000000">修改日志格式,统一加上 -> 符号</span>
  </div> </li> 
 <li> 
  <div> 
   <div> 
    <div>
     <span style="color:#000000">曾经偷的懒还是还上吧,类型转换加上err返回值.去掉无用的日期格式转换,驱动获取的并不是[]byte</span>
    </div> 
   </div> 
  </div> </li> 
 <li> 
  <div> 
   <div> 
    <div>
     <span style="color:#000000">修复Finder.Append和GetSQL为nil的bug</span>
    </div> 
   </div> 
  </div> </li> 
 <li><span style="color:#000000">完善文档，注释</span></li> 
</ol>
                                        </div>
                                      
</div>
            