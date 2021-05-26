
---
title: 'Kubernetes 稳定性保障手册：洞察+预案'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/bf382e2403fb45e58fd476ccf3f6bf31.png'
author: Dockone
comments: false
date: 2021-05-26 00:21:57
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/bf382e2403fb45e58fd476ccf3f6bf31.png'
---

<div>   
<br>作者 | 悟鹏<br>
来源 | <a href="https://mp.weixin.qq.com/s/xubOge8x-hpHj6Wl6sxQ8A">阿里巴巴云原生公众号</a><br>
<br>《Kubernetes 稳定性保障手册》系列文章：<br>
​<br>
- <a href="http://mp.weixin.qq.com/s?__biz=MzUzNzYxNjAzMg==&mid=2247501775&idx=1&sn=8b3b27934e7bced10b2a7f81483e3256&chksm=fae6cc00cd9145168b57c579ed488a7f92b67f86daf039de6b9518995d9e1ad27df2a382290e&scene=21#wechat_redirect">Kubernetes 稳定性保障手册 -- 极简版</a><br>
- <a href="http://mp.weixin.qq.com/s?__biz=MzUzNzYxNjAzMg==&mid=2247501886&idx=1&sn=a518c619a5c795c77b53566b4a82f95d&chksm=fae6c3f1cd914ae78f51ff95c3782fc40e46b13a8f510aa95834ca816853692d2db4613849c6&scene=21#wechat_redirect">Kubernetes 稳定性保障手册 -- 日志专题</a><br>
- <a href="http://mp.weixin.qq.com/s?__biz=MzUzNzYxNjAzMg==&mid=2247503394&idx=1&sn=8d2e5464e2193eb60162f004e9c4f262&chksm=fae6c5edcd914cfbe00341b334681588e698327087e05a92c664139a455ac386c99c4c0d9747&scene=21#wechat_redirect">Kubernetes 稳定性保障手册 -- 可观测性专题</a><br>
- Kubernetes 稳定性保障手册 -- 洞察+预案（本文）<br>
<br><h1>综述​</h1>​<br>
稳定性保障是个复杂的话题，需要<strong>有效、可迭代、可持续</strong>保障集群的稳定性，系统性的方法或许可以解决该问题。<br>
​<br>
为了形成系统性的方法，可以梳理出稳定性保障复杂性的源头，制定数据模型来对其进行描述，然后在数据模型的基础上对集群的稳定性保障进行<strong>数字化</strong>和<strong>可视化</strong>，以数据模型为内核来持续迭代对稳定性保障的理解、实践以及经验的固化。<br>
​<br>
<h1>稳定性复杂性源头</h1>​<br>
稳定性保障的复杂性源头，一般会有如下维度：<br>
​<br>
- <strong>系统组件数量和交互关系</strong>：随着时间持续变化<br>
- <strong>系统组件和交互的动态行为特征</strong>：不易推导和观察<br>
- <strong>系统资源类型和数量</strong>：随着时间持续变化<br>
- <strong>系统资源的动态行为特征</strong>：不易推导和观察<br>
- <strong>集群的稳定性保障动作</strong>：不易规范和安全执行<br>
<br>总结下来，即：<br>
​<br>
- 如何有效、全面<strong>洞察</strong>集群<br>
- 如何通过<strong>预案</strong>安全执行稳定性保障动作<br>
<br><h1>数据模型</h1>​<br>
可以通过 4 张图和 3 张表对洞察和预案进行数据模型的抽象：<br>
​<br>
<h2>4 张图</h2>​<br>
- <strong>架构关系图</strong>：描述集群组件及其交互关系<br>
- <strong>架构运行图</strong>：描述集群组件及交互的动态特征<br>
- <strong>资源构成图</strong>：描述集群资源的构成<br>
- <strong>资源运行图</strong>：描述集群资源的动态使用特征<br>
<br><h2>3 张表</h2>​<br>
- <strong>事件列表</strong>：描述集群产生的需要关注的事件<br>
- <strong>操作列表</strong>：描述集群中可以执行的管理操作<br>
- <strong>预案列表</strong>：描述集群中事件和操作的关联关系<br>
<br>如下：<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/bf382e2403fb45e58fd476ccf3f6bf31.png" alt="1.png" referrerpolicy="no-referrer"><br>
<br><h1>洞察</h1>​<br>
集群的功能由集群架构提供，功能组件基于集群资源运行，故对于集群稳定性的洞察，核心在于把握<strong>集群架构</strong>和<strong>集群资源</strong>的特征。<br>
​<br>
<h2>1. 架构关系图</h2>​<br>
集群架构通常可以通过<strong>图</strong>来表征，其中节点表征组件，边表征交互关系，通过图结构可以直观把握集群的架构，形如下图：<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/3d7cfbad85054660b8f2ef9150a97f71.png" alt="2.png" referrerpolicy="no-referrer"><br>
<br>可通过形如下的数据结构描述：<br>
<br><code class="prettyprint">&#123;<br>
    &quot;nodes&quot;: [<br>
        &#123;<br>
            &quot;_id&quot;: &quot;0ce0e913f6e5516846c654dbd81db6ecab1f684e&quot;,<br>
            &quot;name&quot;: &quot;kube-apiserver&quot;,<br>
            &quot;description&quot;: &quot;XXX VPC 内&quot;,<br>
            &quot;type&quot;: &quot;managed component&quot;,<br>
            &quot;dependencies&quot;: &#123;&#125;<br>
        &#125;,<br>
        &#123;<br>
            &quot;_id&quot;: &quot;f0740d8bb67520857061a9b71d4a9e4fc50bfe3d&quot;,<br>
            &quot;name&quot;: &quot;etcd&quot;,<br>
            &quot;description&quot;: &quot;XXX VPC 内&quot;,<br>
            &quot;type&quot;: &quot;managed component | storage&quot;,<br>
            &quot;dependencies&quot;: &#123;&#125;<br>
        &#125;,<br>
        &#123;<br>
            &quot;_id&quot;: &quot;05952a825e91cb50a81cbaf23c6941d5c3bb2c89&quot;,<br>
            &quot;name&quot;: &quot;eni-operator&quot;,<br>
            &quot;description&quot;: &quot;XXX VPC 内，管理 ENI&quot;,<br>
            &quot;type&quot;: &quot;component&quot;,<br>
            &quot;dependencies&quot;: &#123;<br>
                &quot;serviceaccount&quot;: &quot;enioperator&quot;,<br>
                &quot;clusterrole&quot;: &quot;enioperator&quot;,<br>
                &quot;clusterrolebinding&quot;: &quot;enioperator&quot;,<br>
                &quot;configmaps&quot;: [&quot;eniconfig&quot;],<br>
                &quot;secrets&quot;: [&quot;enioperator&quot;]<br>
            &#125;<br>
        &#125;,<br>
        &#123;<br>
            &quot;_id&quot;: &quot;42699513a7561e89a5f99881d7b05653a1625c51&quot;,<br>
            &quot;name&quot;: &quot;Network Service&quot;,<br>
            &quot;description&quot;: &quot;提供 VPC/VSwitch 等云网络资源的管理服务&quot;,<br>
            &quot;type&quot;: &quot;cloud service&quot;<br>
        &#125;<br>
    ],<br>
    &quot;edges&quot;: [<br>
        &#123;<br>
            &quot;_id&quot;: &quot;38bce9ca8a0cec6d8586d96298bd63b0523fc946&quot;,<br>
            &quot;source&quot;: &quot;eni-operator&quot;, &quot;target&quot;: &quot;kube-apiserver&quot;,<br>
            &quot;description&quot;: &quot;管理 ENI 请求&quot;<br>
        &#125;,<br>
        &#123;<br>
            &quot;_id&quot;: &quot;93f3c21247165f0be3a969fc80f72bc1a402e9f5&quot;,<br>
            &quot;source&quot;: &quot;eni-operator&quot;, &quot;target&quot;: &quot;Network Service&quot;,<br>
            &quot;description&quot;: &quot;访问阿里云 ECS OpenAPI，管理 VPC/VSwitch 等网络资源&quot;<br>
        &#125;<br>
    ]<br>
