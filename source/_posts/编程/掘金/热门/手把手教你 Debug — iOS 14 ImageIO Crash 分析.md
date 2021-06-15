
---
title: '手把手教你 Debug — iOS 14 ImageIO Crash 分析'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c115c8a15f64bc08ab723907b73c911~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 20 May 2021 18:21:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c115c8a15f64bc08ab723907b73c911~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c115c8a15f64bc08ab723907b73c911~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<p><strong>作者：字节移动技术——陈奕</strong></p>
<h1 data-id="heading-0">背景</h1>
<p>去年 9 月份开始，许多用户升级到 iOS 14 之后，线上出现很多 ImageIO 相关堆栈的 Crash 问题，而且公司内几乎所有的 APP 上都有出现，在部分 APP上甚至达到了 Top 3  Crash。</p>
<p>得益于 APM 平台精准数据采集机制和丰富的异常信息现场，我们通过收集到详细的 Crash 日志信息进行分析解决。</p>
<h1 data-id="heading-1">问题定位</h1>
<h2 data-id="heading-2">堆栈信息</h2>
<p>从堆栈信息看，是在 ImageIO 解析图片信息的时候 Crash ，并且最后调用的方法都是看起来都是和 <code>INameSpacePrefixMap</code> 相关，推测 Crash 应该是和这个方法 <code>CGImageSourceCopyPropertiesAtIndex</code> 的实现有关。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2e26b748765459c998a36b27412630a~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe9f4b3c224848c7a36ba391e959a787~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec929b88a614405dbd915813624ff9b5~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">问题聚合特点</h2>
<p>机型集中在 iOS14 以上的版本，同时是在后台出现</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9341bb33c573460995d1cc58d806ebc9~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">分析</h2>
<p>从 CrashLog 做一个初步分析</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c50e9a6537ca42658baefd8b683bc77a~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>从堆栈信息看，这段代码是图片库在子线程通过 <code>CGImageSourceCopyPropertiesAtIndex</code> 解析 <code>imageSource</code> 中的图片相关信息，然后发生了野指针的 Crash。</p>
</li>
<li>
<p><code>CGImageSourceCopyPropertiesAtIndex</code> 的输入只有一个 <code>imageSource</code>，<code>imageSource</code> 由图片的 data 生成，调用栈并没有多线程操作，可以排除是多线程操作 <code>imageSource</code>、data 导致的 Crash。</p>
</li>
<li>
<p>看堆栈是在解析 PNG 图片，通过将下发的图片格式换成 JPG 格式，发现量级并没有降低。推测 Crash 不是某种特定图片格式引起的。</p>
</li>
</ul>
<h2 data-id="heading-5">反汇编分析</h2>
<h3 data-id="heading-6"><strong>反汇编准备</strong></h3>
<ul>
<li>iOS 14.3 的 iPhone 8</li>
<li>ImageIO 系统库：~/Library/Developer/Xcode/iOS DeviceSupport目录下找到对应 iOS 14.3 的 ImageIO</li>
<li>一份 iOS 14.3、iPhone 8 上发生的  CrashLog</li>
<li>Hopper</li>
</ul>
<h3 data-id="heading-7"><strong>反汇编</strong></h3>
<ol>
<li>从 CrashLog 上找到 Crash 对应的指令偏移地址 <strong>2555072</strong></li>
</ol>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b7f4bb0ce264a03bb51cd59aa8460ae~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<ol start="2">
<li>通过 Hopper 打开 ImageIO，跳转到指令偏移地址 <strong>2555072</strong></li>
</ol>
<p><strong>Navigate</strong> => <strong>Go To</strong> <strong>File Offset</strong> <strong>2555072</strong></p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6335e6f521b4e9085a89be6a28d7b90~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<ol start="3">
<li>Crash 对应的指令应该是<code>0000000181b09cc0 ldr x8, [x8, #0x10]</code>，可以看到应该是访问 <code>[x8, #0x10]</code>指向的内存出错了</li>
</ol>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c123e7717b34b4daff252681b824630~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<ol start="4">
<li>查看 Crashlog 中对应寄存器的值，错误地址 <code>far: 0x000021a1ee2fa271</code>，而且 x8 寄存器已经是一个错误的值 <code>0x000021a1ee2fa261</code></li>
</ol>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f6aef24d5374d889cac7e9e7a4e020c~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<ol start="5">
<li>向上回溯查看 x8 的来源</li>
</ol>
<ul>
<li>
<p><code>0000000181b09cbc ldr x8, [x20]</code> x8 是存在 x20 指向的内存中（即 <code>x8 = *x20</code>）</p>
</li>
<li>
<p><code>0000000181b09c98 ldr x20, [x21, #0x8]</code> x20 又存在<code> [x21, #0x8]</code> 指向的内存中</p>
</li>
<li>
<p><code>0000000181b09c8c adrp x21, #0x1da0ed000   </code>，<code>0000000181b09c90 add x21, x21, #0xe10</code> x21 指向的是一个 data 段，推测 x21 应该是一个全局变量，所以，可能是这个全局变量野了，或者是这个全局变量引用的某些内存（x20）野了</p>
</li>
</ul>
<ol start="6">
<li>运行时 debug 查看 x8、x20、x21 对应寄存器的值是什么</li>
</ol>
<ul>
<li>x21 从内存地址的名字看，应该是一个全局的 Map</li>
</ul>
<pre><code class="copyable">ImageIO`AdobeXMPCore_Int::ManageDefaultNameSpacePrefixMap(bool)::sDefaultNameSpacePrefixMap
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dad15612dde842898d67fc33439cb207~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a8fdf1ac3a147fbb0d696ce903dad61~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<ol start="7">
<li>从 Hopper 上看，这个<code>sDefaultNameSpacePrefixMap</code>只在</li>
</ol>
<p><code>AdobeXMPCore_Int::ManageDefaultNameSpacePrefixMap(bool)</code> 这个函数中调用。可能会在多线程下调用这个函数，而导致这个全局变量的出现 data race 导致了野指针。</p>
<pre><code class="copyable">__ZZN16AdobeXMPCore_IntL31ManageDefaultNameSpacePrefixMapEbE26sDefaultNameSpacePrefixMap:        // AdobeXMPCore_Int::ManageDefaultNameSpacePrefixMap(bool)::sDefaultNameSpacePrefixMap

00000001da0ede10         dq         0x0000000000000000                          ; DATA XREF=__ZN16AdobeXMPCore_IntL31ManageDefaultNameSpacePrefixMapEb+44, __ZN16AdobeXMPCore_IntL31ManageDefaultNameSpacePrefixMapEb+120, __ZN16AdobeXMPCore_IntL31ManageDefaultNameSpacePrefixMapEb+392
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li>经过在运行时反复调试，这个</li>
</ol>
<p><code>AdobeXMPCore_Int::ManageDefaultNameSpacePrefixMap(bool)</code> 会在多个方法中调用（并且调用时都加了锁，不太可能会出现 data race）：</p>
<ul>
<li>
<p><code>AdobeXMPCore_Int::INameSpacePrefixMap_I::CreateDefaultNameSpacePrefixMap()</code></p>
</li>
<li>
<p><code>AdobeXMPCore_Int::INameSpacePrefixMap_I::InsertInDefaultNameSpacePrefixMap(char const*, unsigned long long, char const*, unsigned long long)</code></p>
</li>
<li>
<p><code>AdobeXMPCore_Int::INameSpacePrefixMap_I::DestroyDefaultNameSapcePrefixMap()</code></p>
</li>
</ul>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da99431e76a245089079ddeff993fdb0~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdc7e28b88904fd4897d11f570e79657~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9645e67566b047b88a3700a8d5db4c02~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<ol start="9">
<li>在后台线程访问访问全局变量 <code>sDefaultNameSpacePrefixMap</code> 时 Crash，推测可能是用户手动杀进程后，全局变量在主线程已经被析构，后台线程还会继续访问这个全局变量，从而出现野指针访问异常。发现 Crash 日志的主线程堆栈也出现 _exit 的调用，可以确定是全局变量析构导致。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0ab163aa1d243fea57a022b35f89523~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">Crash 发生的原因：</h2>
<p>在用户手动杀进程后，主线程将这个全局变量析构了，这时候子线程再访问这个全局变量就出现了野指针。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b2e5b4629f4485faee144822d6d8d93~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">复现问题</h1>
<p>尝试在子线程不断调用 <code>CFDictionaryRef CGImageSourceCopyPropertiesAtIndex(CGImageSourceRef isrc, size_t index, CFDictionaryRef options);</code>，并且手动杀掉进程触发这个 crash</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1d07e8e01e74815935832bcfcf68d86~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">成功复现</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51afd95c9b434773a3bcf74208ace5a5~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以证明上述的推理是正确的。</p>
<h1 data-id="heading-11">总结</h1>
<ul>
<li>
<p><code>CFDictionaryRef CGImageSourceCopyPropertiesAtIndex(CGImageSourceRef isrc, size_t index, CFDictionaryRef options);</code> 这个方法在解析部分图片的时候最终会访问全局变量</p>
<pre><code class="copyable">ImageIO`AdobeXMPCore_Int::ManageDefaultNameSpacePrefixMap(bool)::sDefaultNameSpacePrefixMap
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在用户手动杀进程后，这个<code>sDefaultNameSpacePrefixMap</code>被析构，如果这时候在子线程再被访问就可能出现野指针的问题</p>
</li>
</ul>
<h1 data-id="heading-12">修复 ImageIO Crash 方案</h1>
<p>因为<code>sDefaultNameSpacePrefixMap</code> 是在系统库内部的全局变量，没办法对其进行修改，只能避免在子线程调用 <code>CGImageSourceCopyPropertiesAtIndex</code> 方法</p>
<ul>
<li>
<p>方法一： <code>CGImageSourceCopyPropertiesAtIndex</code> 是用来获取图片的宽高、<code>imageOrientation</code>、动图帧等信息，选择用其他方法来替换，e.g. 宽高用 <code>CGImageRef</code> 来获取</p>
</li>
<li>
<p>方法二：将 <code>CGImageSourceCopyPropertiesAtIndex</code> 被调用的线程收敛起来，调用atexit函数来注册一个进程结束回调函数，进程结束的时候将终止线程</p>
</li>
</ul>
<h1 data-id="heading-13">关于字节移动平台团队</h1>
<p>字节跳动移动平台团队(Client Infrastructure)是大前端基础技术行业领军者，负责整个字节跳动的中国区大前端基础设施建设，提升公司全产品线的性能、稳定性和工程效率，支持的产品包括但不限于抖音、今日头条、西瓜视频、火山小视频等，在移动端、Web、Desktop等各终端都有深入研究。</p>
<p>就是现在！<strong>客户端／前端／服务端／端智能算法／测试开发</strong> 面向全球范围招聘！<strong>一起来用技术改变世界</strong>，感兴趣可以联系邮箱 <strong><a href="https://security.feishu.cn/link/safety?target=mailto:chenxuwei.cxw@bytedance.com&scene=ccm&logParams=%7B%22location%22:%22drivesdk_creation%22%7D&lang=zh-CN" target="_blank" rel="nofollow noopener noreferrer">chenxuwei.cxw@bytedance.com</a></strong>，邮件主题 <strong>简历-姓名-求职意向-电话</strong>。</p></div>  
</div>
            