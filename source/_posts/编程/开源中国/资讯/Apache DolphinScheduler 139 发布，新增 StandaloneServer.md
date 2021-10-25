
---
title: 'Apache DolphinScheduler 1.3.9 发布，新增 StandaloneServer'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-41bfe0ed5eaeb5a211c64488b607bd0b340.png'
author: 开源中国
comments: false
date: Mon, 25 Oct 2021 02:31:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-41bfe0ed5eaeb5a211c64488b607bd0b340.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img height="640" src="https://oscimg.oschina.net/oscnet/up-41bfe0ed5eaeb5a211c64488b607bd0b340.png" width="1080" referrerpolicy="no-referrer"></p> 
<p><span>2021 年 10 月 22 日，Apache DolphinScheduler 正式发布 1.3.9 版本。<span>时隔一个半月，在社区贡献者的共同努力下，Apache DolphinScheduler 1.3.9 为大家带来了 StandaloneServer，这是本版本的一项重大更新，也意味着其在易用性上又迈出了一步，详情将在下文介绍。另外，本次升级还修复了 1.3.8 的两个重要 bug。</span></span></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0; text-align:left"><strong>1.3.9 下载地址：https://dolphinscheduler.apache.org/zh-cn/download/download.html</strong></p> 
</blockquote> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:justify"><span>在本版中，主要的更新包括：</span></p> 
<h2 style="margin-left:8px; margin-right:8px; text-align:center">新增功能</h2> 
<h3 style="margin-left:0px; margin-right:0px"><strong><span>[Feature#6480]<span> </span></span></strong>增加 Sta<strong><span>ndaloneServer，让开发和运行更简单</span></strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>StandaloneServer 是为了让用户快速体验产品而创建的服务，其中内置了注册中心和数据库 H2-DataBase、Zk-TestServer，用户仅用一行命令，即可一键启动 StandaloneServer 进行调试。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><span>一行命令启动<span> </span><span>StandaloneServer</span><span> </span>的方法：切换到有sudo权限的用户，运行脚本</span></span></p> 
<pre style="margin-left:0; margin-right:0"><code><span>sh ./bin/dolphinscheduler-daemon.sh <span style="color:#ca7d37">start</span> <span style="color:#ca7d37">standalone</span>-<span style="color:#ca7d37">server</span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>可以看到，1.3.9 通过内置组件减少了配置成本，只需要配置 jdk 环境并登录，即可一键启动 DolphinScheduler 系统，从而提高研发效率。</span></p> 
<p style="text-align:center"><img height="777" src="https://oscimg.oschina.net/oscnet/up-f2d1d4b9d2e6cdd06bbdf7755a12a4a762a.png" width="821" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>登录界面地址 IP (self-modified)：http://192.168.</span><span style="color:#ff4c00">xx.xx:</span><span>12345/dolphinscheduler，默认账号密码：admin/dolphinscheduler123。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span>详细的 S<span>tandalone</span><span> </span>使用文档请参考</span></strong><span>：https://dolphinscheduler.apache.org/zh-cn/docs/1.3.9/user_doc/standalone-server.html。</span></p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:center"><span style="color:#000000">优化及修复 <img alt="图片" src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==" referrerpolicy="no-referrer"></span></h2> 
<h3 style="margin-left:0px; margin-right:0px"><strong>☆[Fix #6337][Task] Sql limit param no default value</strong></h3> 
<p><span>当执行 SqlTask 时如果没有设置 limit 参数，则显示结果为空，1.3.9 基于此增加了默认参数，同时在日志上做了相关说明，让用户能够更清楚地追踪问题。</span></p> 
<h3 style="margin-left:0px; margin-right:0px">☆<strong>[Bug#6429] [ui] sub_process node open sub_task show empty page #6429</strong></h3> 
<p><span>修复sub_task节点显示为空的问题。</span></p> 
<h2 style="text-align:center">贡献者</h2> 
<p style="margin-left:8px; margin-right:8px; text-align:justify"><span>感谢来自 SkyWalking 社区的 PMC 柯振旭为 StandaloneServer 所做的贡献，Apache DolphinScheduler 将会在更多贡献者的参与下持续优化功能设计，提升用户体验，敬请关注。</span></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:center">1 <span><strong><span style="color:#000000">DolphinScheduler 介绍</span></strong></span></h3> 
<p><span><span style="color:#171717"><span style="background-color:#ffffff; color:#171717">Apache DolphinScheduler</span><span> </span>新一代大数据任务调度系统</span><span style="color:#171717">致力于“解决大数据任务之间错综复杂的依赖关系，使整个数据处理流程直观可见”。DolphinScheduler以 DAG(有向无环图) 的方式将 Task 组装起来，可实时监控任务的运行状态，同时支持重试、从指定节点恢复失败、暂停及 Kill 任务等操作，并专注于以下 6 大能力：</span></span></p> 
<p style="text-align:center"><img height="647" src="https://oscimg.oschina.net/oscnet/up-6b07844c6c6dafa36cc8719d6a2f50439f1.png" width="1080" referrerpolicy="no-referrer"></p> 
<p><span style="color:#171717">Apache 组织崇尚 “社区大于代码”，DolphinScheduler 目前微信用户群近 5000 人，社区目前有 200 + 贡献者，来自 100+ 家公司、机构和高校(部分统计)。</span></p> 
<p style="text-align:center"><img height="403" src="https://oscimg.oschina.net/oscnet/up-4dfd1d6eb9a1ec67bb90d526c3200eca186.png" width="450" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px; margin-right:0px">2 <span><strong><span style="color:#000000">部分用户案例</span></strong></span></h3> 
<p><span style="color:#171717">据不完全统计，截止 2021 年 9 月，已经有 600 + 家公司及机构采用用 DolphinScheduler 在生产环境使用，部分案例如下(排名不分先后)。</span></p> 
<p style="text-align:center"><img height="687" src="https://oscimg.oschina.net/oscnet/up-1dd167470ab7c1896b7cd80e0c703325266.png" width="887" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><img height="229" src="https://oscimg.oschina.net/oscnet/up-24cae68ce2c5c37b7c266179195107ccc73.png" width="891" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:center">3 <span><strong><span style="color:#000000">参与贡献</span></strong></span></h3> 
<p><span>随着国内开源的迅猛崛起，Apache DolphinScheduler 社区迎来蓬勃发展，为了做更好用、易用的调度，真诚欢迎热爱开源的伙伴加入到开源社区中来，为中国开源崛起献上一份自己的力量，让本土开源走向全球。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">参与 DolphinScheduler 社区有非常多的参与贡献的方式，包括：</span></p> 
<p><img height="39" src="https://oscimg.oschina.net/oscnet/up-269ba76ff20e21e45f3861a6888a3194d8e.png" width="833" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">贡献第一个PR(文档、代码) 我们也希望是简单的，第一个PR用于熟悉提交的流程和社区协作以及感受社区的友好度。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">社区汇总了以下适合新手的问题列表：https://github.com/apache/dolphinscheduler/issues/5689</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">非新手问题列表：https://github.com/apache/dolphinscheduler/issues?q=is%3Aopen+is%3Aissue+label%3A%22volunteer+wanted%22</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">如何参与贡献链接：https://dolphinscheduler.apache.org/zh-cn/docs/development/contribute.html</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">来吧，DolphinScheduler开源社区需要您的参与，为中国开源崛起添砖加瓦吧，哪怕只是小小的一块瓦，汇聚起来的力量也是巨大的。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0052ff">参与开源可以近距离与各路高手切磋，迅速提升自己的技能，如果您想参与贡献，我们有个贡献者种子孵化群，可以添加社区小助手</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0052ff">微信(Leonard-ds) 手把手教会您( 贡献者不分水平高低，有问必答，关键是有一颗愿意贡献的心 )。添加小助手微信时请说明想参与贡献。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">来吧，开源社区非常期待您的参与。</span></p> 
<p><span><strong>社区官网</strong></span></p> 
<p><strong><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdolphinscheduler.apache.org%2F" target="_blank">https://dolphinscheduler.apache.org/</a></span></strong></p> 
<p><strong><span>代码仓地址</span></strong></p> 
<p><strong><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdolphinscheduler" target="_blank">https://github.com/apache/dolphinscheduler</a></span></strong></p> 
<p><span><strong><strong style="color:#353535">您的 Star，是 </strong>Apache DolphinScheduler<span> </span><strong style="color:#353535">为爱发电的动力❤️ </strong>～</strong></span></p>
                                        </div>
                                      
</div>
            