&#125;</code><br>
​<br>
<h2>2. 架构运行图</h2>​<br>
集群运行过程中，组件及交互关系可以通过外部观测数据推测内部状态，如 log/metrics/trace。与集群架构图结合，可以在静态架构的基础上叠加动态的洞察数据，更直观把握集群的健康状态，如下图：<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/7b084eef0eca4d9095fd7cefda5c02f5.png" alt="3.png" referrerpolicy="no-referrer"><br>
<br>其中的数字表征洞察数据，可以是「异常数量」「请求流量」等。除了通过数字进行洞察，还可以使用「颜色表征健康状态」「线条粗细表征流量大小」等。<br>
<br>可通过形如下的数据结构描述：<br>
<br><code class="prettyprint">&#123;<br>
    &quot;nodes&quot;: [<br>
      &#123;<br>
            &quot;_id&quot;: &quot;ea4538dc0625d06b0dc93579998e04288656050f&quot;,<br>
            &quot;name&quot;: &quot;mutatehook&quot;,<br>
            &quot;deploy&quot;: &#123;<br>
                &quot;type&quot;: &quot;K8s:Deployment&quot;,<br>
                &quot;namespace&quot;: &quot;kube-system&quot;,<br>
                &quot;replicas&quot;: 3<br>
            &#125;,<br>
            &quot;insight&quot;: [<br>
                &#123;<br>
                    &quot;source&quot;: &#123;<br>
                        &quot;vendor&quot;: &quot;cloud:aliyun:sls&quot;,<br>
                        &quot;log_project&quot;: &quot;xxx&quot;,<br>
                        &quot;log_store&quot;: &quot;mutatehook&quot;,<br>
                        &quot;log_url&quot;: &quot;https://sls.console.aliyun.com/lognext/project/xxx&quot;<br>
                    &#125;,<br>
                    &quot;signal&quot;: &#123;<br>
                        &quot;exception&quot;: &#123;<br>
                            &quot;fuzzy&quot;: &quot;fail OR Fail OR error OR Error&quot;<br>
                        &#125;<br>
                    &#125;<br>
              &#125;<br>
          ]<br>
      &#125;<br>
    ],<br>
    &quot;edges&quot;: [<br>
        &#123;<br>
            &quot;_id&quot;: &quot;38bce9ca8a0cec6d8586d96298bd63b0523fc946&quot;,<br>
            &quot;source&quot;: &quot;eni-operator&quot;, &quot;target&quot;: &quot;kube-apiserver&quot;,<br>
            &quot;insight&quot;:[<br>
                &#123;<br>
                    &quot;source&quot;: &#123;<br>
                        &quot;vendor&quot;: &quot;cloud:aliyun:sls&quot;,<br>
                        &quot;log_project&quot;: &quot;xxx&quot;,<br>
                        &quot;log_store&quot;: &quot;xxx&quot;,<br>
                        &quot;log_url&quot;: &quot;https://sls.console.aliyun.com/lognext/project/xxx&quot;<br>
                    &#125;,<br>
                    &quot;signal&quot;: &#123;<br>
                        &quot;exception&quot;: &#123;<br>
                            &quot;unauthorized&quot;: &quot;Unauthorized&quot;,<br>
                            &quot;throttling&quot;: &quot;'Throttling' OR 'throttling'&quot;<br>
                        &#125;<br>
                    &#125;<br>
                &#125;<br>
            ]<br>
        &#125;<br>
    ]<br>
