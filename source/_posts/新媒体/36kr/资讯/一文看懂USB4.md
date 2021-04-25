
---
title: '一文看懂USB4'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210425/v2_40b348bd33384203857c629633b26b6d_img_000'
author: 36kr
comments: false
date: Sun, 25 Apr 2021 08:02:27 GMT
thumbnail: 'https://img.36krcdn.com/20210425/v2_40b348bd33384203857c629633b26b6d_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/xdV_7I1YUU730nw6qhByuQ">“半导体行业观察”（ID:icbank）</a>，作者：Tomshardware，36氪经授权发布。</p> 
<p>“USB4”(官方拼写缺少空格，但我们在本文中使用它来反映读者的搜索方式)于2019年首次发布，并被一些电脑所采用，其中包括苹果新推出的M1驱动的 iMac、基于M1的Macbook和Mac Mini，以及搭载<a class="project-link" data-id="3968654" data-name="英特尔" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968654" target="_blank">英特尔</a>第11代Gen Tiger Lake的笔记本电脑。虽然目前采用USB 4的设备并不多，但是新一代USB 4供电的扩展坞和外设正在涌入。</p> 
<p>USB 4能够带来许多好处，包括提供更快的传输速度，更好的视频带宽管理以及与Thunderbolt 3的可选兼容性。</p> 
<p>就目前市场情况来看，各大PC和外设供应商的产品所采用的USB版本有所不同，因此，业界需要为USB制定新的标准。在这其中，有很多值得我们去期待的功能，而这就需要我们来全面地了解下USB 4。</p> 
<h2>USB 4的主要优势</h2> 
<p>新的USB 4标准与以前版本的USB相比有四个主要优点。</p> 
<p>最大传输速度可达40 Gbps：通过使用 two-lane cables,，设备能够以40gbps的速度运行，与Thunderbolt 3相同的速度。数据可在两组四个双向通道中进行传输。</p> 
<p>DisplayPort替代模式2.0：USB 4在其替代模式下支持DisplayPort 2.0。DisplayPort 2.0可以以HDR10颜色支持60 Hz的8K分辨率。DisplayPort 2.0可以使用高达80 Gbps的速度，这是USB数据可用量的两倍，因为它可以在一个方向上（向显示器）发送所有数据，因此可以同时使用所有八个<a class="project-link" data-id="523574" data-name="数据通" data-logo="https://img.36krcdn.com/20201107/v2_8d4e65c101ed4f0faf825308bc1b67fe_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/523574" target="_blank">数据通</a>道。</p> 
<p>与Thunderbolt 3设备兼容：某些（但不是全部）USB 4也可以与Thunderbolt 3设备<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210422/v2_9d94d5f89e394f8082c3b500e50c340d_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>使用。</p> 
<p>更好的视频，PCIe视频资源分配： 其他接口接管连接时可以代替替代模式，USB 4设备可以使用称为“协议通道（protocol tunneling）”的过程，该过程可以同时发送DisplayPort，PCIe和USB数据包，同时相应地分配带宽。</p> 
<p>因此，如果视频仅需要20％的带宽来驱动作为集线器的1080p显示器，则另外80％的带宽则可用于外部SSD传输文件，这部分可通过USB协议或PCIe进行操作。</p> 
<h2>使用Type-C 端口</h2> 
<p>毫无疑问，USB 4将只能通过Type-C连接器操作。Type-A端口的USB 4设备或集线器不可能出现。这不足为奇，因为其他最新标准（例如USB Power Delivery）仅适用于Type-C。如果使用适配器连接到Type-A，5 Gbps USB 3端口，那么将会对速度和功耗产生巨大的影响。</p> 
<h2>与Thunderbolt 3兼容（可选）</h2> 
<p>英特尔曾表示已将Thunderbolt 3协议授予USB Promoter Group，从而使具有USB 4端口的设备可能与Thunderbolt 3设备互相兼容。这对所有人来说都是个好消息，尤其是那些想通过连接eGPU(外置显卡)来玩游戏的笔记本电脑用户。</p> 
<p>虽然市面上有很多Thunderbolt 3的eGPU，但很少有笔记本电脑和台式机配备Thunderbolt 3，而且几乎没有主板支持Thunderbolt 3。因为Thunderbolt是英特尔的标准，你不会在任何amd驱动的电脑上找到它。Thunderbolt 3的实现成本也高于标准USB，因为它不是开放标准，而且需要额外的芯片。所以今天，如果你想要一个eGPU或一个超快速的Thunderbolt 3存储驱动器，你的电脑选择是非常有限的。</p> 
<p>借助USB 4，设备和主机制造商将不必向英特尔支付任何专利费，因此有更大的机会被广泛采用。然而，有一个问题:Thunderbolt兼容性不是USB 4规格的必要部分，所以制造商不需要实现它。您可能最终购买了带有USB 4的笔记本电脑，却发现它不能与您的Razer Core X图形扩展坞一起使用。 </p> 
<p>“我们确实期望PC供应商广泛支持Thunderbolt的向后兼容性，因为他们所需的大多数东西已经内置在USB 4设计中”，USB开发者论坛主席Brad Saunders表示：“这是基于相同的技术，所以我们确实预计会有很高的普及率，但手机制造商可能会选择不添加额外的一点，他们需要向后兼容。”</p> 
<p>到目前为止，苹果公司称其M1计算机具有Thunderbolt 3 / USB 4端口，而新的Tiger Lake笔记本电脑（如Dell XPS 13）则表示它们支持USB 4 / Thunderbolt4。不幸的是，尽管拥有这些端口，但新Mac电脑却没有。不能与外部GPU配合使用。</p> 
<p>然而，重要的是要记住，Thunderbolt 3和Thunderbolt 4是英特尔认证的项目，这些计划需要花费制造商的时间和金钱。因此，虽然支持USB 4的计算机可以与40 Gbps设备甚至是标记为Thunderbolt的设备一起使用，但如果未通过认证，则可能不会被列为支持Thunderbolt的设备。 </p> 
<p>例如，手机或平板电脑供应商可以通过不提供40 Gbps的传输速度或不支持PCIe数据传输来节省成本。你不会(也不能)将你的手机连接到eGPU或高性能的外部SSD。</p> 
<h2>USB 4的两种速度</h2> 
<p>虽然它可以达到40 Gbps的理论速度，但并不是所有的USB设备或主机都支持这个标准。预计更小、更便宜的设备，如手机和chromebook，将使用每秒20 Gbps的USB 4版本，它仍然比USB 3快得多。今天你可以从大多数笔记本电脑上获得5 Gbps的连接(尽管存在10 Gbps和20 Gbps的USB 3.2连接)。如果你想要最快的USB 4连接，请务必查看说明书。</p> 
<h2>USB 4标签不会使用版本号</h2> 
<p>那么，您如何知道所购买的设备是否兼容USB 4？制造商可能会在规格表中提到USB 4，但USB-IF的标识程序仅专注于连接的传输速度，即20或40 Gbps。 </p> 
<p><img src="https://img.36krcdn.com/20210425/v2_40b348bd33384203857c629633b26b6d_img_000" data-img-size-val="792,335" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc">图片来源：USB Implementers Forum</p> 
<p>你会在零售包装上看到认证标识，偶尔也会在设备本身上看到，它将被标记为USB 20gbps或USB 40gbps，或者USB三角形标志旁边有一个20或40。</p> 
<p>现在，重要的是要注意，还有一个SuperSpeed USB 20gbps标准，技术上USB 3.2，它没有USB 4的其他功能。而这将有一个不同的标识。</p> 
<p>还值得一提的是，市场上数以百万计的USB产品均未获得USB-IF的官方认证，因此它们根本无法使用这些标识。因此，尽管组织已尽力而为，但您可能仍会在其产品说明中看到很多使用术语USB 4的产品。 </p> 
<h2>在视频和数据之间共享带宽方面表现优秀</h2> 
<p>USB 4规范的很大一部分是协议通道，当你通过同一连接发送视频和数据时，可以动态调整可用资源的数量。因此，假设您拥有最大40 Gbps的USB 4，并且正在从外部SSD复制大量文件的同时输出到4K显示器。让我们规定视频源需要大约12.5 Gbps。在这种情况下，USB 4会将剩余的27.5 Mbps分配给您的备份驱动器。</p> 
<p>USB-C引入了“替代模式”，即能够从Type-C端口传输DisplayPort / HDMI视频的功能，但是当前的3.x规范并未提供拆分资源的好方法。根据桑德斯（Saunders）的说法，DisplayPort替代模式可以将USB数据和视频数据之间的带宽精确地分配为50/50，而HDMI替代模式根本不允许同时传输USB数据。 </p> 
<p>但是，通过协议通道传输，USB 4可以将DisplayPort，PCIe或USB作为数据包发送，因此可以控制资源分配。 </p> 
<p>“使用USB SuperSpeed，我们在架构上没有足够的灵活性，没能够真正地在连接器上以组合方式管理这两个不同的带宽（数据和视频）”， Saunders说：“而新技术的出现，则优化了不同应用之间的可扩展性。”</p> 
<h2>所有USB 4主机均支持USB PD</h2> 
<p>当前的一些USB Type-C设备支持USB Power Delivery (USB PD)标准，用于为大功率设备输送电力，但并非所有的设备都支持。每个USB 4设备和主机将必须遵守USB PD，这样才能提供更高的功率和更好的电源管理。</p> 
<p>USB PD理论上可以提供高达100瓦的功率，但充电设备不必支持该功率。因此，不能保证给定的USB 4端口能够提供或占用特定笔记本电脑运行所需的数量，但是您可以期望它符合规格。</p> 
<h2>向后兼容旧设备</h2> 
<p>关于所有USB版本，最好的事情是它们如何协同工作。USB 4可与USB 3和USB 2设备和端口一起使用。不用说，您只会<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>连接中最薄弱那部分的速度和功能。当你把USB 4连接到一个USB 3.2端口时，它的传输速度不会达到40 Gbps，而一个老式的USB 2端口也不会因为你连接到一个全新的USB 4备份驱动器而突然变得更快。</p> 
<h2>您旧的数据线将以其最大速度工作</h2> 
<p class="image-wrapper"><img data-img-size-val="831,575" src="https://img.36krcdn.com/20210425/v2_838f01031212489b8d7c8f94f35d79da_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc">图片来源：Shutterstock</p> 
<p>您现有的USB数据线和适配器可与USB 4配合使用，但与其他所有向后兼容的产品一样，它们仅能以其最大额定速度运行。所以，如果你有一根可以以每秒5Gbps速度运行的USB 3.2数据线，那么即使你用它来连接USB 4端口到USB 4设备，你也只能达到每秒5Gbps。要获得Thunderbolt 3支持，您可能需要Thunderbolt 3数据线。</p> 
<h2>Thunderbolt 4拥有与USB 4一样的功能</h2> 
<p>在USB 4出现的同时，英特尔的Thunderbolt 4也进入了市场，但是这两个标准实际上并没有竞争。要使计算机或外围设备获得Thunderbolt 4认证，制造商必须获得英特尔的认证，证明其能够支持USB 4的所有功能，包括对Thunderbolt 3的支持。</p> 
<p>Thunderbolt 4只是一个认证，证明该设备已被英特尔认可，并支付了制造商一定费用。如<a class="project-link" data-id="376073" data-name="果您" data-logo="https://img.36krcdn.com/20201106/v2_0cfbcc847cfd4708bba80947653719aa_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/376073" target="_blank">果您</a>看到一个产品宣称支持Thunderbolt 4，则真正的意思是它是具有40 Gbps连接性并且与Thunderbolt 3设备向后兼容的USB 4。但是，正如我们所看到的，即使像兼容“ Thunderbolt 3”的新Apple MacBook Pro也可能无法与Thunderbolt 3 eGPU一起使用。 </p> 
<p>“Thunderbolt 4是一个品牌推广项目”，Saunders 说：“正如英特尔所传达的，这个品牌计划实际上是USB 4，它需要支持所有高端功能，其中一些是可选的。”</p> 
<h2>成本将超过USB 3.2</h2> 
<p>大规模采用USB 4的一个挑战是成本的增加。虽然我们不知道PC和设备厂商增加USB 4连接的具体成本是多少，但我们知道它需要比当前最新标准USB 3.2更昂贵的组件。</p> 
<p>“我认为它将比Thunderbolt便宜，但在产品开发商的实际材料成本方面，它不会像SuperSpeed那么便宜”，Saunders说：“在这其中有很多事情需要去完善，使得该产品可以完成所有SuperSpeed的工作。”</p> 
<p>Saunders补充说，他希望成本能够迅速下降。但是，我们猜测至少在一开始，成本差异会将USB 4供给高端PC使用。</p> 
<h2>为什么USB 4被正式拼写为“ USB4”（没有空格）</h2> 
<p>与其他USB版本不同，新规范的正式拼写是在版本号前没有空格。虽然我们认为大多数人可能会将其写为USB 4，但官方名称是USB4。USB Promoter Group首席执行官布拉德·桑德斯（Brad Saunders）解释说，他删除空间的目的是将重点从版本号转移到<a class="project-link" data-id="4260022" data-name="品牌名" data-logo="https://img.36krcdn.com/20210422/v2_0e0d30565f9c4de9b324d0432e62f383_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4388500024" target="_blank">品牌名</a>称上。</p> 
<p>他告诉我们：“我现在要传达的信号之一是，我们不打算进入4.0、4.1、4.2的迭代路径。我们不希望它与产品联系在一起，并被用作差异化产品……我们想让它尽可能简单。”</p> 
<p>USB 3.x规范已经填充了不同的版本号，包括USB 3.0, USB 3.1 Gen 1, USB 3.1 Gen 2和四个不同的USB 3.2版本，除了有或没有可选的功能，如USB PD和替代模式。但是Saunders告诉我们，这些数字确实适合开发人员，他希望OEM在推销产品时会使用更简单的术语，例如“ SuperSpeed USB”。</p> 
<p>也许是因为担心营销人员向消费者抛出太多数字，Saunders说，该组织不计划使用版本号来更新规格。因此，即使两年内有更快的迭代速度，它也可能仍被称为USB 4，但是速度会更高（我们想象像USB 4 80 Gbps之类的东西）。他和他的团队还没有决定一个品牌战略，所以USB 4可能还会有一个营销名称。很像USB 3.x被称为“SuperSpeed USB”，USB 4可能最终会有自己的名字(我们建议“supersuperspeed USB”)。</p> 
<p>“我希望这是一个明确的区别。USB 4有它自己的架构和速度，并试图不被困于在某个版本号中规定某个速度，”他说。“如果速度加快，我们就能获得更快的认证和品牌。”</p> 
<h2>今日的USB 4产品</h2> 
<p>在撰写本文时，市场上以“USB 4”设备销售的设备屈指可数。这些包括金斯顿SD5700T，Acasis M.2 NVMe机箱，OWC Thunderbolt集线器和Cable Matters 40 Gbps数据线。</p> 
<p>即使没有专用的USB 4外设，你也可以通过连接Thunderbolt 3扩展坞、eGPU和高速SSD来使用该规范。</p>  
</div>
            