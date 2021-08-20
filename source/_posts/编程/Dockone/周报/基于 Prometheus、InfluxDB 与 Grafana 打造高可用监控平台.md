
---
title: '基于 Prometheus、InfluxDB 与 Grafana 打造高可用监控平台'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/c2dfc2687534979d52e6de955c1cf51e.png'
author: Dockone
comments: false
date: 2021-08-20 08:08:38
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/c2dfc2687534979d52e6de955c1cf51e.png'
---

<div>   
<br>在本文中，我将把几个常用的监控部分给梳理一下。前面我们提到过，在性能监控图谱中，有操作系统、应用服务器、中间件、队列、缓存、数据库、网络、前端、负载均衡、Web 服务器、存储、代码等很多需要监控的点。显然这些监控点不能在一个专栏中全部覆盖并一一细化，我只能找最常用的几个，做些逻辑思路的说明，同时也把具体的实现描述出来。如果你遇到了其他的组件，也需要一一实现这些监控。<br>
<br>在本篇中，主要想说明白下图的这个监控逻辑。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/c2dfc2687534979d52e6de955c1cf51e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/c2dfc2687534979d52e6de955c1cf51e.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这应该是现在最流行的一套监控逻辑了吧。我今天把常见的使用 Grafana、Prometheus、InfluxDB、Exporters 的数据展示方式说一下，如果你刚进入性能测试领域，也能有一个感性的认识。<br>
<br>有测试工具，有监控工具，才能做后续的性能分析和瓶颈定位，所以有必要把这些工具的逻辑跟你摆一摆。<br>
<br>所有做性能的人都应该知道一点，不管数据以什么样的形式展示，最要紧的还是看数据的来源和含义，以便做出正确的判断。<br>
<br>我先说明一下 JMeter 和 node_exporter 到 Grafana 的数据展示逻辑。至于其他的 Exporter，我就不再解释这个逻辑了，只说监控分析的部分。<br>
<h3>JMeter + InfluxDB + Grafana 的数据展示逻辑</h3>一般情况下，我们用 JMeter 做压力测试时，都是使用 JMeter 的控制台来查看结果。如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/ca43a3b3c3d1af83730d3f35182caec5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/ca43a3b3c3d1af83730d3f35182caec5.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
或者装个插件来看结果：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/7b221e643ac68405fa3c128474a73ba4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/7b221e643ac68405fa3c128474a73ba4.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
或者用 JMeter 来生成 HTML：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/348d21f3b2a4087df74639723b5d8b81.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/348d21f3b2a4087df74639723b5d8b81.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这样看都没有问题，我们在前面也强调过，对于压力工具来说，我们最多只关心三条曲线的数据：TPS（T 由测试目标定义）、响应时间、错误率。这里的错误率还只是辅助排查问题的曲线，没有问题时，只看 TPS 和响应时间即可。<br>
<br>不过采取以上三种方式有几个方面的问题。<br>
<ol><li>整理结果时比较浪费时间。</li><li>在 GUI 用插件看曲线，做高并发时并不现实。</li><li>在场景运行时间比较长的时候，采用生成 HTML 的方式，会出现消耗内存过大的情况，而实际上，在生成的结果图中，有很多生成的图我们并不是那么关注。</li><li>生成的结果保存之后再查看比较麻烦，还要一个个去找。</li></ol><br>
<br>那么如何解决这几个问题呢？<br>
<br>用 JMeter 的 Backend Listener 帮我们实时发送数据到 InfluxDB 或 Graphite 可以解决这样的问题。<br>
<br>Graphite Backend Listener 的支持是在 JMeter 2.13 版本，InfluxdDB Backend Listener 的支持是在 JMeter 3.3 的版本，它们都是用异步的方式把数据发送出来，以便查看。<br>
<br>其实有这个 JMeter 发送给 InfluxDB 的数据之后，我们不需要看上面的那些 HTML 数据，也可以直观地看到系统性能的性能趋势。<br>
<br>并且这样保存下来的数据，在测试结束后想再次查看也比较方便比对。<br>
<br>JMeter + InfluxDB + Grafana 的结构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/2e0d2a6bd287f06a4423e6fc407cb19e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/2e0d2a6bd287f06a4423e6fc407cb19e.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在这个结构中，JMeter 发送压力到服务器的同时，统计下 TPS、响应时间、线程数、错误率等信息。默认每 30 秒在控制台输出一次结果（在 jmeter.properties 中有一个参数 #summariser.interval=30 可以控制）。<br>
<br>配置了 Backend Listener 之后，将统计出的结果异步发送到 InfluxDB 中。最后在 Grafana 中配置 InfluxDB 数据源和 JMeter 显示模板。<br>
<br>然后就可以实时查看 JMeter 的测试结果了，这里看到的数据和控制台的数据是一样。<br>
<br>但如果这么简单就说完了，这篇文章也就没价值了。下面我们来说一下，数据的传输和展示逻辑。<br>
<h3>JMeter 中 Backend Listener 的配置</h3>下面我们就 InfluxDB 的 Backend Listener 做个说明。它的配置比较简单，在脚本中加上即可。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/c859e72d8c865bae46eb9e24f74fe4c6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/c859e72d8c865bae46eb9e24f74fe4c6.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们先配置好 InfluxDB URL、Application 等信息，Application 这个配置可以看成是场景名。<br>
<br>那么 JMeter 如何将数据发给 InfluxDB 呢？请看源码中的关键代码，如下所示：<br>
<pre class="prettyprint">private void addMetrics(String transaction, SamplerMetric metric) &#123;<br>
    // FOR ALL STATUS<br>
    addMetric(transaction, metric.getTotal(), metric.getSentBytes(), metric.getReceivedBytes(), TAG_ALL, metric.getAllMean(), metric.getAllMinTime(),<br>
            metric.getAllMaxTime(), allPercentiles.values(), metric::getAllPercentile);<br>
    // FOR OK STATUS<br>
    addMetric(transaction, metric.getSuccesses(), null, null, TAG_OK, metric.getOkMean(), metric.getOkMinTime(),<br>
            metric.getOkMaxTime(), okPercentiles.values(), metric::getOkPercentile);<br>
    // FOR KO STATUS<br>
    addMetric(transaction, metric.getFailures(), null, null, TAG_KO, metric.getKoMean(), metric.getKoMinTime(),<br>
            metric.getKoMaxTime(), koPercentiles.values(), metric::getKoPercentile);<br>