&#125;</code><br>
​<br>
<h2>3. 资源构成图</h2>资源管理是个复杂的话题，通过分析集群中资源的构成关系，也可以尝试通过<strong>图</strong>结构来表征集群的资源构成，节点表征资源，边表征资源的从属或绑定关系。<br>
​<br>
可通过形如下的数据结构描述：<br>
<br><code class="prettyprint">&#123;<br>
    &quot;kinds&quot;: [&quot;vpc&quot;, &quot;vswitch&quot;, &quot;securitygroup&quot;, &quot;ecs&quot;, &quot;clb&quot;, &quot;rds&quot;, &quot;nat&quot;, &quot;eip&quot;],<br>
    &quot;tags&quot;: &#123;<br>
        &quot;cluster/product&quot;: &quot;xxx&quot;,<br>
        &quot;cluster/id&quot;: &quot;2736f42d4e882ad6825d6364545a3f1cb5136859&quot;,<br>
        &quot;cluster/name&quot;: &quot;xxx&quot;,<br>
        &quot;cluster/env&quot;: &quot;staging&quot;<br>
    &#125;,<br>
    &quot;nodes&quot;: [<br>
        &#123;<br>
            &quot;kind&quot;: &quot;vpc&quot;,<br>
            &quot;nodes&quot;: [<br>
                &#123;<br>
                    &quot;_id&quot;: &quot;c505f21871bac7385c1387988cf226310af0831e&quot;,<br>
                    &quot;id&quot;: &quot;vpc-xxx&quot;,<br>
                    &quot;description&quot;: &quot;&quot;,<br>
                    &quot;ipv4&quot;: &quot;xxx&quot;,<br>
                    &quot;tags&quot;: &#123;<br>
                        &quot;resource/creator&quot;: &quot;product&quot;,<br>
                        &quot;resource/role&quot;: &quot;&quot;<br>
                     &#125;,<br>
                     &quot;url&quot;: &quot;https://vpc.console.aliyun.com/vpc/xxx&quot;<br>
                &#125;<br>
            ]<br>
        &#125;,<br>
        &#123;<br>
            &quot;kind&quot;: &quot;ecs&quot;,<br>
            &quot;nodes&quot;: [<br>
                &#123;<br>
                    &quot;_id&quot;: &quot;47c4fe5cc2585a49f07798a0b8b69cda7f8d4a23&quot;,<br>
                    &quot;id&quot;: &quot;xxx&quot;,<br>
                    &quot;az&quot;: &quot;xxx&quot;,<br>
                    &quot;interfaces&quot;: &#123;<br>
                        &quot;primary&quot;: &#123;<br>
                            &quot;ip&quot;: &quot;xxx&quot;,<br>
                            &quot;eni&quot;: &quot;xxx&quot;,<br>
                            &quot;mac&quot;: &quot;xxx&quot;<br>
                        &#125;<br>
                    &#125;,<br>
                    &quot;instance-type-family&quot;: &quot;xxx&quot;,<br>
                    &quot;instance-type&quot;: &quot;xxx&quot;,<br>
                    &quot;tags&quot;: &#123;<br>
                        &quot;resource/creator&quot;: &quot;product&quot;,<br>
                        &quot;resource/role&quot;: &quot;worker&quot;,<br>
                        &quot;node/container-runtime&quot;: &quot;xxx&quot;,<br>
                        &quot;node/user-networking&quot;: &quot;xxx&quot;,<br>
                        &quot;node/system-networking&quot;: &quot;xxx&quot;<br>
                    &#125;,<br>
                    &quot;status&quot;: &quot;&quot;,<br>
                    &quot;condition&quot;: &quot;&quot;,<br>
                    &quot;url&quot;: &quot;https://ecs.console.aliyun.com/#/server/xxx&quot;<br>
                &#125;<br>
            ]<br>
        &#125;<br>
    ],<br>
    &quot;edges&quot;: [<br>
        &#123;<br>
            &quot;_id&quot;: &quot;a754c748b2723a25c017421dd0969d00df3c000b&quot;,<br>
            &quot;source&quot;: &quot;vsw-xxx&quot;, &quot;target&quot;: &quot;vpc-xxx&quot;,<br>
            &quot;description&quot;: &quot;&quot;<br>
        &#125;,<br>
        &#123;<br>
            &quot;_id&quot;: &quot;c34b164eba2897cfb2b574a576672d8aa441d709&quot;,<br>
            &quot;source&quot;: &quot;eip-xxx&quot;, &quot;target&quot;: &quot;ngw-xxx&quot;,<br>
            &quot;description&quot;: &quot;&quot;<br>
        &#125;<br>
    ]<br>
