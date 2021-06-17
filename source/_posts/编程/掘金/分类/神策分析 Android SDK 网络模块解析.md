
---
title: '神策分析 Android SDK 网络模块解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb253f1cb7304eb29fd63e7844ca70bf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 23:41:51 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb253f1cb7304eb29fd63e7844ca70bf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、前言</h1>
<p>在信息化时代，数据成为移动互联网企业的宝贵资源。数据的获取、上报、储存、分析乃至可视化地呈现，都成为了当前重要的研究方向。当然，大数据分析最核心的还是数据，其中数据的来源更是至关重要的。如何保证数据能够准确、及时、完整地上传到指定的服务端，是神策分析 Android SDK 需要面临的核心问题。</p>
<p>神策分析 Android SDK 针对数据传输，从完整性、正确性以及高效性等多方面综合考虑，设计并实现了一套适用于数据采集的网络传输方案。下面针对神策分析 Android SDK 网络模块进行详细的介绍，希望能够给大家提供一些参考。</p>
<h1 data-id="heading-1">二、网络请求方案</h1>
<p>大多数 App 都会和服务端进行交互，因此需要连接到网络才能正常使用。数据采集 SDK 需要将数据上传到指定的服务端，同样需要依赖网络。Android 中网络请求的实现有多种方式，例如：可以使用一些比较成熟的网络框架，快速实现网络请求功能；或者使用 Android 系统提供的网络访问 API 实现网络请求功能。下面分别介绍这两种方案的优缺点。</p>
<h2 data-id="heading-2">2.1 基于开源网络框架</h2>
<p>Android 中有很多优秀的开源网络框架，例如：Volley、OkHttp、Retrofit + RxJava 、NoHttp 等，基于开源网络框架可以方便快捷地实现网络请求功能。</p>
<p>基于开源网络框架实现有如下优点：</p>
<ol>
<li>可以减少代码量，将重点放在业务上，不需要在技术框架上耗费过多的时间；</li>
<li>功能丰富，使用门槛低；</li>
<li>流行的开源网络框架经过众多应用的验证，性能相对稳定。</li>
</ol>
<p>但是，基于开源网络框架实现也有一些缺点：</p>
<ol>
<li>功能较多，代码逻辑复杂，学习成本较高；</li>
<li>内部缺陷修复难度大甚至需要依赖作者来更新维护；</li>
<li>包含很多可能使用不到的功能以及冗余的代码，引入后会导致体积增大很多。</li>
</ol>
<p>基于开源网络框架实现网络请求方案有利有弊，可以根据实际需要选择合适的开源网络框架。</p>
<h2 data-id="heading-3">2.2 基于系统方法</h2>
<p>基于系统方法实现的网络请求方案通常采用 HttpURLConnection 或 HttpClient：</p>
<ul>
<li>HttpURLConnection：在 JDK 的 java.net 包提供的一种多用途、轻量级的访问 HTTP 协议的基本功能类，大多数的应用程序都使用该接口进行网络访问请求；</li>
<li>HttpClient：是 Apache 开源组织提供的网络访问类，封装了 HTTP 协议的细节实现，Android 6.0 之前包含在系统 API 中。</li>
</ul>
<p>它们都提供较多的 API，而且相对比较稳定。这两种网络请求类均有以下功能：</p>
<ol>
<li>支持 HTTPS 协议网络请求；</li>
<li>可以配置超时时间；</li>
<li>支持 IPv6 协议；</li>
<li>支持连接池；</li>
<li>可以实现流媒体的上传与下载。</li>
</ol>
<p>在 Android 6.0 之前大多数应用的网络请求是通过 HttpClient 实现的，相比较于 HttpURLConnection ，使用 HttpClient 具有以下优势：</p>
<ol>
<li>从易用性方面对比：HttpClient 封装了 HTTP 协议的细节，使用起来比较方便。HttpURLConnection 是 Java 的标准类，由于缺少封装导致使用不便；</li>
<li>从稳定性方面对比：HttpClient 功能强大且更稳定，容易控制细节。而之前的 HttpURLConnection 一直存在着版本兼容的问题。</li>
</ol>
<p>从 Android 6.0 开始移除了 HttpClient，如果在 Android 6.0 以上继续使用 HttpClient 时，需要在相应的 module下的 build.gradle 中进行依赖库配置。具体配置如下：</p>
<pre><code class="copyable">android &#123;
     useLibrary 'org.apache.http.legacy'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，Android 6.0 以上，更推荐使用 HttpURLConnection。从上述的分析可以看出：之前一直使用 HttpClient 是由于 HttpURLConnection 不稳定导致的。目前谷歌已经修复了 HttpURLConnection 存在的一些问题，相比 HttpClient 优势如表 2-1 所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb253f1cb7304eb29fd63e7844ca70bf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>表 2-1 HttpURLConnection 与 HttpClient 功能对比</p>
