
---
title: '【云原生AI】Fluid + JindoFS 助力微博海量小文件模型训练速度提升 18 倍'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/a8bd7be50b90435f9a814a8f4b91bc5b.png'
author: Dockone
comments: false
date: 2021-06-08 12:09:58
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/a8bd7be50b90435f9a814a8f4b91bc5b.png'
---

<div>   
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/a8bd7be50b90435f9a814a8f4b91bc5b.png" alt="1.png" referrerpolicy="no-referrer"><br>
<br>作者 ｜<br>
吴彤  微博深度学习平台工程师<br>
郝丽  微博深度学习平台工程师<br>
<br>导读：深度学习平台在微博社交业务扮演着重要的角色。计算存储分离架构下，微博深度学习平台在数据访问与调度方面存在性能低效的问题。本文将介绍微博内部设计实现的一套全新的基于 Fluid（内含 JindoRuntime）的新架构方案，显著提升了海量小文件场景模型训练的性能和稳定性，多机多卡分布式训练场景可将模型训练的速度提升 18 倍。<br>
<br><h1>背景​</h1>​<br>
新浪微博是中国最大的社交媒体平台，每天上亿条内容产生并在万亿级关系的社交网络上进行传播。下图是微博的业务生态图，通过优质用户生产、传播优质内容，普通用户消费这些内容，进而关注自己喜欢的博主，建立联系，形成闭环生态。<br>
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/4d59154cc16e4b048f4d075491b42859.png" alt="2.png" referrerpolicy="no-referrer"><br>
<br>微博机器学习平台的主要作用是让整个过程流转得更高效流畅：通过理解优质内容，构建用户画像，把用户感兴趣的优质内容推给用户，让他们和内容生产者互动，进而刺激生产者生产更多更好的内容, 实现信息消费者和信息生产者的双赢。而随着多媒体内容变成主流，深度学习技术就变得更为重要。从多媒体的内容理解，到 CTR 任务的优化，都离不开深度学习技术的支持。<br>
​<br>
<h1>大规模深度学习模型训练挑战</h1>​<br>
随着深度学习在微博业务场景中的广泛使用，微博深度学习平台扮演了非常核心的角色。该平台采用了存储与计算分离的架构，使得计算资源得以与存储资源解耦，从而实现了灵活的资源配比以及便捷的存储扩展，并且降低了存储成本。<br>
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/523b8fe3e74143f4a6932e893f7ef9ba.png" alt="3.png" referrerpolicy="no-referrer"><br>
<br>然而，这种架构也带来了一些挑战，其中比较关键的问题体现在数据访问性能和稳定性方面：<br>
​<br>
1. <strong>计算存储分离架构导致数据访问高延时，导致训练慢</strong>：业务团队使用的深度学习任务（图像或语音模型）会访问海量小文件。实验表明，HDFS 读取海量小文件场景与本地读取对比性能相差近十倍甚至百倍。<br>
<ol><li><br><strong>Kubernetes 调度器数据缓存无感知，同一数据源多次运行访问依旧慢</strong>：相同模型、不同超参的；微调模型、相同输入的；AutoML 等深度学习任务运行会不断重复访问同一数据，产生可以复用的数据缓存。但是由于原生的 Kubernetes 调度器无法感知缓存，导致应用调度的结果不佳，缓存无法重用，性能得不到提升。</li><li><br><strong>多数深度学习框架并不支持 HDFS 接口，导致开发难</strong>：比如 PyTorch，MxNet 等框架只支持 POSIX 协议接口，HDFS 接口需要额外的对接开发。因此需要同时支持模型开发阶段的 POSIX 接口以及模型训练阶段的 HDFS 接口，引入模型代码适配不同存储的复杂性。</li><li><br><strong>HDFS 成为数据并发访问的瓶颈点，稳定性挑战大</strong>：微博机器学习平台上百台 GPU 机器同时训练都会并发访问 HDFS 集群，同时深度学习训练的 IO 压力比较大，HDFS 服务成为了性能单点，这对 HDFS 的性能和稳定性提出了巨大的挑战。一旦某个任务拖慢了 HDFS 系统，其他的训练任务也会受到影响。而且，一旦 HDFS 无法工作，整个训练集群也会受到影响。</li></ol><br>
<br>通过对微博深度学习平台的监控分析，我们发现：一方面由于 IO 性能问题导致 GPU 等昂贵计算资源不能被充分利用；另一方面，我们也发现集群中的内存和本地硬盘的水位很低，余量较多并且稳定，这是由于多数的深度学习任务并不使用本地磁盘，同时内存使用率也不高。因此我们考虑如果能够充分利用集群自身的内存和磁盘资源加速数据访问会是一种更好的方案。<br>
<br><h1>Fluid + JindoRuntime：为微博深度学习平台提供高效支撑</h1>​<br>
为了能更好满足大规模深度学习模型训练的计算需求，需要取得更好的数据本地性效果。因此，我们希望达到以下目标：<br>
<ol><li><br>计算能够充分利用本地化访问数据，这样数据就不需通过网络反复读取，加速深度学习模型训练的速度和提升集群的 GPU 使用率。</li><li><br>降低 HDFS 负载压力，通过应用对于部分数据的本地读取，减小数据访问延时和提升 HDFS 的可用性。</li><li><br>充分发挥热点数据集的缓存节点优势，在对用户无感知的前提下，智能的将任务调度到数据缓存节点上。让常用的模型训练程序越来越快。</li><li><br>通过 POSIX 接口读取数据，这样无需在模型开发和训练阶段使用不同的数据访问接口，降低开发深度学习模型程序的成本。</li></ol><br>
<br>为了达到上述目标，我们迫切希望找到 Kubernetes 上具有分布式缓存加速能力的软件。很幸运，我们发现 CNCF Sandbox 项目 Fluid 正好可以满足我们的诉求。于是，我们设计了基于 Fluid 的新架构方案，经过验证比较，我们选择 JindoRuntime 作为加速运行时。<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/199e00cf37bc4fa783c83ad79763c895.png" alt="4.png" referrerpolicy="no-referrer"><br>
<br><h2>1. 架构组件介绍</h2>​<br>
<h3>1）Fluid</h3><strong>​</strong><br>
<br>Fluid[1] 是一个运行在 Kubernetes 上可扩展的分布式数据编排和加速系统，它通过数据的编排和使用数据的应用调度，解决云原生编排框架运行此类应用面临数据访问延时高、多数据源联合分析难、应用使用数据过程复杂等痛点。<br>
​<br>
<h3>2）JindoRuntime</h3><strong>​</strong><br>
<br>JindoRuntimed[2] 是 Fluid 一种分布式缓存 Runtime 的实现，基于 JindoFS 分布式缓存加速引擎。JindoFS 是阿里云 EMR 团队自研大数据存储优化引擎，完全兼容 Hadoop 文件系统接口，给客户带来更加灵活、高效的计算存储方案。JindoRuntime 使用 JindoFS 的 Cache 模式进行远端文件的访问和缓存，支持 OSS、HDFS、标准 S3 协议等多种存储产品的访问和缓存加速。在 Fluid 上使用和部署 JindoRuntime 流程简单、兼容原生 K8s 环境、可以开箱即用。深度结合对象存储特性，使用 Navite 框架优化性能，并支持免密、checksum 校验等云上数据安全功能。<br>
​<br>
<h2>2. 使用基于 JindoRuntime 的 Fluid 的原因</h2>​<br>
1. Fluid 可以将数据集编排在 Kubernetes 集群中，实现数据和计算的同置，并且提供基于 Persistent Volume Claim 接口，实现 Kubernetes 上应用的无缝对接。同时 JindoRuntime 提供对 HDFS 上数据的访问和缓存加速能力，并且可以利用 FUSE 的 POSIX 文件系统接口实现可以像本地磁盘一样轻松使用 HDFS 上的海量文件，pytorch 等深度学习训练工具可利用 POSIX 文件接口读取训练数据。<br>
<ol><li><br>针对海量小文件的远程数据访问性能问题，JindoRuntime 对小文件的数据组织管理和访问性能进行了大量针对性的优化，能够提供高效的小文件访问性能，远高于直接对 HDFS 的数据访问性能。</li><li><br>提供元数据和数据分布式分层缓存，以及高效小文件检索。</li><li><br>提供数据预热机制，避免在训练时刻拉取数据造成的数据访问竞争。</li><li><br>Slab allocation 方式组织文件数据，高效利用缓存空间。</li><li><br>通过 Fluid 的数据感知调度能力，用户无需知道缓存节点信息就可以将任务放置到有缓存数据的节点，实现数据访问性能的优势最大化。</li><li><br>对于大文件和小文件提供不同的缓存策略和存储方式，对于小文件 AI 训练场景具有很好的自适应性，无需用户配置。</li></ol><br>
<br><h2>3. 落地实践</h2>​<br>
1. <strong>选择合适的缓存节点</strong>：使用 JindoRuntime 可以获得更好的数据本地性能，在实际生产中我们也发现不是所有的节点都来做缓存性能就比较好。原因是有些节点的磁盘和网络 IO 性能不是很好，这个时候需要我们能够把缓存节点尽量选择一些大容量磁盘和网络较好的节点上去。Fluid 支持 dataset 的可调度性，换言之就是缓存节点的可调度性，我们通过指定 dataset 的 nodeAffinity 来进行数据集缓存节点的调度，从而保证缓存节点可高效的提供缓存服务。<br>
<ol><li><br><strong>指定 Master 调度策略</strong>：JindoRuntime 由 master/worker/fuse 三部分组成，master 负责集群的大脑，负责元数据和集群缓存的管理，所以 master 节点得具有很强的可靠性和故障恢复速度。在生产过程中我们发现在不使用多 master 的条件下，单个 master 也具有很强的稳定性和故障恢复速度，影响 master 节点稳定性的重要因素还是宿主机的稳定性，比如宿主机满磁盘、通信故障等，基于此我们对 mater 节点使用 nodeselector 来选择性能较好的宿主机作为 master 容器的环境，进一步保证 master 环境的稳定性。</li><li><br><strong>定时数据预热</strong>：在进行训练前的一个重要的步骤是进行元数据和数据的预热，Fluid 提供了 CRD 的形式进行元数据和数据的缓存，在训练前将训练文件的元数据和数据缓存到本地，可大大加速训练速度。但是存储在 HDFS 上的训练文件是每天一次更新，于是需要进行周期性定时的进行数据预热流程，基于 dataload 的 CRD，我们使用 cronJob 的形式进行周期性调度，使得在每次训练前都能够完成元数据和数据的准备，从而进行高效训练。当然 JindoRuntime 本身也支持增量同步的功能，所以每次只需要更新变化的文件即可，也大大加快了数据预热的速度。</li></ol><br>
<br><h2>4. 性能测试方案</h2>​<br>
为了验证以上方案的整体效果，我们从稳定性、性能不同角度进行了验证，这里着重介绍性能测试方案，训练的模型都是基于 mmaction 的视频理解模型，采用的是 rawframes_train 方式，是拥有 400w 图片的训练数据集实验，数据是从真实业务场景中提取的 40w 视频中抽帧得到，每个场景下抽 10 帧图片，由于视频清晰度各异，每张图片大小由几 KB 到十几 M 各异，总计大小 780G 左右，每个缓存节点提供 300G 的缓存空间；同时根据经验一般在 50epoch 左右会实现模型收敛。<br>
​<br>
而当我们把测试的视频数据量调整到 100w，总共的数据大小 2T，由于数据量大和延时长，HDFS 接口的方式完全不能工作；而通过 Fluid+JindoRuntime 则可以满足业务的需要。<br>
​<br>
测试的流程是会通过 Fluid JindoRuntime 进行数据预热，之后进行模型训练。<br>
​<br>
<h2>5. 性能测试结果</h2>​<br>
结合 Fluid+JindoRuntime 方案，在数据预热的前提下，我们取得了非常明显的训练速度提升，从下图可以看到：在 3 机 12 卡的场景下，我们发现基于 HDFS 接口读取数据的实验往往会因为网络通信等问题中断，导致实验不能跑完，增加异常处理后，workers 之间的等待时间加长，导致增加卡数并不能增加训练速度，反而会拖慢。可以观察到 1 机 8 卡和 3 机 12 卡的场景总体训练速度基本持平，计算资源的扩容。而通过新的方案，我们发现相比于 HDFS 接口，1 机 4 卡可以得到 5 倍的加速，2 机 8 卡可以得到 9 倍的加速，3 机 12 卡可以得到 18 倍的加速。<br>
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/84b44ba3a7bb4d19a1e31a336735e026.png" alt="5.png" referrerpolicy="no-referrer"><br>
<br>由于训练的速度和稳定性得到了保障，端到端的模型训练时间也得到了显著的提升，训练总时长由原来的 389 小时（16 天）缩短到了 16 小时。<br>
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/67ee9a4629fe4dc1a9a4f4f53e211ee5.png" alt="6.png" referrerpolicy="no-referrer"><br>
<br><h1>总结：从两周到 16 小时的训练速度跃升</h1>​<br>
集成了 Fluid+JindoRuntime 后，显著提升了小文件场景模型训练的性能和稳定性，在多机多卡分布式训练的情况下，可以将模型训练的速度提升 18 倍；将过去需要两周才能完成的训练缩减到了 16 个小时。更短的训练时间和更小的 HDFS 压力，也提升了训练任务的稳定性，将训练的成功率从 37.1% 提升到了 98.3%。目前我们在生产环境的数据量是 4TB，同时随着不断迭代数据量还在持续增长。<br>
<br>微博 AI 训练场景对于数据读取有很高的性能要求，而且海量的小文件对于访问延时也非常敏感，通过 JindoRuntime 的缓存能力可以有效地对大数据存储系统上的数据进行缓存加速，提供稳定可靠的高吞吐、低延时的数据访问性能，同时也可以有效地缓解对后端存储系统的的压力，保证后端存储的稳定性。结合自身的具体场景，优化小文件读取和缓存，不仅可以缓解 HDFS 集群的 IO 压力，也大大提高训练效率。<br>
<br><h1>展望</h1>​<br>
目前 Fluid+JindoRuntime 更像是杀手锏，用来加速小文件场景，而非常规性武器对于所有数据集进行加速优化，我们期望能够把弹性的数据加速作为微博深度学习平台的差异化能力，提升整体训练任务速度和计算资源的利用率；另一方面也帮助社区不断演进，帮助到更多的开发者。具体来说：<br>
​<br>
- 支持定时任务支持动态扩缩容<br>
- 数据预热性能的提升和元数据备份机制的提供，实现快速重建数据集的能力<br>
- 提供性能监控控制台<br>
- 支持 Runtime 元数据的高可用和镜像升级<br>
- 支持规模化 K8s 集群中多数据集的全生命周期管理<br>
<br><strong>致谢</strong><br>
​<br>
感谢阿里云 JindoFS 团队的辰山、扬礼和容器团队的车漾在整个方案设计和优化过程中的巨大帮助，在几乎没有任何应用改造前提下，将数据加速能力赋予了现有应用；同时对于测试和生产环境中的需求和问题也及时专业的提供了支持。<br>
​<br>
<strong>相关链接</strong><br>
<br>更多 Fluid 和 JindoFS 相关介绍请参考以下链接：<br>
<ul><li><br>[1] Fluid：<a href="https://github.com/fluid-cloudnative/fluid">_</a><a href="https://github.com/fluid-cloudnative/fluid_" rel="nofollow" target="_blank">https://github.com/fluid-cloudnative/fluid_</a></li><li><br>[2] JindoFS：<a href="https://github.com/aliyun/alibabacloud-jindofs">_</a><a href="https://github.com/aliyun/alibabacloud-jindofs_" rel="nofollow" target="_blank">https://github.com/aliyun/alibabacloud-jindofs_</a></li></ul>
                                
                                                              
</div>
            