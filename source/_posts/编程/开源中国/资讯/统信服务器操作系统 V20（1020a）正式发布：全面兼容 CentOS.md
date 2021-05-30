
---
title: '统信服务器操作系统 V20（1020a）正式发布：全面兼容 CentOS'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1e773ec260e7bc31c2bc63e7caf94bc10e9.png'
author: 开源中国
comments: false
date: Sun, 30 May 2021 09:36:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1e773ec260e7bc31c2bc63e7caf94bc10e9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt src="https://oscimg.oschina.net/oscnet/up-1e773ec260e7bc31c2bc63e7caf94bc10e9.png" referrerpolicy="no-referrer"></p> 
<p>统信服务器操作系统V20（1020a）是基于OpenAnolis社区Anolis OS 8商业化发行的Linux操作系统，它针对统信原有主线产品进行了<strong>功能增强，提供自主访问控制和强制访问控制的安全能力，提供对全链路通讯数据的国密算法支持，并经过7×24小时LTP无差别级高负载压力测试</strong>，是一款安全、稳定、可靠、高性能的服务器操作系统产品。</p> 
<p>统信服务器操作系统V20（1020a）同源支持鲲鹏、飞腾、海光、兆芯等自主CPU芯片及国际主流CPU芯片多计算架构，提供ISO、容器、云镜像交付物进行环境部署，支持<strong>高可用集群、负载均衡集群、容器云平台</strong>等应用场景。</p> 
<p>本次发布的正式版本，在硬件适配支撑、基础功能优化、安全、性能、生态等方面投入了大量的研发工作，力臻充分释放硬件资源的一切潜能，打造操作系统创新生态。</p> 
<h1><strong>关键特性</strong></h1> 
<h2>01 <strong>硬件适配支撑</strong></h2> 
<h3><strong>多计算架构支持</strong></h3> 
<p>操作系统内核、工具链、基础库、典型服务等所有组件，基于一套源代码并行触发多处理器架构进行同源编译。</p> 
<p>操作系统内核集成了鲲鹏、飞腾、海光、兆芯等自主CPU厂商原厂补丁，以及统信在硬件生态适配中的积累成果，实现一套内核代码同源<strong>支持鲲鹏、飞腾、海光、兆芯等自主CPU及x86_64平台</strong>，为信创项目提供自主、安全、稳定的操作系统产品。</p> 
<p>针对自主CPU平台和主流服务器整机进行适配和优化，实现跨平台技术路线统一，便于软件跨平台开发和移植，简化软硬件适配流程。</p> 
<p>提供统一的编译工具链和运行、开发环境，在某CPU平台完成一次开发，即可在多种架构CPU平台完成构建；提供统一的文档、手册，降低运维门槛，改善运维管理体验。</p> 
<h3><strong>多内核支持</strong></h3> 
<p>同步上游社区Linux Kernel 4.19 LTS版本的最新成果，帮助用户及时获得开源社区创新红利，同时提供兼容版本内核，定期维护更新，满足多场景需求。</p> 
<h2>02 <strong>基础功能优化</strong></h2> 
<h3><strong>安装优化与备份还原</strong></h3> 
<p>对操作系统安装子系统进行产品化和本地化改进，优化分区方式、分区类型和默认启动参数，增加安装后配置接口及优化系统配置，增加多CPU架构支持，优化GUI环境安装策略，并修复部分上游版本缺陷。</p> 
<p>安装子系统增加备份还原组件，支持系统初始状态及用户自定义的文件系统级备份与还原。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-8b8af30691fef5b87bca9b1f11964a2faaf.png" referrerpolicy="no-referrer"></p> 
<h3><strong>软件多版本仓库支持</strong></h3> 
<p>丰富的系统软件仓库，除提供BaseOS仓库外，还配套提供Powertools、Extra、Update仓库，以及商业项目所需的上游软件包仓库等。此外，还支持私有仓库部署，并提供实施部署指导书。</p> 
<p>在操作系统中新引入应用程序流（Application Streams，简称AppStream）概念，并将其商用化。</p> 
<blockquote> 
 <p>应用程序流是当前较为先进的软件包管理方式，它实现了在不影响系统运行稳定性的前提下，为单个操作系统提供同一个组件的多个版本，使用户的生产环境能得到最大限度底层依赖支持，也能让用户非生产环境的组件测试、运行调优有更多版本选择。</p> 
