
---
title: 'C++ 基础库 co v2.0.0 正式发布 (协程库,网络编程,日志库,JSON..)'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9541'
author: 开源中国
comments: false
date: Sat, 29 May 2021 23:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9541'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fidealvin%2Fco" target="_blank">github.com/idealvin/co</a></p> 
<p style="text-align:start">co 是一个优雅、高效的 C++ 基础库，支持 Linux, Windows 与 Mac 平台，它包含协程库、网络库、日志库、命令行与配置文件解析库、单元测试框架、JSON 库等基本组件。</p> 
<p style="text-align:start">co 遵循极简的设计理念，提供的接口都尽可能简单明了，用户可以轻松上手。co 尽量避免过度封装，引入过多的概念，以减轻用户的学习负担，如 co 提供的协程化的 socket API，与原生 socket API 形式上基本一致，熟悉 socket 编程的用户，几乎不需要增加新的学习成本，就能轻松用这些 API 写出高性能的网络程序。</p> 
<h2 style="text-align:start">详细的参考文档</h2> 
<p style="text-align:start"><br> 首先特别强调的是，这次提供了更加详细的参考文档：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fwww.yuque.com%2Fidealvin%2Fco" target="_blank">中文 https://www.yuque.com/idealvin/co</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fwww.yuque.com%2Fidealvin%2Fco_en" target="_blank">English https://www.yuque.com/idealvin/co_en</a></li> 
</ul> 
<p style="text-align:start">这次直接将文档放到语雀上了，它的目录编排做得不错。有现成的平台，就直接拿来用了，懒得再去折腾个人网站啥的.. 大家可以去上面留言、提建议..<br>  </p> 
<h2 style="text-align:start">新特性</h2> 
<p style="text-align:start"> </p> 
<h3 style="text-align:start">SSL</h3> 
<p style="text-align:start"><br> co 2.0 终于支持 SSL 了，用户需要安装 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fopenssl%2Fopenssl" target="_blank">openssl 1.1</a> 以上的版本，目前已在 openssl 上测试通过，其他 SSL 库暂未测试。<br> <br> 推荐使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">xmake</a> 编译，它会提示用户是否安装 openssl, libcurl, zlib 等三方库。要启用 SSL 特性，需要预定义 <code>CO_SSL</code> 宏，xmake 在检测到 openssl 时会自动定义这个宏。<br> <br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fidealvin%2Fco%2Fblob%2Fmaster%2Finclude%2Fco%2Fso%2Fssl.h" target="_blank">co/so/ssl.h</a> 中提供了协程化的 openssl 接口，不过用户很可能不会直接使用它们，因为 co 已经将 SSL 功能内嵌到 TCP 模块中，用户可以直接使用 tcp::Server 与 tcp::Client。<br>  </p> 
<h2 style="text-align:start">重要改进</h2> 
<p style="text-align:start"> </p> 
<h3 style="text-align:start">协程</h3> 
<ul> 
 <li>go()<br> go() 支持任意带 0 个或 1 个参数的函数或类方法，以及 <code>std::function<void()></code> 类型的函数对象或指针。</li> 
</ul> 
<div style="text-align:start"> 
 <pre><code class="language-cpp"><span style="color:#175199">void</span> <span style="color:#f1403c">f</span>();
<span style="color:#175199">void</span> <span style="color:#f1403c">g</span>(<span style="color:#175199">int</span>);
<span style="color:#175199">void</span> <span style="color:#f1403c">h</span>(<span style="color:#175199">int</span>, <span style="color:#175199">int</span>);
struct <span style="color:#175199">T</span> &#123;
    <span style="color:#175199">void</span> <span style="color:#f1403c">f</span>();
    <span style="color:#175199">void</span> <span style="color:#f1403c">g</span>(<span style="color:#175199">int</span>);
&#125;;

T o;
std::function<<span style="color:#175199">void</span>()> k(std::bind(h, <span style="color:#0066ff">3</span>, <span style="color:#0066ff">7</span>));

go(f);
go(g, <span style="color:#0066ff">7</span>);
go(&T::f, &o);
go(&T::g, &o, <span style="color:#0066ff">3</span>);
go(k);
go(&k); <em>// The user must ensure that k is alive when the coroutine is running.
</em></code></pre> 
</div> 
<ul> 
 <li>协程 API 
  <ul> 
   <li>增加 co::timeout() 函数，用户可以用它判断上次调用的 co::recv(), co::send() 等 I/O 函数是否超时。</li> 
   <li>co::coroutine_id() 函数返回一个全局唯一的 id，1.x 版本中，不同调度线程中的协程可能有相同的 id。</li> 
  </ul> </li> 
