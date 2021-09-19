
---
title: 'Flink链路延迟测量的LatencyMarker机制实现'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/195230-fb89a3a58bd59c40.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/195230-fb89a3a58bd59c40.png'
---

<div>   
<h3>前言</h3>
<p>今天本应放一首适合高考气氛的歌的，但是既然受疫情影响推迟了，还是老老实实写点技术相关的吧。</p>
<p>对于实时的流式处理系统来说，我们需要关注数据输入、计算和输出的及时性，所以处理延迟是一个比较重要的监控指标，特别是在数据量大或者软硬件条件不佳的环境下。Flink早在<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-3660" target="_blank">FLINK-3660</a>就为用户提供了开箱即用的链路延迟测量功能，只需要配置好<code>metrics.latency.interval</code>参数，再观察<code>TaskManagerJobMetricGroup/operator_id/operator_subtask_index/latency</code>这个metric即可。本文简单walk一下源码，看看它是如何实现的，并且简要说明注意事项。</p>
<h3>LatencyMarker的产生</h3>
<p>与通过水印来标记事件时间的推进进度相似，Flink也用一种特殊的流元素（StreamElement）作为延迟的标记，称为LatencyMarker。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="518" data-height="397"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-fb89a3a58bd59c40.png" data-original-width="518" data-original-height="397" data-original-format="image/png" data-original-filesize="36428" src="https://upload-images.jianshu.io/upload_images/195230-fb89a3a58bd59c40.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>LatencyMarker的数据结构甚简单，只有3个field，即它被创建时携带的时间戳、算子ID和算子并发实例（sub-task）的ID。</p>
<pre><code class="java">private final long markedTime;
private final OperatorID operatorId;
private final int subtaskIndex;
</code></pre>
<p>LatencyMarker和水印不同，不需要通过用户抽取产生，而是在Source端自动按照<code>metrics.latency.interval</code>参数指定的周期生成。StreamSource专门实现了一个内部类LatencyMarksEmitter用来发射LatencyMarker，而它又借用了负责协调处理时间的服务ProcessingTimeService（之前的文章已经多次提到过），如下代码所示。</p>
<pre><code class="java">LatencyMarksEmitter<OUT> latencyEmitter = null;
if (latencyTrackingInterval > 0) &#123;
    latencyEmitter = new LatencyMarksEmitter<>(
        getProcessingTimeService(),
        collector,
        latencyTrackingInterval,
        this.getOperatorID(),
        getRuntimeContext().getIndexOfThisSubtask());
&#125;

private static class LatencyMarksEmitter<OUT> &#123;
    private final ScheduledFuture<?> latencyMarkTimer;

    public LatencyMarksEmitter(
            final ProcessingTimeService processingTimeService,
            final Output<StreamRecord<OUT>> output,
            long latencyTrackingInterval,
            final OperatorID operatorId,
            final int subtaskIndex) &#123;
        latencyMarkTimer = processingTimeService.scheduleAtFixedRate(
            new ProcessingTimeCallback() &#123;
                @Override
                public void onProcessingTime(long timestamp) throws Exception &#123;
                    try &#123;
                        // ProcessingTimeService callbacks are executed under the checkpointing lock
                        output.emitLatencyMarker(new LatencyMarker(processingTimeService.getCurrentProcessingTime(), operatorId, subtaskIndex));
                    &#125; catch (Throwable t) &#123;
                        // we catch the Throwables here so that we don't trigger the processing
                        // timer services async exception handler
                        LOG.warn("Error while emitting latency marker.", t);
                    &#125;
                &#125;
            &#125;,
            0L,
            latencyTrackingInterval);
    &#125;

    public void close() &#123;
        latencyMarkTimer.cancel(true);
    &#125;
&#125;
</code></pre>
<p>通过调用Output.emitLatencyMarker()方法，LatencyMarker就会随着数据流一起传递到下游了。</p>
<h3>LatencyMarker的粒度</h3>
<p>AbstractStreamOperator是所有Flink Streaming算子的基类，在它的初始化方法setup()中，会先创建用于延迟统计的LatencyStats实例。</p>
<pre><code class="java">final String configuredGranularity = taskManagerConfig.getString(MetricOptions.LATENCY_SOURCE_GRANULARITY);
LatencyStats.Granularity granularity;
try &#123;
    granularity = LatencyStats.Granularity.valueOf(configuredGranularity.toUpperCase(Locale.ROOT));
&#125; catch (IllegalArgumentException iae) &#123;
    granularity = LatencyStats.Granularity.OPERATOR;
    LOG.warn(
        "Configured value &#123;&#125; option for &#123;&#125; is invalid. Defaulting to &#123;&#125;.",
        configuredGranularity,
        MetricOptions.LATENCY_SOURCE_GRANULARITY.key(),
        granularity);
&#125;
TaskManagerJobMetricGroup jobMetricGroup = this.metrics.parent().parent();
this.latencyStats = new LatencyStats(jobMetricGroup.addGroup("latency"),
    historySize,
    container.getIndexInSubtaskGroup(),
    getOperatorID(),
    granularity);
