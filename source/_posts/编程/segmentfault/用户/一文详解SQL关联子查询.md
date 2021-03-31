
---
title: '一文详解SQL关联子查询'
categories: 
 - 编程
 - segmentfault
 - 用户
headimg: 'https://segmentfault.com/img/remote/1460000039740751'
author: segmentfault
comments: false
date: 2021-03-31 04:10:03
thumbnail: 'https://segmentfault.com/img/remote/1460000039740751'
---

<div>   
<p><strong>简介：</strong> 本文主要介绍什么是关联子查询以及如何将关联子查询改写为普通语义的sql查询。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740751" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span><br>本文主要介绍什么是关联子查询以及如何将关联子查询改写为普通语义的sql查询。</p><p>在背景介绍中我们将讲讲常见的关联子查询的语义，关联子查询语法的好处以及其执行时对数据库系统的挑战。第二章中我们将主要介绍如何将关联子查询改写为普通的查询的形式，也就是解关联。第三章中我们会介绍解关联中的优化方法。</p><h3>一 背景介绍</h3><p>关联子查询是指和外部查询有关联的子查询，具体来说就是在这个子查询里使用了外部查询包含的列。</p><p>因为这种可以使用关联列的灵活性，将sql查询写成子查询的形式往往可以极大的简化sql以及使得sql查询的语义更加方便理解。下面我们通过使用tpch schema来举几个例子以说明这一点。tpch schema是一个典型的订单系统的database，包含customer表，orders表，lineitem表等，如下图：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740752" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>假如我们希望查询出“所有从来没有下过单的客户的信息”，那么我们可以将关联子查询作为过滤条件。使用关联子查询写出的sql如下。可以看到这里的not exists子查询使用列外部的列c_custkey。</p><pre><code>-- 所有从来没有下过单的客户的信息
select c_custkey
from
 customer where
  not exists (
    select
      *
    from
      orders
    where
      o_custkey = c_custkey
  )</code></pre><p>如果不写成上面的形式，我们则需要考虑将customer和orders两个表先进行left join，然后再过滤掉没有join上的行，同时我们还需要markorder的每一行，使得本来就是null的那些。查询sql如下：</p><pre><code>-- 所有从来没有下过单的客户的信息
select c_custkey
from
  customer
  left join (
    select
      distinct o_custkey
    from
      orders
  ) on o_custkey = c_custkey
where
  o_custkey is null</code></pre><p>从这个简单的例子中就可以看到使用关联子查询降低了sql编写的难度，同时提高了可读性。</p><p>除了在exists/in子查询中使用关联列，关联子查询还可以出现在where中作为过滤条件需要的值。比如tpch q17中使用子查询求出一个聚合值作为过滤条件。</p><pre><code>-- tpch q17
SELECT Sum(l1.extendedprice) / 7.0 AS avg_yearly 
FROM   lineitem l1, 
       part p
WHERE  p.partkey = l1.partkey 
       AND p.brand = 'Brand#44' 
       AND p.container = 'WRAP PKG' 
       AND l1.quantity < (SELECT 0.2 * Avg(l2.quantity) 
                         FROM   lineitem l2
                         WHERE  l2.partkey = p.partkey);</code></pre><p>除了出现在where里面，关联子查询可以出现在任何允许出现单行(scalar)的地方，比如select列表里。如果我们需要做报表汇总一些customer的信息，希望对每一个customer查询他们的订单总额，我们可以使用下面包含关联子查询的sql。</p><pre><code>-- 客户以及对应的消费总额
