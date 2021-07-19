
---
title: 'ARMS企业级场景被集成场景介绍'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b60d1c29874441659b02411995deb57a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 22:51:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b60d1c29874441659b02411995deb57a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>简介：</strong> ARMS企业级场景被集成场景介绍</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b60d1c29874441659b02411995deb57a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过本次最佳实践内容，您可以看到ARMS OpenAPI可以灵活的被集成到客户链路监控场景，并对其进行可视化图形展示监控信息。</p>
<h1 data-id="heading-0">1. 背景信息</h1>
<p>应用实时监控服务ARMS（Application Real-Time Monitoring Service）是一款应用性能管理产品，能帮助你实现全栈式的性能监控和端到端的全链路追踪诊断，让应用运维更加高效。</p>
<p>本次最佳实践是基于调用ARMS OpenAPI的形式来实现客户应用场景链路监控的可视化图形展示，使用环境为专有云V3.10版本ASCM控制台，调用ARMS OpenAPI接口通过工具Postman进行测试，在第二章节详细介绍了测试环境及测试工具。第三章节通过一个查询所有应用ARMS OpenAPI接口描述调用过程，并且包含该接口需要请求传入的参数接口列表。最后一章节将对一个复杂应用场景，获取链路监控信息使用到ARMSOpenAPI接口，对每个接口列表字段、调用过程及返回结果详细介绍。</p>
<h1 data-id="heading-1">最佳实践价值</h1>
<p>通过调用ARMS OpenAPI在应用场景的使用，直观给阅读者了解到ARMS产品的能力，及ARMS提供一套OpenAPI可以容易的集成到客户应用中，快速实现复杂的微服务链路监控能力，由ARMS监控服务能力涵盖范围能力比较广，包含浏览器、小程序、APP、分布式应用和容器环境，因此完整的监控能力，开发过程中不需要集成多开源组件的形式，使微服务程序监控功能开发简单，让应用运维变得容易。</p>
<h1 data-id="heading-2">2. 环境</h1>
<p>在使用ARMS前您需要按照以下内容对当前的系统环境进行检查。</p>
<p>本次最佳实践基于专有云企业版V3.10.0版本ARMS。</p>
<p><strong>说明</strong>：ARMS OpenAPI各个版本变化不大，使用方式保持一致，所以此文档也适用于公共云产品或专有云V3.7.0以上版本。专有云V3.10.0控制台称为ASCM，V3.10.0之前版本为Apsara Stack。</p>
<p>1.登录ASCM控制台。</p>
<p>2.将鼠标指向页面上方导航栏中的<strong>产品</strong>，单击<strong>企业级分布式应用服务EDAS</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/980d525331d943749c8564e2e6624688~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图1：ASCM</p>
<p><strong>说明</strong>：由于ARMS监控应用数据，需要EDAS产品配合。本次测试先通过EDAS部署一个标准的Spring Boot应用，开通ARMS监控并得到监控数据。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93683633dcc54e598268e49bbde5779d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 2：EDAS控制台</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cdf1f964bb24f0681ac82987868fb66~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 3：ARMS控制台</p>
<p>3.测试工具检查。</p>
<p>本实践将会在专有云环境中创建win64虚拟机，然后在虚拟机中安装Postman进行测试。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bc5d13f7b054c5e87ee1aa06fd84718~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图4：Postman测试</p>
<h1 data-id="heading-3">3. Open API使用</h1>
<p><strong>调用URL确认</strong></p>
<p>OpenAPI接口均为REST服务，首先确认服务的URL。<br>
每个专有云环境域名不同，会导致URL不同。请根据具体环境信息修改URL信息，前缀及端口不变。<br>
<a href="https://link.juejin.cn/?target=http%3A%2F%2Farms.console.example.com%3A8099%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://arms.console.example.com:8099/" ref="nofollow noopener noreferrer">arms.console.example.com:8099/</a></p>
<p>名称</p>
<p>接口</p>
<p>数据集API</p>
<p>/dataset/GeneralQuery.json</p>
<p>关键应用性能指标</p>
<p>/metric/Metric.json</p>
<p>报警信息</p>
<p>无</p>
<p>应用监控-应用拓扑</p>
<p>/trace/Dependecies.json</p>
<p>事件集</p>
<p>/eventset/EventList.json</p>
<p>调用示例-查看所有应用：</p>
<p><strong>API说明</strong></p>
<p>URL：<a href="https://link.juejin.cn/?target=http%3A%2F%2Farms.console.example.com%3A8099%2Ftrace%2FServices.json" target="_blank" rel="nofollow noopener noreferrer" title="http://arms.console.example.com:8099/trace/Services.json" ref="nofollow noopener noreferrer">arms.console.example.com:8099/trace/Servi…</a></p>
<p>参数列表</p>
<p>字段名称</p>
<p>字段类型</p>
<p>字段含义</p>
<p>是否必选</p>
<p>备注</p>
<p>_userId</p>
<p>String</p>
<p>用户id</p>
<p>是</p>
<p>用户名称(如arms_admin)</p>
<p><strong>返回格式示例</strong></p>
<pre><code class="copyable">&#123;
    "code": 200,
    "data": &#123;
        "details": [
            &#123;               
                "pid": "string", //应用对应的pid
                "regionId": "string",                
                "serviceName": "string" //应用名称
            &#125;
        ],
        "services":[ //应用名称列表
           "string",
           "string"
        ]
    &#125;,
    "success": true
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Postman调用结果</p>
<p>参数设置：_userId= 121827433423****</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61b410f5fb194445871688ccad491bb5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图5：Postman调用结果</p>
<h1 data-id="heading-4">4. 应用描述</h1>
<p>从ARMS中取得应用拓扑数据、曲线图、应用监控指标数据，将通过大屏DataV展示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8040d6e9e7cd4cd8b91f0f80cc49cf11~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图6：DataV展示</p>
<h1 data-id="heading-5">5. 查询接口调用次数</h1>
<p>通过/metric/Metric.json接口获得应用相关性能数据，查询接口调用次数。</p>
<p><strong>API说明</strong></p>
<ul>
<li>URL ：<a href="https://link.juejin.cn/?target=http%3A%2F%2Farms.console.example.com%3A8099%2Fmetric%2FMetric.json" target="_blank" rel="nofollow noopener noreferrer" title="http://arms.console.example.com:8099/metric/Metric.json" ref="nofollow noopener noreferrer">arms.console.example.com:8099/metric/Metr…</a></li>
<li>接口说明：</li>
</ul>
<p>字段名称</p>
<p>字段类型</p>
<p>字段含义</p>
<p>是否必选</p>
<p>备注</p>
<p>startTime</p>
<p>Long</p>
<p>查询数据的起始时间</p>
<p>是</p>
<p>无</p>
<p>endTime</p>
<p>Long</p>
<p>查询数据的截止时间</p>
<p>是</p>
<p>无</p>
<p>intervalInSec</p>
<p>Integer</p>
<p>时间间隔</p>
<p>否</p>
<p>建议填写</p>
<p>metric</p>
<p>String</p>
<p>metric字段</p>
<p>是</p>
<p>详细填写参考参数填写示范</p>
<p>filters</p>
<p>List[String]</p>
<p>过滤字段</p>
<p>是</p>
<p>详细填写参考参数填写示范</p>
<p>measures</p>
<p>List[String]</p>
<p>指标</p>
<p>是</p>
<p>详细填写参考参数填写示范</p>
<p>dimensions</p>
<p>List[String]</p>
<p>维度</p>
<p>是</p>
<p>详细填写参考参数填写示范</p>
<p>orderBy</p>
<p>String</p>
<p>排序字段</p>
<p>否</p>
<p>无</p>
<p>sortOrder</p>
<p>String</p>
<p>排序</p>
<p>否</p>
<p>默认不排序(ASC或者DESC)</p>
<p>limit</p>
<p>Integer</p>
<p>返回条数</p>
<p>否</p>
<p>无</p>
<p>_userId</p>
<p>String</p>
<p>用户id</p>
<p>是</p>
<p>用户名称(如arms_admin)</p>
<p><strong>调用示例</strong></p>
<p>查询指定应用过往7天的接口调用次数</p>
<p>参数填写示范：</p>
<p>字段名称</p>
<p>字段类型</p>
<p>字段含义</p>
<p>必选</p>
<p>示例值</p>
<p>值来源</p>
<p>startTime</p>
<p>Long</p>
<p>查询数据的起始时间</p>
<p>是</p>
<p>1578199319898</p>
<p>系统时间</p>
<p>endTime</p>
<p>Long</p>
<p>查询数据的截止时间</p>
<p>是</p>
<p>1578804119898</p>
<p>系统时间</p>
<p>intervalInSec</p>
<p>Integer</p>
<p>时间间隔</p>
<p>否</p>
<p>默认3600秒，即1小时</p>
<p>人工设置</p>
<p>metric</p>
<p>String</p>
<p>metric字段，查询的指标</p>
<p>是</p>
<p>APPSTAT.DETAIL</p>
<p>人工设置</p>
<p>filters</p>
<p>List[String]</p>
<p>过滤字段,严格按照格式，否则调用出错</p>
<p>是</p>
<p>[&#123;key=pid,value=1218274334230390@db61f75c2f******&#125;,&#123;key=regionId,value=cn-******-d01&#125;]</p>
<p>Pid、regionid来自于专有云环境</p>
<p>measures</p>
<p>List[String]</p>
<p>指标</p>
<p>是</p>
<p>[rt,count,error,errrate]</p>
<p>API文档</p>
<p>dimensions</p>
<p>List[String]</p>
<p>维度</p>
<p>是</p>
<p>[pid,rpcType,rootIp]</p>
<p>API文档</p>
<p>orderBy</p>
<p>String</p>
<p>排序字段</p>
<p>否</p>
<p>无</p>
<p>无</p>
<p>sortOrder</p>
<p>String</p>
<p>排序</p>
<p>否</p>
<p>默认不排序(ASC或者DESC)</p>
<p>无</p>
<p>limit</p>
<p>Integer</p>
<p>返回条数</p>
<p>否</p>
<p>无</p>
<p>无</p>
<p>_userId</p>
<p>String</p>
<p>用户id</p>
<p>是</p>
<p>121827433423****</p>
<p>无</p>
<p><strong>查询结果</strong></p>
<p>参数设置：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60be7558874142038ed941b696aa6962~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图7：参数设置</p>
<p>结果说明：</p>
<ul>
<li>返回结果为JSON数据集。</li>
<li>数据集会标示查询状态，成功返回200，如果失败会返回相应的错误码和错误原因。典型错误例如缺少必要参数、身份认证错误等（是因为filters参数没按格式要求写好）。</li>
<li>OpenAPI返回的结果集组织形式与查询数据的开始时间、结束时间、数据间隔时间有关。本次查询是查询了过往7天，数据间隔时间设置成了24小时，所以这个结果集里返回了7个”data”的集合。</li>
<li>每个data里包括在“measure”和”dimension”里指定的查询，以本结果集为例，就包括：Count:0.0<br>
PID:<br>
rpcDesc: HTTP入口<br>
rpcType:0（HTTP调用）</li>
<li>调整查询的开始、结束、间隔时间，会影响data数据的条数，调整接口查询参数会影响每条data里的数据。</li>
<li>如果需要计算一些聚合值，比如过往7天总的HTTP调用次数，需要自行把多条data数据进行计算相加后得出结果。</li>
</ul>
<h1 data-id="heading-6">6. 查询异常数量</h1>
<p>通过/metric/Metric.json 接口获得应用相关性能数据，查询异常数量。</p>
<p><strong>API说明</strong></p>
<ul>
<li>URL ：<a href="https://link.juejin.cn/?target=http%3A%2F%2Farms.console.example.com%3A8099%2Fmetric%2FMetric.json" target="_blank" rel="nofollow noopener noreferrer" title="http://arms.console.example.com:8099/metric/Metric.json" ref="nofollow noopener noreferrer">arms.console.example.com:8099/metric/Metr…</a></li>
<li>接口说明：</li>
</ul>
<p>字段名称</p>
<p>字段类型</p>
<p>字段含义</p>
<p>是否必选</p>
<p>备注</p>
<p>startTime</p>
<p>Long</p>
<p>查询数据的起始时间</p>
<p>是</p>
<p>无</p>
<p>endTime</p>
<p>Long</p>
<p>查询数据的截止时间</p>
<p>是</p>
<p>无</p>
<p>intervalInSec</p>
<p>Integer</p>
<p>时间间隔</p>
<p>否</p>
<p>建议填写</p>
<p>metric</p>
<p>String</p>
<p>metric字段</p>
<p>是</p>
<p>详细填写参考下文</p>
<p>filters</p>
<p>List[String]</p>
<p>过滤字段</p>
<p>是</p>
<p>详细填写参考下文</p>
<p>measures</p>
<p>List[String]</p>
<p>指标</p>
<p>是</p>
<p>详细填写参考下文</p>
<p>dimensions</p>
<p>List[String]</p>
<p>维度</p>
<p>是</p>
<p>详细填写参考下文</p>
<p>orderBy</p>
<p>String</p>
<p>排序字段</p>
<p>否</p>
<p>无</p>
<p>sortOrder</p>
<p>String</p>
<p>排序</p>
<p>否</p>
<p>默认不排序(ASC或者DESC)</p>
<p>limit</p>
<p>Integer</p>
<p>返回条数</p>
<p>否</p>
<p>无</p>
<p>_userId</p>
<p>String</p>
<p>用户id</p>
<p>是</p>
<p>用户名称(如arms_admin)</p>
<p><strong>调用示例</strong></p>
<p>查询指定应用过往7天的接口调用次数。</p>
<p>参数填写示范：</p>
<p>字段名称</p>
<p>字段类型</p>
<p>字段含义</p>
<p>必选</p>
<p>示例值</p>
<p>值来源</p>
<p>startTime</p>
<p>Long</p>
<p>查询数据的起始时间</p>
<p>是</p>
<p>1577980826988</p>
<p>系统时间</p>
<p>endTime</p>
<p>Long</p>
<p>查询数据的截止时间</p>
<p>是</p>
<p>1578585626989</p>
<p>系统时间</p>
<p>intervalInSec</p>
<p>Integer</p>
<p>时间间隔</p>
<p>否</p>
<p>默认3600秒，即1小时</p>
<p>人工设置</p>
<p>metric</p>
<p>String</p>
<p>metric字段，查询的指标</p>
<p>是</p>
<p>APPSTAT.EXCEPTION</p>
<p>人工设置</p>
<p>filters</p>
<p>List[String]</p>
<p>过滤字段,严格按照格式，否则调用出错。</p>
<p>是</p>
<p>[&#123;key=pid,value=1218274334230390@db61f75c2f******&#125;,&#123;key=regionId,value=cn-******-d01&#125;]</p>
<p>Pid、regionid来自于专有云环境</p>
<p>measures</p>
<p>List[String]</p>
<p>指标</p>
<p>是</p>
<p>[count]</p>
<p>API 文档</p>
<p>dimensions</p>
<p>List[String]</p>
<p>维度</p>
<p>是</p>
<p>[pid,rpc,endpoint,exceptionInfo]</p>
<p>API文档</p>
<p>orderBy</p>
<p>String</p>
<p>排序字段</p>
<p>否</p>
<p>无</p>
<p>无</p>
<p>sortOrder</p>
<p>String</p>
<p>排序</p>
<p>否</p>
<p>默认不排序(ASC或者DESC)</p>
<p>无</p>
<p>limit</p>
<p>Integer</p>
<p>返回条数</p>
<p>否</p>
<p>无</p>
<p>无</p>
<p>_userId</p>
<p>String</p>
<p>用户id</p>
<p>是</p>
<p>1218274334230390</p>
<p>无</p>
<p><strong>查询结果</strong></p>
<p>参数设置：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66aa3e53f3194953a79feb5d6240a8d6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图8：参数设置</p>
<p>查询结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac178352c3244a1db15d555400886d15~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图9：查询结果</p>
<p>结果说明：</p>
<ul>
<li>返回结果为JSON数据集。</li>
<li>数据集会标示查询状态，成功返回200，如果失败会返回相应的错误码和错误原因。典型错误例如缺少必要参数、身份认证错误等（是因为filters参数没按格式要求写好）。</li>
<li>本次查询未查到相关数据，所以exception数量为0。</li>
</ul>
<h1 data-id="heading-7">7. 查询当前应用实例数量</h1>
<p>通过/metric/Metric.json接口获得应用相关性能数据，查询当前应用实例数量。</p>
<p><strong>API说明</strong></p>
<ul>
<li>URL ：<a href="https://link.juejin.cn/?target=http%3A%2F%2Farms.console.example.com%3A8099%2Fmetric%2FMetric.json" target="_blank" rel="nofollow noopener noreferrer" title="http://arms.console.example.com:8099/metric/Metric.json" ref="nofollow noopener noreferrer">arms.console.example.com:8099/metric/Metr…</a></li>
<li>接口说明：</li>
</ul>
<p>字段名称</p>
<p>字段类型</p>
<p>字段含义</p>
<p>是否必选</p>
<p>备注</p>
<p>startTime</p>
<p>Long</p>
<p>查询数据的起始时间</p>
<p>是</p>
<p>无</p>
<p>endTime</p>
<p>Long</p>
<p>查询数据的截止时间</p>
<p>是</p>
<p>无</p>
<p>intervalInSec</p>
<p>Integer</p>
<p>时间间隔</p>
<p>否</p>
<p>建议填写</p>
<p>metric</p>
<p>String</p>
<p>metric字段</p>
<p>是</p>
<p>详细填写参考下文</p>
<p>filters</p>
<p>List[String]</p>
<p>过滤字段</p>
<p>是</p>
<p>详细填写参考下文</p>
<p>measures</p>
<p>List[String]</p>
<p>指标</p>
<p>是</p>
<p>详细填写参考下文</p>
<p>dimensions</p>
<p>List[String]</p>
<p>维度</p>
<p>是</p>
<p>详细填写参考下文</p>
<p>orderBy</p>
<p>String</p>
<p>排序字段</p>
<p>否</p>
<p>无</p>
<p>sortOrder</p>
<p>String</p>
<p>排序</p>
<p>否</p>
<p>默认不排序(ASC或者DESC)</p>
<p>limit</p>
<p>Integer</p>
<p>返回条数</p>
<p>否</p>
<p>无</p>
<p>_userId</p>
<p>String</p>
<p>用户id</p>
<p>是</p>
<p>用户名称(如arms_admin)</p>
<p><strong>调用示例</strong></p>
<p>查询指定应用过往7天的接口调用次数。</p>
<p>参数填写示范：</p>
<p>字段名称</p>
<p>字段类型</p>
<p>字段含义</p>
<p>必选</p>
<p>示例值</p>
<p>值来源</p>
<p>startTime</p>
<p>Long</p>
<p>查询数据的起始时间</p>
<p>是</p>
<p>1577980826988</p>
<p>系统时间</p>
<p>endTime</p>
<p>Long</p>
<p>查询数据的截止时间</p>
<p>是</p>
<p>1578585626989</p>
<p>系统时间</p>
<p>intervalInSec</p>
<p>Integer</p>
<p>时间间隔</p>
<p>否</p>
<p>默认3600秒，即1小时</p>
<p>人工设置</p>
<p>metric</p>
<p>String</p>
<p>metric字段，查询的指标</p>
<p>是</p>
<p>APPSTAT.DETAIL</p>
<p>人工设置</p>
<p>filters</p>
<p>List[String]</p>
<p>过滤字段,严格按照格式，否则调用出错。</p>
<p>是</p>
<p>[&#123;key=pid,value=1218274334230390@db61f75c2f28609&#125;,&#123;key=regionId,value=******&#125;]</p>
<p>Pid、regionid来自于专有云环境</p>
<p>measures</p>
<p>List[String]</p>
<p>指标</p>
<p>是</p>
<p>[count]</p>
<p>API 文档</p>
<p>dimensions</p>
<p>List[String]</p>
<p>维度</p>
<p>是</p>
<p>[pid,rootIp]</p>
<p>API文档</p>
<p>orderBy</p>
<p>String</p>
<p>排序字段</p>
<p>否</p>
<p>无</p>
<p>无</p>
<p>sortOrder</p>
<p>String</p>
<p>排序</p>
<p>否</p>
<p>默认不排序(ASC或者DESC)</p>
<p>无</p>
<p>limit</p>
<p>Integer</p>
<p>返回条数</p>
<p>否</p>
<p>无</p>
<p>无</p>
<p>_userId</p>
<p>String</p>
<p>用户id</p>
<p>是</p>
<p>12182743342******</p>
<p>无</p>
<p><strong>查询结果</strong></p>
<p>参数设置：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12fb6291eef5492a98db3a8e045165e2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图10：参数设置</p>
<p>查询结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9645a02ae0c84493a688561528de0818~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图11：查询结果</p>
<p>结果说明：</p>
<ul>
<li>返回结果为JSON数据集。</li>
<li>数据集会标示查询状态，成功返回200，如果失败会返回相应的错误码和错误原因。典型错误例如缺少必要参数、身份认证错误等（是因为filters参数没按格式要求写好）。</li>
<li>Openapi返回的结果集组织形式与查询数据的开始时间、结束时间、数据间隔时间有关。本次查询是查询了过往7天，数据间隔时间设置成了24小时，所以这个结果集里返回了7个”data”的集合。</li>
<li>每个data里包括在<strong>measure</strong>和<strong>dimension</strong>里指定的查询，以本结果集为例，就包括：Count:0.0<br>
RootIP</li>
<li>本次查询需求是要看此应用一共部署了多少实例，所以对结果中不同IP进行计算，即可以算出共有多少实例数量。另外一个方法是设置intervalInSec的值，让它等查询区间，这样出来的data集合的条数就是实例数量值，因为每个IP都会有条数据。</li>
</ul>
<h1 data-id="heading-8">8. 查询当前应用拓扑图</h1>
<p>通过/trace/Dependecies.json接口获得应用拓扑相关数据。</p>
<p><strong>API说明</strong></p>
<ul>
<li>URL ：<a href="https://link.juejin.cn/?target=http%3A%2F%2Farms.console.example.com%3A8099%2Ftrace%2FDependecies.json" target="_blank" rel="nofollow noopener noreferrer" title="http://arms.console.example.com:8099/trace/Dependecies.json" ref="nofollow noopener noreferrer">arms.console.example.com:8099/trace/Depen…</a></li>
<li>接口说明：</li>
</ul>
<p>字段名称</p>
<p>字段类型</p>
<p>字段含义</p>
<p>是否必选</p>
<p>备注</p>
<p>startTime</p>
<p>Long</p>
<p>查询数据的起始时间</p>
<p>是</p>
<p>无</p>
<p>endTime</p>
<p>Long</p>
<p>查询数据的截止时间</p>
<p>是</p>
<p>无</p>
<p>_userId</p>
<p>String</p>
<p>用户id</p>
<p>是</p>
<p>用户名称（如arms_admin）</p>
<p>type</p>
<p>String</p>
<p>查询类型</p>
<p>是</p>
<p>查询全部关系使用ALL；单个应用的关系使用APP</p>
<p>pid</p>
<p>String</p>
<p>应用对应的pid</p>
<p>否</p>
<p>当type=APP时必须填写</p>
<p><strong>调用示例</strong></p>
<p>查询指定应用过往7天的接口调用次数。</p>
<p>参数填写示范：</p>
<p>本测试1月12日进行，查询过去7天的数据。</p>
<p>字段名称</p>
<p>字段类型</p>
<p>字段含义</p>
<p>必选</p>
<p>示例值</p>
<p>startTime</p>
<p>Long</p>
<p>查询数据的起始时间</p>
<p>是</p>
<p>1578199319898 （1月5日）</p>
<p>endTime</p>
<p>Long</p>
<p>查询数据的截止时间</p>
<p>是</p>
<p>1578804119898 （1月12日）</p>
<p>_userId</p>
<p>String</p>
<p>用户id</p>
<p>是</p>
<p>1218274334******</p>
<p>type</p>
<p>String</p>
<p>查询类型</p>
<p>是</p>
<p>APP</p>
<p>pid</p>
<p>String</p>
<p>应用对应的pid</p>
<p>否</p>
<p>1218274334230390@db61f75c******</p>
<p><strong>查询结果</strong></p>
<p>参数设置：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b41f40a69174566803d7f21cd9c68b8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图12：参数设置</p>
<p>查询结果：</p>
<pre><code class="copyable">&#123;
    "code": 200,
    "data": &#123;
        "link": [&#123;
    "code": 200,
    "data": &#123;
        "link": [
            &#123;
                "callCount": 26997.0,
                "child": "Demo-Service",
                "childNodeId": 731107445,
                "childPid": "1218274334230390@db61f75c2******",
                "elapsed": 16.2328,
                "errorCount": 16.0,
                "parent": "USER",
                "parentNodeId": 812148234,
                "parentPid": "1218274334230390@db61f75c2******",
                "protocol": "HTTP"
            &#125;,
            &#123;
                "callCount": 8.0,
                "child": "pdsa_lhh_rocketmq",
                "childNodeId": -1762019072,
                "childPid": "pdsa_lhh_rocketmq",
                "elapsed": 11190.5,
                "errorCount": 8.0,
                "parent": "Demo-Service",
                "parentNodeId": 731107445,
                "parentPid": "1218274334230390@db61f75c2******",
                "protocol": "AliWareMQ"
            &#125;
        ],
        "nodes": [
            &#123;
                "elapsed": 0.0,
                "errorCount": 0.0,
                "id": 812148234,
                "name": "USER",
                "pid": "1218274334230390@db61f75c2******",
                "requestCount": 0.0,
                "type": "USER"
            &#125;,
            &#123;
                "elapsed": 0.0,
                "errorCount": 0.0,
                "id": 731107445,
                "name": "Demo-Service",
                "pid": "1218274334230390@db61f75c2******",
                "requestCount": 0.0,
                "type": "MQ_PRODUCER"
            &#125;,
            &#123;
                "elapsed": 0.0,
                "errorCount": 0.0,
                "id": -1762019072,
                "name": "pdsa_****_rocketmq",
                "pid": "pdsa_****_rocketmq",
                "requestCount": 0.0,
                "type": "METAQ"
           &#125;
       ]
    &#125;,
    "success": true
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际拓扑图效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e62fab26f13454095a5f5c066d65b78~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图13：拓扑图</p>
<p>结果说明：</p>
<ul>
<li>返回结果为JSON数据集。</li>
<li>数据集会标示查询状态，成功返回200，如果失败会返回相应的错误码和错误原因。典型错误例如缺少必要参数、身份认证错误等（是因为filters参数没按格式要求写好）。</li>
<li>查询结果是一个点线图的节点数据和连接数据，需要使用者自行按照图表控件组装相应数据。</li>
</ul>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000284240%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000284240/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            