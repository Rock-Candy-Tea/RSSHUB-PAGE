
---
title: '重构、插件化、性能提升 20 倍，DolphinScheduler 2.0 alpha 发布亮点太多！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-008723578373b65f3870d3c384388003604.png'
author: 开源中国
comments: false
date: Fri, 29 Oct 2021 02:45:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-008723578373b65f3870d3c384388003604.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#2c2051; margin-left:0; margin-right:0; text-align:left"><img height="383" src="https://oscimg.oschina.net/oscnet/up-008723578373b65f3870d3c384388003604.png" width="900" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p><span>社区的小伙伴们，好消息！经过 100 多位社区贡献者近 10 个月的共同努力，我们很高兴地宣布 Apache DolphinScheduler 2.0 alpha 发布。这是 DolphinScheduler 自进入 Apache 以来的首个大版本，进行了多项关键更新和优化，是 DolphinScheduler 发展中的里程碑。</span></p> 
 <p><span>DolphinScheduler 2.0 alpha 主要重构了 Master 的实现，大幅优化了元数据结构和处理流程，增加了 SPI 插件化等能力，在性能上提升 20 倍。同时，新版本设计了全新的 UI 界面，带来更好的用户体验。另外，2.0 alpha 还新添加和优化了一些社区呼声极高的功能，如参数传递、版本控制、导入导出等功能。</span></p> 
 <p><span>注意：当前 alpha 版本还未支持自动升级，我们将在下个版本中支持这一功能。</span></p> 
</blockquote> 
<p style="margin-left:0; margin-right:0; text-align:left"><em><strong>2.0 alpha 下载地址：https://dolphinscheduler.apache.org/en-us/download/download.html </strong></em></p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left"><strong style="color:#ffffff"><span style="color:#000000">优化内核，性能提升 20 倍</span></strong></h2> 
<p style="color:#ffffff; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">优化内核，性能提升 20 倍 相较于 DolphinScheduler 1.3.8，同等硬件配置下(3 台 8 核 16 G)，2.0 alpha 吞吐性能提升 20 倍，这主要得益于 Master 的重构，Master 执行流程和优化了工作流处理流程等，包括：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>重构 Master 的执行流程，将之前状态轮询监控改为事件通知机制，大幅减轻了数据库的轮询压力；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>去掉全局锁，增加了 Master 的分片处理机制，将顺序读写命令改为并行处理，增强了 Master 横向扩展能力；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化工作流处理流程，减少了线程池的使用，大幅提升单个 Master 处理的工作流数量；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>增加缓存机制，大幅减少数据库的操作次数；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化数据库连接方式，极大地缩减数据库操作耗时；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>简化处理流程，减少处理过程中不必要的耗时操作。</span></p> </li> 
</ul> 
<h2>优化 UI 组件，全新的 UI 界面</h2> 
<p><img height="667" src="https://oscimg.oschina.net/oscnet/up-e42949961f6216fea5e1499439764f014e5.png" width="917" referrerpolicy="no-referrer"></p> 
<p><img height="643" src="https://oscimg.oschina.net/oscnet/up-42f92f409b9d2f2c412f1714c1b37a6d191.png" width="1080" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span style="color:#888888">UI 界面对比：1.3.9（上） VS. 2.0 alpha（下）</span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span>2.0 UI 重要优化在以下几个方面：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化组件显示：界面更简洁，流程显示更清晰，一目了然；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>突出重点内容：鼠标点击任务框，显示任务详情信息；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>增强可识别性：左侧工具栏标注名称，使工具更易识别，便于操作；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>调整组件顺序：调整组件排列顺序，更符合用户习惯。</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span>除了性能与 UI 上的变化外，DolphinScheduler 也新增和优化了 20 多项功能</span></p> 
<p style="margin-left:0; margin-right:0"><span>及 BUG 修复。</span></p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left"><span style="color:#000000">新功能列表</span></h2> 
<ul> 
 <li><span>任务结果传递功能</span></li> 
 <li><span>新增 Switch 任务和 Pigeon 任务组件</span></li> 
 <li><span>新增环境管理功能</span></li> 
 <li><span>新增批量导入导出和批量移动功能</span></li> 
 <li><span>新增注册中心插件功能</span></li> 
 <li><span>新增任务插件功能</span></li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px">优化项</h2> 
<ul> 
 <li><span>优化告警组功能</span></li> 
 <li><span>优化 RestApi</span></li> 
 <li><span>优化工作流版本管理</span></li> 
 <li><span>优化导入导出</span></li> 
 <li><span>优化 Worker 分组管理功能</span></li> 
 <li><span>优化 install.sh 安装脚本，简化配置过程</span></li> 
