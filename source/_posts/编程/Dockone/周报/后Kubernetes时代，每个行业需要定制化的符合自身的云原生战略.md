
---
title: '后Kubernetes时代，每个行业需要定制化的符合自身的云原生战略'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/a5f041a73161af5e90f1019b796ddbcd.png'
author: Dockone
comments: false
date: 2021-05-25 00:16:19
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/a5f041a73161af5e90f1019b796ddbcd.png'
---

<div>   
<br>本文由谐云CTO苌程撰写，就国内外云原生生态概况做了详细介绍，在国内大厂纷纷构建云原生生态的背景下，谐云认为在各个行业云原生落地需要符合行业属性，具备行业特点。在此基础上，谐云论证了金融、通信、能源行业的云原生体系演进方向，推出了针对金融、通信、能源行业的云原生解决方案，总结了云原生落地实践经验，供大家大家交流分享。<br>
<br><strong>「一、国内外云原生的生态全景图」</strong><br>
<br><strong>1.1CNCF云原生生态全景图</strong><br>
<br>提到云原生，就不得不提到CNCF（Cloud Native Computing Foundation）-云原生行业基金会。CNCF于2015 年7月由Google 牵头成立，隶属于 Linux 基金会，初衷是围绕云原生服务云计算，致力于培育和维护一个厂商中立的开源生态系统，维护和集成开源技术，支持编排容器化微服务架构应用，通过将最前沿的模式民主化，让这些创新为大众所用。<br>
<br>自2016 年 11 月起，CNCF 开始维护 Cloud Native Landscape，汇总流行热门的云原生技术与工具，并加以分类，为企业构建云原生体系提供参考。     <br>
<br>截止2021年2月28日，全景图列举了和云原生相关的产品及服务的完整名单，由1449个项目共同构成了恢弘庞大的云原生世界。整个全景图按照功能分为29个模块，分别归属于9种大的类别（应用定义与开发、编排与管理、运行时、配置、平台、可观察性与分析、Serverless、会员和其它）。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210521/a5f041a73161af5e90f1019b796ddbcd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/a5f041a73161af5e90f1019b796ddbcd.png" class="img-polaroid" title="图片_1.png" alt="图片_1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>CNCF维护的云原生生态全景图<br>
<br><strong>1.2云原生产业联盟-中国云原生生态全景图</strong><br>
<br>2019年4月，由中国信通院发起的云原生产业联盟正式成立，联盟聚焦容器、DevOps、微服务、Serverless等前沿开源技术和理念，推动云原生技术在中国的产业化落地，是汇聚国内外云原生领域创新应用与实践案例的技术生态联盟。<br>
<br>2020年7月，中国信通院发布了国内首个云原生技术生态图景，对国内云原生技术进行详细梳理，从云原生底层技术、云原生应用编排及管理、云原生应用、云原生安全技术、云原生监测分析共五大类、20个细化分类，详细展示国内云原生技术生态的全景视图，为国内云原生技术生态全貌提供了重要参考。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210521/139bff920c4f8e72168b5a38b1bd3fea.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/139bff920c4f8e72168b5a38b1bd3fea.png" class="img-polaroid" title="图片_2.png" alt="图片_2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>中国云原生技术生态图景<br>
<br><strong>1.3国内大厂围绕云原生的产品生态</strong><br>
<br><strong>1.3.1 阿里巴巴成立云原生技术委员会，云原生升级为阿里技术新战略</strong><br>
<br>2020年9月，阿里巴巴成立云原生技术委员会，大力推动阿里经济体全面云原生化，并沉淀阿里巴巴10多年的云原生实践，对外赋能数百万家企业进行云原生改造，提升30%研发效率的同时降低30%IT成本，帮助客户迈入数字原生时代。<br>
<br>云原生技术委员会的成立，标志着阿里将云原生升级为新的战略方向。阿里自2009年首次上线核心中间件系统、2011年淘宝天猫使用容器调度、再到自研云原生硬件神龙服务器、云原生数据库PolarDB，阿里拥有10多年的云原生实践经验，并拥有国内规模最大的云原生产品家族和开源生态。<br>
<br>阿里云原生产品家族及开源生态，提供云原生裸金属服务器、云原生数据库、数据仓库、数据湖、容器、微服务、DevOps、Serverless等超100款产品，覆盖政务、零售、教育、医疗等各个领域。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210521/d87b3021483f0a670674b89e05974564.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/d87b3021483f0a670674b89e05974564.png" class="img-polaroid" title="图片_3.png" alt="图片_3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>阿里云原生全景图<br>
<br><strong>1.3.2 华为发布云原生2.0的战略，打造围绕以应用为中心的云原生基础设施</strong><br>
<br>2020年11月30日，华为基于云原生的数字化转型实践，发布了华为云云原生2.0全景图，提出云原生2.0是企业智能升级新阶段，企业云化从「ON Cloud」走向「IN Cloud」，成为「新云原生企业」。<br>
<br>华为提出云原生2.0时代，是面向所有企业的，任何企业只要有意愿都可以成为新云原生企业。在云原生2.0时代，原有的基础设施将全面升级为云原生基础设施。云原生，就是企业生产力，是中国企业应对市场不确定性的关键。<br>
<br>在华为云原生2.0全景图中，提出以容器为核心的统一计算，以应用为中心、支持多种算力和不同场景的云原生基础设施。并通过擎天架构软硬件协同能力、多云治理及边云协同等高效计算能力，全面打造资源高效、应用敏捷、业务智能和安全可信的云原生2.0计划。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210521/67441d240e4228e354438793666b16c2.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/67441d240e4228e354438793666b16c2.jpeg" class="img-polaroid" title="3_下午5.23_.22_.jpeg" alt="3_下午5.23_.22_.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>华为云原生2.0全景图<br>
<br><strong>1.3.3 谐云云原生全景图理解：云原生全景图的落地需要具备行业属性和行业特点</strong><br>
<br>国内外全景图覆盖全行业所涉及领域太大，所有细节项目都研究透花的精力太多。每个企业最实用的手段是只关注对其行业属性有帮助、能够辅助其更好的落地行业应用的云原生项目，并将这些内容有机组合形成满足自身需求的云原生战略。<br>
<br>浙大SEL实验室自2011年开始在PaaS技术层面的展开研究，并于2015年作为高校代表以创始会员的身份和google一起创建了CNCF组织。起源于浙大SEL实验室的谐云从成立起，就致力于助力企业落地云原生技术，在金融、通信、能源等行业有着近百个项目的实践经验，并帮助客户打造了全球最大的客服云平台、数千台主机的金融业案例等行业标杆案例，为云原生在金融、通信、能源行业的落地提供了参考。<br>
<br>根据10多年的云原生项目技术落地经验，谐云将金融、通信、能源行业的云原生技术落地分成了几个阶段：建好容器云、管好容器云、用好容器云这三个阶段，每个阶段谐云都提供符合这几个行业的产品和服务。谐云希望能够帮助这些行业更好的落地云原生，用好云原生，管好云原生。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210521/1fa400e08fd51f9c352d27526270b2dc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/1fa400e08fd51f9c352d27526270b2dc.png" class="img-polaroid" title="图片_5.png" alt="图片_5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>谐云产品图谱<br>
<br><strong>「二、未来，金融、通信、能源行业云原生战略重点将从传统容器云、微服务、devops三驾马车向融合云原原生可观测性及云原生生安全的云原生体系演进」</strong><br>
<br>自2016年起，谐云开始大规模推广云原生技术在金融、通信、能源行业的落地，这三个行业都属于国家的支柱产业，和民生戚戚相关，对云原生落地所承载的业务的可用性要求很高。另外这几个行业的IT机房规模也是全国排在前几名的行业，都需符合国家产业层面的“瘦身健体”要求，在宏观经济不确定的情况下，IT投资需要降本增效。据谐云的观察，未来，云原生在这三个行业的应用趋势，将重点在原有容器平台中增强云原生可观测性及云原生安全版块。<br>
<br>这一趋势也与信通院报告一致，信通院云大所何宝宏在云原生趋势中指明“云原生其内涵已从容器、微服务和DevOps的老三样，扩展纳入了与底层融合、安全、监测和编排管理等。”这也从侧面证明了谐云的判断，未来，云原生行业符合金融、通信、能源等行业的云原生战略除了微服务、devops、容器以外，为了能够管好容器云、用好容器云，云原生版图里面还应该包含云原生可观测性和云原生安全。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210521/992e5ad5ce9cd1e4df72c8e9f4fe0d15.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/992e5ad5ce9cd1e4df72c8e9f4fe0d15.png" class="img-polaroid" title="云原生发展图.png" alt="云原生发展图.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>金融、通信、能源行业云原生发展图<br>
<br><strong>「三、谐云推荐的金融、通信、能源云原生解决方案」</strong><br>
<br>根据多年的实践经验，谐云联合合作伙伴一起推出了面向金融、通信、能源等行业的云原生解决方案，在业务可用级别高、应用安全性能及应用可监控可观测性三方面进行了实践。<br>
<br><strong>3.1云原生可观测性对金融、通信、能源行业落地云原生十分重要</strong><br>
<br>国内目前支持云原生可观测性的方案除了promethus和APM方案以外，没有很好的方案。Pomethus在资源层面的监控已经成为事实上的标准，但是仅仅有他还不足以帮助这些行业的企业进行很好地业务运维。而APM方案虽然不用重新开发业务，但是APM对技术开发语言的限制和对业务代码动态修改侵入，在相对保守行业使用度并不高。<br>
<br>根据谐云服务金融、通信、能源行业客户的经验，可观测性方案要实现以下指标，才能更好的服务业务运维。<br>
<br>a. 云原生上的业务是否正常，需要从访问量、错误率、延时等反应业务健康度的判断指标<br>
<br>b. 云原生上的业务一旦出现不正常，需要秒级定位至具体的service或者pod的定位指标<br>
<br>c. 在定位到service或者pod之后，需要进一步排查问题原因：是业务开发供应商的代码导致的，还是容器网络、容器组件所导致的排查指标。<br>
<br>只有完成了以上三个层次的可观测指标采集，才能实现对云原生的业务了然于胸。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210521/b7ad5deb396501fbf3b3e01b0efa31b4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/b7ad5deb396501fbf3b3e01b0efa31b4.png" class="img-polaroid" title="图片_7.png" alt="图片_7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>可观测性指标图解<br>
<br><strong>3.2随着业务对云原生平台依赖度的增加，云原生安全的重要性也提上日程</strong><br>
<br>云原生安全和传统技术安全最主要的区别在于云原生在开源层面引入了非常多的组件，这对云原生的业务带来新的安全挑战。<br>
<br>在容器镜像的构建阶段，需要对代码进行审计，使用可信无漏洞的基础镜像，并对构建的镜像进行漏洞扫描。<br>
<br>在容器镜像分发阶段，需要对镜像进行签名确保无篡改，同时对镜像仓库进行访问控制。<br>
<br>在容器运行时，需要对容器运行时漏洞进行扫描、入侵检测、异常检测。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210521/900f5f747a479bb765178804919722eb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/900f5f747a479bb765178804919722eb.png" class="img-polaroid" title="图片_8.png" alt="图片_8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>容器安全问题总结<br>
<br><strong>3.3面对不断推陈出新的云原生领域，谐云始终伫立桥头引领技术方向</strong><br>
<br>云原生是一个新技术层出不穷的领域。基于此，谐云联合浙大，产学研一体化，不断引入云原生最新的技术，如使用ebpf构建可观测性方案等，引领国内云原生的技术发展方向。在多年的云原生实践中完成了金融、通信、能源行业的云原生可观测性及云安全的技术架构，实现了对云上业务监控和故障，实现了故障的秒级发现和分钟级修复，并通过容器运行时保障业务安全达到了行业领先水平。<br>
<br>未来，谐云将重点围绕着金融、通信、能源行业，在建好容器云、管好容器云、用好容器云的相关环节联合合作伙伴精深产品战略，一起夯实企业落地云原生的基础，提高企业综合竞争力。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                    <a href="http://dockone.io/uploads/article/20210521/e4ef17c504d9ff0536d07d25e63acd89.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/e4ef17c504d9ff0536d07d25e63acd89.png" class="img-polaroid" alt="图片_4.png" referrerpolicy="no-referrer"></a>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            