
---
title: '彻底理解Prometheus查询语法'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/30208af6efe2ac86fcd0ad2702ae650e.png'
author: Dockone
comments: false
date: 2021-07-11 14:06:06
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/30208af6efe2ac86fcd0ad2702ae650e.png'
---

<div>   
<br>本文档主要分为两部分，分别讲解PromQL和Grafana的基础使用，在阅读PromQL部分时，建议不要联想Grafana中要怎么使用这些查询表达式，又是怎么根据查询结果绘图的，因为PromQL对于Grafana来说和SQL并没有区别，都是查询出结果，然后根据各种指定配置进行绘图，所以阅读和理解PromQL部分，应关注查询结果是什么样的，不要关注这些结果在Grafana中是怎么绘图的。<br>
<h3>理解时间序列</h3><h4>指标</h4>指标就是要监控的目标。<br>
<br>在形式上，所有的指标（Metric）都通过如下格式标示：<br>
<pre class="prettyprint"><metric name>&#123;<label name>=<label value>, ...&#125; <br>
</pre><br>
指标名称（metric name）一般反映被监控样本的含义（比如，http_request_total - 表示当前系统接收到的HTTP请求总量）。<br>
<br>​ 标签（label）反映了当前样本的特征维度，通过这些维度可以对样本数据进行过滤，聚合等。<br>
<h4>样本</h4>Prometheus会定时到指定的Exportor上pull当前的样本数据，然后根据pull的时间以时间序列的方式保存在内存数据库中，并且定时持久化到硬盘上，Exportor只维护指标的值。每条时间序列由指标名称（metrics）和一组标签集（labelset）确定并命令，也就是说一个指标名称可能对应很多条时间序列。<br>
<br>可以将时间序列理解为一个以时间为轴的矩阵，如下所示，有三个时间序列在时间轴上分别对应不同的值：<br>
<pre class="prettyprint">^<br>
│     . . . . . . . . . .   node_cpu&#123;cpu="cpu0",mode="idle"&#125;<br>
│     . . . . . . . . . .   node_cpu&#123;cpu="cpu0",mode="system"&#125;<br>
│     . . . . . . . . . .   node_load1&#123;&#125;<br>
v<br>
<------- 时间 ----------><br>
</pre><br>
每一个点称为一个样本（sample），样本由以下三部分组成：<br>
<ul><li>指标（metric）：metric name和描述当前样本特征的labelsets；</li><li>时间戳（timestamp）：一个精确到毫秒的时间戳；</li><li>值（value）：表示该时间的样本的值。</li></ul><br>
<br><pre class="prettyprint"><--------------- metric ---------------------><-timestamp -><-value-><br>
http_request_total&#123;status="200", method="GET"&#125;@1434417560938 => 94355<br>
http_request_total&#123;status="200", method="GET"&#125;@1434417561287 => 94334<br>
http_request_total&#123;status="404", method="GET"&#125;@1434417560938 => 38473<br>
http_request_total&#123;status="404", method="GET"&#125;@1434417561287 => 38544<br>
http_request_total&#123;status="200", method="POST"&#125;@1434417560938 => 4748<br>
http_request_total&#123;status="200", method="POST"&#125;@1434417561287 => 4785<br>
</pre><br>
所以查询值的where条件就是指标、标签和时间戳（区间）。<br>
<h3>查询语法</h3><h4>指标查询（瞬时向量查询）</h4>通过指标名称和标签进行查询，可以查询该指标下的所有时间序列距离当前系统时间最新的值，无时间概念，所以查询的结果称为瞬时向量（instant vector），如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/30208af6efe2ac86fcd0ad2702ae650e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/30208af6efe2ac86fcd0ad2702ae650e.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
而且可以看到查询到的多条时间序列都包含指定的标签。单独使用指标名称，相当于不使用标签进行过滤，同样独单使用标签查询也可以。<br>
<br>标签过滤支持使用=和!=两种完全匹配模式：<br>
<ul><li>通过使用label=value可以选择那些标签满足表达式定义的时间序列；</li><li>反之使用label!=value则可以根据标签匹配排除时间序列。</li></ul><br>
<br>除了使用完全匹配的方式对时间序列进行过滤以外，还支持使用正则表达式作为匹配条件，多个正则表达式之间使用|进行分离：<br>
<ul><li>使用label=~regx表示选择符合正则表达式定义的时间序列；</li><li>反之使用label=!~regx进行反向选择。</li></ul><br>
<br>例如，如果想查询多个环境下的请求数统计，可以使用如下表达式：<br>
<pre class="prettyprint">http_requests_total&#123;environment=~"prodect|test|development",method!="GET"&#125; <br>
</pre><br>
每个正则表达式就是简单的字符串。<br>
<h4>时间范围查询（区间向量查询）</h4>如果我们想过去一段时间范围内的样本数据时，我们则需要使用区间向量表达式。区间向量表达式和瞬时向量表达式之间的差异在于需要定义时间范围，通过时间范围选择器[]进行定义。例如查询距离当前系统时间最近5分钟内的所有样本数据：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/1466b66ee786d227762c4d1cc32a0fc2.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/1466b66ee786d227762c4d1cc32a0fc2.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到结果中每个时间序列都有5个值并且@了不同的时间戳（因为该prometheus每分钟pull一次，所以5分钟有5个结果）。<br>
<br>除了使用m表示分钟以外，PromQL的时间范围选择器支持其它时间单位：<br>
<ul><li>s - 秒</li><li>m - 分钟</li><li>h - 小时</li><li>d - 天</li><li>w - 周</li><li>y - 年</li></ul><br>
<br><h4>时间位移</h4>在瞬时向量表达式或者区间向量表达式中，都是以Prometheus当前系统时间为基准进行查询：<br>
<pre class="prettyprint">http_request_total&#123;&#125; # 瞬时向量表达式，选择当前最新的数据<br>
http_request_total&#123;&#125;[5m] # 区间向量表达式，选择以当前时间为基准过去5分钟内的所有数据<br>
</pre><br>
而如果我们想查询5分钟之前的最新数据，或者想查询昨天的所有数据呢？<br>
<br>这个时候我们就可以使用位移操作，位移操作的关键字为offset，例如：<br>
<pre class="prettyprint">http_request_total&#123;&#125; offset 5m<br>
http_request_total&#123;&#125;[1d] offset 1d<br>
</pre><br>
<h4>操作符</h4>除了能够方便的查询和过滤时间序列以外，还支持丰富的操作符，用户可以使用这些操作符进一步的对事件序列进行二次加工。这些操作符包括：数学运算符，逻辑运算符，布尔运算符等等。<br>
<br><strong>数学运算符</strong><br>
<br>操作数可以是一个常数，也可以是一个查询表达式，比如：<br>
<br><blockquote><br>bet_amount_total / 100 : bet_amount是投注金额的总计，经常单位是分，为了转成元，可以除以100<br>
  http_requests_total&#123;api="/bet“&#125; + http_requests_total&#123;api="/login“&#125; 计算投注和登录请求的和</blockquote>支持的所有数学运算符如下所示：<br>