&#125;</code><br>
​<br>
<h2>4. 资源运行图</h2>​<br>
资源使用过程中，也可以对资源及资源间的关系通过外部观测数据推测内部状态，如 log/metrics/event。与资源构成图结合，可以在静态资源的基础上叠加动态的洞察数据，直观把握集群资源的使用状态。<br>
​<br>
可通过形如下的数据结构描述：<br>
<br><code class="prettyprint">&#123;<br>
    &quot;nodes&quot;: [<br>
         &#123;<br>
            &quot;_id&quot;: &quot;35103ac62d4ef0a314e2a5128f44c684205bea2f&quot;,<br>
            &quot;id&quot;: &quot;vpc&quot;,<br>
            &quot;insight&quot;: [<br>
                &#123;<br>
                    &quot;source&quot;: &#123;<br>
                        &quot;vendor&quot;: &quot;cloud:aliyun:vpc&quot;,<br>
                        &quot;type&quot;: &quot;OpenAPI&quot;<br>
                    &#125;,<br>
                    &quot;signal&quot;: &#123;<br>
                        &quot;vpc/exist&quot;: &quot;DescribeVpcs&quot;,<br>
                        &quot;vswitch/count&quot;: &quot;DescribeVSwitches&quot;<br>
                    &#125;<br>
                &#125;,<br>
                &#123;<br>
                    &quot;source&quot;: &#123;<br>
                        &quot;vendor&quot;: &quot;cloud:aliyun:ecs&quot;,<br>
                        &quot;type&quot;: &quot;OpenAPI&quot;<br>
                    &#125;,<br>
                    &quot;signal&quot;: &#123;<br>
                        &quot;ecs/count&quot;: &quot;DescribeInstances&quot;,<br>
                        &quot;securitygroup/count&quot;: &quot;DescribeSecurityGroups&quot;<br>
                    &#125;<br>
                &#125;<br>
            ]<br>
        &#125;,<br>
        &#123;<br>
            &quot;_id&quot;: &quot;6450e07dc67027f76f29fbfcb841e57200855196&quot;,<br>
            &quot;id&quot;: &quot;ecs&quot;,<br>
            &quot;insight&quot;: [<br>
                &#123;<br>
                    &quot;source&quot;: &#123;<br>
                        &quot;vendor&quot;: &quot;cloud:aliyun:ecs&quot;,<br>
                        &quot;type&quot;: &quot;OpenAPI&quot;<br>
                    &#125;,<br>
                    &quot;signal&quot;: &#123;<br>
                        &quot;ecs/exist&quot;: &quot;DescribeInstances&quot;,<br>
                        &quot;ecs/count&quot;: &quot;DescribeInstances&quot;,<br>
                        &quot;ecs/usage&quot;: &quot;DescribeInstanceMonitorData&quot;<br>
                    &#125;<br>
                &#125;,<br>
                &#123;<br>
                    &quot;source&quot;: &#123;<br>
                        &quot;vendor&quot;: &quot;cloud:aliyun:ecs&quot;,<br>
                        &quot;type&quot;: &quot;auto&quot;<br>
                    &#125;,<br>
                    &quot;signal&quot;: &#123;<br>
                        &quot;ecs/state_change&quot;: &quot;&quot;<br>
                    &#125;<br>
                &#125;<br>
            ]<br>
        &#125;<br>
    ],<br>
    &quot;edges&quot;: [<br>
        &#123;<br>
            &quot;_id&quot;: &quot;caa1e395c713f47766ca7bcfc20419c0be0f0803&quot;,<br>
            &quot;source&quot;: &quot;i-xxx&quot;, &quot;target&quot;: &quot;sg-xxx&quot;,<br>
            &quot;insight&quot;: [<br>
                &#123;<br>
                    &quot;source&quot;: &#123;<br>
                        &quot;vendor&quot;: &quot;cloud:aliyun:ecs&quot;,<br>
                        &quot;type&quot;: &quot;OpenAPI&quot;<br>
                    &#125;,<br>
                    &quot;signal&quot;: &#123;<br>
                        &quot;exist&quot;: &quot;DescribeInstances&quot;<br>
                    &#125;<br>
                &#125;<br>
            ]<br>
        &#125;,<br>
        &#123;<br>
            &quot;_id&quot;: &quot;537dc478d95714792b3694674d6164f72b361bb0&quot;,<br>
            &quot;source&quot;: &quot;eip-xxx&quot;, &quot;target&quot;: &quot;ngw-xxx&quot;,<br>
            &quot;insight&quot;: [<br>
                &#123;<br>
                    &quot;source&quot;: &#123;<br>
                        &quot;vendor&quot;: &quot;cloud:aliyun:vpc&quot;,<br>
                        &quot;type&quot;: &quot;OpenAPI&quot;<br>
                    &#125;,<br>
                    &quot;signal&quot;: &#123;<br>
                        &quot;exist&quot;: &quot;DescribeEipAddresses&quot;<br>
                    &#125;<br>
                &#125;<br>
            ]<br>
        &#125;<br>
    ]<br>
