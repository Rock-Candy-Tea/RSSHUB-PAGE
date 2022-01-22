
---
title: '在Rainbond上使用Locust进行压力测试'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://static.goodrain.com/wechat/locust/install-locust.png'
author: Dockone
comments: false
date: 2022-01-22 08:08:50
thumbnail: 'https://static.goodrain.com/wechat/locust/install-locust.png'
---

<div>   
<br><h2>Locust简介</h2><a href="https://locust.io/">Locust</a> 是一种易于使用、可编写脚本且可扩展的性能测试工具。并且有一个用户友好的 Web 界面，可以实时显示测试进度。甚至可以在测试运行时更改负载。它也可以在没有 UI 的情况下运行，使其易于用于 CI/CD 测试。<br>
<br>Locust 使运行分布在多台机器上的负载测试变得容易。Locust 基于事件（gevent），因此可以在一台计算机上支持数千个并发用户。与许多其他基于事件的应用程序相比，它不使用回调。相反，它通过gevent使用轻量级进程。并发访问站点的每个Locust（蝗虫）实际上都在其自己的进程中运行（Greenlet）。这使用户可以在Python中编写非常有表现力的场景，而不必使用回调或其他机制。<br>
<br><h2>快速部署Locust</h2><code class="prettyprint">Locust</code> 应用已发布到 <code class="prettyprint">开源应用商店</code>，搜索 <code class="prettyprint">locust</code> 安装最新<code class="prettyprint">2.5.1</code>版本即可。<br>
<br><img src="https://static.goodrain.com/wechat/locust/install-locust.png" alt referrerpolicy="no-referrer"><br>
<br>安装完成后，您将会得到一个Locust主从集群，其中，master组件负责提供UI界面，和并发任务的调度；slave组件负责执行并发任务，slave组件同时支持横向伸缩，当产生的测试并发达到一定的限额时，只需扩展 slave 组件实例即可，例如：<br>
<br><img src="https://static.goodrain.com/wechat/locust/tp.png" alt referrerpolicy="no-referrer"><br>
<br><h2>如何使用</h2><code class="prettyprint">Locust_Master</code> 提供了一个基于WEB-UI的图形化管理界面，首次登陆，会提示输入一些信息：<br>
<br><blockquote><br>默认用户密码：locust locust，可配置 <code class="prettyprint">Locust_Master</code> 组件的环境变量 <code class="prettyprint">LOCUST_WEB_AUTH</code>进行修改。</blockquote><img src="https://static.goodrain.com/wechat/locust/locust-index.png" alt referrerpolicy="no-referrer"><br>
<br><strong>Number of users</strong> 填写模拟的并发用户数量，经过测试，单个slave实例可以轻松提供上千个用户并发的压力。<br>
<br><strong>Spawn rate</strong> 填写<code class="prettyprint">蝗虫</code>的孵化率，即每秒产生多少用户。<br>
<br><strong>Host</strong> 填写想要压测的站点地址。<br>
<br>当Host以及用户，并发量定义完毕以后，还需要去定义一下测试用例，即用户访问Host之后的行为，Locust是通过一个名为<code class="prettyprint">/locustfile.py</code> 的Python脚本来定义用户行为，在Rainbond平台的 <code class="prettyprint">Locust_Master</code> 组件内 <code class="prettyprint">环境配置</code> -> <code class="prettyprint">配置文件设置</code> 进行编辑修改。<br>
<br><img src="https://static.goodrain.com/wechat/locust/locustfile.png" alt referrerpolicy="no-referrer"><br>
<br>代码示例如下：<br>
<pre class="prettyprint">from locust import HttpUser, task, between<br>
<br>
class MyUser(HttpUser):<br>
wait_time = between(5, 15)<br>
<br>
@task(2)<br>
def index(self):<br>
    self.client.get("/")<br>
<br>
@task(1)<br>
def about(self):<br>
    self.client.get("/docs/")<br>
</pre><br>
<br>这个脚本将按照顺序模仿以下行为：<br>
<ol><li>请求Host的 <code class="prettyprint">/</code> 路径两次</li><li>请求Host的 <code class="prettyprint">/docs/</code> 路径一次</li><li>每次执行任务之间，间隔5-15秒</li></ol><br>
<br>之所以要这么设计的原因，是Locust的设计者们认为，真正的用户行为，不会像脚本一样接连不断的执行完所有的请求然后退出。更多的情况是，用户做完一件事后，会停顿一会，比如读读说明，思考下一步要干嘛。所以会在每个步骤之间留下一个随机时长的空白期。这种假设实际上更符合用户实际行为。<br>
<br>这个文件，将会以配置文件的方式挂载到 <code class="prettyprint">locust_master</code> 组件上，并且共享挂载给所有的<code class="prettyprint">locust_slave</code>组件。这意味着，如果你想要更改这个文件的内容，只需要去编辑 <code class="prettyprint">locust_master</code> 组件中，环境配置下所挂载的配置文件即可。然后更新整个 Locust 集群即可生效。<br>
<br><h2>结果分析</h2>借助Locust提供的WEB-UI界面，我们可以非常方便的分析压力测试结果。<br>
<br><img src="https://static.goodrain.com/wechat/locust/locust-result.png" alt referrerpolicy="no-referrer"><br>
<br>Statistics页面，将向我们展示所有被压测接口的汇总报告。结果包括：<br>
<br><strong>Type</strong> 请求类型；<br><br>
<strong>Name</strong> 请求路径；<br><br>
<strong>Requests</strong> 请求总数；<br><br>
<strong>Fails</strong> 失败次数；<br><br>
<strong>Median</strong> 中位数响应时间；<br><br>
<strong>90%ile</strong> 90%请求响应时间；<br><br>
<strong>Average</strong> 平均响应时间；<br><br>
<strong>Min</strong> 最小响应时间；<br><br>
<strong>Max</strong> 最大响应时间；<br><br>
<strong>Average size</strong> 请求的平均大小；<br><br>
<strong>Current PRS</strong> 当前吞吐率；<br><br>
<strong>Current Failures</strong> 当前错误率；<br>
<br><img src="https://static.goodrain.com/wechat/locust/locust-charts.png" alt referrerpolicy="no-referrer"><br>
<br>Charts页面将主要结果绘制成为随时间变化的图表，能够在趋势上给予用户指引。<br>
<br>除了这些之外，还有几项值得关注的值会在最上面一排全局展示，包括当前请求的主机域名、当前产生的并发用户数量、slave节点数量、当前所有请求接口的总吞吐率、错误率。以及停止测试的按钮。<br>
<br>其它的几个页面会提供：<br>
<br><strong>Failures</strong> 请求失败的接口及失败原因；<br><br>
<strong>Expections</strong> 测试中意外的错误以及错误原因<br><br>
<strong>Download Data</strong> csv格式的测试数据下载地址<br><br>
<strong>Workers</strong> 所有slave实例的信息  <br>
<br>更多教程请参考<a href="http://docs.locust.io/en/stable/what-is-locust.html">Locust官方文档</a><br>
<br><h2>关于Rainbond</h2><a href="https://www.rainbond.com/?channel=dockone">Rainbond</a> 是一个开源的云原生应用管理平台，使用简单，不需要懂容器和Kubernetes，支持管理多个Kubernetes集群，提供企业级应用的全生命周期管理，功能包括应用开发环境、应用市场、微服务架构、应用持续交付、应用运维、应用级多云管理等。
                                
                                                              
</div>
            