</blockquote> 
<h3><strong>DDE桌面套件支持</strong></h3> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-c45ff749d9f552013d71f2d4c7e0a0e394f.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-749c86212d954f2a330f66de0ed50969c58.png" referrerpolicy="no-referrer"></p> 
<p>支持统信软件自主研发的桌面运行环境DDE和图形界面应用程序，提高服务器操作系统的易用性。</p> 
<h2><strong>03 安全、性能与生态</strong></h2> 
<h3><strong>安全修复与增强</strong></h3> 
<p>遵照统信软件《漏洞发布流程及方式》技术方案要求，本次发布修复截止2021年5月之前所发现的CVE各级别漏洞80+个，提供补丁、漏洞修复、更新、升级的推送，保障系统安全、可靠运行。<strong>默认提供SM2、SM3和SM4的国密算法套件支持。</strong></p> 
<h3><strong>持续性能优化</strong></h3> 
<p>持续对系统服务、CPU调度等进行调优，并根据项目实际需要提供内核社区最新增强功能和优化支撑，目前已针对Unixbench ，Stream等基准性能指标实现优化。增加io_uring新异步I/O框架支持，拥有完善的Cgroup V2支持，提供多种IO隔离方案。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-36a17b9688f5fcc7b3557378ad33a78c67d.png" referrerpolicy="no-referrer"></p> 
<h3><strong>软件生态完善</strong></h3> 
<p>为完善和丰富统信服务器操作系统基础软件生态，针对WEB服务、数据库、运维监控、中间件、云等场景进行广泛适配，并提供系统增值组件，如<strong>高可用集群套件、容器云管理套件、OpenStack（Ussuri）套件</strong>等的底层技术支撑。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-73ad75897e06e0392f9e9835cad062cc774.png" referrerpolicy="no-referrer"></p> 
<p><em>统信容器云平台</em></p> 
<p><strong>适配主流自研及开源数据库、中间件、虚拟化、容器和大数据软件，以及第三方商业闭源软件和解决方案。</strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f79752a30a0a6c383b062f097ca8fb288f1.png" referrerpolicy="no-referrer"></p> 
<p><em>高可用集群管理</em></p> 
<h2><strong>04 专业服务支持</strong></h2> 
<p>提供并支持Zabbix、Ansible和Grafana等常用运维工具，并拥有丰富的研发经验、专业的支持团队和规范的服务体系，可为企业级用户提供以Linux操作系统为核心的专业技术支持服务，解决用户信息化建设及生产过程中的技术问题。</p> 
<p>统信软件结合自身对Linux操作系统发行版的深度研究和深刻理解，兼顾“兼容CentOS保障用户业务连续性”和“面向国产平台自主创新”两条技术路线，旨在为用户的业务系统提供平滑而无风险的自主基础软件替代。</p> 
<p>统信服务器操作系统V20（1020a）将继续支撑CentOS 8的生态延续和技术演进，充分利用上游社区的创新增强，以及统信软件自身在信创生态的成果，<strong>面向企业级关键业务、云、容器、大数据、人工智能，以及工业互联应用场景，提供可靠、安全、高性能的承载支撑。</strong></p> 
<p>统信服务器操作系统V20（1020a）作为CentOS 8的替代和创新发展的新一代操作系统产品，将为金融、教育、财税、公安、审计、交通、医疗、制造等领域带来企业级支持服务，为客户提供一个商业价值更高更好的选择。</p>
                                        </div>
                                      
</div>
            