&#125;</code><br>
<br><h1>预案</h1>​<br>
集群出现异常是不可避免的，需要在出现异常时安全、有效处理。<br>
​<br>
异常可以通过事件来表征，安全、有效的操作是经过评审、演练过的操作，将异常与操作结合，由异常触发操作，形成经过评审、演练的预案，可以安全有效处理集群异常。<br>
​<br>
<h2>1. 事件列表</h2>​<br>
集群运行过程中会产生需要关注的事件，事件自身的格式可基于社区 CloudEvents标准来使用：_<a href="https://github.com/cloudevents/spec/blob/v1.0.1/spec.md_" rel="nofollow" target="_blank">https://github.com/cloudevents ... c.md_</a>。<br>
​<br>
可通过形如下的数据结构描述：<br>
<br><code class="prettyprint">&#123;<br>
    &quot;events&quot;: [<br>
        &#123;<br>
            &quot;_id&quot;: &quot;a1ab5b61857be35a5c5b203dd84b49248161c823&quot;,<br>
            &quot;description&quot;: &quot;restart workload manually&quot;,<br>
            &quot;event&quot;: &#123;<br>
                &quot;id&quot;: &quot;restart-workload&quot;,<br>
                &quot;source&quot;: &quot;xxx&quot;,<br>
                &quot;specversion&quot;: &quot;1.0&quot;,<br>
                &quot;type&quot;: &quot;com.aliyun.trigger.manual&quot;,<br>
                &quot;datacontenttype&quot;: &quot;application/json&quot;,<br>
                &quot;data&quot;: &quot;&#123;\&quot;NAMESPACE\&quot;: \&quot;\&quot;, \&quot;NAME\&quot;: \&quot;\&quot;, \&quot;TYPE\&quot;: \&quot;\&quot;&#125;&quot;<br>
            &#125;<br>
        &#125;<br>
    ]<br>
