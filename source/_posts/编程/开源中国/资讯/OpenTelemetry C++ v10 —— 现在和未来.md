
---
title: 'OpenTelemetry C++ v1.0 —— 现在和未来'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9115'
author: 开源中国
comments: false
date: Tue, 26 Oct 2021 16:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9115'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">上个月，OpenTelemetry C++ 发布了稳定版 v1.0，它实现了 OpenTelemetry 分布式跟踪规范！</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">根据定义的<strong style="color:#0080ff">发布策略</strong>[1]，这个发布是一个单源发布，包括以下内容：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>OpenTelemetry C++<span> </span><strong style="color:#0080ff">API</strong>[2]：Tracing API、Baggage API、Context API 和 Propagators API。</p> </li> 
 <li> <p>提供采样、处理和导出控件的<strong style="color:#0080ff">SDK</strong>[3]，以及 Resource API。</p> </li> 
 <li> <p>Jaeger（Thrift/UDP、Thrift/HTTP）、Zipkin 和 OpenTelemetry 协议（OTLP/HTTP、OTLP/gRPC）的<strong style="color:#0080ff">导出器</strong>[4]。</p> </li> 
 <li> <p>文档，其中包括<strong style="color:#0080ff">示例</strong>[5]、<strong style="color:#0080ff">API</strong>[6]和<strong style="color:#0080ff">SDK 入门指南</strong>[7]以及<strong style="color:#0080ff">API 参考文档</strong>[8]。</p> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">更多细节请参阅<strong style="color:#0080ff">发布说明</strong>[9]。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">这里有一些有趣的特性亮点：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>OpenTelemetry API 的头文件实现——工具库只需要包含这组头文件，就可以用 OpenTelemetry 来测仪它们的代码。</p> </li> 
 <li> <p>API 级别的 ABI 遵从性——这意味着针对标准 C++库的一个版本编译的工具库可以与针对不同版本 C++标准库编译的应用程序或库一起工作。</p> </li> 
 <li> <p>可选支持在应用程序运行时动态加载自定义 SDK 实现。这是很有价值的，因为现在应用程序可以插入不同的 OpenTelemetry SDK 实现，而无需重新构建它们。</p> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">值得一提的是，基于 OpenTelemetry C++的工具库可以作为 Nginx 和 Apache web 服务器的动态加载模块。以及 Fluentd 使用 TCP、UDP 或 unix 域套接字转发跟踪的输入插件。关于这些组件的更多信息可以在<strong style="color:#0080ff">opentelemetry-cpp-contrib</strong>[10]仓库上找到。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">这个开源项目包括来自<strong style="color:#0080ff">10 多个组织</strong>[11]的<strong style="color:#0080ff">57 位个开发人员</strong>[12]的贡献。非常感谢所有贡献者使这一里程碑成为可能。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">我们未来几个月的路线图包括：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>建立 Metrics API/SDK。</p> </li> 
 <li> <p>发布后跟踪 API/SDK 的改进。</p> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">我们正在积极寻找更多的贡献者！任何有兴趣贡献或学习更多关于 OpenTelemetry C++的人都欢迎加入我们在<strong style="color:#0080ff">GitHub</strong>[13]上快速增长的社区，通过<strong style="color:#0080ff">Slack</strong>[14]（如果你是新手，你可以在<strong style="color:#0080ff">这里</strong>[15]创建一个 CNCF Slack 帐户），或参加我们<strong style="color:#0080ff">每周的社区会议</strong>[16]！</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>参考资料</span></h3> 
<p><span><span>[1]</span> 发布策略:<span> </span><em>https://github.com/open-telemetry/opentelemetry-cpp/blob/main/Versioning.md#release-policy</em></span></p> 
<p><span><span>[2]</span> API:<span> </span><em>https://github.com/open-telemetry/opentelemetry-cpp/tree/main/api</em></span></p> 
<p><span><span>[3]</span> SDK:<span> </span><em>https://github.com/open-telemetry/opentelemetry-cpp/tree/main/sdk</em></span></p> 
<p><span><span>[4]</span> 导出器:<span> </span><em>https://github.com/open-telemetry/opentelemetry-cpp/tree/main/exporters</em></span></p> 
<p><span><span>[5]</span> 示例:<span> </span><em>https://github.com/open-telemetry/opentelemetry-cpp/tree/main/examples</em></span></p> 
<p><span><span>[6]</span> API 入门指南:<span> </span><em>https://opentelemetry-cpp.readthedocs.io/en/latest/api/GettingStarted.html</em></span></p> 
<p><span><span>[7]</span> SDK 入门指南:<span> </span><em>https://opentelemetry-cpp.readthedocs.io/en/latest/sdk/GettingStarted.html</em></span></p> 
<p><span><span>[8]</span> API 参考文档:<span> </span><em>https://opentelemetry-cpp.readthedocs.io/en/latest/otel_docs/otel_docs.html</em></span></p> 
<p><span><span>[9]</span> 发布说明:<span> </span><em>https://github.com/open-telemetry/opentelemetry-cpp/releases/tag/v1.0.0</em></span></p> 
<p><span><span>[10]</span> opentelemetry-cpp-contrib:<span> </span><em>https://github.com/open-telemetry/opentelemetry-cpp-contrib</em></span></p> 
<p><span><span>[11]</span> 10 多个组织:<span> </span><em>https://opentelemetry.devstats.cncf.io/d/66/developer-activity-counts-by-companies?orgId=1&var-period_name=Last%20year&var-metric=contributions&var-repogroup_name=open-telemetry%2Fopentelemetry-cpp&var-country_name=All&var-companies=All</em></span></p> 
<p><span><span>[12]</span> 57 位个开发人员:<span> </span><em>https://github.com/open-telemetry/opentelemetry-cpp/graphs/contributors</em></span></p> 
<p><span><span>[13]</span> GitHub:<span> </span><em>https://github.com/open-telemetry/opentelemetry-cpp</em></span></p> 
<p><span><span>[14]</span> Slack:<span> </span><em>https://cloud-native.slack.com/archives/C01N3AT62SJ</em></span></p> 
<p><span><span>[15]</span> 创建CNCF Slack帐户:<span> </span><em>http://slack.cncf.io/</em></span></p> 
<p><span><span>[16]</span> 每周的社区会议:<span> </span><em>https://github.com/open-telemetry/opentelemetry-cpp#contributing</em></span></p> 
<p> </p>
                                        </div>
                                      
</div>
            