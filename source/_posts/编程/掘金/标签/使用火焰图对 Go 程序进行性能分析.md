
---
title: '使用火焰图对 Go 程序进行性能分析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24a67ad9d6bb4594ad25fbee018a0d9b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 09:10:55 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24a67ad9d6bb4594ad25fbee018a0d9b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
</blockquote>
<p>软件工程中，系统上线之后，仍需要持续对系统进行优化或者重构。</p>
<p>学会对应用系统进行运行时数据采集与性能分析是软件工程实践常用的基本技能。通常使用 <code>profile</code> 表示性能分析与采集，或者使用 profiling 代表性能分析这个行为。比如 Java 语言中相关的工具为 <code>jprofiler</code>，意为 Java Profiler。</p>
<p>Go 语言非常注重性能，其内置库里就自带了性能分析库  pprof。pprof 有两个包用来分析程序： runtime/pprof 与 net/http/pprof，其中 net/http/pprof 只是对 runtime/pprof 包进行封装并用 http 暴露出来。runtime/pprof 用于对普通的应用程序进行性能分析，主要用于可结束的代码块，比如一次函数调用；而 net/http/pprof 专门用于对后台服务型程序的性能采集与分析。</p>
<p>本小节将会介绍如何基于 pprof 进行性能分析与优化，包括 CPU 、内存占用、Block 阻塞以及 Goroutine 使用等方面。除此之外，还会介绍更加直观的图形工具：火焰图，基于 go-torch 将 pprof 的结果转换成火焰图。</p>
<h3 data-id="heading-0">普通应用程序的性能分析</h3>
<p>我们已经知道，runtime/pprof 用于对普通的应用程序进行性能分析，主要用于可结束的代码块。因此，我们下面通过案例来实践。</p>
<h4 data-id="heading-1">计算圆周率</h4>
<p>笔者选取的案例是计算圆周率的算法。</p>
<blockquote>
<p>众所周知，可以说，它是世界上最有名的无理常数了，代表的是一个圆的周长与直径之比或称为“圆周率”。公元前 250 年左右，阿基米德给出了“圆周率”的估计值在  223/71~22/7 之间。</p>
</blockquote>
<p>中国南北朝时期的著名数学家祖冲之(429-500)首次将“圆周率”精算到小数第七位，即在 3.1415926 至 3.1415927 之间，他提出的“密率与约率”对数学的研究有重大贡献。直到 15 世纪，阿拉伯数学家阿尔·卡西才以“精确到小数点后17位”打破了这一纪录。<br>
代表“圆周率”的字母是第十六个希腊字母的小写。也是希腊语 περιφρεια（表示周边，地域，圆周）的首字母。1706 年英国数学家威廉·琼斯(William Jones, 1675-1749)最先使用“π”来表示圆周率。1736 年，瑞士数学家欧拉(Leonhard Euler, 1707-1783)也开始用表示圆周率。从此，便成了圆周率的代名词。</p>
<p>通常的计算方法有如下几种：</p>
<ul>
<li>蒙特卡罗法；</li>
<li>正方形逼近；</li>
<li>迭代法；</li>
<li>丘德诺夫斯基公式</li>
</ul>
<h4 data-id="heading-2">测试代码的实现</h4>
<p>笔者这里采用蒙特卡罗方法计算圆周率，大致思路如下：</p>
<blockquote>
<p>正方形内部有一个相切的圆，它们的面积之比是π/4。</p>
</blockquote>
<p>在这个正方形内部，随机产生10000个点（即10000个坐标对 (x, y)），计算它们与中心点的距离，从而判断是否落在圆的内部。
如果这些点均匀分布，那么圆内的点应该占到所有点的 π/4，因此将这个比值乘以4，就是π的值。通过随机模拟30000个点，π的估算值与真实值相差0.07%。</p>
<p>最后，实现的完整代码如下所示：</p>
<pre><code class="copyable">package main

