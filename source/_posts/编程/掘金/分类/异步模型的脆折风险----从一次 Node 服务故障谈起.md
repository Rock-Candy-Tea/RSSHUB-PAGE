
---
title: '异步模型的脆折风险----从一次 Node 服务故障谈起'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5800fbc3aa8b4c57ba7a595362f713e9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 19:20:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5800fbc3aa8b4c57ba7a595362f713e9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style>
<blockquote>
<p>当抵达 Node 服务的请求数达到理论最高吞吐量时, 单个请求的响应时间和所有请求平均响应时间会是什么关系?</p>
<p>   </p>
<p>答: 所有请求平均响应时间一切如常, 单个请求响应时间突然飞涨</p>
<p>   </p>
<p>为什么是这样?</p>
</blockquote>
<p>周末接到三次报警, 线上 Node 服务突然出现大量接口 30 秒超时. 但每次都是刚连上 vpn, 报警就消失. 期间没有上线操作, 流量不大且平稳, 报错的是普通接口逻辑流程正常, 99.5%的请求响应时间在 100ms 以内, 服务器 CPU 使用率稳定在 30% 且无波动, 内存使用无波动, 硬盘读写无波动. 但就是突然几千个请求响超时, 故障期间连服务器上的静态资源文件也拉不下来, 然后自动恢复正常...why?</p>
<h2 data-id="heading-0">排查步骤</h2>
<h3 data-id="heading-1">问题表现</h3>
<p>需要先确认问题表现, 在这次报警中, 问题表现如下</p>
<ol>
<li>服务短时间内出现大量请求超时, 30 秒内无响应, 504 报错</li>
<li>在服务故障期间(排查期间正好赶上一次故障), 访问服务器上的静态资源文件(只需要服务进程进行简单读取磁盘)也没有响应, 说明服务进程处于"卡死"状态</li>
<li>代码发版
<ul>
<li>最近 7 天无发版操作</li>
</ul>
</li>
<li>通过查询日志, 报错前 3 天内没有发生过重启, 报错期间也没有进程重启事件</li>
<li>历史报警
<ul>
<li>5 天前晚 7 点左右也有一次 504 报警, 1 分钟后解除, 当时排查后认为是网络抖动, 没有注意</li>
</ul>
</li>
<li>服务器
<ul>
<li>服务器 CPU 使用率无波动, 稳定在 30% 左右</li>
<li>服务进程 CPU 使用率大致在 16~25% 之间</li>
<li>磁盘 io 无波动</li>
<li>内存使用无波动, 且有较大冗余空间</li>
</ul>
</li>
<li>请求流量
<ul>
<li>日常 QPS 6~10</li>
<li>故障期间(11:05:00~11:20:00)
<ul>
<li>最高 QPS 67, 持续 1 秒, 随后恢复正常</li>
<li>平均每分钟有一次 QPS 为 20 的并发, 但只维持 1 秒</li>
</ul>
</li>
</ul>
</li>
<li>接口响应时间
<ul>
<li>日常接口响应时间 40~50ms</li>
<li>故障期间(11:05:00~11:20:00)
<ul>
<li>每分钟有一批接口响应时间在 1~3 秒, 只持续 1 秒</li>
<li>故障期间接口响应时间快速升高, 然后达到 30s, 持续 60s 后快速下降回正常状态</li>
</ul>
</li>
</ul>
</li>
<li>线上服务器日志
<ul>
<li>服务器本身只有 200 的日志记录, 通过 grep 遍历搜索, 没有 504 超时记录.</li>
<li>504 超时记录只出现在 Nginx 日志中</li>
<li>看到的记录响应耗时大部分为 0, 偶有 40~100 的情况</li>
</ul>
</li>
<li>服务器情况
<ul>
<li><strong>线上三台服务器几乎同步发生异常, 然后同步恢复</strong></li>
</ul>
</li>
<li>日常接口响应时间
<ul>
<li>每天大约有 1000 个请求响应时间在 300ms 以上, 但都是集中出现一阵后消失, 没有规律</li>
</ul>
</li>
<li>原始请求日志</li>
</ol>
<pre><code class="hljs language-java copyable" lang="java">    请求时间  响应时长  请求接口
    09:<span class="hljs-number">20</span>:<span class="hljs-number">25</span> <span class="hljs-number">0.091</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">25</span> <span class="hljs-number">0.036</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">25</span> <span class="hljs-number">0.040</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">25</span> <span class="hljs-number">0.036</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">25</span> <span class="hljs-number">0.045</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">25</span> <span class="hljs-number">0.054</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">25</span> <span class="hljs-number">0.151</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">25</span> <span class="hljs-number">0.036</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">25</span> <span class="hljs-number">0.106</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">26</span> <span class="hljs-number">0.046</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">26</span> <span class="hljs-number">0.061</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">26</span> <span class="hljs-number">0.056</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">26</span> <span class="hljs-number">0.042</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">28</span> <span class="hljs-number">2.177</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">28</span> <span class="hljs-number">0.811</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">28</span> <span class="hljs-number">2.377</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">28</span> <span class="hljs-number">0.929</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">29</span> <span class="hljs-number">2.916</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">30</span> <span class="hljs-number">2.735</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">40</span> <span class="hljs-number">14.397</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">46</span> <span class="hljs-number">19.809</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">46</span> <span class="hljs-number">1.723</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">48</span> <span class="hljs-number">21.274</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">48</span> <span class="hljs-number">1.063</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">49</span> <span class="hljs-number">3.777</span>   /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">49</span> <span class="hljs-number">22.506</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">49</span> <span class="hljs-number">21.235</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">49</span> <span class="hljs-number">22.760</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">49</span> <span class="hljs-number">22.239</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">49</span> <span class="hljs-number">22.534</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">50</span> <span class="hljs-number">21.391</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">50</span> <span class="hljs-number">14.277</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">50</span> <span class="hljs-number">21.354</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">50</span> <span class="hljs-number">15.353</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">50</span> <span class="hljs-number">22.900</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">50</span> <span class="hljs-number">20.077</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">50</span> <span class="hljs-number">20.772</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">50</span> <span class="hljs-number">10.949</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">50</span> <span class="hljs-number">16.745</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">50</span> <span class="hljs-number">22.802</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">50</span> <span class="hljs-number">22.125</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">56</span> <span class="hljs-number">30.000</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">57</span> <span class="hljs-number">30.001</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">57</span> <span class="hljs-number">30.001</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">58</span> <span class="hljs-number">30.000</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">59</span> <span class="hljs-number">30.000</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">59</span> <span class="hljs-number">30.000</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">59</span> <span class="hljs-number">30.001</span>  /api/xxx/list
    09:<span class="hljs-number">20</span>:<span class="hljs-number">59</span> <span class="hljs-number">30.000</span>  /api/xxx/list
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">代码问题?</h3>
<p>对于线上服务故障, 第一反应就是检查代码本身是否有问题. 由于是新业务, 排查日志发现 90%的请求都在访问<code>/api/xxx/list</code>, 所以检查起来比较简单. 经审核, 代码没有问题, 也没有明显存在风险的点. 考虑到如果代码真有问题, 那之前一定会有报错记录. 于是翻查请求历史日志, 发现请求都能在 50ms 内正常响应, 说明代码本身确实没毛病.</p>
<h3 data-id="heading-3">MySQL 慢查询 / 远程服务无响应?</h3>
<p>排除代码本身问题后, 紧接着需要考虑的是 MySQL 集群故障/ 慢查询的可能. 如果 MySQL 调用超时, 那 await 等待远程接口响应的 Node 服务自然也会超时.但这个想法很快被排除掉了, 主要是两个原因:</p>
<ol>
<li>假设是 MySQL 集群故障, 查询无响应. 那么同一时间段内, 依赖 MySQL 集群的其他服务必然也会报错, 不会只有我们一个服务故障. 但现实是故障期间只有我们的服务出现了 504 超时错误.</li>
<li>如果请求卡在等待远程调用中, 由于 Node 使用的是异步模型, 服务进程并不会阻塞在等待接口响应上. 此时其他接口/静态文件(不依赖外部接口)应该可以继续访问. 但在问题描述中可以看到, 故障期间静态文件也无法访问. 所以问题更像是整个服务进程失去了响应, 而非 MySQL 集群有问题.</li>
</ol>
<p>MySQL 问题排除.</p>
<h3 data-id="heading-4">服务器问题?</h3>
<p>有没有可能是服务器本身挂了呢? 但这也没可能:</p>
<ol>
<li>故障期间服务器上其他应用响应正常</li>
<li>位于三台服务器上的进程几乎同步故障, 说明是三台机器间共有的部分出错, 不像是单台服务器故障</li>
</ol>
<h3 data-id="heading-5">服务进程本身问题</h3>
<p>代码没有问题, MySQL 没有问题, 服务器也没有问题. 那只能是服务进程本身出了毛病.</p>
<p>通过故障期间每秒接口响应数(QPS)+接口响应时长合并图可以看到, 接口响应时长和 QPS 明显相关, 当 QPS 变大时, 接口响应时长一般都会随之增加, 而增大到极值(11:17~11:19), 响应时长突破 30s, 对应的就是线上 Nginx 504 报错. 但是, 服务器压力大导致接口超时可以理解, 但为什么静态资源请求也跟着超时? 为什么会这样?</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5800fbc3aa8b4c57ba7a595362f713e9~tplv-k3u1fbpfcp-zoom-1.image" alt="抖动期间QPS+接口响应时长合并数据" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">异步模型的脆折风险</h1>
<p>所有这些, 需要从 io 请求处理模型说起.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f44e1d7abeb442688b2386a7b1b73677~tplv-k3u1fbpfcp-zoom-1.image" alt="理想同步io模型" loading="lazy" referrerpolicy="no-referrer"></p>
<p>传统 io 模型是串行模式, 一个一个处理请求. 可以看到, 处理 6 个请求时, 总耗时 1200ms. 大量时间浪费在 io 等待中.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/195c72504f0043da8e2e3cb7fed40821~tplv-k3u1fbpfcp-zoom-1.image" alt="理想异步io处理模型" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了避免浪费, 提升服务器吞吐率, 异步 io 模型应运而生. 异步的基本思路是时间复用, 在等待 io 的期间让 CPU 去处理其他请求, 从而充分利用计算资源. 可以看到, 在理想情况下, 异步模型处理 6 个请求只需要 650ms.</p>
<p>不过, 这是理想情况. 在实际应用中, 请求的计算部分和 io 等待部分会交织在一起, 由于每个部分消耗时间都不太长, 因此会形成<strong>时间片</strong>的效果. 只有执行完所有时间片, 一个任务才能执行完成.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36cecdf217774019bfecfc38543e2535~tplv-k3u1fbpfcp-zoom-1.image" alt="请求模型.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而当多个请求同时到达 Node 进程时, Node 的任务队列会变成下边这样: 不同请求的回调在任务队列中进行等待执行.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91e603963b554b4a8e2955dbe93e2fd7~tplv-k3u1fbpfcp-zoom-1.image" alt="Node任务队列.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于接口响应过程被异步等待被拆分成一个个子任务, 形成了<strong>细碎的时间片</strong>, 接口的异步处理模型如下图所示. 当多个请求同时到达时, 由于 io 等待+任务队列调度的效果, Node 倾向于在请求间平均分配时间片, <strong>对同一接口同时到达的请求倾向于同时完成</strong>. 但可以看出, 即使切换时间片本身需要时间, 导致单个请求响应时长增加, 但因为可以利用 io 等待时间, 异步模型仍然比串行模式要高效.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25213a498117480295152928f17fbb88~tplv-k3u1fbpfcp-zoom-1.image" alt="实际异步io处理模型" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那如果待执行的任务没有 io 操作, 是<strong>纯计算密集型请求</strong>呢?</p>
<p>那就会悲剧. 如果是计算密集型请求, 异步模型的处理能力会回落到和串行模型同一水平, 甚至更差: <strong>在串行模式下, 高并发时串行模式至少可以保证前几个接口的正常响应</strong>, 后续接口由于等待时间过长才会超时报 504. 但在异步模型下, <strong>由于在各个任务间不断进行调度, 所有任务的完成时间都差不多, 会导致最终没有一个请求可以正常响应, 所有任务一起 504 超时报错</strong></p>
<p>如下图所示</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af7e0220cdf346dda42f99ad66696305~tplv-k3u1fbpfcp-zoom-1.image" alt="计算密集型异步io处理模型" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一般认为, web 服务是典型的 io 密集型场景, 大量时间消耗在 MySQL 通信与和其他接口交互中, 所以 Node 的异步模型天然适合用做 web 服务器. 但在特殊场景下, web 服务也会由 io 密集型退化为计算密集型: <strong>当请求数量超过阈值, 请求提供的 io 等待时长不足以完成其他请求的 CPU 操作时</strong>, 此时 CPU 就会变成服务的性能瓶颈. 由于所有请求都没有足够的 CPU 资源完成运算, 导致所有请求都<code>无法在可接受时间内响应</code>, 出现服务进程<code>"卡死"</code>的效果.</p>
<p>由于这个过程的临界点是<code>待处理请求所需的总CPU处理时长</code>大于<code>待处理请求所需的总IO时长</code>, 所以当问题发生时, 会有类似于钢板脆折的效果. 在临界点以下, 一切安好, 响应时长正常, 看不出有什么问题. 一旦超过临界点, 响应时长快速增加, 然后就是大规模 504 报错, 直到请求量降到临界点以下, 处理完所有挤压请求后, 一切又回归正常.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/248ff0cb31e64f65bfa095d02edb628a~tplv-k3u1fbpfcp-zoom-1.image" alt="并发量过大时的异步io处理模型" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以 Node 服务会有一个很特殊的现象: 绝大多数情况下表现正常, 但当并发量比最大容纳值稍微高一点, <strong>所有接口</strong>响应速度就会快速抬升(脆折), 但请求量只要降一点, 服务性能又会恢复正常. 整个表现非常反直觉, 但符合异步模型的原理.</p>
<h1 data-id="heading-7">实践验证</h1>
<p>说了这么多, 实际测试一下.</p>
<p>压测框架使用 koa, 分别用<code>asyncSetTimeoutSleep</code>和<code>asyncCPUSleep</code>模拟 io 密集型和计算密集型请求, 压测工具使用 ApacheBench, 测试命令为<code>ab -c 1/10/100/400 -n 10000 -k 'http://127.0.0.1:3000/'</code>, <code>-n</code>指测试总数, 取 10000, <code>-c</code>指每轮测试并发请求数, 分别取 1/10/100/400 进行测试, 测试代码&实验结果如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 测试代码</span>
<span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">"koa"</span>);
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncSetTimeoutSleep</span>(<span class="hljs-params">ms = <span class="hljs-number">0</span></span>) </span>&#123;
  <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      reslove(<span class="hljs-literal">true</span>);
    &#125;, ms);
  &#125;);
  <span class="hljs-keyword">return</span>;
