
---
title: 'fastmybatis 2.3.0 发布，mybatis 开发利器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4250'
author: 开源中国
comments: false
date: Wed, 08 Jun 2022 09:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4250'
---

<div>   
<div class="content">
                                                                                            <p>fastmybatis 2.3.0 发布，本次更新内容如下：</p> 
<pre><span style="color:#cc7832">- </span>listByCollection,listByArray,listByIds<span>当</span>value<span>为空直接返回空结果
</span><span style="color:#cc7832">- </span><span>新增子条件查询
</span><span style="color:#cc7832">- </span><span>新增</span>or<span>条件查询
</span><span style="color:#cc7832">- </span>mapper<span>新增</span>getMap<span>方法，将查询结果转换成</span>Map<span>对象
</span><span style="color:#cc7832">- </span>saveBatch<span>批量插入返回主键值</span></pre> 
<p style="color:#a9b7c6; text-align:start"><span style="color:#000000">or条件查询示例：</span></p> 
<pre style="text-align:start"><code class="language-java"><span><span style="color:#808080">// WHERE id = ? OR username = ?</span></span>
<span>Query query = <span style="color:#cc7832">new</span> Query()</span>
<span>    .eq(<span style="color:#6a8759">"id"</span><span style="color:#cc7832">,</span> <span style="color:#6897bb">6</span>)</span>
<span>    .orEq(<span style="color:#6a8759">"username"</span><span style="color:#cc7832">,</span> <span style="color:#6a8759">"jim"</span>)<span style="color:#cc7832">;</span></span></code></pre> 
<p><span style="color:#000000">子条件查询示例：</span></p> 
<pre style="text-align:start"><code class="language-java"><span><span style="color:#808080">// WHERE (id = ? OR id between ? and ?) AND ( money > ? OR state = ? )</span></span>
<span>Query query = <span style="color:#cc7832">new</span> Query()</span>
<span>    .and(q -> q.eq(<span style="color:#6a8759">"id"</span><span style="color:#cc7832">,</span> <span style="color:#6897bb">3</span>).orBetween(<span style="color:#6a8759">"id"</span><span style="color:#cc7832">,</span> <span style="color:#6897bb">4</span><span style="color:#cc7832">,</span> <span style="color:#6897bb">10</span>))</span>
<span>    .and(q -> q.gt(<span style="color:#6a8759">"money"</span><span style="color:#cc7832">,</span> <span style="color:#6897bb">1</span>).orEq(<span style="color:#6a8759">"state"</span><span style="color:#cc7832">,</span> <span style="color:#6897bb">1</span>))<span style="color:#cc7832">;</span></span>

<span><span style="color:#808080">// WHERE ( id = ? AND username = ? ) OR ( money > ? AND state = ? )</span></span>
<span>Query query = <span style="color:#cc7832">new</span> Query()</span>
<span>    .and(q -> q.eq(<span style="color:#6a8759">"id"</span><span style="color:#cc7832">,</span> <span style="color:#6897bb">3</span>).eq(<span style="color:#6a8759">"username"</span><span style="color:#cc7832">,</span> <span style="color:#6a8759">"jim"</span>))</span>
<span>    .or(q -> q.gt(<span style="color:#6a8759">"money"</span><span style="color:#cc7832">,</span> <span style="color:#6897bb">1</span>).eq(<span style="color:#6a8759">"state"</span><span style="color:#cc7832">,</span> <span style="color:#6897bb">1</span>))<span style="color:#cc7832">;</span></span>
</code></pre> 
<p style="color:#a9b7c6; text-align:start"><span style="color:#000000">getMap方法示例：</span></p> 
<pre style="text-align:start"><code class="language-java"><span>Query query = <span style="color:#cc7832">new</span> Query()</span>
<span>        .ge(<span style="color:#6a8759">"id"</span><span style="color:#cc7832">,</span> <span style="color:#6897bb">1</span>)<span style="color:#cc7832">;</span></span>

<span><span style="color:#808080">// 查询Map，主键id作为key，行记录作为value，方便通过主键id获取某条记录</span></span>
<span><span style="color:#808080">// id -> TUser</span></span>
<span>Map<Integer<span style="color:#cc7832">,</span> TUser> map = mapper.getMap(query<span style="color:#cc7832">,</span> TUser::getId)<span style="color:#cc7832">;</span></span>
<span>System.out.println(map.get(<span style="color:#6897bb">6</span>))<span style="color:#cc7832">;</span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>关于 fastmybatis</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">fastmybatis 是一个 mybatis 开发框架，其宗旨为：简单、快速、有效。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>零配置快速上手，无需依赖 Spring</li> 
 <li>无需编写 xml 文件即可完成增删改查操作</li> 
 <li>支持 mysql、sqlserver、oracle、postgresql、sqlite</li> 
 <li>支持自定义 sql，对于基本的增删改查不需要写 SQL，对于其它特殊 SQL（如统计 SQL）可写在 xml 中</li> 
 <li>支持与 spring-boot 集成，依赖 starter 即可</li> 
 <li>支持插件编写</li> 
 <li>支持 ActiveRecord 模式</li> 
 <li>支持多租户</li> 
 <li>提供通用 Service</li> 
 <li>API 丰富，多达 40 + 方法，满足日常开发需求。</li> 
 <li>轻量级，无侵入性，是官方 mybatis 的一种扩展</li> 
</ul>
                                        </div>
                                      
</div>
            