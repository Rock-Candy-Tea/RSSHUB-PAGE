
---
title: 'canvas图像识取技术以及智能化设计的思考'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4aacae065e5e42749867b4e6b8fea5ba~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 04 Jun 2021 23:03:38 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4aacae065e5e42749867b4e6b8fea5ba~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>笔者最近一直在研究 <strong>前端可视化</strong> 和 <strong>搭建化</strong> 的技术, 最近也遇到一个非常有意思的课题, 就是基于设计稿自动提取图片信息, 来智能化出码. 当然本文并不会介绍很多晦涩难懂的技术概念, 我会从几个实际应用场景出发, 介绍如何通过<code>canvas</code>图像识取技术来实现一些有意思的功能. 最后会总结一些对智能化的思考以及对低代码方向的规划, 希望能对各位有所启发.</p>
<h2 data-id="heading-0">canvas图像识取技术</h2>
<p>熟悉前端的朋友们也许对<code>canvas</code>并不陌生, 接下来我会带大家去实现如下几个应用场景, 来深入理解<code>canvas</code>图像识取技术.</p>
<ul>
<li>基于图片动态生成网站主色和渐变色</li>
<li>基于图片/设计稿一键生成网站配色方案</li>
<li>图像识别技术方案</li>
</ul>
<h3 data-id="heading-1">基于图片动态生成网站主色和渐变色</h3>
<p>也许有朋友会问, 基于图片动态生成网站主色和渐变色, 它能解决什么问题呢? 又有怎样的应用场景呢? 这里笔者举几个实际应用的例子.</p>
<p>网易云音乐大家也许不陌生, 细心的朋友也许可以观察到, 网站<strong>banner</strong>部分的背景, 是不是很好的和<strong>banner</strong>形成很好的统一?
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4aacae065e5e42749867b4e6b8fea5ba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们会发现, 每个轮播图的背景都基于当前图片颜色进行的渐变或模糊, 来实现和轮播图实现完美的统一.
目还有还很多类似的例子, 比如图片网站的背景, 图片卡片的背景, 都应用了类似的技术.</p>
<h4 data-id="heading-2">实现原理</h4>
<p>我们知道<code>canvas</code>对象有3个方法:</p>
<ul>
<li><strong>createImageData()</strong> 创建新的、空白的 <code>ImageData</code> 对象</li>
<li><strong>getImageData()</strong> 返回 <code>ImageData</code> 对象，该对象为画布上指定的矩形复制像素数据</li>
<li><strong>putImageData()</strong> 把图像数据（从指定的 ImageData 对象）放回画布上</li>
</ul>
<p>为了分析图片数据, 我们需要用到上述的第二个方法<code>getImageData</code>.
<code>ImageData</code> 对象不是图像，它规定了画布上一个部分（矩形），并保存了该矩形内每个像素的信息。对于 <code>ImageData</code> 对象中的每个像素，都存在着四元信息，即 <code>RGBA</code> 值：</p>
<ul>
<li>R - 红色（0-255）</li>
<li>G - 绿色（0-255）</li>
<li>B - 蓝色（0-255）</li>
<li>A - alpha 通道（0-255; 0 是透明的，255 是完全可见的）</li>
</ul>
<p><code>color/alpha</code> 信息以数组形式存在，并存储于 <code>ImageData</code> 对象的 <code>data</code> 属性中。</p>
<p>有了以上的技术基础, 我们就完全有可能提取到图片的颜色信息, 并分析出图片的主色了. 所以我们的实现流程如下:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/892262ab32234e2ead5f86beef4e389f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实现的参考代码如下:</p>
<pre><code class="hljs language-js copyable" lang="js">img.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    ctx.drawImage(img, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
    img.style.display = <span class="hljs-string">'none'</span>
    <span class="hljs-comment">// 获取像素数据</span>
    <span class="hljs-keyword">let</span> data = context.getImageData(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, img.width, img.height).data
    <span class="hljs-comment">// ImageData.data 类型为Uint8ClampedArray的一维数组，每四个数组元素代表了一个像素点的RGBA信息，每个元素数值介于0~255</span>
    <span class="hljs-keyword">let</span> r = <span class="hljs-number">0</span>,
        g = <span class="hljs-number">0</span>,
        b = <span class="hljs-number">0</span>
        
    <span class="hljs-comment">// 取所有像素平均值</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> row = <span class="hljs-number">0</span>; row < img.height; row++) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> col = <span class="hljs-number">0</span>; col < img.width; col++) &#123;
            r += data[(img.width * row + col) * <span class="hljs-number">4</span>]
            g += data[(img.width * row + col) * <span class="hljs-number">4</span> + <span class="hljs-number">1</span>]
            b += data[(img.width * row + col) * <span class="hljs-number">4</span> + <span class="hljs-number">2</span>]
        &#125;
    &#125;
    
    <span class="hljs-comment">// 计算平均值</span>
    r /= img.width * img.height
    g /= img.width * img.height
    b /= img.width * img.height

    <span class="hljs-comment">// 将结果取整</span>
    r = <span class="hljs-built_in">Math</span>.round(r)
    g = <span class="hljs-built_in">Math</span>.round(g)
    b = <span class="hljs-built_in">Math</span>.round(b)
    
    <span class="hljs-comment">// 给背景设置渐变</span>
    bgBox.style.backgroundImage = <span class="hljs-string">`linear-gradient(rgb(<span class="hljs-subst">$&#123;r&#125;</span>), rgb(<span class="hljs-subst">$&#123;g&#125;</span>), rgb(<span class="hljs-subst">$&#123;b&#125;</span>)`</span>;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>值得说明的是, 根据不同的区值场景, 我们还可以用到其他算法诸如:</p>
<ul>
<li>平均值算法(获取主色调)</li>
<li>中位切分法（获取png图片的主色）</li>
<li>互补色计算法</li>
</ul>
<h3 data-id="heading-3">基于图片/设计稿一键生成网站配色方案</h3>
<p>以上介绍了使用<code>canvas</code>的取色方案, 接下来我们更进一步, 来探索一下如何基于图片/设计稿一键生成网站配色方案.</p>
<p>其实基于以上的例子我们完全可以自己实现一套网站配色生成工具, 这里为了节约时间, 笔者推荐一款比较强大的插件, 来帮我们实现类似的功能.</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1acad6696394d91afe7cc0ed575d629~tplv-k3u1fbpfcp-watermark.image" alt="chrome-capture.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>没错, 就是<code>colorthief</code>, 它支持浏览器和node环境, 所以作为前端, 我们可以很轻松的使用它并获取图像/设计稿的配色方案.</p>
<p>github传送门: <a href="https://github.com/lokesh/color-thief" target="_blank" rel="nofollow noopener noreferrer">在线生成图片色系方案库</a></p>
<p>简单的使用例子如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> ColorThief <span class="hljs-keyword">from</span> <span class="hljs-string">'./node_modules/colorthief/dist/color-thief.mjs'</span>

<span class="hljs-keyword">const</span> colorThief = <span class="hljs-keyword">new</span> ColorThief();
<span class="hljs-keyword">const</span> img = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'img'</span>);

