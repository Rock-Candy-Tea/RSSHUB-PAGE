
---
title: 'Mozi.DataAccess 1.1.2 发布，ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7637'
author: 开源中国
comments: false
date: Tue, 31 May 2022 14:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7637'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Mozi.DataAccess是一个基于.Net开发的SQL ORM套件。框架的设计理念是：轻量，简洁，务实。目前文档还没有完善，今后会逐步完善文档。其中MSSQL的部分已经实战考验，可用性比较高。</p> 
<h2>目的和愿景</h2> 
<p>开发这个项目就是为了最大限度的降低学习和使用成本，减少项目重构成本，提高开发效率。ORM这个圈子本身是有很多成熟的优秀的框架，今年流行这个明年流行那个，常常使我们疲于学习。 无论框架怎么变，一个ORM框架的核心无非是：1，持久化；2，对象映射；3，数据库访问。在以上三点的基础上需要同时保证：1，易用且实用；2，充分解耦合重构成本低；3，性能损耗低。</p> 
<h2>特点</h2> 
<ol> 
 <li> <p>轻量化<br> 项目编译结果小，没有复杂的配置文件</p> </li> 
 <li> <p>可用性<br> 框架经过了长周期的项目考验</p> </li> 
 <li> <p>低耦合<br> 实现了业务逻辑和SQL的彻底分离，框架只专注于数据库的访问</p> </li> 
 <li> <p>可控性<br> 框架的使用最大限度的保留了SQL的原貌</p> </li> 
</ol> 
<h2>SQL表达式定义</h2> 
<div> 
 <div> 
  <pre><span><span>[&#123;</span></span>
<span><span></span><span>"name"</span><span>:</span><span> </span><span>"mz.createtableuser"</span><span>,</span></span>
<span><span></span><span>"command"</span><span>:</span><span> </span><span>"query"</span><span>,</span></span>
<span><span></span><span>"parameter"</span><span>:</span><span> </span><span>[</span><span> </span><span>],</span></span>
<span><span></span><span>"statement"</span><span>:</span><span> </span><span>"</span></span>
<span><span>IF NOT EXISTS(SELECT 1 FROM sysobjects WHERE id=object_id(</span><span>\'</span><span>$schema$.tbUsers</span><span>\'</span><span>) AND TYPE =</span><span>\'</span><span>U</span><span>\'</span><span>))</span></span>
<span><span>CREATE TABLE tbUsers</span></span>
<span><span>(</span></span>
<span><span>UserId   varchar(10) default </span><span>\'\'</span><span> not null ,</span></span>
<span><span>NickName varchar(100) default </span><span>\'\'</span><span> not null,</span></span>
<span><span>UserPwd  varchar(32) default </span><span>\'\'</span><span> not null,</span></span>
<span><span>RegDate  date not null,</span></span>
<span><span>Mobile   varchar(20) default </span><span>\'\'</span><span> not null,</span></span>
<span><span>IsForbidden int default 0 not null</span></span>
<span><span>CONSTRAINT PK_TBUSERS PRIMARY KEY (UserId)</span></span>
<span><span>)</span></span>
<span><span>"</span><span>,</span></span>
<span><span></span><span>"results"</span><span>:</span><span> </span><span>[</span><span> </span><span>],</span></span>
<span><span></span><span>"comment"</span><span>:</span><span> </span><span>"创建用户信息表"</span></span>
<span><span>&#125;,&#123;</span></span>
<span><span></span><span>"name"</span><span>:</span><span> </span><span>"mz.getuserinfo"</span><span>,</span></span>
<span><span></span><span>"command"</span><span>:</span><span> </span><span>"query"</span><span>,</span></span>
<span><span></span><span>"parameter"</span><span>:</span><span> </span><span>[</span><span> </span><span>"UserId"</span><span> </span><span>],</span></span>
<span><span></span><span>"statement"</span><span>:</span><span> </span><span>"select * from $schema$.tbUsers where UserId=#param.UserId# "</span><span>,</span></span>
<span><span></span><span>"results"</span><span>:</span><span> </span><span>[</span><span> </span><span>"UserId"</span><span>,</span><span> </span><span>"Nickname"</span><span> </span><span>],</span></span>
<span><span></span><span>"comment"</span><span>:</span><span> </span><span>"获取用户信息"</span></span>
<span><span>&#125;]</span><span>   </span></span>
</pre> 
 </div> 
</div> 
<p> </p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            