
---
title: '以数据编排技术提高数据提取效率，「Alluxio」已收获全球五大云厂商用户'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2073'
author: 36kr
comments: false
date: Tue, 13 Apr 2021 00:20:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=2073'
---

<div>   
<p>随着数字经济的发展，企业数字化转型的不断推进，企业数据规模正在以前所未有的速度迅速扩大，大数据、云计算、AI分析等诸多技术应用<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>了快速应用。同时，计算量和存储量不匹配而影响运行效率的问题日渐凸显。由此，计算与存储分离的架构（如分布式架构）渐渐成为主流，算力的按需使用成为可能。 </p> 
<p>但新的问题也随之出现:如今，企业拥有PB级数据已经成为常态，EB级数据时代也将很快到来，但是面对复杂、多元的海量数据，企业快速、精准地找到有效数据，合理分配相应的算力资源的难度也越来越大，相应的企业投入的用于数据进行管理、处理、分析的人力、财力也越来越多，希望通过技术手段优化数据管理，提升数据使用率的需求也越来越大。</p> 
<p>为了应对这些问题，36氪曾报道过的「Alluxio」构建了一个计算层和存储层之间的桥梁，在二者之间抽象出一个易使用、标准化的数据编排层（Data Orchestration），来屏蔽异构的存储和复杂的部署。这是面向云环境的的开源数据编排软件，能够跨集群、跨区域和跨国家将数据从存储层移动到距离数据驱动型应用（如数据分析、AI /ML应用程序）更近的位置，从而能够更容易被访问，从而使得数据的访问速度能比现有方案快几个数量级。 </p> 
<p>“数据编排平台就好比构建了一个数据‘滴滴’平台，一方面将各类型、存储在各个不同地方的数据，也就是各个型号的‘车’进行虚拟化统一到平台中；另一方面，接受各类应用的需求，按需快速匹配相应的数据（车）。”Alluxio创始人李浩源告诉36氪，“如此，数据编排平台简化应用程序访问其数据的方式，其最大的价值就是提升了企业从数据中提取有效信息的效率，从而加速了数据应用的市场化速度，以AI应用为例，Alluxio可以帮助提升4倍以上的市场化效率。而对于云厂商而言，Alluxio也可助其突破I/O瓶颈，提升性能。”</p> 
<p>比如，几家云EMR团队与Alluxio社区合作，探索出了开箱即用的计算存储分离优化版本，大幅优化网络带宽，带宽削峰10%-95%，节省总带宽10%-50%，同时能在IO密集型场景提升性能10倍；云端一站式数据管理与分析平台 Kyligence 集成 Alluxio 架构后，查询响应性能提升了大概在50%以上，云上 API Call 的次数也减少了70%。 </p> 
<p>此前，36氪曾详细介绍过Alluxio的成立背景、产品原理、特征优势及其相关应用的情况。经过近6年的发展，如今，Alluxio已在全球Web规模的现代化数据服务的生产环境中得到验证，在包括<a class="project-link" data-id="7133" data-name="阿里巴巴" data-logo="https://img.36krcdn.com/20201030/v2_504c85fa199d4413a7f31069f7faa667_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/7133" target="_blank">阿里巴巴</a>，Facebook，微软，腾讯等诸多行业领导者的生产环境中落地，Alluxio的智能数据分层和数据管理的功能已经为金融、高科技、零售、电信领域和基因制药的客户提供了服务。</p> 
<p> 今年2月初，Alluxio公布了其2021财年的报告，其中显示2021财年（2020年2月-2021年1月）营收比2020财年增长3.5倍，实现正现金流。在这一年中，Alluxio实现了为全球排名前六公有云中的五家提供数据编排层，客户总数相较于2020年翻了一番，其中70%为世界财富五百强。2020年某顶级手机制造公司在大规模环境部署中采用了3,000个节点的Alluxio集群；某互联网科技公司（财富50强）使用Alluxio部署管理的数据量超过了1 ZetaByte。 </p> 
<p>“这些成绩反映出Alluxio在商业上的价值。以开源为基础，开发专业级企业软件，并以收取license 授权年费为主要收入来源是我们的商业模式。”李浩源说，“而核心竞争力和壁垒则来源于活跃开源社区构建的生态。”</p> 
<p>据透露，目前Alluxio开源社区在Github的项目贡献者数量已超过1100个，在社区Slack频道上有超过6000名成员，包括阿里巴巴、 Alluxio、 <a class="project-link" data-id="28215" data-name="百度" data-logo="https://img.36krcdn.com/20210325/v2_fa02010c4a8b46da9f4e1d3b1fd59f22_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/28215" target="_blank">百度</a>、 CMU、Google、 IBM、 Intel、 <a class="project-link" data-id="3968591" data-name="南京大学" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968591" target="_blank">南京大学</a>、 Red Hat、 腾讯、 UC Berkeley和 Yahoo在内的已经300多个组织机构也是社区成员。另外有超过5,000名开发者和数据工程师参加了包括Alluxio Day和Data Orchestration Summit在内的Alluxio的在线会议。</p> 
<p>产品方面，去年10月，Alluxio的2.4版本中已经配置了Alluxio的全新一代数据编排创新技术，提供增强的元数据服务，以及用于混合云和多云部署的全新管理控制台，同时支持集成Vault来安全管理敏感信息，支持更多的云原生部署方式。</p> 
<p>接下来，Alluxio还将继续优化产品，继续增加细分功能支撑更大规模集群规模的部署。在商业化方面，李浩源还透露，将进一步扩大公司的商务销售团队，在中国、欧洲、美国等地区设置商业化服务团队，以进一步推动销售。 </p> 
<p>“在大数据、机器学习持续发展的大趋势下，智能计算的需求也在不断扩大。另外，全球科技竞赛的大背景下，世界主要KA对开源IP拥抱趋势也日益明确，这都是我们需要抓住的机会。”李浩源说。</p> 
<p>据悉，Alluxio由Tachyon开源项目的创建者在加州大学伯克利分校AMPLab创立，以 Apache License 2.0 协议的方式开源，由Andreessen Horowitz，Seven Seas Partners和Volcanics Venture等提供风险投资支持。 </p>  
</div>
            