
---
title: '利用G渲染器实现的音频可视化方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d53bbdbe7c49420696dcb2765b99e1d1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 16:37:04 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d53bbdbe7c49420696dcb2765b99e1d1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>利用阿里Antvis出品的G底层图形渲染器，结合AudioContext提供的音频数据获取API，实现出类似网易云播放音频特效。</p>
<p>项目地址：</p>
<ul>
<li><a href="https://github.com/leon-kfd/g-music-visualizer" target="_blank" rel="nofollow noopener noreferrer">⚡Github</a></li>
<li><a href="https://leon-kfd.github.io/g-music-visualizer/" target="_blank" rel="nofollow noopener noreferrer">💡Demo</a></li>
</ul>
<h2 data-id="heading-0">🍭关于G渲染器</h2>
<p><code>G</code>是一款易用、高效、强大的 2D 可视化渲染引擎，提供 Canvas、SVG 等多种渲染方式的实现。目前，已有多个顶级的可视化开源项目基于<code>G</code>开发，比如图形语法库<code>G2</code>、图可视化库<code>G6</code>等。</p>
<p>作为一个底层渲染器，其内置了许多常用的内置图形，提供完整的DOM事件模拟，同时提供了流程的动画实现，这些特性对我们这次实现音频特效都是很有必要的。</p>
<p>目前与<code>G</code>相似的竞品还有<code>Echart</code>的<code>ZRender</code>，相比较以我个人看法来说，Zrender提供的API更丰富，但是上手难度比G要高一点，而<code>G</code>的API相对<code>简洁</code>一点。</p>
<p>类似的还有老大哥<code>d3</code>，这个相较以上两个更底层，API更丰富，但上手难度就更大了。同时<code>g</code>里面的一些方法好像也是参考了<code>d3</code>算法思路。</p>
<p><a href="https://g.antv.vision/zh/docs/api/canvas" target="_blank" rel="nofollow noopener noreferrer">G官方文档</a> <em>（这里吐槽说一下，G的官方文档感觉还有很大优化空间，实在太简洁了，很多API都是一笔带过，用法也不怎么说明）</em></p>
<h2 data-id="heading-1">🌟AudioContext读取音频数据</h2>
<p>实现音频特效动画的前提是需要拿到一个音频的音频数据，浏览网上一些方案后，发现<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/AudioContext" target="_blank" rel="nofollow noopener noreferrer">AudioContext</a>含有相关的API。</p>
<p>原理：</p>
<ul>
<li>首先需要基于<code>AudioContext.createAnalyser()</code>创建一个<code>Analyser</code></li>
<li>为<code>Analyser</code>关联音频源，目前常用的音频源方式一般为以下两个
<ul>
<li><code>createMediaElementSource()</code>: 关联到<code>audio</code>或<code>video</code>标签中（当前方案选择了这个）</li>
<li><code>createMediaStreamSource()</code>: 关联到本地计算机或网络音频媒体流对象</li>
</ul>
</li>
<li>创建<code>Gain</code>音量节点并关联到<code>Analyser</code>的<code>destination</code>中</li>
<li>通过<code>AnalyserNode.getByteFrequencyData()</code>方法将当前频率数据复制到传入的最终需读取音频的Uint8Array中</li>
</ul>
<p>把以上操作封装到一个类中，便于初始化，可参考以下代码:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// src/plugins/MusicVisualizer.ts</span>
<span class="hljs-keyword">const</span> _analyser = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.AudioContext();

