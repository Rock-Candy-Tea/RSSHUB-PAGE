
---
title: 'PostgreSQL 14 pageinspect 新增 gist 索引支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5045'
author: 开源中国
comments: false
date: Fri, 04 Jun 2021 18:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5045'
---

<div>   
<div class="content">
                                                                    
                                                        <p>pageinspect插件可以用来查看表和索引的内部结构，但并不是所有的索引类型都支持，PG14中增加了三个函数用来支持对gist索引的支持。</p> 
<p>function gist_page_items(bytea,regclass)<br> function gist_page_items_bytea(bytea)<br> function gist_page_opaque_info(bytea)</p> 
<p>例子：</p> 
<p>创建测试表和索引：</p> 
<pre><code>bill@bill=>CREATE TABLE test_gist AS SELECT point(i,i) p, i::text t FROM
bill-#      generate_series(1,1000) i;
SELECT 1000
bill@bill=> CREATE INDEX test_gist_idx ON test_gist USING gist (p);
CREATE INDEX</code></pre> 
<p>使用pageinspect观察gist索引结构：</p> 
<pre><code>bill@bill=> SELECT * FROM gist_page_opaque_info(get_raw_page('test_gist_idx', 0));
 lsn | nsn | rightlink  | flags
-----+-----+------------+-------
 0/1 | 0/0 | 4294967295 | &#123;&#125;
(1 row)
bill@bill=> SELECT * FROM gist_page_opaque_info(get_raw_page('test_gist_idx', 1));
 lsn | nsn | rightlink  | flags
-----+-----+------------+--------
 0/1 | 0/0 | 4294967295 | &#123;leaf&#125;
(1 row)
bill@bill=> SELECT * FROM gist_page_opaque_info(get_raw_page('test_gist_idx', 2));
 lsn | nsn | rightlink | flags
-----+-----+-----------+--------
 0/1 | 0/0 |         1 | &#123;leaf&#125;
(1 row)
bill@bill=> SELECT * FROM gist_page_items(get_raw_page('test_gist_idx', 0), 'test_gist_idx');
 itemoffset |   ctid    | itemlen | dead |       keys
------------+-----------+---------+------+-------------------
          1 | (1,65535) |      40 | f    | (p)=((166,166))
          2 | (2,65535) |      40 | f    | (p)=((332,332))
          3 | (3,65535) |      40 | f    | (p)=((498,498))
          4 | (4,65535) |      40 | f    | (p)=((664,664))
          5 | (5,65535) |      40 | f    | (p)=((830,830))
          6 | (6,65535) |      40 | f    | (p)=((996,996))
          7 | (7,65535) |      40 | f    | (p)=((1000,1000))
(7 rows)
bill@bill=> SELECT * FROM gist_page_items(get_raw_page('test_gist_idx', 1), 'test_gist_idx') LIMIT 5;
 itemoffset | ctid  | itemlen | dead |    keys
------------+-------+---------+------+-------------
          1 | (0,1) |      40 | f    | (p)=((1,1))
          2 | (0,2) |      40 | f    | (p)=((2,2))
          3 | (0,3) |      40 | f    | (p)=((3,3))
          4 | (0,4) |      40 | f    | (p)=((4,4))
          5 | (0,5) |      40 | f    | (p)=((5,5))
(5 rows)
bill@bill=> SELECT * FROM gist_page_items(get_raw_page('test_gist_idx', 2), 'test_gist_idx') LIMIT 5;
 itemoffset |  ctid  | itemlen | dead |      keys
------------+--------+---------+------+-----------------
          1 | (1,10) |      40 | f    | (p)=((167,167))
          2 | (1,11) |      40 | f    | (p)=((168,168))
          3 | (1,12) |      40 | f    | (p)=((169,169))
          4 | (1,13) |      40 | f    | (p)=((170,170))
          5 | (1,14) |      40 | f    | (p)=((171,171))
(5 rows)
bill@bill=> SELECT * FROM gist_page_items_bytea(get_raw_page('test_gist_idx', 0));
 itemoffset |   ctid    | itemlen | dead |                                      key_data
------------+-----------+---------+------+------------------------------------------------------------------------------------
          1 | (1,65535) |      40 | f    | \x00000100ffff28000000000000c064400000000000c06440000000000000f03f000000000000f03f
          2 | (2,65535) |      40 | f    | \x00000200ffff28000000000000c074400000000000c074400000000000e064400000000000e06440
          3 | (3,65535) |      40 | f    | \x00000300ffff28000000000000207f400000000000207f400000000000d074400000000000d07440
          4 | (4,65535) |      40 | f    | \x00000400ffff28000000000000c084400000000000c084400000000000307f400000000000307f40
          5 | (5,65535) |      40 | f    | \x00000500ffff28000000000000f089400000000000f089400000000000c884400000000000c88440
          6 | (6,65535) |      40 | f    | \x00000600ffff28000000000000208f400000000000208f400000000000f889400000000000f88940
          7 | (7,65535) |      40 | f    | \x00000700ffff28000000000000408f400000000000408f400000000000288f400000000000288f40
(7 rows)
bill@bill=> SELECT * FROM gist_page_items_bytea(get_raw_page('test_gist_idx', 1)) LIMIT 5;
 itemoffset | ctid  | itemlen | dead |                                      key_data
------------+-------+---------+------+------------------------------------------------------------------------------------
          1 | (0,1) |      40 | f    | \x0000000001002800000000000000f03f000000000000f03f000000000000f03f000000000000f03f
          2 | (0,2) |      40 | f    | \x00000000020028000000000000000040000000000000004000000000000000400000000000000040
          3 | (0,3) |      40 | f    | \x00000000030028000000000000000840000000000000084000000000000008400000000000000840
          4 | (0,4) |      40 | f    | \x00000000040028000000000000001040000000000000104000000000000010400000000000001040
          5 | (0,5) |      40 | f    | \x00000000050028000000000000001440000000000000144000000000000014400000000000001440
(5 rows)
bill@bill=> SELECT * FROM gist_page_items_bytea(get_raw_page('test_gist_idx', 2)) LIMIT 5;
 itemoffset |  ctid  | itemlen | dead |                                      key_data
------------+--------+---------+------+------------------------------------------------------------------------------------
          1 | (1,10) |      40 | f    | \x000001000a0028000000000000e064400000000000e064400000000000e064400000000000e06440
          2 | (1,11) |      40 | f    | \x000001000b0028000000000000006540000000000000654000000000000065400000000000006540
          3 | (1,12) |      40 | f    | \x000001000c0028000000000000206540000000000020654000000000002065400000000000206540
          4 | (1,13) |      40 | f    | \x000001000d0028000000000000406540000000000040654000000000004065400000000000406540
          5 | (1,14) |      40 | f    | \x000001000e0028000000000000606540000000000060654000000000006065400000000000606540
(5 rows)</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            