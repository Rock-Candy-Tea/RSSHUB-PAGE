
---
title: 'Web Audio - 绘制音频图谱'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/838522ad9bd14af0ac9662cc2b39a062~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 22:08:19 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/838522ad9bd14af0ac9662cc2b39a062~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>前端处理音频，目前一些开源的插件和js库已经提供了非常好的支持。其中小编了解的比较多的是sound.js和wavasuffer.js这俩个库。其中sound.js是一个大而全的音频处理库，功能丰富，兼容性也处理的很好。wavesuffer则偏重于音频波形图绘制处理，相对比较轻量。小编此篇不在于比较二者的差异，而是和大家一起学习下如何自己实现一个简易的音频图谱绘制。</p>
<h2 data-id="heading-1">实现思路</h2>
<p>先介绍下小编的整体思路吧。所谓的音频图谱，其实只是将声音的响度具象化为一个波形图，响度高对应的波形高，响度低波形也就低。所以第一步，我们可以通过xhr拿到一个音频文件的数据。那么，第二步便是如何处理这组数据，让数据能够比较真实的反应音频的响度。这时候就需要前端的Web Audio Api来发挥作用了，具体如何处理，我们后面详细说明。完成数据处理之后，最后一步就是需要根据数据绘制出波形图，这里我们使用canvas来做波形图的绘制。</p>
<h3 data-id="heading-2">获取音频文件</h3>
<p>首先，我们利用fetch，来获取一个线上音频。这里，我们借用一下wavesuffer官网demo中用的线上音频来做示范。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-comment">// 音频url</span>
<span class="hljs-keyword">let</span> audioUrl = <span class="hljs-string">'https://wavesurfer-js.org/example/media/demo.wav'</span>;
<span class="hljs-comment">// 创建音频上下文</span>
<span class="hljs-keyword">let</span> audioCtx = <span class="hljs-keyword">new</span> (<span class="hljs-built_in">window</span>.AudioContext || <span class="hljs-built_in">window</span>.webkitAudioContext)();
<span class="hljs-comment">// 创建音频源</span>
<span class="hljs-keyword">let</span> source = audioCtx.createBufferSource();

<span class="hljs-comment">/* 
 * 通过fetch下载音频，responseType设置为'arrayBuffer'，我们以arrayBuffer格式接收返回的数据
*/</span>

