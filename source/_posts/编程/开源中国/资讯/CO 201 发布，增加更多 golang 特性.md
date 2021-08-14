
---
title: 'CO 2.0.1 发布，增加更多 golang 特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4499'
author: 开源中国
comments: false
date: Fri, 13 Aug 2021 19:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4499'
---

<div>   
<div class="content">
                                                                                            <h3><strong>GitHub</strong></h3> 
<div>
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fidealvin%2Fco" target="_blank">https://github.com/idealvin/co</a>
</div> 
<h3><strong>参考文档</strong></h3> 
<ul> 
 <li> <p><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">中文: </span><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#032f62">[</span><u>github</u><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#032f62">]</span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">(https://idealvin.github.io/cn/about/co/) </span><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#032f62">[</span><u>gitee</u><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#032f62">]</span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">(https://idealvin.gitee.io/cn/about/co/)</span></p> </li> 
 <li> <p><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">English: </span><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#032f62">[</span><u>github</u><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#032f62">]</span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">(https://idealvin.github.io/en/about/co/) </span><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#032f62">[</span><u>gitee</u><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#032f62">]</span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">(https://idealvin.gitee.io/en/about/co/)</span></p> </li> 
</ul> 
<h3><strong>新特性</strong></h3> 
<ul> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">xrepo</span></li> 
</ul> 
<div> 
 <pre><code>sh
xrepo install -f "openssl=true,libcurl=true" co</code></pre> 
 <p> </p> 
</div> 
<ul> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">vcpkg</span></li> 
</ul> 
<div> 
 <pre><code>sh
vcpkg install co:x64-windows
 
# http & ssl support
vcpkg install co[libcurl,openssl]:x64-windows
</code></pre> 
 <p> </p> 
</div> 
<ul> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">defer (类似于 golang 中的 defer)</span></li> 
</ul> 
<div> 
 <pre><code>cpp
#include "co/defer.h"
Timer t;
defer(LOG << "time elapse: " << t.us() << "us");</code></pre> 
 <p> </p> 
</div> 
<ul> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">channel (类似于 golang 中的 channel)</span></li> 
</ul> 
<div> 
 <pre><code>cpp
#include "co/co.h"
 
DEF_main(argc, argv) &#123;
    co::Chan<int> ch;
    go([ch]() &#123;
        ch << 7;
    &#125;);
 
    int v = 0;
    ch >> v;
    LOG << "v: "<< v;
 
    return 0;
&#125;</code></pre> 
 <p> </p> 
</div> 
<ul> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">waitgroup (类似于 golang 中的 sync.WaitGroup)</span></li> 
</ul> 
<div> 
 <pre><code>cpp
#include "co/co.h"
 
DEF_main(argc, argv) &#123;
    FLG_cout = true;
 
    co::WaitGroup wg;
    wg.add(8);
 
    for (int i = 0; i <8; ++i) &#123;
        go([wg]() &#123;
            LOG << "co: "<< co::coroutine_id();
            wg.done();
        &#125;);
    &#125;
 
    wg.wait();
    return 0;
&#125;</code></pre> 
 <p> </p> 
</div> 
<ul> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">协程在 windows 平台支持 hook。</span></li> 
</ul> 
<div> 
 <ul> 
  <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">在指定调度线程中创建协程。</span></li> 
 </ul> 
 <pre><code>cpp
auto s = co::next_scheduler();
s->go(f1);
s->go(f2);
</code></pre> 
</div> 
<div> 
 <ul> 
  <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">在所有调度线程中创建协程。</span></li> 
 </ul> 
 <pre><code>cpp
auto& s = co::all_schedulers();
for (size_t i = 0; i <s.size(); ++i) &#123;
    s[i]->go(f);
&#125;
</code></pre> 
</div> 
<ul> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">增加 </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">`void flag::init(const fastring& path);`</span></li> 
</ul> 
<h3><strong>改变</strong></h3> 
<ul> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">全局的 </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">`Closure`</span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e"> 改为 </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">`co::Closure`</span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">.</span></li> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">改进 </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">`co::Event`</span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">, 可以在协程及非协程中使用, 支持拷贝构造、lambda 中按值捕获.</span></li> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">改进 </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">`co::Mutex`</span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">, </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">`co::Pool`</span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">, 支持拷贝构造、lambda 中按值捕获.</span></li> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">改进 </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">`co::close()`</span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">, 可以在任何地方调用.</span></li> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">部分支持 mingw, 协程相关特性暂时不能在 mingw 上运行.</span></li> 
</ul> 
<h3><strong>问题修复</strong></h3> 
<ul> 
 <li> <span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">修复 </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">`fs::file`</span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e"> 读写超过 4G 长度数据的 bug.</span></li> 
 <li> <span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">修复 http::Client 连接超时时的错误信息.</span></li> 
 <li> <span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e">修复 #165 中的链接问题.</span></li> 
</ul>
                                        </div>
                                      
</div>
            