</ul> 
<p style="text-align:start"> </p> 
<ul> 
 <li>co::Event<br> 内部增加 signaled 状态，解决没有协程等待的情况下，同步信号会丢失的问题。</li> 
</ul> 
<p> </p> 
<ul> 
 <li>co::IoEvent<br> 1.x 版本中仅在内部使用，2.0 中公开这个类，方便用户自行将三方网络库协程化。</li> 
</ul> 
<div style="text-align:start"> 
 <pre><code class="language-cpp"><span style="color:#175199">int</span> <span style="color:#f1403c">recv</span>(SSL* s, <span style="color:#175199">void</span>* buf, <span style="color:#175199">int</span> n, <span style="color:#175199">int</span> ms) &#123;
    CHECK(co::scheduler()) << <span style="color:#f1403c">"must be called in coroutine.."</span>;
    <span style="color:#175199">int</span> r, e;
    <span style="color:#175199">int</span> fd = SSL_get_fd(s);
    if (fd <<span style="color:#0066ff">0</span>) return -<span style="color:#0066ff">1</span>;

    do &#123;
        ERR_clear_error();
        r = SSL_read(s, buf, n);
        if (r> <span style="color:#0066ff">0</span>) return r; <em>// success
</em>        if (r == <span style="color:#0066ff">0</span>) &#123;
            DLOG << <span style="color:#f1403c">"SSL_read return 0, error: "</span><< SSL_get_error(s, <span style="color:#0066ff">0</span>);
            return <span style="color:#0066ff">0</span>;
        &#125;

        e = SSL_get_error(s, r);
        if (e == SSL_ERROR_WANT_READ) &#123;
            co::IoEvent ev(fd, co::EV_read);
            if (!ev.wait(ms)) return -<span style="color:#0066ff">1</span>;
        &#125; else if (e == SSL_ERROR_WANT_WRITE) &#123;
            co::IoEvent ev(fd, co::EV_write);
            if (!ev.wait(ms)) return -<span style="color:#0066ff">1</span>;
        &#125; else &#123;
            DLOG << <span style="color:#f1403c">"SSL_read return "</span><< r << <span style="color:#f1403c">", error:"</span> << e;
            return r;
        &#125;
    &#125; while (<span style="color:#0066ff">true</span>);
&#125;
</code></pre> 
</div> 
<ul> 
 <li>上面是将 openssl 中的 SSL_read() 函数协程化的例子，只需要使用 non-blocking socket，在 openssl 产生 SSL_ERROR_WANT_READ 或 SSL_ERROR_WANT_WRITE 错误时，调用 co::IoEvent 的 wait() 方法，等待相应的 I/O 事件即可。</li> 
</ul> 
<p style="text-align:start"> </p> 
<h3 style="text-align:start">TCP</h3> 
<ul> 
 <li>新增 tcp::Connection 类，用于 TCP server 的实现，该类提供了 recv(), send() 等方法，用户可以直接用该类接收、发送数据，而无需关心底层是否启用了 SSL。</li> 
 <li>tcp::Server</li> 
</ul> 
<div style="text-align:start"> 
 <pre><code class="language-cpp"><span style="color:#175199">void</span> <span style="color:#f1403c">on_connection</span>(tcp::Connection* conn);

tcp::Server s;
s.on_connection(on_connection);
s.start(<span style="color:#f1403c">"0.0.0.0"</span>, <span style="color:#0066ff">7788</span>);                                   <em>// no ssl
</em>s.start(<span style="color:#f1403c">"0.0.0.0"</span>, <span style="color:#0066ff">7788</span>, <span style="color:#f1403c">"privkey.pem"</span>, <span style="color:#f1403c">"certificate.pem"</span>); <em>// use ssl
</em></code></pre> 
</div> 
<p style="text-align:start"><br> tcp::Server 只需要在 start() 方法中指定 SSL private key 与证书文件，即可启用 SSL。</p> 
<ul> 
 <li>tcp::Client</li> 
</ul> 
<div style="text-align:start"> 
 <pre><code class="language-cpp"><span style="color:#175199">bool</span> use_ssl = <span style="color:#0066ff">false</span>;
