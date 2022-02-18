
---
title: '主流的微服务API网关性能比较'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://www.jianshu.com/p/undefined'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://www.jianshu.com/p/undefined'
---

<div>   
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1075" data-height="766"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-a3a41e01dccfedeb" data-original-width="1075" data-original-height="766" data-original-format="image/png" data-original-filesize="334330" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>API Gateway示意图</p>
<p>API Gateway主要是为了解决微服务下调用、统一接入等问题。</p>
<p>用于实现API网关的技术有很多，大致分为这么几类：</p>
<ul>
<li><p>通用反向代理：Nginx、Haproxy、……</p></li>
<li><p>网络编程框架：Netty、Servlet、……</p></li>
<li><p>API网关框架：Spring Cloud Gateway、Zuul、Zuul2、……</p></li>
</ul>
<p>API网关最基本的功能就是反向代理，所以在对API网关做技术选型的时候需要着重考察其性能表现，本文对Nginx、Haproxy、Netty、Spring Cloud Gateway、Zuul2做了性能测试，测试代码可以在github获得。</p>
<h2>测试方法</h2>
<ul>
<li><p>准备了三台2CPU 4G内存的服务器，分别运行Tomcat、API Gateway、Gatling（压测工具）</p></li>
<li><p>先对Tomcat做压测，取Tomcat充分预热后的压测结果作为基准。压的是Tomcat自带的example：<code>/examples/jsp/jsp2/simpletag/book.jsp</code></p></li>
<li><p>在对Netty、Zuul2、Spring Cloud Gateway做压测时候也是先压个几轮做预热。</p></li>
<li><p>被测的API网关都没有添加额外业务，只做反向代理</p></li>
</ul>
<h2>吞吐量</h2>
<p>下图是吞吐量的情况，可以看到Netty、Nginx、Haproxy均比直压Tomcat低一点点，而Spring Cloud Gateway和Zuul2则要低得多。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="800" data-height="399"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-e04727723562fa67" data-original-width="800" data-original-height="399" data-original-format="image/png" data-original-filesize="63466" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>下面这张图可以更明显的看到吞吐量比较，Tomcat为100%因为它是基准值，Netty、Nginx、Haproxy的只比基准值低8%，而Spring Cloud Gateway和Zuul2则只是基准值的35%和34%（难兄难弟）。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="800" data-height="395"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-6abebed2670b93a2" data-original-width="800" data-original-height="395" data-original-format="image/png" data-original-filesize="58785" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h2>平均响应时间</h2>
<p>下图可以看到Netty、Nginx、Haproxy的平均响应时间与Tomcat差不多。但是Spring Cloud Gateway和Zuul2则是Tomcat的3倍多，不出所料。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="800" data-height="389"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-c43ed42079b389da" data-original-width="800" data-original-height="389" data-original-format="image/png" data-original-filesize="45422" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>下图同样是以Tomcat作为基准值的比较：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="800" data-height="390"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-61c6eb62a636ae6f" data-original-width="800" data-original-height="390" data-original-format="image/png" data-original-filesize="50208" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h2>响应时间分布</h2>
<p>光看平均响应时间是不够的，我们还得看P50、P90、P99、P99.9以及Max响应时间（可惜Gatling只能设置4个百分位，否则我还想看看P99.99的响应时间）。</p>
<blockquote>
<p>为何要观察P99.9的响应时间？光看P90不够吗？理由有两个：</p>
<p>1）观察P99、P99.9、P99.99的响应时间可以观察系统的在高压情况下的稳定性，如果这三个时间的增长比较平滑那么说明该系统在高压力情况下比较稳定，如果这个曲线非常陡峭则说明不稳定。</p>
<p>2）观察P99、P99.9、P99.99的响应时间能够帮助你估算用户体验。假设你有一个页面会发出5次请求，那么这5次请求均落在P90以内概率是多少？90%^5=59%，至少会经历一次 > P90响应时间的概率是 100%-59%=41%，如果你的P90=10s，那么就意味着用户有41%的概率会在加载页面的时候超过10s，是不是很惊人？如果你的P99=10s，那么用户只有5%的概率会在访问页面的时候超过10s。如果P99.9=10s，则有0.4%的概率。</p>
<p>关于如何正确测量系统可以看 “How NOT to Measure Latency” by Gil Tene</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="800" data-height="323"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-2898f390873ad489" data-original-width="800" data-original-height="323" data-original-format="image/png" data-original-filesize="68860" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>下面同样是把结果与Tomcat基准值做对比：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="800" data-height="251"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-a399880d21f79aab" data-original-width="800" data-original-height="251" data-original-format="image/png" data-original-filesize="60395" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>可以看到几个很有趣的现象：</p>
<ul>
<li><p>Haproxy、Nginx的P50、P90、P99、P99.9、Max都是逐渐递增的。</p></li>
<li><p>Netty的P50、P90、P99、P99.9是很平坦的，Max则为基准值的207%。</p></li>
<li><p>Spring Cloud Gateway和Zuul2则是相反的，它们的平面呈现下降趋势。Spring Cloud Gateway的Max甚至还比基准值低了一点点（94%），我相信这只是一个随机出现的数字，不要太在意。</p></li>
</ul>
<h2>结论</h2>
<p>Nginx、Haproxy、Netty三者的表现均很不错，其对于吞吐量和响应时间的性能损耗很低，可以忽略不计。</p>
<p>但是目前最为火热的Spring Cloud Gateway和Zuul2则表现得比较糟糕，因我没有写额外的业务逻辑这，可以推测这和它们的内置逻辑有关，那么大致有这么几种可能：</p>
<ol>
<li><p>内置逻辑比较多</p></li>
<li><p>内置逻辑算法存在问题，占用了太多CPU时间</p></li>
<li><p>内置逻辑存在阻塞</p></li>
<li><p>内置逻辑没有用正确姿势使用Netty（两者皆基于Netty）</p></li>
</ol>
<p>不管是上面的哪一种都需要再后续分析。</p>
<p>不过话说回来考虑选用那种作为API网关（的基础技术）不光要看性能，还要看：</p>
<ul>
<li><p>是否易于扩展自己的业务逻辑</p></li>
<li><p>API使用的便利性</p></li>
<li><p>代码的可维护性</p></li>
<li><p>文档是否齐全</p></li>
<li><p>...</p></li>
</ul>
<p>性能只是我们手里的一个筹码，当我们知道这个东西性能到底几何后，才可以与上面的这些做交换（trade-off）。比如Nginx和Haproxy的可扩展性很差，那么我们可以使用Netty。如果你觉得Netty的API太底层了太难用了，那么可以考虑Spring Cloud Gateway或Zuul2。前提是你知道你会失去多少性能。</p>
<blockquote>
<p>来源： <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000018838988" target="_blank">https://segmentfault.com/a/1190000018838988</a></p>
</blockquote>
<hr>
<ul>
<li><em>更多测试技术分享、学习资源以及一些其他福利可关注公众号：【Coding测试】获取：</em></li>
</ul>
  
</div>
            