​<br>
​<br>
    metric.getErrors().forEach((error, count) -> addErrorMetric(transaction, error.getResponseCode(),<br>
                error.getResponseMessage(), count));<br>
&#125; <br>
</pre><br>
从这段代码可以看出，站在全局统计的视角来看，这里把 JMeter 运行的统计结果，比如事务的 Total 请求、发送接收字节、平均值、最大值、最小值等，都加到 metric 中，同时也会把成功和失败的事务信息添加到 metric 中去。<br>
<br>在源码中，还有更多的添加 metric 的步骤，你有兴趣的话，也可以看一下 JMeter 源码中的InfluxdbBackendListenerClient.java。<br>
<br>保存了 metric 之后，再使用 InfluxdbMetricsSender 发送到 InfluxDB 中去。发送关键代码如下：<br>
<pre class="prettyprint">@Override public void writeAndSendMetrics() &#123;<br>
........ if (!copyMetrics.isEmpty()) &#123; try &#123; if(httpRequest == null) &#123;<br>
                httpRequest = createRequest(url);<br>
            &#125;<br>
            StringBuilder sb = new StringBuilder(copyMetrics.size()*35); for (MetricTuple metric : copyMetrics) &#123; // Add TimeStamp in nanosecond from epoch ( default in InfluxDB )<br>
