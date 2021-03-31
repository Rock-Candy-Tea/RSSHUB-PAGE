
---
title: '记一次 Kubernetes 机器内核问题排查'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/6d0e3c327eab3f78ecd5ca7e466e0371.png'
author: Dockone
comments: false
date: 2021-03-31 12:10:36
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/6d0e3c327eab3f78ecd5ca7e466e0371.png'
---

<div>   
<br>此次排查发生在 2020-11 月份，一直没时间写博客描述事情经过，本次正好一起写了吧。<br>
<h3>具体现象</h3>在线上环境中的某个应用出现了接口缓慢的问题！<br>
<br>就凭这个现象，能列出来的原因数不胜数。本篇博客主要叙述一下几次排查以及最后如何确定原因的过程，可能不一定适用于其他集群，就当是提供一个参考吧。排查过程比较冗长，过去太久了，我也不太可能回忆出所有细节，希望大家见谅。<br>
<h3>网络拓扑结构</h3>网络请求流入集群时，对于我们集群的结构：<br>
<pre class="prettyprint">用户请求=> Nginx => Ingress => uwsgi<br>
</pre><br>
不要问为什么有了 Ingress 还有 Nginx，这是历史原因，有些工作暂时需要由 Nginx 承担。<br>
<h3>初次定位</h3>请求变慢一般马上就会考虑，程序是不是变慢了，所以在发现问题后，首先在 uwsgi 中增加简单的小接口，这个接口是处理快并且马上返回数据，然后定时请求该接口。在运行几天之后，确认到该接口的访问速度也很慢，排除程序中的问题，准备在链路中查找原因。<br>
<h3>再次定位 – 简单的全链路数据统计</h3>由于我们的 Nginx 有 2 层，需要针对它们分别确认，看看究竟是哪一层慢了。请求量是比较大的，如果针对每个请求去查看，效率不高，而且有可能掩盖真正原因，所以这个过程采用统计的方式。统计的方式是分别查看两层 Nginx 的日志情况。由于我们已经在 ELK 上接入了日志，ELK 中筛选数据的脚本简单如下：<br>
<pre class="prettyprint">&#123;<br>
"bool": &#123;<br>
"must": [<br>
  &#123;<br>
    "match_all": &#123;&#125;<br>
  &#125;,<br>
  &#123;<br>
    "match_phrase": &#123;<br>
      "app_name": &#123;<br>
        "query": "xxxx"<br>
      &#125;<br>
    &#125;<br>
  &#125;,<br>
  &#123;<br>
    "match_phrase": &#123;<br>
      "path": &#123;<br>
        "query": "/app/v1/user/ping"<br>
      &#125;<br>
    &#125;<br>
  &#125;,<br>
  &#123;<br>
    "range": &#123;<br>
      "request_time": &#123;<br>
        "gte": 1,<br>
        "lt": 10<br>
      &#125;<br>
    &#125;<br>
  &#125;,<br>
  &#123;<br>
    "range": &#123;<br>
      "@timestamp": &#123;<br>
        "gt": "2020-11-09 00:00:00",<br>
        "lte": "2020-11-12 00:00:00",<br>
        "format": "yyyy-MM-dd HH:mm:ss",<br>
        "time_zone": "+08:00"<br>
      &#125;<br>
    &#125;<br>
  &#125;<br>
]<br>
&#125;<br>
&#125; <br>
</pre><br>
<h4>数据处理方案</h4>根据 trace_id 可以获取到 Nignx 日志以及 Ingress 日志，通过 ELK 的 API 获得。<br>
<pre class="prettyprint"># 这个数据结构用来记录统计结果，<br>
# [[0, 0.1], 3]表示落在 0~0.1 区间的有 3 条记录<br>
# 因为小数的比较和区间比较麻烦，所以采用整数，这里的 0~35 其实是 0~3.5s 区间<br>
# ingress_cal_map = [<br>
#     [[0, 0.1], 0],<br>
#     [[0.1, 0.2], 0],<br>
#     [[0.2, 0.3], 0],<br>
#     [[0.3, 0.4], 0],<br>
#     [[0.4, 0.5], 0],<br>
#     [[0.5, 1], 0],<br>
# ]<br>
ingress_cal_map = []<br>
for x in range(0, 35, 1):<br>
ingress_cal_map.append(<br>
    [[x, (x+1)], 0]<br>
)<br>
nginx_cal_map = copy.deepcopy(ingress_cal_map)<br>
nginx_ingress_gap = copy.deepcopy(ingress_cal_map)<br>
ingress_upstream_gap = copy.deepcopy(ingress_cal_map)<br>
<br>
<br>
def trace_statisics():<br>
trace_ids = []<br>
# 这里的 trace_id 是提前查找过，那些响应时间比较久的请求所对应的 trace_id<br>
with open(trace_id_file) as f:<br>
    data = f.readlines()<br>
    for d in data:<br>
        trace_ids.append(d.strip())<br>