select
  c_custkey,
  (
    select sum(o_totalprice)
    from
      orders
    where o_custkey = c_custkey 
    ）
from
  customer</code></pre><p>更复杂一些的比如，我们希望查询每一个customer及其对应的在某个日期前已经签收的订单总额。利用关联子查询只需要做一些小的改变如下：</p><pre><code>select
  c_custkey,
  (
    select
      sum(o_totalprice)
    from
      orders
    where
      o_custkey = c_custkey
      and '2020-05-27' > (
        select
          max(l_receiptdate)
        from
          lineitem
        where
          l_orderkey = o_orderkey
      ) 
    ）
from
   customer</code></pre><p>看了这些例子，相信大家都已经感受到使用关联子查询带来的便捷。但是同时关联子查询也带来了执行上的挑战。为了计算关联结果的值（子查询的输出），需要iterative的执行方式。</p><p>以之前讨论过的tpch 17为例子：</p><pre><code>SELECT Sum(l1.extendedprice) / 7.0 AS avg_yearly 
FROM   lineitem l1, 
       part p
WHERE  p.partkey = l1.partkey 
       AND p.brand = 'Brand#44' 
       AND p.container = 'WRAP PKG' 
       AND l1.quantity < (SELECT 0.2 * Avg(l2.quantity) 
                         FROM   lineitem l2
                         WHERE  l2.partkey = p.partkey);</code></pre><p>这里的子查询部分使用了外部查询的列 p.partkey。</p><pre><code>SELECT 0.2 * Avg(l2.quantity) 
FROM   lineitem l2
WHERE  l2.partkey = p.partkey  -- p.partkey是外部查询的列</code></pre><p>优化器将这个查询表示为如下图的逻辑树：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740739" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>如果数据库系统不支持查看逻辑树，可以通过explain命令查看物理计划，一般输出如下图：</p><pre><code>+---------------+
| Plan Details  |
+---------------+
 1- Output[avg_yearly] avg_yearly := expr
 2    -> Project[] expr := (`sum` / DOUBLE '7.0')
 3        - Aggregate sum := `sum`(`extendedprice`)
 4            -> Filter[p.`partkey` = l1.`partkey` AND `brand` = 'Brand#51' AND `container` = 'WRAP PACK' AND `quantity` < `result`]
 5                - CorrelatedJoin[[p.`partkey`]]
 6                    - CrossJoin
 7                        - TableScan[tpch:lineitem l1]
 8                        - TableScan[tpch:part p]
 9                    - Scalar
10                        -> Project[] result := (DOUBLE '0.2' * `avg`)
11                            - Aggregate avg := `avg`(`quantity`)
12                                -> Filter[(p.`partkey` = l2`partkey`)] 
13                                    - TableScan[tpch:lineitem l2]</code></pre><p>我们将这个连接外部查询和子查询的算子叫做CorrelatedJoin(也被称之为lateral join, dependent join等等。它的左子树我们称之为外部查询(input)，右子树称之为子查询(subquery)。子查询中出现的外部的列叫做关联列。在栗子中关联列为p.partkey。</p><p>例子中对应的逻辑计划和相关定义如下图所示，explain返回结果中第6-8行为外部查询，9-13行为子查询，关联部位在子查询中第12行的filter。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740760" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>这个算子的输出等价于一种iterative的执行的结果。也就将左子树的每一行关联列的值带入到右子树中进行计算并返回一行结果。有些类似将子查询看成一个user defined function（udf），外部查询的关联列的值作为这个udf的输入参数。需要注意的是，我们需要子查询是确定的，也就是对同样值的关联列，每次运行子查询返回的结果应该是确定的。</p><p>在上图的栗子中，如果外部查询有一行的p.partkey的值为25，那么这一行对应的correlatedjoin的输出就是下面这个查询的结果：</p><pre><code>-- p.partkey = 25 时对应的子查询为
SELECT 0.2 * Avg(l2.quantity) 
FROM   lineitem l2
WHERE  l2.partkey = 25</code></pre><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740741" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span><br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740749" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>需要注意的是，如果计算结果为空集，则返回一行null。而如果运行中子查询返回了超过一行的结果，应该报运行时错误。在逻辑计划里，用enforcesinglerow这个node来约束。</p><p>从上面的介绍中可以发现，CorrelatedJoin这个算子打破了以往对逻辑树自上而下的执行模式。普通的逻辑树都是从叶子节点往根结点执行的，但是CorreltedJoin的右子树会被带入左子树的行的值反复的执行。</p><p>correlatedjoinnode的输出就是在外部查询的结果上增加了一列，但是可以看到这种iterative的执行方式的复杂度和将外部查询和子查询关联产生之前的那部分树进行cross join的复杂度相同。</p><p>同时，这样iterative的执行方式对分布式数据库系统来说是很大的挑战。因为需要修改执行时调度的逻辑。而且我们可以看到，这样的执行方式如果不进行结果的缓存，会进行很多重复结果的计算。</p><p>传统的优化器的优化规则没有特别的针对Correlatedjoin node进行处理，为了支持关联子查询的这种iterative的形式，在优化器初始阶段就会把Correlatedjoin进行等价转换，转换过后的逻辑树用join，aggregation等普通算子来进行关联子查询结果的计算。这个过程被称为解关联（decorrelation/unnesting）。下面一章我们主要介绍常见的解关联的方式。</p><h3>二 常见的解关联方式</h3><p>为了方便起见，我们在这一章只讨论scalar关联子查询，就是会输出一列值的关联子查询。</p><p>在讨论如何解关联之前，我们总结一下关联子查询的输出有以下特点：</p><ul><li>correlated join算子的计算结果为在外部查询上增加一列。</li><li>增加的那一列的结果为将外部查询关联列的值带入子查询计算得出的。当计算结果超过一行则报错，计算结果为空则补充null。</li><li>不同于join算子，correlated join不改变外部查询的其他列（不少行也不膨胀）。</li></ul><p>解开关联的关键在于使得子查询获得对应的外部查询的行的值。</p><p>表现在计划上，就是将correleted join算子向右下推到产生关联的部位的下面。当correlated join算子的左右子树没有关联列的时候，correlated join算子就可以转换成join算子。这样子查询就通过和外部查询join的方式获得了关联列的值，从而可以自上而下计算，回到原本的计算方式。如下图，下图中rest subquery为在关联产生部位之前的子查询部分。当correlated join 推到产生关联的部位之下，就可以转换为普通的join了。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740742" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>correlated join推过的那些算子都是需要进行改写，以保持等价性（上图的栗子中subquery变为了subquery’）。</p><h4>1 下推规则</h4><p>论文Orthogonal Optimization of Subqueries and Aggregation[2]给出了将correlatedjoin_算子下推到其他算子（filter，project，aggregation，union 等）下面的的等价转换规则。但是文中的correlatedjoin_算子是会过滤外部查询的行数的，类似于inner join（论文中称为 ）。我们这里讨论更加general的类似于left join的 correlatedjoin (论文中称为 )，并讨论如果要保证外部查询行数不被过滤需要做哪些改写。</p><p>由于篇幅限制，下面我们只介绍下推到filter，project，aggregation算子下面的等价规则。</p><p>为了简单起见，我们在逻辑树中去掉了enforcesinglerow。</p><p><strong>转换1 无关联时转换为join</strong></p><p>回顾前文所说，correlated join算子的左子树为input，右子树为subquery。当correlated join的左右子树没有关联的时候，这个时候对外部查询的每一行，子查询的结果都是相同的。</p><p>我们就可以把correlated join转换成普通的没有join criteria的leftjoin算子。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740740" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><blockquote>注：需要在subquery上添加enforcesinglerow来保证join语义和correlatedjoin相同（不会造成input的膨胀）。</blockquote><p><strong>转换2 简单关联条件时转换为join</strong></p><p>当correlated join右子树中最上面的节点为一个关联filter而他的下面无关联时，可以直接将这个filter放到left join的条件中，也可以理解为filter上提。如下图：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740757" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p><strong>转换3 下推穿过filter</strong></p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740750" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>论文中correlatedjoin*可以直接推过filter。如果需要下推的为correlatedjoin，则需要对filter进行改写，改写成带有case when的project。当subquery的行不满足filter的条件时应输出null。</p><p><strong>转换4 下推穿过project</strong></p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740743" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>correlated join下推过project，需要在project中添加input的输出列。</p><p><strong>转换5 下推穿过aggregation</strong></p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740746" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>correlated join下推到带有group by的aggregation时，需要对aggregation进行改写。</p><p>改写为在aggregation的group by的列中增加外部查询的全部列。这里要求外部查询一定有key，如果没有则需要生成临时的key。生成可以的算子在图中为assignuniqueid算子。</p><p>如果aggregation为全局的，那么还需要进行额外的处理。如下图：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740745" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>correlated join下推到全局aggregation的时候，需要对aggregation增加input的列(以及key)作为group by的列。这个下推规则还需要一个前提，那就是aggregation函数需要满足满足特性 agg(Ø)=agg(null) 。这个的意思就是aggragtion函数需要对空集和对null的计算结果是相同的。</p><blockquote>注：在mysql和AnalyticDB for MySQL（阿里云自研的云原生数据仓库[1]，兼容mysql语法，下文简称ADB）的语法里，sum, avg等都不满足这个特性。空集的平均值为0, 而对包含null值的任意集合取平均值结果为null不为0。所以需要mark子查询里的每一行，对空集进行特别的处理，在这里就不展开解释了。</blockquote><p>论文Orthogonal Optimization of Subqueries and Aggregation[2]反复运用上面这些规则进行correlatedjoin的下推，直到correlatedjoin可以转换为普通的join。</p><p>带入之前的tpch q17的栗子中，我们先使用将correlated join推到子查询中的project下面，查询变为：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740747" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>然后下推穿过这个agg，并改写这个agg，如下图：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740744" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>这里我们忽略 avg(Ø)!=avg(null) 。如果考虑这个情况，则需要mark子查询全部的行，在correlated join之后根据子查询的结果结合mark的值对空集进行特别处理（将mark了的行的值从null变为0）。感兴趣的读者可以参考下一张中q17的最终计划。</p><p>接着直接调用之前的规则2，上提这个filter。这样这个查询就变为普通的没有关联的查询了。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740748" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><h4>2 结果复用</h4><p>回顾上一节所说，子查询的查询结果是带入每一行关联列的值之后计算得出的，那么显而易见相同值的关联列带入子查询中计算出的结果是完全相同的。在上面的栗子中，对同样的p.partkey，correlatedjoin输出的子查询的结果是相等的。如下图中外部查询partkey为25的话产生的关联子查询时是完全相同的，那么结果也自然相同。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740754" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>15年Newmann的论文Unnesting Arbitrary Queries[3]介绍了一种方法就是先对外部查询里关联列取distinct，再将correlated join返回的值和原本的外部查询根据关联列进行left join，如下图所示：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740753" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>这里的not distinct join的条件对应mysql里面的<=>，null<=>null的结果为true，是可以join到一起的。</p><p>带入到之前的例子中如下图所示，对外部查询的关联列partkey先进行distinct，然后带入子查询计算结果，最后再通过join将对应的结果接到原本的外部查询上。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740756" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>如果进行了上述转换，那么我们可以认为新的input的关联列永远是distinct的。而现在的correlatedjoin*算子可以允许input的列被过滤。这样做的好处除了对于相同的列不进行重复的子查询的计算之外，主要还有下面两个：</p><ul><li>新的外部查询是永远有key的，因为distinct过了。</li><li>correlatedjoin*算子由于过滤外部查询的列，所以它的下推更为简单（不需要assignuniqueid，不需要保留全部行）。</li></ul><p>进行上述的转换后，紧接着再套用之前的等价下推规则，我们又可以将correlatedjoin*下推到一个左右子树没有关联的地方，从而改写为inner join。</p><p>如果按照Unnesting Arbitrary Queries[3]的方法进行解关联，需要将input的一部分结果进行复用，这个复用需要执行引擎的支持。需要注意的是，当系统不支持复用的时候，我们需要执行两次input的子树（如下图），这个时候就需要input这颗子树的结果是deterministic的，否则无法用这个方法进行解关联。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740755" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><h3>三 关联子查询的优化</h3><p>在ADB的优化器中，逻辑计划会根据每一条转换规则进行匹配和转换，也就意味着在关联解开之后不需要关心解关联产生的计划的效率而将它直接交给后续的优化规则。但是现实并不是那么的美好，因为后续规则不够完备，以及解关联之后丢失了外部查询和子查询之间的关系，我们希望在解关联的时候就将计划尽可能优化。</p><h4>1 exists/in/filter关联子查询</h4><p>在之前的章节中为了简化，我们只讨论了scalar子查询。因为exists/in这些子查询都可以改写成scalar子查询。比如将exists改写为count(*) > 0</p><p>但是可以看到，如果子查询的返回结果被用来过滤外部查询的行，实际上会简化整个解关联的过程。所以我们对exists/in这样的子查询进行特殊处理，在语法解析时就进行区分。在解关联的过程中，如果可以使用semijoin/antijoin算子进行解关联则直接解开关联，否则后续会转化成scalar子查询也就是correlatedjoin的形式。</p><h4>2 关联条件的上提</h4><p>看到这里会发现，随着correlatedjoin的下推，这个逻辑树会变得更加复杂，所以我们在下推之前会在子查询内部进行关联算子的上提。当这个逻辑就是产生关联的算子越高，correlatedjoin就可以早点推到关联部位的下面。比如下面这个查询：</p><pre><code>SELECT t1.c2
FROM
  t1
WHERE t1.c2 < (
    SELECT 0.2 * max(t2.x)
    FROM
      t2
    WHERE t2.c1 = t2.c1
   GROUP BY t2.c1
  );</code></pre><p>这里由于t2.c1 = t2.c1可以推到agg 上面(因为对于子查询这是一个在group by列上的条件)，我们就可以进行下面的转换。先把关联的filter上提（有时需要改写），这样就只要把correlatedjoin推过filter，调用转换2就可以了。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740758" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>更具体的例子就是前文提到的tpch q17。这里的scalar子查询作用在过滤条件中的情况也可以进行进一步改写。</p><p>下图为按照之前说的理论下推correlated join并改写为left join之后的逻辑计划。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740761" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span><br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740764" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span><br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740767" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>而由于这个scalar子查询是作为filter条件的，这种情况下子查询没有结果返回为null对应的外部查询是一定会被过滤掉的。所以correlatedjoin可以直接转为 correlatedjoin*，再加上将filter进行上提，我们可以得到下面的计划。这样改写的好处是可以在join前先进行agg(early agg)。坏处就是如果不小心处理，很容易造成语义不等价造成count bug。</p><h4>3 代价相关的子查询优化</h4><p><strong>利用window算子解关联</strong></p><p>回顾到目前为止我们讲的这些，是不是印象最深刻的在于correlatedjoin算子是在外部查询上增加一列。而他的这个行为和window算子类似。window算子的语义就是不改变输入的行数，只是在每一行上增加一个在window的frame里计算出的值。所以我们可以利用window算子进行解关联，如果感兴趣可以参考这两篇论文Enhanced Subquery Optimizations in Oracle[4]和 WinMagic : Subquery Elimination Using Window Aggregation[5]。</p><p>window解关联的改写就是在外部查询包含子查询中全部的表和条件时，可以直接使用window将子查询的结果拼接到外部查询上。他好处是节约了很多tablescan。比如说tpch q2。可以进行下面的改写：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740759" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>这里之所能改写成window是因为外部查询包含了内部查询全部的表和条件。而且agg函数min也满足特性agg(Ø)=agg(null) （如果不满足，需要对行进行mark以及用case when 改写输出）。</p><p>可以看到改写后tablescan的数量大大减少。更进一步，优化器后面的优化规则会进行根据primarykey的信息以及agg函数的特性进行join 和 window的顺序交换从而进一步减少window算子输入的数据量（filter-join pushdown）。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740765" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>这些好处很多文章里都说了。我们在这里讨论一下这样改写的不好的地方：</p><ul><li>比如在pk未能显示提供/agg的函数对duplicates敏感的情况下，window算子会阻挡filter-join的下推，从而打断了joingraph造成join的中间结果变大。</li><li>如果改写为两棵子树的join，filter-join可以下推到其中一颗子树上。而进行window改写后，filter-join无法下推。</li><li>在pipeline的执行模型下/&使用cte的情况下，扫表获得的收益有限。</li><li>传统优化器对join&agg的优化处理/优化规则比对window好/丰富很多。</li></ul><p>综上所述，什么时候使用window进行改写关联子查询需要进行收益和代价的估计。</p><p><strong>CorrelatedJoin在外部查询中的下推</strong></p><p>在将correlatedJoin往子查询方向下推之前，我们会将correlatedjoin先在外部查询中进行下推(比如推过cross join等)。</p><p>这样做是因为correlatedJoin永远不会造成数据的膨胀，所以理论上应该早点做。但实际上correlatejoin下推后也可能切割joingraph，从而造成和window改写差不多的问题。</p><h4>4 等价列的利用</h4><p>如果在子查询中存在和外部等价的列，那么可以先用这个列改写子查询中的关联列减少关联的地方从而简化查询。下面举一个简单的例子。</p><pre><code>Select t1.c2
From
  t1
Where
  t1.c3 < (
    Select min(t2.c3)
    From t2
    Where t1.c1 = t2.c1
   group by t1.c1
  )
  
-- 在子查询中使用t2.c1 代替 t1.ct进行简化

Select t1.c2
From
  t1
Where
  t1.c3 < (
    Select min(t2.c3)
    From t2
    Where t1.c1 = t2.c1
   group by t2.c1
  )</code></pre><h4>5 子查询相关的优化规则</h4><p>一个方面correaltedjoin这个算子的特性给了我们一些进行优化的信息。下面举一些例子：</p><ol><li>经过correaltedjoin算子之后的行数与左子树的行数相同。</li><li>enforcesinglerow的输出为1行。</li><li>外部查询的关联列决定(function dependency)correaltedjoin的新增的输出列。</li><li>assignuniqueid产生的key具备unique的属性等，可用于之后化简aggregation和group by等。</li><li>子查询里的sort可以被裁剪。</li></ol><p>另一个方面，在子查询的改写中，可以通过属性推导进行子查询的化简。比如：</p><ol><li>如果原本外部查询就是unique的则没有别要增加uniqueid列。</li><li>enforcesinglerow的子节点的输出如果永远为1行则可以进行裁剪。</li><li>关联列在project上的子查询，如下图，在一些情况下改写为exists子查询。</li></ol><pre><code>select t1.orderkey,
  (
    select
      min(t1.orderkey)
    from
      orders t2
    where
      t2.orderkey > t1.orderkey
  )
from
  orders t1
order by
  1</code></pre><h4>6 需要注意的地方</h4><p>子查询解关联中最需要注意的地方就是两个地方，一个是确保仅对外部查询进行加一列的操作，一个是对null值的处理。</p><p><strong>计数错误</strong></p><p>文献中常提到的是一个经典的解关联容易出错的地方。比如下面的查询，我们有一个前提条件就是t1.c3全都是小于0的。在这个情况下子查询参与的关联条件应该是没有任何过滤度的。而改写成inner join则会过滤掉一些行。语义上是不等价的。</p><pre><code>Select t1.c2
From
  t1
Where
  t1.c3 < (
    Select COUNT (*)
    From t2
    Where t1.c1 = t2.c1
  )</code></pre><p><strong>分布式下的leftmarkjoin</strong></p><p>另一个容易出错的地方是论文Unnesting Arbitrary Queries[3]中的LeftMarkJoin，其输出的结果与in的语义相同。简单来说就是下面这个查询的结果。</p><pre><code>select t1.c1 
    in ( select
      t2.c1
    from
      t2)
from
  t1</code></pre><p>这个查询对应的逻辑计划如下：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740762" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>其输出结果为在左子树结果上加一列in的结果，in的结果有三种可能true,false和null。</p><p>在分布式环境下，对这个算子进行repartition和落盘很容易造成和null值相关的计算出错。</p><p>举一个简单的例子，当leftmarkjoin为repartition的执行方式时，会对左表和右表的数据根据c1的hash值进行重分布reshuffle。那么t1.c1中为null的行会被shuffle到同一台executor上。这个时候假如右表没有数据被shuffle到这台机器上，那么这一台executor并不知道对于null的这些行该输出null还是false。因为null in空集的结果为false，而null in 任何非空集合的结果为null。此时这台executor并不知道右表是否为空。</p><p><strong>解开关联后的效率</strong></p><p>在最开始的时候我们提到了iterative的执行方式，这里我们需要说明对有些关联子查询来说即使关联被解开为join/agg等算子，计算查询结果也需要一个cross join的代价。</p><p>比如下面这个两个查询， 第一个是我们常见的关联子查询的样子，可以转换成inner join + early agg的形式。而第二个解开关联后则会变成一个left join on非等值条件（代价同cross join）。</p><pre><code>-- sql 1
SELECT t1.c1
  FROM t1
 WHERE t1.c2 > ( 
   SELECT min(t2.c2) 
     FROM t2 
    WHERE t2.c1 = t1.c1
   );

-- sql 2
SELECT t1.c1
  FROM t1
 WHERE t1.c2 > ( 
   SELECT min(t2.c2) 
     FROM t2 
    WHERE t2.c1 > t1.c1
   );</code></pre><p>sq1解开关联后的计划如下：<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740763" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>sql2解开关联后的计划如下：<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740766" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>对于sql1来说，从语义上理解，外部查询的每一行带入子查询里扫过的行都是没有重叠的，所以代价和innerjoin on等值条件是一样的。再加上同样的外部行对应的子查询中min的结果相同可以应用early agg从而可以进一步优化。</p><p>对于sql2来说，从语义上理解，外部查询的每一行都必须要带入子查询中扫过所有的行才能判断在满足t2.c1 > t1.c1这个条件下的子查询的输出应该是什么。为了计算出结果这个代价是无法通过优化节约的。但是对同样的t1.c1输出始终是相同的，Unnesting Arbitrary Queries[3]中的结果复用仍然可以产生优化。</p><blockquote>参考文献<br>[1] <a href="https://www.aliyun.com/product/ApsaraDB/ads" rel="nofollow">https://www.aliyun.com/product/ApsaraDB/ads</a><br>[2] Galindo-Legaria，César和Milind Joshi。“子查询和聚合的正交优化。” ACM SIGMOD记录30.2（2001）：571-581。<br>[3] Neumann，Thomas和Alfons Kemper。“取消嵌套任意查询。” 商业，技术和网络数据库系统（BTW 2015）（2015年）。<br>[4]贝拉姆康达（Bellamkonda），斯里坎特（Srikanth）等。“增强了Oracle中的子查询优化。” VLDB基金会论文集2.2（2009）：1366-1377<br>[5] Zuzarte，Calisto等人。“ Winmagic：使用窗口聚合消除子查询。” 2003 ACM SIGMOD国际数据管理国际会议论文集。2003。<br>[6] Neumann，Thomas，Viktor Leis和Alfons Kemper。“联接的完整故事（inHyPer）。” 商业，技术和网络数据库系统（BTW 2017）（2017）。<br>[7]加利福尼亚州加林多-莱加里亚（Galindo-Legaria），参数化查询和嵌套等效项。技术报告，Microsoft，2001年。MSR-TR-2000-31，2000年。<p><a href="https://developer.aliyun.com/article/783124?utm_content=g_1000257748" rel="nofollow">原文链接</a><br>本文为阿里云原创内容，未经允许不得转载。</p></blockquote>  
</div>
            