</ul> 
<p style="color:#ffffff; margin-left:0; margin-right:0; text-align:left">B</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug 修复</h2> 
<ul> 
 <li><span>[#6550]DAG 任务弹出窗口中的环境列表未更新</span></li> 
 <li><span>[#6342]任务实例页面</span><span>日期不显示</span></li> 
 <li><span>[#6497]Shell 任务不能正确地</span><span>使</span><span>用</span><span>用户定义的环境</span></li> 
 <li><span>[#6478]在补数模式下</span><span>删除</span><span>历史</span><span>数据</span><span>的问题</span></li> 
 <li><span>[#6352]使用复制工作流功能时不能生成新的流程定义</span></li> 
 <li><span>[#5701]删除用户时，关联的访问令</span><span>牌</span><span>用户未删除</span></li> 
 <li><span>[#4809]启用kerberos身份验证时</span><span>无法获取程序状态</span></li> 
 <li><span>[#4450]启用Kerberos身份验证，</span><span>Hive/Spark数据源不支持多租户</span></li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left"><span style="color:#000000">感谢贡献者 </span></h2> 
<p><span><span><span>DolphinScheduler </span>2.0 alpha 的发布凝聚了众多社区贡献者的智慧和力量，是他们的积极参与和极大的热情开启了 DolphinScheduler 2.0 时代！</span></span></p> 
<p><span>非常感谢 100+ 位（GitHub ID）社区小伙伴</span><span>的贡献，期待更多人能够加</span><span>入 DolphinScheduler 社区共</span><span>建，为打造一个更好用的大数据工作流调度平</span><span>台贡献自己的力量！</span></p> 
<p><img height="676" src="https://oscimg.oschina.net/oscnet/up-0dea84bcfd3b54e59dd2992b8bd91d15c15.png" width="719" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#888888">2.0 alpha 贡献者名单</span></p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left"><span style="color:#000000">加入我们 </span></h2> 
<p><span>随着国内开源的迅猛崛起，Apache DolphinScheduler 社区迎来蓬勃发展，为了做更好用、易用的调度，真诚欢迎热爱开源的伙伴加入到开源社区中来，为中国开源崛起献上一份自己的力量，让本土开源走向全球。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">参与 DolphinScheduler 社区有非常多的参与贡献的方式，包括：</span></p> 
<p><img height="34" src="https://oscimg.oschina.net/oscnet/up-35980c0f66d5e381ed961c25661d3b5fe16.png" width="549" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">贡献第一个PR(文档、代码) 我们也希望是简单的，第一个PR用于熟悉提交的流程和社区协作以及感受社区的友好度。</span></p> 
<ul> 
 <li><span style="color:#000000">社区汇总了以下适合新手的问题列表：https://github.com/apache/dolphinscheduler/issues/5689</span></li> 
 <li><span style="color:#000000">进阶问题列表：https://github.com/apache/dolphinscheduler/issues?q=is%3Aopen+is%3Aissue+label%3A%22volunteer+wanted%22</span></li> 
 <li><span style="color:#000000">如何参与贡献链接：https://dolphinscheduler.apache.org/zh-cn/docs/development/contribute.html</span></li> 
</ul> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">来吧，DolphinScheduler开源社区需要您的参与，为中国开源崛起添砖加瓦吧，哪怕只是小小的一块瓦，汇聚起来的力量也是巨大的。</span></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0052ff">参与开源可以近距离与各路高手切磋，迅速提升自己的技能，如果您想参与贡献，我们有个贡献者种子孵化群，可以添加社区小助手</span><span style="color:#0052ff">微信(Leonard-ds) 手把手教会您( 贡献者不分水平高低，有问必答，关键是有一颗愿意贡献的心 )。</span><span style="color:#0052ff">添加小助手微信时请说明想参与贡献。</span></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">来吧，开源社区非常期待您的参与。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:center"> </p> 
<p style="text-align:center"><span><strong>社区官网</strong></span></p> 
<p style="text-align:center"><strong><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdolphinscheduler.apache.org%2F" target="_blank">https://dolphinscheduler.apache.org/</a></span></strong></p> 
<p style="text-align:center"><strong><span>代码仓地址</span></strong></p> 
<p style="text-align:center"><strong><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdolphinscheduler" target="_blank">https://github.com/apache/dolphinscheduler</a></span></strong></p> 
<p style="text-align:center"><span><strong><strong>您的 Star，是 </strong>Apache DolphinScheduler <strong>为爱发电的动力❤️ </strong>～</strong></span></p>
                                        </div>
                                      
</div>
            