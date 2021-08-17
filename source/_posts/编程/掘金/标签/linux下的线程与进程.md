
---
title: 'linux下的线程与进程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5489b16490d5483daed54f98064ca54a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 17:59:55 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5489b16490d5483daed54f98064ca54a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“<strong>这是我参与8月更文挑战的第15天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong>”</p>
<h2 data-id="heading-0">两种线程设计模型</h2>
<ul>
<li>
<p><strong>核心级线程设计模型</strong>:</p>
<p>由操作系统内核实现, 特点是: 速度快 <em>windows系统采用的是这种设计模型</em></p>
<p>可以比喻为用自己的大脑控制自己十根手指头</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5489b16490d5483daed54f98064ca54a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p><strong>用户级线程设计模型</strong>:</p>
<p>操作系统核外实现的线程模式, 特点是: 线程调度在核外 速度不如核内 <em>Linux系统采用的是这种</em></p>
<p>可以比喻为自己的十根手指头需要借助外力才能动</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c3a401cd6364326932416ee8c5981df~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">Linux系统下有真正意义的多线程么?</h2>
<p>由上面Linux采用的线程设计模型可知,Linux系统并没有真正意义上的多线程</p>
<p>因此, Linux系统里处理多线程不如Windows强悍</p>
<h2 data-id="heading-2">Linux系统的两个线程库</h2>
<ul>
<li>LinuxThreads线程库</li>
<li>RedHat的NPTL</li>
</ul>
<p>这两个线程库实际上并没有完全按照线程模式进行实现</p>
<h2 data-id="heading-3">进程的生命周期</h2>
<h4 data-id="heading-4">进程的创建及回收</h4>
<p>在Android中, ActivityThead的创建预示着进程的创建</p>
<h4 data-id="heading-5">进程的级别(由高到低)</h4>
<ul>
<li><strong>前台进程</strong>: 优先级最高, 正处于Activity Resume()状态, 杀死前台进程需要用户响应</li>
<li><strong>可见进程</strong></li>
<li><strong>服务进程</strong></li>
<li><strong>后台进程</strong></li>
<li><strong>空进程:</strong> 无组件启动,做进程缓存使用, 恢复速度快</li>
</ul>
<p>当一个应用启动的时候, 它的进程级别不是保持固定的, Android内部通过Handler进行轮询检测当前进程的状态,ActivityThread掌控的Activity 的生命周期, 如果栈中无Activity存在, 但是有Service存在的情况下, 此时的进程级别就会从前台进程降为服务进程</p>
<p>如果想要查询当前进程的级别, 可以通过ActivityManager .RuningAppProcessInfo进行查询,内部有对应的变量和方法</p>
<h4 data-id="heading-6">进程级别的记忆方法</h4>
<p>前见服后空</p>
<p>谐音: 权健服后空 (懂?)</p>
</li>
</ul></div>  
</div>
            