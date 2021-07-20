
---
title: 'Spark 大数据处理最佳实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fb92a39473c4428a68d89d118552b24~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 19:21:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fb92a39473c4428a68d89d118552b24~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">开源大数据社区 & 阿里云 EMR 系列直播 第十一期</h1>
<p>**主题：**Spark 大数据处理最佳实践</p>
<p>**讲师：**简锋，阿里云 EMR 数据开发平台 负责人</p>
<p><strong>内容框架：</strong></p>
<ul>
<li>大数据概览</li>
<li>如何摆脱技术小白</li>
<li>Spark SQL 学习框架</li>
<li>EMR Studio 上的大数据最佳实践</li>
</ul>
<p>**直播回放：**进入链接<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.aliyun.com%2Flive%2F247072" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.aliyun.com/live/247072" ref="nofollow noopener noreferrer">developer.aliyun.com/live/247072</a></p>
<h1 data-id="heading-1">一、大数据概览</h1>
<ul>
<li>大数据处理 ETL (Data → Data)</li>
<li>大数据分析 BI (Data → Dashboard)</li>
<li>机器学习 AI (Data → Model)</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fb92a39473c4428a68d89d118552b24~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">二、如何摆脱技术小白</h1>
<p><strong>什么是技术小白？</strong></p>
<ul>
<li>只懂表面，不懂本质</li>
</ul>
<p>比如：只懂得参考别人的 Spark 代码，不懂得 Spark 的内在机制，不懂得如何调优 Spark Job</p>
<p><strong>摆脱技术小白的药方</strong></p>
<ul>
<li>懂得运行机制</li>
<li>学会配置</li>
<li>学会看 Log</li>
</ul>
<p><strong>懂得运行机制：Spark SQL Architecture</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d3ba342b18a4a40b6ccfb189620f2b1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>学会配置：如何配置 Spark App</strong></p>
<ul>
<li><strong>配置 Driver</strong></li>
</ul>
<p>• spark.driver.memory</p>
<p>• spark.driver.cores</p>
<ul>
<li><strong>配置 Executor</strong></li>
</ul>
<p>• spark.executor.memory</p>
<p>• spark.executor.cores</p>
<ul>
<li><strong>配置 Runtime</strong></li>
</ul>
<p>• spark.files</p>
<p>• spark.jars</p>
<ul>
<li><strong>配置 DAE</strong></li>
<li>…..........</li>
</ul>
<p>**参考网址：**<a href="https://link.juejin.cn/?target=https%3A%2F%2Fspark.apache.org%2Fdocs%2Flatest%2Fconfiguration.html" target="_blank" rel="nofollow noopener noreferrer" title="https://spark.apache.org/docs/latest/configuration.html" ref="nofollow noopener noreferrer">spark.apache.org/docs/latest…</a></p>
<p><strong>学会看 Log：Spark Log</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5915fa05a0124ee9b81c751b7d37d96a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">三、Spark SQL 学习框架</h1>
<p><strong>Spark SQL 学习框架( 结合图形/几何）</strong></p>
<p>1. Select Rows</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bbaa1b2de814670a3f9975a0ea25a70~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e67d8c8f07c64ea5aaea605b6417b30c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>2. Select Columns</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11ff1287416542f2a41193b84a3b6890~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9695df8555e04387825bbf684a1c41a7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>3. Transform Column</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fd14cf1d66a488a9ce8687432c0059c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96956c6fea414173b9d4f9a71fe13ae0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>4. Group By / Aggregation</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b0bfe93d8e943b4b9a4a432058ce2f1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf8591db3f864a70b2fa4ebdfed08f0c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>5. Join</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c64d5f704da84504a3823da9a5fde195~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20465d34a8df433c97d2a0b910eeaf48~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Spark SQL 执行计划</strong></p>
<p>1. Spark SQL - Where</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/611dfa6abdb8454fa7c6900db8f4b0c0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>2. Spark SQL - Group By</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03d812768c5542f495adbca0ced296bf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>3. Spark SQL - Order by</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59df2ece64894b27a507d05d4a782f92~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">四、EMR Studio 实践</h1>
<p><strong>EMR Studio 特性：</strong></p>
<ul>
<li>兼容开源组件</li>
<li>支持连接多个集群</li>
<li>适配多个计算引擎</li>
<li>交互式开发 + 作业调度无缝衔接</li>
<li>适用多种大数据应用场景</li>
<li>计算存储分离</li>
</ul>
<p>1. 兼容开源组件</p>
<ul>
<li>EMR Studio 在开源软件 Apache Zeppelin，Jupyter Notebook, Apache Airflow 的基础上优化了做了优化和增强。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b59bb6bd95c44cd9ffd260c611e76da~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>2. 支持连接多个集群</p>
<ul>
<li>一个 EMR Studio 可以连接多个 EMR 计算集群，您可以很方便地切换计算集群，提交作业到不同的计算集群上运行。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0432341674541f88051c0b31306d618~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>3. 适配多个计算引擎</p>
<ul>
<li>自动适配 Hive、Spark、Flink、Presto、Impala 和 Shell 等多个计算引擎，无需复杂配置，多个计算引擎间协同工作</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b236cff8994a46b18fcf1679e038e44b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>4. 交互式开发 + 作业调度无缝衔接</p>
<p><strong>Notebook + Airflow : 无缝衔接开发环节和生产调度环节</strong></p>
<ul>
<li>利用交互式开发模式可以快速验证作业的正确性.</li>
<li>在 Airflow 里调度 Notebook 作业，最大程度得保证开发环境和生产环境的一致性，防止由于开发阶段和生产阶段环境不一致而导致的问题。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/839f94356eef4b7bb71bef0f26a23bbe~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>5. 适用多种大数据应用场景</p>
<ul>
<li>大数据处理 ETL</li>
<li>交互式数据分析</li>
<li>机器学习</li>
<li>实时计算</li>
</ul>
<p>6. 计算存储分离</p>
<ul>
<li><strong>所有数据都保存在 OSS 上，包括：</strong></li>
</ul>
<p>• 用户 Notebook 代码</p>
<p>• 调度作业 Log</p>
<ul>
<li><strong>即使集群销毁，也可以重建集群轻松恢复数据</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82a524031e68454b917c6139724db528~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>EMR Studio Demo 演示：</strong></p>
<p>**参考文档：**<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhelp.aliyun.com%2Fdocument%255C_detail%2F208107.html%3Fspm%3Da2c4g.11186623.6.845.6cfc24577t1RbI" target="_blank" rel="nofollow noopener noreferrer" title="https://help.aliyun.com/document%5C_detail/208107.html?spm=a2c4g.11186623.6.845.6cfc24577t1RbI" ref="nofollow noopener noreferrer">help.aliyun.com/document\_d…</a></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000284515%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000284515/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            