&#125;</code><br>
​<br>
<h2>2. 操作列表</h2>​<br>
为了降低误操作的可能性，同时避免异常发生时执行未经审核、验证的操作，需要定义集群中可以进行的操作列表。<br>
​<br>
可通过形如下的数据结构描述：<br>
<br><code class="prettyprint">&#123;<br>
    &quot;actions&quot;: [<br>
        &#123;<br>
            &quot;_id&quot;: &quot;47abc5cd9d64018ebf96dc5b2d6a4fbd35a3cb6d&quot;,<br>
            &quot;name&quot;: &quot;Action Restart Workload&quot;,<br>
            &quot;exec&quot;: &quot;restart-workload&quot;,<br>
            &quot;env&quot;: [<br>
                &quot;NAMESPACE&quot;,<br>
                &quot;NAME&quot;,<br>
                &quot;TYPE&quot;<br>
            ]<br>
        &#125;<br>
    ]<br>
&#125;</code><br>
<br><h2>3. 预案列表</h2>​<br>
在事件列表和操作列表基础上，可以将事件和操作关联起来，以事件驱动的方式处理异常，即预案。<br>
​<br>
可通过形如下的数据结构描述：<br>
<br><code class="prettyprint">&#123;<br>
    &quot;plans&quot;: [<br>
        &#123;<br>
            &quot;_id&quot;: &quot;29a091c48d8992991ed69e8694b017a11abe3eec&quot;,<br>
            &quot;name&quot;: &quot;Plan Restart Workload&quot;,<br>
            &quot;description&quot;: &quot;重启 workload&quot;,<br>
            &quot;event&quot;: &quot;a1ab5b61857be35a5c5b203dd84b49248161c823&quot;,<br>
            &quot;actions&quot;: [&quot;47abc5cd9d64018ebf96dc5b2d6a4fbd35a3cb6d&quot;]<br>
        &#125;<br>
    ]<br>
