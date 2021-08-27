
---
title: 'Weed3 v3.3.21 发布，微型 ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6323'
author: 开源中国
comments: false
date: Fri, 27 Aug 2021 11:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6323'
---

<div>   
<div class="content">
                                                                                            <p>Weed3 v3.3.21 已经发布，微型 ORM 框架。</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li>增加 WeedConfig.isSelectItemEmptyAsNull 配置项</li> 
 <li>修复 MapperBase update(item, bool, wq) 数据没进去的 bug</li> 
 <li>条件器的 Iterable 改为 Iterable 类型</li> 
 <li>增加新接口 db.mapperBase(clz,tableName);</li> 
</ul> 
<p>微型ORM框架（支持：java sql，xml sql，annotation sql，template sql；事务；缓存；监控；等...）</p> 
<h4>Weed3 特点和理念：</h4> 
<ul> 
 <li>跨平台：可以嵌入到JVM脚本引擎（js, groovy, lua, python, ruby）及GraalVM支持的部分语言。</li> 
 <li>很小巧：0.1Mb（且是功能完整，方案丰富；可极大简化数据库开发）。</li> 
 <li>有个性：不喜欢反射、不喜欢配置...（除了连接，不需要任何配置）。</li> 
 <li>其它的：支持缓存控制和跨数据库事务（算是分布式事务的一种吧）。</li> 
</ul> 
<h4>核心对象和功能：</h4> 
<ul> 
 <li>上下文：DbContext db</li> 
 <li>四个接口：db.mapper(), db.table(), db.call(), db.sql()</li> 
</ul> 
<pre>//BaseMapper 接口
db.mapperBase(User.class).selectById(1);

//BaseMapper 接口，条件查询
db.mapperBase(User.class).selectList(mq->mq.whereLt(User::getGroup,1).andEq(User::getLabel,"T"));


//Table 接口
db.table("user u")
  .innerJoin("user_ext e").onEq("u.id","e.user_id")
  .whereEq("u.type",11)
  .limit(100,20)
  .selectList("u.*,e.sex,e.label", User.class);

//Table 接口，拼装条件查询（特别适合管理后台）
db.table(logger)
  .where("1 = 1")
  .andIf(TextUtils.isNotEmpty(trace_id), "trace_id = ?", trace_id)
  .andIf(TextUtils.isNotEmpty(tag), "tag = ?", tag)
  .andIf(TextUtils.isNotEmpty(tag1), "tag1 = ?", tag1)
  .andIf(TextUtils.isNotEmpty(tag2), "tag2 = ?", tag2)
  .andIf(TextUtils.isNotEmpty(tag3), "tag3 = ?", tag3)
  .andIf(log_date > 0, "log_date = ?", log_date)
  .andIf(log_id > 0, "log_id <= ?", log_id)
  .andIf(level > 0, "level=?", level)
  .orderBy("log_fulltime desc")
  .limit(size)
  .selectList("*", LogModel.class);</pre> 
<h4>详情查看：<a href="https://gitee.com/noear/weed3/releases/v3.3.21">https://gitee.com/noear/weed3/releases/v3.3.21</a></h4>
                                        </div>
                                      
</div>
            