
---
title: '基于ESB的企业服务集成平台建设之道'
categories: 
 - 编程
 - 开源中国
 - 数字型账号用户博客
headimg: 'https://oscimg.oschina.net/oscnet/edb0fd56-253a-4a9c-9174-200d94443de1.jpg'
author: 开源中国
comments: false
date: 2022-07-04 10:20:09
thumbnail: 'https://oscimg.oschina.net/oscnet/edb0fd56-253a-4a9c-9174-200d94443de1.jpg'
---

<div>   
<div class="content">
                                                                                                                                                                                        <div class="rich_media_content                                                                     " id="js_content"> 
 <section style="text-align: center;margin-bottom: 0em;margin-left: 16px;margin-right: 16px;" data-mpa-powered-by="yiban.io"> 
  <img class="rich_pages wxw-img js_insertlocalimg" data-cropselx1="0" data-cropselx2="546" data-cropsely1="0" data-cropsely2="382" data-ratio="0.66640625" data-s="300,640" src="https://oscimg.oschina.net/oscnet/edb0fd56-253a-4a9c-9174-200d94443de1.jpg" data-type="jpeg" data-w="1280" style="width: 573px;height: 382px;" referrerpolicy="no-referrer"> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="color: rgb(178, 178, 178);font-size: 14px;"><strong><span style="font-size: 14px;color: rgb(178, 178, 178);letter-spacing: 2px;">转载本文请注明出处：微信公众号EAWorld</span></strong></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="color: rgb(74, 148, 231);"><strong><span style="font-size: 15px;letter-spacing: 2px;"><br></span></strong></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="color: rgb(74, 148, 231);"><strong><span style="font-size: 15px;letter-spacing: 2px;">行者：</span></strong></span> 
  <span style="font-size: 15px;letter-spacing: 2px;">在关乎企业生存的必选项“数字化转型”以及国家信创战略的共同冲击下，企业需要改变现有业务和IT的架构，更快速地应对挑战、响应变化，增强自身的竞争力。其中，作为企业服务集成核心的ESB平台如何进行信创迁移和建设，是企业解决系统间信息贯通的关键问题，实现完整的服务治理，达成能力开放，以及化解风险隐患，横纵向打通系统集成通道，从业务层与通讯层两方面保证信息安全的重要事项。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="padding-right: 16px;padding-left: 16px;font-size: 16px;"> 
  <section style="margin-top: 10px;margin-bottom: 10px;text-align: center;" powered-by="xiumi.us"> 
   <section style="padding-left: 1em;padding-right: 1em;display: inline-block;"> 
    <span style="display: inline-block;padding: 0.3em 0.5em;border-radius: 0.5em;background-color: rgb(249, 110, 87);font-size: 14px;color: rgb(255, 255, 255);" title opera-tn-ra-cell="_$.pages:0.layers:0.comps:0.title1"><p><span style="font-size: 17px;"><strong>目    录</strong></span><span style="font-size: 15px;"></span></p></span> 
   </section> 
   <section style="border-width: 1px;border-style: solid;border-color: rgb(192, 200, 209);margin-top: -1em;padding: 20px 10px 10px;background-color: rgb(239, 239, 239);"> 
    <section style="text-align: justify;" powered-by="xiumi.us"> 
     <section style="white-space: normal;line-height: 1.75em;"> 
      <span style="color: rgb(0, 0, 0);"><em><span style="font-size: 17px;"><strong><span style="letter-spacing: 2px;">01</span></strong></span></em><strong><span style="font-size: 14px;letter-spacing: 2px;"> </span></strong><span style="font-size: 14px;letter-spacing: 2px;">ESB信创项目建设必要性及难点</span><strong><span style="font-size: 14px;letter-spacing: 2px;"></span></strong></span> 
     </section> 
     <section style="white-space: normal;line-height: 1.75em;"> 
      <span style="color: rgb(0, 0, 0);"><em><span style="font-size: 17px;"><strong><span style="letter-spacing: 2px;">02</span></strong></span></em><strong><span style="font-size: 14px;letter-spacing: 2px;"> </span></strong><span style="font-size: 14px;letter-spacing: 2px;">ESB信创项目建设路径</span><strong><span style="font-size: 14px;letter-spacing: 2px;"></span></strong></span> 
     </section> 
     <section style="white-space: normal;line-height: 1.75em;"> 
      <span style="color: rgb(0, 0, 0);"><em><span style="font-size: 17px;"><strong><span style="letter-spacing: 2px;">03</span></strong></span></em></span> 
      <strong><span style="font-size: 14px;letter-spacing: 2px;"> </span></strong> 
      <span style="font-size: 14px;letter-spacing: 2px;">ESB信创项目实践亮点与案例</span> 
      <strong><span style="font-size: 14px;letter-spacing: 2px;"></span></strong> 
     </section> 
    </section> 
   </section> 
  </section> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"></span> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;text-align: center;"> 
  <span style="color: rgb(255, 76, 65);"><strong><span style="color: rgb(255, 76, 65);font-size: 28px;">01</span></strong></span> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;text-align: center;"> 
  <span style="color: rgb(74, 148, 231);"><strong><span style="color: rgb(74, 148, 231);letter-spacing: 2px;font-size: 17px;">ESB信创项目建设必要性及难点</span></strong></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <strong><span style="font-size: 15px;letter-spacing: 2px;">一、服务集成平台解决系统间信息贯通的关键问题</span></strong> 
  <span style="font-size: 15px;letter-spacing: 2px;"></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">中间件在信创体系中，处于关键的“承上启下” 的作用，为应用的开发、运行、管理、监控提供全生命周期的服务管理能力。而企业服务总线（ESB）是数据中间件的重要组成，主要帮助企业建设服务集成平台，解决系统间信息贯通的关键问题，如业务跨部门、跨企业的互联互通，服务注册、运行、监控等生命周期的管理。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <strong><span style="font-size: 15px;letter-spacing: 2px;">二、应用国外ESB中间件的风险隐患</span></strong> 
  <span style="font-size: 15px;letter-spacing: 2px;"></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">目前企业服务总线（ESB）系统，国内通信、能源、政务等各行业主要使用国外大厂相关产品，存在信息安全、技术不可控、定制化困难、全局性风险等诸多风险隐患。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">信息安全：</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">（1）ESB系统承担各业务的数据交换，数据敏感性突出；（2）交换系统采用国外厂商的产品套件及技术架构，存在数据安全隐患。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">技术不可控：</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">ESB系统的IT底层标准、架构、技术、接口、产品生态，均由国外IT商业公司制定，存在诸多的底层技术被限制的风险，技术方面无法自主定义和自主可控。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">定制化困难：</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">原厂服务依赖国外厂商，面对定制化需求如适配生态、新增协议、熔断、限流、预警等功能时，定制困难，成本高昂。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">全局性风险：</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">企业服务总线系统作为各业务数据交换的中枢系统，牵一发而动全身，由企业服务总线系统导致的安全问题，会直接影响到企业整个核心业务的信息安全。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"> </span> 
 </section> 
 <section style="text-align: center;margin-bottom: 0em;text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <img class="rich_pages wxw-img js_insertlocalimg" data-ratio="0.45692567567567566" data-s="300,640" src="https://oscimg.oschina.net/oscnet/b1921758-05ce-4c0f-854d-9e8acbf2c8a8.png" data-type="png" data-w="1184" style referrerpolicy="no-referrer"> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;text-align: center;"> 
  <span style="letter-spacing: 2px;font-size: 14px;color: rgb(178, 178, 178);">企业服务总线系统</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;text-align: center;"> 
  <span style="letter-spacing: 2px;font-size: 14px;color: rgb(178, 178, 178);">是各业务数据交换的中枢系统</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <strong><span style="font-size: 15px;letter-spacing: 2px;">三、ESB信创项目建设的重点与难点</span></strong> 
  <span style="font-size: 15px;letter-spacing: 2px;"></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">ESB信创项目的重中之重，表现在如何从原有架构平滑地全面迁移到信创架构，保证ESB系统及已有接口服务的稳定性和可靠性，并能够满足业务性能以及不断增长的需要。其难点体现在三大方面。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">难点一：应用是否能平滑迁移？</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">该难点需要攻克的问题是，企业服务总线系统迁移到信创环境时，之前已经集成的系统接口服务是否能够不受影响继续平稳运行。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">难点二：能否满足业务高并发性能的需要？</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">该难点需要攻克的问题包含系统稳定和应用性能两方面，即系统迁移到信创环境后，系统稳定性究竟如何，是否能保障系统稳定运行；应用性能能否满足业务的需求，及后续的业务连续增长对性能的要求。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">难点三：能否覆盖原ESB所有能力？</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">该难点体现在产品功能层面，即系统迁移到信创环境后，系统能否覆盖原ESB（国外厂商ESB）所有功能，细粒度、多角度掌握服务运行情况。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;text-align: center;"> 
  <span style="color: rgb(255, 76, 65);font-size: 28px;"><strong><span style="font-size: 28px;color: rgb(255, 76, 65);letter-spacing: 2px;">02</span></strong></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;text-align: center;"> 
  <span style="font-size: 17px;color: rgb(74, 148, 231);"><strong><span style="color: rgb(74, 148, 231);font-size: 17px;letter-spacing: 2px;">ESB信创项目建设路径</span></strong></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">我们自主研发的企业服务总线（服务集成平台）ESB长期以来，主要经历了面向EAI服务集成达成商用、以SOA架构服务治理打造多行业标杆用户、以微服务与混合架构实现国内领先三个发展阶段。产品成熟可靠，支持信创环境、云环境等，能够全面支持微服务架构下与异构系统的无缝对接，在混合架构中作为新老架构间的通讯桥梁支撑其服务整合与业务集成，帮助客户突破ESB信创项目建设的重点与难点，完全替换国外同类产品。在丰富的实践中，我们对ESB信创项目建设进行了深入的思考，并总结了从系统服务摸底、系统迁移分析到系统实施及迁移方案落地的完整建设路径。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">系统服务摸底：</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">技术环境摸底（运行环境、部署模式、数据库、依赖组件、部署架构等），已经完成的服务接入情况、服务类型及使用情况（哪些系统接入总线、其中哪些冗余、哪些不冗余、哪些可以从总线系统去掉）。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">系统迁移分析：</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">技术路线总体可行性分析（包括部署架构、操作系统、数据库等），迁移影响分析（如：接口改造、现有部署架构及部署模式的改变、业务系统配合、数据割接等），需要详细了解所选择的技术路线对客户业务系统会产生哪些影响。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">系统实施及迁移方案：</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">实施阶段有一次性迁移和分步迁移两种方案，建议采用分步迁移方案，从办公系统、一般业务系统、核心业务系统的顺序进行迁移，在分步迁移过程中要考虑服务共生问题，最终制定详细的实施方案、迁移计划及方案。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">建设完成的服务集成平台（ESB）总体架构大致如下图，其基于SEDA架构实现ESB的高性能与高可靠，基于流式处理架构保证海量日志高效落地，支持在各类环境下灵活部署，提供成熟可靠的系统平滑迁移方案，并通过对服务注册、运行、监控等生命周期的系列管理功能，准确掌握运行期状态，及时获悉异常状态，从业务层与通讯层两方面保证信息安全，全面适配信创生态、完全自主可控。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"> </span> 
 </section> 
 <section style="text-align: center;margin-bottom: 0em;text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <img class="rich_pages wxw-img js_insertlocalimg" data-ratio="0.5311986863711001" data-s="300,640" src="https://oscimg.oschina.net/oscnet/2a12aa72-55f5-4b36-bc7b-5a80cc1ba46c.png" data-type="png" data-w="1218" style referrerpolicy="no-referrer"> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;text-align: center;"> 
  <span style="letter-spacing: 2px;color: rgb(178, 178, 178);font-size: 14px;">建设完成的服务集成平台（ESB）总体架构</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <strong><span style="font-size: 15px;letter-spacing: 2px;">一、支持在各类环境下灵活部署</span></strong> 
  <span style="font-size: 15px;letter-spacing: 2px;"></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">企业服务总线（ ESB ）产品具有强大的兼容性特性，支持在各类部署环境下进行安装部署，能够适应各类部署环境：传统物理部署环境、云环境（私有云、公有云）、容器化部署。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <strong><span style="font-size: 15px;letter-spacing: 2px;">二、成熟可靠的系统平滑迁移方案</span></strong> 
  <span style="font-size: 15px;letter-spacing: 2px;"></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">为保障ESB系统国产化替代过程的业务无感知，可以通过并行流量分发的方式实现系统的平滑迁移。即：将接口迁移至国产化ESB服务总线后，通过负载均衡器的流量分配，将部分接口的请求流量接入到ESB，并依次逐步地将全量接口请求切换至ESB。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <strong><span style="font-size: 15px;letter-spacing: 2px;">三、支持零编码实现服务注册、报文转换及消息路</span></strong> 
  <strong><span style="font-size: 15px;letter-spacing: 2px;">由</span></strong> 
  <span style="font-size: 15px;letter-spacing: 2px;"></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">通过配置化方式、零编码实现服务注册、协议转换、报文转换，减少90%以上服务开发工作。支持标准WebService、Http、JMS协议间互相转换。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <strong><span style="font-size: 15px;letter-spacing: 2px;">四、多视角图形化监控，准确掌握运行期状态</span></strong> 
  <span style="font-size: 15px;letter-spacing: 2px;"></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">提供接口服务调用统计、消费方/提供方服务统计、实时交易状态监控、平均响应时间、TOP10分析、引擎资源监控、MQ队列监控等多种图形化监控视图，提升系统运行期状态监控能力，保障系统服务稳定运行。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <strong><span style="font-size: 15px;letter-spacing: 2px;">五、灵活的运行期状态告警推送机制，及时获悉异常状态</span></strong> 
  <span style="font-size: 15px;letter-spacing: 2px;"></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">服务接口交易状态告警，及时通知接口负责人接口异常情况及原因；模型资源状态告警提前发现模型资源消耗情况，预先做好服务降级准备等；系统资源状态告警为业务高峰期系统稳定运行护航，为业务高峰期的系统动态扩容提供信号。为保障在线告警、邮件告警保障告警信息不遗漏，以及移动办公场景下及时获悉告警情况，自定义告警接口可灵活定义出现告警时的处理方式，如资源使用率过高时的扩容等。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><strong>六、基于SEDA架构实现ESB的高性能与高可靠</strong></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">技术架构层面采用SEDA（staged event-driven architecture）阶段事件驱动架构，替换传统的线程并发模型，通过对每段逻辑进行有效的资源和处理能力的调配，提高系统的吞吐能力、稳定性，能够支撑客户实现每天亿级服务调用，达到核心生产系统互联网级服务调用能力。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <strong><span style="font-size: 15px;letter-spacing: 2px;">七、基于流式处理架构保证海量日志高效落地</span></strong> 
  <span style="font-size: 15px;letter-spacing: 2px;"></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">数据架构层面采用高性能的数据框架，实现日志的异步采集、日志持久化、日志分析，替换原有SOA系统的传统数据库存储模式，提升接口服务日志的高效查询、统计、监控、问题定位，以及保证服务的高效稳定运行。在某信创项目中保证海量日志高效落地，峰值达到每天4.9亿条日志记录，约450G 日志分析，超亿次服务访问。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><strong>八、从业务层与通讯层两方面保证信息安全</strong></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">服务控制包含访问流量控制、访问频度控制、访问超时控制、IP黑白名单、调用关系配置等，即能够在业务层使用业务授权能力包的方式，自动开通，在业务安全的前提下让最终用户无感知，也能够在通讯层通过合作伙伴私钥方式进行合作伙伴身份识别，实现数据保密与防篡改，保证通信安全。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <strong><span style="font-size: 15px;letter-spacing: 2px;">九、全面适配信创生态、完全自主可控</span></strong> 
  <span style="font-size: 15px;letter-spacing: 2px;"></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">企业服务总线ESB产品是普元全栈式信创中间件的重要产品之一，产品适配认证覆盖整个信息技术应用创新基础软硬件生态体系，与包含芯片、服务器、操作系统、数据库等主流厂商在内的几十家合作伙伴共建全栈信创生态，保障业务扩展、业务创新、客户维护和安全运营，达成完全自主可控。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;text-align: center;"> 
  <span style="color: rgb(255, 76, 65);font-size: 28px;"><strong><span style="font-size: 28px;color: rgb(255, 76, 65);letter-spacing: 2px;">03</span></strong></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;text-align: center;"> 
  <span style="color: rgb(74, 148, 231);"><strong><span style="color: rgb(74, 148, 231);font-size: 15px;letter-spacing: 2px;">ESB信创项目实践亮点与案例</span></strong></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">结合电信、金融、政务等多行业客户的信创实践来看，普元企业服务总线ESB（服务集成平台）产品被客户认可的亮点主要集中在以下五大方面。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><strong>一、完整的服务治理方案</strong></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">（1）</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">相比于国外产品，普元服务治理方案更加系统化、集成化，从平台工具、管理规范、度量体系、组织等多维度给出切实方案，并落地在工具平台中。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">（2）</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">平台易用、扩展性强，管控操作界面丰富，更加符合国人使用习惯。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <strong><span style="font-size: 15px;letter-spacing: 2px;">二、高性能与高可靠</span></strong> 
  <span style="font-size: 15px;letter-spacing: 2px;"></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">（1）</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">在所有参与的运营商级 性能测试中，特别是在云化、分布式发展迅速且要求严苛的电信、金融领域，普元产品性能优异，在TPS、容错、响应时间、错误率、日志读写等多项指标均优于国外产品或开源方案。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">（2）</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">采用SEDA阶段事件驱动架构及Elasticsearch 等其他业界前沿技术，有效提高系统性能和稳定性。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">（3）</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">普元ESB是国内第一家生产环境支撑每天亿级调用，峰值TPS8000+的服务总线产品。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <strong><span style="font-size: 15px;letter-spacing: 2px;">三、无缝迁移替换</span></strong> 
  <span style="font-size: 15px;letter-spacing: 2px;"></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">（1）</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">与华为合作成功在尼日利亚电信完全替换TibcoESB，现生产系统已经迁移，正式上线运行中。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">（2）</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">参与运营商去Oracle信创化测试，产品功能、性能、可靠性等多项指标完全满足。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">（3）</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">完全对标国外产品，功能、接口、界面、应用场景均可无缝迁移。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">（4）</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">完全适配兼容信创环境，覆盖芯片、操作系统、数据库等全栈生态。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><strong>四、功能全面易用</strong></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">完全对标并覆盖国外产品功能，且功能更加全面易用。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">（1）</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">功能全面，实现数据服务从注册、部署、运行、审计、注销的全生命周期闭环管理。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">（2）</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">简单易用，支持在线化、零编码方式进行服务注册、协议/报文转换、消息路由配置等功能，更加符合国人的操作及使用习惯。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">（3）</span> 
  <span style="font-size: 15px;letter-spacing: 2px;">产品组件化，安装部署简单。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <strong><span style="font-size: 15px;letter-spacing: 2px;">五、行业案例丰富</span></strong> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">ESB产品市场占有率高，在电信、金融、政务、军工、能源、电力等行业都有大型的头部客户案例。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">一个产品两个方案，全面支持服务管控需求</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">ESB产品高效、稳定、业务化，在运营商集成平台、智能网管、CRM服务总线等众多项目中案例验证，能够提供服务治理解决方案、能力开放平台解决方案两个方案，全面支持服务管理需求。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">服务治理解决方案以接口服务全生命周期管理切入，主要面向内部进行服务治理，架构先进、轻松应对高并发，监控指标和统计分析支持个性化定制。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">能力开放平台解决方案通过企业级能力开放产品，面向外部用户提供个性化、场景化的服务。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(74, 148, 231);">基于服务集成平台横纵向全面打通系统集成通道</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;"><br></span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;">在超大型企业的项目服务集成信创实践中，ESB横向实现集团及板块公司内部各业务系统之间的集成，纵向实现集团与板块公司之间服务集成，全面打通系统集成通道，最终以一级集成平台集群支撑党建云、网上大学、电子采购、移动门户、邮件系统等各业务系统，并向外部单位提供合作的能力。</span> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <br> 
 </section> 
 <section style="text-indent: 0em;margin-left: 16px;margin-right: 16px;line-height: 1.75em;"> 
  <span style="font-size: 15px;letter-spacing: 2px;color: rgb(178, 178, 178);">篇幅所限，很多内容无法充分展开，欢迎关注信创ESB平台实施的专家、学者、技术，与我们共同探讨，伴随信创产业发展，在更广泛的应用场景中，一起实现信创ESB平台的完整落地。</span> 
 </section> 
 <p style="margin-bottom: 0em;white-space: normal;text-align: center;"><img class="rich_pages wxw-img" data-galleryid data-ratio="1" data-s="300,640" src="https://oscimg.oschina.net/oscnet/37e16e51-b82f-46f3-9d07-96f4139d05d5.jpg" data-type="jpeg" data-w="430" style="width: 179.177px;" referrerpolicy="no-referrer"></p> 
 <p style="margin-right: 16px;margin-left: 16px;white-space: normal;outline: 0px;color: rgb(34, 34, 34);font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);line-height: 1.75em;text-align: center;"><span style="outline: 0px;font-size: 14px;color: rgb(136, 136, 136);letter-spacing: 2px;">添加小助手微信加入信创讨论群<br style="outline: 0px;"></span></p> 
 <p style="margin-right: 16px;margin-bottom: 0em;margin-left: 16px;white-space: normal;outline: 0px;color: rgb(34, 34, 34);font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);line-height: 1.75em;text-align: center;"><span style="outline: 0px;font-size: 14px;color: rgb(136, 136, 136);letter-spacing: 2px;">和大咖、同道之人们一起探讨~</span></p> 
 <section class="channels_iframe_wrp"> 
  <mpvideosnap class="js_uneditable custom_select_card channels_live_iframe" data-pluginname="videosnap" data-headimgurl="https://wx.qlogo.cn/finderhead/PiajxSqBRaEIibRRggCicyGaciaAOAOW3GjRECLsCialYppw17IZoRF46pA/0" data-username="v2_060000231003b20faec8c7e6811bc3d4ce02ee31b0778b6dd197acf5595fa89c4f46d29c5670@finder" data-nickname="普元信息" data-desc="将在05月25日 12:30 直播" data-intro="股份制商业银行科技管理信创数字化应用的最佳实践" data-noticeid="finderlivenotice-v2_060000231003b20faec8c7e6811bc3d4ce02ee31b0778b6dd197acf5595fa89c4f46d29c5670@finder-1653354237975970-1037743598" data-type="live"></mpvideosnap> 
 </section> 
 <p style="margin-right: 16px;margin-bottom: 0em;margin-left: 16px;white-space: normal;outline: 0px;color: rgb(34, 34, 34);font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);line-height: 1.75em;text-align: center;"><span style="font-size: 14px;color: rgb(178, 178, 178);">中午12:30，和黄豆一起聊聊银行的最佳实践</span></p> 
 <p style="margin-right: 16px;margin-bottom: 0em;margin-left: 16px;white-space: normal;outline: 0px;color: rgb(34, 34, 34);font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);line-height: 1.75em;text-align: center;"><br></p> 
 <p style="white-space: normal;outline: 0px;color: rgb(34, 34, 34);font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);"><img class="rich_pages wxw-img" data-cropselx1="0" data-cropselx2="120" data-cropsely1="0" data-cropsely2="160" data-galleryid data-ratio="1.5" data-s="300,640" src="https://oscimg.oschina.net/oscnet/b178ddc4-88cb-400b-a13b-c890acac51c3.jpg" data-type="jpeg" data-w="382" style="outline: 0px;float: left;width: 120px;border-color: rgb(255, 255, 255);border-style: solid;border-width: 8px;box-sizing: border-box !important;visibility: visible !important;height: 180px;" referrerpolicy="no-referrer"><strong style="outline: 0px;"><span style="outline: 0px;font-size: 14px;letter-spacing: 2px;color: rgb(0, 0, 0);">关于作者：</span></strong><span style="outline: 0px;font-size: 14px;letter-spacing: 2px;color: rgb(0, 0, 0);">行者，普元信创军团高级顾问，负责公司信创中间件及其他数据类相关产品研发和实施工作，在数据成交换、数据治理、数据资产等领域等方向较深的积累。</span></p> 
 <section class="mp_profile_iframe_wrp"> 
  <mpprofile class="js_uneditable custom_select_card mp_profile_iframe" data-pluginname="mpprofile" data-id="MzI5MDEzMzg5Nw==" data-headimg="http://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJUhO6T2E28dBM7fEklBQJDpibExWibpoX6Hwwj7olhcDwFsGx20oibhoAyUqLib78bECEqfzn6EZiaHuHA/0?wx_fmt=png" data-nickname="EAWorld" data-alias="eaworld" data-signature="加速企业数字化转型" data-from="0"></mpprofile> 
 </section> 
 <p style="margin: 0px 16px;padding: 0px;clear: both;min-height: 1em;max-width: 100%;overflow-wrap: break-word !important;box-sizing: border-box !important;font-size: 17px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;orphans: 2;text-indent: 0px;text-transform: none;white-space: normal;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;text-decoration-style: initial;text-decoration-color: initial;outline: 0px;color: rgb(34, 34, 34);font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);line-height: 1.75em;text-align: center;"><strong style="margin: 0px;padding: 0px;max-width: 100%;overflow-wrap: break-word !important;box-sizing: border-box !important;outline: 0px;"><span style="margin: 0px;padding: 0px;max-width: 100%;overflow-wrap: break-word !important;box-sizing: border-box !important;outline: 0px;font-size: 14px;letter-spacing: 2px;">关于EAWorld</span></strong><span style="margin: 0px;padding: 0px;max-width: 100%;overflow-wrap: break-word !important;box-sizing: border-box !important;outline: 0px;font-size: 14px;letter-spacing: 2px;"></span><br style="margin: 0px;padding: 0px;max-width: 100%;overflow-wrap: break-word !important;box-sizing: border-box !important;"></p> 
 <p style="margin: 0px 16px;padding: 0px;min-height: 1em;max-width: 100%;font-size: 17px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;orphans: 2;text-indent: 0px;text-transform: none;white-space: normal;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;text-decoration-style: initial;text-decoration-color: initial;outline: 0px;color: rgb(34, 34, 34);font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);line-height: 1.75em;text-align: center;overflow-wrap: break-word !important;box-sizing: border-box !important;"><span style="margin: 0px;padding: 0px;max-width: 100%;overflow-wrap: break-word !important;box-sizing: border-box !important;outline: 0px;font-size: 14px;letter-spacing: 2px;">使能数字转型，共创数智未来！</span></p> 
</div> 
<p style="color: #858585; font-size: 13px;">本文分享自微信公众号 - EAWorld（eaworld）。<br>如有侵权，请联系 support@oschina.cn 删除。<br>本文参与“<a href="https://www.oschina.net/sharing-plan" target="_blank">OSC源创计划</a>”，欢迎正在阅读的你也加入，一起分享。</p>
                                        </div>
                                      
</div>
            