</code></pre>
<p>在创建LatencyStats之前，先要根据<code>metrics.latency.granularity</code>配置项来确定延迟监控的粒度，分为以下3档：</p>
<ul>
<li>single：每个算子单独统计延迟；</li>
<li>operator（默认值）：每个下游算子都统计自己与Source算子之间的延迟；</li>
<li>subtask：每个下游算子的sub-task都统计自己与Source算子的sub-task之间的延迟。</li>
</ul>
<p><strong>一般情况下采用默认的operator粒度即可，这样在Sink端观察到的latency metric就是我们最想要的全链路（端到端）延迟</strong>，以下也是以该粒度讲解。subtask粒度太细，会增大所有并行度的负担，不建议使用。</p>
<h3>LatencyMarker的流转与计量</h3>
<p>AbstractStreamOperator分别提供了用于单输入流算子OneInputStreamOperator、双输入流算子TwoInputStreamOperator的LatencyMarker处理方法。</p>
<pre><code class="java">// ------- One input stream
public void processLatencyMarker(LatencyMarker latencyMarker) throws Exception &#123;
    reportOrForwardLatencyMarker(latencyMarker);
&#125;

// ------- Two input stream
public void processLatencyMarker1(LatencyMarker latencyMarker) throws Exception &#123;
    reportOrForwardLatencyMarker(latencyMarker);
&#125;

public void processLatencyMarker2(LatencyMarker latencyMarker) throws Exception &#123;
    reportOrForwardLatencyMarker(latencyMarker);
&#125;

protected void reportOrForwardLatencyMarker(LatencyMarker marker) &#123;
    // all operators are tracking latencies
    this.latencyStats.reportLatency(marker);
    // everything except sinks forwards latency markers
    this.output.emitLatencyMarker(marker);
&#125;
</code></pre>
<p>这些方法都会做两件事，一是计算延时并报告给LatencyStats，二是继续将LatencyMarker发射到下游。不妨来看看RecordWriterOutput.emitLatencyMarker()方法的具体实现。</p>
<pre><code class="java">@Override
public void emitLatencyMarker(LatencyMarker latencyMarker) &#123;
    serializationDelegate.setInstance(latencyMarker);
    try &#123;
        recordWriter.randomEmit(serializationDelegate);
    &#125;
    catch (Exception e) &#123;
        throw new RuntimeException(e.getMessage(), e);
    &#125;
&#125;

/**
 * This is used to send LatencyMarks to a random target channel.
 */
public void randomEmit(T record) throws IOException, InterruptedException &#123;
    emit(record, rng.nextInt(numberOfChannels));
&#125;
</code></pre>
<p>可见是从该算子所有的输出channel中随机选择一条来发射LatencyMarker，这样在度量算子级别延迟的基础上不会造成LatencyMarker泛滥，同时也不会受到并行度调整（重新分区）的影响。</p>
<p>注意StreamSink的reportOrForwardLatencyMarker()方法不会再发射LatencyMarker（因为已经处理完了），只会更新延迟。</p>
<pre><code class="java">@Override
protected void reportOrForwardLatencyMarker(LatencyMarker marker) &#123;
    // all operators are tracking latencies
    this.latencyStats.reportLatency(marker);
    // sinks don't forward latency markers
&#125;
</code></pre>
<p>LatencyStats中的延迟最终会转化为直方图表示，通过直方图就可以统计出延时的最大值、最小值、均值、分位值（quantile）等指标。以下是reportLatency()方法的源码。</p>
<pre><code class="java">public void reportLatency(LatencyMarker marker) &#123;
    final String uniqueName = granularity.createUniqueHistogramName(marker, operatorId, subtaskIndex);
    DescriptiveStatisticsHistogram latencyHistogram = this.latencyStats.get(uniqueName);
    if (latencyHistogram == null) &#123;
        latencyHistogram = new DescriptiveStatisticsHistogram(this.historySize);
        this.latencyStats.put(uniqueName, latencyHistogram);
        granularity.createSourceMetricGroups(metricGroup, marker, operatorId, subtaskIndex)
            .addGroup("operator_id", String.valueOf(operatorId))
            .addGroup("operator_subtask_index", String.valueOf(subtaskIndex))
            .histogram("latency", latencyHistogram);
    &#125;
    long now = System.currentTimeMillis();
    latencyHistogram.update(now - marker.getMarkedTime());
&#125;
</code></pre>
<p>可见，延迟是由当前时间戳减去LatencyMarker携带的时间戳得到的，所以在Sink端统计到的就是全链路延迟了。</p>
<h3>注意事项</h3>
<p>由以上分析可知，<strong>LatencyMarker是不会像Watermark一样参与到数据流的用户逻辑中的，而是直接被各算子转发并统计</strong>。这如何能得到真正的延时呢？如果由于网络不畅、数据流量太大等原因造成了反压（back pressure，之后再提），那么LatencyMarker的流转就会被阻碍，传递到下游的时间差就会增加，所以还是能够近似估算出整体的延时的。为了让它尽量精确，有两点特别需要注意：</p>
<ul>
<li>ProcessingTimeService产生时间戳最终是靠<code>System.currentTimeMillis()</code>方法，所以必须保证Flink集群内所有节点的时区、时间是同步的，可以用ntp等工具来配置。</li>
<li>
<code>metrics.latency.interval</code>的时间间隔宜大不宜小，在我们的实践中一般配置成30000（30秒）左右。一是因为延迟监控的频率可以不用太频繁，二是因为LatencyMarker的处理也要消耗时间，只有在LatencyMarker的耗时远小于正常StreamRecord的耗时时，metric反映出的数据才贴近实际情况，所以LatencyMarker的密度不能太大。</li>
</ul>
<h3>The End</h3>
<p>待会该买菜做饭了，就这样吧。</p>
<p>民那周末愉快（不是</p>
  
</div>
            