&#125;</code><br>
<br><h1>全局可视化稳定性保障</h1>​<br>
基于上述<strong>4 张图</strong>和<strong>3 张表</strong>的数据模型，形成对集群稳定性保障的<strong>洞察+预案</strong>的内核，可以衍生出一种全局可视化的稳定性保障服务。<br>
​<br>
这样的服务具有如下关键点：<br>
​<br>
- 全局视角<br>
- 数字化<br>
- 可视化<br>
<br>这种服务基于两种原理实现：<br>
​<br>
- 人们对图像的处理效率远高于文字<br>
- 全局视角可以提供「端到端理解系统」「精准定位问题」「安全处理问题」的能力<br>
<br>以日常生活中的交通图为例：<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/622e908b5fdc4d748a7582dc5ac83c90.png" alt="4.png" referrerpolicy="no-referrer"><br>
<br>通过交通图，可以快速了解到一个区域的道路分布和关键节点，约定俗成的红黄绿颜色可以直观表达道路的拥堵状况。在更丰富的交通图上，还会观察到诸如修路、封路等重要事件。<br>
​<br>
这样，基于可视化的方式，就可以迅速理解一个区域的交通和地理情况。<br>
​<br>
底层的数据模型是基础，应用可视化的手段，使得数据的价值更易被发挥。<br>
​<br>
<h2>一种实现</h2>​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/99ff1f53975c4870bed7d3d45eb01785.png" alt="5.png" referrerpolicy="no-referrer"><br>
<br><h3>1）部署形态</h3>​<br>
- Region 化部署<br>
- 面向 Region 内单集群或多集群提供服务<br>
<br><h3><strong>2）使用体感</strong></h3>​<br>
<strong>根据稳定性保障的最佳实践，将稳定性保障分为如下几个栏目</strong>：<br>
<ul><li>运行链路图：<br>
<ul>- 该栏目是日常稳定性保障高频使用的区域，通过可视化的能力，直观感知异常的发生、异常范围和影响程度、白屏化+可视化方式处理异常</ul></li><li>部署架构图<br>
<ul><li>该栏目用于理解集群的部署架构，感知和处理部署维度的问题</li>- 容量管理 (包括节点管理、容量规划等) 在此栏目进行</ul></li><li>业务流程图<br>
<ul><li>该栏目沉淀业务的功能流程图，一方面协助业务控制功能复杂度，一方面协助业务理解业务功能现状，共同助力业务迭代</li>- 业务相关的数据分析可放在该栏目</ul></li><li>数据分析：该栏目服务两方面的数据需求<br>
<ul><li>业务需求<br>
<ul><li>查看类：集群规模等 SLI 信息、集群稳定性等 SLO 信息</li>- 查询类：根据特征查询统计信息 (如根据 label 查询资源申请等)</ul></li>- 稳定性保障需求<li><br>查看类：集群水位等 SLI 信息，集群稳定性保障效果等 SLO 信息</li>  - 查询类：根据特征查询统计信息 (如根据 label 查询关联的所有资源信息、资源泄露信息等)</ul></li><li>可观测性管理<br>
<ul>- 该栏目用管理可观测性相关事宜，包括：<li><br>观测数据生成</li><li>观测数据采集</li><li>观测数据处理</li>  - 观测数据消费</ul></li><li>可控性管理<br>
<ul>- 该栏目用于管理与控制相关的操作，包括：<li><br>发布管理</li><li>灾备管理</li><li>预案管理</li><li>资源管理</li><li>混沌工程</li><li>安全管理</li>  - 定期体检</ul></li></ul><br>
<br><strong>系统正常运行期间</strong>：<br>
​<br>
- 通过「数据分析」栏目，确认集群在「可观测性」「可控性」方面的覆盖面和精确性<br>
- 在「可观测性管理」栏目，进行可观测维度的管理，包括 数据源/监控/告警补齐、治理等<br>
- 在「可控性管理」栏目:<br>
   - 根据观测数据发现的问题，进行预案配置、issue 管理等<br>
   - 根据混沌工程或演练发现的问题，进行预案配置等<br>
