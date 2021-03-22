
---
title: '老板让我写个 BUG！'
categories: 
    - 编程
    - 码农网
    - 最新

author: 码农网
comments: false
date: Mon, 17 Dec 2018 06:45:12 GMT
thumbnail: 'http://static.codeceo.com/images/2018/12/006tNbRwly1fy2t4bjv5bj318s0hgjv4.jpg'
---

<div>   
<h2 id="h1_1">前言</h2>
<p>标题没有看错，真的是让我写个 <code>bug</code>！</p>
<p>刚接到这个需求时我内心没有丝毫波澜，甚至还有点激动。这可是我特长啊；终于可以光明正大的写 <code>bug</code> 了。</p>
<p>先来看看具体是要干啥吧，其实主要就是要让一些负载很低的服务器额外消耗一些内存、CPU 等资源（至于背景就不多说了），让它的负载可以提高一些。</p>
<h2 id="h1_2">JVM 内存分配回顾</h2>
<p>于是我刷刷一把梭的就把代码写好了，大概如下：</p>
<p><img class="aligncenter size-full wp-image-56685" title="006tNbRwly1fy2t4bjv5bj318s0hgjv4" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy2t4bjv5bj318s0hgjv4.jpg" alt width="1612" height="628" referrerpolicy="no-referrer"></p>
<p>写完之后我就在想一个问题，代码中的 <code>mem</code> 对象在方法执行完之后会不会被立即回收呢？我想肯定会有一部分人认为就是在方法执行完之后回收。</p>
<p>我也正儿八经的去调研了下，问了一些朋友；果不其然确实有一部分认为是在方法执行完毕之后回收。</p>
<p>那事实情况如何呢？我做了一个试验。</p>
<p>我用以下的启动参数将刚才这个应用启动起来。</p>
<pre class="brush: java; gutter: true; first-line: 1">java -Djava.rmi.server.hostname=10.xx.xx.xx 
-Djava.security.policy=jstatd.all.policy 
-Dcom.sun.management.jmxremote.authenticate=false 
-Dcom.sun.management.jmxremote.ssl=false 
-Dcom.sun.management.jmxremote.port=8888  
-Xms4g -Xmx4g  -jar bug-0.0.1-SNAPSHOT.jar</pre>
<p>这样我就可以通过 JMX 端口远程连接到这个应用观察内存、GC 情况了。</p>
<p><img class="aligncenter size-full wp-image-56686" title="006tNbRwly1fy2xv0wnp8j30s80je405" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy2xv0wnp8j30s80je405.jpg" alt width="1016" height="698" referrerpolicy="no-referrer"></p>
<p>如果是方法执行完毕就回收 <code>mem</code> 对象，当我分配 <code>250M</code> 内存时；内存就会有一个明显的曲线，同时 GC 也会执行。</p>
<p><img class="aligncenter size-full wp-image-56687" title="006tNbRwly1fy2ykiyz7cj31gs0b0dhr" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy2ykiyz7cj31gs0b0dhr.jpg" alt width="1900" height="396" referrerpolicy="no-referrer"></p>
<p>这时观察内存曲线。</p>
<p><img class="aligncenter size-full wp-image-56688" title="006tNbRwly1fy2y2psuhzj318c0oatbp" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy2y2psuhzj318c0oatbp.jpg" alt width="1596" height="874" referrerpolicy="no-referrer"></p>
<p>会发现确实有明显的涨幅，但是之后并没有立即回收，而是一直保持在这个水位。同时左边的 GC 也没有任何的反应。</p>
<p>用 <code>jstat</code> 查看内存布局也是同样的情况。</p>
<p><img class="aligncenter size-full wp-image-56689" title="006tNbRwly1fy2ynuuog3j317i0f2e81" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy2ynuuog3j317i0f2e81.jpg" alt width="1566" height="542" referrerpolicy="no-referrer"></p>
<p>不管是 <code>YGC,FGC</code> 都没有，只是 Eden 区的使用占比有所增加，毕竟分配了 250M 内存嘛。</p>
<p>那怎样才会回收呢？</p>
<p>我再次分配了两个 250M 之后观察内存曲线。</p>
<p><img class="aligncenter size-full wp-image-56690" title="006tNbRwly1fy2z2yxof0j30n60buab4" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy2z2yxof0j30n60buab4.jpg" alt width="834" height="426" referrerpolicy="no-referrer"></p>
<p><img class="aligncenter size-full wp-image-56691" title="006tNbRwly1fy2z7i5qrdj316m0eeb29" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy2z7i5qrdj316m0eeb29.jpg" alt width="1534" height="518" referrerpolicy="no-referrer"></p>
<p>发现第三个 250M 的时候 <code>Eden</code> 区达到了 <code>98.83%</code> 于是再次分配时就需要回收 <code>Eden</code> 区产生了 <code>YGC</code>。</p>
<p>同时内存曲线也得到了下降。</p>
<p>整个的换算过程如图：</p>
<p><img class="aligncenter size-full wp-image-56692" title="006tNbRwly1fy2zn03yjoj30sy0mg4qp" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy2zn03yjoj30sy0mg4qp.jpg" alt width="1042" height="808" referrerpolicy="no-referrer"></p>
<p>由于初始化的堆内存为 <code>4G</code>，所以算出来的 <code>Eden</code> 区大概为 <code>1092M</code> 内存。</p>
<p>加上应用启动 <code>Spring</code> 之类消耗的大约 <code>20%</code> 内存，所以分配 3 次 250M 内存就会导致 <code>YGC</code>。</p>
<p>再来回顾下刚才的问题：</p>
<p><img class="aligncenter size-full wp-image-56685" title="006tNbRwly1fy2t4bjv5bj318s0hgjv4" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy2t4bjv5bj318s0hgjv4.jpg" alt width="1612" height="628" referrerpolicy="no-referrer"></p>
<p><code>mem</code> 对象既然在方法执行完毕后不会回收，那什么时候回收呢。</p>
<p>其实只要记住一点即可：对象都需要垃圾回收器发生 <code>GC</code> 时才能回收；不管这个对象是局部变量还是全局变量。</p>
<p>通过刚才的实验也发现了，当 <code>Eden</code> 区空间不足产生 <code>YGC</code> 时才会回收掉我们创建的 <code>mem</code> 对象。</p>
<p>但这里其实还有一个隐藏条件：那就是这个对象是局部变量。如果该对象是全局变量那依然不能被回收。</p>
<p>也就是我们常说的对象不可达，这样不可达的对象在 <code>GC</code> 发生时就会被认为是需要回收的对象从而进行回收。</p>
<p>在多考虑下，为什么有些人会认为方法执行完毕后局部变量会被回收呢？</p>
<p>我想这应当是记混了，其实方法执行完毕后回收的是<code>栈帧</code>。</p>
<p>它最直接的结果就是导致 <code>mem</code> 这个对象没有被引用了。但没有引用并不代表会被马上回收，也就是上面说到的需要产生 <code>GC</code> 才会回收。</p>
<p>所以使用的是上面提到的对象不可达所采用的可达性分析算法来表明哪些对象需要被回收。</p>
<p>当对象没有被引用后也就认为不可达了。</p>
<p>这里有一张动图比较清晰：</p>
<p><img class="aligncenter size-full wp-image-56693" title="68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f342f34612f416e696d6174696f6e5f6f665f7468655f4e616976655f4d61726b5f616e645f53776565705f476172626167655f436f6c6c656374" src="http://static.codeceo.com/images/2018/12/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f342f34612f416e696d6174696f6e5f6f665f7468655f4e616976655f4d61726b5f616e645f53776565705f476172626167655f436f6c6c656374.gif" alt width="420" height="321" referrerpolicy="no-referrer"></p>
<p>当方法执行完之后其中的 <code>mem</code> 对象就相当于图中的 <code>Object 5</code>，所以在 <code>GC</code> 时候就会回收掉。</p>
<h3 id="h2_3">优先在 Eden 区分配对象</h3>
<p>其实从上面的例子中可以看出对象是优先分配在新生代中 Eden 区的，但有个前提就是对象不能太大。</p>
<p>以前也写过相关的内容：</p>
<p><img class="aligncenter size-full wp-image-56694" title="006tNbRwly1fy359itj30j30mn0ecjuh" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy359itj30j30mn0ecjuh.jpg" alt width="815" height="516" referrerpolicy="no-referrer"></p>
<h3 id="h2_4">大对象直接进入老年代</h3>
<p>而大对象则是直接分配到老年代中（至于多大算大，可以通过参数配置）。</p>
<p><img class="aligncenter size-full wp-image-56695" title="006tNbRwly1fy35t541v1j30qn06pjs4" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy35t541v1j30qn06pjs4.jpg" alt width="959" height="241" referrerpolicy="no-referrer"></p>
<p>当我直接分配 1000M 内存时，由于 Eden 区不能直接装下，所以改为分配在老年代中。</p>
<p><img class="aligncenter size-full wp-image-56696" title="006tNbRwly1fy35u96ercj309n03eaa5" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy35u96ercj309n03eaa5.jpg" alt width="347" height="122" referrerpolicy="no-referrer"></p>
<p><img class="aligncenter size-full wp-image-56697" title="006tNbRwly1fy37wlwaabj30lq09d4ax" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy37wlwaabj30lq09d4ax.jpg" alt width="782" height="337" referrerpolicy="no-referrer"></p>
<p>可以看到 <code>Eden</code> 区几乎没有变动，但是老年代却涨了 37% ，根据之前计算的老年代内存 <code>2730M</code> 算出来也差不多是 <code>1000M</code> 的内存。</p>
<h2 id="h1_5">Linux 内存查看</h2>
<p>回到这次我需要完成的需求：增加服务器内存和 CPU 的消耗。</p>
<p>CPU 还好，本身就有一定的使用，同时每创建一个对象也会消耗一些 CPU。</p>
<p><img class="aligncenter size-full wp-image-56698" title="006tNbRwly1fy35yw0qw9j309w04ewed" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy35yw0qw9j309w04ewed.jpg" alt width="356" height="158" referrerpolicy="no-referrer"></p>
<p>主要是内存,先来看下没启动这个应用之前的内存情况。</p>
<p><img class="aligncenter size-full wp-image-56699" title="006tNbRwly1fy3638jhdvj30lh02s422" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy3638jhdvj30lh02s422.jpg" alt width="773" height="100" referrerpolicy="no-referrer"></p>
<p>大概只使用了 3G 的内存。</p>
<p>启动应用之后大概只消耗了 600M 左右的内存。</p>
<p><img class="aligncenter size-full wp-image-56700" title="006tNbRwly1fy364kujo3j30ly05zjz6" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy364kujo3j30ly05zjz6.jpg" alt width="790" height="215" referrerpolicy="no-referrer"></p>
<p>为了满足需求我需要分配一些内存，但这里有点需要讲究。</p>
<p>不能一直分配内存，这样会导致 CPU 负载太高了，同时内存也会由于 GC 回收导致占用也不是特别多。</p>
<p>所以我需要少量的分配，让大多数对象在新生代中，为了不被回收需要保持在百分之八九十。</p>
<p>同时也需要分配一些大对象到老年代中，也要保持老年代的使用在百分之八九十。</p>
<p>这样才能最大限度的利用这 4G 的堆内存。</p>
<p>于是我做了以下操作：</p>
<ul>
<li>先分配一些小对象在新生代中（800M）保持新生代在90%</li>
<li>接着又分配了<code>老年代内 *（100%-已使用的28%）；也就是 2730*60%=1638M</code> 让老年代也在 90% 左右。</li>
</ul>
<p><img class="aligncenter size-full wp-image-56701" title="006tNbRwly1fy36g355cbj30av04wglr" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy36g355cbj30av04wglr.jpg" alt width="391" height="176" referrerpolicy="no-referrer"></p>
<p><img class="aligncenter size-full wp-image-56702" title="006tNbRwly1fy36jxum8kj30o20b4wvb" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy36jxum8kj30o20b4wvb.jpg" alt width="866" height="400" referrerpolicy="no-referrer"></p>
<p>效果如上。</p>
<p>最主要的是一次 <code>GC</code> 都没有发生这样也就达到了我的目的。</p>
<p>最终内存消耗了 3.5G 左右。</p>
<p><img class="aligncenter size-full wp-image-56703" title="006tNbRwly1fy36kw89b5j30mq08m4ae" src="http://static.codeceo.com/images/2018/12/006tNbRwly1fy36kw89b5j30mq08m4ae.jpg" alt width="818" height="310" referrerpolicy="no-referrer"></p>
<h2 id="h1_6">总结</h2>
<p>虽说这次的需求是比较奇葩，但想要精确的控制 <code>JVM</code> 的内存分配还是没那么容易。</p>
<p>需要对它的内存布局，回收都要有一定的了解，写这个 Bug 的过程确实也加深了印象，如果对你有所帮助请不要吝啬你的点赞与分享。</p>


<a id="soft-link" name="soft-link" href="http://www.codeceo.com/article/undefined"></a>




<!--开源软件资源链接-->
<!--开源软件资源链接结束-->







  
</div>
            