&#125;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncCPUSleep</span>(<span class="hljs-params">ms = <span class="hljs-number">0</span></span>) </span>&#123;
  <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
    <span class="hljs-comment">// 这里必须使用setTimeout模拟sleep, 否则Node会由于没有调度机会,只能按先后顺序处理请求</span>
    <span class="hljs-comment">// (接受请求1->处理请求1->响应请求1->接受请求2->处理请求2->响应请求2->...)</span>
    <span class="hljs-comment">// 此时异步模式降级为串行模式, 失去比较意义</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 运算150000次在我的机器上正好是1ms, 单纯用来模拟CPU密集型操作, 没有特别意义</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">1500000</span> * ms; i++) &#123;&#125;
      reslove(<span class="hljs-literal">true</span>);
    &#125;, <span class="hljs-number">0</span>);
  &#125;);
  <span class="hljs-keyword">return</span>;
&#125;

app.use(<span class="hljs-keyword">async</span> (ctx) => &#123;
  <span class="hljs-comment">// await asyncCPUSleep(10);</span>
  <span class="hljs-keyword">await</span> asyncSetTimeoutSleep(<span class="hljs-number">10</span>);
  ctx.body = <span class="hljs-string">"Hello Koa"</span>;
&#125;);

app.listen(<span class="hljs-number">3000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>

<p>计算密集型</p>























































<table><thead><tr><th align="left">并发量/响应时长</th><th align="left">最小值[ms]</th><th align="left">平均数[ms]</th><th align="left">中位数[ms]</th><th align="left">最大值[ms]</th><th>平均请求响应时间(总时长/总请求数)[ms]</th><th>总响应时长[s]</th><th>QPS[次/秒]</th></tr></thead><tbody><tr><td align="left">1</td><td align="left">7</td><td align="left">11</td><td align="left">10</td><td align="left">37</td><td>11.172</td><td>111.724</td><td>89.51</td></tr><tr><td align="left">10</td><td align="left">10</td><td align="left">108</td><td align="left">106</td><td align="left">264</td><td>10.792</td><td>107.920</td><td>92.66</td></tr><tr><td align="left">100</td><td align="left">34</td><td align="left">1081</td><td align="left">1097</td><td align="left">1403</td><td>10.847</td><td>108.472</td><td>92.19</td></tr><tr><td align="left">400</td><td align="left">100</td><td align="left">4216</td><td align="left">4437</td><td align="left">4675</td><td>10.753</td><td>107.534</td><td>92.99</td></tr></tbody></table>
<p>io 密集型</p>

































































<table><thead><tr><th align="left">并发量/响应时长</th><th align="left">最小值[ms]</th><th align="left">平均数[ms]</th><th align="left">中位数[ms]</th><th align="left">最大值[ms]</th><th>平均请求响应时间(总时长/总请求数)[ms]</th><th>总响应时长[s]</th><th>QPS[次/秒]</th></tr></thead><tbody><tr><td align="left">1</td><td align="left">9</td><td align="left">11</td><td align="left">11</td><td align="left">12</td><td>10.614</td><td>106.139</td><td>94.22</td></tr><tr><td align="left">10</td><td align="left">9</td><td align="left">11</td><td align="left">11</td><td align="left">14</td><td>1.086</td><td>10.857</td><td>921.03</td></tr><tr><td align="left">100</td><td align="left">10</td><td align="left">14</td><td align="left">13</td><td align="left">43</td><td>0.144</td><td>1.442</td><td>6934.20</td></tr><tr><td align="left">400</td><td align="left">20</td><td align="left">43</td><td align="left">35</td><td align="left">150</td><td>0.110</td><td>1.099</td><td>9099.80</td></tr><tr><td align="left">1000</td><td align="left">35</td><td align="left">70</td><td align="left">67</td><td align="left">130</td><td>0.086</td><td>0.861</td><td>11618.10</td></tr></tbody></table>
<p>可以看到</p>
<ul>
<li>当并发量为 1 时, 实际为串行模式, 此时<code>请求平均响应时间</code>等于<code>平均请求响应时间</code>, 计算密集型请求和 io 密集型请求吞吐量&平均请求响应时长接近.</li>
<li>当并发量增大时
<ul>
<li>对于 计算密集型请求
<ul>
<li>异步模型没有可供利用的 io 等待时间, <code>平均请求响应时间</code>等于<code>单个请求必要CPU时间</code>, 因此 <code>平均请求响应时间</code>不变, 异步模式劣化为串行模式</li>
<li>同时, 由于框架中的各种 await 等待形成了时间片效果, 导致 Node 会在各个请求间对时间片进行调度, 所有请求接近同时完成, <code>请求平均响应时间</code>大幅上升</li>
<li>需要说明的是, 由于事件驱动的随机性, 这里的调度并不是指公平调度, 先进入的请求大概率先集齐所有时间片完成请求, 但不代表先进入的请求一定先完成</li>
</ul>
</li>
<li>对于 io 密集型请求
<ul>
<li>异步框架充分利用 io 等待时间进行 CPU 运算, <code>平均请求响应时间</code>不断缩短, 直到逼近<code>单个请求必要CPU时间</code></li>
<li>随着并发量增大, 在 io 等待时间内(10ms)不足以完成请求, CPU 时间逐渐变为性能瓶颈, 性能表现逐步向计算密集型请求靠近, 体现为<code>请求平均响应时间</code>不断增大</li>
<li>换言之, 由于接收请求/给出响应总会消耗 CPU 资源, <strong>只要并发请求量够大, io 密集型总会退化为 CPU 密集型.</strong></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>顺带提一句, 处理计算密集型请求时还有一个特殊情况:</p>
<p>如果 CPU 运算为整块代码, 期间没有 await 形成时间片供 Node 调度, 那么会 Node 处理模型劣化为串行模式, 执行过程变为<code>接收请求1</code>-><code>处理响应请求1</code>-><code>接收请求2</code>-><code>处理响应请求2</code>-><code>接收请求3</code>-><code>处理响应请求3</code>...</p>
<p>由于所有请求同时发出, 串行处理, 所以请求响应时长会呈递增关系, 如下所示</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 示例代码</span>
<span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">"koa"</span>);
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncCPUSleep</span>(<span class="hljs-params">ms = <span class="hljs-number">0</span></span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">1500000</span> * ms; i++) &#123;&#125;
  <span class="hljs-keyword">return</span>;
&#125;

<span class="hljs-comment">// response</span>
app.use(<span class="hljs-keyword">async</span> (ctx) => &#123;
  <span class="hljs-comment">// 由于没有promise返回, 这里的await是无效的, 不会形成时间片</span>
  <span class="hljs-comment">// 阻塞式休眠1秒</span>
  <span class="hljs-keyword">await</span> asyncCPUSleep(<span class="hljs-number">1000</span>);
  ctx.body = <span class="hljs-string">"Hello Koa"</span>;
&#125;);

app.listen(<span class="hljs-number">3000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 串行模式对应日志</span>
第<span class="hljs-number">0</span>条请求完成, 耗时<span class="hljs-number">842</span>毫秒
第<span class="hljs-number">1</span>条请求完成, 耗时<span class="hljs-number">1573</span>毫秒
第<span class="hljs-number">2</span>条请求完成, 耗时<span class="hljs-number">2275</span>毫秒
第<span class="hljs-number">3</span>条请求完成, 耗时<span class="hljs-number">2987</span>毫秒
第<span class="hljs-number">4</span>条请求完成, 耗时<span class="hljs-number">3683</span>毫秒
第<span class="hljs-number">5</span>条请求完成, 耗时<span class="hljs-number">4396</span>毫秒
第<span class="hljs-number">7</span>条请求完成, 耗时<span class="hljs-number">5085</span>毫秒
第<span class="hljs-number">6</span>条请求完成, 耗时<span class="hljs-number">5821</span>毫秒
第<span class="hljs-number">9</span>条请求完成, 耗时<span class="hljs-number">6535</span>毫秒
第<span class="hljs-number">11</span>条请求完成, 耗时<span class="hljs-number">7247</span>毫秒
第<span class="hljs-number">8</span>条请求完成, 耗时<span class="hljs-number">7963</span>毫秒
第<span class="hljs-number">10</span>条请求完成, 耗时<span class="hljs-number">8671</span>毫秒
第<span class="hljs-number">12</span>条请求完成, 耗时<span class="hljs-number">9381</span>毫秒
第<span class="hljs-number">13</span>条请求完成, 耗时<span class="hljs-number">10151</span>毫秒
第<span class="hljs-number">14</span>条请求完成, 耗时<span class="hljs-number">10852</span>毫秒
第<span class="hljs-number">15</span>条请求完成, 耗时<span class="hljs-number">11555</span>毫秒
第<span class="hljs-number">16</span>条请求完成, 耗时<span class="hljs-number">12225</span>毫秒
第<span class="hljs-number">24</span>条请求完成, 耗时<span class="hljs-number">12996</span>毫秒
第<span class="hljs-number">23</span>条请求完成, 耗时<span class="hljs-number">13723</span>毫秒
第<span class="hljs-number">25</span>条请求完成, 耗时<span class="hljs-number">14531</span>毫秒
第<span class="hljs-number">28</span>条请求完成, 耗时<span class="hljs-number">15235</span>毫秒
第<span class="hljs-number">22</span>条请求完成, 耗时<span class="hljs-number">15954</span>毫秒
第<span class="hljs-number">18</span>条请求完成, 耗时<span class="hljs-number">16860</span>毫秒
第<span class="hljs-number">29</span>条请求完成, 耗时<span class="hljs-number">17906</span>毫秒
第<span class="hljs-number">21</span>条请求完成, 耗时<span class="hljs-number">18595</span>毫秒
第<span class="hljs-number">26</span>条请求完成, 耗时<span class="hljs-number">19400</span>毫秒
第<span class="hljs-number">27</span>条请求完成, 耗时<span class="hljs-number">20333</span>毫秒
第<span class="hljs-number">17</span>条请求完成, 耗时<span class="hljs-number">21199</span>毫秒
第<span class="hljs-number">20</span>条请求完成, 耗时<span class="hljs-number">22080</span>毫秒
第<span class="hljs-number">19</span>条请求完成, 耗时<span class="hljs-number">23064</span>毫秒
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但如果在处理过程中不断有 await 形成时间片, 可供 Node 调度. 则 Node 服务仍然遵循异步模型规律, 所有请求一起返回(一起超时)</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">"koa"</span>);
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncCPUSleep</span>(<span class="hljs-params">ms = <span class="hljs-number">0</span></span>) </span>&#123;
  <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">1500000</span> * ms; i++) &#123;&#125;
      reslove(<span class="hljs-literal">true</span>);
    &#125;, <span class="hljs-number">0</span>);
  &#125;);
  <span class="hljs-keyword">return</span>;
&#125;

app.use(<span class="hljs-keyword">async</span> (ctx) => &#123;
  <span class="hljs-comment">// 切片式休眠1秒</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">100</span>; i++) &#123;
    <span class="hljs-keyword">await</span> asyncCPUSleep(<span class="hljs-number">10</span>);
  &#125;
  ctx.body = <span class="hljs-string">"Hello Koa"</span>;
&#125;);

app.listen(<span class="hljs-number">3000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 异步模式对应日志</span>
第<span class="hljs-number">0</span>条请求完成, 耗时<span class="hljs-number">27696</span>毫秒
第<span class="hljs-number">1</span>条请求完成, 耗时<span class="hljs-number">27701</span>毫秒
第<span class="hljs-number">2</span>条请求完成, 耗时<span class="hljs-number">27711</span>毫秒
第<span class="hljs-number">3</span>条请求完成, 耗时<span class="hljs-number">27721</span>毫秒
第<span class="hljs-number">4</span>条请求完成, 耗时<span class="hljs-number">27731</span>毫秒
第<span class="hljs-number">5</span>条请求完成, 耗时<span class="hljs-number">27741</span>毫秒
第<span class="hljs-number">6</span>条请求完成, 耗时<span class="hljs-number">27751</span>毫秒
第<span class="hljs-number">7</span>条请求完成, 耗时<span class="hljs-number">27760</span>毫秒
第<span class="hljs-number">8</span>条请求完成, 耗时<span class="hljs-number">27770</span>毫秒
第<span class="hljs-number">9</span>条请求完成, 耗时<span class="hljs-number">27780</span>毫秒
第<span class="hljs-number">10</span>条请求完成, 耗时<span class="hljs-number">27790</span>毫秒
第<span class="hljs-number">11</span>条请求完成, 耗时<span class="hljs-number">27799</span>毫秒
第<span class="hljs-number">12</span>条请求完成, 耗时<span class="hljs-number">27808</span>毫秒
第<span class="hljs-number">13</span>条请求完成, 耗时<span class="hljs-number">27818</span>毫秒
第<span class="hljs-number">14</span>条请求完成, 耗时<span class="hljs-number">27827</span>毫秒
第<span class="hljs-number">15</span>条请求完成, 耗时<span class="hljs-number">27837</span>毫秒
第<span class="hljs-number">16</span>条请求完成, 耗时<span class="hljs-number">27847</span>毫秒
第<span class="hljs-number">17</span>条请求完成, 耗时<span class="hljs-number">27857</span>毫秒
第<span class="hljs-number">18</span>条请求完成, 耗时<span class="hljs-number">27866</span>毫秒
第<span class="hljs-number">19</span>条请求完成, 耗时<span class="hljs-number">27875</span>毫秒
第<span class="hljs-number">20</span>条请求完成, 耗时<span class="hljs-number">27885</span>毫秒
第<span class="hljs-number">21</span>条请求完成, 耗时<span class="hljs-number">27895</span>毫秒
第<span class="hljs-number">22</span>条请求完成, 耗时<span class="hljs-number">27905</span>毫秒
第<span class="hljs-number">23</span>条请求完成, 耗时<span class="hljs-number">27917</span>毫秒
第<span class="hljs-number">24</span>条请求完成, 耗时<span class="hljs-number">27927</span>毫秒
第<span class="hljs-number">25</span>条请求完成, 耗时<span class="hljs-number">27937</span>毫秒
第<span class="hljs-number">26</span>条请求完成, 耗时<span class="hljs-number">27946</span>毫秒
第<span class="hljs-number">27</span>条请求完成, 耗时<span class="hljs-number">27957</span>毫秒
第<span class="hljs-number">28</span>条请求完成, 耗时<span class="hljs-number">27963</span>毫秒
第<span class="hljs-number">29</span>条请求完成, 耗时<span class="hljs-number">27973</span>毫秒
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般而言, 由于 web 接口中总有需要 await 的地方(动态文件路由/远程接口调用/MySQL 查询/中间件处理/接口返回/etc), 所以不会出现纯计算密集型的现象, 基本上是...一起超时, 一起报警.</p>
<h1 data-id="heading-8">后续</h1>
<p>了解异步模型的这个特征后, 服务器突发的 504 报警的原因就很清楚了. 由于线上服务器流量过大, CPU 性能成为接口瓶颈(稳定在 20%~30%, 相当于在临界点徘徊), 导致当 QPS 提升时接口超时, Nginx 自动返回 504. 实际上, 在这次故障期间, 每一个请求 Node 最后都有响应, 只是响应时间非常长, 有一个请求的响应时长甚至达到了 118.36 秒. 这也是为什么只有 Nginix 日志有 504 记录, 服务器日志全部都是 200 的原因.</p>
<p>发现问题后第一时间向运维申请增加了服务器, 后来也给常用计算逻辑添加了 redis 缓存, 将 CPU 负载由 15%~25% 降低到了 4%~5%, 从而解决了这个问题.</p>
<p>事实上, 由于存在<code>单个请求必要CPU时间</code>, 在<strong>保证每个请求响应时间可接受</strong>的前提下, 实际业务 Node 很难打到很高的 QPS 值, 一般的 SSR 服务也只有 50 左右. 对于高并发情况, 常见的解决方案一般是以下几种</p>
<ul>
<li>启动集群模式(cluster). 在默认状态下, 单进程只能使用 CPU 的一个核, 这样导致服务器上其他的 31/63 个核事实上被浪费了. 启动集群模式后, Node 服务的 QPS 值大致扩张为单进程状态下 QPS * 系统核心数, 基本可以满足线上服务需要
<ul>
<li>PS: 这实际上是 php-fpm 的做法, 所有请求来到 Nginx 后进行负载均衡, 将请求分散到后端的 32 个进程上, 虽然每个进程的 QPS 只有 30, 但由于进程总数大, 最后的 QPS 仍然有 900~1000</li>
</ul>
</li>
<li>缓存运算结果, 将计算结果存在 redis/memcache</li>
<li>优化代码逻辑, 避免冗余运算</li>
<li>加机器.</li>
</ul>
<p>但一般来说, 如果发现 CPU 使用率飙升, 接口响应时间随着并发量快速增长且隐隐有突破 1 秒的趋势时, 不用考虑太多, 加机器吧.</p>
<blockquote>
<p>程序员的时间比计算机的时间更宝贵</p>
<p>---- 编程人生, 第五章, Joshua Bloch</p>
</blockquote>
<h1 data-id="heading-9">附注</h1>
<ol>
<li>高 QPS 的响应时间问题只对高计算量的 Node 服务有意义. 这次服务故障是因为使用了 ORM 对数据进行反复建模浪费了大量计算性能, SSR 的 QPS 低是因为要在服务器上完成本应由浏览器完成的 js 处理逻辑. 但如果只进行后台服务转发, io 时长(远端接口响应时长)远大于自身计算时长, 这是最适合 Node 使用的业务场景, 一般不需要担心 QPS 问题.</li>
<li>文中进行的计算密集型/io 密集型压力测试结果如下
<ul>
<li>计算密集型
<ul>
<li>计算密集型-并发 1
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a90088cda81746f0aa11a72b505cbc7c~tplv-k3u1fbpfcp-zoom-1.image" alt="计算密集型-并发1.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>计算密集型-并发 10
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acd750e4cb3f4850a660ec82e3db6182~tplv-k3u1fbpfcp-zoom-1.image" alt="计算密集型-并发10.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>计算密集型-并发 100
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6d16c1715f345839f0522712d6774ec~tplv-k3u1fbpfcp-zoom-1.image" alt="计算密集型-并发100.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>计算密集型-并发 400
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35660c071f10404c885bd5d320233d93~tplv-k3u1fbpfcp-zoom-1.image" alt="计算密集型-并发400.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
</li>
<li>io 密集型
<ul>
<li>io 密集型-并发 1
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/723e549f43894ef89252a61a0b9af342~tplv-k3u1fbpfcp-zoom-1.image" alt="io密集型-并发1.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>io 密集型-并发 10
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e265dd8573847739bda39c2920598d1~tplv-k3u1fbpfcp-zoom-1.image" alt="io密集型-并发10.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>io 密集型-并发 100
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0deafb3113540159b66ea871856f268~tplv-k3u1fbpfcp-zoom-1.image" alt="io密集型-并发100.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>io 密集型-并发 400
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/653ebb6e8413419aa0d1e1ed99cdd3f2~tplv-k3u1fbpfcp-zoom-1.image" alt="io密集型-并发400.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>io 密集型-并发 1000
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e83b770eba04ccb89c4eecce0df6633~tplv-k3u1fbpfcp-zoom-1.image" alt="io密集型-并发1000.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
</li>
</ul>
</li>
</ol>
<h1 data-id="heading-10">参考文章</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000039165643" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000039165643" ref="nofollow noopener noreferrer">深入理解 nodejs 的 HTTP 处理流程</a></p></div>  
</div>
            