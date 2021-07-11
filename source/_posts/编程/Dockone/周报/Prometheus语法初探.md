
---
title: 'Prometheus语法初探'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/724d6173d4a1dc35db0426ebca3cf92b.png'
author: Dockone
comments: false
date: 2021-07-11 04:08:34
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/724d6173d4a1dc35db0426ebca3cf92b.png'
---

<div>   
<br><h3>概述</h3>Prometheus是一套使用Go语言进行编写的监控工具，专注于基础监控，默认仅保留15天的监控数据，15天的监控数据，已经足够运维人员去排查和分析运维故障。Prometheus有专门的PQL语言，可以对采集上来的指标进行多维度、函数分析，具有高度的指标定制化能力。本文将同大家一起学习Prometheus的PQL语法，验证并记录下过程。<br>
<h3>PQL重要概念</h3><h4>即时向量</h4>一个时间点某指标的值，如：<br>
<pre class="prettyprint">node_cpu_seconds_total&#123;mode="idle"&#125; <br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210711/724d6173d4a1dc35db0426ebca3cf92b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/724d6173d4a1dc35db0426ebca3cf92b.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>区间向量</h4>指的是在某段时间内metric的取值，每个时间点都包含一系列的值，如：<br>
<pre class="prettyprint">node_cpu_seconds_total&#123;mode="idle"&#125;[5m] <br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210711/03e01f6d38f7c7089cb682bc9a68a2c6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/03e01f6d38f7c7089cb682bc9a68a2c6.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>指标类型</h4><ul><li>Gauge，度量值，这个值是有变化的，如CPU使用率，有高有低</li><li>Counter，累计值，从程序开始，只增不减，如开机运行时长</li></ul><br>
<br><h4>标签</h4>一个指标，可以包括多个标签（label），用来指示这个指标的具体表示信息，起到对一个指标的修饰作用，标签可使用正则表达式进行匹配。<br>
<br>如node_cpu_seconds_total 指标，直接查询该指标，会打印出该指标的全部标签数据。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210711/3db554de6351d8fa60a25a786cd05f68.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/3db554de6351d8fa60a25a786cd05f68.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
拿关系型数据比较，可以这么类似比喻，node_cpu_seconds_total为表，cpu，instance，job，mode，value为其字段，表数据总为最新的数据，数据量总数等于各个字段的枚举值相乘。<br>
<br>当我们给这个Metric指标做了标签过滤时，相当于执行了where限制性语句，如node_cpu_seconds_total&#123;mode="idle"&#125;，只过滤出包含mode字段，并且其值为idle，类似于SQL语句。<br>
<pre class="prettyprint">select * from node_cpu_seconds_total where mode = 'idle'<br>
</pre><br>
标签支持正则表达式，使用=~(Rexp)，如node_cpu_seconds_total&#123;mode=\~"idle|iowait"&#125;，类似于SQL语句。<br>
<pre class="prettyprint">select * from node_cpu_seconds_total where mode = 'idle' or mode = 'iowait'<br>
</pre><br>
标签过滤器可以有多个，用逗号进行隔开，相当于执行了where … and … 语句，如node_cpu_seconds_total&#123;mode="idle",cpu='0'&#125;，类似于SQL语句。<br>
<pre class="prettyprint">select * from node_cpu_seconds_total where mode = 'idle' and cpu = '0'<br>
</pre><br>
配合标签，我们可以精确的找到我们需要用于展示或者计算的指标值。<br>
<h4>偏移量offset</h4>指标通过偏移量offset关键字，可以查询相对于当前时间点之前的数据，默认获取当前最新数据，如node_cpu_seconds_total offset 5m，获取5分钟前该指标的数据。<br>
<h4>注释</h4>PQL使用"#"对语法进行注释。<br>
<h4>函数</h4><strong>sum</strong><br>
<ul><li>sum函数可以对瞬时向量进行求和，如sum(node_cpu_seconds_total)，将统计所有值的总和。类似于select sum(value) from node_cpu_seconds_total</li><li>sum后面可以加 by 关键字，表示通过那个维度进行数据统计求和，如sum by (mode) (node_cpu_seconds_total) 类似于 select sum(vaule) from node_cpu_seconds_total group by mode</li></ul><br>
<br><strong>min</strong><br>
<ul><li>min函数可以对瞬时向量进行求最小值，min(node_cpu_seconds_total)。类似于select min(value) from node_cpu_seconds_total</li><li>同样，也支持by关键字，进行某个维度的求最小值</li></ul><br>
<br><strong>max</strong><br>
<ul><li>max函数可以对瞬时向量进行求最大值，max(node_cpu_seconds_total)。类似于select max(value) from node_cpu_seconds_total</li><li>同样，也支持by关键字，进行某个维度的求最大值</li></ul><br>
<br><strong>avg</strong><br>
<ul><li>avg函数可以对瞬时向量进行求平均avg(node_cpu_seconds_total)。类似于select avg(value) from node_cpu_seconds_total</li><li>同样，也支持by关键字，进行某个维度的求最均值</li></ul><br>
<br><strong>count</strong><br>
<ul><li>count函数可以对瞬时向量个数求总数，如count(node_cpu_seconds_total)类似于select count(*) from node_cpu_seconds_total</li><li>同样，也支持by关键字，进行某个维度的求最总个数</li></ul><br>
<br><strong>topk</strong><br>
<ul><li>topk函数可以对瞬时向量的值从大到小进行排列，并获取前N个值，需要传入两个参数，一个是N，一个是指标，如topk(5,node_cpu_seconds_total)，类似于select * from (select * from node_cpu_seconds_total order by value desc) where rownum<=5</li><li>同样，也支持by关键字，进行某个维度进行计算</li></ul><br>
<br><strong>bottomk</strong><br>
<ul><li>同topk相反，这里不再赘述。</li></ul><br>
<br><h4>计算</h4><strong>+ 加法运算</strong><br>
<ul><li>指标支持加法运算，一个即时向量，由于标签值不一致，所以会有多个值，这些值可以跟另外一个即时向量进行相加，这里的相加要保持一个原则，那就是需要具有同一个标签值的才会相加。node_cpu_seconds_total + node_cpu_seconds_total，这相当于所有值都多加一个原来的值，总体的值的数量是保持不变的。</li><li>相加的两个瞬时向量个数不一致情况：node_cpu_seconds_total和node_cpu_seconds_total&#123;mode="idle"&#125;，后者经过过滤后，数量上明显比第一个少，此时输出的结果个数同过滤后数量少的个数一致。</li><li>两个即时向量都不具备有同样的标签值情况：如node_cpu_seconds_total + node_memory_Active_bytes，此时由于没有任何一个值具有相同的标签值，所以结果为nodata，此时我们可以用ignoring关键字，对标签值进行忽略，使他们可以进行相加。由于node_cpu_seconds_total比node_memory_Active_bytes多了cpu和mode标签，所以node_cpu_seconds_total数量个数一般大于node_memory_Active_bytes个数，所以需要使用group_left，node_cpu_seconds_total + ignoring(cpu,mode) group_left node_memory_Active_bytes，结果集以左边的node_cpu_seconds_total个数为准，如果加号两个即时向量位置相反，则可以使用group_right，如node_memory_Active_bytes + ignoring(cpu,mode) group_right node_cpu_seconds_total</li></ul><br>
<br><strong>- 减法运算</strong><br>
<ul><li>类似加法运算</li></ul><br>
<br>** * 乘法运算 **<br>
<ul><li>类似加法运算</li></ul><br>
<br><strong>/ 除法运算</strong><br>
<ul><li>类似加法运算</li></ul><br>
<br><h4>逻辑比较</h4><strong>== 判断是否相等</strong><br>
<ul><li>==用于判断左右两边的值是否相等，如果相等则为1（true），如果不等则为0（false），如node_cpu_seconds_total ==BOOL 0 判断是否有存在0值</li></ul><br>
<br><strong>!= 判断是否不等</strong><br>
<ul><li>类似==</li></ul><br>
<br><strong>>= 大于等于</strong><br>
<ul><li>>=用于判断左边的值是否大于或等于右边的值，如果满足，则为1（true），如果不满足则为0（false）</li></ul><br>
<br><strong><=小于等于</strong><br>
<ul><li>类似大于等于</li></ul><br>
<br><strong>> 大于</strong><br>
<ul><li>类似大于等于</li></ul><br>
<br><strong>< 小于</strong><br>
<ul><li>类似大于等于</li></ul><br>
<br><h4>数据集操作</h4><strong>and</strong><br>
<br>对多个指标的数据集进行标签判断，获取两个指标集具有共同的标签的值node_cpu_seconds_total and node_cpu_guest_seconds_total，类似sql select * from node_cpu_seconds_total a,node_cpu_guest_seconds_total b where a.cpu = b.cpu and a.instance = b.instance and a.job=b.job and a.mode = b.mode<br>
<br><strong>or</strong><br>
<br>对多个指标集数据进行展示，如果有标签重复，则仅显示其中一个标签的值。<br>
<br><strong>unless</strong><br>
<br>对多个指标的数据集进行标签判断，获取两个指标集不具有共同的标签的值，结果集以最左边为准，如 node_memory_Active_bytes unless node_cpu_seconds_total 和 node_cpu_seconds_total unless node_memory_Active_bytes结果是不一样的。<br>
<h3>函数</h3><h4>用于即时向量的函数</h4><strong>abs</strong><br>
<ul><li>abs返回即时向量的绝对值</li></ul><br>
<br><strong>absent</strong><br>
<ul><li>absent用于检测即时向量中，某个标签是否存在，如果不存在，则value为1，如检查标签为node_arp_entries&#123;instance=“localhost:9100”&#125;是否存在有元素，如果存在则返回nodata，如果不存在value则为1</li><li>常用于检测指标是否丢失。</li></ul><br>
<br><strong>ceil</strong><br>
<ul><li>用于将浮点数向上化为最接近的一个整数，如值为0.1，则为向上取整，成为1。</li></ul><br>
<br><strong>floor</strong><br>
<ul><li>用于将浮点数向下化为最接近的一个整数，如值为0.1，则为向下取整，成为0。</li></ul><br>
<br><strong>clamp_max</strong><br>
<ul><li>该函数需要两个参数，一个是向量，另外一个是封顶值，如果一个向量的值超过该封顶值，该向量的值则为封顶值。</li></ul><br>
<br><strong>clamp_min</strong><br>
<ul><li>该函数需要两个参数，一个是向量，另外一个是触底值，如果一个向量的值超过该触底值，该向量的值则为触底值。</li></ul><br>
<br><h4>用于区间向量的函数</h4>区间向量的函数执行完成后，便成为了即时向量。<br>
<br><strong>absent_over_time</strong><br>
<ul><li>absent_over_time用于检测在给定的区间向量中，是否存在有元素，如果没有则value为1。</li></ul><br>
<br><strong>changes</strong><br>
<ul><li>返回给定的区间向量中，对比于当前值，发生变化的元素的数量</li></ul><br>
<br><strong>delta</strong><br>
<ul><li>返回区间向量中，第一个元素和最后一个元素之间的变化值，时间区间也参与算法计算，所以即时第一个元素和最后一个元素均为整数，该值也未必是整数。</li><li>须作用在gauge类型的指标</li></ul><br>
<br><strong>deriv</strong><br>
<ul><li>返回区间向量中，满足线性规律的每秒变化值</li><li>须作用在gauge类型的指标</li></ul><br>
<br><strong>idelta</strong><br>
<ul><li>该函数计算区间向量间，最后两个元素的差值，如果区间内没有两个元素，则返回nodata</li><li>须作用在gauge类型的指标</li></ul><br>
<br><strong>irate</strong><br>
<ul><li>该函数计算区间向量间，最后两个元素的差值，并且除以区间的秒数，如果区间内没有两个元素，则返回nodata</li></ul><br>
<br><strong><aggregation>_over_time</strong><br>
<ul><li>该函数技术按区间向量的最大（max）、最小（min）、平均（avg）、求和（sum）、求总数（）等汇聚值。</li></ul><br>
<br>原文链接：<a href="https://blog.csdn.net/xiaojinran/article/details/112398797" rel="nofollow" target="_blank">https://blog.csdn.net/xiaojinr ... 98797</a>，作者：xiaojinran
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            