<span class="hljs-keyword">type</span> MusicVisualizerOptions = &#123;
    audioEl?: HTMLAudioElement;
    size?: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MusicVisualizer</span> </span>&#123;
    <span class="hljs-keyword">private</span> analyser: AnalyserNode;
    <span class="hljs-keyword">private</span> gainNode: GainNode;
    <span class="hljs-keyword">private</span> audioSource?: MediaElementAudioSourceNode;
    <span class="hljs-keyword">private</span> options: MusicVisualizerOptions & &#123;
            <span class="hljs-attr">size</span>: <span class="hljs-built_in">number</span>
    &#125;;
    <span class="hljs-keyword">private</span> visualArr: <span class="hljs-built_in">Uint8Array</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options?: MusicVisualizerOptions</span>)</span> &#123;
        <span class="hljs-keyword">const</span> defaultOptions = &#123;
            <span class="hljs-attr">size</span>: <span class="hljs-number">128</span>
        &#125;
        <span class="hljs-built_in">this</span>.options = &#123;
            ...defaultOptions,
            ...options
        &#125;
        <span class="hljs-built_in">this</span>.analyser = _analyser.createAnalyser();
        <span class="hljs-built_in">this</span>.analyser.fftSize = <span class="hljs-built_in">this</span>.options.size * <span class="hljs-number">2</span>;
        <span class="hljs-built_in">this</span>.gainNode = _analyser.createGain();
        <span class="hljs-built_in">this</span>.gainNode.connect(_analyser.destination);
        <span class="hljs-built_in">this</span>.analyser.connect(<span class="hljs-built_in">this</span>.gainNode);
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.options.audioEl) &#123;
            <span class="hljs-built_in">this</span>.audioSource = _analyser.createMediaElementSource(<span class="hljs-built_in">this</span>.options.audioEl)
            <span class="hljs-built_in">this</span>.audioSource.connect(<span class="hljs-built_in">this</span>.analyser)
        &#125;
        <span class="hljs-built_in">this</span>.visualArr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>(<span class="hljs-built_in">this</span>.analyser.frequencyBinCount);
        <span class="hljs-built_in">this</span>.resumeAudioContext();
    &#125;
    <span class="hljs-comment">// 新版Chrome Audio需要有交互行为后才可以利用JS执行播放</span>
    <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">resumeAudioContext</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (_analyser) &#123;
            <span class="hljs-keyword">const</span> resumeAudio = <span class="hljs-function">() =></span> &#123;
                <span class="hljs-keyword">if</span> (_analyser.state === <span class="hljs-string">'suspended'</span>) _analyser.resume();
                <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'click'</span>, resumeAudio)
            &#125;
            <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'click'</span>, resumeAudio)
        &#125;
    &#125;
    <span class="hljs-comment">// 更换Audio</span>
    <span class="hljs-function"><span class="hljs-title">setAudioEl</span>(<span class="hljs-params">el: HTMLAudioElement</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.audioSource) &#123;
            <span class="hljs-built_in">this</span>.audioSource.disconnect(<span class="hljs-built_in">this</span>.analyser)
        &#125;
        <span class="hljs-built_in">this</span>.audioSource = _analyser.createMediaElementSource(el)
        <span class="hljs-built_in">this</span>.audioSource.connect(<span class="hljs-built_in">this</span>.analyser)
    &#125;
    <span class="hljs-comment">// 获取音频频域数据</span>
    <span class="hljs-function"><span class="hljs-title">getVisualizeValue</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.analyser.getByteFrequencyData(<span class="hljs-built_in">this</span>.visualArr)
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.visualArr;
    &#125;
    <span class="hljs-comment">// 更改音量</span>
    <span class="hljs-function"><span class="hljs-title">changeVolumn</span>(<span class="hljs-params">value: <span class="hljs-built_in">number</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.gainNode.gain.value = value
    &#125;
    <span class="hljs-comment">// 卸载</span>
    <span class="hljs-function"><span class="hljs-title">destory</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.analyser.disconnect(<span class="hljs-built_in">this</span>.gainNode);
        <span class="hljs-built_in">this</span>.audioSource?.disconnect(<span class="hljs-built_in">this</span>.analyser)
        <span class="hljs-built_in">this</span>.gainNode.disconnect(_analyser.destination);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化之后，就可以监听Audio的播放事件，当播放时利用<code>getVisualizeValue()</code>方法获取到实时音频（可结合利用requestAnimationFrame或setTimeout获取），这里因为是做可视化动画，当然是利用<code>requestAnimationFrame</code>读取每帧的数据后渲染。</p>
<p>还有一个需要注意的点，当Audio的数据源是网络音频时，有可能会出现无法读取到音频数据的问题。这个问题一般可能是因为网络音频的<strong>跨域限制</strong>，需要为Audio标签加入<code>crossOrigin="anonymous"</code>属性。
一般的CDN资源是很少设置AccessHeader跨域限制的，但加入这个属性后仍然出现了跨域的报错，说明这网络路径是设置了跨域限制的，这时候可以考虑用Nginx反向代理或服务端解决。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">audio</span> <span class="hljs-attr">controls</span> <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;audioURL&#125;</span> <span class="hljs-attr">crossOrigin</span>=<span class="hljs-string">"anonymous"</span>></span><span class="hljs-tag"></<span class="hljs-name">audio</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">🌈可视化特效实现</h2>
<p><strong>以下选取项目部分功能的实现原理进行说明</strong></p>
<h3 data-id="heading-3">专辑图片旋转动画</h3>
<p>因为每个示例都需要用到专辑图片旋转动画，因此为了方便把专辑图片的创建抽离了出来。</p>
<p>在G中画一个圆形图片需要用到<code>Clip</code>，这个在文档中并没有说明，但从github中找到了该用法。</p>
<p>旋转动画不能直接使用基础属性模拟，这里用到了矩阵变换，利用<code>shape.getMatrix()</code>获取初始矩阵，再通过<code>transform</code>计算出每个<code>ratio</code>对应的矩阵。</p>
<p><code>transform</code>是G提供的一个扩展矩阵变换方法，接收2个参数，第一个是当前矩阵，第二个参数是Action数组。这里的旋转对应的action是:</p>
<pre><code class="copyable">['t', -x, -y],
['r', 旋转角度],
['t', x, y],
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d53bbdbe7c49420696dcb2765b99e1d1~tplv-k3u1fbpfcp-watermark.image" alt="play.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码参考如下:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Canvas &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@antv/g-canvas"</span>;
<span class="hljs-keyword">import</span> &#123; ext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@antv/matrix-util'</span>;

<span class="hljs-keyword">const</span> &#123; transform &#125; = ext <span class="hljs-comment">// G提供的矩阵变换快捷方法</span>

<span class="hljs-keyword">type</span> ImageCircleConfig = &#123;
  <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>;
  y: <span class="hljs-built_in">number</span>;
  r: <span class="hljs-built_in">number</span>;
  shadowColor?: <span class="hljs-built_in">string</span>
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getImageCircle</span>(<span class="hljs-params">canvas: Canvas, &#123; x, y, r, shadowColor &#125;: ImageCircleConfig</span>) </span>&#123;
  <span class="hljs-keyword">const</span> shadowConfig = shadowColor ? &#123;
    shadowColor,
    <span class="hljs-attr">shadowBlur</span>: <span class="hljs-number">16</span>
  &#125; : &#123;&#125;
  canvas.addShape(<span class="hljs-string">'circle'</span>, &#123;
    <span class="hljs-attr">attrs</span>: &#123;
      x,
      y,
      r,
      <span class="hljs-attr">fill</span>: <span class="hljs-string">'#262626'</span>,
      ...shadowConfig
    &#125;
  &#125;)
  <span class="hljs-keyword">const</span> shape = canvas.addShape(<span class="hljs-string">'image'</span>, &#123;
    <span class="hljs-attr">attrs</span>: &#123;
      <span class="hljs-attr">x</span>: x - r,
      <span class="hljs-attr">y</span>: y - r,
      <span class="hljs-attr">width</span>: <span class="hljs-number">2</span> * r,
      <span class="hljs-attr">height</span>: <span class="hljs-number">2</span> * r,
      <span class="hljs-attr">img</span>: <span class="hljs-string">`https://source.unsplash.com/random/<span class="hljs-subst">$&#123;<span class="hljs-number">2</span> * r&#125;</span>x<span class="hljs-subst">$&#123;<span class="hljs-number">2</span> * r&#125;</span>?Nature`</span>
    &#125;
  &#125;)
  shape.setClip(&#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'circle'</span>,
    <span class="hljs-attr">attrs</span>: &#123;
      x,
      y,
      r
    &#125;
  &#125;)
  <span class="hljs-comment">// 旋转动画</span>
  <span class="hljs-keyword">const</span> matrix = shape.getMatrix()
  <span class="hljs-keyword">const</span> radian = <span class="hljs-number">2</span> * <span class="hljs-built_in">Math</span>.PI <span class="hljs-comment">// 旋转360度</span>
  shape.animate(<span class="hljs-function">(<span class="hljs-params">ratio: <span class="hljs-built_in">number</span></span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">matrix</span>: transform(matrix, [
        [<span class="hljs-string">'t'</span>, -x, -y],
        [<span class="hljs-string">'r'</span>, radian * ratio],
        [<span class="hljs-string">'t'</span>, x, y],
      ])
    &#125;
  &#125;, &#123;
    <span class="hljs-attr">duration</span>: <span class="hljs-number">10000</span>,
    <span class="hljs-attr">repeat</span>: <span class="hljs-literal">true</span>
  &#125;)
  <span class="hljs-comment">// 创建后先暂停动画，等待播放后再恢复</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    shape.pauseAnimate()
  &#125;)
  <span class="hljs-keyword">return</span> shape
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">在圆上的点</h3>
<p>示例中经常要计算的就是在圆上的点，以柱状条特效（示例一）为例，首先就是要出围绕着圆的平均64个点作为初始坐标。</p>
<p>可通过利用当前点与圆心的夹角结合简单三角函数运算出x,y的偏移量。</p>
<p>如下图, <strong>l = cos(θ) * r</strong>, <strong>t = sin(θ) * r</strong>, 通过圆心O坐标加上偏移量即可算出点A坐标。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d3ca5377137458e84dd60d09683c618~tplv-k3u1fbpfcp-watermark.image" alt="deg.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// POINT_NUM = 64 柱状条数</span>
sArr.current = <span class="hljs-built_in">Array</span>.from(&#123; <span class="hljs-attr">length</span>: POINT_NUM &#125;, <span class="hljs-function">(<span class="hljs-params">item, index: <span class="hljs-built_in">number</span></span>) =></span> &#123;
    <span class="hljs-keyword">const</span> deg = index * (<span class="hljs-number">360</span> / POINT_NUM) - <span class="hljs-number">150</span>;  <span class="hljs-comment">// 当前角度</span>
    <span class="hljs-keyword">const</span> l = <span class="hljs-built_in">Math</span>.cos(deg * <span class="hljs-built_in">Math</span>.PI / <span class="hljs-number">180</span>)    <span class="hljs-comment">// x方向偏移系数</span>
    <span class="hljs-keyword">const</span> t = <span class="hljs-built_in">Math</span>.sin(deg * <span class="hljs-built_in">Math</span>.PI / <span class="hljs-number">180</span>)       <span class="hljs-comment">// y方向偏移系数</span>
    <span class="hljs-keyword">const</span> r = R + OFFSET
    <span class="hljs-keyword">return</span> (canvas.current <span class="hljs-keyword">as</span> Canvas).addShape(<span class="hljs-string">'rect'</span>, &#123;
        <span class="hljs-attr">attrs</span>: &#123;
            <span class="hljs-attr">width</span>: RECT_WIDTH,
            <span class="hljs-attr">height</span>: RECT_WIDTH,
            <span class="hljs-attr">radius</span>: RECT_WIDTH / <span class="hljs-number">2</span>,
            <span class="hljs-attr">x</span>: X + l * r - RECT_WIDTH / <span class="hljs-number">2</span>,
            <span class="hljs-attr">y</span>: Y + t * r - RECT_WIDTH / <span class="hljs-number">2</span>,
            <span class="hljs-attr">fill</span>: RECT_COLOR
        &#125;
    &#125;).rotateAtPoint(X + l * r, Y + t * r, (deg - <span class="hljs-number">90</span>) * <span class="hljs-built_in">Math</span>.PI / <span class="hljs-number">180</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里每个柱状条都需要进行旋转来围绕圆排列，使用的是<code>rotateAtPoint</code>绕着初始点旋转对应角度。</p>
<p>基本所有的示例都需要首先计算出围绕圆的点坐标，都是采用这种方式计算即可。</p>
<h3 data-id="heading-5">使用Path绘制圆形</h3>
<p>某些场景下需实现一些类圆动画（示例二、三），但圆形是无法实现这种动画的，这时候可以采用Path实现。</p>
<p>在初始状态未进行播放时，默认会显示一个圆形，这是为了减少创建一个圆的实例，可以直接利用Path绘制出圆形，后续的动画直接更改这个Path实例。</p>
<p>可以使用2个圆弧生成生成一个圆形的Path， 参考以下代码</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getCirclePath</span>(<span class="hljs-params">cx: <span class="hljs-built_in">number</span>, cy: <span class="hljs-built_in">number</span>, r: <span class="hljs-built_in">number</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`M <span class="hljs-subst">$&#123;cx - r&#125;</span>, <span class="hljs-subst">$&#123;cy&#125;</span>
  a <span class="hljs-subst">$&#123;r&#125;</span>, <span class="hljs-subst">$&#123;r&#125;</span> 0 1, 0 <span class="hljs-subst">$&#123;r * <span class="hljs-number">2</span>&#125;</span>, 0 
  a <span class="hljs-subst">$&#123;r&#125;</span>, <span class="hljs-subst">$&#123;r&#125;</span> 0 1, 0 <span class="hljs-subst">$&#123;-r * <span class="hljs-number">2</span>&#125;</span>, 0`</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">通过点形成平滑曲线</h3>
<p>若仅仅是将目标一组点连接成线，在视觉效果上会显得很突兀，及时改换成Path来连接成曲线也是不够平滑。</p>
<p>这时候可以采用插值法为连续目标点再插入中间点来为Path更加平滑，一般来说都是采用<code>三次样条插值</code>算法实现。</p>
<p>在d3中内置了很多连线算法方案，可以直接采用。在本次的示例中，遇到多个点生成平滑曲线的都是采用了d3的<a href="https://d3js.org.cn/document/d3-shape/#curves" target="_blank" rel="nofollow noopener noreferrer">curveCardinalClosed</a>算法来生成Path路径。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// s-path.tsx</span>
<span class="hljs-keyword">import</span> &#123; line, curveCardinalClosed &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'d3'</span>
<span class="hljs-comment">// some other code...</span>
useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (props.data?.length) &#123;
        <span class="hljs-keyword">const</span> pathArr: <span class="hljs-built_in">any</span>[] = [[],[],[],[]]
        getArray(props.data).map(<span class="hljs-function">(<span class="hljs-params">item,index</span>) =></span> &#123;
            pathArr[index % <span class="hljs-number">4</span>].push(getPointByIndex(index, item * item / <span class="hljs-number">65025</span> * POINT_OFFSET + <span class="hljs-number">4</span>))
        &#125;)
        pathArr.map(<span class="hljs-function">(<span class="hljs-params">item,index</span>) =></span> &#123;
            <span class="hljs-comment">// 使用d3的curveCardinalClosed为目标点数组插值生成平滑曲线Path</span>
            <span class="hljs-keyword">const</span> path = line().x(<span class="hljs-function">(<span class="hljs-params">d: [<span class="hljs-built_in">number</span>,<span class="hljs-built_in">number</span>]</span>) =></span> d[<span class="hljs-number">0</span>]).y(<span class="hljs-function">(<span class="hljs-params">d: [<span class="hljs-built_in">number</span>, <span class="hljs-built_in">number</span>]</span>) =></span> d[<span class="hljs-number">1</span>]).curve(curveCardinalClosed)(item)
            sPathArr.current[index]?.attr(<span class="hljs-string">'path'</span>, path)
        &#125;)
    &#125;
&#125;, [ props.data ])
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>d3</code>其他平滑曲线算法示例可参考笔者在很久以前写的Demo: <a href="https://kongfandong.cn/blog/d3-mulitpoint-connection/" target="_blank" rel="nofollow noopener noreferrer">Click here</a></p>
<h3 data-id="heading-7">在圆上的点跟随圆放大的同时做圆周运动</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c35cd0f095f5466a92924e56f424a7cd~tplv-k3u1fbpfcp-watermark.image" alt="circle.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>示例五中的动画会出现在圆上的点跟随圆放大的同时做圆周运动，这种动画在实现时有两种方案：</p>
<p>第一种，是大圆利用Path模拟，然后动画开始后在每帧动画中，利用<code>Path.getPoint(ratio: number)</code>获取当前大圆中点当前帧下某个对应点的坐标。</p>
<p>第二种，是直接计算出当前帧下这个点在圆上的位置，利用三角函数结合大圆的放大偏移系数与<code>ratio</code>即可计算出当前点坐标。</p>
<p>在实现第一种方案时，发现效果不太理想，不知道是不是有setTimeout的原因，弃用了然后选择了方案二实现。</p>
<p>部分参考代码如下:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">Array</span>.from(&#123; <span class="hljs-attr">length</span>: CIRCLE_NUM &#125;, <span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
    circleArrStart.current.push(<span class="hljs-literal">false</span>)
    <span class="hljs-comment">// circle大圆</span>
    circleArr.current.push(addCircle())
    circleArr.current[index].animate(<span class="hljs-function">(<span class="hljs-params">ratio: <span class="hljs-built_in">number</span></span>) =></span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">r</span>: R + ratio * CIRCLE_SCALE_OFFSET,
            <span class="hljs-comment">// path: getCirclePath(X, Y, R + ratio * 80),</span>
            <span class="hljs-attr">opacity</span>: ratio > <span class="hljs-number">0.02</span> && ratio < <span class="hljs-number">0.9</span> ? <span class="hljs-number">0.8</span> - ratio * <span class="hljs-number">0.8</span> : <span class="hljs-number">0</span>
        &#125;
    &#125;, animateOption)
    <span class="hljs-comment">// circle-dot大圆上的点</span>
    circleDotArr.current.push(addCircleDot())
    circleDotDegArr.current.push(<span class="hljs-number">0</span>)
    circleDotArr.current[index].animate(<span class="hljs-function">(<span class="hljs-params">ratio: <span class="hljs-built_in">number</span></span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (props.data && ratio < <span class="hljs-number">0.05</span> && !circleDotDegArr.current[index]) &#123;
            circleDotDegArr.current[index] = pickStartPoint()
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (ratio > <span class="hljs-number">0.9</span>) &#123;
            circleDotDegArr.current[index] = <span class="hljs-number">0</span>
        &#125;
        <span class="hljs-keyword">const</span> deg = circleDotDegArr.current[index] + ratio * <span class="hljs-number">360</span> - <span class="hljs-number">180</span>
        <span class="hljs-keyword">const</span> l = <span class="hljs-built_in">Math</span>.cos(deg * <span class="hljs-built_in">Math</span>.PI / <span class="hljs-number">180</span>)
        <span class="hljs-keyword">const</span> t = <span class="hljs-built_in">Math</span>.sin(deg * <span class="hljs-built_in">Math</span>.PI / <span class="hljs-number">180</span>)
        <span class="hljs-keyword">const</span> r = R + ratio * CIRCLE_SCALE_OFFSET
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">x</span>: X + l * r,
            <span class="hljs-attr">y</span>: Y + t * r,
            <span class="hljs-attr">r</span>: DOT_R * (<span class="hljs-number">1</span> - ratio / <span class="hljs-number">2</span>),
            <span class="hljs-attr">opacity</span>: ratio > <span class="hljs-number">0.05</span> && ratio < <span class="hljs-number">0.9</span> ? <span class="hljs-number">0.8</span> - ratio * <span class="hljs-number">0.8</span> : <span class="hljs-number">0</span>
        &#125;
    &#125;, animateOption)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">粒子特效的实现</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e05ae8b50c0438687d24c69d1845f14~tplv-k3u1fbpfcp-watermark.image" alt="particle.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>示例六是一个粒子特效效果，也是实现这么多示例中耗时比较多的一个，这里拿出来说一下实现原理。</p>
<p>与其他示例一样初始化时，先初始化出专辑圆形图。</p>
<p>然后准备初始化粒子，定义圆形作为粒子形状，尽量小一点，可以开启阴影效果，但是性能会很差，这次就把Shadow阴影关闭了。</p>
<p>定义每个取样点周围的粒子数，当前为64个音频样点，一个样点设置12个粒子（可以更多，同样越多就约耗能），最终粒子数为64 X 12个。</p>
<p>使用随机值生成粒子样点，这里可以使用样点当前角度再随机偏移一定量即可生成均匀的粒子。</p>
<p>粒子效果的比较难的在于动画上，要选择一个合适的漂浮动画函数。这次示例选择了<code>正弦函数</code>实现左右均匀漂浮，在加上利用<code>setTimeout</code>随机延迟粒子生成时间即可完成粒子按一定规律下漂浮的动画。</p>
<p>定义粒子动画时，通过正弦函数与ratio计算出每帧粒子的实际x,y坐标即可。因为这次还会结合当前音频数据，让某个样点的粒子飘得高一点，让粒子的偏移量加大，这时还需要进一步对动画进行更改。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// POINT_NUM = 64 样点数</span>
<span class="hljs-comment">// PARTICLE_NUM = 12 样点周围粒子数</span>
<span class="hljs-built_in">Array</span>.from(&#123; <span class="hljs-attr">length</span>: POINT_NUM &#125;, <span class="hljs-function">(<span class="hljs-params">point, index1</span>) =></span> &#123;
    <span class="hljs-built_in">Array</span>.from(&#123; <span class="hljs-attr">length</span>: PARTICLE_NUM &#125;, <span class="hljs-function">(<span class="hljs-params">particle, index2</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> deg = index1 * (<span class="hljs-number">360</span> / POINT_NUM) - <span class="hljs-number">150</span> + (<span class="hljs-built_in">Math</span>.random() - <span class="hljs-number">0.5</span>) * <span class="hljs-number">10</span>;
        <span class="hljs-keyword">const</span> l = <span class="hljs-built_in">Math</span>.cos(deg * <span class="hljs-built_in">Math</span>.PI / <span class="hljs-number">180</span>)
        <span class="hljs-keyword">const</span> t = <span class="hljs-built_in">Math</span>.sin(deg * <span class="hljs-built_in">Math</span>.PI / <span class="hljs-number">180</span>)
        <span class="hljs-keyword">const</span> r = R + OFFSET
        <span class="hljs-keyword">const</span> x = X + l * r
        <span class="hljs-keyword">const</span> y = Y + t * r
        <span class="hljs-keyword">const</span> particleShape = (canvas.current <span class="hljs-keyword">as</span> Canvas).addShape(<span class="hljs-string">'circle'</span>, &#123;
            <span class="hljs-attr">attrs</span>: &#123;
                x,
                y,
                <span class="hljs-attr">r</span>: <span class="hljs-number">0.8</span>,
                <span class="hljs-attr">fill</span>: <span class="hljs-string">'#fff'</span>,
                <span class="hljs-attr">opacity</span>: <span class="hljs-number">0</span>,
                <span class="hljs-comment">// ⚠开启阴影会掉帧</span>
                <span class="hljs-comment">// shadowColor: '#fcc8d9',</span>
                <span class="hljs-comment">// shadowBlur: 1</span>
            &#125;
        &#125;)
        particleShape.animate(<span class="hljs-function">(<span class="hljs-params">ratio: <span class="hljs-built_in">number</span></span>) =></span> &#123;
            <span class="hljs-keyword">const</span> deg = index1 * (<span class="hljs-number">360</span> / POINT_NUM) - <span class="hljs-number">150</span> + <span class="hljs-built_in">Math</span>.sin(ratio * <span class="hljs-number">20</span>) * <span class="hljs-number">4</span>;
            <span class="hljs-keyword">const</span> l = <span class="hljs-built_in">Math</span>.cos(deg * <span class="hljs-built_in">Math</span>.PI / <span class="hljs-number">180</span>)
            <span class="hljs-keyword">const</span> t = <span class="hljs-built_in">Math</span>.sin(deg * <span class="hljs-built_in">Math</span>.PI / <span class="hljs-number">180</span>)
            <span class="hljs-keyword">const</span> _index = POINT_NUM * index1 + index2
            <span class="hljs-keyword">if</span> (particleActiveArr.current[_index]) &#123;
                <span class="hljs-keyword">if</span> (ratio < <span class="hljs-number">0.02</span>) &#123;
                    particleActiveArr.current[_index] = 
                        index1 >= currentActiveIndex.current - <span class="hljs-number">1</span> && index1 <= currentActiveIndex.current + <span class="hljs-number">1</span> 
                        ? POINT_ACTIVE_MOVE_LENGTH 
                        : POINT_MOVE_LENGTH
                &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (ratio > <span class="hljs-number">0.98</span>) &#123;
                    particleActiveArr.current[_index] = POINT_MOVE_LENGTH
                &#125;
            &#125;
            <span class="hljs-keyword">const</span> offset = particleActiveArr.current[_index] || POINT_MOVE_LENGTH
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">x</span>: x + l * ratio * offset,
                <span class="hljs-attr">y</span>: y + t * ratio * offset,
                <span class="hljs-attr">opacity</span>: <span class="hljs-number">1</span> - ratio
            &#125;
        &#125;, &#123;
            <span class="hljs-attr">duration</span>: POINT_CREATE_DELAY,
            <span class="hljs-attr">repeat</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">easing</span>: <span class="hljs-string">'easeSinInOut'</span>
        &#125;)
        particleArr.current.push(particleShape)
        particleStartArr.current.push(<span class="hljs-literal">false</span>)
        particleActiveArr.current.push(POINT_MOVE_LENGTH)
    &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">✨其他说明</h2>
<p>这个项目是一个练手项目，基于<code>vite</code>、<code>React</code>、<code>Typescript</code>，因为react平时用的不多，项目中存在什么问题或写的不好的地方欢迎指点。</p>
<p>或者有什么好看的特效也可以提ISSUE或PR交流一下怎么实现。</p>
<p>项目Github: <a href="https://github.com/leon-kfd/g-music-visualizer" target="_blank" rel="nofollow noopener noreferrer"><strong>Click Here</strong></a></p>
<p>项目Demo: <a href="https://leon-kfd.github.io/g-music-visualizer/" target="_blank" rel="nofollow noopener noreferrer"><strong>Click Here</strong></a></p>
<p>笔者往期推荐文章</p>
<ul>
<li><a href="https://juejin.cn/post/6967588280070045733" target="_blank">Vite + Vue3开发一个自定义浏览器起始页网站</a></li>
<li><a href="https://juejin.cn/post/6972727914030858248" target="_blank">如何实现一个轻量的断点续传个人网盘系统</a></li>
</ul></div>  
</div>
            