
---
title: 'iOS摸鱼周报 第十一期'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d6518be73e445bba9f8fd3597e309a0~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 16:30:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d6518be73e445bba9f8fd3597e309a0~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d6518be73e445bba9f8fd3597e309a0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>iOS摸鱼周报，主要分享开发过程中遇到的经验教训、优质的博客、高质量的学习资料、实用的开发工具等。周报仓库在这里：<a href="https://github.com/zhangferry/iOSWeeklyLearning" target="_blank" rel="nofollow noopener noreferrer">github.com/zhangferry/…</a> ，如果你有好的的内容推荐可以通过 issue 的方式进行提交。</p>
<p>也欢迎申请成为我们的常驻编辑，一起维护这份周报。另可关注公众号：iOS成长之路，后台点击进群交流，联系我们，获取更多内容。</p>
<h2 data-id="heading-0">开发Tips</h2>
<h3 data-id="heading-1">如何通过 ASWebAuthenticationSession 获取身份验证</h3>
<p>整理编辑：<a href="https://juejin.cn/user/3192637497025335/posts" target="_blank">FBY展菲</a></p>
<p>一般获取第三方平台身份验证的途径就是接入对应平台的 SDK，但通常接入 SDK 会伴随各种问题，包体增大，增加潜在bug等。其实大部分的服务商都有实现一种叫做 OAuth 的开放授权机制，我们可以不通过SDK，直接利用该机制完成授权流程。</p>
<p>符合OAuth2.0 标准的 Authorization Code 授权流程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ac3d9d6005b43e8811907900ad160c1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图片参考：<a href="https://appcoda.com.tw/ios-oauth/" title="用iOS 内建的ASWebAuthenticationSession 实作OAuth 2.0 授权流程！" target="_blank" rel="nofollow noopener noreferrer">用iOS 内建的ASWebAuthenticationSession 实作OAuth 2.0 授权流程！</a></p>
<p>苹果把 OAuth 流程进行了封装，就是 <code>ASWebAuthenticationSession</code> 。该API 最低支持到 iOS 12.0，在这之前可以使用 <code>SFAuthenticationSession</code> ，该API 只存在于 iOS 11.0 和 iOS 12.0，目前已被废弃。使用方法如下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">oauthLogin</span>(<span class="hljs-params">type</span>: <span class="hljs-type">String</span>)</span> &#123;
    <span class="hljs-comment">// val GitHub、Google、SignInWithApple</span>
    <span class="hljs-keyword">let</span> redirectUrl <span class="hljs-operator">=</span> <span class="hljs-string">"配置的 URL Types"</span>
    <span class="hljs-keyword">let</span> loginURL <span class="hljs-operator">=</span> <span class="hljs-type">Configuration</span>.shared.awsConfiguration.authURL <span class="hljs-operator">+</span> <span class="hljs-string">"/authorize"</span> <span class="hljs-operator">+</span> <span class="hljs-string">"?identity_provider="</span> <span class="hljs-operator">+</span> type <span class="hljs-operator">+</span> <span class="hljs-string">"&redirect_uri="</span> <span class="hljs-operator">+</span> redirectUri <span class="hljs-operator">+</span> <span class="hljs-string">"&response_type=CODE&client_id="</span> <span class="hljs-operator">+</span> <span class="hljs-type">Configuration</span>.shared.awsConfiguration.appClientId
    session <span class="hljs-operator">=</span> <span class="hljs-type">ASWebAuthenticationSession</span>(url: <span class="hljs-type">URL</span>(string: loginURL)<span class="hljs-operator">!</span>, callbackURLScheme: redirectUri) &#123; url, error <span class="hljs-keyword">in</span>
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"URL: <span class="hljs-subst">\(String(describing: url))</span>"</span>)
        <span class="hljs-comment">// The callback URL format depends on the provider.</span>
        <span class="hljs-keyword">guard</span> error <span class="hljs-operator">==</span> <span class="hljs-literal">nil</span>, <span class="hljs-keyword">let</span> responseURL <span class="hljs-operator">=</span> url<span class="hljs-operator">?</span>.absoluteString <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span>
        &#125;
        <span class="hljs-keyword">let</span> components <span class="hljs-operator">=</span> responseURL.components(separatedBy: <span class="hljs-string">"#"</span>)
        <span class="hljs-keyword">for</span> item <span class="hljs-keyword">in</span> components &#123;
            <span class="hljs-keyword">guard</span> <span class="hljs-operator">!</span>item.contains(<span class="hljs-string">"code"</span>) <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">continue</span>
            &#125;
            <span class="hljs-keyword">let</span> tokens <span class="hljs-operator">=</span> item.components(separatedBy: <span class="hljs-string">"&"</span>)
            <span class="hljs-keyword">for</span> token <span class="hljs-keyword">in</span> tokens &#123;
                <span class="hljs-keyword">guard</span> <span class="hljs-operator">!</span>token.contains(<span class="hljs-string">"code"</span>) <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-keyword">continue</span>
                &#125;
                <span class="hljs-keyword">let</span> idTokenInfo <span class="hljs-operator">=</span> token.components(separatedBy: <span class="hljs-string">"="</span>)
                <span class="hljs-keyword">guard</span> idTokenInfo.count <span class="hljs-operator"><=</span> <span class="hljs-number">1</span> <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-keyword">continue</span>
                &#125;
                <span class="hljs-keyword">let</span> code <span class="hljs-operator">=</span> idTokenInfo[<span class="hljs-number">1</span>]
                <span class="hljs-built_in">print</span>(<span class="hljs-string">"code: <span class="hljs-subst">\(code)</span>"</span>)
                <span class="hljs-keyword">return</span>
            &#125;
        &#125;
    &#125;
    session.presentationContextProvider <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>
    session.start()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里面有两个参数，一个是 <strong>redirectUri</strong>，一个是 <strong>loginURL</strong>。</p>
