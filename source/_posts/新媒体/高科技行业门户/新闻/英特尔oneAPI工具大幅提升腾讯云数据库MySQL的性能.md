
---
title: '英特尔oneAPI工具大幅提升腾讯云数据库MySQL的性能'
categories: 
 - 新媒体
 - 高科技行业门户
 - 新闻
headimg: 'https://cors.zfour.workers.dev/?http://images.ofweek.com/Upload/News/2022-09/07/Zyong/1662540949078045517.png'
author: 高科技行业门户
comments: false
date: Wed, 07 Sep 2022 08:54:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://images.ofweek.com/Upload/News/2022-09/07/Zyong/1662540949078045517.png'
---

<div>   
<p style="text-indent: 2em; text-align: left;">腾讯实现了数据库托管服务<span style="text-indent: 32px;">腾讯云数据库MySQL</span>性能的大幅提升，这一服务基于开源关系型数据库管理系统MySQL，在英特尔&reg;至强&reg;处理器上开发而成。此次腾讯云数据库MySQL性能提升是通过使用先进的英特尔&reg;oneAPI DPC＋＋／C＋＋编译器和英特尔&reg;VTune&trade;测评器（英特尔&reg;oneAPI基础工具包的一部分）实现的。</p><p style="text-indent: 2em; text-align: left;">英特尔副总裁兼软件产品和生态事业部总经理Joe Curley表示：“腾讯云数据库MySQL的优化结果说明了使用英特尔oneAPI DPC＋＋／C＋＋编译器等最新开发工具和基于英特尔VTune测评器的最新优化技术的重要价值。性能方面的显著改善可以提高关键业务应用（business－critical applications）产生结果的效率或数量。”</p><p style="text-indent: 2em; text-align: left;">分布式存储在包括互联网、金融和电商在内的各种行业及用例上都发挥着关键作用。腾讯云数据库MySQL等解决方案为开发者提供了分布式数据存储服务，支持用户在云上轻松地创建、操作和扩展关系型数据库。然而，不断增长的存储和数据处理需求及对更高性能的要求给开发人员带来了巨大的挑战。优化MySQL，提升其性能，可以帮助企业更快地处理交易流程和查询数据，从而更好地满足不断发展的业务及客户需求。</p><p style="text-align:center"><img src="https://cors.zfour.workers.dev/?http://images.ofweek.com/Upload/News/2022-09/07/Zyong/1662540949078045517.png" width="50%" title="英特尔oneAPI工具大幅提升腾讯云数据库MySQL的性能" alt="英特尔oneAPI工具大幅提升腾讯云数据库MySQL的性能" referrerpolicy="no-referrer"></p><p style="text-indent: 2em; text-align: left;">通过将硬件和软件工具方面的独特优势，与在功能强大、可加速计算和创新的开源软件上的持续开发投入相结合，英特尔正在引领整个开放生态系统的发展。英特尔oneAPI DPC＋＋／C＋＋编译器适用于并行编程（parallel programming）程序，提供跨CPU和加速器的生产力和性能。利用该编译器，团队以结合链接时优化（LTO）和配置文件引导优化（PGO）的方法，帮助腾讯构建了高性能MySQL。通过链接时优化，编译器对应用程序进行模块间优化（IPO）， 允许对代码实现深入分析和进一步的优化，来达到更好的性能。配置文件引导优化则向编译器提供程序中最常被执行区域的信息。这些技术相结合，共同使腾讯云数据库MySQL的性能得到显著提升，最高可达85％1。</p><p style="text-align:center"><img src="https://cors.zfour.workers.dev/?http://images.ofweek.com/Upload/News/2022-09/07/Zyong/1662540949844005315.png" width="50%" title="英特尔oneAPI工具大幅提升腾讯云数据库MySQL的性能" alt="英特尔oneAPI工具大幅提升腾讯云数据库MySQL的性能" referrerpolicy="no-referrer"></p><p style="text-indent: 2em; text-align: left;">英特尔&reg;VTune&trade;测评器则被于收集采取默认配置的MySQL的性能信息，并识别和分析调用栈（call stacks）中的热点（hot spots），以找到额外的区域，更大程度地提高性能。</p><p style="text-indent: 2em; text-align: left;"><strong>附属细则：</strong></p><p style="text-indent: 2em; text-align: left;"><strong>注意事项和免责声明</strong></p><p style="text-indent: 2em; text-align: left;"><sup>1 </sup>MySQL的性能受很多因素的影响，其中包括它的配置。不同的配置可能对性能有不同的影响。腾讯使用了一个配置文件，用链接时优化和配置文件引导优化搭建了MySQL，并用Sysbench评估了性能。oltp＿read＿write．lua的每秒查询率（QPS）如上图所示。</p><p style="text-indent: 2em; text-align: left;">英特尔不控制或审计第三方数据，在评估数据准确性时，请参考其他信息源。</p><p style="text-indent: 2em; text-align: left;">实际性能受使用情况、配置和其他因素的差异影响。</p><p style="text-indent: 2em; text-align: left;">英特尔技术可能需要支持的硬件、软件或激活服务。</p><p style="text-indent: 2em; text-align: left;">测试日期：性能结果基于腾讯在2021年9月1日和17日进行的测试，且可能并未反映所有公开可用的安全更新。英特尔公司不控制或审核第三方公司的数据。您应该咨询其他来源以评估准确性。</p><p style="text-indent: 2em; text-align: left;">配置细节和工作负载设置：英特尔&reg;至强&reg;Platinum 8255C CPU ＠ 2．50GHz，32G内存。MySQL配置文档：腾讯MySQL默认配置。测试套件：Sysbench－1．1．0－ead2689（配套使用LuaJIT 2．1．0－beta3）。Sysbench测试套件配置：脚本：oltp＿read＿write．lua，表数量：1，表大小：100W，测试线程数：1、2、4、8、16、32、64、128、256，配套使用NUMA Node1。用于比较的编译器：GCC－10．2．0和ICX－Intel（R） oneAPI DPC＋＋ Compiler 2021．2．0 （2021．2．0．20210317）。性能评价指标：每秒事务处理量（TPS）和每秒查询数（QPS）的水平。</p><p style="text-indent: 2em; text-align: left;">基于测试的性能结果基于配置中显示的日期，可能无法反映所有公开的更新信息。详情请参见配置部分。任何产品或组件都不是绝对安全的。</p><p style="text-indent: 2em; text-align: left;">实际性能受使用情况、配置和其他因素的差异影响。您的成本和结果可能会有所不同。</p> 
  
</div>
            