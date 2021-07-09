
---
title: '定时器_ Linux中的定时器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87f16fa7dc42475285a132434903a55a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 08:06:20 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87f16fa7dc42475285a132434903a55a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>在看 Node http 模块文档的时候， 才留意到 <code>server.timeout</code> 这个属性， 本想简单介绍一下， 但是在梳理过后发现关于 <code>timeout</code> 有庞大的内容支撑： <code>server.timout -> node core timers -> uv timers -> linux msleep/hrtimer -> clocksource -> tsc -> cmos rtc -> clock cycle</code>， 所以拆分成几部分大致做下介绍， 期望定时器系列结束之后， noder 能够大致明白: <code>clock cycle</code> 是如何驱动 linux 的 <code>msleep/hrtimer</code>； linux 的 timers 与 uv timers 的关系； node timers 与 uv timers的关系。</p>
</blockquote>
<p>了解Linux的定时器的工作原理，有助于我们更深刻的认识Node中的定时器真面目。</p>
<h2 data-id="heading-0">定时器核心组件</h2>
<ol>
<li>石心 - 时钟源 - 硬件</li>
<li>守护者 - 记录时间 - 软件</li>
<li>定时狗 - 事件源 - 硬件</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87f16fa7dc42475285a132434903a55a~tplv-k3u1fbpfcp-watermark.image" alt="linux_timer.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意区分时刻和时间: 2020-11-22T12:31:37.696Z 时刻； 1000ms 是时间。系统初始化时刻来自RTC，后面的时刻都来自于 时刻 + 时间的计算</p>
</blockquote>
<h2 data-id="heading-1">石心</h2>
<p>硬件层面上有两个主要的模块: CMOS 和 CPU。 CMOS 可以在断电后继续<code>振动</code>和<code>更新RTC</code>时间， CPU上电后在<code>TSC寄存器</code>可以在记录<code>上电后</code>的cycles总和，其本质只是一个收到高电压后+1的<code>Counter</code>。</p>
<p>此时操作系统可以获取到: RTC, TSC, Frequecy，那么系统的时间就可以通过<code>公式</code>计算出来: <code>RTC + TSC/Frequency</code></p>
<p>硬件的<code>缺陷</code>:</p>
<p>CMOS: RTC 是整个系统<code>初始化</code>的时间，但其本身<code>精度较低</code>，毫秒级，所以多台机器时钟很难在毫秒以下<code>对齐</code></p>
<p>TSC: TSC 精度虽然可以在<code>纳秒</code>级别，但是只能记录上电之后的时间；TSC 通过64位存储，在10GHz情况下，<code>溢出</code>时间为<code>2**64/(1e10*3600*24*365)≈58Y</code></p>
<blockquote>
<p>注意区分时刻和时间: 2020-11-22T12:31:37.696Z 时刻； 1000ms 是时间。系统初始化时刻来自RTC，那么系统时刻 = 初始时刻 + 时间。</p>
</blockquote>
<h2 data-id="heading-2">守护者</h2>
<p>ClockSource是对<code>硬件TSC</code>的一种抽象，可以通过 read 方法读取到 TSC 寄存器中的 cycle，然后将cycle赋值给自身，只是在没有调用read方法之前，其时间<code>落后</code>于真正的TSC。</p>
<p>目前最高精度的硬件: tsc > hpet > acpi_pm， 他们都是时间记录者，里面存储的是cycle.</p>
<pre><code class="copyable">#$ cat /sys/devices/system/clocksource/clocksource0/available_clocksource 
tsc hpet acpi_pm 
#$ cat /sys/devices/system/clocksource/clocksource0/current_clocksource 
tsc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>TimeKeeper 的主要工作就是<code>主动调用</code>ClockSource中的read，然后做cycle到timestamp的转换(<code>时间到时刻的转换</code>)，并记录到自身。此时操作系统读取的时间就是从TimeKeeper中读取。</p>
<p>管家的缺陷:</p>
<p>TimeKeeper 只是时间的抽象，没有办法实现时间的<code>自动更新</code>，需要<code>外部调用</code>更新，所以时间落后于真正的TSC。</p>
<h2 data-id="heading-3">定时狗</h2>
<p>无论是ClockSource还是TimerKeepr，他们只是对数字的一抽象，没有办法主动更新， 所以为了保持时间的实时性，需要一个程序不断的调用 read 来更新时间.</p>
<p>结合<a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer">定时器: 石心</a>中的内容，一个自更新的时间的原型大概是这样的:</p>
<pre><code class="copyable">while(true) &#123;
 const cycles = TimeKeeper.ClockSOurce.read(tsc);
 const now = TimeKeeper.setTimer(cycles);
 if (now != '双11') &#123;
 schedule(); // 让CPU干点其他的，等会在更新时间，毕竟时间不能当饭吃
 &#125;
&#125;
优惠();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该定时器的问题是: 无法控制CPU回调的时间，可能超时；频繁CPU调度。</p>
<p>软件与硬件必须互相配合，上面的问题在没有硬件加持下是无法避免的，所以需要引入一个非常中的硬件<code>APIC 高级可编程中断控制</code>。</p>
<p>目前最牛X的APIC为: lapic-deadline，而ClockeEventDevice就是对APIC硬件的抽象。</p>
<pre><code class="copyable">#$ cat /sys/devices/system/clockevents/clockevent0/current_device 
lapic-deadline
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之所以说它最牛，是因为<code>它本身就是一个(硬件)定时器: 可以给apic设定一个超时的cycle数量，当TSC中的cycle到达该值时，发送一个事件</code>。</p>
<p>有了基于cycle(精度)的事件(通知)，实现高精度定时器就不在话下了；低精度定时器完全也可以通过高精度定时器来模拟出来。</p>
<h2 data-id="heading-4">总结</h2>
<ol>
<li>CMOS中的RTC提供初始化时刻</li>
<li>CMOS中的晶体提供震荡</li>
<li>CPU中的TSC寄存器只记录上电以来的震荡个数cycle</li>
<li>CPU中的APIC可以根据预设的cycle产生事件</li>
</ol>
<p>硬件和软件相辅相成，需要效率支撑的通过硬件来支撑，硬件缺失的情况下可以通过软件来模拟。</p>
<p>关注我的微信公众号“SUNTOPO WLOG”，欢迎留言讨论，我会尽可能回复，感谢您的阅读。</p></div>  
</div>
            