import (
"flag"
"fmt"
"log"
"os"
"runtime"
"runtime/pprof"
"time"
)

var n int64 = 10000000000
var h float64 = 1.0 / float64(n)

func f(a float64) float64 &#123;
return 4.0 / (1.0 + a*a)
&#125;

func chunk(start, end int64, c chan float64) &#123;
var sum float64 = 0.0
for i := start; i < end; i++ &#123;
x := h * (float64(i) + 0.5)
sum += f(x)
&#125;
c <- sum * h
&#125;

func main() &#123;
var cpuProfile = flag.String("cpuprofile", "", "write cpu profile to file")
var memProfile = flag.String("memprofile", "", "write mem profile to file")
flag.Parse()
//采样cpu运行状态
if *cpuProfile != "" &#123;
f, err := os.Create(*cpuProfile)
if err != nil &#123;
log.Fatal(err)
&#125;
pprof.StartCPUProfile(f)
defer pprof.StopCPUProfile()
&#125;
//记录开始时间
start := time.Now()

var pi float64
np := runtime.NumCPU()
runtime.GOMAXPROCS(np)
c := make(chan float64, np)
fmt.Println("np: ", np)

for i := 0; i < np; i++ &#123;
    //利用多处理器，并发处理
go chunk(int64(i)*n/int64(np), (int64(i)+1)*n/int64(np), c)
&#125;

for i := 0; i < np; i++ &#123;
tmp := <-c
fmt.Println("c->: ", tmp)

pi += tmp
fmt.Println("pai: ", pi)

&#125;

fmt.Println("Pi: ", pi)

//记录结束时间
end := time.Now()

