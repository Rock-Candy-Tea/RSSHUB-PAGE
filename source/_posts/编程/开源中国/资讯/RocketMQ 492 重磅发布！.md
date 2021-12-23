
---
title: 'RocketMQ 4.9.2 重磅发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/a5d3b880-6cc5-4126-b541-f52640857a69.jpg'
author: 开源中国
comments: false
date: Thu, 23 Dec 2021 16:05:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/a5d3b880-6cc5-4126-b541-f52640857a69.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0; margin-right:0; text-align:center"><img src="https://oscimg.oschina.net/oscnet/a5d3b880-6cc5-4126-b541-f52640857a69.jpg" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">经过社区多轮投票，Apache RocketMQ 初冬的第一个版本4.9.2 终于来了！</p> 
<p style="margin-left:0; margin-right:0"><span>在该版本中，优化核心特性及文档超过 40 项，并且再次对性能进行了全面提升，此外最值得关注的 RIP-7 Commitlog 多目录存储支持重磅发布。</span></p> 
<p style="margin-left:0; margin-right:0"><em><strong>Commitlog多目录存储支持</strong></em></p> 
<p style="margin-left:0; margin-right:0">通过Commitlog多目录存储功能，一方面能有效利用服务器上多个磁盘的存储空间，另一方还能让单个Broker实例通过动态挂载新磁盘的方式，实现动态地扩充存储能力。具体实现的示意图如下:</p> 
<p style="margin-left:0; margin-right:0; text-align:center"><img src="https://oscimg.oschina.net/oscnet/9fd09ae3-9a85-4c30-a75b-5ca5c455cdb9.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">要使用该功能，需要在配置文件中的 storePathCommitLog设置多个目录，目录之间使用逗号隔开，如"storePathCommitLog=/data1/commitlog,/data2/commitlog,/data3/commitlog"。</p> 
<p style="margin-left:0; margin-right:0">如此配置后，Broker在每次单个Commitlog文件写满之后，会选择新的目录创建下一个commitlog文件。storePathCommitLog 参数支持动态更新，但是如果从单目录切换到多目录，需要重启。此外，针对单个磁盘异常需要替换的情况，新增了readOnlyCommitLogStorePaths配置项，用于标记目录只读，通过禁写和数据过期策略，可实现单盘的平滑下线。当前，我们采用了轮询的方式来选择下一个要使用的目录，并且会自动跳过被标记只读和磁盘空间不够（默认85%阈值）的目录，用户不必担心因为磁盘空间不均衡从而导致浪费的情况。</p> 
<p style="margin-left:0; margin-right:0"><em><strong>高性能优化 </strong></em></p> 
<p style="margin-left:0; margin-right:0">本次是4.9.1开启性能优化版本的延续: 使用LongAdder替换AtomicLong，在指标统计时，性能数倍提升。</p> 
<p style="margin-left:0; margin-right:0">LongAdder 与 AtomicLong 的区别在于高并发时前者将对单一变量的CAS操作分散为对数组中多个元素的CAS操作，取值时进行求和。</p> 
<p style="margin-left:0; margin-right:0">这里分享测试代码， 欢迎大家跑一跑，留言分享自己测试的结果。</p> 
<pre style="margin-left:0; margin-right:0"><code><span><span><span style="color:#6a737d">@BenchmarkMode</span></span><span style="color:#6a737d">(Mode.Throughput)</span></span></code><code><span><span><span style="color:#6a737d">@Fork</span></span><span style="color:#6a737d">(</span><span><span style="color:#6a737d">1</span></span><span style="color:#6a737d">)</span></span></code><code><span><span><span style="color:#6a737d">@Threads</span></span><span style="color:#6a737d">(</span><span><span style="color:#6a737d">4</span></span><span style="color:#6a737d">)</span></span></code><code><span><span><span style="color:#6a737d">@Warmup</span></span><span style="color:#6a737d">(iterations = </span><span><span style="color:#6a737d">1</span></span><span style="color:#6a737d">, time = </span><span><span style="color:#6a737d">1</span></span><span style="color:#6a737d">)</span></span></code><code><span><span><span style="color:#6a737d">@Measurement</span></span><span style="color:#6a737d">(iterations = </span><span><span style="color:#6a737d">2</span></span><span style="color:#6a737d">, time = </span><span><span style="color:#6a737d">5</span></span><span style="color:#6a737d">)</span></span></code><code><span><span><span style="color:#6a737d">@State</span></span><span style="color:#6a737d">(Scope.Benchmark)</span></span></code><code><span><span><span style="color:#d73a49">public</span></span> <span><span><span><span style="color:#d73a49">class</span></span></span><span> </span><span><span><span style="color:#6f42c1">CasVsAdder</span></span></span><span> </span></span>&#123;</span></code><code><span>    <span><span style="color:#d73a49">private</span></span> AtomicLong count;</span></code><code><span>    <span><span style="color:#d73a49">private</span></span> LongAdder adder;</span></code>
<code><span>    <span><span style="color:#6a737d">@Setup</span></span></span></code><code><span>    <span><span><span style="color:#d73a49">public</span></span> <span>void</span> <span><span style="color:#d73a49">init</span></span><span>()</span> </span>&#123;</span></code><code><span>        count = <span>new</span> AtomicLong(<span><span>0</span></span>);</span></code><code><span>        adder = <span>new</span> LongAdder();</span></code><code><span>    &#125;</span></code>

