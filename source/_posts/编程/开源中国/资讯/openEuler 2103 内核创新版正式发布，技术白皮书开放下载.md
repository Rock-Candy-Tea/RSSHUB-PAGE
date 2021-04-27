
---
title: 'openEuler 21.03 内核创新版正式发布，技术白皮书开放下载'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-be8f79fcf651685dda29c0806684a4deb79.png'
author: 开源中国
comments: false
date: Tue, 27 Apr 2021 07:22:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-be8f79fcf651685dda29c0806684a4deb79.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>【中国，深圳，2021 年 4 月 25 日】在华为开发者大会 2021（Cloud）上，华为计算研发管理部总裁熊彦宣布<strong> openEuler 21.03 内核创新版正式发布，技术白皮书开放下载</strong>。</p> 
<p>openEuler 21.03 基于 Linux Kernel 5.10 开发，华为在该内核版本贡献全球第一。在此基础上，openEuler 21.03 围绕内核创新增加千核调度、PB 级内存分级扩展、内核热升级、机密计算等创新特性。同时，openEuler 21.03 也是社区开发者共建共创的版本，合入了很多来自社区开发者贡献的特性，<strong>贡献占比 30%</strong>。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-be8f79fcf651685dda29c0806684a4deb79.png" referrerpolicy="no-referrer"></p> 
<h1><strong>围绕内核创新带来 4 大特性</strong></h1> 
<h2><strong>千核调度，充分释放多样性算力</strong></h2> 
<p><img src="https://static.oschina.net/uploads/space/2021/0427/071818_Elri_2720166.png" referrerpolicy="no-referrer"></p> 
<p>优化内核的 8 种资源锁，大幅提升资源访问并行度，同时通过反馈式调度机制，精准感知业务运行状态，通过 NUMA 层次化调度让业务运行在最佳性能区域，综合性能提升 10%以上。</p> 
<h2><strong>PB 级内存扩展，扩容量，提性能</strong></h2> 
<p><img src="https://static.oschina.net/uploads/space/2021/0427/071929_wfhw_2720166.png" referrerpolicy="no-referrer"></p> 
<p>进程级的策略控制，灵活使用多种介质扩展内存容量，结合精准冷热页面识别与淘汰算法，实现业务无感的内存自动调度。我们实际测试 MySQL 应用，在同等成本条件下性能提升 40%。</p> 
<h2><strong>内核热升级，业务不停机</strong></h2> 
<p><img src="https://static.oschina.net/uploads/space/2021/0427/072023_Wcdp_2720166.png" referrerpolicy="no-referrer"></p> 
<p>内核并行快速加载技术，内核的启动时间缩短到毫秒级。通过进程级状态实时保存与恢复技术，进程及外设免重启，从而实现系统不停机的内核升级。</p> 
<h2><strong>机密计算，完整保护敏感数据</strong></h2> 
<h2><img alt src="https://oscimg.oschina.net/oscnet/up-ef60b628f67400241d3529ae0da33973fd6.png" referrerpolicy="no-referrer"></h2> 
<p>secGear 机密计算框架，支持多样性算力，提供统一的 API 和丰富的安全中间件，给开发者带来一致的编程体验。同时华为自研安全微内核 iTrustee。安全微内核经过形式化验证，从数学上证明了微内核的安全性，具备了商用 OS 内核最高安全等级 CC EAL 5+的能力。</p> 
<p><strong>除支持鲲鹏、昇腾、x86 处理器外，openEuler 21.03新增对飞腾、兆芯等处理器的支持，成为了汇聚多样性计算的创新平台。openEuler 21.03 也是社区开发者共建共创的版本，中国联通、华为、麒麟软件、统信软件、北京拓林思、润和软件在该版本中都贡献了重要特性：</strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-d3d09e44ed3eefa53e7f68c2047a7d80758.png" referrerpolicy="no-referrer"></p> 
<ol> 
 <li> <p><strong>中国联通</strong>和<strong>华为</strong>将 OpenStack 移植到 openEuler 的软件仓库，在移植过程中将和 OpenStack 相关的 200 多款依赖包引入社区。<strong>润和软件</strong>和<strong>华为</strong>将 Kubernetes 移植到 openEuler 的软件仓库。openEuler 21.03 初步实现云化基座，这是迈向云原生操作系统的第一步。</p> </li> 
 <li> <p><strong>麒麟软件</strong>将 HA 高可用解决方案贡献到 openEuler 21.03 中，针对不能上云同时又要保障业务平稳运行的用户，提供一个故障秒级切换、保障业务连续性、数据保护和灾难恢复的高可用环境。</p> </li> 
 <li> <p><strong>统信软件</strong>和<strong>北京拓林思</strong>将 DDE 和 Xfce 移植到 openEuler。目前 openEuler 支持三款桌面环境，分别是：UKUI、DDE、Xfce。</p> </li> 
 <li> <p>Compass-CI 多样性算力测试平台提供从内核到上层软件的自动化测试和持续集成，目前完成任务超 100 万，每月给上游社区报告 100 个 bug</p> </li> 
</ol> 
<p>操作系统是释放多样性算力的关键，内核是操作系统的最重要核心技术。openEuler 社区会坚持内核创新和持续贡献上游社区，联合伙伴共建共创繁荣的 openEuler 生态，将 openEuler 打造成多样性算力首选的开源社区。</p> 
<p><strong>欢迎下载 openEuler 21.03 技术白皮书：</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopeneuler.org%2Fwhitepaper%2FopenEuler-whitepaper-2103.pdf" target="_blank">https://openeuler.org/whitepaper/openEuler-whitepaper-2103.pdf</a></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f906b156a460905570269d01613a72293d4.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            