//输出执行时间，单位为毫秒。
fmt.Printf("spend time: %vs\n", end.Sub(start).Seconds())
//采样 memory 状态
if *memProfile != "" &#123;
f, err := os.Create(*memProfile)
if err != nil &#123;
log.Fatal(err)
&#125;
pprof.WriteHeapProfile(f)
f.Close()
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上就是计算 π 的算法，基于 go 语言的 goroutine和 channel，充分利用多核处理器，提高 CPU 资源计算的速度。</p>
<p>我们在依赖中引入了 runtime/pprof，在实现的代码中添加了相关的 CPU Profiling 和 Memory Profiling 代码就可以实现 CPU 和内存的性能评测。</p>
<h4 data-id="heading-3">编译与执行</h4>
<p>接着就是编译获得可执行文件，执行后获得 pprof 的采样数据，然后就可以利用相关工具进行分析。相关的命令如下：</p>
<pre><code class="copyable">$ go build  -o pai main.go
$ ./pai --cpuprofile=cpu.pprof
$ ./pai --memprofile=mem.pprof

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的命令依次生成了 cpu.pprof 和 mem.pprof 两个采样文件，我们使用 <code>go tool pprof</code>  命令进行分析：</p>
<pre><code class="copyable">$ go tool pprof cpu.pprof
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行完上述命令即进入 pprof 命令行交互模式。pprof 支持多个指令，比如 top 用于显示 pprof 文件中的前 10 项数据，可以通过top 20等方式显示20行数据；其他的指令如 list，pdf、eog 等。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24a67ad9d6bb4594ad25fbee018a0d9b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中，其他的一些参数解释如下：</p>
<ul>
<li>Duration：程序执行时间。多核执行程序，总计耗时 13.47s，而采样时间为 24.44s；每个核均分采样时间。</li>
<li>flat/flat%：分别表示在当前层级 CPU 的占用时间和百分比。</li>
<li>cum/cum%：分别表示截止到当前层级累积的 CPU 时间和占比。</li>
<li>sum%：所有层级的 CPU 时间累积占用，从小到大一直累积到100%，即 24.44s。</li>
</ul>
<p>本例中，main.chunk 在当前层级占用 CPU 时间 21.86s，占比本次采集时间的 89.44%。而该函数累积占用时间 24.44s，占本次采集时间的 100%。通过 cum 数据可以看到，chunk 函数的 CPU 占用时间最多。</p>
<p>上图很清楚的说明了应用程序耗时的主要函数，接着就利用 list 命令查看占用的主要因素。list 命令根据你的正则表达式输出相关的方法，直接跟可选项 -o 会输出所有的方法，也可以指定方法名。这样就能查看匹配函数的代码以及每行代码的耗时：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb0ade46b1ba4ddfb292454e80dbeadc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上图可以看出，在第 24 行调用函数 f(x) 还额外花了 2.58s，每一行代码花费的时间都有显示出来，根据这些信息可以开展代码的优化。</p>
<h4 data-id="heading-4">图形化渲染</h4>
<p>对于 pprof 采集的结果，我们不仅可以使用 pprof 自带的命令进行分析，还可以通过更加直观的矢量图进行分析。借助于 graphviz，pprof 可以直接生成对应的图像化文件。</p>
<p>笔试基于 Centos 7.5 系统，通过如下的命令直接安装 graphviz：</p>
<pre><code class="copyable">$ sudo yum install graphviz
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多系统环境的安装说明，请参见 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.graphviz.org%2Fdownload%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.graphviz.org/download/" ref="nofollow noopener noreferrer">graphviz 官网</a></p>
<p>安装好 graphviz，继续在 pprof 交互命令行中输入 svg：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d931e0bef2246c2a297099c26fea433~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意 web 命令在服务器类型的系统不支持，通过 svg 命令来生成矢量图，使用浏览器打开，如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9dfe7e098e14cc4962a3a3f1a17e178~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>笔者截取了部分内容，从上图同样可以看到，主要耗时的函数为 main.chunk，耗时时间为 21.86s，关联调用的函数 f(x) 耗时为 2.58s。图中各个方块的大小也代表 CPU 占用的情况，方块越大说明占用 CPU 时间越长。</p>
<h3 data-id="heading-5">后台服务程序的性能分析</h3>
<p>针对一直运行的后台服务，比如 web 应用或者分布式应用，我们可以使用 net/http/pprof 库，它能够在应用提供 HTTP 服务时进行分析。</p>
<p>pprof 采集后台服务，如果使用了默认的 http.DefaultServeMux，通常是代码直接使用 http.ListenAndServe("0.0.0.0:8000", nil)，这种情况则比较简单，只需要导入包即可。</p>
<pre><code class="copyable">import (
_ "net/http/pprof"
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意该包利用下划线"_"导入，意味着我们只需要该包运行其init()函数即可，如此该包将自动完成信息采集并保存在内存中。</p>
<p>如果你使用自定义的 ServerMux复用器，则需要手动注册一些路由规则：</p>
<pre><code class="hljs language-go copyable" lang="go">r.HandleFunc(<span class="hljs-string">"/debug/pprof/"</span>, pprof.Index)
r.HandleFunc(<span class="hljs-string">"/debug/pprof/heap"</span>, pprof.Index)
r.HandleFunc(<span class="hljs-string">"/debug/pprof/cmdline"</span>, pprof.Cmdline)
r.HandleFunc(<span class="hljs-string">"/debug/pprof/profile"</span>, pprof.Profile)
r.HandleFunc(<span class="hljs-string">"/debug/pprof/symbol"</span>, pprof.Symbol)
r.HandleFunc(<span class="hljs-string">"/debug/pprof/trace"</span>, pprof.Trace)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些路径分别表示：</p>
<ul>
<li>/debug/pprof/profile：访问这个链接会自动进行 CPU profiling，持续 30s，并生成一个文件供下载，可以通过带参数?=seconds=60进行60秒的数据采集。</li>
<li>/debug/pprof/block：Goroutine阻塞事件的记录。默认每发生一次阻塞事件时取样一次。</li>
<li>/debug/pprof/goroutines：活跃Goroutine的信息的记录。仅在获取时取样一次。</li>
<li>/debug/pprof/heap： 堆内存分配情况的记录。默认每分配512K字节时取样一次。</li>
<li>/debug/pprof/mutex: 查看争用互斥锁的持有者。</li>
<li>/debug/pprof/threadcreate: 系统线程创建情况的记录。 仅在获取时取样一次。</li>
</ul>
<h4 data-id="heading-6">改写测试代码</h4>
<p>将计算圆周率的程序改写成一个服务，对外提供一个接口，并引入 net/http/pprof 依赖，来采集 HTTP 服务的性能指标。</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">package</span> main

<span class="hljs-keyword">import</span> (
<span class="hljs-string">"fmt"</span>
<span class="hljs-string">"net/http"</span>
_ <span class="hljs-string">"net/http/pprof"</span>
<span class="hljs-string">"runtime"</span>
)

<span class="hljs-keyword">var</span> n <span class="hljs-keyword">int64</span> = <span class="hljs-number">10000000000</span>
<span class="hljs-keyword">var</span> h = <span class="hljs-number">1.0</span> / <span class="hljs-keyword">float64</span>(n)

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">f</span><span class="hljs-params">(a <span class="hljs-keyword">float64</span>)</span> <span class="hljs-title">float64</span></span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-number">4.0</span> / (<span class="hljs-number">1.0</span> + a*a)
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">chunk</span><span class="hljs-params">(start, end <span class="hljs-keyword">int64</span>, c <span class="hljs-keyword">chan</span> <span class="hljs-keyword">float64</span>)</span></span> &#123;
<span class="hljs-keyword">var</span> sum <span class="hljs-keyword">float64</span> = <span class="hljs-number">0.0</span>
<span class="hljs-keyword">for</span> i := start; i < end; i++ &#123;
x := h * (<span class="hljs-keyword">float64</span>(i) + <span class="hljs-number">0.5</span>)
sum += f(x)
&#125;
c <- sum * h
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">callFunc</span><span class="hljs-params">(w http.ResponseWriter, r *http.Request)</span></span> &#123;

<span class="hljs-keyword">var</span> pi <span class="hljs-keyword">float64</span>
np := runtime.NumCPU()
runtime.GOMAXPROCS(np)
c := <span class="hljs-built_in">make</span>(<span class="hljs-keyword">chan</span> <span class="hljs-keyword">float64</span>, np)
fmt.Println(<span class="hljs-string">"np: "</span>, np)

<span class="hljs-keyword">for</span> i := <span class="hljs-number">0</span>; i < np; i++ &#123;
<span class="hljs-keyword">go</span> chunk(<span class="hljs-keyword">int64</span>(i)*n/<span class="hljs-keyword">int64</span>(np), (<span class="hljs-keyword">int64</span>(i)+<span class="hljs-number">1</span>)*n/<span class="hljs-keyword">int64</span>(np), c)
&#125;

<span class="hljs-keyword">for</span> i := <span class="hljs-number">0</span>; i < np; i++ &#123;
tmp := <-c
fmt.Println(<span class="hljs-string">"c->: "</span>, tmp)

pi += tmp
fmt.Println(<span class="hljs-string">"pai: "</span>, pi)

&#125;

fmt.Println(<span class="hljs-string">"Pi: "</span>, pi)
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span> &#123;
http.HandleFunc(<span class="hljs-string">"/getAPi"</span>, callFunc)
http.ListenAndServe(<span class="hljs-string">":8000"</span>, <span class="hljs-literal">nil</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在上述代码的实现中，对外暴露了 8000 端口，并定义了一个接口 <code>getAPi</code>。计算圆周率的实现和之前相同，每次调用接口都将会触发计算 π 一次。</p>
<h4 data-id="heading-7">编译执行</h4>
<p>该写完代码，我们就可以进行编译和执行 HTTP 服务了，执行如下的命令：</p>
<pre><code class="copyable">$ go build -o httpapi main.go

$ ./httpapi
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将程序编译成功之后，运行二进制文件，可以获取服务的性能数据后，</p>
<p>此时，我们就可以通过 pprof 的 HTTP 接口访问 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8000%2Fdebug%2Fpprof%2F%25EF%25BC%259A" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8000/debug/pprof/%EF%BC%9A" ref="nofollow noopener noreferrer">http://localhost:8000/debug/pprof/：</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85ea14b22d8343c89496d298efb03840~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图展示了 pprof web 查看服务的运行情况，同时不断刷新网页可以发现采样结果也在不断更新。</p>
<h4 data-id="heading-8">图形化分析</h4>
<p>与上面可结束的程序进行性能分析一样，我们对于后台程序也可以使用图像化的方式分析性能。</p>
<p>接下来使用 go tool pprof 工具对这些数据进行分析和保存了，一般都是使用 pprof 通过 HTTP 访问上面列的那些路由端点直接获取到数据后再进行分析，获取到数据后 pprof 会自动让终端进入交互模式。</p>
<p>通过如下的命令查看内存 Memory 相关情况：</p>
<pre><code class="copyable">$ go tool pprof main http://localhost:8000/debug/pprof/heap
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e3cd4032ada4729bfe7c140d1a542bd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述命令采集内存信息，控制台输出了生成的图片名称：profile001.svg，默认在当前目录，当然我们也可以指定位置和文件名。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff1ef10a61a44203a7a6cfe4610a6ead~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于没有 http 请求的访问，因此内存的占用比较低，没有任何异常。下面我们将通过压测模拟线上情况，来分析在正常运行时的各项性能。</p>
<h3 data-id="heading-9">利用 go-torch 生成火焰图</h3>
<p>上面的小节介绍了 net/http/pprof 和 runtime/pprof 进行 Go 程序的性能分析。然而上面的案例仅仅只是采样了部分代码段。同时只有当有大量请求时才能看到应用服务的主要优化信息。这时候就需要借助于另一款 Uber 开源的火焰图工具 go-torch，以便辅助我们完成分析。要想实现火焰图的效果，需要安装如下 3 个工具：压测组件 wrk、FlameGraph 火焰图、go-torch 工具。下面将会依次介绍这三款组件的安装使用。</p>
<h4 data-id="heading-10">压测组件 wrk</h4>
<p>wrk 是一款针对 HTTP 协议的基准测试工具，它能够在单机多核 CPU 的条件下，使用系统自带的高性能 I/O 机制，如 epoll，kqueue 等，通过多线程和事件模式，对目标机器产生大量的负载。安装命令如下所示：</p>
<pre><code class="copyable">$ git clone https://github.com/brendangregg/FlameGraph.git
$ cd wrk/
$ make
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过如上的命令，我们就生成了可执行的 wrk 文件。其使用比较简单，主要参数说明如下：</p>
<ul>
<li>-c：总的连接数（每个线程处理的连接数=总连接数/线程数）</li>
<li>-d：测试的持续时间，如2s(2second)，2m(2minute)，2h(hour)</li>
<li>-t：需要执行的线程总数</li>
<li>-s：执行Lua脚本，这里写lua脚本的路径和名称，后面会给出案例</li>
<li>-H：需要添加的头信息，注意header的语法，举例，-H “token: abcdef”，说明一下，token，冒号，空格，abcdefg（不要忘记空格，否则会报错的）。</li>
</ul>
<p>笔者刚开始执行的压测参数如下：</p>
<pre><code class="copyable">./wrk -t5 -c10 -d120s http://localhost:8000/getAPi
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即 5 个线程并发，每秒保持 10 个连接，持续时间 120s。如果出现如下的错误，</p>
<pre><code class="copyable">unable to create thread 419: Too many open files
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是由于 /socket连接数量超过系统设定值，则需要调整每个用户最大允许打开文件数量。</p>
<pre><code class="copyable">$ ulimit -n 2048
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">FlameGraph 火焰图与 go-torch</h4>
<p>火焰图（flame graph）是性能分析的利器，通过它可以快速定位性能瓶颈点。在 Linux 服务器，一般配合 perf 一起使用。</p>
<p>go-torch 是 uber 开源的一个工具，可以直接读取 pprof的 profiling 数据，并生成一个火焰图的 svg 文件。火焰图 svg 文件可以通过浏览器打开，它对于调用图的优点是：可以通过点击每个方块来分析它上面的内容。</p>
<p>执行如下的命令进行安装：</p>
<pre><code class="copyable">$ git clone https://github.com/brendangregg/FlameGraph.git
$ go get github.com/uber/go-torch
<span class="copy-code-btn">复制代码</span></code></pre>
<p>go-torch 使用的命令如下：</p>
<pre><code class="copyable">$ go-torch -u http://localhost:8000 -t 100
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上的命令将会开启 go-torch 工具对 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8000" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8000" ref="nofollow noopener noreferrer">http://localhost:8000</a> 采集 100s 信息。</p>
<h4 data-id="heading-12">压测生成火焰图</h4>
<p>安装好上述三个组件之后，我们将会进行测试。首先是启动我们的应用服务：</p>
<pre><code class="copyable">$ ./httpapi
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着启动压测和 go-torch：</p>
<pre><code class="copyable">$ ./wrk -t5 -c10 -d120s http://localhost:8000/getAPi
$ go-torch -u http://localhost:8000 -t 100
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de2fb26728f2491e8a56c1052d20fc55~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b117e376577b4b5da55b8e4a862cb975~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，我们压测的请求，已经在服务端生成相应的火焰图：torch.svg。注：在 FlameGraph 目录下执行 go-torch，否则需将该二进制可执行文件的路径添加到系统环境变量。</p>
<p>打开火焰图，如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3b4f3c2ff0448cb9b0ff82297e01213~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>火焰图形似火焰，故此得名，其横轴是 CPU 占用时间，纵轴是调用顺序。火焰图的调用顺序从下到上，每个方块代表一个函数，它上面一层表示这个函数会调用哪些函数，方块的大小代表了占用 CPU 使用的长短。火焰图的配色并没有特殊的意义，默认的红、黄配色是为了更像火焰而已。</p>
<p>与我们上面所分析的结果是一样的，总体的耗时都在 chunk 函数。我们再来看一张没有请求访问时的火焰图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/883a375bac1e4c1082699d29e50850fb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，这种情况 CPU 占用时间和内存占用非常平稳，主要集中在提供 http 服务的库函数。</p>
<h3 data-id="heading-13">小结</h3>
<p>本文主要介绍了如何通过 pprof 对 Go 应用程序进行性能指标的采集以及性能分析。我们通过 pprof 获取到 CPU 和内存使用的细节，更进一步可以指导哪些函数耗时，函数之间的调用链。想更细致分析，就要精确到代码级别了，看看每行代码的耗时，直接定位到出现性能问题的那行代码。</p>
<p>结合 Uber 开源的 go-torch 生成火焰图，从全局来查看系统运行时的内存和 CPU，以及 Goroutines 和阻塞锁等情况，熟练使用性能分析的工具，能够帮助我们更快地定位线上问题并解决问题的 bug。</p>
<p>通过本文的讲解，你也了解到，开启后台程序的性能分析需要有请求，而不是静态的服务，本文使用的是压测来模拟大量的请求。当然在生产环境开启 pprof 也是需要考虑性能的开销，在上线前解决问题肯定是最好的选择。</p>
<p><strong>感谢你的耐心阅读，最后，需要你的点赞加油。</strong></p>
<p><strong>阅读最新文章，关注wechat公众号：aoho求索</strong></p></div>  
</div>
            