<p>因此，使用基于系统方法实现的网络请求方案一般采用 HttpURLConnection 来实现。</p>
<h1 data-id="heading-4">三、SDK 网络模块</h1>
<p>如果 SDK 网络模块基于开源网络框架实现，可维护性和版本控制都有一定的风险，此外还会导致 SDK 体积增大很多。由于这些缺点很难被用户所接受，因此基于开源网络框架实现网络模块不适用于 SDK。</p>
<p>考虑到上述原因，SDK 网络模块最终采用了基于 HttpURLConnection 的方式实现。</p>
<p>HttpURLConnection 是系统提供的网络访问 API，不仅可满足 SDK 网络请求的需要，而且系统 API 功能更稳定，更易扩展。</p>
<h2 data-id="heading-5">3.1 原理介绍</h2>
<p>3.1.1 实现原理</p>
<p>Android 中进行网络请求是基于 HTTP 协议实现的。HTTP 协议是目前 Internet 上最常使用、最重要的协议，该协议为典型的请求 - 响应模型：</p>
<ol>
<li>客户端建立连接并发送请求；</li>
<li>服务端接受并处理请求；</li>
<li>服务端发送应答；</li>
<li>客户端接受并处理应答。</li>
</ol>
<p>在基于 HttpURLConnection 实现网络请求方案时，很有必要对 HttpURLConnection 有进一步的了解。HttpURLConnection 继承自 URLConnection  抽象类，URLConnection 类本身依赖于 Socket 类实现网络连接。Socket 又称做套接字，它把复杂的网络操作抽象为简单的接口供上层调用。由于 HttpURLConnection 并不是底层的连接，而是在底层连接上的一个请求，因此 HttpURLConnection 不需要设置 Socket。</p>
<p>HttpURLConnection 支持 GET、POST、PUT、DELETE  等请求方式，最常用的就是 GET 与 POST 请求，下面从数据传输长度和安全性两方面对比：</p>
<ol>
<li>数据传输长度：一般来说， GET 请求传输的数据长度有限制（URL 有长度限制），POST 请求传输的数据长度没有限制；</li>
<li>安全性：GET 请求安全性较差（发送的数据会拼接在 URL 后面），POST 请求相对安全（数据不显示在 URL 中）。</li>
</ol>
<p>考虑到 SDK 采集的数据量相对较大，且对数据安全性要求较高，因此采用 HttpURLConnection POST 方式实现网络请求。</p>
<p>3.1.2 使用方式</p>
<p>HttpURLConnection 的具体使用步骤如图 3-1 所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8eef259fa0f2486092a28ce9d37ac9ed~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 3-1 HttpURLConnection 使用流程</p>
<p>由于涉及到网络访问，需要在 Manifest 文件中添加网络访问权限：</p>
<pre><code class="copyable"><uses-permission android:name="android.permission.INTERNET"/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上是对 HttpURLConnection 的原理以及具体使用的介绍，下面对 SDK 中网络请求的具体实现进行介绍。</p>
<h2 data-id="heading-6">3.2 具体实现</h2>
<p>3.2.1 网络相关配置</p>
<p>SDK 可以对数据上报进行一系列的配置，开发者可根据 App 的特点设置相应的配置，从而达到最高效的数据上报效果。SDK 的相关配置在初始化时完成，可以配置的参数如下：</p>
<p>mServerUrl：数据上报地址，采集的本地数据将上报到该地址；
mFlushInterval：两次数据发送的最小时间间隔（单位毫秒），默认值为 15；
mFlushBulkSize：本地缓存数据的最大条目数，当本地缓存条数达到 mFlushBulkSize 则会上报数据， 默认值为 100；
mNetworkTypePolicy：网络上传策略，可配置为 3G、4G、5G、WIFI 等网络类型进行上报。</p>
<p>3.2.2 工作线程封装</p>
<p>SDK 数据上报是在子线程中完成的，当采集的数据满足上报策略时触发数据异步上报，上传任务的管理调度在 Worker 类中完成。在 Worker 初始化时，创建 HandlerThread 实例，HandlerThread 本质上是一个线程类，它继承自 Thread 类。HandlerThread 内有自己的 Looper 对象，可以进行 Looper 循环。通过获取 HandlerThread 中 Looper 对象传递给 Handler 对象，可以在 handleMessage 方法中执行异步任务。</p>
<p>AnalyticsMessageHandler 继承自 Handler，在 handleMessage 中接收 Worker 发送的消息并执行数据上报或删除。</p>
<p>在 HandlerThread 中的 Looper 对象，传递给 AnalyticsMessageHandler 对象，在 handleMessage 方法中实现异步网络任务。AnalyticsMessageHandler 代码实现如下：</p>
<pre><code class="copyable">private class AnalyticsMessageHandler extends Handler &#123;
           ......
        Worker() &#123;
            final HandlerThread thread =
                    new HandlerThread("com.sensorsdata.analytics.android.sdk.AnalyticsMessages.Worker",
                            Thread.MIN_PRIORITY);
            thread.start();
            mHandler = new AnalyticsMessageHandler(thread.getLooper());
        &#125;
         @Override
         public void handleMessage(Message msg) &#123;
               ......
            if (msg.what == FLUSH_QUEUE) &#123;
               sendData();
            &#125; else if (msg.what == DELETE_ALL) &#123;
                try &#123;
                     mDbAdapter.deleteAllEvents();
                 &#125; catch (Exception e) &#123;
                     com.sensorsdata.analytics.android.sdk.SALog.printStackTrace(e);
                 &#125;
            &#125; else &#123;
                 SALog.i(TAG, "Unexpected message received by SensorsData worker: " + msg);
            &#125;
            ......
        &#125;
    ......
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Worker 中封装了两个方法 runMessage 和 runMessageOnce ：</p>
<ul>
<li>runMessage 方法用于执行数据实时上报；</li>
<li>runMessageOnce 方法用于延时执行上报任务。</li>
</ul>
<p>Handler 中的 sendMessageDelayed() 方法可以实现数据的延时上报。</p>
<p>3.2.3 数据上报策略</p>
<p>在 SDK 数据存储解析中介绍了数据的采集与存储策略：采集的数据会先保存到本地，符合上报策略才会上报。</p>
<ul>
<li>客户端本地存储的数据超过一定条数时（默认 100 条）会上报数据</li>
</ul>
<p>在 SDK 初始化时，可配置 mFlushBulkSize 参数来控制条数限制。如果不进行设置，则默认为 100 条。如果用户设置的条数小于 50 条，则默认为 50 条。SDK 采集的数据较多，如果设置上报条数太小会导致频繁的网络请求（上报数据），从而影响性能。如果用户设置上报条数过多，会导致一次上传的数据过大，这样不仅会导致上传时间长还很可能会出现上传失败的情况。如果没有特殊要求，可直接使用默认值。</p>
<ul>
<li>数据采集后间隔一定时间（默认 15 秒）会上报数据</li>
</ul>
<p>在 SDK 初始化时，可配置 mFlushInterval 参数来控制时间间隔限制。如果不满足上报条数限制时，SDK 会执行一个延时任务，延时 mFlushInterval 设定的时间后执行。</p>
<p>除了上文中提到的策略外，还会在触发以下事件时，会以阻塞的形式将本地缓存的数据全部上报：</p>
<ul>
<li>在采集 $AppEnd 事件时上报数据；</li>
<li>捕获 App 异常时上报数据；</li>
<li>在激活事件触发后上报数据。</li>
</ul>
<p>3.2.4 数据安全</p>
<p>3.2.4.1 数据加密</p>
<p>SDK 上报的数据涉及到用户隐私，保护用户隐私是开发者应尽的责任和义务。SDK 提供数据加密策略对上报的数据进行加密，以防止用户信息在传输过程中发生泄漏。</p>
<p>SDK 的数据加密策略是将采集到的数据缓存到本地，然后采用 RSA + AES 加密算法进行加密，主要实现流程如下：</p>
<ol>
<li>App 内置 RSA 公钥及密钥（假设为 A），或者从服务端获取（从服务端获取方便更换公钥，缺点是使用更多的传输带宽、增加初始化的成本；另外服务端同时使用多个密钥对，解密时需要选取对应私钥，若密钥过多可能会影响导入性能）；</li>
<li>随机生成长度为 128 位的对称加密 AES 对称秘钥（假设为 B），使用 RSA 公钥 A 对 AES 对称密钥 B 进行加密；</li>
<li>用户触发事件产生 JSON 数据，使用 AES 对称秘钥 B 对采集的事件（即整条 JSON 数据）进行加密产生密文数据；</li>
<li>按照与后台约定的格式拼装数据存储到本地。</li>
</ol>
<p>拼装后的格式如下：</p>
<pre><code class="copyable">&#123;
    "pkv": RSA 公钥对应的秘钥编号,
    "ekey": "使用 RSA 公钥 A 对 AES 对称密钥 B 加密产生的密文",
    "payload": "使用 AES 对称秘钥 B 对采集的事件即整条 JSON 数据进行加密产生密文数据"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上报数据时，会从磁盘读取数据。根据加密方案，“ekey” 字段会很长（与 RSA 密钥长度有关），每条带一个“ekey” 冗余较多。因此，在上报之前会进行数据合并，对于 “ekey” 相同的数据，合并到一个数组中。合并后发送到服务端的数据格式如下：</p>
