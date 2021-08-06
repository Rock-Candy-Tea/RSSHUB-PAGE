
---
title: '利用共享内存实现比NCCL更快的集合通信'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0986778c2b86494aa0d8ec4c8ded3e8a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 22:41:20 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0986778c2b86494aa0d8ec4c8ded3e8a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者：曹彬 | 旷视 MegEngine 架构师</p>
<h2 data-id="heading-0">简介</h2>
<p>从 2080Ti 这一代显卡开始，所有的民用游戏卡都取消了 P2P copy，导致训练速度显著的变慢。针对这种情况下的单机多卡训练，MegEngine中实现了更快的集合通信算法，对多个不同的网络训练相对于NCCL有3%到10%的加速效果</p>
<p>MegEngine v1.5 版本，可以手动切换集合通信后端为 shm（默认是 nccl），只需要改一个参数。（由于 shm 模式对 CPU 有额外的占用，且只有在特定卡下才能提高效率，因此并没有默认打开）</p>
<pre><code class="copyable">gm = GradManager()
gm.attach(model.parameters(), callbacks=[dist.make_allreduce_cb("sum", backend="shm")])
目前只实现了单机版本，多机暂不支持
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">背景</h2>
<p>在大规模训练中，数据并行是最简单最常见的训练方式，每张卡运行完全一样的网络结构，然后加上参数同步就可以了。</p>
<p>对于数据并行的参数同步，目前有两种常用的方法，Parameter Server 和 Gradient AllReduce：</p>
<ul>
<li>
<p>Parameter Server 方案需要额外机器作为参数服务器来更新参数，而且中心式的通讯方式对带宽的压力很大，增加训练机器的同时通信量也线性增加；</p>
</li>
<li>
<p>而 AllReduce 方案只是参与训练的机器之间互相同步参数，不需要额外的机器，可扩展性好。</p>
</li>
</ul>
<p>MegEngine 目前也是使用 AllReduce 方案作为数据并行的参数同步方案。而在AllReduce方案中，大家目前常用的是 NCCL，Nvidia 自家写的 GPU 集合通讯库，通信效率很高。</p>
<p>看到这里，可以得到一个结论，数据并行的情况，用 NCCL 通讯库能达到不错的效果。</p>
<p>到这里就结束了？当然不是，在 2080Ti 8卡训练的情况下，在多个网络下，我们相对 NCCL 有 3% 到 10% 的性能提升。（以 2080Ti 为例子是因为游戏卡不支持 P2P 通信，相对来说通信较慢，通信时间长，节省通信时间能获得的收益较大）</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0986778c2b86494aa0d8ec4c8ded3e8a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是怎么做到的呢，我们一步一步来分析（以下数据都是用 megengine.utils.profiler 导出，相关文档在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmegengine.org.cn%2Fdoc%2Fstable%2Fzh%2Fuser-guide%2Fmodel-development%2Fprofiler%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://megengine.org.cn/doc/stable/zh/user-guide/model-development/profiler/index.html" ref="nofollow noopener noreferrer">profiler文档</a>）。</p>
<p>通常我们是在 backward 阶段同时做 gradient 的同步，我们来看单卡的 backward耗时，只有 164ms：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fea5196c8e1e48989bc1121c1b029e69~tplv-k3u1fbpfcp-watermark.image" alt="图 1（单卡 ResNet50 训练" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再来看 8 卡训练时 backward 的耗时，增长到了 203ms，比单卡的情况下多了 39ms：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbd10cf64827471a9d40af2324ebe716~tplv-k3u1fbpfcp-watermark.image" alt="图 2（使用 NCCL 做 8卡 ResNet50 训练）" loading="lazy" referrerpolicy="no-referrer"></p>
<p>确实，backward 时间变长了不少，可是为什么？我们有没有可能消除它？</p>
<p>1）为什么</p>
<p>一句话：NCCL AllReduce 占用了 cuda 计算资源，所以计算变慢。</p>
<p>具体原因是 NCCL AllReduce 对应的 cuda kernel 需要既做通信又做计算，所以占用了计算对应需要的计算资源，但是大部分时间都花在了通信上，导致计算资源的利用率不够高。</p>
<p>2）能不能消除它</p>
<p>当然是可以的，cuda 计算和通信是可以并行的，让计算和通信运行在两个不同的 cuda stream 上，就可以并行起来，这一点在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.nvidia.com%2Fcuda%2Fcuda-c-programming-guide%2Findex.html%23overlap-of-data-transfer-and-kernel-execution" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#overlap-of-data-transfer-and-kernel-execution" ref="nofollow noopener noreferrer">cuda 开发者文档</a>中有提到。</p>
<p>3）实际测试计算和通信并行的例子</p>
<p>stream0 进行矩阵乘法运算，stream1 进行拷贝，前后矩阵乘法的速度没有受到影响：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ae49077adc146099e046c4b3d5928d1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/652056dd98bf417180e67d43b863c7d7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aaa0e48b0a88495986fda9b228a9854b~tplv-k3u1fbpfcp-watermark.image" alt="图3（计算通信并行，stream0 做矩阵乘法，stream1 做 d2d copy）" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">实现思路</h2>
<p>这里先介绍一下 AllReduce 的两种实现方法。</p>
<h3 data-id="heading-3">1）ReduceScatter + AllGather</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03a67ce264b6456b96d127b3b3cb1975~tplv-k3u1fbpfcp-watermark.image" alt="图4（ReduceScatter算子图解）" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87da3031f09d4c20893afab9964a85cf~tplv-k3u1fbpfcp-watermark.image" alt="图5（ AllGather 算子图解）" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Ring AllReduce 就是用的 ReduceScatter + AllGather 的模式：首先第一轮通信在各个节点上计算出部分和，然后第二轮通信把部分和聚集一下得到最终结果。</p>
<h3 data-id="heading-4">2）Reduce + Broadcast</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fa0b3d0058b41408af2a64597c8620f~tplv-k3u1fbpfcp-watermark.image" alt="图6（ Reduce 算子图解）" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee69d05f760e44a880753a4600d76938~tplv-k3u1fbpfcp-watermark.image" alt="图7 （Broadcast算子图解）" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Reduce + Broadcast 的方式像 Parameter Server，会先在一个节点计算出完整的累加和，然后再广播到各个节点上。</p>
<p>新的算法采用的是 Reduce + Broadcast 的方法，首先将数据全部拷贝到 cpu（使用 Shared Memory），然后由 cpu 进行累加，再拷贝回 gpu。</p>
<p>由于直接拷贝累加没有把计算和通信 overlap 起来，我们还采用了类似 Ring AllReduce 的分块策略，让通信和计算充分 overlap，如下图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f4a39d77c5e47dc85a8a14b2edfa0ca~tplv-k3u1fbpfcp-watermark.image" alt="图8（Shared Memory AllReduce 中 Reduce 阶段图解）" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为用到了 Shared Memory，所以把这个后端简称为 SHM。</p>
<h2 data-id="heading-5">实现效果</h2>
<h3 data-id="heading-6">1）算子性能</h3>
<p>相对 NCCL 来说，SHM 的延迟稍微高了一些，带宽低了一些，数据大一些的情况可以达到 NCCL 的 90% 左右的性能。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2533fa7cc194491496e5285358f3f286~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a6611d280324584bd2da3c85ef4c064~tplv-k3u1fbpfcp-watermark.image" alt="图9（ SHM 和 NCCL 算子性能对比）" loading="lazy" referrerpolicy="no-referrer"></p>
<p>SHM 性能需要在数据包大的情况发挥，和 ParamPack 策略搭配能最大发挥 SHM 的作用（在 MegEngine 中 distributed.make_allreduce_cb 中使用了 ParamPack 策略， 默认打包大小为 10M）。ParamPack 策略是指将参数对应的梯度打包进行发送，减少小包发送，以减少通信延迟增加带宽利用率。</p>
<h3 data-id="heading-7">2）实际训练效果</h3>
<p>继续使用 ResNet50 8卡训练的例子，SHM 与 NCCL 相比，backward 时间快了近 30ms（203ms->174ms）。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed50cf964e76481598d8232cfeabc502~tplv-k3u1fbpfcp-watermark.image" alt="图10（使用 SHM 后端进行 ResNet50 8卡训练）" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">Shared Memory AllReduce 的不足之处/后续改进</h2>
<h3 data-id="heading-9">1）cpu 占用多</h3>
<p>因为占用了 cpu 资源做 reduce 运算，所以在 cpu 资源紧张的情况下会比较慢，需要确定 cpu 资源是否够用再进行使用。</p>
<h3 data-id="heading-10">2）额外通信成本</h3>
<p>因为 copy 和 reduce 之间有数据依赖关系，copy需要等待上一次的reduce完成才能开始，reduce要等待copy数据就位才能开始，所以中间插入了信号量的同步，引入了额外的通信成本，在分块越多的情况越明显。</p>
<h3 data-id="heading-11">3）多进程负载均衡</h3>
<p>各个进程的 copy 和 reduce 速度不一致导致了进度不同步的问题，会造成多余的等待时间，根据实际运行速度进行分配任务性能会有进一步的提升。</p>
<h3 data-id="heading-12">4）更多的 overlap</h3>
<p>目前只用到了 copy 和 reduce 之间的 overlap，但是其实 h2d 和 d2h 拷贝也是可以 overlap 起来的，可以有进一步加速。</p>
<hr>
<h2 data-id="heading-13">附：</h2>
<p>GitHub：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2FMegEngine" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=https%3A//github.com/MegEngine" ref="nofollow noopener noreferrer">MegEngine 天元</a></p>
<p>官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fmegengine.org.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=https%3A//megengine.org.cn/" ref="nofollow noopener noreferrer">MegEngine-深度学习，简单开发</a></p>
<p>欢迎加入 MegEngine 技术交流 QQ 群：1029741705</p></div>  
</div>
            