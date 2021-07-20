
---
title: '如何用LogQL在几秒内查询TB级的日志？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/d62d60590ccfc7a0180a258ab6a37954.png'
author: Dockone
comments: false
date: 2021-07-20 06:09:02
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/d62d60590ccfc7a0180a258ab6a37954.png'
---

<div>   
<br>LogQL在很大程度上受Prometheus的PromQL启发。但是，当涉及到在过滤海量日志时，我们就像面临在大海捞针一样复杂。LogQL是Loki特有的语句，在本文中，我们将提供LogQL的快速过滤器查询技巧，这些查询可以在几秒钟内过滤掉数TB的数据。  <br>
<br>在Loki中，我们可以使用三种类型的过滤器：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210714/d62d60590ccfc7a0180a258ab6a37954.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/d62d60590ccfc7a0180a258ab6a37954.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Label matchers</h3>Label matchers（标签匹配器）是你的第一道防线，是大幅减少你搜索的日志数量（例如，从100TB到1TB）的最好方法。当然，这意味着你需要在的日志采集端上有良好的标签定义规范。基本上，标签应该定义的类型包括，工作负载、集群、命名空间和容器等，这样你就可以在多个不同的维度上对数据进行切分。比如说：<br>
<ul><li>一个应用在多个集群上运行</li><li>落在多个Kubernetes集群命名空间的开发环境</li><li>生产环境的命名空间</li></ul><br>
<br>一个有效的经验法则是：你至少需要一个<code class="prettyprint">=</code>匹配器<code class="prettyprint">（例如，&#123;cluster=&quot;us-central1&quot;&#125;）</code>。否则，你将不得不提取整个索引数据。<br>
<br><blockquote><br>但有一个例外。如果匹配器包含一个或多个字元，比如<code class="prettyprint">&#123;container=~&quot;promtail|agent&quot;&#125;</code>，同时只有一个单一的regex匹配器，Loki可以自行优化查询。</blockquote>下面就是一些实用的样例：<br>
<br>好例子：<br>
<pre class="prettyprint">&#123;cluster="us-central1"&#125;  <br>
<br>
&#123;container="istio"&#125;  <br>
<br>
&#123;cluster="us-central1", container=~"agent|promtail"&#125; <br>
</pre><br>
坏例子：<br>
<pre class="prettyprint">&#123;job=~".*/queue"&#125;  <br>
<br>
&#123;namespace!~"dev-.*"&#125; <br>
</pre><br>
<h3>Line filters</h3>Line filters（行过滤器）是你的第二个好朋友，因为它们执行过程超级快。它允许你过滤包含（<code class="prettyprint">|=</code>）或不包含（<code class="prettyprint">!=</code>）字符串的日志，你也可以使用正则来匹配（<code class="prettyprint">|~</code>）或不匹配（<code class="prettyprint">!~</code>）日志，但你<code class="prettyprint">应该把它们放在标签匹配器之后</code>。<br>
<br>现在，当我们将这些过滤器连起来使用时，要注意<code class="prettyprint">过滤器的顺序</code>。先用那些能过滤最多日志的过滤器，然后再使用正则，它比<code class="prettyprint">=</code>和<code class="prettyprint">!=</code>慢。<br>
<br><blockquote><br>但有一个例外。<code class="prettyprint">|~ &quot;error|fatal &quot;</code>可以被Loki优化掉 实际上这两个字符串被Loki自动过滤掉了，所以不会执行正则匹配。</blockquote>一个好的方法是先添加一个符合你要找的东西的过滤器，例如，<code class="prettyprint">|= &quot;err&quot;</code>。然后再添加越来越多的不等式来过滤你不想要的东西，直到最终得到类似于下面这样的结果。<br>
<pre class="prettyprint">|= "err" != "timeout" != "cancelled" |~ "failed.*" != "memcached"<br>
</pre><br>
现在，如果你意识到你的大部分错误来自memcached，那么就把它移到第一个位置。<br>
<pre class="prettyprint">!= "memcached" |= "err" != "timeout" != "cancelled" |~ "failed.*"<br>
</pre><br>
这样一来，后续过滤器的执行次数就会减少。<br>
<br>除此之外，行过滤器也很适合查找IP、TraceID、UUID等类型的日志。比如下面这个也一个很好的查询方式。<br>
<pre class="prettyprint">&#123;namespace="prod"&#125; |= "traceID=2e2er8923100"<br>
</pre><br>
如果你想让这个traceID的所有日志都符合某个regex，可以在ID过滤器后面加上<code class="prettyprint">|~ &quot;/api/v.+/query&quot;</code>，这样就不会对prod命名空间的每个Pod中去添加查询。<br>
<h3>Label filters</h3>Label filters（标签过滤器）提供了更复杂的计算功能（duration，numerical等），但是它们通常需要先提取标签，然后再将标签值转换为另一种类型。这意味着它们通常是最慢的，因此我们应该<strong>最后使用它们</strong>。<br>
<br><blockquote><br>实际上我们可以在不提取标签的情况下使用标签过滤器（使用<code class="prettyprint">|json</code>或<code class="prettyprint">|logfmt</code>等解析器）。标签过滤器也可以在索引标签上工作。例如，<code class="prettyprint">&#123;job=&quot;ingress/nginx&quot;&#125;。| status_code >= 400 and cluster=&quot;us-central2&quot;</code>可以正常工作，但你真正应该问自己的是，你是否需要将 status_code 作为索引标签。一般来说，你不应该，但你可以考虑提取 status_code 作为标签，这可以将大批量的流（每秒超过一千行）分解成独立的流。</blockquote>尽管<code class="prettyprint">| json</code>  和<code class="prettyprint">| logfmt</code>解析器很快，但是解析<code class="prettyprint">| regex</code>却很慢。这就是为什么在使用解析器时，我总是在它前面加上一个行过滤器。例如，在我的Go应用程序（包括Loki）中，我的所有日志均支持显示文件名和行号（此处为<code class="prettyprint">caller=metrics.go:83</code>）。<br>
<pre class="prettyprint">level=info ts=2020-12-07T21:03:22.885781801Z caller=metrics.go:83 org_id=29 traceID=4078dafcbc079822 latency=slow query="&#123;cluster=\"ops-tools1\",job=\"loki-ops/querier\"&#125; != \"logging.go\" != \"metrics.go\" |= \"recover\"" query_type=filter range_type=range length=168h0m1s step=5m0s duration=54.82511258s status=200 throughput=8.3GB total_bytes=454GB<br>
</pre><br>
因此，当我们想过滤缓慢的请求时，应该先对<code class="prettyprint">记录文件和行号</code>进行过滤，然后再进行解析，最后再将提取的标签进行比较。<br>
<pre class="prettyprint">&#123;namespace="loki-ops",container="query-frontend"&#125; |= "caller=metrics.go:83" | logfmt | throughput > 1GB and duration > 10s and org_id=29<br>
</pre><br>
<h3>结论</h3>这三个过滤器（Label matchers，Line filters和Label filters）就像一个管道，将逐步处理日志。我们应该尝试在每个步骤上尽可能减少操作，因为对于每个行，每个后续步骤执行的速度都可能更慢。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/i4dCY611r0pWO_9lZQkGZA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/i4dCY611r0pWO_9lZQkGZA</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            