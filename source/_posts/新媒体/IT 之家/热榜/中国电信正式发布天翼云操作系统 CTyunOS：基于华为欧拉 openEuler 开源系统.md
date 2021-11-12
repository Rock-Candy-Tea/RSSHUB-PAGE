
---
title: '中国电信正式发布天翼云操作系统 CTyunOS：基于华为欧拉 openEuler 开源系统'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/11/63ece3e6-7c1e-4c3d-9e57-835d25d5f6dc.jpg@s_2,w_820,h_545'
author: IT 之家
comments: false
date: Thu, 11 Nov 2021 15:15:18 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/11/63ece3e6-7c1e-4c3d-9e57-835d25d5f6dc.jpg@s_2,w_820,h_545'
---

<div>   
<p data-vmark="019e"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 11 月 11 日消息，据 openEuler 发布，在 openEuler Summit 2021 上，工信部副部长王志军表示，国产操作系统已逐步摆脱缺技术少生态的困境，在重点行业获得规模化应用和市场认可。现场华为宣布将欧拉开源操作系统（openEuler，简称“欧拉”）正式捐赠给开放原子开源基金会。</p><p data-vmark="bce1">峰会上，中国电信副总经理刘桂清正式发布天翼云操作系统 CTyunOS，这也意味着天翼云逐渐起步布局底层核心技术。中国电信根据操作系统领域新趋势，结合自身业务需求，以云网融合战略为牵引，推出基于 openEuler 的操作系统 CTyunOS。中国电信在全行业中首个全业务选择欧拉技术路线，同时，在运营商中首个推出基于欧拉的 x86 和 ARM 自主研发双版本，当前已实现规模商用，为云网边端提供统一的操作系统服务。</p><p data-vmark="ccb7"><img src="https://img.ithome.com/newsuploadfiles/2021/11/63ece3e6-7c1e-4c3d-9e57-835d25d5f6dc.jpg@s_2,w_820,h_545" w="1080" h="718" title="中国电信正式发布天翼云操作系统 CTyunOS：基于华为欧拉 openEuler 开源系统" srcset="https://img.ithome.com/newsuploadfiles/2021/11/63ece3e6-7c1e-4c3d-9e57-835d25d5f6dc.jpg 2x" width="1080" height="545" referrerpolicy="no-referrer"></p><p data-vmark="99f2">中国电信从加入欧拉开源社区开始，一直在参与 OpenStack SIG 的工作，全程参与了 OpenStack Q 版本的软件迁移工作，并对功能、兼容性进行了测试与验证；openEuler 21.03 发布后，中国电信通过与 Kernel SIG 合作，对内存分层扩展（EtMem）的使用场景展开探索；中国电信将其在系统资源压力检测方面的经验贡献到社区，向社区提交贡献了 PSI 工具。</p><p data-vmark="e674">IT之家获悉，中国电信的天翼云操作系统 CTyunOS 提供了以下技术研发优化：通过对系统内核的优化，实现了性能的大幅提升；通过多个独有创新技术对虚拟化组件深度定制，提供高性能、低时延的虚拟化能力；通过自研云平台的计算管理等关键组件，多维度提升云平台的整体性能；通过对不同架构的芯片适配优化，提供同源异构支持能力；同时还大大增强了系统的安全特性，是一款面向云计算领域的专业服务器操作系统。</p><p data-vmark="a47b"><strong>中国电信的天翼云操作系统 CTyunOS 主要特性如下：</strong></p><ul class=" list-paddingleft-2"><li><p data-vmark="f2cf"><strong>优化内核性能：</strong>在内核中创新使用了分域调度技术，在多种场景下提升了进程调度的性能，CPU、内存、IO、网络调度的性能领先业内标杆 CentOS 17%。大数据、web、数据库场景领先 CentOS 15%-22%。基于 SEDI 和 PMU 的 NMI 机制，能够更精准的进行性能分析；通过限制 page cache 占用内存的比例，让业务的运行更顺畅；通过统计分析扩展（Statistical Profiling Extension）来增强 perf 下的调优能力，同时还支持 SAS/NVME 盘热插拔。</p></li><li><p data-vmark="6fd8"><strong>增强虚拟化能力：</strong>针对 KVM 进行了深度定制，通过 CPU 积分机制、CPU 智能调度等技术，提供高性能、低时延的虚拟化能力。支持智能网卡，能够灵活实现网络和存储卸载，降低主机 CPU 和内存消耗，从而大幅提升性能和虚拟机密度。</p></li><li><p data-vmark="39a3"><strong>提升云平台能力：</strong>天翼云打造的计算管理组件，提供支持超大规模集群（10k + 宿主机集群）的低延迟、高性能云平台。定制化的鉴权组件 GoStone 项目，相比 OpenStack Keystone，通过缓存、升级令牌生成方式、优化密码加密方式等方式，大幅提升鉴权认证性能，在相同资源消耗的情况下具备高达百倍的安全性能提升。steel 裸金属管理组件，采用 squashfs 轻量化小尺寸镜像，更易于保存和传输，同时上线周期缩短为分钟级，纯异步系统架构设计，提供可灵活伸缩的集群能力。</p></li><li><p data-vmark="bb38"><strong>适配 ARM 和 X86，支持多样性算力：</strong>适配同源异构多样性算力，支持 X86、ARM 等多种架构，并在鲲鹏、飞腾、兆芯、海光上适配优化。针对多核场景，从调度、锁、减少 CPU 共享资源冲突等方面提升 CPU 多核的并行度，实现任务加速；通过 ktask 将单核串行任务并行到多 CPU 上执行，充分利用多核优势；通过鲲鹏加速引擎 KAE，实现了加密算法硬件加速；通过 ARM64 内核热补丁，利用 ARM64 指令集的特点，提升基础库性能和 CRC 校验时的性能。</p></li><li><p data-vmark="f4b7"><strong>增强系统安全性：</strong>能够提供 IMA 完整性度量框架和 secGear 机密计算框架，可判断运行环境是否安全可信，并屏蔽不同架构下机密计算 SDK 的差异，使调用过程更加高效易用；同时还能提供安全架构工具 security-tool，使安全设置更便捷、更自动化。</p></li><li><p data-vmark="bd56">内存分级扩展：内存分级扩展按照不同策略使用 DRAM 和低速内存介质如 SCM、AEP 等不同内存，通过内存分级调度让热数据在 DRAM 高速内存区中运行，让冷数据交换到低速内存区，达到提升物理内存使用效率的效果。该特性适用于内存容量敏感型应用，典型如 mysql 数据库，spark 等应用。与天翼云在虚拟机场景进行联合创新，拓展介质为 AEP 时，开启 etmem 相比于不开启 etmem 时业务性能提高了约 30%，提升了物理内存性价比。</p></li></ul>
          
</div>
            