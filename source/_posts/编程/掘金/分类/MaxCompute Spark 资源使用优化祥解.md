
---
title: 'MaxCompute Spark 资源使用优化祥解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/738925ca5a6a41a4aafcbf960f8c089b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 18:14:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/738925ca5a6a41a4aafcbf960f8c089b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>简介：</strong> 本文主要讲解MaxCompute Spark资源调优，目的在于在保证Spark任务正常运行的前提下，指导用户更好地对Spark作业资源使用进行优化，极大化利用资源，降低成本。</p>
<p>本文作者：吴数傑 阿里云智能 开发工程师</p>
<h1 data-id="heading-0">1. 概述</h1>
<p>本文主要讲解MaxCompute Spark资源调优，目的在于在保证Spark任务正常运行的前提下，指导用户更好地对Spark作业资源使用进行优化，极大化利用资源，降低成本。</p>
<h1 data-id="heading-1">2. Sensor</h1>
<ul>
<li>Sensor提供了一种可视化的方式监控运行中的Spark进程，每个worker（Executor）及master（Driver）都具有各自的状态监控图，可以通过Logview中找到入口，如下图所示：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/738925ca5a6a41a4aafcbf960f8c089b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>打开Sensor之后，可以看到下图提供了Driver/Executor在其生命周期内的CPU和内存的使用情况：</p>
</li>
<li>
<p>cpu_plan/mem_plan（蓝线）代表了用户申请的CPU和内存计划量</p>
</li>
<li>
<p>用户可以直观地从cpu_usage图中看出任务运行中的CPU利用率</p>
</li>
<li>
<p>mem_usage代表了任务运行中的内存使用，是mem_rss和page cache两项之和，详见下文</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af98ceab07aa4249a7fa88be918c3e88~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>Memory Metrics</p>
</li>
<li>
<p>mem_rss 代表了进程所占用了常驻内存，这部分内存也就是Spark任务运行所使用的实际内存，通常需要用户关注，如果该内存超过用户申请的内存量，就可能会发生OOM，导致Driver/Executor进程终止。此外，该曲线也可以用于指导用户进行内存优化，如果实际使用量远远小于用户申请量，则可以减少内存申请，极大化利用资源，降低成本。</p>
</li>
<li>
<p>mem_cache（page_cache）用于将磁盘中的数据缓存到内存中，从而减少磁盘I/O操作，通常由系统进行管理，如果物理机内存充足，那么mem_cache可能会使用很多，用户可以不必关心该内存的分配和回收。</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e69aa94244545d2a3f412573b574049~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">3. 资源参数调优</h1>
<p><strong>（1）Executor Cores</strong></p>
<p>相关参数：spark.executor.cores</p>
<ul>
<li>每个Executor的核数，即每个Executor中的可同时运行的task数目</li>
<li>Spark任务的最大并行度是num-executors * executor-cores</li>
<li>Spark任务执行的时候，一个CPU core同一时间最多只能执行一个Task。如果CPU core数量比较充足，通常来说，可以比较快速和高效地执行完这些Task。同时也要注意，每个Executor的内存是多个Task共享的，如果单个Executor核数太多，内存过少，那么也很可能发生OOM。</li>
</ul>
<p><strong>（2）Executor Num</strong></p>
<p>相关参数：spark.executor.instances</p>
<ul>
<li>该参数用于设置Spark作业总共要用多少个Executor进程来执行</li>
<li>通常用户可以根据任务复杂度来决定到底需要申请多少个Executor</li>
</ul>
<p>此外，需要注意，如果出现Executor磁盘空间不足，或者部分Executor OOM的问题，可以通过减少单个Executor的cores数，增加Executor的instances数量来保证任务总体并行度不变，同时降低任务失败的风险。</p>
<p><strong>（3）Executor Memory</strong></p>
<p>相关参数：spark.executor.memory</p>
<ul>
<li>该参数用于设置每个Executor进程的内存。Executor内存的大小，很多时候直接决定了Spark作业的性能，而且JVM OOM在Executor中更为常见。</li>
</ul>
<p>相关参数2：spark.executor.memoryOverhead</p>
<ul>
<li>设置申请Executor的堆外内存，主要用于JVM自身，字符串, NIO Buffer等开销，注意memoryOverhead 这部分内存并不是用来进行计算的，用户代码及spark都无法直接操作。</li>
<li>如果不设置该值，那么默认为spark.executor.memory * 0.10，最小为384 MB</li>
</ul>
<p>Executor 内存不足的表现形式：</p>
<ul>
<li>在Executor的日志（Logview->某个Worker->StdErr）中出现Cannot allocate memory</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/903f68c11ebe46c9967ef9015d0d9fa7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在任务结束的Logview result的第一行中出现：The job has been killed by "OOM Killer", please check your job's memory usage.</li>
<li>在Sensor中发现内存使用率非常高</li>
<li>在Executor的日志中出现java.lang.OutOfMemoryError: Java heap space</li>
<li>在Executor的日志中出现GC overhead limit exceeded</li>
<li>Spark UI中发现频繁的GC信息</li>
<li>可能出现OOM的间接表现形式：部分Executor出现No route to host: workerd********* / Could not find CoarseGrainedScheduler等错误</li>
</ul>
<p>可能原因及解决方案：</p>
<ul>
<li>限制executor 并行度，将cores 调小：多个同时运行的 Task 会共享一个Executor 的内存，使得单个 Task 可使用的内存减少，调小并行度能缓解内存压力增加单个Executor内存</li>
<li>增加分区数量，减少每个executor负载</li>
<li>考虑数据倾斜问题，因为数据倾斜导致某个 task 内存不足，其它 task 内存足够</li>
<li>如果出现了上文所述的Cannot allocate memory或The job has been killed by "OOM Killer", please check your job's memory usage，这种情况通常是由于系统内存不足，可以适当增加一些堆外内存来缓解内存压力，通常设置spark.executor.memoryOverhead为1g/2g就足够了</li>
</ul>
<p><strong>（4）Driver Cores</strong></p>
<p>相关参数spark.driver.cores</p>
<ul>
<li>通常Driver Cores不需要太大，但是如果任务较为复杂（如Stage及Task数量过多）或者Executor数量过多（Driver需要与每个Executor通信并保持心跳），在Sensor中看到Cpu利用率非常高，那么可能需要适当调大Driver Cores</li>
</ul>
<p>另外要注意，在Yarn-Cluster模式运行Spark任务，不能直接在代码中设置Driver的资源配置（core/memory），因为在JVM启动时就需要该参数，因此需要通过--driver-memory命令行选项或在spark-defaults.conf文件/Dataworks配置项中进行设置。</p>
<p><strong>（5）Driver Memory</strong></p>
<p>相关参数1：spark.driver.memory</p>
<ul>
<li>设置申请Driver的堆内内存，与executor类似</li>
</ul>
<p>相关参数2：spark.driver.maxResultSize</p>
<ul>
<li>代表每个Spark的action（例如collect）的结果总大小的限制，默认为1g。如果总大小超过此限制，作业将被中止，如果该值较高可能会导致Driver发生OOM，因此用户需要根据作业实际情况设置适当值。</li>
</ul>
<p>相关参数3：spark.driver.memoryOverhead</p>
<ul>
<li>
<p>设置申请Driver的堆外内存，与executor类似</p>
</li>
<li>
<p>Driver的内存通常不需要太大，如果Driver出现内存不足，通常是由于Driver收集了过多的数据，如果需要使用collect算子将RDD的数据全部拉取到Driver上进行处理，那么必须确保Driver的内存足够大。</p>
</li>
</ul>
<p>表现形式：</p>
<ul>
<li>Spark应用程序无响应或者直接停止</li>
<li>在Driver的日志（Logview->Master->StdErr）中发现了Driver OutOfMemory的错误</li>
<li>Spark UI中发现频繁的GC信息</li>
<li>在Sensor中发现内存使用率非常高</li>
<li>在Driver的日志中出现Cannot allocate memory</li>
</ul>
<p>可能原因及解决方案：</p>
<ul>
<li>代码可能使用了collect操作将过大的数据集收集到Driver节点</li>
<li>在代码创建了过大的数组，或者加载过大的数据集到Driver进程汇总</li>
<li>SparkContext，DAGScheduler都是运行在Driver端的。对应rdd的Stage切分也是在Driver端运行，如果用户自己写的程序有过多的步骤，切分出过多的Stage，这部分信息消耗的是Driver的内存，这个时候就需要调大Driver的内存。有时候如果stage过多，Driver端甚至会有栈溢出</li>
</ul>
<p><strong>（6）本地磁盘空间</strong></p>
<p>相关参数：spark.hadoop.odps.cupid.disk.driver.device_size：</p>
<ul>
<li>该参数代表为单个Driver或Executor申请的磁盘空间大小，默认值为20g，最大支持100g</li>
<li>Shuffle数据以及BlockManager溢出的数据均存储在磁盘上</li>
</ul>
<p>磁盘空间不足的表现形式：</p>
<p>在Executor/Driver的日志中发现了No space left on device错误</p>
<p>解决方案：</p>
<p>最简单的方法是直接增加更多的磁盘空间，调大spark.hadoop.odps.cupid.disk.driver.device_size。</p>
<p>如果增加到100g之后依然出现该错误，可能是由于存在数据倾斜，shuffle或者cache过程中数据集中分布在某些block，也可能是单个Executor的shuffle数据量确实过大，可以尝试：</p>
<ul>
<li>对数据重分区，解决数据倾斜问题</li>
<li>缩小单个Executor的任务并发spark.executor.cores</li>
<li>缩小读表并发spark.hadoop.odps.input.split.size</li>
<li>增加executor的数量spark.executor.instances</li>
</ul>
<p>需要注意：</p>
<ul>
<li>同样由于在JVM启动前就需要挂载磁盘，因此该参数必须配置在spark-defaults.conf文件或者dataworks的配置项中，不能配置在用户代码中</li>
<li>此外需要注意该参数的单位为g，不能省略g</li>
<li>很多时候由于用户配置位置有误或者没有带单位g，导致参数实际并没有生效，任务运行依然失败</li>
</ul>
<h1 data-id="heading-3">4. 总结</h1>
<p>上文主要介绍了MaxCompute Spark在使用过程中可能遇到的资源不足的问题及相应的解决思路，为了能够最大化利用资源，首先建议按照1: 4的比例来申请单个worker资源，即1 core: 4 gb memory，如果出现OOM，那么需要查看日志及Sensor对问题进行初步定位，再进行相应的优化和资源调整。不建议单个Executor Cores 设置过多，通常单个Executor在2-8 core是相对安全的，如果超过8，那么建议增加instance数量。适当增加堆外内存（为系统预留一些内存资源）也是一个常用的调优方法，通常在实践中可以解决很多OOM的问题。最后，用户可以参考官方文档<a href="https://link.juejin.cn/?target=https%3A%2F%2Fspark.apache.org%2Fdocs%2F2.4.5%2Ftuning.html%25EF%25BC%258C%25E5%258C%2585%25E5%2590%25AB%25E6%259B%25B4%25E5%25A4%259A%25E7%259A%2584%25E5%2586%2585%25E5%25AD%2598%25E8%25B0%2583%25E4%25BC%2598%25E6%258A%2580%25E5%25B7%25A7%25EF%25BC%258C%25E5%25A6%2582gc%25E4%25BC%2598%25E5%258C%2596%25EF%25BC%258C%25E6%2595%25B0%25E6%258D%25AE%25E5%25BA%258F%25E5%2588%2597%25E5%258C%2596%25E7%25AD%2589%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://spark.apache.org/docs/2.4.5/tuning.html%EF%BC%8C%E5%8C%85%E5%90%AB%E6%9B%B4%E5%A4%9A%E7%9A%84%E5%86%85%E5%AD%98%E8%B0%83%E4%BC%98%E6%8A%80%E5%B7%A7%EF%BC%8C%E5%A6%82gc%E4%BC%98%E5%8C%96%EF%BC%8C%E6%95%B0%E6%8D%AE%E5%BA%8F%E5%88%97%E5%8C%96%E7%AD%89%E3%80%82" ref="nofollow noopener noreferrer">spark.apache.org/docs/2.4.5/…</a></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000285451%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000285451/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            