<ul><li><ul>+ （加法）</ul></li><li><ul>- （减法）</ul></li><li><ul>* （乘法）</ul></li><li>/ （除法）</li><li>% （求余）</li><li>^ （幂运算）</li></ul><br>
<br><strong>布尔运算符</strong><br>
<br>通过布尔运算对时间序列进行过滤，例如如下想查询node_cpu_seconds_total&#123;mode=“idle”&#125; > 22000的时间序列，不大于的时间序列会被过滤掉。<br>
<br>过滤前：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/22210f800dd3c282a25d12bf197690e6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/22210f800dd3c282a25d12bf197690e6.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
过滤后：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/1dc9a002b4a859df3645e272390be0f4.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/1dc9a002b4a859df3645e272390be0f4.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
目前，Prometheus支持以下布尔运算符如下：<br>
<ul><li>== （相等）</li><li>!= （不相等）</li><li>> （大于）</li><li>< （小于）</li><li>>= （大于等于）</li><li><= （小于）</li></ul><br>
<br><strong>获取布尔运算结果</strong><br>
<br>布尔运算的默认行为是对时间序列进行过滤。而有时候我们需要的是的运算结果。例如，只需要知道当前HTTP请求量是否>=1000，如果大于等于1000则返回1否则返回0。这时可以使用bool修饰符改变布尔运算的默认行为。 例如：<br>
<pre class="prettyprint">http_requests_total > bool 1000<br>
</pre><br>
使用bool修饰符后，布尔运算不会对时间序列进行过滤，而是直接依次对各个样本数据进行比较，结果是0或者1。从而形成一条新的时间序列，如下图value等于0或者1：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/850897ba245f3cbfd977a9f6f4f0ed4f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/850897ba245f3cbfd977a9f6f4f0ed4f.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>聚合函数</h4>查询可能会返回多条满足指定标签的时间序列，可是有时候我们并不希望分开查看，恰恰大多数情况其实是想查询一条时间序列的结果，例如查询请求总数时想要的结果是：<br>
<pre class="prettyprint">http_requests_total&#123;&#125; 170<br>
</pre><br>
而并不是想要：<br>
<pre class="prettyprint">http_requests_total&#123;environment="product“&#125; 30<br>
http_requests_total&#123;environment="test“&#125; 60<br>
http_requests_total&#123;environment="developement“&#125; 80<br>
</pre><br>
为了实现这个需求，PromQL提供的聚合操作可以用来对这些时间序列进行处理，通过处理形成一条新的时间序列，上述需求的表达式应该是：sum(http_requests_total)，例如下图会自动将所有时间序列的值相加后形成一条新的时间序列作为结果。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/1398421403ae8f3cab297f078331396b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/1398421403ae8f3cab297f078331396b.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
sum函数非常常用，因为常常不知道查询到时间序列究竟又多少条，注意不要再误认为sum是求指标在某个时间段的和。<br>
<br>有下面这些聚合操作符：<br>
<ul><li>sum：求和</li><li>min：最小值</li><li>max：最大值</li><li>avg：平均值</li><li>stddev：标准差</li><li>stdvar：方差</li><li>count：元素个数</li><li>count_values：等于某值的元素个数</li><li>bottomk：最小的k个元素</li><li>topk：最大的k个元素</li><li>quantile：分位数</li></ul><br>
<br><strong>部分聚合</strong><br>
<br>有时候，聚合并不想完全聚合，想根据某个标签进行区分时候，可以使用by进行拆分，比如监控每个CPU累计的空闲时间：sum(node_cpu_seconds_total&#123;mode=“idle”&#125; )by (cpu)，并设置了时间序列的名称模式为：cpu-&#123;&#123;cpu&#125;&#125;。<br>
<br>图示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/d7d3fe98f5378a2961fdd8132ef83f16.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/d7d3fe98f5378a2961fdd8132ef83f16.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>内置函数</h4>为了方便查询，Prometheus 内置了一些函数来辅助计算，下面介绍一些典型的。<br>
<ul><li>instant-vector abs(instant-vector)：绝对值</li><li>instant-vector sqrt(instant-vector)：平方根</li><li>instant-vector exp(instant-vector)：指数计算</li><li>instant-vector ln(instant-vector )：自然对数</li><li>instant-vector ceil(instant-vector)：向上取整</li><li>instant-vector floor(instant-vector)：向下取整</li><li>instant-vector round(instant-vector)：四舍五入取整</li><li>instant-vector delta(range-vector)：计算区间向量里最大最小的差值</li><li>instant-vector increase(range-vector)：计算区间向量里最后一个值和第一个值的差值</li><li>instant-vector rate(range-vector)：计算区间向量里的平均增长率</li></ul><br>
<br>然而在实际使用中，发现increase函数计算有误差，比如一分钟的前值和后值分别是1和183，差值应该是182，但是increase(m e t r i c [ 1 m ] )的结果是185，使用&#123;metric&#125;[1m])的结果是185，使用metric[1m])的结果是185，使用&#123;metric&#125; - $&#123;metric&#125; offset 1的结果却是正确的182。误差原因目前还没有确定。<br>
<br>以下函数允许随着时间的推移聚合给定范围向量的每个序列，并返回具有每个序列聚合结果的即时向量：<br>
<ul><li>avg_over_time(range-vector)：指定间隔内所有点的平均值。</li><li>min_over_time(range-vector)：指定间隔中所有点的最小值。</li><li>max_over_time(range-vector)：指定间隔内所有点的最大值。</li><li>sum_over_time(range-vector)：指定时间间隔内所有值的总和。</li></ul><br>
<br><h3>指标分类(了解)</h3>Prometheus根据目标功能和内容的不同，把指标分了4种类型（metric type）：Counter（计数器）、Gauge（仪表盘）、Histogram（直方图）、Summary（摘要）；但是本质上都是指标，都是时间序列，只是进行了简单的分类，更方便理解和沟通。<br>
<h4>Counter：只增不减的计数器</h4>Counter类型的指标其工作方式和计数器一样，只增不减（除非系统发生重置）。常见的监控指标，如http_requests_total，node_cpu都是Counter类型的监控指标。<br>
<br>Counter是一个简单但有强大的工具，例如我们可以在应用程序中记录某些事件发生的次数，通过以时序的形式存储这些数据，我们可以轻松的了解该事件产生速率的变化。PromQL内置的聚合函数可以用户对这些数据进行进一步的分析：<br>
<br>例如，通过rate()函数获取HTTP请求量的增长率：<br>
<pre class="prettyprint">rate(http_requests_total[5m])<br>
</pre><br>
查询当前系统中，访问量前10的HTTP地址：<br>
<pre class="prettyprint">topk(10, http_requests_total)<br>
</pre><br>
<h4>Gauge：可增可减的仪表盘</h4>与Counter不同，Gauge类型的指标侧重于反应系统的当前状态。因此这类指标的样本数据可增可减。常见指标如：node_memory_MemFree（主机当前空闲的内容大小）、node_memory_MemAvailable（可用内存大小）都是Gauge类型的监控指标。<br>
<br>通过Gauge指标，用户可以直接查看系统的当前状态：<br>
<pre class="prettyprint">node_memory_MemFree<br>
</pre><br>
对于Gauge类型的监控指标，通过PromQL内置函数delta()可以获取样本在一段时间返回内的变化情况。例如，计算CPU温度在两个小时内的差异：<br>
<pre class="prettyprint">delta(cpu_temp_celsius&#123;host="zeus"&#125;[2h])<br>
</pre><br>
<h4>Histogram和Summary：数据分布</h4>除了Counter和Gauge类型的监控指标以外，Prometheus还定义分别定义Histogram和Summary的指标类型，主用用于统计和分析样本的分布情况。<br>
<br>在大多数情况下，我们都倾向于使用某些量化指标的平均值，例如CPU的平均使用率、页面的平均响应时间。这种方式的问题很明显，以系统API调用的平均响应时间为例：如果大多数API请求都维持在100ms的响应时间范围内，而个别请求的响应时间需要5s，那么就会导致某些Web页面的响应时间落到中位数的情况，而这种现象被称为长尾问题。<br>
<br>为了区分是平均的慢还是长尾的慢，最简单的方式就是按照请求延迟的范围进行分组。例如，统计延迟在010ms之间的请求数有多少而1020ms之间的请求数又有多少。通过这种方式可以快速分析系统慢的原因。Histogram和Summary都是为了能够解决这样问题的存在，通过Histogram和Summary类型的监控指标，我们可以快速了解监控样本的分布情况。<br>
<br>例如，Prometheus自身监控的指标【prometheus_tsdb_wal_fsync_duration_seconds】的指标类型为Summary。 它记录了Prometheus Server中wal_fsync操作的耗时，通过访问Prometheus Server的/metrics地址，可以获取到以下监控样本数据（当前时间的样本）：<br>
<pre class="prettyprint"># HELP prometheus_tsdb_wal_fsync_duration_seconds Duration of WAL fsync.<br>
# TYPE prometheus_tsdb_wal_fsync_duration_seconds summary<br>
prometheus_tsdb_wal_fsync_duration_seconds&#123;quantile="0.5"&#125; 0.012352463<br>
prometheus_tsdb_wal_fsync_duration_seconds&#123;quantile="0.9"&#125; 0.014458005<br>
prometheus_tsdb_wal_fsync_duration_seconds&#123;quantile="0.99"&#125; 0.017316173<br>
prometheus_tsdb_wal_fsync_duration_seconds_sum 2.888716127000002<br>
prometheus_tsdb_wal_fsync_duration_seconds_count 216<br>
</pre><br>
从上面的样本中可以得知当前Prometheus Server进行wal_fsync操作的总次数为216次，总耗时为2.888716127000002s，并且50%操作耗时不超过0.012352463秒，90%的操作耗时不超过0.014458005s，99%的操作耗时不超过0.017316173s。<br>
<br>在Prometheus自身监控中，我们还能找到类型为Histogram的监控指标：prometheus_tsdb_compaction_chunk_range_bucket。<br>
<pre class="prettyprint"># HELP prometheus_tsdb_compaction_chunk_range Final time range of chunks on their first compaction<br>
# TYPE prometheus_tsdb_compaction_chunk_range histogram<br>
prometheus_tsdb_compaction_chunk_range_bucket&#123;le="100"&#125; 0<br>
prometheus_tsdb_compaction_chunk_range_bucket&#123;le="400"&#125; 0<br>
prometheus_tsdb_compaction_chunk_range_bucket&#123;le="1600"&#125; 0<br>
prometheus_tsdb_compaction_chunk_range_bucket&#123;le="6400"&#125; 0<br>
prometheus_tsdb_compaction_chunk_range_bucket&#123;le="25600"&#125; 0<br>
prometheus_tsdb_compaction_chunk_range_bucket&#123;le="102400"&#125; 0<br>
prometheus_tsdb_compaction_chunk_range_bucket&#123;le="409600"&#125; 0<br>
prometheus_tsdb_compaction_chunk_range_bucket&#123;le="1.6384e+06"&#125; 260<br>
prometheus_tsdb_compaction_chunk_range_bucket&#123;le="6.5536e+06"&#125; 780<br>
prometheus_tsdb_compaction_chunk_range_bucket&#123;le="2.62144e+07"&#125; 780<br>
prometheus_tsdb_compaction_chunk_range_bucket&#123;le="+Inf"&#125; 780<br>
prometheus_tsdb_compaction_chunk_range_sum 1.1540798e+09<br>
prometheus_tsdb_compaction_chunk_range_count 780<br>
</pre><br>
从上面的样本中可以得知当前Prometheus Server tsdb数据库的压缩后数据库共有780个，总大小是1.1540798e+09，小于等于100/400/1600/…/409600的有0。<br>
<br>与Summary类型的指标相似之处在于Histogram类型的样本同样会反应当前指标的记录的总数(以_count作为后缀)以及其值的总量（以_sum作为后缀）。不同在于Histogram指标直接反应了在不同区间内样本的个数，区间通过标签len进行定义。<br>
<br>同时对于Histogram的指标，我们还可以通过histogram_quantile()函数计算出其值的分位数。和Summary不同在于Histogram通过histogram_quantile函数在服务器端计算的分位数，即Prometheus计算； 而Sumamry的分位数则是由客户端计算，Prometheus直接pull即可。因此对于分位数的计算而言，Summary在通过PromQL进行查询时有更好的性能表现，而Histogram则会消耗更多的资源；反之对于客户端而言Histogram消耗的资源更少。<br>
<pre class="prettyprint"># 查询 prometheus_tsdb_compaction_chunk_range 95 百分位<br>
<br>
histogram_quantile(0.95, prometheus_tsdb_compaction_chunk_range_bucket)<br>
</pre><br>
<h3>HTTP API</h3><h4>Grafana查询报错</h4>比如想在Grafana绘制折线图（Graph），因为需要很多时间点的值，似乎应该使用时间范围查询或者说是区间查询，因为指标查询（瞬时查询）只能查询的当前的最新值，让我们试一试：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/e0745be55945d521f81c30c3826ecb8a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/e0745be55945d521f81c30c3826ecb8a.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
红色叹号错误提示：<br>
<br><blockquote><br>“invalid expression type “range vector” for range query, must be Scalar or instant Vector”</blockquote>非法的表达式类型：区间向量用于区间查询，必须是标量（常数）或者瞬时向量。<br>
<br>这是因为在Grafana查询需要调用prometheus的http api，所以首先了解Prometheus的http api是什么？<br>
<h4>Query</h4>通过使用如下API我们可以查询PromQL表达式在指定时间点下的计算结果。<br>
<pre class="prettyprint">GET /api/v1/query<br>
</pre><br>
URL请求参数：<br>
<ul><li>query=：PromQL表达式。</li><li>time=：指定时间戳。可选参数，默认情况下使用Prometheus当前系统时间。</li></ul><br>
<br>例如：<br>
<pre class="prettyprint">$ curl 'http://192.168.40.161:9090/api/v1/query?query=node_cpu_seconds_total&#123;mode="idle"&#125;&time=1587690566.034'<br>
&#123;<br>
"status": "success",<br>
"data": &#123;<br>
"resultType": "vector",<br>
"result": [<br>
  &#123;<br>
    "metric": &#123;<br>
      "__name__": "node_cpu_seconds_total",<br>
      "cpu": "0",<br>
      "instance": "192.168.40.161:9100",<br>
      "job": "linux",<br>
      "mode": "idle"<br>
    &#125;,<br>
    "value": [<br>
      1587690566.034,<br>
      "24745.92"<br>
    ]<br>
  &#125;,<br>
  &#123;<br>
    "metric": &#123;<br>
      "__name__": "node_cpu_seconds_total",<br>
      "cpu": "1",<br>
      "instance": "192.168.40.161:9100",<br>
      "job": "linux",<br>
      "mode": "idle"<br>
    &#125;,<br>
    "value": [<br>
      1587690566.034,<br>
      "24846.7"<br>
    ]<br>
  &#125;<br>
]<br>
&#125;<br>
&#125; <br>
</pre><br>
<strong>响应数据类型</strong><br>
<br>当API调用成功后，Prometheus会返回JSON格式的响应内容，格式如上小节所示。并且在data节点中返回查询结果。data节点格式如下：<br>
<pre class="prettyprint">&#123;<br>
"resultType": "matrix" | "vector",<br>
"result": <value><br>
&#125; <br>
</pre><br>
PromQL表达式可能返回多种数据类型，在响应内容中使用resultType表示当前返回的数据类型，包括：<br>
<br>1、瞬时向量：vector<br>
<br>当返回数据类型resultType为vector时，result响应格式如下：<br>
<pre class="prettyprint">[<br>
&#123;<br>
"metric": &#123; "<label_name>": "<label_value>", ... &#125;,<br>
"value": [ <unix_time>, "<sample_value>" ]<br>
&#125;,<br>
...<br>
] <br>
</pre><br>
其中Metrics表示当前时间序列的特征维度，value只包含一个唯一的样本。<br>
<br>2、区间向量：matrix<br>
<br>当返回数据类型resultType为matrix时，result响应格式如下：<br>
<pre class="prettyprint">[<br>
&#123;<br>
"metric": &#123; "<label_name>": "<label_value>", ... &#125;,<br>
"values": [ [ <unix_time>, "<sample_value>" ], ... ]<br>
&#125;,<br>
...<br>
] <br>
</pre><br>
其中Metrics表示当前时间序列的特征维度，values包含当前事件序列的一组样本，例如：<br>
<pre class="prettyprint">$ curl 'http://192.168.40.161:9090/api/v1/query?query=node_cpu_seconds_total&#123;mode="idle"&#125;[5m]&time=1587690566.034'<br>
<br>
&#123;<br>
"status": "success",<br>
"data": &#123;<br>
"resultType": "matrix",<br>
"result": [<br>
  &#123;<br>
    "metric": &#123;<br>
      "__name__": "node_cpu_seconds_total",<br>
      "cpu": "0",<br>
      "instance": "192.168.40.161:9100",<br>
      "job": "linux",<br>
      "mode": "idle"<br>
    &#125;,<br>
    "values": [<br>
      [<br>
        1587690266.034,<br>
        "24499.47"<br>
      ],<br>
      [<br>
        1587690326.034,<br>
        "24548.82"<br>
      ],<br>
      [<br>
        1587690386.034,<br>
        "24598.17"<br>
      ],<br>
      [<br>
        1587690446.034,<br>
        "24648.21"<br>
      ],<br>
      [<br>
        1587690506.034,<br>
        "24697.37"<br>
      ],<br>
      [<br>
        1587690566.034,<br>
        "24745.92"<br>
      ]<br>
    ]<br>
  &#125;,<br>
  &#123;<br>
    "metric": &#123;<br>
      "__name__": "node_cpu_seconds_total",<br>
      "cpu": "1",<br>
      "instance": "192.168.40.161:9100",<br>
      "job": "linux",<br>
      "mode": "idle"<br>
    &#125;,<br>
    "values": [<br>
      [<br>
        1587690266.034,<br>
        "24600.32"<br>
      ],<br>
      [<br>
        1587690326.034,<br>
        "24649.97"<br>
      ],<br>
      [<br>
        1587690386.034,<br>
        "24698.96"<br>
      ],<br>
      [<br>
        1587690446.034,<br>
        "24747.99"<br>
      ],<br>
      [<br>
        1587690506.034,<br>
        "24797.52"<br>
      ],<br>
      [<br>
        1587690566.034,<br>
        "24846.7"<br>
      ]<br>
    ]<br>
  &#125;<br>
]<br>
&#125;<br>
&#125; <br>
</pre><br>
<h4>query_range</h4>使用如下API，我们可以查询PromQL表达式在一段时间内的数据。<br>
<pre class="prettyprint">GET /api/v1/query_range<br>
</pre><br>
URL请求参数：<br>
<ul><li>query=：PromQL表达式。</li><li>start=：起始时间。</li><li>end=：结束时间。</li><li>step=：查询步长。</li></ul><br>
<br>返回结果一定是一个区间向量：<br>
<pre class="prettyprint">&#123;<br>
"resultType": "matrix",<br>
"result": <value><br>
&#125; <br>
</pre><br>
比如：<br>
<pre class="prettyprint">$ curl 'http://192.168.40.161:9090/api/v1/query_range?query=node_cpu_seconds_total&#123;mode="idle"&#125;&start=1587693926.035&end=1587694166.034&step=2m'<br>
<br>
&#123;<br>
"status": "success",<br>
"data": &#123;<br>
"resultType": "matrix",<br>
"result": [<br>
  &#123;<br>
    "metric": &#123;<br>
      "__name__": "node_cpu_seconds_total",<br>
      "cpu": "0",<br>
      "instance": "192.168.40.161:9100",<br>
      "job": "linux",<br>
      "mode": "idle"<br>
    &#125;,<br>
    "values": [<br>
      [<br>
        1587693926.035,<br>
        "27510.45"<br>
      ],<br>
      [<br>
        1587694046.035,<br>
        "27607.39"<br>
      ]<br>
    ]<br>
  &#125;,<br>
  &#123;<br>
    "metric": &#123;<br>
      "__name__": "node_cpu_seconds_total",<br>
      "cpu": "1",<br>
      "instance": "192.168.40.161:9100",<br>
      "job": "linux",<br>
      "mode": "idle"<br>
    &#125;,<br>
    "values": [<br>
      [<br>
        1587693926.035,<br>
        "27645.27"<br>
      ],<br>
      [<br>
        1587694046.035,<br>
        "27743.97"<br>
      ]<br>
    ]<br>
  &#125;<br>
]<br>
&#125;<br>
&#125; <br>
</pre><br>
需要注意的是，只能使用瞬时向量类型的表达式。<br>
<br>这是因为区间数据查询实现，首先根据时间范围和步长计算时间点集合，比如：<br>
<br>start=1s & end=60s & setp=10s,<br>
<br>那么时间点集合是：1s 、11s、21s、31s、41s、51s<br>
<br>因为下一个时间点应该是61s，不在时间范围内。<br>
<br>然后查询距离每个时间点最近的值作为该时间点的值。<br>
<br>而如果使用区间向量表达式，那么每个时间点计算结果将是一个区间，而目标查询结果也是区间，并且两个区间的含义不相同，所以无法融合在一块。<br>
<h4>Grafana报错原因</h4>Grafana默认调用的api是query_range api，可通过【Query Inspector】按钮展开查询请求和结果，如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/02eee205198335aeaa9de05911dec54b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/02eee205198335aeaa9de05911dec54b.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
所以Graph中不能直接使用区间向量查询，而应该使用瞬时向量，然后调用区间数据查询API来查询指定时间范围的值（时间范围是Grafana面板右上角选择的时间范围，步长默认15秒，可通过Min step设置）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/62bb206ba6a37c091df13770de66aa32.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/62bb206ba6a37c091df13770de66aa32.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
Graph通过查询结果中的各个时间点的值绘制成线。<br>
<br>可以通过开启Instant开关，使Grafana调用瞬时数据查询API，例如：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/ff8cf843d8cbb8236583961ca8500525.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/ff8cf843d8cbb8236583961ca8500525.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到API改成了Query，并且Prometheus返回了5个时间点的值，此时Graph不会连接成线。<br>
<h4>区间向量的应用</h4>前面说到通过瞬时向量查询+query_rangw API可以查询到指定时间范围的值，那么区间向量查询似乎没啥用了？<br>
<br>区间向量可用于计算某个时间点的附近的状态，通过内置函数可以将区间向量转成瞬时向量，就能用在Graph图中了；比如返回时间范围内中每个时间点的过去1分钟内 HTTP 请求数：increase(http_requests_total[1m])<br>
<h3>Grafana配置方法</h3>通过前面的学习，我们知道如何编写Prometheus查询表达式，也知道Grafana通过调用HTTP API接口来查询时间序列的，可能查到很多条时间序列，查询结果中每个时间序列可能只有最新的值，也可能包含一个时间范围内很多个值。接下来，讲解Grafana提供了那些数据展示方法，以及如何使用查询结构。<br>
<h4>Graph</h4>Graph默认以时间为X轴展示所有查询到的时间序列，如下图所示，查询到两条时间序列：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/d3b0be68c7303b0163e8aa83ddf5c5fa.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/d3b0be68c7303b0163e8aa83ddf5c5fa.jpg" class="img-polaroid" title="12.jpg" alt="12.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
右上角按钮【Last 5 minutes】指定时间范围，可以改为其他的时间范围。注意这里的Last 5 Time的时间基准是Grafana页面所在PC机的当前时间，如果PC机的时间异常，可能查询到的并不是目标时间范围的数据,比如系统当前时间是12:05:00，那么Last 5 minutes的时间范围会转换成：start=12:00:00&end=12:05:00。具体的请求和响应信息，可以通过按钮【Query Inspector】展示。<br>
<br>通过按钮【Add Query】可以添加查询表达式，需要注意的是一条查询语句可以展示多条线，这取决于查询结果中有多少条时间序列。<br>
<br>通过指定【Min step】可以修改步长，可以改变查询结果中时间点的密度，即步长越大，则相同时间范围的时间点就越少，密度就越小，那么折线可能更陡峭。<br>
<h4>SingleStat</h4>显示查询结果中最新的一个值，查询结果不能包含多条时间序列，否者提示错误。如果未开启Instant，则可显示指定时间范围内的变化曲线，如果开启Instant则仅显示一个数值；<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/7f078567089dfc0ce14131742765d541.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/7f078567089dfc0ce14131742765d541.jpg" class="img-polaroid" title="13.jpg" alt="13.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
支持设置阈值来显示不同的颜色，例如大于0.5显示红色：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/2218465c4aee6ec811e6d3e363b9842b.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/2218465c4aee6ec811e6d3e363b9842b.jpg" class="img-polaroid" title="14.jpg" alt="14.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
Stat和SingStat基本一样，不同的是Stat支持查询并显示多条时间序列的变化曲线和值。<br>
<h4>Gauge</h4>和SingleStat一样，也是显示查询结果中最新的一个值，支持一次查询多条时间序列，例如下图一个表达式返回两条时间序列：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/452851bde337a3d867d64d273a685f17.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/452851bde337a3d867d64d273a685f17.jpg" class="img-polaroid" title="15.jpg" alt="15.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
也可以设置阈值来显示不同的颜色，例如上图小于0.5时显示绿色，大于0.5时内边填充黄色，更加醒目，并且在仪表盘的边上根据值的分布动态显示绿色和黄色的比例。<br>
<h4>Table</h4>默认情况下，表格显示所有时间序列在不同时间点上的值，最左列是时间戳对应的时间，后边就是所有指标对用的值：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/8193fc6efdef7c6c2b9548559e54a2f9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/8193fc6efdef7c6c2b9548559e54a2f9.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如果开启Instant，则只显示最新的时间戳和最新的值：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/7fe44ed9b5fd244a12e802695087138f.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/7fe44ed9b5fd244a12e802695087138f.jpg" class="img-polaroid" title="17.jpg" alt="17.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
可通过【Column Styles】对列进行设置：<br>
<br>隐藏列：设置列的Type是Hidden<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/712d43371b6ab6c1498a81ac91365d80.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/712d43371b6ab6c1498a81ac91365d80.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
设置列的值：比如设置某列为查询表达式B的值，设置名称正则【Apply to columns named】为 Value #B<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210710/09846c2777f15301c9d2bb6e05664565.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210710/09846c2777f15301c9d2bb6e05664565.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如果想显示某个标签的值，那么【Apply to columns named】就是标签的名字。<br>
<br>原文链接：<a href="https://blog.csdn.net/zhouwenjun0820/article/details/105823389" rel="nofollow" target="_blank">https://blog.csdn.net/zhouwenj ... 23389</a>，作者：imagine0623
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            