<br>
cnt = 0<br>
for trace_id in trace_ids:<br>
    try:<br>
        access_data, ingress_data = get_igor_trace(trace_id)<br>
    except TypeError as e:<br>
        # 继续尝试一次<br>
        try:<br>
            access_data, ingress_data = get_igor_trace.force_refresh(trace_id)<br>
        except TypeError as e:<br>
            print("Can't process trace &#123;&#125;: &#123;&#125;".format(trace_id, e))<br>
            continue<br>
    if access_data['path'] != "/app/v1/user/ping":  # 过滤脏数据<br>
        continue<br>
    if 'request_time' not in ingress_data:<br>
        continue<br>
<br>
    def get_int_num(data):  # 数据统一做 *10 处理<br>
        return int(float(data) * 10)<br>
<br>
    # 针对每个区间段进行数据统计，可能有点罗嗦和重复，我当时做统计够用了<br>
    ingress_req_time = get_int_num(ingress_data['request_time'])<br>
    ingress_upstream_time = get_int_num(ingress_data['upstream_response_time'])<br>
    for cal in ingress_cal_map:<br>
        if ingress_req_time >= cal[0][0] and ingress_req_time < cal[0][1]:<br>
            cal[1] += 1<br>
            break<br>
<br>
    nginx_req_time = get_int_num(access_data['request_time'])<br>
    for cal in nginx_cal_map:<br>
        if nginx_req_time >= cal[0][0] and nginx_req_time < cal[0][1]:<br>
            cal[1] += 1<br>
            break<br>
<br>
    gap = nginx_req_time - ingress_req_time<br>
    for cal in nginx_ingress_gap:<br>
        if gap >= cal[0][0] and gap <= cal[0][1]:<br>
            cal[1] += 1<br>
            break<br>
<br>
    gap = ingress_req_time - ingress_upstream_time<br>
    for cal in ingress_upstream_gap:<br>
        if gap >= cal[0][0] and gap <= cal[0][1]:<br>
            cal[1] += 1<br>
            break <br>