sb.append(metric.measurement)<br>
                    .append(metric.tag)<br>
                    .append(" ") //$NON-NLS-1$<br>
.append(metric.field)<br>
                    .append(" ")<br>
                    .append(metric.timestamp+"000000") <br>
                    .append("\n"); //$NON-NLS-1$<br>
&#125;<br>
<br>
<br>
            StringEntity entity = new StringEntity(sb.toString(), StandardCharsets.UTF_8);<br>
<br>
            httpRequest.setEntity(entity);<br>
            lastRequest = httpClient.execute(httpRequest, new FutureCallback<HttpResponse>() &#123;<br>
                @Override public void completed(final HttpResponse response) &#123; int code = response.getStatusLine().getStatusCode(); /* * HTTP response summary 2xx: If your write request received<br>
                     * HTTP 204 No Content, it was a success! 4xx: InfluxDB<br>
                     * could not understand the request. 5xx: The system is<br>
                     * overloaded or significantly impaired. */<br>
                    if (MetricUtils.isSuccessCode(code)) &#123; if(log.isDebugEnabled()) &#123;<br>
                            log.debug("Success, number of metrics written: &#123;&#125;", copyMetrics.size());<br>
                        &#125; <br>
                    &#125; else &#123;<br>
                        log.error("Error writing metrics to influxDB Url: &#123;&#125;, responseCode: &#123;&#125;, responseBody: &#123;&#125;", url, code, getBody(response));<br>
                    &#125;<br>
                &#125;<br>
                @Override public void failed(final Exception ex) &#123;<br>
                    log.error("failed to send data to influxDB server : &#123;&#125;", ex.getMessage());<br>
                &#125;<br>
                @Override public void cancelled() &#123;<br>
                    log.warn("Request to influxDB server was cancelled");<br>
                &#125;<br>
            &#125;);               <br>
........<br>
        &#125;<br>
    &#125;<br>
&#125; <br>
</pre><br>
通过 writeAndSendMetrics，就将所有保存的 metrics 都发给了 InfluxDB。<br>
<h3>InfluxDB 中的存储结构</h3>然后我们再来看下 InfluxDB 中如何存储：<br>
<pre class="prettyprint">> show databases  <br>
name: databases  <br>
name  <br>
----  <br>
_internal  <br>
jmeter  <br>
> use jmeter  <br>
Using database jmeter  <br>
>  <br>
> show MEASUREMENTS  <br>
name: measurements  <br>
name  <br>
----  <br>
events  <br>
jmeter  <br>
> select * from events where application='7ddemo'  <br>
name: events  <br>
time application text title  <br>
---- ----------- ---- -----  <br>
1575255462806000000 7ddemo Test Cycle1 started ApacheJMeter  <br>
1575256463820000000 7ddemo Test Cycle1 ended ApacheJMeter  <br>
..............  <br>
n> select * from jmeter where application='7ddemo' limit 10  <br>
name: jmeter  <br>
time application avg count countError endedT hit max maxAT meanAT min minAT pct90.0 pct95.0 pct99.0 rb responseCode responseMessage sb startedT statut transaction  <br>
---- ----------- --- ----- ---------- ------ --- --- ----- ------ --- ----- ------- ------- ------- -- ------------ --------------- -- -------- ------ -----------  <br>
1575255462821000000 7ddemo 0 0 0 0 0 internal  <br>
1575255467818000000 7ddemo 232.82352941176472 17 0 17 849 122 384.9999999999996 849 849 0 0 all all  <br>
1575255467824000000 7ddemo 232.82352941176472 17 849 122 384.9999999999996 849 849 0 0 all 0_openIndexPage  <br>
1575255467826000000 7ddemo 232.82352941176472 17 849 122 384.9999999999996 849 849 ok 0_openIndexPage  <br>
1575255467829000000 7ddemo 0 1 1 1 1 internal  <br>
1575255472811000000 7ddemo 205.4418604651163 26 0 26 849 122 252.6 271.4 849 0 0 all all  <br>
1575255472812000000 7ddemo 0 1 1 1 1 internal  <br>
1575255472812000000 7ddemo 205.4418604651163 26 849 122 252.6 271.4 849 ok 0_openIndexPage  <br>
1575255472812000000 7ddemo 205.4418604651163 26 849 122 252.6 271.4 849 0 0 all 0_openIndexPage  <br>
1575255477811000000 7ddemo 198.2142857142857 27 0 27 849 117 263.79999999999995 292.3500000000001 849 0 0 all all<br>
</pre><br>
这段代码也就是说，在 InfluxDB 中，创建了两个 MEASUREMENTS，分别是 events 和 jmeter。这两个各自存了数据，我们在界面中配置的 testtile 和 eventTags 放在了 events 这个 MEASUREMENTS 中。在模板中这两个值暂时都是不用的。<br>
<br>在 JMeter 这个 MEASUREMENTS 中，我们可以看到 application 和事务的统计信息，这些值和控制台一致。在 Grafana 中显示的时候，就是从这个表中取出的数据，根据时序做的曲线。<br>
<h3>Grafana 中的配置</h3>有了 JMeter 发送到 InfluxDB 中的数据，下面就来配置一下 Grafana 中的展示。首先，要配置一个 InfluxDB 数据源。如下所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/f95becbc97e79bb45d1c74433b420d09.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/f95becbc97e79bb45d1c74433b420d09.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在这里配置好 URL、Database、User、Password 之后，直接点击保存即可。<br>
<br>然后添加一个 JMeter Dashboard，我们常用的 Dashboard 是 Grafana 官方 ID 为 5496 的模板。导入进来后，选择好对应的数据源。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/dc361ad18567240361a2d6eb185fc28b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/dc361ad18567240361a2d6eb185fc28b.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
然后就看到界面了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/f61251f161b6f94ca0a76d9d47d93b44.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/f61251f161b6f94ca0a76d9d47d93b44.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这时还没有数据，我们稍后做个示例，看下 JMeter 中的数据怎么和这个界面的数据对应起来。我们先看下图中两个重要的数据查询语句吧。<br>
<h4>TPS 曲线</h4><pre class="prettyprint">SELECT last("count") / $send_interval FROM "$measurement_name" WHERE ("transaction" =~ /^$transaction$/ AND "statut" = 'ok') AND $timeFilter GROUP BY time($__interval)<br>
</pre><br>
上面这个就是 Total TPS 了，在这里称为 throughput。<br>
<br>关于这个概念，我在第一篇中就已经有了说明，这里再次提醒，概念的使用在团队中要有统一的认识，不要受行业内一些传统信息的误导。<br>
<br>这里取的数据来自 MEASUREMENTS 中成功状态的所有事务。<br>
<br>响应时间曲线：<br>
<pre class="prettyprint">SELECT mean("pct95.0") FROM "$measurement_name" WHERE ("application" =~ /^$application$/) AND $timeFilter GROUP BY "transaction", time($__interval) fill(null)<br>
</pre><br>
这里是用 95 pct 内的响应时间画出来的曲线。<br>
<br>整体展示出来的效果如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/7f4ddbdd2aeada167ca9c973a80fb7a7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/7f4ddbdd2aeada167ca9c973a80fb7a7.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>数据比对</h4>首先，我们在 JMeter 中配置一个简单的场景。10 个线程，每个线程迭代 10 次，以及两个 HTTP 请求。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/eb3b8adf8b6b2efff7e76ea9ecb2939a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/eb3b8adf8b6b2efff7e76ea9ecb2939a.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
也就是说，这时会产生 10x10x2=200 次请求。我们用 JMeter 跑起来看一下。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/babad6d47d202c50b023937bb4fc0520.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/babad6d47d202c50b023937bb4fc0520.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
看到了吧，这个请求数和我们预想的一样。下面我们看一下 Grafana 中展示出来的结果。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/a3f53bd6eea707d8c19f168a810ef176.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/a3f53bd6eea707d8c19f168a810ef176.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
还有针对每个事务的统计情况。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/3bd44fe909bebc6ed296336e5fd352ab.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/3bd44fe909bebc6ed296336e5fd352ab.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
至此，JMeter 到 Grafana 的展示过程就完成了。以后我们就不用再保存 JMeter 的执行结果了，也不用等着 JMeter 输出 HTML 了。<br>
<h3>node_exporter + Prometheus + Grafana 的数据展示逻辑</h3>对性能测试来说，在常用的 Grafana + Prometheus + Exporter 的逻辑中，第一步要看的就是操作系统资源了。所以在这一篇中，我们将以 node_exporter 为例来说明一下操作系统抽取数据的逻辑，以便知道监控数据的来源，至于数据的含义，我们将在后续的文章中继续描述。<br>
<br>首先，我们还是要画一个图。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/b9da16dbb1b01ec05d5e6baf4b86df68.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/b9da16dbb1b01ec05d5e6baf4b86df68.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
现在 node_exporter 可以支持很多个操作系统了。官方列表如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/c0066de00102a51f4cecce5986dc5c2e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/c0066de00102a51f4cecce5986dc5c2e.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
当然不是说只支持这些，你也可以扩展自己的 Exporter。<br>
<h4>配置 node_exporter</h4>node_exporter 目录如下：<br>
<pre class="prettyprint">[root@7dgroup2 node_exporter-0.18.1.linux-amd64]# ll  <br>
total 16524  <br>
-rw-r--r-- 1 3434 3434 11357 Jun 5 00:50 LICENSE  <br>
-rwxr-xr-x 1 3434 3434 16878582 Jun 5 00:41 node_exporter  <br>
-rw-r--r-- 1 3434 3434 463 Jun 5 00:50 NOTICE<br>
</pre><br>
启动：<br>
<pre class="prettyprint">[root@7dgroup2 node_exporter-0.18.1.linux-amd64]#./node_exporter --web.listen-address=:9200 &<br>
</pre><br>
是不是很简洁？如果想看更多的功能 ，可以查看下它的帮助。<br>
<h4>配置 Prometheus</h4>先下载 Prometheus：<br>
<pre class="prettyprint">[root@7dgroup2 data]# wget -c https://github.com/prometheus/prometheus/releases/download/v2.14.0/prometheus-2.14.0.linux-amd64.tar.gz  <br>
..........  <br>
100%[=============================================================================================>] 58,625,125 465KB/s in 6m 4s<br>
<br>
<br>
2019-11-29 15:40:16 (157 KB/s) - ‘prometheus-2.14.0.linux-amd64.tar.gz’ saved [58625125/58625125]<br>
<br>
<br>
[root@7dgroup2 data]<br>
</pre><br>
解压之后，我们可以看到目录结构如下：<br>
<pre class="prettyprint">[root@7dgroup2 prometheus-2.11.1.linux-amd64]# ll  <br>
total 120288  <br>
drwxr-xr-x. 2 3434 3434 4096 Jul 10 23:26 console_libraries  <br>
drwxr-xr-x. 2 3434 3434 4096 Jul 10 23:26 consoles  <br>
drwxr-xr-x. 3 root root 4096 Nov 30 12:55 data  <br>
-rw-r--r--. 1 3434 3434 11357 Jul 10 23:26 LICENSE  <br>
-rw-r--r--. 1 root root 35 Aug 7 23:19 node.yml  <br>
-rw-r--r--. 1 3434 3434 2770 Jul 10 23:26 NOTICE  <br>
-rwxr-xr-x. 1 3434 3434 76328852 Jul 10 21:53 prometheus  <br>
-rw-r--r-- 1 3434 3434 1864 Sep 21 09:36 prometheus.yml  <br>
-rwxr-xr-x. 1 3434 3434 46672881 Jul 10 21:54 promtool  <br>
[root@7dgroup2 prometheus-2.11.1.linux-amd64]#<br>
</pre><br>
在prometheus.yml中添加如下配置，以取数据：<br>
<pre class="prettyprint">- job_name: 's1'  <br>
static_configs:  <br>
- targets: ['172.17.211.143:9200']<br>
</pre><br>
启动：<br>
<pre class="prettyprint">[root@7dgroup2 data]# ./prometheus --config.file=prometheus.yml &<br>
</pre><br>
这样就行了吗？当然不是。根据上面的流程图，我们还需要配置 Grafana。<br>
<h4>配置 Grafana</h4>首先配置一个数据源，非常简单。如下所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/b9923e55f56086d12331cf74c34c8c99.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/b9923e55f56086d12331cf74c34c8c99.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
再配置一个 node_exporter 的模板，比如我这里选择了官方模板（ID：11074），展示如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/a42fa3677beab12b6c431d7e1ead5338.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/a42fa3677beab12b6c431d7e1ead5338.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>数据逻辑说明</h4>说明完上面的过程之后，对我们做性能测试和分析的人来说，最重要的，就是要知道数据的来源和含义了。<br>
<br>拿上面图中的 CPU 使用率来说吧（因为 CPU 使用率是非常重要的一个计数器，所以我们今天先拿它来开刀）。<br>
<br>我们先点一下 title 上的 edit，看一下它的 query 语句。<br>
<pre class="prettyprint">avg(irate(node_cpu_seconds_total&#123;instance=~"$node",mode="system"&#125;[30m])) by (instance) avg(irate(node_cpu_seconds_total&#123;instance=~"$node",mode="user"&#125;[30m])) by (instance) avg(irate(node_cpu_seconds_total&#123;instance=~"$node",mode="iowait"&#125;[30m])) by (instance) 1 - avg(irate(node_cpu_seconds_total&#123;instance=~"$node",mode="idle"&#125;[30m])) by (instance)<br>
</pre><br>
这些都是从 Prometheus 中取出来的数据，查询语句读了 Prometheus 中node_cpu_seconds_total的不同的模块数据。<br>
<br>下面我们来看一下，node_exporter暴露出来的计数器。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/4635598d6d63370fff8f3e8aa2257e44.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/4635598d6d63370fff8f3e8aa2257e44.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这些值和 top 一样，都来自于/proc/目录。下面这张图是 top 数据，我们可以比对一下。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210820/5994917cfb6560db64aca29bba77fb5c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210820/5994917cfb6560db64aca29bba77fb5c.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
到此，我们就了解到了操作系统中监控数据的取值逻辑了，也就是从操作系统本身的计数器中取出值来，然后传给 Prometheus，再由 Grafana 中的 query 语句查出相应的数据，最后由 Grafana 展示在界面上。<br>
<h3>总结</h3>为什么要解释数据的逻辑呢？因为最近在工作中遇到一些情况，有人觉得有了 Prometheus + Grafana + Exportor 这样的组合工具之后，基本上都不再用手工执行什么命令了。但我们要了解的是，对于监控平台来说，它取的所有的数据必然是被监控者可以提供的数据，像 node_exporter 这样小巧的监控收集器，它可以获取的监控数据，并不是整个系统全部的性能数据，只是取到了常见的计数器而已。这些计数器不管是用命令查看，还是用这样炫酷的工具查看，它的值本身都不会变。所以不管是在监控平台上看到的数据，还是在命令行中看到的数据，我们最重要的是要知道含义以及这些值的变化对性能测试和分析的下一步骤的影响。<br>
<br>原文链接：<a href="https://www.cnblogs.com/siguadd/p/14878035.html" rel="nofollow" target="_blank">https://www.cnblogs.com/siguadd/p/14878035.html</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            