tcp::Client c(<span style="color:#f1403c">"127.0.0.1"</span>, <span style="color:#0066ff">7788</span>, use_ssl);
c.connect(<span style="color:#0066ff">1000</span>);
c.send(...);
</code></pre> 
</div> 
<p style="text-align:start"><br> tcp::Client 可以通过构造函数的第 3 个参数启用 SSL。<br>  </p> 
<h3 style="text-align:start">HTTP</h3> 
<ul> 
 <li>http::Client<br> co 2.0 中，http::Client 基于 libcurl 实现，要启用此特性，必须安装 libcurl，并预定义 <code>HAS_LIBCURL</code> 宏。还是那句话，建议用 xmake 构建，它会自动搞定这些三方依赖。</li> 
</ul> 
<div style="text-align:start"> 
 <pre><code class="language-cpp">http::Client c(<span style="color:#f1403c">"https://github.com"</span>);
http::Client c(<span style="color:#f1403c">"http://127.0.0.1:7777"</span>);
c.get(<span style="color:#f1403c">"/"</span>);
c.get(<span style="color:#f1403c">"/idealvin/co"</span>);
LOG << c.response_code();
</code></pre> 
</div> 
<ul> 
 <li>http::Server<br> 基于 tcp::Server 实现，只要在 start() 方法中带上 SSL 私钥及证书文件，就能启用 SSL。</li> 
</ul> 
<div style="text-align:start"> 
 <pre><code class="language-cpp">http::Server s
s.on_req(...);
s.start(<span style="color:#f1403c">"0.0.0.0"</span>, <span style="color:#0066ff">7777</span>);                                    <em>// http
</em>s.start(<span style="color:#f1403c">"0.0.0.0"</span>, <span style="color:#0066ff">7777</span>, <span style="color:#f1403c">"privkey.pem"</span>, <span style="color:#f1403c">"certificate.pem"</span>);  <em>// https
</em></code></pre> 
</div> 
<p style="text-align:start"> </p> 
<h3 style="text-align:start">RPC</h3> 
<p style="text-align:start"><br> co 2.0 中，RPC 框架添加了一些新特性：</p> 
<ul> 
 <li>支持 SSL。</li> 
 <li>支持用户名与密码认证，RPC server 可以设置多个用户名、密码。</li> 
 <li>rpc::Server 可以添加多个 service。</li> 
 <li>RPC 代码生成器可以生成 RPC client 代码。</li> 
</ul> 
<p style="text-align:start"> </p> 
<h3 style="text-align:start">JSON</h3> 
<p style="text-align:start"><br> 1.x 版本中，JSON 库仅用一个 <code>json::Value</code> 类表示 JSON，JSON 对象中的元素也是 json::Value，构建 JSON 对象时需要为每个元素分配内存，JSON 对象析构时，内部所有元素都要调用 <code>json::Value</code> 的析构函数。基于这种方式的实现，会导致频繁的内存分配及释放操作，非常影响程序性能。<br> <br> co 2.0 中，将 JSON 对象构建到一块连续的内存上，程序运行稳定后，解析 JSON 几乎不需要内存分配操作，大大提高了 parsing 速度，实测可以达到 rapidjson 的两倍以上。<br> <br> 另外，co 2.0 用 <code>Json</code> 类表示 JSON 对象，<code>json::Value</code> 类表示 JSON 对象中的元素。<code>json::Value</code> 只是一个平凡类，仅包含它在 JSON 内存块中的索引位置。JSON 对象析构时，仅调用一次 Json 类的析构函数，而不会调用 json::Value 的析构函数。<br>  </p> 
<h2 style="text-align:start">其他</h2> 
<ul> 
 <li>修复 co/log 中的嵌套 log bug。</li> 
 <li>修复一些全局静态变量相互依赖引起的 bug。</li> 
 <li>co/log 日志时间增加毫秒。</li> 
 <li>TaskSched 类重命名为 Tasked。</li> 
 <li>co/time.h 新增 epoch::ms() 与 epoch::us()，用于获取自 EPOCH 开始的时间。</li> 
 <li>co/os.h 新增 os::signal() 方法，设置信号处理函数。</li> 
 <li>fastring 中新增 safe_clear() 方法。</li> 
 <li>Json 中新增 safe_clear() 方法。</li> 
</ul>
                                        </div>
                                      
</div>
            