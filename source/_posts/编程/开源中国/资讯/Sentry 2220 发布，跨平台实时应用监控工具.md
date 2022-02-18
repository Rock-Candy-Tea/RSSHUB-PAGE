
---
title: 'Sentry 22.2.0 发布，跨平台实时应用监控工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7427'
author: 开源中国
comments: false
date: Fri, 18 Feb 2022 07:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7427'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Sentry 从根本上是一项服务，可跨平台实时监控和修复应用程序崩溃，它重点关注于错误报告。Sentry 服务器使用 Python，但它包含一个完整的 API，用于在任何应用程序中从任何语言发送事件。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Sentry 可以帮助你将 Python 程序的所有 exception 自动记录下来，然后在一个好用的 UI 上呈现和搜索，处理 exception 是每个程序的必要部分，所以 Sentry 也几乎可以说是所有项目的必备组件。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前， Sentry 发布了 22.2.0 版本，此版本带来以下内容：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>ref(ui)<span> </span><span style="color:#24292f">将表单移出视图/设置/组</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31785" target="_blank">#31785</a>) </li> 
 <li>feat(perf):<span> </span><span style="color:#2e3033">当一些重要的网络数据丢失时，显示到文档的链接</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31764" target="_blank">#31764</a>) </li> 
 <li>feat(dashboard):<span> </span><span style="color:#2e3033">在仪表盘编辑模式中添加重复的小部件按钮</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31776" target="_blank">#31776</a>) </li> 
 <li>feat(metrics):<span> </span><span style="color:#2e3033">添加串联变压器指标</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31783" target="_blank">#31783</a>) </li> 
 <li>ref(new-widget-builder-experience):<span> </span><span style="color:#2e3033">添加可视化和查询字段</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31786" target="_blank">#31786</a>) </li> 
 <li>feat(profiling): 添加 flamegraph 提示框 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31663" target="_blank">#31663</a>) </li> 
 <li>ref(endpoints): 添加<span> </span><span style="color:#24292f">SentryApp 端点模块 </span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31749" target="_blank">#31749</a>)</li> 
 <li>feat(ui): 为审查选项卡添加空白状态 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31782" target="_blank">#31782</a>) </li> 
 <li>ref(models):<span> </span><span style="color:#24292f">将更多模块移动到子模块</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31583" target="_blank">#31583</a>) </li> 
 <li>feat(workflow):<span> </span><span style="color:#24292f">添加 警报规则状态页面（alert-rule-status-page） 标志</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31796" target="_blank">#31796</a>) </li> 
 <li>fix(perf): 处理<span> </span><span style="color:#2e3033">perfForSentry 中的事务丢失</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31801" target="_blank">#31801</a>) </li> 
 <li>feat(codeowners):<span> </span><span style="color:#2e3033">将 api 所有者组添加到CODEOWNERS</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31739" target="_blank">#31739</a>) </li> 
 <li>meta(gha):<span> </span><span style="color:#24292f">部署工作流 issue-routing-helper.yml</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31798" target="_blank">#31798</a>) </li> 
 <li>chore(auth):<span> </span><span style="color:#24292f">为所有用户启用自动 IdP 迁移</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31774" target="_blank">#31774</a>) </li> 
 <li>feat(ratelimits): 开启速率<span style="color:#2e3033">限制执行功能<span> </span></span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31789" target="_blank">#31789</a>) </li> 
 <li>ref(perf):<span> </span><span style="color:#24292f">切换 VC 组件以使用 perf.now<span> </span></span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31795" target="_blank">#31795</a>) </li> 
 <li>ref(api): 重构 organization_member_team_details (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31751" target="_blank">#31751</a>)</li> 
 <li>fix(pagerduty): 修复日志参数问题  (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F31794" target="_blank">#31794</a>) </li> 
 <li>...</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Freleases%2Ftag%2F22.2.0" target="_blank">https://github.com/getsentry/sentry/releases/tag/22.2.0</a></p>
                                        </div>
                                      
</div>
            