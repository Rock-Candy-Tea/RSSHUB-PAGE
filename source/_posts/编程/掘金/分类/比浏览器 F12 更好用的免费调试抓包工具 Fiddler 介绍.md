
---
title: '比浏览器 F12 更好用的免费调试抓包工具 Fiddler 介绍'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2aafadc2acff4882be5128258dd38d61~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 05:03:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2aafadc2acff4882be5128258dd38d61~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767/" target="_blank" title="https://juejin.cn/post/6978685539985653767/">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<blockquote>
<p>本文是关于 Fiddler 工具介绍的学习笔记，这里做个总结与分享，有不足之处还望斧正~</p>
</blockquote>
<p>身为一名前端搬砖工，长久以来有两个问题困扰着我，一个是做后台项目接口返回的数据都为空，不方便做更进一步的对数据的查改及测试；另一个是做移动端的项目，比如 uniapp，每次遇到接口问题都只能 console 在 HBuilder 进行调试，苦不堪言，后来发现我司 TE 同学用 Fiddler 进行抓包测试，一问这软件还是免费的，遂进行了一番学习了解，发现可以直接解决刚刚提到的这两个问题，所以在这里做个分享。</p>
<h1 data-id="heading-0">简介</h1>
<ul>
<li>Fiddler  是位于客户端和服务器端的 HTTP 代理</li>
<li>目前最常用的 HTTP 抓包工具之一</li>
<li>功能非常强大，是 web 调试的利器
<ul>
<li>监控浏览器所有的 HTTP/HTTPS 流量</li>
<li>查看、分析请求内容细节</li>
<li>伪造客户端请求和服务器响应</li>
<li>解密 HTTPS 的 web 会话</li>
<li>全局、局部断点功能</li>
<li>第三方插件</li>
</ul>
</li>
<li>使用场景
<ul>
<li>接口的测试与调试</li>
<li>线上环境调试</li>
<li>web 性能分析</li>
</ul>
</li>
</ul>
<h1 data-id="heading-1">下载</h1>
<p>直接去官网下载 Fiddler Classic 即可：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2aafadc2acff4882be5128258dd38d61~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">原理</h1>
<p>学习一件新事物，最好是知其然亦知其所以然，这样遇到问题心里有底，才不容易慌，下面就介绍下 Fiddler 抓包的原理。</p>
<p>Fiddler 是位于客户端和服务器端之间的 HTTP 代理。一旦启动 Fiddler，其会自动将代理服务器设置成本机，默认端口为 8888，并设置成系统代理（Act as system proxy on startup）。可以在 Fiddler 通过 'Tools -> Options -> Connections' 查看， 图示如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5acf45aa586a4957b504c620fa47ca41~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
在 Fiddler 运行的情况下，以 Chrome 浏览器为例，可以在其 '设置 -> 高级 -> 系统 -> 打开您计算机的代理设置 -> 连接 -> 局域网（LAN）设置' 里看到，'代理服务器' 下的 '为 LAN 使用代理服务器' 选项被勾选了（如果没有运行 Fiddler，默认情况下是不会被勾选的），如下图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abb9f985af8b47ceb70a8a715ff96083~tplv-k3u1fbpfcp-watermark.image" alt="image (1).png" loading="lazy" referrerpolicy="no-referrer"><br>
点开 '高级'，会发现 '要使用的代理服务器地址' 就是本机 ip，端口为 8888。如下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e85287a5ce2d4ab88e4694013cc954bc~tplv-k3u1fbpfcp-watermark.image" alt="image (2).png" loading="lazy" referrerpolicy="no-referrer"><br>
也就是说浏览器的 HTTP 请求/响应都被代理到了系统的 8888 端口，被 Fiddler 拦截了。</p>
<h1 data-id="heading-3">界面介绍</h1>
<p>下面开始对整个 Fiddler 的界面进行一个庖丁解牛</p>
<h2 data-id="heading-4">工具栏</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d26ea9be60cd466d9eba41eb4118e4ca~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
主要介绍上图中几个标了号的我认为比较常用的功能：</p>
<ol>
<li>Replay：重放选中的那条请求，同时按下 shift + R 键，可以输入重复发送请求的次数（这些请求是串行发送的）。可以用来做重放攻击的测试。</li>
<li>删除会话（sessions）</li>
<li>继续打了断点的请求：打断点后请求会被拦截在 Fiddler，点击这个 Go 继续发送。打断点的方式是点击界面底部的空格，具体位置如下图所示：</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8cdb471d2b4487ca178d2f10787995b~tplv-k3u1fbpfcp-watermark.image" alt="image (1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>这个类似瞄准器的工具时用于选择抓取请求的应用：按住不放将鼠标拖放到目标应用即可</li>
<li>可用于查找某条请求，比如你知道请求参数里的某个字段，可以直接输入进行查找</li>
<li>编码解码工具，可以进行多种编码的转换，是个人觉得挺好用的一个工具，能够编码的格式包括但不限于 base64、md5 和 URLEncode 等</li>
<li>可以查看一些诸如本机 ip（包括 IPv4，IPv6） 等信息，就用不着去 cmd 里 输入ipconfig 查看了，如下图：</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5262664517124b3680bd56c047e20154~tplv-k3u1fbpfcp-watermark.image" alt="image (2).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">会话列表（Session List）</h2>
<p>位于软件界面的左半部的就是会话列表了，抓取到的每条 http 请求都列在这，每一条被称为一个 session，如下图所示：<br>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41bc43f0c8c04008824665b2dc3a112a~tplv-k3u1fbpfcp-watermark.image" alt="image (3).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">每条会话默认包含的信息</h3>
<ul>
<li>请求的状态码（result）</li>
<li>协议（protocol）</li>
<li>主机名（host）</li>
<li>URL</li>
<li>请求大小（body，以字节为单位）</li>
<li>缓存信息（caching）</li>
<li>响应类型（content-type）</li>
<li>发出请求的 Windows 进程及进程 ID（process）</li>
</ul>
<h3 data-id="heading-7">自定义列</h3>
<p>除了以上这些，我们还可以添加自定义列，比如想添加一列请求方法信息：</p>
<ol>
<li>点击菜单栏 -> Rules -> Customize Rules 调出 Fiddler ScriptEditor 窗口</li>
<li>按下 ctrl + f 输入 static function Main() 进行查找</li>
<li>然后在找到的函数 Main 里添加：</li>
</ol>
<pre><code class="hljs language-c# copyable" lang="c#">FiddlerObject.UI.lvSessions.AddBoundColumn(<span class="hljs-string">"Method"</span>,<span class="hljs-number">60</span>,getHTTPMethod );
<span class="hljs-function"><span class="hljs-keyword">static</span> function <span class="hljs-title">getHTTPMethod</span>(<span class="hljs-params">oS: Session</span>)</span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-literal">null</span> != oS.oRequest) <span class="hljs-keyword">return</span> oS.oRequest.headers.HTTPMethod; 
  <span class="hljs-keyword">else</span> <span class="hljs-keyword">return</span> String.Empty;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>图示如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc6d907e210849038508d45217460eba~tplv-k3u1fbpfcp-watermark.image" alt="image (4).png" loading="lazy" referrerpolicy="no-referrer">
4. 按下 ctrl + s 保存。然后就可以在会话列表里看到多出了名为 Method 的一列，内容为请求方法。</p>
<h3 data-id="heading-8">排序和移动</h3>
<ol>
<li>点击每一列的列表头，可以反向排序</li>
<li>按住列表头不放进行拖动，可以改变列表位置</li>
</ol>
<h2 data-id="heading-9">QuickExec 与状态栏</h2>
<p>位于软件界面底部的那条黑色的是 QuickExec，可用于快速执行输入的一些命令，具体命令可输入 help 跳转到官方的帮助页面查看。图示如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/112757b18fa94745ab94ef81ac121f4b~tplv-k3u1fbpfcp-watermark.image" alt="image (5).png" loading="lazy" referrerpolicy="no-referrer"><br>
在 QuickExec 下面的就是状态栏，</p>
<ol>
<li>Capturing：代表目前 Fiddler 的代理功能是开启的，也就是是否进行请求响应的拦截，如果想关闭代理，只需要点击一下 Capturing 图标即可</li>
<li>All Processes：选择抓取的进程，可以只选浏览器进程或是非浏览器进程等</li>
<li>断点：按一次是请求前断点，也就是请求从浏览器发出到 Fiddler 这停住；再按一次是响应后的断点，也就是响应从服务器发出，到Fiddler 这停住；再按一次就是不打断点</li>
<li>当前选中的会话 / 总会话数</li>
<li>附加信息</li>
</ol>
<h2 data-id="heading-10">辅助标签 + 工具</h2>
<p>位于软件界面右边的这一大块面板，即为辅助标签 + 工具，如下图所示，它拥有 10 个小标签，我们先从 Statistics 讲起，<em>btw</em>，这单词的发音是 [stəˈtɪstɪks]，第 3 个字母 a 发 'ə' 的音，而不是 'æ'~</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7ad70c7e9da46c49c509c090779e7b6~tplv-k3u1fbpfcp-watermark.image" alt="image (6).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">Statistics（统计）</h3>
<p>这个 tab 里都是些 http 请求的性能数据分析，如 DNS Lookup（DNS 解析时间）、 TCP/IP Connect（TCP/IP 连接时间）等。</p>
<h3 data-id="heading-12">Inspectors（检查器）</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7aabd14b49904782b3e960d676cb61e7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
以多种不同的方式查看请求的请求报文和响应报文，比如可以只看头部信息（Headers）、或者是查看请求的原始信息（Raw）,再比如请求的参数是 x-www-form-urlencoded 的话，就能在 WebForms 里查看...</p>
<h3 data-id="heading-13">AutoResponder（自动响应器）</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba266fe3fa8a4557b87d1f5e3668e926~tplv-k3u1fbpfcp-watermark.image" alt="image (1).png" loading="lazy" referrerpolicy="no-referrer"><br>
这是一个我认为比较有用的功能了，它可以篡改从服务器返回的数据，达到欺骗浏览器的目的。</p>
<h4 data-id="heading-14">实战案例</h4>
<p>我在做一个后台项目的时候，因为前台还没弄好，数据库都是没有数据的，在获取列表时，请求得到的都是如下图所示的空数组：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa13a290bbe94ef3b6bd0934d3b9003e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
那么在页面上显示的也就是“暂无数据”，这就影响了之后一些删改数据的接口的对接。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/487b1a60721d4a8194206dce80580076~tplv-k3u1fbpfcp-watermark.image" alt="image (2).png" loading="lazy" referrerpolicy="no-referrer"><br>
此时，我们就可以通过 AutoResponder ，按照接口文档的返回实例，对返回的数据进行编辑，具体步骤如下：</p>
<ol>
<li>勾选上 Enable rules（激活自动响应器） 和 Unmatched requests passthrough（放行所有不匹配的请求）</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd6ff6f214684d509caa8cda00399640~tplv-k3u1fbpfcp-watermark.image" alt="image (3).png" loading="lazy" referrerpolicy="no-referrer"><br>
2. 在左侧会话列表里选中要修改响应的那条请求，按住鼠标直接拖动到 AutoResponder 的面板里，如下图红框所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f9c1c68679e4c4b98d14c791a0d7c11~tplv-k3u1fbpfcp-watermark.image" alt="image (4).png" loading="lazy" referrerpolicy="no-referrer"><br>
3. 选中上图红框里的请求单机鼠标右键，选择 Edit Response...</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2d32776bf704d26bbe72cb3226ecb37~tplv-k3u1fbpfcp-watermark.image" alt="image (5).png" loading="lazy" referrerpolicy="no-referrer"><br>
4. 进入编辑面板选择 Raw 标签就可以直接进行编辑了，这里我按照接口文档的返回示例，给 items 数组添加了数据，如下图所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f13a3e3d8c243c0b1f300fb4828d780~tplv-k3u1fbpfcp-watermark.image" alt="image (6).png" loading="lazy" referrerpolicy="no-referrer"><br>
这样，浏览器接收到数据，页面就如下图所示有了内容，方便进行之后的操作</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce06c1445a404f4696da38ae9fa208f4~tplv-k3u1fbpfcp-watermark.image" alt="image (7).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">Composer（设计者）</h3>
<p>说完了对响应的篡改，现在介绍的 composer 就是用于对请求的篡改。这个单词的翻译是作曲家，按照我们的想法去修改一个请求，宛如作曲家谱一首乐曲一般。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05e1a28f79ba40c8bcf724caaa4ff0ab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
用法与 AutoResponder 类似，也是可以从会话列表里直接拖拽一个请求到上图红框中，然后对请求的内容进行修改即可。应用场景之一就是可以绕过一些前端用 js 写的限制与验证，直接发送请求，通过返回的数据可以判断后端是否有做相关限制，测试系统的健壮性。</p>
<h3 data-id="heading-16">Filters（过滤器）</h3>
<p>在默认情况下，Filters 会抓取一切能够抓取到的请求，统统列在左侧的会话列表里，如果我们是有目的对某些接口进行测试，就会觉得请求列表很杂乱，这时可以点开 Filters 标签，勾选 Use Filters，启动过滤工具，如下图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/779239a0c7a44409bd9406fc533facf4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
接着就可以根据我们需要对左侧列表里展示的所抓取的接口进行过滤，比如根据 Hosts 进行过滤，只显示 Hosts 为 api.juejin.cn 的请求，就可以如下图在 Hosts 那选择 'Show only the following Hosts'，然后点击右上角 Actions 里的 'Run Filterset now' 执行过滤。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ca8b1c00b9c4c7d9a78e42b75aed499~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
过滤的筛选条件还有很多，比如据请求头字段里 URL 是否包含某个单词等，都很简单，一看便知，这里不再一一细说。</p>
<h2 data-id="heading-17">HTTPS 抓包</h2>
<p>默认情况下，Fiddler 没办法显示 HTTPS 的请求，需要进行证书的安装：</p>
<ol>
<li>点击 'Tools -> Options...' ，勾选上 'Decrypt HTTPS traffic' (解密HTTPS流量)</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/368963e0a4ba4e57858eb4a3cd8335bf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>点击 Actions 按钮，点击 'Reset All Certicicates' （重置所有证书），之后遇到弹出的窗口，就一直点击 '确定' 或 'yes' 就行了。</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d24b0ef5ed594dcc9a2a4da71d404c36~tplv-k3u1fbpfcp-watermark.image" alt="image (1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>查看证书是否安装成功：点击 'Open Windows Certificate Manager' 打开 Windows 证书管理器窗口</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dff92680217f43b3bb37f5ea31c6a142~tplv-k3u1fbpfcp-watermark.image" alt="image (2).png" loading="lazy" referrerpolicy="no-referrer"><br>
点击 '操作' 选择 '查找证书'，在 '包含' 输入框输入 fiddler 进行查找</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ebd266d88c84ec2bfbdc4df844017fd~tplv-k3u1fbpfcp-watermark.image" alt="image (3).png" loading="lazy" referrerpolicy="no-referrer"><br>
查找结果类似下图即安装证书成功</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c73dd434e5d48bb9bb85ee557f833fd~tplv-k3u1fbpfcp-watermark.image" alt="image (4).png" loading="lazy" referrerpolicy="no-referrer"><br>
现在会话列表就能成功显示 https 协议的请求了。</p>
<h2 data-id="heading-18">断点应用</h2>
<h3 data-id="heading-19">全局断点</h3>
<p>通过 'Rules -> Automatic Breakpoints' 可以给请求打断点，也就是中断请求，断点分为两种：</p>
<ol>
<li>Before Requests（请求前断点）：请求发送给服务器之前进行中断</li>
<li>After Responses（响应后断点）：响应返回给客户端之前进行中断</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77346028203b44679b3bfe04fd08cfc7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
打上断点之后，选中想要修改传输参数的那一条请求，按 R 进行重发，这条请求就会按要求在请求前或响应后被拦截，我们就可以根据需要进行修改，然后点击工具栏的 'Go'，或者点击如下图所示的绿色按钮 'Run to Completion'，继续完成请求。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/830803e2567c49cab3e410ff04fa1265~tplv-k3u1fbpfcp-watermark.image" alt="image (1).png" loading="lazy" referrerpolicy="no-referrer"><br>
这样打断点是全局断点，即所有请求都会被拦截，下面介绍局部断点。</p>
<h3 data-id="heading-20">局部断点</h3>
<p>如果只想对某一条请求打断点，则可以在 QuickExec 输入相应的命令执行。</p>
<ul>
<li><strong>请求前断点</strong></li>
</ul>
<ol>
<li>在 QuickExec 输入 <code>bpu query_adverts</code> 。注意：query_adverts 为请求的 url 的一部分，这样就只有 url 中包含 query_adverts 的请求会被打上断点。</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59f2dcfe514247a4b5a915d608f915c3~tplv-k3u1fbpfcp-watermark.image" alt="image (2).png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>按下 Enter 键，可以看到红框中显示 query_adverts 已经被 breakpoint 了，而且是 RequestURI</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/420a9d4dbb3b4b01a60b819dfd60d459~tplv-k3u1fbpfcp-watermark.image" alt="image (3).png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>选中 url 中带 query_adverts 的这条请求，按 R 再次发送，在发给服务器前就会被中断（原谅我又拿掘金的请求做例子~）</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d29b596d23a94497b967fc8afbc751c8~tplv-k3u1fbpfcp-watermark.image" alt="image (4).png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>取消断点：在 QuickExec 输入 <code>bpu</code> 按下 Enter 即可</li>
</ol>
<ul>
<li><strong>响应后断点</strong></li>
</ul>
<p>与请求前断点步骤基本一致，区别在于输入的命令是 <code>bpafter get_today_status</code>
按下 Enter 后在 'Composer' 标签下点击 'Execute' 执行，再次发送该请求则服务器的响应在发送给浏览器之前被截断，注意下红色的图标，跟之前的请求前断点的区别在于一个是向上的箭头，一个是向下的箭头。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af9a055af9d046be9d128fb618f7c3b2~tplv-k3u1fbpfcp-watermark.image" alt="image (5).png" loading="lazy" referrerpolicy="no-referrer"><br>
取消拦截则是输入 <code>bpafter</code> 后回车，可以看到状态栏显示 'ResponseURI breakpoint cleared'</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15b7cd3bc85247c6a43a1e6e9a1184ed~tplv-k3u1fbpfcp-watermark.image" alt="image (6).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-21">弱网测试</h2>
<p>Fiddler 还可以用于弱网测试，'Rules -> Performance -> 勾选 Simulate Modem Speeds' 即可</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a59f4a6e116b4fefaab7f3a9b8497d57~tplv-k3u1fbpfcp-watermark.image" alt="image (7).png" loading="lazy" referrerpolicy="no-referrer"><br>
再次刷新网页会感觉回到了拨号上网的年代，可以测试网站在网速很低的情况下的表现。</p>
<h3 data-id="heading-22">修改网速</h3>
<p>网速还可以修改，点击 'FiddlerScript' 标签，在下图绿框中搜索 simulateM，按几下回车找到 <code>if (m_SimulateModem)</code> 这段代码，可以修改上下传输的速度：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67af8a73266c4bf2a8e56b3805b819e4~tplv-k3u1fbpfcp-watermark.image" alt="image (8).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-23">安卓手机抓包</h2>
<p>最后一部分主要内容是关于手机抓包的，我用的是小米手机 9，MIUI 12.5.1 稳定版，安卓版本为 11。</p>
<ol>
<li>首先保证安装了 Fiddler 的电脑和手机连的是同一个 wifi</li>
<li>在 Fiddler 中，点击 'Tools -> Options...' ，在弹出的 Options 窗口选择  Connections 标签，勾选 'Allow remote computers to connect'</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e840049990e4f95a307879d4ebf48a3~tplv-k3u1fbpfcp-watermark.image" alt="image (9).png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>手机打开 '设置 -> WLAN -> 连接的那个 WLAN 的设置' 进入如下图所示的页面</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e44d329f233840fd91f3e678c2a15b3b~tplv-k3u1fbpfcp-watermark.image" alt="image (10).png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>'代理' 选择 '手动'，'主机名' 填写电脑的主机名，端口则是 Fiddler 默认监听的 8888，然后点击左上角的 '打钩图标' 进行保存</li>
<li>下载证书：打开手机浏览器，输入 '<a href="https://link.juejin.cn/?target=http%3A%2F%2F192.168.1.1%3A8888" target="_blank" rel="nofollow noopener noreferrer" title="http://192.168.1.1:8888" ref="nofollow noopener noreferrer">http://192.168.1.1:8888</a>' （注意：192.168.1.1 要替换成你电脑的 ip 地址），会出现如下页面</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13c5bde617d44f5189b90a00f7ffeac0~tplv-k3u1fbpfcp-watermark.image" alt="image (11).png" loading="lazy" referrerpolicy="no-referrer"><br>
点击红框中链接进行证书的下载</p>
<ol start="6">
<li>安装证书：打开 '设置 -> 密码与安全 -> 系统安全 -> 加密与凭据 -> 安装证书（从存储设备安装证书）-> 证书 ' 找到刚刚下载的证书进行安装</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ae35b1c2b4548a58e6fab7867de73ff~tplv-k3u1fbpfcp-watermark.image" alt="image (12).png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="7">
<li>安装完成可以在 '加密与凭据 -> 信任的凭据' 下查看</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edbf2989be8f48faadb7266b80545114~tplv-k3u1fbpfcp-watermark.image" alt="image (13).png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="8">
<li>现在 Fiddler 就可以抓到手机里 app 发送的请求了</li>
<li>最后注意：测试完毕需要关闭手机的 WLAN 代理，否则手机就上不了网了~</li>
</ol>
<h1 data-id="heading-24">One More Thing</h1>
<h2 data-id="heading-25">几个常用快捷键</h2>
<ul>
<li>双击某一条请求：打开该请求的 Inspectors 面板</li>
<li>ctrl + X：清除请求列表</li>
<li>R：选中某一条请求，按 R 键可重新发送该请求</li>
<li>shift+delete：删除除了选中那一条之外的请求</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d160e26986d1447e8ef2dfe783fc6eb6~tplv-k3u1fbpfcp-watermark.image" alt="感谢.gif" loading="lazy" referrerpolicy="no-referrer"><br>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a7fbbcaca1c480c942b7735a7228e9f~tplv-k3u1fbpfcp-watermark.image" alt="点赞.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            