<pre><code class="copyable">[&#123;
    "pkv": RSA 公钥对应的秘钥编号1,
    "ekey": "使用 RSA 公钥 A 对 AES 对称密钥 B 加密产生的密文",
    "payloads": [“加密后的事件数据1”，“加密后的事件数据2”]
&#125;,&#123;
    "pkv": RSA 公钥对应的秘钥编号2,
    "ekey": "使用 RSA 公钥 A 对 AES 对称密钥 B 加密产生的密文",
    "payloads": [“加密后的事件数据3”，“加密后的事件数据4”]
&#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，服务端使用 “pkv” 对应的私钥解密 “ekey” 字段得到 AES 对称密钥的参数 key，解密 payloads 得到多条消息原文。</p>
<p>3.2.4.2 HTTPS 双向验证</p>
<p>HTTPS 是在 HTTP 上建立的 SSL 加密层，并对传输数据进行加密，是 HTTP 协议的安全版。</p>
<p>在 HTTP 协议中可能存在安全问题，主要包括以下几个方面：</p>
<ol>
<li>传输的数据使用明文，可能被窃取；</li>
<li>无法校验数据是否完整；</li>
<li>无法确认通信双方的身份。</li>
</ol>
<p>使用 HTTPS 协议可以有效地防止这些问题：</p>
<ol>
<li>内容经过加密并生成一个唯一的加密秘钥；</li>
<li>能够校验数据是否完整；</li>
<li>可以确认通信双方的身份。</li>
</ol>
<p>SDK 支持 HTTPS 协议网络请求，通过 HTTPS 双向验证保证数据的安全性。</p>
<p>3.2.5 数据上报流程</p>
<p>数据采集时，会创建一个异步任务加入到任务队列中，通过 TrackTaskManagerThread 调度任务顺序执行。在子线程中执行一个任务时，首先采集预置属性信息，其次将预置信息和自定义属性信息封装成神策需要的 JSON 格式，存储到数据库中。</p>
<p>如果当前处于 Debug 模式或者数据库超过最大缓存限制时，会进行上报数据操作；不满足时会进行如下判断：如果触发的事件为 “$SignUp” 或者本地缓存的条数大于设置的 mFlushBulkSize 时会进行上报数据；否则会触发延时上报，在间隔设置的 mFlushInterval 时间上报数据。上报流程如图 3-2 所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72b21471c56c4c12a9d4a2b4aa8d1900~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 3-2 数据上报流程图</p>
<p>发送数据时，以下情况不会发送数据：</p>
<ul>
<li>用户设置 mEnableNetworkRequest 为 false 不会上报数据，用户可通过 enableNetworkRequest 方法设置是否上报数据；</li>
<li>serverURL 为空时不会上报数据；</li>
<li>不在主进程时不会上报数据；</li>
<li>无网络时不会上报数据；</li>
<li>不满足 SDK 设置的上报策略时不会上报数据。</li>
</ul>
<p>满足上报条件时，SDK 会将本地的数据全部上报。如果一次传输的数据较大，会增加数据上传失败的可能性，同时对性能的影响也比较大。因此，SDK 一次最多读取 50 条数据，对读取的原始事件数据先采用 Gzip 压缩，然后对压缩的内容进行 Base64 编码，保证高效的传输。同时考虑到数据的完整性和安全性，会将原始数据的 hashCode 值传到服务端，用于对数据完整性校验。</p>
<p>数据上报后，根据网络请求状态码判断数据是否上报成功：网络请求状态码在 200 ~ 300 之间时，认为 SDK 上报数据是成功的，会删除本地上报成功的数据。网络请求失败时，本地数据不删除。每次发送都会循环读取本地缓存的数据，直到数据全部上传完成。</p>
<h1 data-id="heading-7">四、数据上报校验</h1>
<p>开发者在集成 SDK 开发过程中，需要校验 SDK 是否将数据正常、准确地上报到服务端。SDK 提供了通过查看 Logcat 控制台日志和 Debug 实时查询的方式来校验数据上报的准确性。</p>
<h2 data-id="heading-8">4.1Logcat 本地日志校验</h2>
<p>通过日志查看数据是否上报成功，首先需要在初始化 SDK 后调用 enableLog(true) 打开 SDK 的日志输出功能。如果相应事件触发，SDK 会自动进行采集并定时发送到神策分析后台。可以通过 Logcat 查看日志进行数据校验， 在 Logcat 中筛选 “SA.”  可查看事件采集上报的相关日志，具体分为以下几种情况：</p>
<ul>
<li>埋点事件触发成功时，输出 “track event” 开头的事件数据；</li>
<li>埋点事件触发失败时，输出相应的错误原因；</li>
<li>事件数据上报成功时，输出 “valid message” 字段开头的事件数据；</li>
<li>事件数据上报失败时，输出 “invalid message” 字段开头的事件数据并输出错误原因。</li>
</ul>
<p>开发过程中通过日志即可判断数据是否正常上报。</p>
<h2 data-id="heading-9">4.2 Debug 实时数据查询</h2>
<p>SDK 提供了 Debug 模式上报数据功能，方便开发者在集成 SDK 时校验数据。Debug 模式下 SDK 采集的数据会实时上报，SDK 提供了， DEBUG_ONLY 和 DEBUG_AND_TRACK 两种模式：</p>
<p>DEBUG_ONLY：采集数据上报到服务端但不会入库，可以在 Debug 实时查询中看到上报的数据，避免在测试过程中产生的脏数据入库；
DEBUG_AND_TRACK：会实时上报数据，同时数据也会入库。
Debug 实时数据查询是在神策分析系统中查看数据是否正常上报。使用 Debug 模式需要根据文档正确配置 scheme，Android 中的 scheme 是一种页面内跳转协议。定义自己的 scheme 后，可以实现通过链接拉起应用或者跳转应用中的某个页面。</p>
<p>SDK 中配置 scheme 的目的就是通过扫码拉起应用作为开启 Debug 调试模式的入口。使用方法是：</p>
<ol>
<li>先使用调试设备扫描网页二维码，开启该设备的「调试模式」；</li>
<li>点击开始刷新后，操作 App 触发事件；</li>
<li>事件上传成功就会在 Debug 实时数据查看中看到对应的事件。</li>
</ol>
<h1 data-id="heading-10">五、总结</h1>
<p>本文主要介绍了神策分析 Android SDK 网络模块的具体实现，SDK 网络请求没有基于开源网络框架来实现，避免了体积的过度增加和代码的冗余。通过对系统类 HttpURLConnection 进行封装，采用完善的上报策略，同时对数据进行压缩、编码、校验等操作，实现了数据及时、准确、高性能的上报。</p>
<p>最后，希望通过这篇文章，大家能够对神策分析 Android SDK 网络模块有一个系统的了解。</p>
<p>参考文献
HttpURLConnection  用法解析：
<a href="https://www.jianshu.com/p/7330b4ad895a" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/7330b4ad8…</a></p>
<p>Android  探索之  HttpURLConnection  网络请求：
<a href="https://www.cnblogs.com/whoislcj/p/5520384.html" target="_blank" rel="nofollow noopener noreferrer">www.cnblogs.com/whoislcj/p/…</a></p>
<p>文章来源：神策技术社区</p></div>  
</div>
            