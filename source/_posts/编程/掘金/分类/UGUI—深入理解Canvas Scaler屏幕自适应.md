
---
title: 'UGUI—深入理解Canvas Scaler屏幕自适应'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7825c87bd705433285dd3d379851327b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 23:30:51 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7825c87bd705433285dd3d379851327b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">前言</h2>
<blockquote>
<p>在学习Canvas Scaler组件之间，让我们先来了解一下什么是像素、图片分辨率、屏幕分辨率、像素比以及宽高比。</p>
</blockquote>
<p><strong>像素</strong>：像素指的是图像最小的单位，是独立的一个色块(像素点)，一张图片就是由这些像素点构成的，单位面积内像素点越多，越密集，那么图像就会越清晰。</p>
<p><strong>图片分辨率</strong>：图像分辨率是指每英寸图像内的像素。图像分辨率是有单位的，叫像素没英寸。分辨率越高，像素的点密度越高，图像越逼真。</p>
<p><strong>屏幕分辨率</strong>：屏幕所能显示像素的多少，分辨率1920x1080的意思就是水平方向含有像素数为1920个，垂直方向像素数为1080个。屏幕尺寸一样的情况下，分辨率越高，显示效果越精细和细腻。</p>
<p><strong>像素比</strong>：是指每个格子(像素)是方的还是扁的。1：1就是正方的，4：3是有点扁的，16：9是很扁。</p>
<p><strong>宽高比(画面比)</strong>：指视频图像的宽度和高度之间的比例。</p>
<p><em><strong>注意：</strong></em></p>
<ul>
<li>实际的屏幕宽高比不一定是分辨率之比，除非像素比是1：1。</li>
<li>实际的屏幕宽高比 = 横向分辨率x横向像素长度：纵向分辨率x纵向像素长度。</li>
</ul>
<p>比如一部电影，分辨率是640 * 360，画面宽高比是16：9(640:360)，那么像素比正好是1：1。</p>
<hr>
<h2 data-id="heading-1">Canvas Scaler</h2>
<blockquote>
<p>Unity官方对于Canvas Scaler的定义是"The Canvas Scaler Component is used for controlling the overall scale and pixel density of UI elements in the Canvas. This scaling effects everything under the Canvas, including font size and image borders"。意思是Canvas Scaler组件用于控制在画布上所有的UI元素的缩放比例和像素密度。并且这个缩放比例会影响所有在Canvas上面的东西，包括字体大小和图片边界。</p>
</blockquote>
<p>为了适用不同分辨率，我们可能需要允许适当的UI整体性的缩放，外加一些尽可能少的局部微调，这样可以达到一个比较理想的效果。Canvas Scaler就说负责该功能的组件。</p>
<p>当Canvas的Render Mode为Screen Space - Overlay或者是Screen Space - Camera时，Canvas Scaler的UI Scale Model有三个选项，分别是:Constant Pixel Size、Scale With Screen Size、Constant Physical Size，如下图所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7825c87bd705433285dd3d379851327b~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当Canvas的Render Mode为World Space时，Canvas Scaler的UI Scale Model只有一个为Wordl默认选项，且不可更改，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/732a912cce39438db7e364b67a72c9dd~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面来详细介绍一下Constant Pixel Size、Scale With Screen Size、Constant Physical Size这三种模式。</p>
<hr>
<h2 data-id="heading-2">UI Scale Mode — Constant Pixel Size</h2>
<p><strong>说明:</strong>
当屏幕分辨率设置为1000 * 1000时，创建一个Canvas，再在Canvas里面添加一张宽高为100 * 100的图片。</p>
<ul>
<li>
<p><strong>参数详解:</strong></p>
<ul>
<li>Scale Factor：画布的缩放比例。默认为1，代表正常大小。</li>
<li>Reference Pixels Per Unit：每单位代表的像素量。</li>
</ul>
</li>
<li>
<p>当Scale Factor设置为1时，Canvas的宽高为1000 * 1000，图片的宽高为100 * 100，如下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d80cfe39e5f4a91a4494b306ad09842~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd4781fceb5c4a6fb7d60bcc5d7520e6~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>当Scale Factor设置为2时，Canvas的宽高为500 * 500，图片的宽高还是为100 * 100，如下图所示：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98b681852f3347cd9078f4705c582985~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e9993507a9b4d089f1a6d7d97cf990d~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p><strong>总结：</strong>
无论屏幕大小如何，UI元素都保持相同的像素大小。使用该模式时，可以在屏幕上按像素指定UI元素的位置和大小。这也是画布在未附加任何画布缩放器时的默认功能。但是借助画布缩放器中的”Scale Factor”设置，可以向画布中的所有UI元素应用常量缩放。</p>
<h2 data-id="heading-3">UI Scale Mode — Scale With Screen Szie</h2>
<p><strong>说明</strong>
当屏幕分辨率设置为1000 * 1000时，创建一个Canvas，再在Canvas里面添加一张宽高为800 * 600的图片，UI布局设计分辨率设置为800 * 600。</p>
<ul>
<li><strong>参数详解：</strong>
<ul>
<li><em><strong>Reference Resolution:</strong></em> UI布局的设计分辨率。</li>
<li><em><strong>Screen Match Mode - Macth Width Height</strong></em>
<ul>
<li>Match是一个滑条，当Match为0时，按狂赌进行Canvas等比缩放；当Match为1时，按高度进行Canvas等比缩放。一般情况下这个值非0即1，不用纠结中间值。</li>
<li>如果屏幕分辨率<strong>小于等于</strong>设计分辨率时，那么不管Match的值是多少，Canvas的宽高都为设计分辨率。此时案例中为800 * 600.</li>
<li>如果屏幕分辨率<strong>大于</strong>设计分辨率，那么当Match为0时，Canvas的宽为设计分辨率的宽，高再根据屏幕分辨率计算所得，这种情况案例中Canvas的宽为800，高为800；当match为1时，Canvas的高为设计分辨率的高，宽再根据屏幕分辨率计算所得，这种情况案例中的Canvas的宽为600，高为600；</li>
</ul>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cab3b6e619f40ba8187536ee2adf889~tplv-k3u1fbpfcp-watermark.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></li>
<li><em><strong>Screen Match Mode - Expend</strong></em>
<ul>
<li>当屏幕分辨率<strong>小于等于</strong>设计分辨率时，那么此时Canvas的宽高为设计分辨率800 * 600。</li>
<li>当屏幕分辨率<strong>大于</strong>设计分辨率时，选择屏幕分辨率与设计分辨率的宽高差值较小的那个作为缩放标准，另外一个再根据屏幕分辨率进行缩放。案例中，高度差值为(1000 - 800)200，宽度差值为(1000 - 600)400,200较小，所有此时案例中Canvas的宽为800，高再根据屏幕分辨率1：1得到800。</li>
<li>此举旨在减少扩大分辨率时由于非等比扩大而对UI整体布局造成影响。适合制作较小标准尺寸，扩充到较大屏幕。</li>
</ul>
</li>
<li><em><strong>Screen Match Mode - Shrink</strong></em>
<ul>
<li>和Expend类似，但是更适合缩小的情形。</li>
<li>选择屏幕分辨率与设计分辨率的宽高差值较大的那个作为缩放标准，另外一个再根据屏幕分辨率进行缩放。案例中，高度差值为(1000 - 800)200，宽度差值为(1000 - 600)400,400较大，600，宽再根据屏幕分辨率1：1得到600。</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><strong>总结：</strong>
屏幕越大，UI元素越大。使用该模式时，可以根据指定分辨率像素来指定位置和大小，如果当前屏幕的分辨率大于参考分辨率，则画布会保持参考分辨率，但是会放大以便适应屏幕。如果当前屏幕的分辨率小于参考分辨率，则画布会相应缩小以适应屏幕。</p>
<hr>
<h2 data-id="heading-4">UI Scale Mode — Constant Physical Size</h2>
<p><strong>说明：</strong>
与 <strong>Constant Pixel Size</strong> 模式本质相同， Constant Pixel Size 通过逻辑像素大小调节来维持缩放，Constant Physical Size 通过物理大小调节来维持缩放。使用这种模式必须指定一个像素转换物理大小的因数，运行时通过具体设备的 DPI 计算最终的 Canvas 像素大小和缩放比例。</p>
<ul>
<li><strong>参数详解：</strong>
<ul>
<li><em><strong>Physical Unit：</strong></em> 用于指定 UI 位置和大小的物理单位</li>
</ul>
属性描述计算中的 targetDPICentimeters厘米2.54Millimeters毫米25.4Inches英寸,约 25.4 毫米1Points点，1/72 英寸，1/12 派卡72Picas派卡，1/6 英寸6
<ul>
<li><em><strong>Fallback Sprite DPI:</strong></em> 如果未获取到屏幕的DPI，将使用此值参与计算缩放。</li>
<li><em><strong>Default Sprite DPI：</strong></em> 与Reference Pixels Per Unit共同计算每单位UI单位像素数。</li>
<li><em><strong>Reference Pixels Per Unit：</strong></em> 与Default Sprite DPI共同计算每UI单位像素数。</li>
</ul>
</li>
<li><strong>源码：</strong></li>
</ul>
<pre><code class="hljs language-c# copyable" lang="c#"><span class="hljs-comment"><span class="hljs-doctag">///</span><span class="hljs-doctag"><summary></span></span>
<span class="hljs-comment"><span class="hljs-doctag">///</span>Handles canvas scaling for a constant physical size.</span>
<span class="hljs-comment"><span class="hljs-doctag">///</span><span class="hljs-doctag"></summary></span></span>
<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">virtual</span> <span class="hljs-keyword">void</span> <span class="hljs-title">HandleConstantPhysicalSize</span>(<span class="hljs-params"></span>)</span>
&#123;
    <span class="hljs-built_in">float</span> dpi = (currentDpi == <span class="hljs-number">0</span> ? m_FallbackScreenDPI : currentDpi);
    <span class="hljs-built_in">float</span> targetDPI = <span class="hljs-number">1</span>;
    <span class="hljs-keyword">switch</span> (m_PhysicalUnit)
    &#123;
        <span class="hljs-keyword">case</span> Unit.Centimeters: targetDPI = <span class="hljs-number">2.54f</span>; <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> Unit.Millimeters: targetDPI = <span class="hljs-number">25.4f</span>; <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> Unit.Inches: targetDPI = <span class="hljs-number">1</span>; <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> Unit.Points: targetDPI = <span class="hljs-number">72</span>; <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> Unit.Picas: targetDPI = <span class="hljs-number">6</span>; <span class="hljs-keyword">break</span>;
    &#125;
    SetScaleFactor(dpi / targetDPI);
    <span class="hljs-comment">//设置Canvas中每个单位有多少像素</span>
    SetReferencePixelsPerUnit(m_ReferencePixelsPerUnit * targetDPI / m_DefaultSpriteDPI);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>总结：</strong>
无论屏幕大小和分辨率如何，UI元素都保持相同的物理大小。使用该模式时，可以在屏幕上按照物理单位指定UI元素的位置和大小。此模式要求设备正确报告其屏幕DPI(分辨率)。对于不报告DPI的设备，可以指定回退DPI</p>
<h2 data-id="heading-5">引用参考</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_32830923%2Farticle%2Fdetails%2F53409802%3FlocationNum%3D1%26fps%3D1" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_32830923/article/details/53409802?locationNum=1&fps=1" ref="nofollow noopener noreferrer"># Unity关于像素,Camera大小,以及分辨率的研究</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fmorning-lee%2Fp%2F7135782.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/morning-lee/p/7135782.html" ref="nofollow noopener noreferrer"># 自适应神器</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_30344995%2Farticle%2Fdetails%2F97063417" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_30344995/article/details/97063417" ref="nofollow noopener noreferrer"># Unity UGUI-Canvas Scaler总结</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_39778582%2Farticle%2Fdetails%2F111118421" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_39778582/article/details/111118421" ref="nofollow noopener noreferrer"># ugui源码_UGUI（二）- Canvas Scaler</a></p></div>  
</div>
            