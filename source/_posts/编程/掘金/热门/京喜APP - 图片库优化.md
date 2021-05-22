
---
title: '京喜APP - 图片库优化'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a95c673969ac4ff78771427deef67368~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 12 May 2021 06:00:14 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a95c673969ac4ff78771427deef67368~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">介绍</h1>
<p>京喜APP早期开发主要是快速<code>原生化</code>迭代替代原有<code>H5</code>，提高用户体验，在这期间也积累了不少性能问题。之后我们开始进行一些性能优化相关的工作，本文主要是介绍<code>京喜图片库</code>相关优化策略以及关于图片相关的一些关联知识。</p>
<h2 data-id="heading-1">图片性能问题</h2>
<p>作为电商APP，图片在各个业务场景被大量使用。我们需要做到尽可能降低<code>网络消耗</code>/<code>内存消耗</code>/<code>硬盘消耗</code>，同时不降低<code>图片质量</code>，提高图片<code>加载速度</code>，给用户带来更好的使用体验。基于这些性能目标，我们也通过初步性能评估梳理出了一些性能问题：</p>
<h4 data-id="heading-2">图片加载慢/流量消耗高</h4>
<p>图片链接主要由后台接口下发，下发图片<code>格式</code>和<code>尺寸</code>由每个业务后台指定。部分业务没有使用更小的图片格式比如<code>WebP</code>，或图片<code>尺寸</code>过大，都会使图片过大导致网络消耗高。特别是网络状况不佳的场景，图片加载过慢给用户带来不好的体验。同时也会导致更多的<code>I/O读写</code>和<code>解码</code>耗时，造成更多的电量消耗。</p>
<h4 data-id="heading-3">图片内存占用高</h4>
<p>经过初步的APP内存使用评估，图片内存消耗占APP总内存消耗的比例<code>最高</code>，特别是大尺寸图片会占用很多内存。一方面APP占用太高内存退到后台容易被系统杀死，导致下次打开重新启动影响体验。另一方面APP大量使用内存，容易被系统杀死产生<code>OOM</code>。特别是我们目前有大量的低端设备用户，设备内存相对比较低。</p>
<h1 data-id="heading-4">优化方向</h1>
<p>基于上面分析出的一些性能问题，我们对图片框架进行了整体重构优化。一方面是<code>降低</code>图片网络传输，提高图片加载速度。另一方面是<code>减少</code>图片内存消耗。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a95c673969ac4ff78771427deef67368~tplv-k3u1fbpfcp-watermark.image" alt="图片优化.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">最小化网络传输</h2>
<p>京东<code>图片服务器</code>提供了多种处理功能，例如图片<code>格式转换，图片降质，图片缩放，图片圆角</code>等功能。这些功能通过在图片<code>URL</code>中添加特定参数实现，图片服务器会根据参数设置提前将图片处理完成并保存到<code>CDN</code>服务器。我们可以通过添加图片处理参数，减少图片传输大小。</p>
<p>虽然后台可以提前进行<code>URL预处理</code>，下发已添加过图片参数的<code>图片URL</code>。但是由于对接后台业务很多，每个业务图片参数设置差异很大无法统一，而且可能会造成性能影响，例如没有使用<code>webP</code>图片格式，下发太大的<code>图片尺寸</code>。同时考虑到推动各业务后台修改成本也很高，并且前端机型多，不同机型需要使用不同的图片尺寸。另外也不方便灰度降级功能，后续功能修改也不方便。所以在<code>客户端</code>进行图片<code>URL预处理</code>是更好的方式，可以统一控制，也方便之后功能更新。</p>
<h3 data-id="heading-6">图片URL预处理</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec3184fa7db14037aa506d4fd3bf8c9e~tplv-k3u1fbpfcp-zoom-1.image" alt="URL预处理" loading="lazy" referrerpolicy="no-referrer">
图片库在网络图片加载前，检测是否是<code>京东</code>域名的图片<code>URL</code>。如果<code>域名</code>匹配，图片框架先对图片<code>URL</code>进行预处理，预处理包括<code>域名统一</code>，<code>添加缩放参数</code>，<code>添加webP参数</code>，<code>添加降质参数</code>的方式减少图片网络传输大小。</p>
<blockquote>
<p>提示：因为后台返回的图片<code>URL</code>可能会带有一部分图片处理参数，例如<code>https://img11.360buyimg.com/img/pingou-head/25.jpg!webp</code>，直接追加图片参数可能会导致图片处理参数不生效，或格式错误导致加载失败。所以转换时会先将所有图片参数提前计算出来，之后一起处理，避免添加重复参数。</p>
</blockquote>
<h4 data-id="heading-7">域名统一</h4>
<p>目前图片服务器提供了多个图片域名可使用，例如<code>m.360buyimg.com</code>，<code>img10.360buyimg.com</code>等多个域名。<code>m.360buyimg.com</code>主要提供给<code>移动端</code>使用。但是由于对接了各种业务后台，导致接口会下发不同的域名图片。图片使用<code>不同域名</code>可能会导致以下问题：</p>
<ul>
<li><code>不利于缓存复用</code> - 图片框架通常默认以<code>URL</code>字符串生成图片<code>缓存key</code>，不同<code>域名</code>导致生成不同的<code>缓存key</code>。<code>硬盘缓存</code>无法复用会导致图片重复下载，<code>内存缓存</code>无法复用导致同样的图片占用多份内存。</li>
<li><code>不利于HTTP/2连接复用</code> - 大部分界面图片比较多，很多场景都会同时加载多张图片，特别是<code>首屏</code>通常会加载几十张图片。当加载多个图片时，每个域名都需要重新建立<code>HTTPS</code>连接，经历<code>DNS解析/TCP连接/TLS握手</code>过程（目前一次HTTPS请求创建过程大概耗时<code>50-150ms</code>）。如果利用<code>HTTP/2</code>链接复用就只需要创建一次<code>HTTPS</code>请求，之后的图片请求可以减少这部分的耗时。</li>
</ul>
<p>所以在预处理时，如果是<code>京东</code>域名的图片，将图片URL<code>域名</code>统一替换为<code>m.360buyimg.com</code>。</p>
<h4 data-id="heading-8">追加图片参数</h4>
<h5 data-id="heading-9">图片缩放</h5>
<p>很多业务后台返回的原始<code>图片URL</code>的<code>size</code>都比客户端实际显示的<code>size</code>要大。一方面导致使用更多的网络流量造成浪费。另一方面会导致占用更多内存。同时因为图片<code>size</code>和实际显示<code>size</code>不一致导致<code>像素不对齐</code>，<code>GPU</code>需要做额外的插值处理，也会一定的影响渲染性能。所以我们通过添加缩放参数的方式，指定图片服务器下发更小和更匹配实际显示<code>size</code>的图片尺寸。</p>
<h6 data-id="heading-10">动态scale计算尺寸</h6>
<p>因为<code>iOS</code>设备主要使用<code>2x/3x</code>的分辨率，所以业务方使用API时需要传入对应的pt<code>size</code>大小，图片库内部根据设备的<code>scale</code>进行动态计算出真实的像素宽高。</p>
<blockquote>
<p>提示：<code>android</code>设备因为屏幕差异比较大，更适合使用固定的<code>scale</code>。太多的图片尺寸不利于<code>CDN</code>缓存，无缓存的时候需要对图片进行相关参数处理，图片处理本身是耗时操作。</p>
</blockquote>
<h6 data-id="heading-11">Scale降级</h6>
<ul>
<li><code>低端机降级</code> - 对于部分<code>3x</code>scale的低端设备，因为机器本身内存比较低，使用<code>3x</code>分辨率计算出来的图片<code>像素</code>宽高比较大，会造成更多的内存消耗以及解码/渲染更多的性能消耗。所以对于宽高超过一定要求的图片，降级到使用<code>2x</code>分辨率来计算<code>像素</code>宽高，减少设备性能消耗。</li>
<li><code>iPad降级</code> - 因为目前APP并没有针对<code>iPad</code>做特定优化，所以iPad设备下默认是放大显示。这会导致在<code>iPad</code>下图片尺寸计算出来特别大。所以也是针对iPad图片尺寸做了特定限制，防止下发图片尺寸过大。</li>
<li><code>大图片降级</code> - 正常情况下图片<code>宽/高</code>不应该超过屏幕<code>宽/高</code>。为了防止部分业务使用过大的图片<code>size</code>，所以添加了一个限制，最终生成的图片<code>像素</code>尺寸不能超过屏幕<code>宽/高</code>。</li>
</ul>
<h5 data-id="heading-12">降质</h5>
<p>图片服务器支持<code>0-100</code>的图片质量参数设置，通过降低图片质量可以减少图片大小，但是质量降低太多也会影响图片的观看体验。我们将图片质量参数设置为<code>q70</code>，指定图片服务器下发<code>70%</code>质量的图片。对于大部分业务，一方面可以大幅减少图片下载大小，同时也可以保证观看体验。通过添加图片降质参数至少可以减少<code>30-40%</code>的图片大小。</p>
<h5 data-id="heading-13">使用WebP</h5>
<p>按照<code>Google</code>官方的数据，与<code>PNG</code>相比，<code>WebP</code>无损图像的字节数要少<code>26％</code>。<code>WebP</code>有损图像比同类<code>JPG</code>图像字节数少<code>25-34％</code>。图片服务器支持转换<code>webP</code>格式，可以减少图片大小。针对<code>png</code>/<code>jpg</code>图片格式，添加<code>webP</code>参数，指定图片服务器下发<code>webp</code>格式。虽然<code>webP</code>相比<code>png</code>/<code>jpg</code>图片解码需要更长时间，但相对网络传输速度提升还是很大。</p>
<blockquote>
<p>提示：由于目前图片服务器并不支持<code>GIF</code>转<code>webP</code>，GIF并没有做处理。</p>
</blockquote>
<h4 data-id="heading-14">URL预处理缓存</h4>
<p>添加轻量缓存，提高<code>URL</code>转换性能。因为<code>URL</code>转换本身有一定的耗时，而且单个图片<code>URL</code>可能会多次加载/多次转换。转换后的<code>URL</code>会直接保存到缓存中，下次使用可以直接返回。缓存<code>key</code>由<code>URL</code>+相关图片<code>转换参数</code>拼接组成。</p>
<h4 data-id="heading-15">图片API设计</h4>
<p>图片处理参数通过<code>options</code>设置，默认使用<code>q70</code>图片质量以及<code>webP</code>格式。业务方在调用加载图片方法时传入，下面是<code>iOS</code>端的API：</p>
<pre><code class="hljs language-swift copyable" lang="swift">imageView6.jx.setImage(url: <span class="hljs-type">URL</span>(string: <span class="hljs-string">"https://img11.360buyimg.com/img/pingou-head/25.jpg"</span>), 
                       placeholder: <span class="hljs-literal">nil</span>, options: [.imageSize(<span class="hljs-type">CGSize</span>(width: <span class="hljs-number">40</span>, height: <span class="hljs-number">40</span>))])
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">降低图片内存消耗</h2>
<p><code>png</code>/<code>jpg</code>等图片格式在显示之前都需要经过<code>解码</code>生成一张位图，之后根据位图创建<code>纹理</code>传给GPU做渲染。一张位图的内存消耗大概是<code>像素宽</code>x<code>像素高</code>x<code>位深</code>。通常图片使用的是<code>RGBA</code>，位深为32位。一张<code>500px_500px</code>的大概<code>1MB</code>内存。对于<code>GIF</code>图片因为本身有多帧，所以最终的内存消耗为<code>单帧内存</code>x<code>帧数</code>。</p>
<p>我们的优化方向一方面是通过图片缩放的方式，减少图片位图的内存消耗。另一方面限制图片缓存上限避免缓存使用过高。</p>
<h3 data-id="heading-17">图片缩放</h3>
<p>通过上面<code>URL</code>预处理过程让图片服务器下发更小的图片格式，已经降低了一部分内存。但是<code>URL</code>预处理只处理了<code>jd</code>域名的<code>jpg</code>/<code>png</code>图片，对于<code>GIF</code>或<code>京东</code>域名外的图片没有处理，包括一部分<code>URL</code>转换后加载失败的图片。所以对于这部分图片，我们会在端侧做图片缩放的处理，降低内存消耗。例如一张<code>300px_300px</code>包含<code>100帧</code>的GIF图片，实际显示区域只有<code>50px_50px</code>，优化后总内存消耗可从<code>30MB+</code>内存降低到<code>3MB</code>。</p>
<h3 data-id="heading-18">设置图片缓存上限</h3>
<p>图片缓存的设计目的是减少<code>图片解码</code>消耗。图片第一次使用的时候，将图片进行<code>解码</code>后的位图保存在内存中，这样可以避免下次使用时避免<code>重复解码</code>。虽然图片内存高可以尽量避免图片重复解码，但是占用太高内存也会导致APP后台被系统杀掉或产生<code>OOM</code>等问题。所以我们应该将内存缓存控制在一定范围内。</p>
<p>例如<code>iOS</code>的第三方图片库<code>SDWebImage</code>/<code>Kingfisher</code>默认都使用系统库<code>NSCache</code>来实现内存缓存。虽然<code>NSCache</code>会在设备内存紧张时回收内存，但是默认并不限制可保存内存最大字节数，所以在设备内存可用的情况下内存可以一直增加。所以通过设置图片缓存上限，防止图片缓存占用太高内存。图片缓存定义了一个默认的初始值上限，之后对于<code>3x</code>大屏幕设备和<code>高端设备</code>(内存比较高)，适当增加更多内存上限。</p>
<h2 data-id="heading-19">优化成果</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25a92e8bbdbf4b0f89d1b47629d9d3db~tplv-k3u1fbpfcp-zoom-1.image" alt="图片优化成果" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-20">其他收益</h5>
<ul>
<li><code>域名统一</code> - 减少了<code>10%+</code>的重复图片下载和内存消耗。同时减少之前<code>多域名</code>图片加载时重复创建<code>HTTPS</code>请求的过程，减少图片加载时间。</li>
</ul>
<h2 data-id="heading-21">其他策略</h2>
<h3 data-id="heading-22">加载异常处理</h3>
<p>因为少量图片通过<code>URL</code>预处理转换后，可能会存在图片不存在的异常场景导致<code>加载失败</code>。所以当发生图片加载失败时，我们还是需要加载原始图片URL。但是这里需要屏蔽一些特殊的加载错误，避免非必要的加载，例如<code>无网络</code>/<code>网络超时</code>/<code>主动取消加载</code>等错误。之后会将错误图片<code>URL</code>上报到后台，方便之后调整<code>URL</code>转换策略，也可以发现一部分错误的图片<code>URL</code>推动业务修改。同时将这部分连接加入到<code>错误连接</code>缓存中，避免下次重复执行预处理和重复上报。</p>
<h3 data-id="heading-23">线上配置</h3>
<p>目前存在的一些功能，例如<code>URL预处理</code>/<code>统一域名</code>/<code>WebP</code>使用等功能，都添加了线上配置，方便灰度/降级。一在出现问题时可以降级某些功能，新功能上线时也可以进行灰度测试。</p>
<h3 data-id="heading-24">大图检测</h3>
<p>需要有一个机制及时发现图片不符合规范的问题。一方面我们通过线上灰度检测的方式，当发现大图片时会进行上报，后续推动业务方进行优化。另一方面我们在日常测试阶段，会开启<code>Debug</code>检测工具，当检测到大图片时，通过<code>图片翻转</code>/<code>高亮背景颜色</code>的方式提醒业务开发同学进行优化。</p>
<h2 data-id="heading-25">Flutter图片库优化</h2>
<p>目前京喜APP有<code>10+</code>个二级界面是基于<code>Flutter</code>开发，所以我们也针对<code>Flutter</code>图片加载做了一些优化。</p>
<h3 data-id="heading-26">对接原生图片库</h3>
<p>因为<code>Flutter</code>框架自带图片库只提供内存图片缓存，并不支持硬盘缓存，所以会导致图片重复下载。所以我们通过重写<code>ImageProvider</code>，当加载网络图片时，通过<code>Channel</code>调用原生图片库，原生图片库下载图片到本地磁盘后，返回图片文件目录。之后<code>Flutter</code>通过文件目录加载解码图片显示。这样一方面可以利用原生图片库相关优化能力，同时也可以<code>复用</code>图片硬盘缓存避免重复下载。</p>
<h3 data-id="heading-27">减少内存消耗</h3>
<p>使用<code>Image</code>组件时，通过设置<code>cacheHeight</code>/<code>cacheWidth</code>，将图片解码为置顶<code>像素</code>宽高的位图尺寸，减少内存消耗。同时因为<code>Flutter</code>内存消耗相对<code>原生</code>更高，所以在<code>Flutter</code>界面关闭时，通过调用<code>imageCache</code>方法清除图片内存消耗降低内存消耗。</p>
<h3 data-id="heading-28">GIF优化</h3>
<ul>
<li><code>动画优化</code> - 因为通常使用<code>Flutter</code>都是混合栈的机制，<code>原生</code>和<code>Flutter</code>界面在页面导航中相互跳转。所以当<code>Flutter</code>界面存在<code>GIF</code>图片时，跳转到原生以后<code>GIF</code>动画还会一直执行。所以我们通过在<code>Image</code>组件内监听<code>Flutter engine</code>发送的生命周期通知，当Flutter界面不在栈顶时，停止<code>GIF</code>动画执行，减少内存和CPU消耗。</li>
<li><code>减少解码次数</code> - Flutter框架内部对<code>GIF</code>渲染的处理方式，在屏幕每一帧判断当前需要显示的GIF帧，之后对该<code>GIF</code>帧进行解码之后渲染。因为并不会把解码过的帧保存，所以会导致频繁解码导致内存波动大。经过优化，对已经解码过的帧进行保存，避免重复解码的消耗，同时避免内存的波动。</li>
</ul>
<blockquote>
<p>优化前内存波动很明显</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e7e52a269ef4638b9a3af563a1d0b0a~tplv-k3u1fbpfcp-zoom-1.image" alt="优化前" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>优化后内存倾于平稳</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fff1d34493a46eb928a88d8c0b72d4d~tplv-k3u1fbpfcp-zoom-1.image" alt="优化后" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>提示：保存每一帧也会导致更多的内存消耗。目前APP中通常是小尺寸的GIF所以整体可控。可以考虑设置缓冲区上限来控制缓存的图片帧数避免内存过高。</p>
</blockquote>
<h2 data-id="heading-29">后续优化方向</h2>
<h3 data-id="heading-30">更优的缓存算法</h3>
<ul>
<li><code>优先移除最大内存</code> - iOS系统<code>NSCache</code>实现。通过设置最大内存数，当内存不足时优先移除最大的值。</li>
<li><code>LRU缓存</code> - 优先淘汰最久未使用的图片内存。对于很多<code>二级界面</code>的场景，用户打开界面后并不会再次打开。但是因为这些图片缓存是最后使用，所以清除内存时也会最后移除，但是在这种场景下就不太合适。</li>
<li><code>界面栈管理</code> - 当界面<code>关闭</code>时将该界面的所有的图片内存移除，但是对于经常会打开的界面会导致频繁图片<code>编解码</code>也不太合适。</li>
</ul>
<p>所以针对不同的业务场景使用不同的回收方式可能更加合适：</p>
<ul>
<li>对于<code>购物车/我的订单</code>这类界面，用户每次加载的图片基本固定，所以更适合在内存中常驻，当内存消耗过高时再回收。</li>
<li>对于<code>商详/搜索商品列表</code>这类界面，通常商品列表展示的图片不一样并且用户也不会频繁进某一个特定的商详，所以更适合<code>优先</code>移除这部分的内存。</li>
<li>对于部分弹窗功能，图片显示后并不会再次使用，可以考虑不添加到内存中。</li>
</ul>
<h3 data-id="heading-31">使用更好的图片格式</h3>
<p>使用更好的图片格式通常可以带来更小的图片字节大小。同时因为压缩率的提高，可以在减少大小的同时提高图片质量。</p>
<blockquote>
<p>提示：使用系统支持硬解码的图片格式更有优势。硬解码就是使用<code>GPU</code>进行解码，相比使用<code>CPU</code>软解码性能更好更省电。</p>
</blockquote>
<ul>
<li><code>APNG/动画WebP代替GIF</code> - 按照<code>Google</code>官方的说法，<code>GIF</code>转换为<code>有损WebP</code>的字节数缩小了64％，而<code>无损WebP</code>字节数缩小了19％。所以使用<code>动画WebP</code>可以减少更多的网络流量传输。<code>APNG</code>是<code>Mozilla</code>推出的基于<code>PNG</code>的动图格式并且完全支持<code>RGBA</code>，相比<code>GIF</code>可以减少<code>20%+</code>的图片大小。而且<code>GIF</code>本身只支持256色索引颜色以及1位alpha(加上透明度后，边缘会出现明显的锯齿)，使用<code>APNG</code>/<code>WebP</code>也可以带来相比<code>GIF</code>更好的显示效果。</li>
</ul>
<blockquote>
<p>提示：相比<code>GIF</code>，<code>WebP</code>的解码比<code>GIF</code>占用更多的CPU资源。<code>有损WebP</code>的解码时间是<code>GIF</code>的2.2倍，而<code>无损WebP</code>的解码时间是<code>GIF</code>的1.5倍。</p>
</blockquote>
<ul>
<li>
<p><code>HEIC</code> - <code>HEIC</code>是基于<code>H.265</code>视频编码格式推出的图片格式。<code>HEIC</code>相比<code>WebP</code>可以减少20%+的图片大小，并且编解码性能更好。在系统兼容性上，<code>Android 9.0</code>以上的系统支持<code>HEIC</code>。苹果在<code>iOS14</code>以上系统才提供了<code>WebP</code>硬解码，之前的系统只能使用软解码，而<code>HEIC</code>在<code>iOS11</code>之后的机器上都已经支持硬解码，不过并不支持<code>浏览器</code>。</p>
</li>
<li>
<p><code>AVIF</code> - <code>AVIF</code>是基于<code>AV1</code>编码格式推出的图片格式。<code>AVIF</code>相比<code>WebP</code>可以减少30%+的图片大小。不过目前只有<code>Android 12</code>以上的版本支持。</p>
</li>
</ul>
<blockquote>
<p>提示：这里主要是以<code>VP8</code>编码格式的<code>WebP</code>，<code>VP9</code>编码格式的<code>WebP</code>整体性能和<code>HEIC</code>差异不大。</p>
</blockquote>
<p>不过这些图片格式需要图片服务器支持之后才能使用。</p>
<h3 data-id="heading-32">Flutter</h3>
<p>虽然我们对<code>Flutter</code>图片库做了一些优化，但总体上还有很多优化空间。包括业界有在使用的基于<code>纹理</code>的图片方案。在原生侧将图片解码后，通过<code>Flutter</code>引擎创建<code>纹理</code>。之后讲图片纹理<code>id</code>传递给<code>Flutter</code>进行渲染。这样可以统一在原生侧管理图片内存缓存，优化之前<code>Flutter</code>和<code>原生</code>都分别有一份内存缓存的方式。而且针对于混合栈的导航栈方式，也可以更好的进行图片内存回收。另外针对<code>Flutter</code>，需要提供更灵活的图片内存回收策略，避免内存消耗过高。</p>
<blockquote>
<p>提示：纹理可以复用内存中的<code>位图</code>缓存，所以并不会导致更多的内存占用。纹理方式大概能减少<code>30%</code>的内存消耗相比Flutter引擎图片库，主要是一些其他对象使用导致。</p>
</blockquote>
<h3 data-id="heading-33">优化H5图片加载</h3>
<p>我们可以通过拦截<code>WebView</code>图片加载的方式，让原生图片库来下载图片之后传递图片<code>二进制</code>数据给<code>WebView</code>显示。</p>
<h4 data-id="heading-34">减少流量消耗</h4>
<p>通过这种方式，我们可以将原生图片库<code>URL预处理</code>相关功能支持到<code>H5</code>图片，减少<code>H5</code>加载过程中图片流量消耗，提高图片加载速度。同时因为APP<code>原生</code>和<code>WebView</code>图片缓存机制是相互独立的，所以通过统一在原生侧管理图片缓存，可以减少相同图片的重复下载。</p>
<h4 data-id="heading-35">支持更多图片格式</h4>
<p>例如在<code>iOS</code>系统上，<code>WKWebView</code>目前只支持<code>PNG</code>/<code>JPG</code>/<code>GIF</code>图片格式。所以我们可以通过在原生端实现下载<code>WebP</code>/<code>HEIC</code>图片，之后对图片进行<code>解码</code>再传给<code>WebView</code>，这样就可以支持其他图片格式的显示。</p>
<blockquote>
<p>提示：因为<code>WebView</code>不支持直接传递<code>位图</code>二进制数据显示，所以需要提前转换为<code>PNG</code>/<code>JPG</code>二进制数据传递。所以对于其他图片格式增加一次<code>PNG</code>/<code>JPG</code>编码过程会造成更多的性能消耗。不过对于<code>Android</code>系统应该可以在web内核层优化减少这块消耗。</p>
</blockquote>
<h3 data-id="heading-36">图片分辨率</h3>
<p>对于同样的图片，因为<code>分辨率</code>不同导致重复下载。如果能在硬盘缓存做优化，分辨率小的图片可以直接硬盘缓存中的大图片，这样就避免图片重复下载，在解码时生成更小分辨率的位图也不会占用更多内存。</p>
<h1 data-id="heading-37">总结</h1>
<p>本文并没有讲底层图片加载库的具体实现，目前图片库不管是直接用第三方库还是自研图片库实现方式通常差异不大。我们更多是关注自身业务以及如何利用图片服务器能力最大化改善网络图片加载性能。所以部分策略可能不一定针对所有APP都合适，应该针对自身业务场景仔细评估优化方案。</p>
<h1 data-id="heading-38">扩展链接</h1>
<ul>
<li><a href="https://developers.google.com/speed/webp" target="_blank" rel="nofollow noopener noreferrer">WebP</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/265881086" target="_blank" rel="nofollow noopener noreferrer">手淘图片库HEIC使用</a></li>
<li><a href="https://developers.google.com/speed/webp/faq#why_should_i_use_animated_webp" target="_blank" rel="nofollow noopener noreferrer">动画WebP和GIF比较</a></li>
<li><a href="https://caniuse.com/?search=webp" target="_blank" rel="nofollow noopener noreferrer">WebP支持</a></li>
<li><a href="https://caniuse.com/?search=apng" target="_blank" rel="nofollow noopener noreferrer">APNG支持</a></li>
<li><a href="https://jakearchibald.com/2020/avif-has-landed/" target="_blank" rel="nofollow noopener noreferrer">AVIF</a></li>
</ul></div>  
</div>
            