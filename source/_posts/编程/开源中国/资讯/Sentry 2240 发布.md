
---
title: 'Sentry 22.4.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7222'
author: 开源中国
comments: false
date: Sun, 17 Apr 2022 07:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7222'
---

<div>   
<div class="content">
                                                                                            <p>Sentry 从根本上是一项服务，可跨平台实时监控和修复应用程序崩溃，它重点关注于错误报告。Sentry 服务器使用 Python，但它包含一个完整的 API，用于在任何应用程序中从任何语言发送事件。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Sentry 可以帮助你将 Python 程序的所有 exception 自动记录下来，然后在一个好用的 UI 上呈现和搜索，处理 exception 是每个程序的必要部分，所以 Sentry 也几乎可以说是所有项目的必备组件。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Sentry 22.4.0 现已发布，具体更新内容如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Various fixes & improvements</strong></p> 
<ul> 
 <li>debug(tests)：为 flakey ado 测试添加了一些调试</li> 
 <li>ref(rate limits)：Tag DD metric w/ rate limit type</li> 
 <li>ref(access log)：添加 Datadog 指标</li> 
 <li>ref(relux)：删除索引签名</li> 
 <li>feat(flamechart)：允许在任意 x 轴上渲染图表</li> 
 <li>fix(ui)：语言上的错别字</li> 
 <li>fix(ui)：不显示警报向导 v3 的项目选择器</li> 
 <li>JSON 语法和 OpenAPI 规范修复，以消除（一些）swagger/openapi 代码生成错误。</li> 
 <li>fix(alertStatus)：处理没有项目时的警报详情页面</li> 
 <li>fix(rate limit)：正确格式化 429 响应</li> 
 <li>fix(workflow)：将查询参数中的 metric date 格式化为数字</li> 
 <li>fix(ui)：将 % 添加到无崩溃会话工具提示</li> 
 <li>feat(replay)：实现全屏查看按钮</li> 
 <li>feat(workflow)：整理项目页面设计</li> 
 <li>fix(sudo modal)：不再尝试在 sudo 上记录超级用户访问权限</li> 
 <li>feat(perf)：将 MEP 添加到 transaction summary</li> 
 <li>feat(dashboards)：更新 Release Health 数据集以使用 sessions v2</li> 
 <li>ref(alerts)：在团队过滤器中使用徽章</li> 
 <li>feat(onboarding)：删除欢迎页面实验并使用新体验</li> 
 <li>feat(workflow)：在删除问题时增加撤销功能</li> 
 <li>ref(page-filters)：All environments -> All env</li> 
 <li>ref(perf)：将长任务移动到应用程序范围</li> 
 <li>fix(new-widget-builder-experience)：不必要的仪表板访问请求</li> 
 <li>ref(page-filters)：将问题排序选项移到表中</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">更新说明：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Freleases%2Ftag%2F22.4.0" target="_blank">https://github.com/getsentry/sentry/releases/tag/22.4.0</a></p>
                                        </div>
                                      
</div>
            