<span class="hljs-keyword">if</span> (img.complete) &#123;
  colorThief.getColor(img);
&#125; <span class="hljs-keyword">else</span> &#123;
  image.addEventListener(<span class="hljs-string">'load'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    colorThief.getColor(img);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该库还有很多细化的<code>api</code>,比如控制生成质量, 粒度等, 我们可以以用它做一些更加智能的工具.</p>
<h3 data-id="heading-4">图像识别技术方案</h3>
<blockquote>
<p>图像识别技术可以帮助技术人员利用计算机对图像进行处理和分析，更好地识别各种不同模式的目标。 图像识别的过程和内容是比较多的，主要包括图像预处理和图像分割等内容，它在图像处理中的有效应用，还能够根据图像的特点对其进行判断匹配，让用户能够更加快速的地在图片中搜索自己想要获取的信息。</p>
</blockquote>
<p>了解神经网络的朋友可能知道, 图像识别技术真正的解决方案是 <strong>卷积神经网络</strong>(CNNs或ConvNets).</p>
<p>从图像识别技术的术语来说就是，卷积神经网络按照关联程度筛选不必要的连接，进而使图像识别过程在计算上更具有可操作性。卷积神经网络有意地限制了图像识别时候的连接，让一个神经元只接受来自之前图层的小分段的输入（假设是3×3或5×5像素），避免了过重的计算负担。因此，每一个神经元只需要负责处理图像的一小部分。</p>
<p>当然作为前端工程师, 我们可能还涉及不到这么深的内容, 不过也不用担心, 目前已有很多工具帮我们解决了底层的分析难题. 比如国内比较有名的<code>imgcook</code>, 通过识别技术来生成可被浏览器消费的<code>html</code>代码.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fe93c1c82964d44bb310dce900a3cab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其工作机制如下:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1976a77171774efa956180acdf69dd15~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其底层识别技术也是基于对图片信息元的分析, 提取和转化, 来实现智能化编排的目的. 当然也有一些开源的库可以帮我们做到一定程度的识别能力. 我们可以基于这些方案, 制作一些对开发更智能化的工具.</p>
<p>这里笔者提一个图片识别的库<strong>GOCR.js</strong>, 供大家参考学习.</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c2b55d0e3ba46768a5d8f63d567734b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>GOCR.js 是 GOCR（开源的 OCR 光学识别程序）项目的纯 JavaScript 版本，使用 Emscripten 进行自动转换。这是一个简单的 OCR （光学字符识别）程序，可以扫描图像中的文字回文本。</p>
</blockquote>
<p>该库的使用也非常简单, 我们只需要引入该库, 输入如下代码即可:</p>
<pre><code class="copyable">var string = GOCR(image);
alert(string);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>演示如下:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dc18a1b4b544442bf47d91efb14bbfd~tplv-k3u1fbpfcp-watermark.image" alt="chrome-capture (1).gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">智能化思考</h2>
<p>最近几年国内外<code>lowcode</code>和<code>nocode</code>平台发展迅猛, 对于基础的搭建化已不能满足科技企业的需求, 智能化/自动化搭建平台不断涌现. 笔者之前文章 <a href="https://juejin.cn/post/6966242039318970399" target="_blank">分享10款2021年国外顶尖的lowcode开发平台</a> 也介绍过很多国外的优秀<code>lowcode</code>平台, 很多也对智能化有了很多的实践落地. 笔者简化如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecca0cab41114ba19d21578d17a82702~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最近<strong>H5-Dooring</strong>可视化编辑器也在持续推迭代, 数据源已基本搭建完成, 后续还会按照更智能化的方向, 可视化大屏<strong>V6.Dooring</strong>也已上线第一个版本.</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c63e431f1eb3472095a22934b210f85f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>国内lowcode平台仍然有很长的路要走, 期待大家一起努力💪!</p>
<p>更多 <strong>低代码</strong> / <strong>可视化</strong> 相关的技术分享和实现, 欢迎 <strong>微信</strong> 搜索 <strong>趣谈前端</strong> 学习探索.</p></div>  
</div>
            