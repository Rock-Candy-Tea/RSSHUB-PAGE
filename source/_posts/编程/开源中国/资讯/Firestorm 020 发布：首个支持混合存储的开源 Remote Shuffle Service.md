
---
title: 'Firestorm 0.2.0 发布：首个支持混合存储的开源 Remote Shuffle Service'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5e4bf7b9ea91283618efdddd2c438f2fde0.png'
author: 开源中国
comments: false
date: Sun, 13 Feb 2022 07:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5e4bf7b9ea91283618efdddd2c438f2fde0.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left"><strong>一、背景</strong></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Firestorm自2021年11月上线开源 0.1.0 版本后，该项目受到了业界的广泛关注。 Firestorm是为了加速分布式计算引擎能上云的重要组件，同时也能解决在大Shuffle场景下，计算任务由于Shuffle过程异常而导致的任务失败。（更详细的背景可以参考此文：[<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcloud.tencent.com%2Fdeveloper%2Farticle%2F1903023" target="_blank"><span> </span>Firestorm - 腾讯自研Remote Shuffle Service在Spark云原生场景的实践]</a>）</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">目前Firestorm迎来了0.2.0 版本的正式发布，而Firestorm也成为了第一个支持混合存储的开源Remote Shuffle Service 方案。<strong>本文将重点介绍 Firestorm 0.2.0 版本的最新特性及性能分析。</strong></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">二、版本新特性—支持混合存储</h1> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>什么是混合存储</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在Firestorm初始版本中，Shuffle数据只能存储在Shuffle Server的本地盘，或者分布式存储系统。而混合存储则充分利用了Shuffle Server的内存资源，并结合本地文件和分布式存储系统，使得Shuffle数据能存储在多个介质中。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>为什么需要混合存储</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在实际的生产过程中，由于Shuffle数据的块大小不一致，小的只有几KB，甚至几十Byte，**而大的能达到256MB以上。这样的场景下，对于HDFS这样的分布式存储非常不友好，大量的小数据块的写入会导致集群响应过慢，严重影响计算任务的效率。**虽然使用Shuffle Server</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">磁盘能很好的缓解该问题，但随之而来的问题是，Shuffle Server必须具备大量的磁盘空间来承载PB级别的Shuffle数据，这样的绑定不利于现在的云原生的大环境。同时，在Shuffle数据写入过程中，必须要等待数据都写入存储后，才能进行下一步，在存储繁忙时，对于计算任务的性能有较大的影响。<strong>为了解决上述提到的问题，基于内存，本地文件和分布式存储相结合的混合存储的方案就油然而生了。</strong></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>混合存储实现原理</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">以Spark为例，先看下基于单一存储的方案是如何对Shuffle数据进行读写的：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-5e4bf7b9ea91283618efdddd2c438f2fde0.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在上图写的过程中，Shuffle数据在经过步骤1，2，3的计算，缓存等操作，在步骤4发送到了Shuffle Server侧，再经过步骤5，6的缓存，数据聚合等操作，最终通过步骤7写入存储介质。所有任务结束后，会发送Commit命令给Shuffle Server，如果是最后一个任务，则必须等待相关数据都写入存储后，才能完成，而Commit操作后等待写入存储的过程对于任务的整体性能影响较大。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-0ee13a6d48ca54fcaf818b6abeb1eec0110.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在写入完成后，读取过程则较为简单，基于存储介质，选择从Shuffle Server读取或直接从分布式存储读取。 了解完之前的方案后，再来看下混合存储是如何实现：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-14afbc845657b64ed34f4b97d7e7676743c.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">相比之前，有3个主要的变化：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>1.首先，步骤5的Flush方案进行了优化：</strong><span> </span>之前的Flush方案是，每个Shuffle Partition数据达到阈值或整个缓存空间达到阈值，则将这部分数据写入存储介质，而现在则设置了缓存空间的上下水位，到达上水位则进行Flush操作，直至缓存空间到达低水位。同时，在Flush数据选择上，优先选择数据量多的Partition。通过上水位的控制，保证了在Flush过程中，缓存依然有足够的空间接受新的数据，而通过下水位及Flush数据的选择，保障了数据量较少的Shuffle数据能驻留在内存，降低存储写入小文件的概率。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>2.其次，对步骤7进行了重构：</strong><span> </span>支持基于写入数据块大小对存储介质进行选择，如，大于32MB的数据块写入分布式存储，而其它的则写入本地存储。这样的策略是为了更好匹配分布式存储的写入模式，达到更好的写入性能。同时，也观察到在实际任务运行过程中，大数据块的数量虽然占比不高，如，30%，但是，大数据块的数据总量占比更高，如，70%。基于这样的存储方案，可以降低对于本地盘容量的依赖，便于Firestorm在各种环境下进行部署，甚至云上部署。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>3.最后，去除了步骤8的Commit操作：</strong><span> </span>Commit操作存在的意义在于读取数据时保证数据都能被读取到。由于内存也作为了混合存储的一部分，且Shuffle Server侧在存储介质正常的情况下能保证Shuffle数据要么在内存中，要么在存储介质中，那么Commit操作也失去了存在的意义。从下图可以看到，BufferManager包含多个Buffer，每个Buffer存储了单个Partition的Shuffle数据，且存储CachedData中。当BufferManager达到高水位时，CachedData的数据会转移到InFlushData，直到存储写入完成，同时，CachedData还能接收新的Shuffle数据。<strong>这样的策略保证了Shuffle数据未写入存储前也不会丢失。</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-9eef5056b333469990d2ba963dad6e962a0.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下图则展示了数据在Shuffle Server的内存区域中是如何流转的，写入前先申请内存空间并占据PreAllocation区域，接收到数据后内存使用转移到CachedData区域，在Flush后进一步移动到InFlushData区域，最后写入存储中，并清理掉内存空间。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-35c6a4ca1250d9515f8788de579a6360db0.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">了解了写入过程，再看读取过程的变化则更容易了，相比之前的单一存储的读取方案，基于混合存储方案读取时，会按序从Shuffle Server Memory, Shuffle Server本地存储及分布式存储读取Shuffle数据。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-dfde167675e0258befe9e14ed7b8b7dac4b.png" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>混合存储的优势</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">上文已经介绍了混合存储解决的问题及相关实现，这里再做下总结，引入混合存储可以带来如下收益: 1.基于写入数据块大小选择存储介质，提升DFS的写入性能 2.降低对于Shuffle Server本地磁盘容量的依赖，在云原生环境下，更容易部署 3.降低写入Shuffle Server本地磁盘的数据量，当采用SSD作为本地存储时，增加SSD使用寿命，降低存储成本 4.引入内存作为存储，提升计算任务性能</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>混合存储的使用方式</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">由于内存的Flush策略进行了变更，Shuffle Server引入的相关配置如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">#基于rss.server.buffer.capacity值的低水位百分比</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>rss.server.memory.shuffle.lowWaterMark.percentage 25.0</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">#基于rss.server.buffer.capacity值的高水位百分比</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>rss.server.memory.shuffle.highWaterMark.percentage 75.0</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>目前支持的混合存储类型有：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Shuffle Server端:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>注意：由于使用了本地文件和HDFS混合存储，需要增加</strong><em>rss.server.flush.cold.storage.threshold.size</em><strong>该配置，设定单次写入数据量阈值，大于该值将写入HDFS，其余的写入本地文件</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>rss.storage.type MEMORY_LOCALFILE_HDFS</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>rss.storage.basePath /path1,/path2</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>rss.server.hdfs.base.path hdfs://ip:port/path</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>rss.server.flush.cold.storage.threshold.size 32m</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Spark Client端:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>spark.rss.storage.type MEMORY_LOCALFILE_HDFS</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>spark.rss.base.path hdfs://ip:port/path</em></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>支持数据过滤</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在读取Shuffle数据的过程中，会先读取所有的元数据信息，如，BlockId，TaskId，Length等，再基于元数据信息读取Shuffle数据。由于分布式计算任务的Shuffle数据会产生冗余，如，Spark的推测执行等。为了减少数据的无效读取，更合理的利用系统资源，增加了读取Shuffle数据时的过滤功能。优化的场景如下： 1.Spark AQE 需要读取指定的上游数据 2.Spark 推测执行产生的冗余数据 3.混合存储场景下，数据已从内存读取，又被写入存储而产生的冗余数据</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>其它特性</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">除了上述的主要特性，版本还有如下改动：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.新增对于Spark版本的支持，目前已能支持，Spark2.3， Spark2.4， Spark3.0， Spark3.1</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.优化Shuffle数据读取策略，改为先读取Index文件，再读取Data文件</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3.新增GRPC相关指标 4.修复已知缺陷</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong>三、版本性能测试</strong></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">由于新版本在存储架构上有了较大的变动，以下是性能测试的相关信息</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>测试环境</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>硬件环境</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.每台服务器为 176 cores，256G内存，4T * 12 HDD，网络带宽 10GB/s</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.Hadoop Yarn集群：1 * ResourceManager + 6 * NodeManager， 4T * 10 HDD 写临时数据</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3.Firestorm集群：1 * Coordinator + 6 * Shuffle Server，</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">4.T * 10 HDD 写Shuffle数据</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>软件环境</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.Hadoop版本2.8.5</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.Spark版本</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3. 2.4.Spark相关配置：  </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>spark.executor.instances 100</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>spark.executor.cores 4</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>spark.executor.memory 9g</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>spark.executor.memoryOverhead 1024</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>spark.shuffle.manager org.apache.spark.shuffle.RssShuffleManager</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>spark.rss.storage.type MEMORY_LOCALFILE</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">4.Firestorm Shuffle Server相关配置：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>rss.storage.type MEMORY_LOCALFILE rss.server.buffer.capacity 50g</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>测试场景:</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>TPC-DS</strong><span> </span>基于1TB数据量的TPC-DS，对Spark原生Shuffle，Firestorm 0.1.0，Firestorm 0.2.0进行了对比性能测试，以下是相关测试结果：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-4732403c07c26fc500d236f11defccbf04b.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-65ea70fc16e55a3541a4e870de6d32eceac.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-dd4be2a47cd060bea4138f1c56a06d9c124.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>从测试结果可以看到，Firestorm0.2.0版本比上一个版本有了30%左右的提升</strong>，但对于Spark原生Shuffle并无任何优势，这个结果是符合预期的，原因有如下几点：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.即使是1TB的TPC-DS测试，query的Shuffle数据量普遍较小，使得磁盘可以忽略由于随机读写而产生的性能下降</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.由于考虑到高并发场景下的网络连接数过多问题，每个Executor和Shuffle Server之间仅存在一个RPC连接，串行发送数据的模式降低了性能</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3.客户端在发送完数据后，会每隔一定时间检查发送成功与否，这个间隔时间也增加了任务运行的性能损耗</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">从性能角度看，Firestorm的优势主要在于减少了存储随机读写带来的性能损耗，由于RPC在实现上更多的考虑稳定性及高并发场景，相比原生Shuffle方案有额外的性能开销，最终导致了在没有磁盘随机IO的场景下，Firestorm性能不如原生Shuffle。 **但是，在磁盘有随机IO的场景下，Firestorm还是具备性能优势的，**为了验证这个结论，将10块HDD降低为2块HDD，选取Shuffle数据量较多的query23a进行测试，测试结果如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">可以很明显的看到，当HDD数量从10下降到2以后，对于原生Spark的Shuffle Read性能影响严重，读取时间上升了5倍，而对于Firestorm来说，由于随机读写问题不突出，Shuffle Read性能基本没有损耗。 测试场景: TeraSort 基于1TB数据集，对原生Spark Shuffle，Firestorm 进行性能对比测试，结果如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-04664dd0fcb7158ea87d8f58226768d485e.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-4a773427fc1dececa6368462a3fdf2125a2.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">由于Shuffle数据量在500GB，从测试结果可以明显看出即使拥有10块HDD，原生Spark的磁盘随机读取造成的Shuffle Read性能下降还是非常明显的。而Firestorm不管是哪个版本，在Shuffle Read的性能上远优于原生Spark。对于Firestorm-0.2.0版本，由于混合存储的存在，Commit操作不再需要，可以看到已经不需要在最后个任务完成后等待Shuffle数据写入存储了。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong>四、总结</strong></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>本文介绍了Firestorm 0.2.0版本对于存储侧的一系列改进，其中最为重要的是引入了混合存储功能，利用了内存，本地磁盘，远程存储等资源更合理的分配存储策略。</strong>除了提高了性能，还降低了对本地磁盘的依赖，能更好的在云原生的环境下进行部署使用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">附上开源地址，欢迎共建:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2FFirestorm" target="_blank">https://github.com/Tencent/Firestorm</a></p>
                                        </div>
                                      
</div>
            