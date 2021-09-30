
---
title: 'Prometheus监控业务指标'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210926/d53cc27c1c2fc70789238092d6775471.png'
author: Dockone
comments: false
date: 2021-09-30 00:27:47
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210926/d53cc27c1c2fc70789238092d6775471.png'
---

<div>   
<br>在Kubernetes已经成了事实上的容器编排标准之下，微服务的部署变得非常容易。但随着微服务规模的扩大，服务治理带来的挑战也会越来越大。在这样的背景下出现了服务可观测性（observability）的概念。在分布式系统里，系统的故障可能出现在任何节点，怎么能在出了故障的时候快速定位问题和解决问题，甚至是在故障出现之前就能感知到服务系统的异常，把故障扼杀在摇篮里。这就是可观测性的意义所在。<br>
<h3>可观测性</h3>可观测性是由Logging，Metrics，Tracing构建的，简称为可观测性三支柱。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210926/d53cc27c1c2fc70789238092d6775471.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210926/d53cc27c1c2fc70789238092d6775471.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>Lgging，展现的是应用运行而产生的事件或者程序在执行的过程中间产生的一些日志，可以详细解释系统的运行状态，但是存储和查询需要消耗大量的资源。所以往往使用过滤器减少数据量。</li><li>Metrics，是一种聚合数值，存储空间很小，可以观察系统的状态和趋势，但对于问题定位缺乏细节展示。这个时候使用等高线指标等多维数据结构来增强对于细节的表现力。例如统计一个服务的 TBS 的正确率、成功率、流量等，这是常见的针对单个指标或者某一个数据库的。</li><li>Tracing，面向的是请求，可以轻松分析出请求中异常点，但与Logging有相同的问题就是资源消耗较大。通常也需要通过采样的方式减少数据量。比如一次请求的范围，也就是从浏览器或者手机端发起的任何一次调用，一个流程化的东西，我们需要轨迹去追踪。</li></ul><br>
<br>我们在这篇文章讨论的主题就是可观测性中的Metrics。在 Kubernetes作为基础设施的背景下，我们知道Kubernetes本身是个复杂的容器编排系统，它本身的稳定运行至关重要。与之相伴的指标监控系统 Promethues也已经成为了云原生服务下监控体系的事实标准。相信大家对资源层面比如CPU，Memory，Network；应用层面比如Http请求数，请求耗时等指标的监控都有所了解。那么业务层面的指标又怎么利用Prometheus去监控和告警呢？这就是这篇文章的核心内容。<br>
<br>以我们一个业务场景为例，在系统中有多种类型的task在运行，并且task的运行时间各异，task本身有各种状态包括待执行、执行中、执行成功、执行失败等。如果想确保系统的稳定运行，我们必须对各个类型的 task 的运行状况了如指掌。比如当前是否有任务挤压，失败任务是否过多，并且当超过阈值是否告警。<br>
<br>为了解决上述的监控告警问题，我们先得了解一下Prometheus的指标类型。<br>
<h3>指标</h3><h4>指标定义</h4>在形式上，所有的指标（Metric）都通过如下格式标示：<br>
<pre class="prettyprint"><metric name>&#123;<label name>=<label value>, ...&#125; <br>
</pre><br>
指标的名称（metric name）可以反映被监控样本的含义（比如，http_request_total - 表示当前系统接收到的HTTP请求总量）。指标名称只能由ASCII字符、数字、下划线以及冒号组成并必须符合正则表达式[a-zA-Z_:][a-zA-Z0-9_:]*。<br>
<br>标签（label）反映了当前样本的特征维度，通过这些维度Prometheus可以对样本数据进行过滤，聚合等。标签的名称只能由ASCII字符、数字以及下划线组成并满足正则表达式[a-zA-Z_][a-zA-Z0-9_]*。<br>
<h4>指标类型</h4>Prometheus定义了4种不同的指标类型（metric type）：Counter（计数器）、Gauge（仪表盘）、Histogram（直方图）、Summary（摘要）<br>
<br><strong>Counter</strong><br>
<br>Counter类型的指标其工作方式和计数器一样，只增不减（除非系统发生重置）。常见的监控指标，如http_requests_total，node_cpu都是Counter类型的监控指标。一般在定义Counter类型指标的名称时推荐使用_total作为后缀。<br>
<br>通过counter指标我们可以和容易的了解某个事件产生的速率变化。<br>
<br>例如，通过rate()函数获取HTTP请求量的增长率：<br>
<pre class="prettyprint">rate(http_requests_total[5m])<br>
</pre><br>
<strong>Gauge</strong><br>
<br>Gauge类型的指标侧重于反应系统的当前状态。因此这类指标的样本数据可增可减。常见指标如：node_memory_MemFree（主机当前空闲的内容大小）、node_memory_MemAvailable（可用内存大小）都是Gauge类型的监控指标。<br>
<br>通过Gauge指标，我们可以直接查看系统的当前状态<br>
<pre class="prettyprint">node_memory_MemFree<br>
</pre><br>
<strong>Summary</strong><br>
<br>Summary主用用于统计和分析样本的分布情况。比如某Http请求的响应时间大多数都在100 ms内，而个别请求的响应时间需要5s，那么这中情况下统计指标的平均值就不能反映出真实情况。而如果通过Summary指标我们能立马看响应时间的9分位数，这样的指标才是有意义的。<br>
<br>例如：<br>
<pre class="prettyprint"># HELP go_gc_duration_seconds A summary of the pause duration of garbage collection cycles.<br>
# TYPE go_gc_duration_seconds summary<br>
go_gc_duration_seconds&#123;quantile="0"&#125; 3.98e-05<br>
go_gc_duration_seconds&#123;quantile="0.25"&#125; 5.31e-05<br>
go_gc_duration_seconds&#123;quantile="0.5"&#125; 6.77e-05<br>
go_gc_duration_seconds&#123;quantile="0.75"&#125; 0.0001428<br>
go_gc_duration_seconds&#123;quantile="1"&#125; 0.0008099<br>
go_gc_duration_seconds_sum 0.0114183<br>
go_gc_duration_seconds_count 85<br>
</pre><br>
<strong>Histogram</strong><br>
<br>Histogram类型的指标同样用于统计和样本分析。与Summary类型的指标相似之处在于Histogram类型的样本同样会反应当前指标的记录的总数（以_count作为后缀）以及其值的总量（以_sum作为后缀）。不同在于Histogram指标直接反应了在不同区间内样本的个数，区间通过标签len进行定义。同时对于Histogram的指标，可以通过<code class="prettyprint">histogram_quantile()</code>函数计算出其值的分位数。<br>
<br>例如：<br>
<pre class="prettyprint"># HELP prometheus_http_response_size_bytes Histogram of response size for HTTP requests.<br>
# TYPE prometheus_http_response_size_bytes histogram<br>
prometheus_http_response_size_bytes_bucket&#123;handler="/",le="100"&#125; 1<br>
prometheus_http_response_size_bytes_bucket&#123;handler="/",le="1000"&#125; 1<br>
prometheus_http_response_size_bytes_bucket&#123;handler="/",le="10000"&#125; 1<br>
prometheus_http_response_size_bytes_bucket&#123;handler="/",le="100000"&#125; 1<br>
prometheus_http_response_size_bytes_bucket&#123;handler="/",le="1e+06"&#125; 1<br>
prometheus_http_response_size_bytes_bucket&#123;handler="/",le="+Inf"&#125; 1<br>
prometheus_http_response_size_bytes_sum&#123;handler="/"&#125; 29<br>
prometheus_http_response_size_bytes_count&#123;handler="/"&#125; 1<br>
</pre><br>
<h3>应用指标监控</h3><h4>暴露指标</h4>Prometheus最常用的方式是通过pull去抓取Metrics。所以我们首先在服务通过<code class="prettyprint">/metrics</code>接口暴露指标，这样Promethues server就能通过http请求抓取到我们的业务指标。<br>
<br>接口示例：<br>
<pre class="prettyprint">server := gin.New()<br>
server.Use(middlewares.AccessLogger(), middlewares.Metric(), gin.Recovery())<br>
<br>
server.GET("/health", func(c *gin.Context) &#123;<br>
c.JSON(http.StatusOK, gin.H&#123;<br>
    "message": "ok",<br>
&#125;)<br>
&#125;)<br>
<br>
server.GET("/metrics", Monitor)<br>
<br>
func Monitor(c *gin.Context) &#123;<br>
h := promhttp.Handler()<br>
h.ServeHTTP(c.Writer, c.Request)<br>
&#125; <br>
</pre><br>
<h4>定义指标</h4>为了方便理解，这里选取了三种类型和两种业务场景的指标。<br>
<br>示例：<br>
<pre class="prettyprint">var (<br>
//HTTPReqDuration metric:http_request_duration_seconds<br>
HTTPReqDuration *prometheus.HistogramVec<br>
//HTTPReqTotal metric:http_request_total<br>
HTTPReqTotal *prometheus.CounterVec<br>
// TaskRunning metric:task_running<br>
TaskRunning *prometheus.GaugeVec<br>
)<br>
<br>
func init() &#123;<br>
// 监控接口请求耗时<br>
// 指标类型是Histogram<br>
HTTPReqDuration = prometheus.NewHistogramVec(prometheus.HistogramOpts&#123;<br>
    Name:    "http_request_duration_seconds",<br>
    Help:    "http request latencies in seconds",<br>
    Buckets: nil,<br>
&#125;, []string&#123;"method", "path"&#125;)<br>
// "method"、"path" 是 label<br>
<br>
// 监控接口请求次数<br>
// 指标类型是 Counter<br>
HTTPReqTotal = prometheus.NewCounterVec(prometheus.CounterOpts&#123;<br>
    Name: "http_requests_total",<br>
    Help: "total number of http requests",<br>
&#125;, []string&#123;"method", "path", "status"&#125;)<br>
// "method"、"path"、"status" 是 label<br>
<br>
// 监控当前在执行的task数量<br>
// 监控类型是Gauge<br>
TaskRunning = prometheus.NewGaugeVec(prometheus.GaugeOpts&#123;<br>
    Name: "task_running",<br>
    Help: "current count  of running task",<br>
&#125;, []string&#123;"type", "state"&#125;)<br>
// "type"、"state" 是 label<br>
<br>
prometheus.MustRegister(<br>
    HTTPReqDuration,<br>
    HTTPReqTotal,<br>
    TaskRunning,<br>
)<br>
&#125; <br>
</pre><br>
通过上述的代码我们就定义并且注册了我们的想要监控的指标。<br>
<h4>生成指标</h4>示例：<br>
<pre class="prettyprint">start := time.Now()<br>
c.Next()<br>
<br>
duration := float64(time.Since(start)) / float64(time.Second)<br>
<br>
path := c.Request.URL.Path<br>
<br>
// 请求数加1<br>
controllers.HTTPReqTotal.With(prometheus.Labels&#123;<br>
"method": c.Request.Method,<br>
"path":   path,<br>
"status": strconv.Itoa(c.Writer.Status()),<br>
&#125;).Inc()<br>
<br>
//  记录本次请求处理时间<br>
controllers.HTTPReqDuration.With(prometheus.Labels&#123;<br>
"method": c.Request.Method,<br>
"path":   path,<br>
&#125;).Observe(duration)<br>
<br>
// 模拟新建任务<br>
controllers.TaskRunning.With(prometheus.Labels&#123;<br>
"type":  shuffle([]string&#123;"video", "audio"&#125;),<br>
"state": shuffle([]string&#123;"process", "queue"&#125;),<br>
&#125;).Inc()<br>
<br>
// 模拟任务完成<br>
controllers.TaskRunning.With(prometheus.Labels&#123;<br>
"type":  shuffle([]string&#123;"video", "audio"&#125;),<br>
"state": shuffle([]string&#123;"process", "queue"&#125;),<br>
&#125;).Dec() <br>
</pre><br>
<h4>抓取指标</h4>Promethues抓取target配置：<br>
<pre class="prettyprint"># 抓取间隔<br>
scrape_interval: 5s<br>
<br>
# 目标<br>
scrape_configs:<br>
- job_name: 'prometheus'<br>
static_configs:<br>
  - targets: ['prometheus:9090']<br>
- job_name: 'local-service'<br>
metrics_path: /metrics<br>
static_configs:<br>
  - targets: ['host.docker.internal:8000']<br>
</pre><br>
在实际应用中静态配置target地址不太适用，在Kubernetes下Promethues通过与Kubernetes API集成目前主要支持5种服务发现模式，分别是：Node、Service、Pod、Endpoints、Ingress。<br>
<br>指标展示如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210926/f78c59b0d894065a903e37ea86fce2ae.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210926/f78c59b0d894065a903e37ea86fce2ae.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210926/b6e23014c32605ff87a5ee786f9aba31.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210926/b6e23014c32605ff87a5ee786f9aba31.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
原文链接：<a href="https://www.lxkaka.wang/app-metrics/" rel="nofollow" target="_blank">https://www.lxkaka.wang/app-metrics/</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            