- 在「运行链路图」「部署架构图」中，通过可视化方式，将已经配置的监控、告警、预案与组件或链路结合<br>
<br><strong>系统异常及恢复期间，在「运行链路图」中</strong>：<br>
​<br>
- 通过集群运行链路图或告警，感知异常的发生<br>
- 自动或手动触发问题跟踪<br>
- 通过集群运行链路图中组件及交互的颜色，感知异常的组件、异常的链路和严重程度<br>
- 点击集群运行链路图中组件的异常数字，获取关联的异常详情，或跳转到日志、tracing 系统等进行手动查询<br>
- 根据异常详情或平台提示，确定待执行的预案和关联的组件<br>
- 在集群运行链路图中执行预案 (阻断问题或恢复服务)<br>
- 通过集群运行链路图中组件及交互的颜色，确认预案执行效果<br>
- 自动或手动结束问题跟踪<br>
<br>问题跟踪过程中记录的主要内容有：<br>
​<br>
- issue<br>
- 异常发生的时刻<br>
- 异常处理期间执行的动作<br>
- 运行链路图 snapshot<br>
- 异常恢复的时刻<br>
<br><h1>数据模型及竞争力分析</h1>​<br>
数据模型是稳定性保障最佳实践进行迭代、分享和应用的媒介，通用的洞察和预案可以形成标准化的服务，个性化的洞察和预案可通过固定的结构来描述，然后使用通用的控制器来落地。<br>
​<br>
以数据模型形成<strong>洞察+预案</strong>的稳定性保障服务，技术核心为：<br>
​<br>
- 洞察模型<br>
   - 关键问题：<br>
      - 如何洞察集群稳定性？<br>
      - 如何洞察业务迭代效率？<br>
- 数据模型<br>
   - 关键问题：<br>
      - 如何定义有效、可扩展的数据描述?<br>
<br>在技术核心的基础上，可以围绕如下的竞争力进行迭代：<br>
​<br>
- 洞察<br>
   - 全局化<br>
   - 数字化<br>
   - 可视化<br>
- 效率<br>
   - 最短操作路径<br>
   - 最小使用成本<br>
- 先进性<br>
   - 流程化最佳实践<br>
<br><h1>小结</h1>​<br>
通过 Spec 规范 7 种数据模型，我们可以基于结构化的描述来表征洞察+预案。以此为核心，不断迭代对稳定性保障的实践和理解，加速业务迭代。再扩展一步，也有可能基于该模型在发展方向反哺业务。<br>
​<br>
如果大家感兴趣，欢迎在留言区进行交流。
                                
                                                              
</div>
            