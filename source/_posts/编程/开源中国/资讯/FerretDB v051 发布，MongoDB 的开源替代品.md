
---
title: 'FerretDB v0.5.1 发布，MongoDB 的开源替代品'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5533'
author: 开源中国
comments: false
date: Thu, 28 Jul 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5533'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <div> 
   <p style="margin-left:0px">FerretDB（以前被称为 MangoDB）的成立是为了成为 MongoDB 的开源替代品。FerretDB 是一个开源代理，将 MongoDB wire protocol 查询转换为 SQL —— 使用 PostgreSQL 作为数据库引擎。</p> 
   <p style="margin-left:0px">目前 FerretDB 已发布 0.5.1 版本，带来如下变更：</p> 
   <h3><strong>新功能</strong></h3> 
   <ul> 
    <li>验证数据库名称 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F913" target="_blank">#913</a></li> 
    <li>支持 <code>$all</code> 数组查询运算符 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F724" target="_blank">#724</a></li> 
    <li>支持 <code>getLog</code> 诊断命令 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F711" target="_blank">#711</a></li> 
    <li>为 <span style="color:#24292f">Tigris </span>实现 <code>MsgCount</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F928" target="_blank">#928</a></li> 
    <li>支持<code>explain</code>诊断命令 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F909" target="_blank">#909</a></li> 
   </ul> 
   <p><strong>Bug 修复</strong></p> 
   <ul> 
    <li>修复 drop 和 dropDatabase 处理程序中的边缘情况 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F891" target="_blank">#891</a> </li> 
    <li>修复 ModifyCount 以更新运算符 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F939" target="_blank">#939</a> </li> 
   </ul> 
   <p><strong>增强</strong></p> 
   <ul> 
    <li>支持数组类型的 gt lt 运算符比较 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F819" target="_blank">#819</a></li> 
    <li>优化文档获取/过滤 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F808" target="_blank">#808</a></li> 
    <li>为数据库名称边框大小写添加测试 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F921" target="_blank">#921</a></li> 
   </ul> 
   <p>更多内容请查看更新公告： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Freleases%2Ftag%2Fv0.5.1" target="_blank">https://github.com/FerretDB/FerretDB/releases/tag/v0.5.1</a></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            