
---
title: 'Fluid 进入 CNCF Sandbox，加速大数据和 AI 应用拥抱云原生'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210511/20d3a80381b520164a4d2802b283efb0.jpg'
author: Dockone
comments: false
date: 2021-05-13 12:04:15
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210511/20d3a80381b520164a4d2802b283efb0.jpg'
---

<div>   
<br>来源 | <a href="https://mp.weixin.qq.com/s/gWiqYAa0Lg3c3tdL_XOxNg">阿里巴巴云原生公众号</a><br>
<br>2021 年 4 月 27 日，云原生计算基金会（CNCF）宣布通过全球 TOC 投票接纳 Fluid 成为 CNCF 官方沙箱项目。Fluid 是一个由南京大学、阿里云以及 Alluxio 开源社区联合发起并开源的云原生数据编排和加速系统。<br>
<br>Fluid 项目地址：<br>
<a href="https://github.com/fluid-cloudnative/fluid">_</a><a href="https://github.com/fluid-cloudnative/fluid_" rel="nofollow" target="_blank">https://github.com/fluid-cloudnative/fluid_</a><br>
<br><h2>项目介绍</h2>云原生环境下，计算存储分离架构在提升系统弹性和灵活性的同时，给大数据 / AI 等数据密集型应用带来了计算性能和管理效率方面的挑战。现有云原生编排框架运行此类应用面临数据访问延时高、多数据源联合分析难、应用使用数据过程复杂等痛点。Fluid 正是为解决这些问题而生的。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210511/20d3a80381b520164a4d2802b283efb0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210511/20d3a80381b520164a4d2802b283efb0.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Fluid 系统架构图<br>
<br>Fluid 运行在 Kubernetes 上，是一个可扩展的分布式数据编排和加速系统，其目标为构建云原生环境下数据密集型应用的高效支撑平台。该项目开源于 2020 年 9 月，短短半年多时间内发展迅速，吸引了众多领域专家和工程师的关注与贡献，并在包括微博、中国电信等多家大型知名IT和互联网企业中使用。<br>
<br><h2>核心功能</h2>Fluid 在云原生应用与数据的协同编排、调度优化、数据缓存等几方面提出一系列技术创新，其核心功能包括：<br>
<ul><li><strong>提供存储无感知的数据对象-数据集(Dataset)</strong>：通过自定义资源对象 (Custom Resource Definition)实现对不同存储系统的统一抽象定义与管理，支持可观测性和弹性伸缩。</li><li><strong>利用分布式缓存技术加速数据集读写</strong>：通过扩展 CacheRuntime 对象，自定义并管理分布式数据缓存引擎。目前已原生支持缓存引擎 <a href="https://www.alluxio.io/">Alluxio</a> 和 <a href="https://github.com/aliyun/alibabacloud-jindofs">JindoFS</a>。</li><li><strong>基于容器调度的智能数据编排</strong>：基于 Kubernetes 容器调度和扩缩容能力，实现数据缓存的智能化编排。</li><li><strong>数据集与应用协同调度</strong>：扩展 Kubernetes 调度器感知数据集缓存信息，就近调度应用，发挥本地读写缓存的性能优势。</li><li><strong>标准访问接口</strong>：使用 Kubernetes 标准存储接口 Persistent Volume Claim  访问数据集，实现无缝兼容云原生应用。</li><li><strong>面向场景的性能调优</strong>：针对深度学习、批量数据处理等任务，提供数据集预热、元数据管理优化、小文件 IO 优化、自动弹性伸缩等手段，普遍提升任务运行效率。</li></ul><br>
<br><h2>展望未来</h2>Fluid 开源项目致力于通过结合学术界的原创研究和工业界的落地实践能力，加速云原生基础设施拥抱数据密集型应用，与开源社区一同构建 Kubernetes 平台应用使用和管理数据的统一界面。Fluid 开源社区目前有 5 位核心维护者 (Maintainer)，分别来自南京大学，阿里巴巴和 Alluxio，并由来自南京大学 PASALab 的顾荣副研究员担任开源社区主席。此外，来自中国电信、微博、Boss 直聘、第四范式、云知声等企业的工程师都贡献了大量的开发工作。<br>
<br>作为对原生 Kubernetes 生态完全兼容的数据密集型应用运行支撑平台，Fluid 将向更灵活、智能、可扩展的架构方向发展，不断提升开发者和用户使用体验。未来，Fluid 将继续与社区并肩、与生态同行，致力于推进云原生技术在大数据 / AI 系统领域的生态建设与普及，与全球开发者一起拓展云原生的边界。<br>
<br>欢迎大家持续关注 Fluid 开源项目并积极参与该项目的共建。
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            