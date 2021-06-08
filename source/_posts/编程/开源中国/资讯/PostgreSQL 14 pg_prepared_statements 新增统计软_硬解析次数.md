
---
title: 'PostgreSQL 14 pg_prepared_statements 新增统计软_硬解析次数'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b386ca79b78342d7185c9f02202e2948a6b.png'
author: 开源中国
comments: false
date: Tue, 08 Jun 2021 15:08:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b386ca79b78342d7185c9f02202e2948a6b.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PostgreSQL 中 prepare statement 可以用来 cache plan，用来减少 plan 的次数。</p> 
<p>默认是前 5 次调用生成 custom plan，然后生成 generic plan。</p> 
<p><img alt height="337" src="https://oscimg.oschina.net/oscnet/up-b386ca79b78342d7185c9f02202e2948a6b.png" width="969" referrerpolicy="no-referrer"></p> 
<p>PG14 中在 pg_prepared_statements 视图中新增了 generic_plans 和 custom_plans 两列，用来统计 generic plan 和 custom plan 的次数。</p> 
<pre><code>bill@bill=>PREPARE pr1 AS SELECT * FROM pg_class WHERE
bill-# relname = $1;
PREPARE
bill@bill=>EXECUTE  pr1('t1');
bill@bill=>select * from pg_prepared_statements;
 name |                    statement                     |         prepare_time          | parameter_types | from_sql | generic_plans | custom_plans
------+--------------------------------------------------+-------------------------------+-----------------+----------+---------------+--------------
 pr1  | PREPARE pr1 AS SELECT * FROM pg_class WHERE     +| 2021-05-13 10:17:28.429238+08 | &#123;name&#125;          | t        |             0 |            1
      | relname = $1;                                    |                               |                 |          |               |
(1 row)</code></pre> 
<p>执行多次后再查看：</p> 
<pre><code>bill@bill=>select * from pg_prepared_statements;
-[ RECORD 1 ]---+-------------------------------------------------
name            | pr1
statement       | PREPARE pr1 AS SELECT * FROM pg_class WHERE     +
                | relname = $1;
prepare_time    | 2021-05-13 10:17:28.429238+08
parameter_types | &#123;name&#125;
from_sql        | t
generic_plans   | 2
custom_plans    | 5</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            