<code><span>    <span><span style="color:#6a737d">@Benchmark</span></span></span></code><code><span>    <span><span><span style="color:#d73a49">public</span></span> <span>void</span> <span>testCas</span><span>()</span> </span>&#123;</span></code><code><span>        <span><span style="color:#d73a49">for</span></span> (<span>int</span> i = <span><span>0</span></span>; i < <span><span>10000</span></span>; i++) &#123;</span></code><code><span>            count.incrementAndGet();</span></code><code><span>        &#125;</span></code><code><span>    &#125;</span></code>

<code><span>    <span><span style="color:#6a737d">@Benchmark</span></span></span></code><code><span>    <span><span><span style="color:#d73a49">public</span></span> <span>void</span> <span>testAdder</span><span>()</span> </span>&#123;</span></code><code><span>        <span><span style="color:#d73a49">for</span></span> (<span>int</span> i = <span><span>0</span></span>; i < <span><span>10000</span></span>; i++) &#123;</span></code><code><span>            adder.increment();</span></code><code><span>        &#125;</span></code><code><span>    &#125;</span></code>
<code><span>    <span><span><span style="color:#d73a49">public</span></span> <span>static</span> <span>void</span> <span>main</span><span>(String[] args)</span> <span>throws</span> RunnerException </span>&#123;</span></code><code><span>        Options options = <span>new</span> OptionsBuilder()</span></code><code><span>                .include(CasVsAdder<span>.<span style="color:#d73a49">class</span>.<span style="color:#6f42c1">getSimpleName</span></span>())</span></code><code><span>                .output(System.getProperty(<span><span style="color:#032f62">"user.home"</span></span>) + <span><span style="color:#032f62">"/"</span></span> + CasVsAdder<span>.<span style="color:#d73a49">class</span>.<span style="color:#6f42c1">getSimpleName</span></span>()</span></code><code><span>                        + <span><span style="color:#032f62">".txt"</span></span>)</span></code><code><span>                .build();</span></code><code><span>        <span>new</span> Runner(options).run();</span></code><code><span>    &#125;</span></code><code><span>&#125;</span></code></pre> 
<p style="margin-left:0; margin-right:0"><em><strong>实用工具 </strong></em></p> 
<p style="margin-left:0; margin-right:0">支持元数据导出 by <span style="color:#007aaa">@panzhi33</span></p> 
<p style="margin-left:0; margin-right:0">支持命令行查询消费者配置 by <span style="color:#007aaa">@zhangjidi2016</span></p> 
<p style="margin-left:0; margin-right:0">支持DLQ topic默认可读 by <span style="color:#007aaa">@maixiaohai</span></p> 
<p style="margin-left:0; margin-right:0">...</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#676464"><em><strong>本次版本的顺利发布，离不开RocketMQ社区的每一位参与贡献者，尤其鸣谢Apache RocketMQ Committer 黄理，江海挺，小伟等。</strong></em></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left">另外，从该版本起，每次发布新版本， 都可以在github上看到每个PR的提供者的名字和第一次贡献者的名字，比如：https://github.com/apache/rocketmq/releases/tag/rocketmq-all-4.9.2。</p> 
<p style="margin-left:0; margin-right:0; text-align:center"><img src="https://oscimg.oschina.net/oscnet/7b22fca9-eef5-4849-b648-a62753a26a9d.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><img src="https://oscimg.oschina.net/oscnet/9e3b941a-7b9a-4b70-9096-6679d3bede82.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>加入 Apache RocketMQ 社区</strong></p> 
<p style="margin-left:0; margin-right:0"><span style="background-color:#ffffff">Apache RocketMQ自2016年走入全球开发者视野以来，已然发展成为电商、金融、教育、科技等领域技术中台最核心的数据底座。据不完全统计，单单在国内，金融100强、保险100强、财富500强、券商50强超过70%的企业在核心应用链路上规模化部署了RocketMQ，全球5朵大云也纷纷上线了RocketMQ云产品服务。在历经2代RocketMQ人的辛勤创作下，目前正迎来10年之大变革 - 下一代架构升级。</span><br> <span style="background-color:#ffffff">欢迎立志打造世界级分布式系统的同学加入社区，</span><span>添加社区开发者微信：</span><span>rocketmq666 即可进群，参与贡献，共同打造下一代消息流融合处理平台。</span></p> 
<p style="margin-left:0; margin-right:0"><em>下载地址：</em></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span style="color:#007aaa"><em>https://rocketmq.apache.org/release_notes/release-notes-4.9.2/</em></span></p>
                                        </div>
                                      
</div>
            