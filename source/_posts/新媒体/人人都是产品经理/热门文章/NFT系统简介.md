
---
title: 'NFT系统简介'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://image.yunyingpai.com/wp/2022/05/rvP7zbFzAKgKjJJLFmUh.png'
author: 人人都是产品经理
comments: false
date: Mon, 09 May 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/05/rvP7zbFzAKgKjJJLFmUh.png'
---

<div>   
<blockquote><p>编辑导语：NFT即非同质化代币，近两年来，发展状况愈演愈烈、十分火热，它顺应了年轻人的喜好，成功吸引了年轻一代的追求。本篇文章对NFT进行了详细的、系统的介绍，希望能给您带来帮助。一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5318948 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/rvP7zbFzAKgKjJJLFmUh.png" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、NFT简介</h2>
<p>非同质化通证（Non-Fungible Token，NFT）是一种架构<strong>在区块链技术上的，不可复制、篡改、分割的加密数字权益证明，可以理解为 一种去中心化的“虚拟资产或实物资产的数字所有权证书”</strong>。</p>
<p>从技术层面来看，NFT以智能合约的形式发行，一份智能合约可以发行一种或多种NFT资产，包括实体收藏品、活动门票等实物资产和图像、音乐、游戏道具等虚拟资产。</p>
<p>从物理层面来看，NFT仅仅是一串机器生成的数据，由于底层技术赋予的不可篡改性等特点，它被用于权利证明。</p>
<p>理解 NFT 本质：简而言之——<strong>由智能合约创建、维护、执行的非同质化数字资产通证</strong>。NFT智能合约记录了每个NFT资产的token ID、资源存储地址及它们的各项信息。</p>
<p>NFT储存于区块链上，但受到成本影响，其映射的实物资产或数字资产一般不上链，而是储存于其他中心化或非中心化的存储系统中，如IPFS，并通过哈希值或URL映射上链。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/o0vZXFoA3QsiifBrQP1D.png" alt="NFT系统简介" width="555" height="165" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/snDB5FSRIqBGWbHpJlrm.png" alt="NFT系统简介" width="580" height="479" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、NFT功能价值</h2>
<h3>1. NFT功能：实现资产的去中心化认证与交易</h3>
<ul>
<li>从认证角度来讲：核心原因是由于认证的不可篡改性和永久性，不可篡改属性实现基础是基于区块链技术的数据交易过程公开以及分布式存储。</li>
<li>从交易角度来讲：除了不可篡改、公开可追溯之外，还由于成本因素，因为 NFT 对应的是资产，中心化机构做中间信任机构有中介成本，而 NFT基于区块链，区块链本身就是基于信任的机器，消除中间成本。</li>
</ul>
<h3>2. NFT价值=虚拟货币+资产权证+流动性</h3>
<ul>
<li>NFT作为铸造在区块链上的非同质化代币，主要通过虚拟货币进行交易，因此 NFT具备一定的虚拟货币价值。</li>
<li>NFT作为资产的数字权证代表了资产本身价值，同时NFT的技术特征赋予了资产所有权流动性和可追溯性，一方面流动性增加了资产价值，另一方面可追溯性解决了艺术藏品等资产辨伪、确权的痛点。</li>
<li>NFT的流动性赋予了资产增量的交易价值。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/sKhjEQeFAlrCr0RyWoSf.png" alt="NFT系统简介" width="522" height="387" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、NFT底层技术</h2>
<p><strong>NFT 基于的底层技术——区块链</strong>。<strong>NFT 所具有的唯一公开、不可篡改、可交易等属性均是基于当前的区块链技术实现。</strong></p>
<p>区块链的数据结构分为区块头、区块体，不同区块之间通过前一区块头的哈希值连接，形成链式结构，区块头与区块体之间通过默克尔根字段相连。以以太坊为例，区块头中存储的数据主要包括父区块头哈希值、当前区块交易相关的默克尔树根节点哈希值、区块难度值、矿工地址、区块高度、Gas 上限、Gas 使用、时间戳、Nonce 值等，区块体中存储的数据包括交易记录表和叔区块，其中 NFT 的交易记录存储于区块体的数据记录表中，由矿工打包。</p>
<p>区块链结构简易图如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/34OiGI7WNhtb4GGirBak.png" alt="NFT系统简介" width="646" height="373" referrerpolicy="no-referrer"></p>
<p>区块链上确认打包入块的数据不可篡改，将永久存于链上。NFT 的数据信息上链确认后，将无法再进行修改。当矿工或者超级节点采用共识算法完成出块后，会通过 P2P 协议向全网广播（P2P 协议是一种分布式网络协议，早于区块链技术出现），各个节点在收到广播信息确认后，会将信息更新，这一机制实现了去中心化的分布式记录，通过共识算法保证恶意节点无法篡改信息。</p>
<h3>1. 区块链分类</h3>
<p><strong>根据去中心化程度可以分为 3 类链，分别是公链、联盟链以及私链。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/Ep9PWYgvSjCRiA9du0wt.png" alt="NFT系统简介" referrerpolicy="no-referrer"></p>
<h3>2. 共识算法</h3>
<p><strong>区块链建立去中心化信任的基础是共识算法</strong>，当前主流公链共识算法分为 3 类，分别为 PoW、PoS、DPoS：</p>
<ul>
<li>PoW 算法：比特币、以太坊 1.0 采用 PoW 算法，即 Proof of Work，工作量证明。以比特币为例，不断进行 SHA256 计算，最终找出满足给定数量前导 0 的哈希值的节点有权出块；</li>
<li>PoS 算法：以太坊 2.0 采用该算法，Proof Of Stake，权益证明，引入币龄概念，持有币越多获得出块的概率越高，该算法降低了计算量，提升了 TPS（每秒并发交易量），牺牲了一定去中心化程度；</li>
<li>DPoS 算法：Delegated Proof of Stake，各节点将手中的代币抵押投票给最有能力、有信誉的节点出块，以 EOS 区块链为例，全网投票选出 21个超级节点，21 个超级节点轮流去生产区块，这一算法可以大幅提升 TPS，但去中心化程度进一步降低</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/4Jxl4jmVhDxp9We9cVDi.png" alt="NFT系统简介" width="790" height="92" referrerpolicy="no-referrer"></p>
<h3>3. 智能合约</h3>
<p><strong>标准协议：NFT 通过智能合约 ERC-721、ERC-1155 等标准合约形式部署在区块链上</strong>。智能合约即部署在区块链上的一段可执行代码，ERC-721 标准适用于任何非同质化的数字内容，ERC-1155 更多用在游戏中，用于标识一类道具。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/9NEzQ1mVjUJM1WymvR44.png" alt="NFT系统简介" width="712" height="311" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/UBaK3Sy04l0KWHqW8tJP.png" alt="NFT系统简介" width="727" height="264" referrerpolicy="no-referrer"></p>
<p><strong>智能合约交易触发与执行机制：</strong>交易是连接外部世界和以太坊内部状态的桥梁，所以以太坊也被称为交易的状态机，NFT 的智能合约部署完成后，外部调用 RPC 接口访问以太坊主网，矿工将交易打包，EVM（以太坊虚拟机）找到对应智能合约并根据外部传入参数执行对应的合约函数，执行完成后在链上将状态更新。</p>
<p><strong>举例：</strong>无聊猿 NFT 开发方将智能合约代码部署至以太坊，NFT 交易平台OpenSea 收录并展示，当其中一名用户在 OpenSea 平台发起购买此无聊猿 NFT 操作，OpenSea 调用 RPC 接口访问以太坊主网发送交易请求，矿工打包交易找到智能合约执行，将链上状态更新完成交易。</p>
<p>以太坊中继在服务集群中充当的是一座连接传统服务器端和以太坊区块链的桥梁，中继负责公链上相关功能的实现，几乎囊括了目前以太坊的DApp 的绝大部分功能。</p>
<p>所谓 RPC 协议，就是规范了一种客户端和实现了 RPC 接口的服务器端交互时的数据格式。RPC 接口实现的大致流程，服务的调用方按照规范好的编码方式把某个 RPC 接口的函数名称和参数进行序列化编码后，发送到服务的提供方即服务器端，服务器端再通过反序列化后把对应的参数提取出来，然后通过调用相关函数，最后把结果返回给服务的调用方。</p>
<p>以太坊智能合约交互模型如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/nk0F5s8MksUypMM5Zg3Z.png" alt="NFT系统简介" width="728" height="207" referrerpolicy="no-referrer"></p>
<p>以太坊智能合约执行流程如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/7KaLYTglxfefldvfgdU7.png" alt="NFT系统简介" width="655" height="352" referrerpolicy="no-referrer"></p>
<p>支持智能合约的区块链一览：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/XipMXNk6g9uuLONDVSNl.png" alt="NFT系统简介" width="722" height="320" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、NFT产业链</h2>
<p>NFT产业链包含<strong>上游基础设施层（结算层）、中游项目创作层（协议层）以及下游衍生应用层</strong>。上游基础设施层为NFT铸造和交易提供基础设施支持，中游项目创作层根据铸币协议铸造NFT并在一级市场发行，下游衍生应用层则围绕一级市场铸造的NFT衍生出NFT二级市场、数据平台和社交平台等。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/uwp6KaNJzfPW32Pa3PYD.png" alt="NFT系统简介" width="627" height="318" referrerpolicy="no-referrer"></p>
<h3>1. 上游基础设施层</h3>
<p><strong>1、以太坊是NFT领域基础设施的绝对霸主</strong></p>
<p><strong>NFT是架构在区块链技术上的加密数字产权证明，NFT的铸造、发行、流通及其衍生应用需要一个较为成熟的可用性强的区块链及其底层生态（开发工具、存储、钱包等）作为底层基础设施支撑。</strong></p>
<p>NFT基础设施层负责价值的记录与结算，搭建起整个NFT生态的安全性和最终性。NFT中下游应用的发展空间受限于上游NFT基础设施层的性能及互操作性。</p>
<p>NFT基础设施层的搭建包含点对点互联网协议、平台中立的计算描述语言、数据储存协议、去信任的交互平台、去信任的交互协议、瞬态数据传输。</p>
<p><strong>以太坊（ETH）的NFT生态发展较早，形成了ECR721、ECR1155等非同质化通证协议标准，是目前NFT领域的基础设施的绝对霸主。</strong></p>
<p>根据Cryptoslam的统计，近30日（9.16-10.15）NFT领域的交易总额为24.41亿美元，其中有71.48%基于以太坊，另外有18.52%基于以太坊的侧链Ronin（主要为Axie Infinity），其余区块链除Solana外占比不足1%。</p>
<p>架构在以太坊上的NFT收藏项目包揽了近30日（9.16-10.15）交易额排名Top10中的9个，包括Art Blocks、CryptoPunks等项目，并占据了历史交易总额（截至10.16）排名Top100的84个。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/ZplaARQ92Aj0HZuVZep6.png" alt="NFT系统简介" width="626" height="267" referrerpolicy="no-referrer"></p>
<p><strong>2、以太坊之外的三种基础设解决方案</strong></p>
<p>对于单个NFT项目尤其是新项目来说，<strong>受以太坊手续费过高（高Gas费）、网络拥堵严重、用户体验差的限制，NFT很难形成规模化市场。</strong></p>
<p><strong>对此，基础设施解决方案主要分为三大类：一是除了以太坊之外对于NFT友好的其他Layer 1区块链，适用于NFT发展的优质公链包括Flow和Near；二是侧链，包括Polygon，xDai以及Ronin；三是以太坊的Layer 2扩容解决方案包括Immutable X。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/PEOnaOQESzCh4SCtvlG6.png" alt="NFT系统简介" width="642" height="275" referrerpolicy="no-referrer"></p>
<p><strong>3、去中心化存储技术</strong></p>
<p>目前主要的去中心化存储的技术为 IPFS（InterPlanetary File System），Filecoin 是建立在 IPFS 技术上的激励层分布式存储项目，此外还有链上永久存储项目Arweave。</p>
<p>IPFS 又名星际文件系统，是一种实现文件分布式存储和多点传输的网络传输协议，IPFS 协议用算法将文件切分为多个小块，分散存储到各个节点，当请求文件时，将各个节点的小块再次拼接成完整文件。</p>
<p>这一模式有赖于节点的数量要足够多，不然就会遇到类似于 BT 文件由于没有节点维护、存储而丢失无法下载的情况。</p>
<p>为了解决这一问题，Filecoin 项目 2020 年正式上线，在 IPFS 基础上搭载了一个基于区块链技术的激励层，发行了 Fil 代币，用于激励更多矿工（节点）维护数据，用户在存储和读取数据时需要支付 Fil 代币，目前 Filecoin全球活跃节点 3761 个，算力总量达到 15.5EB。</p>
<p>Arweave 项目，2018 年上线，拥有自己的底层架构和经济激励层，发行AR 代币，一次存储支付，上链永久保存，后续访问数据完全免费，目前Arweave 全球活跃节点 203 个，数据总量达到 47TB。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/hOADZnvzHA3svkeJHzUx.png" alt="NFT系统简介" width="747" height="185" referrerpolicy="no-referrer"></p>
<p>去中心化存储技术的不断完善，为 NFT 项目的数据永久存储建立了基础，进而从资产确权、存储两端都实现了去中心化，进一步降低链下数据被篡改的风险。</p>
<h3>2. 中游项目创作层</h3>
<p><strong>1、主流NFT协议标准对比（与上文智能合约部分内容重复）</strong></p>
<p><strong>NFT行业中游项目创作层也称为协议层，NFT的铸造遵循底层基础设施的标准协议，目前以太坊最常见的三大NFT标准协议包括ERC721、ERC1155和ERC998，其中ERC721协议和新晋的ERC1155协议是目前应用最广泛、知名度最高的NFT主流协议标准。</strong></p>
<ul>
<li>ERC721诞生自CryptoKitties开发团队，ERC721标准定义了非同质化代币的4个关键元数据：全局ID，名称NAME，符号SYMBOL，URI统一资源标示符，这也成为当今绝大多数NFT的中间协议层。但ERC721协议标准下一份合约只能发行一种NFT资产，以太坊智能合约平台的Solidity语言目前还做不到统一管理不同合约的资产，因此难以胜任需要调用大量资产的应用场景，如游戏道具、活动门票等。</li>
<li>ERC1155在ERC721的基础上进行延伸，支持一份合约发行任意种类的NFT资产，大幅节约了发行和交易NFT时的手续开销，同时支持批量转移（如转账多数量的同一类别资产或多类别资产），提高了转移的便捷程度。但ERC1155标准移除了元数据的名称（NAME）和符号（SYMBOL），牺牲了本身的描述能力。ERC1155标准在进行多种资产转移过程中无法追踪单个资产，这一定程度上是严重的信息损失，并将描述资产的权力让渡给上层的应用层后端（如二级交易市场），这牺牲了网络的去中心化程度。</li>
</ul>
<p><strong>除三大NFT标准协议外，市面上还有EIP1948（可存储动态数据的NFT）、EIP2981（专注于NFT版税的以太坊协议）、ERC809（可租用的NFT）等。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/rqBm7enNknjlZ1XOr61V.png" alt="NFT系统简介" width="672" height="245" referrerpolicy="no-referrer"></p>
<p><strong>2、市场集中度较高</strong></p>
<p><strong>NFT项目集中度较高，历史成交额Top5项目占据超一半的市场份额。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/e8enMcme1PNw06xek9tr.png" alt="NFT系统简介" width="657" height="299" referrerpolicy="no-referrer"></p>
<p><strong>目前NFT的应用领域主要集中在收藏品、艺术品和游戏领域</strong>。按照NFT映射的资产的不同，NFT项目可分为以下几种类型：收藏品、艺术品、游戏、元宇宙、应用程序、体育运动、去中心化金融等。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/lvIxZgM74AGRTlbxqFvv.png" alt="NFT系统简介" width="698" height="308" referrerpolicy="no-referrer"></p>
<h3>3. 下游衍生应用层</h3>
<p><strong>1、丰富应用方向</strong></p>
<p>衍生应用层主要是基于项目创作层铸造出的NFT衍生出的应用，涉及收藏品/艺术品、游戏、元宇宙、公用事业、DeFi等。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/QP8dksn3tTARvjYT4XsJ.png" alt="NFT系统简介" width="658" height="275" referrerpolicy="no-referrer"></p>
<p><strong>2、NFT商业模式</strong></p>
<p>NFT生态系统中，传统的营利模式为直接出售NFT资产、在二级交易市场进行交易时收取手续费和游戏内部的交易收取手续费等。而Defi经济的进一步繁荣也为NFT生态带来了新的盈利模式。</p>
<ol>
<li><strong>治理代币</strong>，即游戏开发者可以通过向社区成员出售治理代币来获取收入，获取治理代币的游戏社区成员可以获得一定的投票权，对游戏未来的发展方式提出新的建议甚至提出新的功能等。</li>
<li><strong>收入分成代币</strong>，即游戏开发者还可以通过推出具有收入分发功能的代币发放给游戏玩家，持有代币的玩家可以在游戏中获取游戏运营商扣除之外的游戏收益。</li>
<li><strong>认购</strong>，用户将加密资产投入到Defi协议或资金池中，将产生的收益提供给游戏开发者，作为与游戏的入场券或其他服务的获取资格。</li>
<li><strong>原生代币</strong>，即NFT项目开发自己的NFT代币，作为游戏或其他项目中获取虚拟资产的唯一货币。</li>
<li><strong>拆分</strong>，目前的部分NFT交易平台允许用户将一个NFT资产拆分成ERC-20（即FT）类型的资产并在平台进行交易，比如NIFTEX平台。</li>
<li><strong>抵押贷款</strong>，即通过抵押NFT来获取资产，对比银行的资产，该种贷款方式下款更快</li>
</ol>
<p><strong>NFT平台商业模式展示图：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/B7igfj3iPkaNhMTm0QTU.png" alt="NFT系统简介" width="741" height="255" referrerpolicy="no-referrer"></p>
<p><strong>主流NFT交易市场商业模式对比：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/XeZyGhThKuZgGWrBHDHl.png" alt="NFT系统简介" width="618" height="562" referrerpolicy="no-referrer"></p>
<p><strong>3、二级交易平台</strong></p>
<p>目前较为活跃的二级加密交易平台包括 OpenSea、Nifty Gateway、MakersPlace、Rarible、SuperRare 和 VIV3，这些市场也提供一级市场铸币和发行服务。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/9ivZJ0cxZGVS6UL4gUlO.png" alt="NFT系统简介" width="720" height="350" referrerpolicy="no-referrer"></p>
<p>目前OpenSea已成为全球最大的NFT交易平台，2021年7月公司获得了1亿美元的B轮融资，OpenSea的整体估值达到15亿美元。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/5OjvA5G4iWAPLfVjMphT.png" alt="NFT系统简介" width="652" height="223" referrerpolicy="no-referrer"></p>
<p><strong>OpenSea的竞争壁垒在于平台领先的交易用户规模和丰富的NFT项目：</strong></p>
<ul>
<li>支持跨链交易，搭载Ethereum（以太坊主链）、Polygon（侧链）、Klaytn（侧链）3种区块链，支持MetaMask等4种钱包</li>
<li>可交易的NFT项目涵盖收藏品、艺术品、域名等8种类型</li>
<li>以零门槛、低费率、易操作的界面向用户提供NFT铸造/交易/查找等功能</li>
</ul>
<p><strong>OpenSea的竞争对手将主要来自具备优质NFT项目孵化能力的平台。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/kzHCqQvnrAaYcMnQg0Ce.png" alt="NFT系统简介" width="637" height="304" referrerpolicy="no-referrer"></p>
<p>OpenSea平台NFT内容铸造过程：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/pjBy3LeaqT50Os7wBWWy.png" alt="NFT系统简介" width="739" height="240" referrerpolicy="no-referrer"></p>
<p>OpenSea平台购买NFT过程：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/3P6azvAzkR8vVFG0YfYG.png" alt="NFT系统简介" width="712" height="235" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、国内NFT生态</h2>
<p><strong>互联网巨头进场，监管体系底层架构尚未成熟，探索数字藏品领域的应用。</strong></p>
<p><strong>国内主要NFT产品时间线：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/nkYMmAOXRiIsk72lSovp.png" alt="NFT系统简介" referrerpolicy="no-referrer"></p>
<p><strong>国内NFT交易平台：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/52yzWWirwTP4HMYPtQTf.png" alt="NFT系统简介" referrerpolicy="no-referrer"></p>
<p><strong>国内虚拟货币相关政策：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="NFT系统简介" src="https://image.yunyingpai.com/wp/2022/05/cfqCUwF9rm3SkseRwgS7.png" alt="NFT系统简介" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、风险提醒</h2>
<p><strong>（1）政策监管风险</strong></p>
<p>现阶段我国尚未出台针对NFT的监管体系，考虑到海外NFT市场相关的虚拟货币、投机炒作都是我国监管政策的红线，NFT应用在国内市场落地可能会面临一系列监管政策。</p>
<p><strong>（2）发展不及预期</strong></p>
<p>目前国内 NFT 资产交易尚处于初级阶段，二级市场交易尚未完整铺开，若 NFT 资产不能合法流通，则可能影响相关数字版权公司借助 NFT 技术实现相关产品的交易和发售。</p>
<p><strong>（3）技术进步低于预期</strong></p>
<p>NFT 技术除应用于收藏品领域，在区块链游戏方面已有良好探索，且未来有望成为元宇宙的基建，若包括元宇宙在内的新技术发展低于预期，则会影响 NFT 资产交易的市场规模，进而影响相关平台和产品的佣金提成。</p>
<p>个人学习记录，欢迎大佬交流~</p>
<p> </p>
<p>本文由@38度产品 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5428974" data-author="759020" data-avatar="https://image.woshipm.com/wp-files/2018/09/rYYL1y0sA19h8Y53s25S.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">1人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/woshipm_def_head_2022_4.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            