fetch(audioUrl, &#123;
  <span class="hljs-attr">method</span>: <span class="hljs-string">'GET'</span>,
  <span class="hljs-attr">responseType</span>: <span class="hljs-string">'arraybuffer'</span>,
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  <span class="hljs-keyword">return</span> res.arrayBuffer();
&#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-comment">// 处理音频数据</span>
  initAudio(data);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">利用Web Audio Api 处理音频数据</h3>
<p>拿到音频数据之后，我们需要利用Web Audio Api，来处理音频数据，实现音频的播放，暂停等操作以及我们后续的波形图绘制。这里简单介绍下，Web Audio Api是一组非常强大的Api，它提供了在Web中控制音频、处理音频的一整套有效通用的系统。它能够允许开发着，控制音频，自选音频源、对音频添加特效，使音频可视化，添加空间效果，添加混响等等。而我们今天要实现的功能，仅仅只用到了其中几个Api，整体流程如下：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/838522ad9bd14af0ac9662cc2b39a062~tplv-k3u1fbpfcp-watermark.image" alt="img1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-comment">// audio 初始化</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initAudio</span> (<span class="hljs-params">data</span>) </span>&#123;
  <span class="hljs-comment">// 音频数据解码</span>
  <span class="hljs-comment">// decodeAudioData方法接收一个arrayBuffer数据作为参数，这也是为什么前面fetch音频时设置以arrayBuffer格式接收数据</span>
  audioCtx.decodeAudioData(data).then(<span class="hljs-function"><span class="hljs-params">buffer</span> =></span> &#123;
    <span class="hljs-comment">// decodeAudioData解码完成后，返回一个AudioBuffer对象</span>
    <span class="hljs-comment">// 绘制音频波形图</span>
    drawWave(buffer);
    
    <span class="hljs-comment">// 连接音频源</span>
    source.buffer = buffer;
    source.connect(audioCtx.destination);
    <span class="hljs-comment">// 音频数据处理完毕</span>
    alert(<span class="hljs-string">'音频数据处理完毕!'</span>);
  &#125;);
&#125;

<span class="hljs-comment">// web audio 规范不允许音频自动播放，需要用户触发页面事件来触发播放，这里我们增加一个播放按钮，数据处理完毕后点击播放</span>
<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#btn'</span>).onclick = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 播放音频</span>
  source.start(<span class="hljs-number">0</span>);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">通过解码后的音频数据，绘制波形图</h3>
<p>音频数据通过AudioContext解码后，返回一个AudioBuffer对象，这个对象，保存有音频的采样率、声道、pcm数据等信息。通过getChannelData方法可以获取到音频某个声道的pcm数据。返回的是一个Float32Array对象，数值范围在-1到1之间。音频数据比较庞大，每一秒钟可能包含成千上万的数据，因此我们在做图形绘制时，需要对数据进一步采样。比如，这里我们采用每1000条数据中，取一个最大值(正数)一个最小值(负数)来绘制图形；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 绘制波形图</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">drawWave</span> (<span class="hljs-params">buffer</span>) </span>&#123;
  <span class="hljs-comment">// buffer.numberOfChannels返回音频的通道数量，1即为单声道，2代表双声道。这里我们只取一条通道的数据</span>
  <span class="hljs-keyword">let</span> data = [];
  <span class="hljs-keyword">let</span> originData = buffer.getChannelData(<span class="hljs-number">0</span>);
  <span class="hljs-comment">// 存储所有的正数据</span>
  <span class="hljs-keyword">let</span> positives = [];
  <span class="hljs-comment">// 存储所有的负数据</span>
  <span class="hljs-keyword">let</span> negatives = [];
  <span class="hljs-comment">// 先每隔100条数据取1条</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < originData.length; i += <span class="hljs-number">100</span>) &#123;
    data.push(originData[i]);
  &#125;
  <span class="hljs-comment">// 再从data中每10条取一个最大值一个最小值</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>, len = <span class="hljs-built_in">parseInt</span>(data.length / <span class="hljs-number">10</span>); j < len; j++) &#123;
    <span class="hljs-keyword">let</span> temp = data.slice(j * <span class="hljs-number">10</span>, (j + <span class="hljs-number">1</span>) * <span class="hljs-number">10</span>);
    positives.push(<span class="hljs-built_in">Math</span>.max.apply(<span class="hljs-literal">null</span>, temp));
    negatives.push(<span class="hljs-built_in">Math</span>.min.apply(<span class="hljs-literal">null</span>, temp));
  &#125;

  <span class="hljs-comment">// 创建canvas上下文</span>
  <span class="hljs-keyword">let</span> canvas = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#canvas'</span>);
  <span class="hljs-keyword">if</span> (canvas.getContext) &#123;
    <span class="hljs-keyword">let</span> ctx = canvas.getContext(<span class="hljs-string">'2d'</span>);
    canvas.width = positives.length;
    <span class="hljs-keyword">let</span> x = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> y = <span class="hljs-number">100</span>;
    <span class="hljs-keyword">let</span> offset = <span class="hljs-number">0</span>;
    ctx.fillStyle = <span class="hljs-string">'#fa541c'</span>;
    ctx.beginPath();
    ctx.moveTo(x, y);
    <span class="hljs-comment">// canvas高度200，横坐标在canvas中点100px的位置，横坐标上方绘制正数据，下方绘制负数据</span>
    <span class="hljs-comment">// 先从左往右绘制正数据</span>
    <span class="hljs-comment">// x + 0.5是为了解决canvas 1像素线条模糊的问题</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> k = <span class="hljs-number">0</span>; k < positives.length; k++) &#123;
      ctx.lineTo(x + k + <span class="hljs-number">0.5</span>, y - (<span class="hljs-number">100</span> * positives[k]));
    &#125;
    
    <span class="hljs-comment">// 再从右往左绘制负数据</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> l = negatives.length - <span class="hljs-number">1</span>; l >= <span class="hljs-number">0</span>; l--) &#123;
      ctx.lineTo(x + l + <span class="hljs-number">0.5</span>, y + (<span class="hljs-number">100</span> * <span class="hljs-built_in">Math</span>.abs(negatives[l])));
    &#125;
    <span class="hljs-comment">// 填充图形</span>
    ctx.fill();
  &#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，简单的音频波形图绘制就完成了。小编这里仅做抛砖引玉，简单介绍下Web Audio的一个应用场景。更多更复杂的应用，大家可以深入了解学习Web Audio相关api。最后，贴一下效果图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be418a0f797e4b888e44b52b8717dc0f~tplv-k3u1fbpfcp-watermark.image" alt="img2.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            