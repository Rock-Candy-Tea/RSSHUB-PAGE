
---
title: '深入OpenTelemetry指标'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220918/a97dd6ea05c68b7cd23afd19aefce956.png'
author: Dockone
comments: false
date: 2022-09-23 15:12:11
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220918/a97dd6ea05c68b7cd23afd19aefce956.png'
---

<div>   
<br><blockquote><br>译注：在本文中，为理解的一致性，我们保留了OpenTelemetry的术语，不作翻译：包括但不限于Instrument、Measurement、Exemplar、Baggage、Context等。需要注意区分Measurement和Instrument的区别，前者指的是度量数据，而后者通常是指用于监测的代码和工具。</blockquote><a href="https://opentelemetry.io/">OpenTelemetry</a>是由<a href="https://www.cncf.io/">云原生计算基金会（CNCF）</a>托管的一个用于基础设施性能检测的开源可观测性框架。该项目在几乎所有主要的云供应商（AWS、Google、Microsoft）以及可观测性供应商（包括Timescale）的贡献下得到了极大的发展，以至于它成为<a href="https://all.devstats.cncf.io/d/1/activity-repository-groups?orgId=1">按活跃度和贡献者排名第二的CNCF项目</a>，仅次于Kubernetes本身。<br>
<br>OpenTelemetry旨在<a href="https://opentelemetry.io/docs/concepts/what-is-opentelemetry/">为所有类型的可观测数据定义一个单一的标准</a>（在OpenTelemetry的术语中被称作Signals信号），包括监控指标、日志和链路追踪。通过一系列的工具、库、API、SDK和exporters，OpenTelemetry从根本上简化了从服务中收集信号并将其发送到你所选用的后端服务的过程，为更多的用户和供应商打开了可观测性的大门。<br>
<br>在设计OpenTelemetry指标标准时，有三个<a href="https://opentelemetry.io/docs/reference/specification/metrics/">设计目标</a>被采纳：<br>
<ul><li>提供将监控指标与其他类型的可观察性数据相连接的能力：要么是通过<a href="https://opentelemetry.io/docs/reference/specification/metrics/datamodel/#exemplars">Exemplars</a>在链路追踪和监控指标之间直接连接，要么是通过<a href="https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/baggage/api.md">Baggage</a>和<a href="https://opentelemetry.io/docs/reference/specification/context/">Context</a>提供与日志和链路追踪享有相同的相关元数据，间接地连接。</li><li>允许从<a href="https://opencensus.io/">OpenCensus</a>标准轻松迁移到OpenTelemetry标准。</li><li>在可能的情况下提供对其他主要指标实现的全面支持。Prometheus和<a href="https://github.com/statsd/statsd">StatsD</a>是专门适配的，能够完全支持：那些迁移到OpenTelemetry的用户可以看到与使用其原生客户端类似的结果。</li></ul><br>
<br>OpenTelemetry提供了一个采集器，可以用来重新聚合和重定向指标数据，经常被用来创建信号管道。由于OpenTelemetry不提供后端实现（它关注的是创建、收集和发送信号），数据将流向另一个或多个系统进行存储并最终能够被查询。之所以OpenTelemetry有时会令人感到复杂，是因为它可以用来模拟许多不同的信号实现。在这篇博文中，我们将聚焦于”表面”，即开发者在OpenTelemetry中使用指标时可能遇到的要素。<br>
<br><h3>OpenTelemetry指标</h3>OpenTelemetry指标与<a href="https://www.timescale.com/blog/four-types-prometheus-metrics-to-collect/">Prometheus指标</a>略有不同，它允许在采集过程中进行更加灵活的转换，并支持许多导出类型，包括Pull和Push模式。由于这种灵活性，许多现有的指标系统都可以用OpenTelemetry建模，而不会损失语义或精确性，这使它成为互操作性的完美指标系统。<br>
<br>OpenTelemetry有三个模型：<br>
<ul><li>事件模型：在这个模型中，你作为一个开发者来创建指标，</li><li>流模型：OpenTelemetry使用该模型进行传输，</li><li>时间序列模型，OpenTelemetry将其用于存储。</li></ul><br>
<br>在这篇文章中讨论的指标都是事件模型的一部分，而转换则是从事件模型到流模型的转换的一部分。(作为一个开发者，你其实不需要担心这些模型，但有一个基本的了解会更有帮助）。<br>
<br>OpenTelemetry SDK允许我们：<br>
<ul><li>通过时间上的聚合（改变分辨率）减少传输的指标数量，</li><li>通过空间聚合减少传输的指标数量（去除不需要的属性），</li><li>从累积表示法（Prometheus使用的）改为差值表示法（表达数值之间的变化，而不是绝对测量值）。</li></ul><br>
<br>OpenTelemetry指标的工作方式是使用全局的<a href="https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#meterprovider">MeterProvider</a>来创建一个<a href="https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#meter">Meter</a>，并将其与一个或多个<a href="https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#instrument">Instrument</a>相关联，每一个Instrument都被用来创建一系列的<a href="https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#measurement">Measurements</a>。这些测量值在<a href="https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/sdk.md#view">View</a>中被汇总为一个指标。然后通过<a href="https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/sdk.md#metricreader">Metric Reader</a>和<a href="https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/sdk.md#metricexporter">Metric Exporter</a>的组合来观察和导出指标（可以是拉或推）。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220918/a97dd6ea05c68b7cd23afd19aefce956.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220918/a97dd6ea05c68b7cd23afd19aefce956.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图示说明OpenTelemetry中MeterProvider的要素</em><br>
<br>Instrument或Measurements是我们在应用中创建或观察到的东西，而指标则表达了我们与可观测性数据的消费者分享的该监测的当前聚合值。<br>
<br>OpenTelemetry允许以多种方式将属性（标签）附加到指标上。最常见的有：<br>
<ul><li>来自任何附加的资源，它可能持有定义主机的标签。例如，一个Kubernetes Pod或一个虚拟机</li><li>来自当前的上下文，它将被附加到所有同步的Instrument上</li><li>Measurement本身所具备的</li></ul><br>
<br><h3>从Measurements到Metrics</h3>Measurements的创建非常快，尤其是在同步的情况下，但这可能会迅速压垮一个指标管道。为了解决这个问题，Prometheus使用了一个带有抓取间隔的Pull机制，而OpenTelemetry通过给每个Instrument附加一个Aggregation View来解决收集路径中的问题，然后将数据传递给观察它们的MetricReader和输出它们的MetricExporter：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220918/f5131cce7507535c9845d276e7b6b6a4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220918/f5131cce7507535c9845d276e7b6b6a4.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>从测量到指标：OpenTelemetry中指标的收集路径图</em><br>
<br>MetricReader负责在Instrument没有View的情况下附加默认的View，也负责定义MetricExporters，然后向其发送这些观测值。MetricReader还将改变指标的时间性，从默认的Cumulative（新值累加到最后一个值上，这与我们在Prometheus中看到的相同）改为Delta（度量值是新旧值之差）。<br>
<br>每个Instrument都与一个MetricReader相关联，如果没有为一个Instrument定义其他View，它就负责附加默认View。此外，它还定义了时间性：可能从默认的Cumulative（当前值加到以前的值，如Prometheus中使用的）切换到Delta（报告当前观测值和最后观测值之间的差异，减少计算速率时客户端的开销）。<br>
<br>MetricReader和MetricExporter的组合决定了数据如何被发送到下游。一个非常流行的方法是使用PeriodicExportingMetricReader和OTLPMetricExporter，每隔一段时间（默认为60秒）对指标进行采样，并将其发送到OpenTelemetry采集器（它将使用另一个Exporter）进行进一步处理。许多其他的导出器可用于各种语言。<br>
<br>一些流行的导出器有：<br>
<ul><li><strong><a href="https://opentelemetry.io/docs/instrumentation/js/exporters/#prometheus">Prometheus Metric Exporter</a></strong>：一个基于Pull模式的导出器，Prometheus客户端可以抓取它的端点</li><li><strong>Prometheus Remote Write Exporter</strong>：一个基于Push模式的导出器，通过Prometheus远程写入协议发送数据</li><li><strong><a href="https://opentelemetry.io/docs/instrumentation/js/exporters/#otlp-endpoint-or-collector">OTLPMetricExporter</a></strong>：它可以向任何理解OpenTelemetry协议的设备推送指标</li><li><strong><a href="https://opentelemetry.io/docs/instrumentation/go/getting-started/#creating-a-console-exporter">ConsoleMetricExporter</a></strong>：它被用来向控制台输出调试信息</li></ul><br>
<br>在Python中，初始化OpenTelemetry指标并附加一个默认的MetricReader和MetricExporter（发送指标到本地OpenTelemetry采集器），代码看起来像这样：<br>
<pre class="prettyprint">from opentelemetry._metrics import get_meter_provider, set_meter_provider<br>
from opentelemetry.exporter.otlp.proto.grpc._metric_exporter import (<br>
OTLPMetricExporter,<br>
)<br>
from opentelemetry.sdk._metrics import MeterProvider<br>
from opentelemetry.sdk._metrics.export import PeriodicExportingMetricReader<br>
<br>
exporter = OTLPMetricExporter(insecure=True)<br>
reader = PeriodicExportingMetricReader(exporter)<br>
provider = MeterProvider(metric_readers=[reader])<br>
set_meter_provider(provider) <br>
</pre><br>
<h3>监测并发送Measurements</h3>OpenTelemetry提供了六种类型的Instruments，我们可以用它们来捕获测量结果。它们可以被分为两大类：同步和异步。每个Instrument都可以发送测量值，每个Instrument都可以与属性相关联。同步Instrument以类似于Prometheus指标的方式在应用程序代码中实现，通过在应用程序中插入代码，每次执行时都会更新一个值。它们可以与当前的Context上下文相关联（这有助于描述当前的应用状态）。<br>
<br>异步Instrument则会注册一个回调函数，只在观察时发送数值。例如，可以注册一个异步Instrument，每10秒报告一个传感器的值。这些Instrument不能与当前的Context相关联，因为它们位于主程序的外部，而不是在主程序运行时被调用，它们根据观察者的要求观察信号数据。在某些方面，它们类似于Prometheus通过Exporter对一个未被检测的应用程序进行监控。<br>
<br>所有Instrument的创建都有一个名称、一个描述和一个测量单位（必须遵循<a href="https://opentelemetry.io/docs/reference/specification/metrics/api/#instrument-unit">Instrument单位规则</a>）。异步Instrument还指定了回调函数，该函数被调用以观察测量结果。开发人员可以使用的OpenTelemetry Instrument类型，如下表所示。(令人困惑的是，语言呈现给用户的建议名称与测量名称不一样，用Observable来代替Asynchronous。即observable_counter）。<br>
<br>下表概述了OpenTelemetry中Instrument类型的名称和特点。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220918/18fd662d992f82261eaea4d7c1ed1b7a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220918/18fd662d992f82261eaea4d7c1ed1b7a.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
现在，让我们来讲一下每一种Instrument类型。<br>
<br><h4>Counter / Asynchronous Counter</h4>> Counter可译为”计数器”，则Asynchronous Counter译为”异步计数器”<br>
<br>Counter是一个同步Instrument，它总是在增加，即它是单调的，只接受非负的值。不出所料，它与Prometheus的Counter是相同的。Counter通过接收增量或Delta差值来工作。<br>
<br>当使用计数器时，语言SDK中会有一个<strong>add</strong>的操作，必须提供一个非负数来增加计数器的值。同时可以附加一组可选的属性。这些属性类似于Prometheus的标签。<br>
<br>异步计数器的不同之处在于通过回调而不是<strong>add</strong>函数来操作。当观察Instrument时，回调函数会被执行，并将传回一个或多个测量值，表示为绝对值（不是delta值）。一旦这些值被传递，它们将在内部通过计算得到delta值。<br>
<br>例如，你可以实现一个异步计数器，报告应用程序自启动以来所消耗的CPU时间。这一信息将在回调中从操作系统中提取并返回。可以一次性返回几个值，比如每个CPU或线程都有一个值。这些测量值总是被期望能够通过一种有意义的方式进行跨属性求和（在这种情况下，我们可以得到系统使用的总CPU时间）。<br>
<br>请注意，由于Python SDK还不稳定，我们需要导入_metrics，而不是本文代码示例的metrics。未来可能还会有一些破坏性的变更。随着项目的进展，我们会保持更新。目前的例子是用OpenTelemetry Python SDK v1.11.1编写的。<br>
<br>在Python中，创建和使用计数器和异步计数器的例子看起来是这样的：<br>
<pre class="prettyprint">from opentelemetry._metrics import get_meter_provider<br>
from opentelemetry._metrics.observation import Observation<br>
<br>
meter = get_meter_provider().get_meter("otel-demo")<br>
<br>
# Counter<br>
counter = meter.create_counter("counter")<br>
<br>
# This adds 100 to the total (a delta value)<br>
counter.add(100,&#123;"app": "timescale"&#125;)<br>
<br>
# Callback function for Async counter<br>
def observable_counter_func() -> [Observation]:<br>
# This reports that the current value is 10, which will be<br>
# converted to a delta internally<br>
return [Observation(10, &#123;"app": "timescale"&#125;]<br>
<br>
# Async Counter<br>
observable_counter = meter.create_observable_counter(<br>
"observable_counter", [observable_counter_func]<br>
)<br>
</pre><br>
<h4>UpDownCounter / Asynchronous UpDownCounter</h4>UpDownCounter是一个类似于Counter的同步Instrument，但它允许传递负的delta值（它可以不是单调的）。Counter适合表示已经提交的作业数量，而UpDownCounter则适合表示当前正在处理的作业数量（它可以向上和向下移动）。需要注意的是，这与Prometheus中的Gauge的用法不一样，因为我们记录的是变化，而不是绝对值。<br>
<br>一个UpDownCounter提供了一个<strong>add</strong>操作，与Counter操作相同：与之相反的是它接受负的数据值。由属性数据关联的值被期望是可以求和的。<br>
<br>不出所料，异步UpDownCounter提供了一个回调接口，返回一个或多个测量值，将每个测量值表达为一个绝对值，该值将在内部被计算为delta值。<br>
<br>OpenTelemetry规范指出，当被返回的值很容易被观察到时，不应该使用同步的UpDownCounter。在这种情况下，应该使用一个异步UpDownCounter来代替。<br>
<br>在Python中，创建和使用UpDownCounter和Asynchronous UpDownCounter的例子看起来是这样的：<br>
<pre class="prettyprint">from opentelemetry._metrics import get_meter_provider<br>
from opentelemetry._metrics.observation import Observation<br>
<br>
meter = get_meter_provider().get_meter("otel-demo")<br>
<br>
# UpDownCounter<br>
up_down_counter = meter.create_up_down_counter("up_down_counter")<br>
<br>
# This adds 100, then removes 10 from the total (both delta values)<br>
up_down_counter.add(100,&#123;"app": "timescale"&#125;)<br>
up_down_counter.add(-10,&#123;"app": "timescale"&#125;)<br>
<br>
# Callback function for Async counter<br>
def observable_up_down_counter_func() -> [Observation]:<br>
# This reports that the current value is 10, which will be<br>
# converted to a delta internally<br>
return [Observation(10, &#123;"app": "timescale"&#125;)]<br>
<br>
# Async UpDownCounter, note the observable prefix<br>
observable_up_down_counter = meter.create_observable_up_down_counter(<br>
"observable_up_down_counter", [observable_up_down_counter_func]<br>
) <br>
</pre><br>
<h4>Histogram</h4>> Histogram可译为直方图<br>
<br>Histogram是一种同步Instrument，它允许记录在统计上相互关联的多个数值。当你不想孤立地分析数据点，而是想通过跟踪落在每个预定义桶中的值的数量以及最小值和最大值（如果有进行配置）来生成关于其分布的统计信息时，你会选择Histogram。<br>
<br>直方图只有一个单一的方法被暴露出来：<strong>record</strong>。记录需要一个非负的观察值，并可以附加一组可选的属性。<br>
<br>当你查看HTTP响应时间时，你可能会选择直方图：知道每个请求发生时的确切响应时间可能并不那么有用（而且更适合链路追踪数据，它将暴露每个请求的开始和结束时间），但从服务层面来看，能够报告中位响应时间和超过95分位数的HTTP请求数量可能更有意思。<br>
<br>需要注意的是，记录测量结果并不能创建Histogram；默认的Aggregation（Explicit Bucket Histogram Aggregation）可以。当使用Histogram Instrument时，重要的是确保桶也被配置了。默认值是[ 0, 5, 10, 25, 50, 75, 100, 250, 500, 1000 ]，而这并不总是理想的。你可以在下面几段看到一些创建View的例子。<br>
<br>在Python中，一个创建和使用直方图的例子是这样的：<br>
<pre class="prettyprint">from opentelemetry._metrics import get_meter_provider<br>
from opentelemetry._metrics.observation import Observation<br>
<br>
meter = get_meter_provider().get_meter("otel-demo")<br>
<br>
# Histogram<br>
histogram = meter.create_histogram("histogram")<br>
<br>
# This records a value of 100<br>
histogram.record(100,&#123;"app": "timescale"&#125;) <br>
</pre><br>
<br><h4>Asynchronous Gauge</h4>异步Gauge在OpenTelemetry API中的独特之处在于两个方面：它没有同步的实现，并且被设计用来表示那些相加没有意义的值，即使它们共享属性数据。这方面的一个例子是一个房子的各个房间的温度。这是常见的数据，但是把它作为一个总值来报告没有任何意义--你可能像求一个平均值或最大值，但绝不是一个总和。这是与Prometheus不同的方法，Prometheus将这些类型的要求编码到指标的命名规则中。在OpenTelemetry中，如果你使用一个Asynchronous Gauge，你不能像使用其他指标类型那样对其进行汇总。<br>
<br>与所有的异步Instrument一样，在创建异步Instrument时，需要传递一个回调，它可以返回一个或多个（在这种情况下是完全离散的）测量值。<br>
<br>在Python中，创建和使用Asynchronous Gauge的例子是这样的：<br>
<pre class="prettyprint">from opentelemetry._metrics import get_meter_provider<br>
from opentelemetry._metrics.observation import Observation<br>
<br>
meter = get_meter_provider().get_meter("otel-demo")<br>
<br>
# Callback function for Async gauge<br>
def observable_gauge_func() -> [Observation]:<br>
# This reports that the current value is 10<br>
return [Observation(10, &#123;"app": "timescale"&#125;)]<br>
<br>
# Async Gauge, note the observable prefix<br>
observable_gauge = meter.create_observable_gauge(<br>
"observable_gauge", [observable_gauge_func]<br>
) <br>
</pre><br>
<br><h3>Views和Aggregations</h3>OpenTelemetry中的View定义了一个Aggregation操作，它接受一系列的Measurements，并在该时间点上将其表达为一个单一的指标值。随着更多的Measurements被创建，指标的值会被持续更新。如果没有为一个Instrument创建View，那么就会根据Instrument类型选择一个默认的Aggregation。自定义View可以通过Meter名称、Instrument名称、Instrument类型或通配符来定位。<br>
<br>在OpenTelemetry中，有三种Aggregation类型：<br>
<ul><li><strong>Sum Aggregation</strong>：简单地跟踪传入的测量值的总和（尊重输入Instrument的单调性），</li><li><strong>Last Value Aggregation</strong>：跟踪最后报告的值，</li><li><strong>Explicit Bucket Histogram Aggregation</strong>：跟踪属于每个预定义桶（必须在创建View时预定义）的测量数量，并可以跟踪最小和最大值。</li></ul><br>
<br>下表定义了每种OpenTelemetry Instrument类型的默认Aggregation：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220918/77227cf9f70ead8264a621ec495ebefb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220918/77227cf9f70ead8264a621ec495ebefb.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这段Python代码使用ConsoleMetricExporter写入控制台，也改变了所有柱状图Instrument的桶状结构：<br>
<pre class="prettyprint">from opentelemetry._metrics import get_meter_provider, set_meter_provider<br>
from opentelemetry.sdk._metrics import MeterProvider<br>
from opentelemetry.sdk._metrics.export import PeriodicExportingMetricReader<br>
from opentelemetry.sdk._metrics.export import ConsoleMetricExporter<br>
from opentelemetry.sdk._metrics.aggregation import ExplicitBucketHistogramAggregation<br>
<br>
exporter = ConsoleMetricExporter()<br>
reader = PeriodicExportingMetricReader(exporter)<br>
provider = MeterProvider(<br>
metric_readers=[reader],<br>
views=[View(<br>
    instrument_name="*”,<br>
    aggregation=ExplicitBucketHistogramAggregation(<br>
        (1,20,50,100,1000)<br>
))],<br>
)<br>
set_meter_provider(provider) <br>
</pre><br>
<h3>总结</h3>在指标系列博文的第二部分，我们讨论了OpenTelemetry标准，重点是它的六种Instrument类型：counters、asynchronous counters、UpDownCounters、asynchronous UpDownCounters、histograms和asynchronous gauges。<br>
<br>在该系列的最后一篇博文中，我们将介绍该模型与Prometheus的比较，解释其中的差异，并分享我们关于选型的建议。<br>
<br><strong>原文链接：<a href="https://www.timescale.com/blog/a-deep-dive-into-open-telemetry-metrics/">A Deep Dive Into OpenTelemetry Metrics</a>（翻译：小灰灰）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            