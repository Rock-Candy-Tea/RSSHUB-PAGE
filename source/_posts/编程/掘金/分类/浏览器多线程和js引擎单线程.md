
---
title: '浏览器多线程和js引擎单线程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0609cdcc308b4efb82b9882f48d00afe~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 01 May 2021 19:09:57 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0609cdcc308b4efb82b9882f48d00afe~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a name="user-content-BtrOp" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-0">浏览器的线程和进程</h1>
<p><a name="user-content-Ul6fx" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-1">进程与线程</h2>
<p><a name="user-content-S0MYM" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-2">进程</h3>
<p>学术上说，进程是一个具有一定独立功能的程序在一个数据集上的一次动态执行的过程，是操作系统进行资源分配和调度的一个独立单位，是应用程序运行的载体。我们这里将进程比喻为工厂的车间，它代表CPU所能处理的单个任务。任一时刻，CPU总是运行一个进程，其他进程处于非运行状态。
<a name="user-content-zfdDp" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-3">线程</h3>
<p>在早期的操作系统中并没有线程的概念，进程是能拥有资源和独立运行的最小单位，也是程序执行的最小单位。</p>
<p>任务调度采用的是时间片轮转的抢占式调度方式，而进程是任务调度的最小单位，每个进程有各自独立的一块内存，使得各个进程之间内存地址相互隔离。</p>
<p>后来，随着计算机的发展，对CPU的要求越来越高，进程之间的切换开销较大，已经无法满足越来越复杂的程序的要求了。</p>
<p>于是就发明了线程，线程是程序执行中一个单一的顺序控制流程，是程序执行流的最小单元。这里把线程比喻一个车间的工人，即一个车间可以允许由多个工人协同完成一个任务。</p>
<p><a name="user-content-NRX2O" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-4">进程和线程的区别和关系</h3>
<ul>
<li>进程是操作系统分配资源的最小单位，线程是程序执行的最小单位。</li>
<li>一个进程由一个或多个线程组成，线程是一个进程中代码的不同执行路线；</li>
<li>进程之间相互独立，但同一进程下的各个线程之间共享程序的内存空间(包括代码段、数据集、堆等)及一些进程级的资源(如打开文件和信号)。</li>
<li>调度和切换：线程上下文切换比进程上下文切换要快得多。</li>
</ul>
<br>
<p><a name="user-content-E0L7c" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-5">多进程和多线程</h2>
<ul>
<li>多进程：多进程指的是在同一个时间里，同一个计算机系统中如果允许两个或两个以上的进程处于运行状态。多进程带来的好处是明显的，比如你可以听歌的同时，打开编辑器敲代码，编辑器和听歌软件的进程之间丝毫不会相互干扰。</li>
<li>多线程：是指程序中包含多个执行流，即在一个程序中可以同时运行多个不同的线程来执行不同的任务，也就是说允许单个程序创建多个并行执行的线程来完成各自的任务。</li>
</ul>
<br>
<p><a name="user-content-USqEO" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-6">浏览器的进程与线程</h2>
<p>首先打开浏览器，然后打开shift + Esc打开chrome的任务管理器<br></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0609cdcc308b4efb82b9882f48d00afe~tplv-k3u1fbpfcp-watermark.image" alt="image (1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><br>此时只有三个进程：</p>
<ul>
<li><strong>浏览器进程（Browser进程）</strong>: 浏览器的主进程（负责协调、主控），只有一个。作用有
<ul>
<li>负责浏览器界面显示，与用户交互。如前进，后退等</li>
<li>负责各个页面的管理，创建和销毁其他进程</li>
<li>将Renderer进程得到的内存中的Bitmap，绘制到用户界面上</li>
<li>网络资源的管理，下载等</li>
</ul>
</li>
<li><strong>GPU进程</strong>：用于3D绘制等（可禁止掉，而且这个与页面渲染过程的Composite Layers 有关系）</li>
<li><strong>浏览器渲染进程（Renderer进程，内部是多线程的）</strong>：每一个标签页的打开都会创建一个浏览器渲染进程（浏览器内核）。默认每个Tab页面一个进程，互不影响。主要作用为页面渲染，脚本执行，事件处理等</li>
</ul>
<br>
<p><a name="user-content-r7Dsm" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-7">浏览器为什么要多进程？</h1>
<p>在浏览器刚被设计出来的时候，那时的网页非常的简单，每个网页的资源占有率是非常低的，因此一个进程处理多个网页时可行的。</p>
<p>然后在今天，大量网页变得日益复杂。把所有网页都放进一个进程的浏览器面临在健壮性，响应速度，安全性方面的挑战。</p>
<p>因为如果浏览器中的一个tab网页崩溃的话，将会导致其他被打开的网页应用。另外相对于线程，进程之间是不共享资源和地址空间的,所以不会存在太多的安全问题，而由于多个线程共享着相同的地址空间和资源,所以会存在线程之间有可能会恶意修改或者获取非授权数据等复杂的安全问题。</p>
<br>
<p><a name="user-content-fqytl" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-8">Browser进程与Render进程，GPU进程之间的如何合作？</h1>
<p><br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f44979a9afd04af3b0a0e0221eece07e~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<br>这里的Browser engine我想对应的就是Browser进程，Rendering engine对应的就是Render进程。针对与用户打开一个标签页，可以看到首先控制的还是Browser进程。然后我们再看一下chromium多线程模型：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f980932ce74468b81f6e0cf1fd99593~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Browser进程收到用户的请求，首先由UI线程处理，而且将相应的任务转给IO线程，他随机将该任务传递Render进程；</li>
<li>Render进程的IO线程经过简单解释后交给渲染线程，渲染线程接收请求，加载网页并渲染网页，这其中可能需要Browser进程获取资源和需要GPU进程来帮助渲染，最后Render进程将结果由IO线程传递给Browser进程；</li>
<li>Browser进程接收到结果并将结果绘制出来；</li>
</ul>
<br>
<p><a name="user-content-wXHUV" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-9">浏览器渲染Render进程（浏览器内核）有哪些进程</h1>
<p><a name="user-content-s5KjD" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-10">GUI渲染线程</h2>
<p>负责渲染浏览器界面，解析HTML，CSS，构建DOM树和RenderObject树，布局和绘制等。<br>当界面需要重绘（Repaint）或由于某种操作引发回流(reflow)时，该线程就会执行<br>注意，GUI渲染线程与JS引擎线程是互斥的，当JS引擎执行时GUI线程会被挂起（相当于被冻结了），GUI更新会被保存在一个队列中等到JS引擎空闲时立即被执行。</p>
<p><a name="user-content-n6z0f" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-11">JS引擎线程</h2>
<p>也称为JS内核，负责处理Javascript脚本程序。（例如V8引擎）JS引擎线程负责解析Javascript脚本，运行代码。JS引擎一直等待着任务队列中任务的到来，然后加以处理，一个Tab页（renderer进程）中无论什么时候都只有一个JS线程在运行JS程序</p>
<p>同样注意，GUI渲染线程与JS引擎线程是互斥的，所以如果JS执行的时间过长，这样就会造成页面的渲染不连贯，导致页面渲染加载阻塞。</p>
<p><a name="user-content-vZZhB" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-12">事件触发线程</h2>
<p>归属于浏览器而不是JS引擎，用来控制事件循环（可以理解，JS引擎自己都忙不过来，需要浏览器另开线程协助）</p>
<p>当JS引擎执行代码块如setTimeOut时（也可来自浏览器内核的其他线程,如鼠标点击、AJAX异步请求等），会将对应任务添加到事件线程中</p>
<p>当对应的事件符合触发条件被触发时，该线程会把事件添加到待处理队列的队尾，等待JS引擎的处理<br>注意，由于JS的单线程关系，所以这些待处理队列中的事件都得排队等待JS引擎处理（当JS引擎空闲时才会去执行）</p>
<p><a name="user-content-FLcHL" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-13">定时触发器线程</h2>
<p>传说中的setInterval与setTimeout所在线程<br>浏览器定时计数器并不是由JavaScript引擎计数的,（因为JavaScript引擎是单线程的, 如果处于阻塞线程状态就会影响记计时的准确）<br>因此通过单独线程来计时并触发定时（计时完毕后，添加到事件队列中，等待JS引擎空闲后执行）<br>注意，W3C在HTML标准中规定，规定要求setTimeout中低于4ms的时间间隔算为4ms。</p>
<p><a name="user-content-O9DdN" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-14">异步http请求线程</h2>
<p>在XMLHttpRequest在连接后是通过浏览器新开一个线程请求<br>将检测到状态变更时，如果设置有回调函数，异步线程就产生状态变更事件，将这个回调再放入事件队列中。再由JavaScript引擎执行。</p>
<br>
<p><a name="user-content-hiZwW" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-15">JS引擎线程的相关介绍</h1>
<p><a name="user-content-raJdA" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-16">为什么JavaScript是单线程？</h2>
<p>首先在明确一个概念，JS引擎线程生存在Render进程（浏览器渲染进程）。其实从前面的进程，线程之间的介绍已经明白，线程之间资源共享，相互影响。假设javascript的运行存在两个线程，彼此操作了同一个资源，这样会造成同步问题，修改到底以谁为标准。所以，JavaScript就是单线程，这已经成了这门语言的核心特征，将来也不会改变。<br></p>
<p><a name="user-content-g0N8Z" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-17">WebWorker会造成js多线程吗？</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>webWorker<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">var</span> worker = <span class="hljs-keyword">new</span> Worker(<span class="hljs-string">"worker.js"</span>);
        worker.postMessage(<span class="hljs-number">123456</span>);

        worker.onmessage = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(e.data)
        &#125;;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//worker.js</span>
onmessage = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">count</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"web worker start"</span>)
 
    <span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>;
 
    <span class="hljs-keyword">while</span>(i < count.data) &#123;
      i ++;
    &#125;
 
    postMessage(<span class="hljs-string">"web worker finish"</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5947687b5bf7493e8b1983068fb5d5de~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<br><strong>得到的结果是webworker可以在js引擎执行代码的时候去执行另外的代码</strong></p>
<p>这里我们需要在明确开始的问题了，<strong>是造成js执行的多线程还是js引擎的多线程</strong>。这里是两个概念。上面的图示中main的栏目中是浏览器渲染Render进程（本人猜测），因为在这个过程中我们可以看到js代码的执行，也有GUI渲染线程进行html代码的解析。</p>
<p><a name="user-content-q8pkg" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-18">js执行的多线程还是js引擎的多线程</h3>
<p>我在MDN上看到一句话：<strong>Worker接口会生成真正的操作系统级别的线程</strong>。所以这里的webworker不是一个新的js引擎线程。而是操作系统级别的线程。线程的执行不会影响到原有的js引擎的执行，也不会影响到浏览器渲染Render进程。但是，人家webworker确实实现了js代码执行的多线程（当然这些都是本人的基于看到的结果猜测的，没有找到实际的论证资料，如果有知道的可以告知，谢谢了）。</p>
<p>所以我目前得到的结论是： webworker是可以造成js代码的多线程执行，但不是js引擎多线程的执行。webwoker的生命周期是由js引擎线程控制的，因为webweoker提供了一系列的api供我们操作。</p>
<p>然后我们再说一下webweoker中的一些不能操作的内容：也是出于安全考虑，如果不太小心，那么并发(concurrency)会对你的代码产生有趣的影响。然而，对于 web worker 来说，与其他线程的通信点会被很小心的控制，这意味着你很难引起并发问题。所以webworker也自己做了限制（下面的内容是在网上找到的，因为我没有这么使用过webworker）：</p>
<ol>
<li>不能访问DOM和BOM对象的，Location和navigator的只读访问，并且navigator封装成了WorkerNavigator对象，更改部分属性。无法读取本地文件系统</li>
<li>子线程和父级线程的通讯是通过值拷贝，子线程对通信内容的修改，不会影响到主线程。在通讯过程中值过大也会影响到性能（解决这个问题可以用transferable objects）</li>
<li>并非真的多线程，多线程是因为浏览器的功能</li>
<li>兼容性</li>
<li>因为线程是通过importScripts引入外部的js，并且直接执行，其实是不安全的，很容易被外部注入一些恶意代码</li>
<li>条数限制，大多浏览器能创建webworker线程的条数是有限制的，虽然可以手动去拓展，但是如果不设置的话，基本上都在20条以内，每条线程大概5M左右，需要手动关掉一些不用的线程才能够创建新的线程（相关解决方案）</li>
<li>js存在真的线程的东西，比如SharedArrayBuffer</li>
</ol>
<p><a name="user-content-b5cbY" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-19">js代码的执行（Event Loop）与其他线程之间的合作</h2>
<p>JavaScript 引擎并不是独立运行的，它运行在宿主环境中，对多数开发者来说通常就是Web 浏览器。提供了一种机制来处理程序中多个块（这里的块可以理解成多个回掉函数）的执行，且执行每块时调用JavaScript 引擎，这种机制被称为事件循环。换句话说，JavaScript 引擎本身并没有时间的概念，只是一个按需执行JavaScript 任意代码片段的环境。“事件”（JavaScript 代码执行）调度总是由包含它的环境进行。这个调度是由事件触发线程调度的。</p>
<p>举例来说，如果你的JavaScript 程序发出一个Ajax 请求，从服务器获取一些数据，那你就在一个函数（通常称为回调函数）中设置好响应代码，然后JavaScript 引擎会通知宿主环境（事件触发线程）：“嘿，现在我要暂停执行，你一旦完成网络请求，拿到了数据，就请调用这个函数。”然后浏览器就会设置侦听来自网络的响应，拿到要给你的数据之后，就会把回调函数插入到事件循环，以此实现对这个回调的调度执行。</p>
<p>请看下图对于一个页面的请求以及js的执行过程中，上面的进程/线程之间的合作，<a href="https://www.processon.com/view/link/593fc61fe4b0848d3ecf1d56" target="_blank" rel="nofollow noopener noreferrer">processon原图链接</a>。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f63b1d5bf90845b5902980ea812d1e1d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br></p>
<br>
<p><a name="user-content-MZQH9" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-20">Promise的出现</h1>
<pre><code class="hljs language-javascript copyable" lang="javascript"><!DOCTYPE html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>webWorker<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout run'</span>);
      &#125;, <span class="hljs-number">0</span>);
 
        <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
        resolve();
        &#125;)
        .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;  
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise run'</span>);
    &#125; );  
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash">promise run
setTimeout run
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的原因不在多说，因为首先js引擎要先执行主线程js的代码（会先执行完，因为一个js的加载，从上往下会执行完成之后，js引擎才会有时间去从事件循环队列中拿出代码块执行），至于setTimeout，间隔时间尽管为0ms，其实真正执行的时候是4ms。而且回掉函数是放在事件循环队列里的。</p>
<p>那么Promise呢？好比我们现在执行的是js主线程，执行完成之后，js引擎不会立即去事件循环队列里取代码块执行，而是说当前主线程还有一点事情没有做完，那就是promise。二者事件的粒度不同，promsie是事件循环队列之上的任务队列。</p>
<br>
<p><a name="user-content-dz6LN" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-21">Macrotasks 和 Microtasks</h1>
<p>这是<a href="https://html.spec.whatwg.org/multipage/webappapis.html#event-loop" target="_blank" rel="nofollow noopener noreferrer">HTML Standard</a>里的概念。</p>
<p>Macrotask 和 microtask 都是属于上述的异步任务中的一种，我们先看一下他们分别是哪些 API ：</p>
<ul>
<li>macrotasks: setTimeout, setInterval, setImmediate, I/O, UI rendering</li>
<li>microtasks: process.nextTick, Promises, Object.observe(废弃), MutationObserver</li>
</ul>
<p><strong>在每一次事件循环中，macrotask 只会提取一个执行，而 microtask 会一直提取，直到 microtasks 队列清空</strong></p>
<p><a name="user-content-K00lr" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-22">事件循环进程模型</h2>
<p><a href="https://html.spec.whatwg.org/multipage/webappapis.html#event-loop-processing-model" target="_blank" rel="nofollow noopener noreferrer">html.spec.whatwg.org/multipage/w…</a><br></p>
<p><a name="user-content-ax6XD" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-23">参照</h1>
<ul>
<li><a href="https://blog.csdn.net/Steward2011/article/details/51319298" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/Steward2011…</a><a href="https://segmentfault.com/a/1190000012925872" target="_blank" rel="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></li>
<li><a href="http://www.imweb.io/topic/58e3bfa845e5c13468f567d5" target="_blank" rel="nofollow noopener noreferrer">www.imweb.io/topic/58e3b…</a></li>
<li><a href="http://www.ruanyifeng.com/blog/2014/10/event-loop.html#comment-text" target="_blank" rel="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2014/1…</a></li>
<li><a href="https://segmentfault.com/a/1190000009313491" target="_blank" rel="nofollow noopener noreferrer">segmentfault.com/a/119000000…</a></li>
<li><a href="https://juejin.cn/post/6844903471280291854" target="_blank">juejin.cn/post/684490…</a></li>
</ul>
<br></div>  
</div>
            