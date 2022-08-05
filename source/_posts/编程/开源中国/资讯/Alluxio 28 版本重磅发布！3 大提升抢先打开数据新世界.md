
---
title: 'Alluxio 2.8 版本重磅发布！3 大提升抢先打开数据新世界'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-138c59f9ccc6cd42e3ee6a3d27c97b62e93.png'
author: 开源中国
comments: false
date: Fri, 05 Aug 2022 11:45:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-138c59f9ccc6cd42e3ee6a3d27c97b62e93.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0px; margin-right:0px"><strong>Alluxio导读</strong></h1> 
<p style="margin-left:0; margin-right:0">全球首创的开源数据编排软件开发商Alluxio宣布正式发布数据编排平台2.8版本，新版本立即可用。</p> 
<p style="margin-left:0; margin-right:0">2.8版本增强了对AWS S3 REST API的接口支持；增加了数据安全功能，对需要满足合规性和监管要求的敏感应用数据实现加密；提升了异构存储系统之间的自动数据迁移功能，用户无需手动迁移或拷贝数据。</p> 
<p><img height="1777" src="https://oscimg.oschina.net/oscnet/up-138c59f9ccc6cd42e3ee6a3d27c97b62e93.png" width="1080" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">Alluxio 2.8新版本提高了S3 API的兼容性，使得在大型数据平台上部署和管理Alluxio更简便。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">此外，新版本还增加了一项重要的企业级安全功能，支持数据在服务器端加密，进一步增强了数据安全和管理。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">对于使用不同服务商、跨云或跨区域存储数据的企业而言，数据迁移往往成为重大挑战。新版本不仅提升了异构存储系统之间数据迁移功能，也增强了基于策略的数据管理的易用性和高可用性。</p> 
<h1 style="margin-left:0px; margin-right:0px"><strong>听听专家们怎么说</strong></h1> 
<p style="margin-left:0; margin-right:0"><strong>梁晨-</strong>Uber交互式分析团队高级软件工程师</p> 
<p style="margin-left:0; margin-right:0">“在Uber，我们通过运行Alluxio来加速大规模分析查询，支撑重要的业务决策，Alluxio帮助我们在大数据处理场景下实现了稳定的性能。在大数据的容器化、存算分离的趋势下，我们相信像Alluxio这样的连接计算和存储的统一层会持续发挥关键作用。”</p> 
<p style="margin-left:0; margin-right:0"><strong>Adit Madan-</strong>Alluxio产品总监</p> 
<p style="margin-left:0; margin-right:0">“Alluxio对于S3 API的支持意义重大，能让更多的客户更容易使用Alluxio。我们拥有S3、HDFS和POSIX API，这些丰富的API能够使企业实现真正意义上的灵活选择存储和实现多云环境部署。Alluxio的数据迁移功能将进一步避免企业被供应商锁定，让企业能够灵活选择其想要的任何计算和存储引擎。”</p> 
<h1 style="margin-left:0px; margin-right:0px; text-align:start"><strong>Alluxio 2.8版本新升级</strong></h1> 
<p><img src="https://pic3.zhimg.com/80/v2-beb38c866ef34eada09ece032cc563e2_720w.jpg" width="5169" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">Alluxio 2.8版本（社区版和企业版）优化了对S3 RESTful API的支持，增加了元数据标签功能。通过S3 API，应用程序可以与Alluxio直接交互，无需通过定制化的驱动，也不需要任何额外的配置。使用S3 API后，数据驱动型应用、终端用户和管理员可以快速地无缝部署Alluxio。元数据标签是新增的功能，使得元数据操作可以通过S3对象和bucket标签的API来实现。</p> 
<p><img src="https://pic3.zhimg.com/80/v2-b1e43927b98f987f84b62efc639aa62a_720w.jpg" width="5169" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">Alluxio 2.8企业版现支持数据加密。在Alluxio中管理数据，可以实现静止数据加密（Encryption at rest），这是企业版安全功能的重大更新。该新功能和SSL共同支持服务器端加密，确保数据安全。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">目前，Alluxio为其管理的数据提供多个加密区，确保满足安全方面的要求。使用此项功能，Alluxio worker上存储的数据始终处于加密状态，并且在发送到客户端之前，在服务器端进行解密。</p> 
<p><img src="https://pic1.zhimg.com/80/v2-d4a5300d44b315ca5049b408e0c44814_720w.jpg" width="5169" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">Alluxio 2.8企业版对于基于策略的数据管理功能进行了提升，这个功能能够实现异构存储系统之间的数据访问和移动，从而提高了性能，节省了成本。Alluxio通过预定义策略管理不同存储系统中的数据存放。企业可以灵活地选择最适合其需求的存储，无需进行复杂的手动数据迁移。</p> 
<h1 style="margin-left:0px; margin-right:0px; text-align:start"><strong>下载</strong></h1> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">Alluxio 2.8 开源社区版和 Alluxio 企业版可在此免费下载：<u><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fxie.infoq.cn%2Flink%253Ftarget%253Dhttps%25253A%25252F%25252Fwww.alluxio.io%25252Fdownload%25252F" target="_blank">https://www.alluxio.io/download/</a></u></p> 
<h1 style="margin-left:0px; margin-right:0px; text-align:start"><strong>资源</strong></h1> 
<ul style="margin-left:0; margin-right:0"> 
 <li>要了解有关 S3 API 的更多信息，请查看 S3 API 访问的技术文档：<u><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fxie.infoq.cn%2Flink%253Ftarget%253Dhttps%25253A%25252F%25252Fdocs.alluxio.io%25252Fos%25252Fuser%25252Fedge%25252Fen%25252Fapi%25252FS3-API.html" target="_blank">https://docs.alluxio.io/os/user/edge/en/api/S3-API.html</a></u></li> 
 <li>有关 Alluxio 的介绍，请访问<u><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fxie.infoq.cn%2Flink%253Ftarget%253Dhttps%25253A%25252F%25252Fwww.alluxio.io%25252F" target="_blank">https://www.alluxio.io</a>.</u></li> 
</ul>
                                        </div>
                                      
</div>
            