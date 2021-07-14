
---
title: 'MaxCompute中如何通过logview诊断慢作业'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80a03f814d8246c3bc75a484fa7b4d23~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 19:26:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80a03f814d8246c3bc75a484fa7b4d23~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>简介：</strong> MaxCompute致力于批量结构化数据的存储和计算，提供海量数据仓库的解决方案及分析建模服务，在MaxCompute执行sql任务的时候有时候作业会很慢，本文通过查看logview排查具体任务慢的原因</p>
<p>在这里把任务跑的慢的问题划分为以下几类</p>
<ol>
<li>资源不足导致的排队(一般是包年包月项目)</li>
<li>数据倾斜，数据膨胀</li>
<li>用户自身逻辑导致的运行效率低下</li>
</ol>
<h1 data-id="heading-0">一、资源不足</h1>
<p>一般的SQL任务会占用CPU、Memory这两个维度的资源，logview如何查看参考链接</p>
<p><strong>1.1 查看作业耗时和执行的阶段</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80a03f814d8246c3bc75a484fa7b4d23~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.2 提交任务的等待</strong></p>
<p>如果提交任务以后一直显示“Job Queueing...”则有可能是由于其他人的任务占用了资源组的资源，使得自己的任务在排队。</p>
<p>在SubStatusHistory中看Waiting for scheduling就是等待的时间</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4aefbc52fb6488a94fee895d1034b8c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.3 任务提交后的资源不足</strong></p>
<p>这里还有另一种情况，虽然任务可以提交成功，但是由于所需的资源较大，当前的资源组不能同时启动所有的实例，导致出现了任务虽然有进度，但是执行并不快的情况。这种可以通过logview中的latency chart功能观察到。latency chart可以在detail中点击相应的task看到</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d4b32ef2f59465e86de755e52197632~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图显示的是一个资源充足的任务运行状态，可以看到蓝色部分的下端都是平齐的，表示几乎在同一时间启动了所有的实例。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a64f1f522277470ab429fbeb5467f0dd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而这个图形的下端呈现阶梯向上的形态，表示任务的实例是一点一点的调度起来的，运行任务时资源并不充足。如果任务的重要性较高，可以考虑增加资源，或者调高任务的优先级。</p>
<p><strong>1.4资源不足的原因</strong></p>
<p>1.通过cu管家查看cu是否占满，点到对应的任务点，找到对应时间看作业提交的情况</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c2856b36c58492cb3adf7f94831e453~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>按cpu占比进行排序</p>
<p>（1）某个任务占用cu特别大，找到大任务看logview是什么原因造成（小文件过多、数据量确实需要这么多资源）。</p>
<p>（2）cu占比均匀说明是同时提交多个大任务把cu资源直接打满。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df0c1430c72840919c47e4be5e3befca~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>2.由于小文件过多导致cu占慢</p>
<p>map阶段的并行度是根据输入文件的分片大小，从而间接控制每个Map阶段下Worker的数量。默认是256m。如果是小文件会当作一个块读取如下图map阶段m1每个task的i/o bytes都只有1m或者几十kb,所以造成2500多个并行度瞬间把资源打满，说明该表下文件过多需要合并小文件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d88a50bcd62c4a4ca5b1d26750762d0d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>合并小文件<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhelp.aliyun.com%2Fknowledge%255C_detail%2F150531.html%3Fspm%3Da2c4g.11186623.6.1198.60ea4560Hr5H8d%23section-5nj-hoa-d7f" target="_blank" rel="nofollow noopener noreferrer" title="https://help.aliyun.com/knowledge%5C_detail/150531.html?spm=a2c4g.11186623.6.1198.60ea4560Hr5H8d#section-5nj-hoa-d7f" ref="nofollow noopener noreferrer">help.aliyun.com/knowledge\_…</a></p>
<p>3.数据量大导致资源占满</p>
<p>可以增加购买资源，如果是临时作业可以加set odps.task.quota.preference.tag=payasyougo;参数，可以让指定作业临时跑到按量付费大资源池，</p>
<p><strong>1.5任务并行度如何调节</strong></p>
<p>MaxCompute的并行度会根据输入的数据和任务复杂度自动推测执行，一般不需要调节，理想情况并行度越大速度处理越快但是对于包年包月资源组可能会把资源组占满，导致任务都在等待资源这种情况会导致任务变慢</p>
<p><strong>map阶段并行度</strong></p>
<p>**odps.stage.mapper.split.size ：**修改每个Map Worker的输入数据量，即输入文件的分片大小，从而间接控制每个Map阶段下Worker的数量。单位MB，默认值为256 MB</p>
<p><strong>reduce的并行度</strong></p>
<p>**odps.stage.reducer.num ：**修改每个Reduce阶段的Worker数量</p>
<p><strong>odps.stage.num：<strong>修改MaxCompute指定任务下所有Worker的并发数，优先级低于</strong>odps.stage.mapper.split.size</strong>、<strong>odps.stage.reducer.mem</strong>和<strong>odps.stage.joiner.num</strong>属性。</p>
<p>**odps.stage.joiner.num：**修改每个Join阶段的Worker数量。</p>
<h1 data-id="heading-1">二、数据倾斜</h1>
<p><strong>数据倾斜</strong></p>
<p>【特征】task 中大多数 instance 都已经结束了，但是有某几个 instance 却迟迟不结束（长尾）。如下图中大多数（358个）instance 都结束了，但是还有 18 个的状态是 Running，这些 instance 运行的慢，可能是因为处理的数据多，也可能是这些instance 处理特定数据慢。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8591fab19a844739212bc0364ef9efa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60bc6b4e2094436b8a965c6151a68a32~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决方法：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhelp.aliyun.com%2Fdocument%255C_detail%2F102614.html%3Fspm%3Da2c4g.11186623.6.1160.28c978569uyE9f" target="_blank" rel="nofollow noopener noreferrer" title="https://help.aliyun.com/document%5C_detail/102614.html?spm=a2c4g.11186623.6.1160.28c978569uyE9f" ref="nofollow noopener noreferrer">help.aliyun.com/document\_d…</a></p>
<h1 data-id="heading-2">三、逻辑问题</h1>
<p>这里指用户的SQL或者UDF逻辑低效，或者没有使用最优的参数设定。表现出来的现象时一个Task的运行时间很长，而且每个实例的运行时间也比较均匀。这里的情况更加多种多样，有些是确实逻辑复杂，有些则有较大的优化空间。</p>
<p><strong>数据膨胀</strong></p>
<p>【特征】task 的输出数据量比输入数据量大很多。</p>
<p>比如 1G 的数据经过处理，变成了 1T，在一个 instance 下处理 1T 的数据，运行效率肯定会大大降低。输入输出数据量体现在 Task 的 I/O Record 和 I/O Bytes 这两项：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f7049a986fe45068aa30fa1eb7078d0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决方法：确认业务逻辑确实需要这样，增大对应阶段并行度</p>
<p><strong>UDF执行效率低</strong></p>
<p>【特征】某个 task 执行效率低，且该 task 中有用户自定义的扩展。甚至是 UDF 的执行超时报错：“Fuxi job failed - WorkerRestart errCode:252,errMsg:kInstanceMonitorTimeout, usually caused by bad udf performance”。</p>
<p>首先确定udf位置，点看慢的fuxi task， 可以看到operator graph 中是否包含udf，例如下图说明有java 的udf。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03b30724bb6043d693f0ed1ffd2d8271~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57c74c9c707c4b23beecb3c347c20d14~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过查看logview 中fuxi instance 的stdout 可以查看该operator 运行速度，正常情况 Speed(records/s) 在百万或者十万级别。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/537a48299bdd481f8d947be166d25031~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决方法：检查udf逻辑尽量使用内置函数</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000283471%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000283471/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            