<p>redirectUri 就是 3.1 配置的白名单，作为页面重定向的唯一标识。</p>
<p><strong>loginURL 是由 5 块组成：</strong></p>
<ol>
<li><strong>服务器地址：</strong> Configuration.shared.awsConfiguration.authURL + "/authorize"</li>
<li><strong>打开的登录平台：</strong> identity_provider = "GitHub"</li>
<li><strong>重定向标识：</strong> identity_provider = "配置的 URL Types"</li>
<li><strong>相应类型：</strong> response_type = "CODE"</li>
<li><strong>客户端 ID：</strong> client_id = "服务器配置"</li>
</ol>
<p>回调中的 url 包含我们所需要的<strong>身份验证 code 码</strong>，需要层层解析获取 code。</p>
<p>参考：<a href="https://mp.weixin.qq.com/s/QUiiCKJObfDPKWCvxAg5nQ" title="如何通过 ASWebAuthenticationSession 获取身份验证" target="_blank" rel="nofollow noopener noreferrer">如何通过 ASWebAuthenticationSession 获取身份验证 - 展菲</a></p>
<h3 data-id="heading-2">使用 Charles 为 Apple TV 抓包</h3>
<p>因为 Apple TV 没法直接设置代理，抓包的话需要借助于 <a href="https://apps.apple.com/nz/app/apple-configurator-2/id1037126344?mt=12" title="Apple Configurator 2" target="_blank" rel="nofollow noopener noreferrer">Apple Configurator 2</a> 。</p>
<p>在 Apple Configurator 2 里创建一个描述文件，填入电脑端的 IP 地址和端口号。按 Command + S 即可保存当前的描述文件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abf43df02f0540bda3da1c20f81f5161~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>到这时还无法抓包 HTTPS 请求，需要导入一个 Charles 的证书。在Charles 里 Help > SSL Proxying > Save Charles Root Certificate，选择cer格式保存起来。在 Apple Configurator 2 里创建一个证书文件，描述文件里选证书即可，配置的时候添加刚才保存的cer文件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36d6603ac0864685a640cdb4d46eda3b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>将这个两个文件通过 Configurator 2 安装到Apple TV里，并在 TV 端的 Settings > About 里的证书选项里进行信任。之后在 Charles 里加入对 443 端口的监听，并保持 TV 和 电脑处在同一Wifi 下即可进行抓包。</p>
<p>参考：<a href="https://www.charlesproxy.com/documentation/using-charles/ssl-certificates/" target="_blank" rel="nofollow noopener noreferrer">www.charlesproxy.com/documentati…</a></p>
<h2 data-id="heading-3">编程概念</h2>
<p>整理编辑：<a href="https://juejin.cn/user/782508012091645" target="_blank">师大小海腾</a>，<a href="https://zhangferry.com/" target="_blank" rel="nofollow noopener noreferrer">zhangferry</a></p>
<p>该期主题来源于对 <a href="https://github.com/crisxuan" target="_blank" rel="nofollow noopener noreferrer">xuan总</a> 的那篇 <a href="https://github.com/zhangferry/iOSWeeklyLearning/tree/main/Resources/Books" target="_blank" rel="nofollow noopener noreferrer">程序必知的硬核知识大全</a> 的部分总结，引用图片也来源于此，该文档已经过其本人授权放到了周报仓库里，有兴趣的读者可以去下载全文阅读。</p>
<h3 data-id="heading-4">什么是 CPU</h3>
<p>中央处理器（Central Processing Unit，简称 CPU）作为计算机系统的运算和控制核心，是信息处理、程序运行的最终执行单元。CPU 与计算机的关系就相当于大脑和人的关系。它是一种小型的计算机芯片，嵌入在电脑的主板上。通过在单个计算机芯片上放置数十亿个微型晶体管来构建 CPU。这些晶体管使它能够执行运行存储在系统内存中的程序所需的计算，也就是说 CPU 决定了你电脑的计算能力。</p>
<p>CPU 的功能主要是解释计算机指令以及处理计算机软件中的数据。几乎所有的冯·诺依曼型计算机的 CPU 的工作都可以分为 5 个阶段：取指令、指令译码、执行指令、访存取数、结果写回。</p>
<p>在指令执行完毕后、结果数据写回之后，若无意外事件（如结果溢出等）发生，计算机就接着从程序计数器中取得下一条指令的地址，开始新一轮的循环。许多新型 CPU 可以同时取出、译码和执行多条指令，体现并行处理的特性。</p>
<p>从功能来看，CPU 的内部由寄存器、控制器、运算器和时钟四部分组成，各部分之间通过电信号连通。对程序员来说，我们只需要了解寄存器就可以了。</p>
<ul>
<li>寄存器负责暂存指令、数据和地址。</li>
<li>控制器负责把内存上的指令、数据读入寄存器，并根据指令的结果控制计算机。</li>
<li>运算器负责运算从内存中读入寄存器的数据。</li>
<li>时钟负责发出 CPU 开始计时的时钟信号。</li>
</ul>
<p>CPU 相关内容还有两个我们经常遇到的概念：位数、架构。</p>
<p>当前常见的 CPU 位数是 32 位和 64 位，这里的位数是指 CPU 一次可以处理的数据位数，就效率上来说 64 位的 CPU 会比 32 位的 CPU 提高一倍。</p>
<p>架构指的是 CPU 的设计架构，目前主流的架构是 x86 和 ARM 两种。</p>
<ul>
<li>x86 是 Intel 芯片选用的架构，它包含 32 位和 64 位，通常 64 位的 x86 架构被表述为 x86_64。该架构芯片多用于 PC 机。</li>
<li>ARM 架构是一个精简指令集（RISC）处理器架构家族，其多用于嵌入式操作系统及手机端。iPhone 上的 A 系列 CPU 就一直是 ARM 架构。ARM 的发展史从 ARMv1 一直到当前的 ARMv8。初代 iPhone 到 iPhone 3GS 之前使用的是 ARMv6；从 3GS 到 5s 之前使用的 ARMv7 架构，5s 开始使用的 ARMv8。但其实 ARMv8 这个叫法却很少出现，而更多的是 ARM64。这是因为从 v8 版本开始分 32 位和 64 位两种（在这之前没有 64 位），苹果使用的都是 64 位，所以就用 ARM64 代替了。</li>
</ul>
<h3 data-id="heading-5">什么是寄存器</h3>
<p>寄存器是 CPU 内的组成部分，是用来暂存指令、数据和地址的电脑存储器。</p>
<p>不同的类型的 CPU，其内部寄存器的种类，数量以及寄存器存储的数值范围是不同的。不过，可以根据功能将寄存器划分为下面几类：</p>
<ul>
<li>累加寄存器：存储运行的数据和运算后的数据。</li>
<li>标志寄存器：用于反应处理器的状态和运算结果的某些特征以及控制指令的执行。</li>
<li>程序计数器：用来存储下一条指令所在单元的地址。</li>
<li>基址寄存器：存储数据内存的起始位置。</li>
<li>变址寄存器：存储基址寄存器的相对位置。</li>
<li>通用寄存器：存储任意数据。</li>
<li>指令寄存器：存储正在被运行的指令，CPU 内部使用，程序员无法对该寄存器进行读写。</li>
<li>栈寄存器：存储栈区域的起始位置。</li>
</ul>
<p>其中，累加寄存器、标志寄存器、程序计数器、指令寄存器和栈寄存器都只有一个，其它寄存器一般有多个。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b85333af08874bbd9ab833d817d46458~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>寄存器的命名是跟着 CPU 类型走的，ARM64 类型的 CPU 有 32 个寄存器，以下列出了部分寄存器的特殊作用：</p>

























