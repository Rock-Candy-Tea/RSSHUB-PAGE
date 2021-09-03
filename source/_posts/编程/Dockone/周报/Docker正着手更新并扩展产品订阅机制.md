
---
title: 'Docker正着手更新并扩展产品订阅机制'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/548923b175e6ff9facc31d1168db2683.png'
author: Dockone
comments: false
date: 2021-09-03 06:09:20
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/548923b175e6ff9facc31d1168db2683.png'
---

<div>   
<br>数百万开发人员正使用Docker构建、共享并运行各类应用程序，调查显示55%的专业开发人员每天都在使用Docker。在这类工作环境中，针对软件供应链的外部攻击可谓持续肆虐，也使得开发人员对Docker可信内容的需求不断提升——包括迫切希望获取Docker官方镜像与Docker验证的发布者镜像。此外，全球开发者数量也在快速增长，预计到2030年将达到4500万。这一切都在推动我们建立起一套可持续扩展，借以持续提供开发者们喜爱、包含创新成果且免费可得的Docker体验。<br>
<br>为了满足这些要求，今天我们宣布更新并扩展Docker的产品订阅机制，具体包括Personal、Pro、Team以及Business四个版本。更新后的产品订阅选项将为开发人员所需要的生产力与协作效果提供相应的规模、安全性与可信内容，并以可持续方式不断为Docker注入新的活力。<br>
<h3>需要了解的一切</h3><ul><li>我们推出新的产品订阅选项Docker Business，适用于大规模使用Docker进行应用程序开发，且需要安全软件供应链管理、单点登录（SSO）以及容器注册表访问控制等功能的组织。</li><li><br>我们的Docker订阅服务协议包含以下Docker Desktop条款变更：<br>
<ul><li>Docker Desktop仍向小型企业（员工人数低于250名，年收入低于1000万美元）、个人使用、教育以及非商业开源项目免费开放。</li><li>对于大型企业中的商业应用，Pro、Team与Business版要求付费订阅，每位用户每月5美元起。</li><li>这些条款的生效起始日期为2021年8月31日，但Docker Desktop的实际付费订阅时间将宽延至2022年1月31日。</li></ul></li><li><br>Docker Pro、Team与Business订阅将直接包含Docker Desktop的商用权限。</li><li>现有Docker Free订阅已更名为Docker Personal。</li><li>Docker引擎以及各类上游开源Docker或Moby项目不受影响。</li><li>查看<a href="https://www.docker.com/pricing/faq">常见问题解答</a>以了解更多细节信息。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/548923b175e6ff9facc31d1168db2683.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/548923b175e6ff9facc31d1168db2683.png" class="img-polaroid" title="Docker-Pricing-1.png" alt="Docker-Pricing-1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Docker Personal = Free</h3>新的Docker Personal订阅取代了原本的Docker Free。Docker Personal主要面向开源社区、个人开发者、教育以及小型企业——总计占Docker用户的半数以上。Docker Personal对这些社群免费开放，并继续允许大家免费使用其中的所有组件——包括Docker CLI，Docker Compose，Docker Build/BuildKit，Docker Engine，Docker Desktop，Docker Hub以及Docker官方镜像等等。<br>
<h3>Docker Business = 大规模管理与安全</h3>新的Docker Business订阅能够为需要大规模软件开发的企业提供覆盖全组织的管理与安全性支持。借助易于使用的、基于SaaS的管理平面，IT领导者现在可以更有效地观察并管理所有Docker开发环境，并加速其安全软件供应链计划。除了Docker Pro与Docker Team订阅中提供的各项功能之外，Docker Business还新增了用于控制开发者可从Docker Hub中访问到哪些具体容器镜像的功能，确保团队从起步阶段就只使用受信内容进行安全构建。很快，Docker Business还将提供SAML SSO，用于实现控制开发人员所能访问的注册表以及远程管理Docker Desktop实例的能力。<br>
<br>从更普遍的意义上讲，新的Docker Business订阅希望帮助大型企业解决组织开发工作中的以下几项挑战：<br>
<ul><li>获取对内容的可见性与控制能力，开发人员们从哪些容器注册表中提取容器镜像？他们在自己的笔记本电脑当中本地运行着哪些镜像？他们运行的是什么版本？这些容器镜像中存在哪些安全漏洞？该如何帮助开发人员保护组织安全？</li><li>管理本地资源与对外部服务的访问，如何确保开发人员拥有安全的本地Docker环境？如何确保Docker与其他本地工具高效共享资源？如何管理Docker的可访问网络？</li><li>大规模管理Docker开发环境，不少大型组织内有成百上千名开发人员在使用Docker，因此需要一个集中的控制点，以便开发者通过SSO、身份验证与授权、行为与内容可观察性以及上述控制的相应配置快速完成入职/离职转换。</li></ul><br>
<br>Docker Business订阅现在以年为订阅单位，每位用户每月须支付21美元。关于更多发展规划，请参阅我们的<a href="https://github.com/docker/roadmap">公开发展路线图</a>。<br>
<h3>Docker Desktop = 新的订阅条款</h3>在Docker，我们致力于继续为个人开发者、开源项目、教育以及小型企业提供易于使用的免费体验。事实上，这部分社群也在Docker全体用户中占比超过一半。Docker Personal及其所有组件——包括Docker CLI，Docker Compose，Kubernetes，Docker Desktop，Docker Build/BuildKit，Docker Hub以及Docker官方镜像等——对这些社群继续免费开放。<br>
<br>具体来讲，小型企业（员工少于250人，年收入少于1000万美元）应该可以继续免费使用Docker Desktop与Docker Personal。但规模更大的企业则需要使用Docker Desktop的Pro、Team或者Business付费订阅，每位用户每月5美元起。<br>
<br>在由Docker Desktop负责管理Windows与Mac桌面环境中的Docker引擎与Kubernetes复杂性集成、配置及维护（具体涵盖文件系统、虚拟机、网络等多个方面）之后，开发人员能够将更多时间投入到应用程序构建之上，而不再需要为基础设施而劳心伤神。通过付费订阅，企业还能获得Docker Desktop的额外价值，包括管理安全软件供应链、集中策略可见性，以及对用户及访问的控制与管理。<br>
<br>Docker Desktop的更新条款，反映出我们需要以可持续方式扩展自身业务，并继续在所有Docker订阅选项中不断交付新的价值。这些新条款从2021年8月31日起生效，但Docker Desktop付费订阅的实际生效期将宽延至2022年1月31日。（请注意，Docker引擎以及上游Docker与Moby开源项目许可不受影响。）<br>
<h3>展望未来</h3>我们都知道，此次订阅机制变更对某些组织来说可能会产生重大影响，我们也将致力于帮助大家顺利完成过渡。个人及小型团队可以<a href="http://docker.com/pricing">点击此处</a>直接购买；如果您隶属于使用Docker产品的大型组织，请向主管人员分享本文以及<a href="https://www.docker.com/products/business/docker-solution-brief/">解决方案简介</a>。<br>
<br>接下来的几个月中，我们将通过网络研讨会、社区聚会、博文等方式进一步介绍此份公告。首先，我们将在9月16日举行社区全体会议，并在9月23日召开首次Docker业务介绍网络研讨会，期待届时与大家相聚！关于产品订阅的更多更新细节，请访问docker.com/pricing及我们的<a href="https://www.docker.com/pricing/faq">常见问题解答</a>。<br>
<br>过去12个月以来，我们见证了一系列重磅成果的发布，从Docker CLI中的镜像扫描、到苹果芯片上的Docker Desktop，从Docker Hub中的审计日志、到Docker Desktop中的GPU支持，再加上BuildKit Dockerfile挂载、新的Docker验证发布者镜像等等。在接下来的12个月中，我们还有更多重要任务，也诚邀各位Docker社区成员参与贡献、投票并发表您的观点。期待我们携手走过的下一段旅途，也期待看到更多开发者朋友能够随时随地运用Docker构建、共享并运行自己的应用程序。<br>
<br><strong>原文链接：<a href="https://www.docker.com/blog/updating-product-subscriptions/">Docker is Updating and Extending Our Product Subscriptions</a></strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            