</pre><br>
我分别针对 request_time（Nginx），request_time（Ingress）以及 requet_time（nginx） - request_time（Ingress）做了统计。<br>
<br>最后的统计结果大概如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/6d0e3c327eab3f78ecd5ca7e466e0371.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/6d0e3c327eab3f78ecd5ca7e466e0371.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/0a2dae72ff5429a3cab24e5a5268d2a8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/0a2dae72ff5429a3cab24e5a5268d2a8.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/76ad051f73d0435ed56fd6e1d74b9214.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/76ad051f73d0435ed56fd6e1d74b9214.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>结果分析</h4>我们总共有约 3000 条数据！<br>
<br>图一：超过半数的请求落在 1 ~ 1.1s 区间，1s ~ 2s 的请求比较均匀，之后越来越少了。<br>
<br>图二：大约 1/4 的请求其实已经在 0.1s 内返回了，但是 1 ~ 1.1s 也有 1/4 的请求落上去了，随后的结果与图一类似。<br>
<br>从图 1 图 2 结合来看，部分请求在 Ingress 侧处理的时间其实比较短的。<br>
<br>图三：比较明显了，2/3 的请求在响应时间方面能够保持一致，1/3 的请求会有 1s 左右的延迟。<br>
<h4>小结</h4>从统计结果来看，Nginx => Ingress 以及 Ingress => upstream，都存在不同程度的延迟，超过 1s 的应用，大约有 2/3 的延迟来自 Ingress => upstream，1/3 的延迟来自 Nginx => Ingress。<br>
<h3>再深入调查 - 抓包处理</h3>抓包调查主要针对 Ingress => uwsgi，由于数据包延迟的情况只是偶发性现象，所以需要抓取所有的数据包再进行过滤……这是一条请求时间较长的数据，本身这个接口返回应该很快。<br>
<pre class="prettyprint">&#123;<br>
"_source": &#123;<br>
"INDEX": "51",<br>
"path": "/app/v1/media/",<br>
"referer": "",<br>
"user_agent": "okhttp/4.8.1",<br>
"upstream_connect_time": "1.288",<br>
"upstream_response_time": "1.400",<br>
"TIMESTAMP": "1605776490465",<br>
"request": "POST /app/v1/media/ HTTP/1.0",<br>
"status": "200",<br>
"proxy_upstream_name": "default-prod-XXX-80",<br>
"response_size": "68",<br>
"client_ip": "XXXXX",<br>
"upstream_addr": "172.32.18.194:6000",<br>
"request_size": "1661",<br>
"@source": "XXXX",<br>
"domain": "XXX",<br>
"upstream_status": "200",<br>
"@version": "1",<br>
"request_time": "1.403",<br>
"protocol": "HTTP/1.0",<br>
"tags": ["_dateparsefailure"],<br>
"@timestamp": "2020-11-19T09:01:29.000Z",<br>
"request_method": "POST",<br>
"trace_id": "87bad3cf9d184df0:87bad3cf9d184df0:0:1"<br>
&#125;<br>
&#125; <br>
</pre><br>
<h4>Ingress 侧数据包</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/fcc1f6477a87475a82a7f68e9a0bf99a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/fcc1f6477a87475a82a7f68e9a0bf99a.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>uwsgi 侧数据包</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/37d56b7a6e469e8413356f716105adc2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/37d56b7a6e469e8413356f716105adc2.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>数据包流转情况</h3>回顾一下 TCP 三次握手：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/8817165c450b4e29922d1b6ed01065fd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/8817165c450b4e29922d1b6ed01065fd.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
首先从 Ingress 侧查看，连接在 21.585446 开始，22.588023 时，进行了数据包重新发送的操作。<br>
<br>从 Node 侧查看，Node 在 Ingress 数据包发出后不久马上就收到了 syn，也立刻进行了 syn 的返回，但是不知为何 1s 后才出现在 Ingress 处。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/fe0a71c5ed4bf8f5e2807380da22de96.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/fe0a71c5ed4bf8f5e2807380da22de96.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/3cbeee704b5a73d8ecf11c257f6836b3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/3cbeee704b5a73d8ecf11c257f6836b3.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
有一点比较令人在意，即便是数据包发生了重传，但是也没有出现丢包的问题，从两台机器数据包的流转来看，此次请求中，大部分的时间是因为数据包的延迟到达造成的，重传只是表面现象，真正的问题是发生了数据包的延迟。<br>
<h3>不止是 ACK 数据包发生了延迟</h3>从随机抓包的情况来看，不止是 SYN ACK 发生了重传：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/3453173d6d6b6e8f3f4e3fbe783bb1d6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/3453173d6d6b6e8f3f4e3fbe783bb1d6.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
有些 FIN ACK 也会，数据包的延迟是有概率的行为！<br>
<h4>小结</h4>单单看这个抓包可能只能确认是发生了丢包，但是如果结合 Ingress 与 Nginx 的日志请求来看，如果丢包发生在 TCP 连接阶段，那么在 Ingress 中，我们就可以查看 upstream_connect_time 这个值来大致估计下超时情况。当时是这么整理的记录：<br>
<br><blockquote><br>我初步猜测这部分时间主要消耗在了 TCP 连接建立时，因为建立连接的操作在两次 Nginx 转发时都存在，而我们的链路全部使用了短连接，下一步我准备增加 $upstream_connect_time 变量，记录建立连接花费的时间。<a href="http://nginx.org/en/docs/http/ngx_http_upstream_module.html" rel="nofollow" target="_blank">http://nginx.org/en/docs/http/ ... .html</a></blockquote><h3>后续工作</h3>既然可以了解到 TCP 连接的建立时间比较久，我们可以用它来作为一个衡量指标，我把 wrk 也修改了下，增加了对于连接时间的测量，具体的PR见<a href="https://github.com/wg/wrk/pull/447">这里</a>，我们可以利用这一项指标衡量后端的服务情况。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/7ee29e2cd7c2738e235eaa479c46a785.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/7ee29e2cd7c2738e235eaa479c46a785.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>寻找大佬，看看是否遇到类似问题</h3>上面的工作前前后后我进行了几次，也没有什么头绪，遂找到公司的其他 Kubernetes 大佬咨询问题，大佬提供了一个思路：<br>
<br><blockquote><br>宿主机延迟也高的话，那就暂时排除宿主机到容器这条路径。我们这边此前排查过一个延迟问题， 是由于 Kubernetes 的监控工具定期 cat proc 系统下的 cgroup 统计信息， 但由于 Docker 频繁销毁重建以及内核 cache 机制，使得每次 cat 时间很长占用内核导致网络延迟， 可否排查一下你们的宿主机是否有类似情形？ 不一定是 cgroup，其他需要频繁陷入到内核的操作都可能导致延迟很高。<br>
  这个跟我们排查的 cgroup 太像了，宿主机上有一些周期性任务，随着执行次数增多，占用的内核资源越来越多，达到一定程度就影响了网络延迟。</blockquote>大佬们也提供了一个内核检查工具（可以追踪和定位中断或者软中断关闭的时间）：<a href="https://github.com/bytedance/trace-irqoff" rel="nofollow" target="_blank">https://github.com/bytedance/trace-irqoff</a><br>
