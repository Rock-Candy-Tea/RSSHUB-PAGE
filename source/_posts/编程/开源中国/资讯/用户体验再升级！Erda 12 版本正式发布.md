
---
title: '用户体验再升级！Erda 1.2 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202108/30100259_N9mV.png'
author: 开源中国
comments: false
date: Mon, 30 Aug 2021 01:38:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202108/30100259_N9mV.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://static.oschina.net/uploads/img/202108/30100259_N9mV.png" referrerpolicy="no-referrer"></p> 
<p>来源｜<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FEVCdNk34Hx72C6_TpW5kOw" target="_blank">尔达 Erda 公众号</a></p> 
<p><strong>Erda v1.2 Changelog</strong>： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ferda-project%2Ferda%2Fblob%2Fmaster%2FCHANGELOG%2FCHANGELOG-1.x.md" target="_blank">https://github.com/erda-project/erda/blob/master/CHANGELOG/CHANGELOG-1.x.md</a> ​</p> 
<p>近期，Erda 1.2 版本正式发布，新版本主要以改善提升用户体验为主，优化内容共计 50 多项，欢迎广大开发者使用体验 ！同时，也非常感谢为新版本做出贡献的社区小伙伴，未来我们将会继续广泛关注、采纳社区的建议，推动 Erda 项目进一步发展，期待听到大家更多的反馈！ ​</p> 
<p>下文是 v1.2 版本中提升改进项的进一步介绍。 ​</p> 
<h1>Erda v1.2 提升改进项</h1> 
<h2>1. 自动化测试执行逻辑优化</h2> 
<p>目前，在 Erda 平台的接口自动化测试用例编排中，如果在一个接口要等待上一个接口执行结果的时候，只能通过中间加一个定时等待时间来解决，但是这种解决方式存在两个很大的问题： ​</p> 
<ul> 
 <li>等待的时间不可计算</li> 
 <li>固定时间等待导致整体执行时间大幅增长。</li> 
</ul> 
<p>为了能够优雅解决上述问题，Erda 产品在 API 接口用例编排定义的时候，加上了本接口等待循环策略，以便在达到循环退出条件的时候，能够第一时间自动结束本接口调用执行。 ​</p> 
<p>在等待循环策略方面包含： ​</p> 
<ul> 
 <li>循环退出条件设置</li> 
 <li>最大循环次数</li> 
 <li>循环衰退比例</li> 
 <li>衰退最大值</li> 
 <li>间隔时间</li> 
</ul> 
<p>具体的使用方法也非常简单，在自动化测试用例的 API 接口配置页面配置即可。 ​</p> 
<p><img alt src="https://static.oschina.net/uploads/img/202108/30100259_zDQx.png" referrerpolicy="no-referrer"></p> 
<p>图 1：自动化测试用例执行判断逻辑配置</p> 
<h2>2. 自动化测试用例的导入导出</h2> 
<p>在标准产品的研发交付过程中，往往在客户侧构建部署完成后，需要测试同学完整地验证一遍产品功能是否正常，这种模式让交付周期变得更长，同时项目交付的人员成本也随之水涨船高。因此，我们希望自动化测试用例也可以作为产品的交付物之一，在实施产品交付时能够通过自动化测试为产品质量验证降本增效。 ​</p> 
<p>新版本在原有的自动化测试基础之上，实现了自动化测试用例的导入导出，最终让自动化测试用例也成为产品的一种交付产物，在产品交互实施的同时能够通过自动化测试快速完成产品的验证。 ​</p> 
<blockquote> 
 <p>入口：DevOps 平台 -> 我的项目 -> 测试管理 -> 测试用例 -> 自动化测试</p> 
</blockquote> 
<p><img alt src="https://static.oschina.net/uploads/img/202108/30100300_ROav.png" referrerpolicy="no-referrer"></p> 
<p>图 2：自动化测试用例导入导出</p> 
<h2>3. 开放多云管理平台功能</h2> 
<p>Erda 1.2 版本中，针对平台注册用户，在 Erda 1.1 版本开放自助创建组织之上，开放了多云管理平台的功能，用户能够自助创建、导入和管理集群，为完整的 CI/CD 功能打通了最后一公里的障碍（即流水线任务和部署资源管理的问题）。 ​</p> 
<blockquote> 
 <p>入口：多云管理平台</p> 
</blockquote> 
<p><img alt src="https://static.oschina.net/uploads/img/202108/30100300_DVOT.png" referrerpolicy="no-referrer"></p> 
<p>图 3：多云管理平台</p> 
<h1>更多特性</h1> 
<ul> 
 <li>优化了微服务总览和项目列表。</li> 
 <li>支持配置钉钉通知时发送测试信息。</li> 
 <li>优化了 EDAS 集群添加方式。</li> 
 <li>优化了 markdown 编辑器交互和样式。</li> 
 <li>优化了 pipeline 日志样式。</li> 
 <li>优化了 pipeline 通知内容。</li> 
</ul> 
<p><strong>Erda v1.2 Changelog</strong>： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ferda-project%2Ferda%2Fblob%2Fmaster%2FCHANGELOG%2FCHANGELOG-1.x.md" target="_blank"><em>https://github.com/erda-project/erda/blob/master/CHANGELOG/CHANGELOG-1.x.md</em></a> ​</p> 
<h1>总结</h1> 
<p>Erda v1.2 主要解决社区用户在实际生产环境中反馈的问题和需求，如果您有任何疑问或建议，欢迎添加小助手微信**：Erda202106**，加入 Erda 用户群参与交流或在 Github 上与我们讨论！</p> 
<ul> 
 <li>Erda Github 地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ferda-project%2Ferda" target="_blank">https://github.com/erda-project/erda</a></li> 
 <li>Erda Cloud 官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erda.cloud%2F" target="_blank">https://www.erda.cloud/</a></li> 
</ul>
                                        </div>
                                      
</div>
            