<table><thead><tr><th>寄存器</th><th>作用</th></tr></thead><tbody><tr><td>x0、x1、x2、x3、x4、x5、x6、x7</td><td>保存函数参数及返回值</td></tr><tr><td>x29</td><td>lr（link register）寄存器，保存函数的返回地址</td></tr><tr><td>x30</td><td>sp（stack pointer）寄存器，保存栈地址</td></tr><tr><td>x31</td><td>pc（program counter）寄存器，指向下一条将执行的指令</td></tr></tbody></table>
<h3 data-id="heading-6">什么是程序计数器</h3>
<p>程序计数器（Program Counter，简称 PC）是一种寄存器，一个 CPU 内部仅有一个 PC。为了保证程序能够连续地执行下去，CPU 必须具有某些手段来确定下一条指令的地址。而 PC 正是起到这种作用，其用来存储下一条指令所在单元的地址，所以通常又称之为“指令计数器”。</p>
<p>PC 的初值为程序第一条指令的地址。程序开始执行，CPU 需要先根据 PC 中存储的指令地址来获取指令，然后将指令由内存取到指令寄存器（存储正在被运行的指令）中，然后解码和执行该指令，同时 CPU 会自动修改 PC 的值为下一条要执行的指令的地址。完成第一条指令的执行后，根据程序计数器取出第二条指令的地址，如此循环，执行每一条指令。</p>
<p>每执行一条指令后，PC 的值会立即指向下一条要执行的指令的地址。当顺序执行时，每执行一条指令，PC 的值就是简单的 +1。而条件分支和循环执行等转移指令会使 PC 的值指向任意的地址，这样程序就可以跳转到任意指令，或者返回到上一个地址来重复执行同一条指令。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efb181e343c646439e65bb48dc6ca1d4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">什么是内存</h3>
<p>内存是计算机中最重要的部件之一，它是程序与 CPU 进行沟通的桥梁。计算机中所有程序的运行都是在内存中进行的，内存又被称为主存，其作用是存放 CPU 中的运算数据，以及与硬盘等外部存储设备交换的数据。只要计算机在运行中，CPU 就会把需要运算的数据调到内存中进行运算，当运算完成后 CPU 再将结果传送出来。</p>
<p>内存通过控制芯片与 CPU 进行相连，由可读写的元素构成，每个字节都带有一个地址编号，注意是一个字节，而不是一个位。CPU 通过地址从内存中读取数据和指令，也可以根据地址写入数据。注意一点：当计算机关机时，内存中的指令和数据也会被清除。</p>
<p>物理结构：内存的内部是由各种 IC 电路组成的，它的种类很庞大，但是其主要分为三种存储器。</p>
<ul>
<li>随机存储器（RAM）：内存中最重要的一种，表示既可以从中读取数据，也可以写入数据。当机器关闭时，内存中的信息会丢失。</li>
<li>只读存储器（ROM）：ROM 一般只能用于数据的读取，不能写入数据，但是当机器停电时，这些数据不会丢失。</li>
<li>高速缓存（Cache）：Cache 也是我们经常见到的，它分为一级缓存（L1 Cache）、二级缓存（L2 Cache）、三级缓存（L3 Cache）这些数据，它位于内存和 CPU 之间，是一个读写速度比内存更快的存储器。当 CPU 向内存中写入数据时，这些数据也会被写入高速缓存中。当 CPU 需要读取数据时，会之间从高速缓存中直接读取，当然，如需要的数据在 Cache 中没有，CPU 会再去读取内存中的数据。</li>
</ul>
<h3 data-id="heading-8">什么是 IC</h3>
<p>集成电路（Integrated Circuit，缩写为 IC）。顾名思义，就是把一定数量的常用电子元件，如电阻、电容、晶体管等，以及这些元件之间的连线，通过半导体工艺集成在一起的具有特定功能的电路。</p>
<p>内存和 CPU 使用 IC 电子元件作为基本单元。IC 电子元件有不同种形状，但是其内部的组成单位称为一个个的引脚。IC 元件两侧排列的四方形块就是引脚，IC 的所有引脚只有两种电压：0V 和 5V，该特性决定了计算机的信息处理只能用 0 和 1 表示，也就是二进制来处理。一个引脚可以表示一个 0 或 1，所以二进制的表示方式就变成 0、1、10、11、100、101 等，虽然二进制数并不是专门为引脚设计的，但是和 IC 引脚的特性非常吻合。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea57dd9605e04379a2bd511eace61d9a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们都知道内存是用来存储数据的，那么这个 IC 中能存储多少数据呢？D0 - D7 表示的是数据信号，也就是说一次可以输入输出 1 byte = 8 bit 数据。A0 - A9 是地址信号，共10个，表示可以指定 2^10 = 1024 个地址。每个地址都都可存放 1 byte 数据，所以这个 IC 的容量就是 1KB。</p>
<h2 data-id="heading-9">优秀博客</h2>
<p>整理编辑：<a href="https://www.jianshu.com/u/739b677928f7" target="_blank" rel="nofollow noopener noreferrer">皮拉夫大王在此</a></p>
<p>1、<a href="https://juejin.cn/post/6844904012857229326" title="Pecker：自动检测项目中不用的代码" target="_blank">Pecker：自动检测项目中不用的代码</a> -- 来自掘金：RoyCao</p>
<p>又看了一遍这篇文章，可以通过这篇文章学习下作者对<strong>IndexStoreDB</strong>的应用的思路。</p>
<p>2、<a href="https://juejin.cn/post/6844904067878092808" title="[译]你可能不知道的iOS性能优化建议（来自前Apple工程师）" target="_blank">【译】你可能不知道的iOS性能优化建议（来自前Apple工程师）</a> -- 来自掘金：RoyCao</p>
<p>RoyCao的另一篇文章，感觉挺有价值的也挺有意思的。</p>
<p>3、<a href="https://mp.weixin.qq.com/s/ZOENpzfYk3b1T-OlRi7EYg" title="在抖音 iOS 基础组的体验（文末附内推方式）" target="_blank" rel="nofollow noopener noreferrer">在抖音 iOS 基础组的体验（文末附内推方式）</a> -- 来自公众号：一瓜技术</p>
<p>一线大厂核心APP的基础技术团队究竟在做什么？技术方向有哪些？深度如何？团队成员发展和团队氛围如何？可能很多同学和我有一样的疑问，可以看看这篇文章</p>
<p>4、<a href="https://juejin.cn/post/6956144382906990623" title="iOS 内存管理机制" target="_blank">iOS 内存管理机制</a> -- 来自掘金：奉孝</p>
<p>内存方面总结的很全面，内容很多，准备面试的同学可以抽时间看看。</p>
<p>5、<a href="https://mp.weixin.qq.com/s/Th1C3_pVES6Km6A7isgYGw" title="LLVM Link Time Optimization" target="_blank" rel="nofollow noopener noreferrer">LLVM Link Time Optimization</a> -- 来自公众号：老司机周报</p>
<p>相信很多同学都尝试开启LTO比较优化效果，但是我们真的完全开启LTO了吗？个人感觉这是一篇让人很有收获的文章，可以仔细阅读一番</p>
<p>6、<a href="https://mp.weixin.qq.com/s/rUZ8RwhWf4DWAa5YHHynsQ" title="A站 的 Swift 实践 —— 上篇" target="_blank" rel="nofollow noopener noreferrer">A站 的 Swift 实践 —— 上篇</a> -- 来自公众号：快手大前端技术</p>
<p>不用看作者，光看插图就知道是戴老师的文章。期待后续对混编和动态性的介绍。</p>
<h2 data-id="heading-10">学习资料</h2>
<p>整理编辑：<a href="https://juejin.cn/user/1433418892590136" target="_blank">Mimosa</a></p>
<h3 data-id="heading-11"><a href="https://www.fivestars.blog/" target="_blank" rel="nofollow noopener noreferrer">Five Stars Blog</a></h3>
<p>该网站由 <a href="https://twitter.com/zntfdr" target="_blank" rel="nofollow noopener noreferrer">Federico Zanetello</a> 一手经营，其全部内容对所有人免费开放，每周都有新的文章发布。网站内较多文章在探寻 <code>iOS</code> 和 <code>Swift</code> 的具体工作原理，其关于 <code>SwiftUI</code> 的文章也比较多，文章的质量不错，值得关注一下。</p>
<h3 data-id="heading-12"><a href="https://zsisme.gitbooks.io/ios-/content/index.html" target="_blank" rel="nofollow noopener noreferrer">iOS Core Animation: Advanced Techniques 中文译本</a></h3>
<p>iOS Core Animation: Advanced Techniques 的中文译本 GitBook 版，翻译自 <a href="http://www.amazon.com/iOS-Core-Animation-Advanced-Techniques-ebook/dp/B00EHJCORC/ref=sr_1_1?ie=UTF8&qid=1423192842&sr=8-1&keywords=Core+Animation+Advanced+Techniques" target="_blank" rel="nofollow noopener noreferrer">iOS Core Animation: Advanced Techniques</a>，很老但是价值很高的书，感谢译者的工作。该书详细介绍了 Core Animation(Layer Kit) 的方方面面：CALayer，图层树，专属图层，隐式动画，离屏渲染，性能优化等等，虽然该书年代久远了一些，但是笔者每次看依然能悟到新知识🤖！如果想复习一下这方面知识，该译本将会是绝佳选择。</p>
<h2 data-id="heading-13">工具推荐</h2>
<p>整理编辑：<a href="https://zhangferry.com/" target="_blank" rel="nofollow noopener noreferrer">zhangferry</a></p>
<h3 data-id="heading-14">Moment</h3>
<p><strong>软件状态</strong>：￥30，可以试用7天</p>
<p><strong>使用介绍</strong></p>
<p>Moment 是一个存在于菜单栏和通知中心的倒计时应用程序，以帮助你记住最难忘的日子和生活。这个类似手机端的 Countdown。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cd0a3b976464f5b9028fc3bef94dd33~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">One Switch</h3>
<p><strong>软件状态</strong>：￥30，可以试用7天</p>
<p><strong>使用介绍</strong></p>
<p>One Switch 是一个聚合的开关控制软件，使用它可以在菜单控制栏直接配置桌面的隐藏显示、锁屏、暗黑模式、连接AirPods 等功能。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b61285a374d42b6a37826daa2a4b571~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">联系我们</h2>
<p><a href="https://zhangferry.com/2021/03/28/iOSWeeklyLearning_7/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第七期</a></p>
<p><a href="https://zhangferry.com/2021/04/11/iOSWeeklyLearning_8/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第八期</a></p>
<p><a href="https://zhangferry.com/2021/04/24/iOSWeeklyLearning_9/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第九期</a></p>
<p><a href="https://zhangferry.com/2021/05/05/iOSWeeklyLearning_10/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第十期</a></p></div>  
</div>
            