<br>有问题的 Ingress 机器的 latency 特别多，好多都是这样的报错，其他机器没有这个日志：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/bed86de765ed9cbc01e59741b7f9fb1b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/bed86de765ed9cbc01e59741b7f9fb1b.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/b26759ce3313e476d9c84c14a57b49d3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/b26759ce3313e476d9c84c14a57b49d3.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
而后，我针对机器中的 kubelet 进行了一次追踪，从火焰图中可以确认，大量的时间耗费在了读取内核信息中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/8991cb21e49d07bfa25c2e5c6995f2af.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/8991cb21e49d07bfa25c2e5c6995f2af.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
其中具体的代码如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/7cbd566fc81a7e0916c47fdde8cef1eb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/7cbd566fc81a7e0916c47fdde8cef1eb.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>小结</h4>根据大佬所给的方向，基本能够确定问题发生的真正原因：机器上定时任务的执行过多，内核缓存一直增加，导致内核速度变慢了。它一变慢，引发了 TCP 握手时间变长，最后造成用户体验下降。既然发现了问题，解决方案也比较容易搜索到了，增加任务，检查内核是否变慢，慢了的话就清理一次：<br>
<pre class="prettyprint">sync && echo 3 > /proc/sys/vm/drop_caches<br>
</pre><br>
<h3>总结</h3>这次的排查过程是由于应用层出现了影响用户体验的问题后，进一步延伸到了网络层，其中经历了漫长的抓包过程，也增加了自己的脚本用于指标衡量，随后又通过内核工具定位到了具体应用，最后再根据应用的 pprof 工具制作出的火焰图定位到了更加精确的异常位置，期间自己一个人没法处理问题，遂请其他大佬来帮忙，大佬们见多识广，可以给出一些可能性的猜想，还是很有帮助的。<br>
<br>当你发现某台机器无论做什么都慢，而 CPU 和内核却不是瓶颈的时候，那有可能是内核慢了。<br>
<br>希望本文能对大家未来排查集群问题时有所帮助。<br>
<br>原文链接：<a href="https://corvo.myseu.cn/2021/03/21/2021-03-" rel="nofollow" target="_blank">https://corvo.myseu.cn/2021/03/21/2021-03-21-</a>记一次kubernetes机器内核问题的排查/，作者：corvofeng
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            