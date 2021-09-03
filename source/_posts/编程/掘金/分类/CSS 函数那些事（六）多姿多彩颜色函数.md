
---
title: 'CSS 函数那些事（六）多姿多彩颜色函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1923f4ec70cd47daa6954ffc8a68f5e2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 01:07:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1923f4ec70cd47daa6954ffc8a68f5e2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1923f4ec70cd47daa6954ffc8a68f5e2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">rgb(),rgba()</h2>
<h4 data-id="heading-1">rgb(red,green,blue)</h4>
<p>rgb(red,green,blue),分别代表着red,green,blue,是色彩三原色，原色以不同比例混合时，会产生其他颜色。为什么会是这三种颜色？这里引用下维基百科的解释：</p>
<blockquote>
<p>人的眼睛内有几种辨别颜色的锥状细胞，分别对黄绿色、绿色和蓝紫色（564、534和420纳米波长）的光最敏感。人类以及其他具有这三种感光受体的生物称为“三色感光体生物”。虽然眼球中的椎状细胞并非对红、绿、蓝三色的感受度最强，但是由肉眼的椎状细胞所能感受的光的带宽很大，红、绿、蓝也能够独立刺激这三种颜色的受光体，因此这三色被视为原色。"原色"的指定并没有唯一的选法，因为就理论上而言，凡是彼此之间无法替代的颜色都可以被选为“原色”，只是目前普遍认定“光的三原色”为红绿蓝。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83b340ed943d424d906e02546b44b7b7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>rgb函数接收三个参数：</p>
<p><strong>R：</strong> 红色值。正整数[0-255] | 百分数[0%-100%]</p>
<p><strong>G：</strong> 绿色值。正整数[0-255] | 百分数[0%-100%]</p>
<p><strong>B：</strong> 蓝色值。正整数[0-255] | 百分数[0%-100%]</p>
<h4 data-id="heading-2">rgba(red,green,blue,alpha)</h4>
<p>rgba在rgb的基础上添加了不透明度(alpha):</p>
<p><strong>A：</strong> 不透明度。取值[0-1]，0代表完全透明，也就是完全看不见，1代表完全不透明，也就是颜色本身</p>
<h4 data-id="heading-3">为什么颜色数值最大为255？</h4>
<p>rgb在计算机中存储为3 byte,每个byte是8个bits，所以rgb对应的最大2进制为11111111,换算成十进制为256，这就意味着有256个不同值，从0开始算，所以最大值为255.颜色的种数那就是256^3 = 16,777,216.</p>
<h2 data-id="heading-4">hsl(),hsla()</h2>
<h4 data-id="heading-5">hsl(hue,saturation,lightness)</h4>
<p>hsl,使用<strong>色调(hue)</strong>,<strong>饱和度(saturation)</strong>,<strong>亮度(lightness)</strong> 表示各种颜色。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0718f53a49e4d05a763731612e20fe7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>色调(hue)</strong>,取值[0,360],代表的是人眼所能感知的颜色范围，这些颜色分布在一个平面的色调环上，取值范围是0°到360°的圆心角，每个角度可以代表一种颜色。色调的意义在于，我们可以在不改变光感的情况下，通过旋转色相环来改变颜色。</p>
<p><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmm1iAtnCpBzZfmYm-rPomRU6cEyGtFAv8Jg&usqp=CAU" alt="色调环" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>饱和度(saturation)</strong>，取值[0%,100%],用0%至100%的值描述了相同色调、亮度下色彩纯度的变化。数值越大，颜色中的灰色越少，颜色越鲜艳，呈现一种从灰度到纯色的变化。</p>
<p><strong>亮度(lightness)</strong>,取值[0%,100%],亮度的作用是控制色彩的明暗变化。它同样使用了0%至100%的取值范围。数值越小，色彩越暗，越接近于黑色；数值越大，色彩越亮，越接近于白色。</p>
<p>hsl更符合人类对颜色表达的习惯，也就是"<strong>什么颜色？颜色多深？颜色多亮？</strong>"。</p>
<h4 data-id="heading-6">hsla()</h4>
<p>与rgba一样，hsla在hsl基础上添加了不透明度(alpha),取值[0-1];</p>
<h4 data-id="heading-7">hsl与rgb</h4>
<p>RGB的几何模型是一个立方体，HSL 则是一个圆柱体，它们之间存在着非线性转换的关系。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hslToRgb</span>(<span class="hljs-params">hue, sat, light</span>) </span>&#123;
  <span class="hljs-keyword">if</span>( light <= <span class="hljs-number">.5</span> ) &#123;
    <span class="hljs-keyword">var</span> t2 = light * (sat + <span class="hljs-number">1</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">var</span> t2 = light + sat - (light * sat);
  &#125;
  <span class="hljs-keyword">var</span> t1 = light * <span class="hljs-number">2</span> - t2;
  <span class="hljs-keyword">var</span> r = hueToRgb(t1, t2, hue + <span class="hljs-number">2</span>);
  <span class="hljs-keyword">var</span> g = hueToRgb(t1, t2, hue);
  <span class="hljs-keyword">var</span> b = hueToRgb(t1, t2, hue - <span class="hljs-number">2</span>);
  <span class="hljs-keyword">return</span> [r,g,b];
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hueToRgb</span>(<span class="hljs-params">t1, t2, hue</span>) </span>&#123;
  <span class="hljs-keyword">if</span>(hue < <span class="hljs-number">0</span>) hue += <span class="hljs-number">6</span>;
  <span class="hljs-keyword">if</span>(hue >= <span class="hljs-number">6</span>) hue -= <span class="hljs-number">6</span>;

  <span class="hljs-keyword">if</span>(hue < <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> (t2 - t1) * hue + t1;
  <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(hue < <span class="hljs-number">3</span>) <span class="hljs-keyword">return</span> t2;
  <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(hue < <span class="hljs-number">4</span>) <span class="hljs-keyword">return</span> (t2 - t1) * (<span class="hljs-number">4</span> - hue) + t1;
  <span class="hljs-keyword">else</span> <span class="hljs-keyword">return</span> t1;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">hwb()</h2>
<p><strong>hwb(hue,whiteness,blackness)</strong>,hwb类似于hsl，也是一种将RGB色彩模型中的点在圆柱坐标系中的表示法。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/200cdedb83114781b4ac0f725b32b03d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>H(hue)</strong>：表示色调,与hsl中的色调一样，取值范围[0-360];</p>
<p><strong>W(whiteness)</strong> :  表示白色浓度，取值[0%,100%];</p>
<p><strong>B(blackness)</strong>:  表示黑色浓度，取值[0%,100%];</p>
<p>由于这个属性暂时还是实验属性，这里只了解一下，不做过多的说明，有兴趣的同学可以去<a href="https://link.juejin.cn/?target=https%3A%2F%2Fweb.archive.org%2Fweb%2F20150709065126%2Fhttp%3A%2F%2Fdev.w3.org%2Fcsswg%2Fcss-color%2F%23funcdef-hwb" target="_blank" rel="nofollow noopener noreferrer" title="https://web.archive.org/web/20150709065126/http://dev.w3.org/csswg/css-color/#funcdef-hwb" ref="nofollow noopener noreferrer">这里</a>了解一下</p>
<h2 data-id="heading-9">lab()</h2>
<p>lab函数用来表示<strong>CIELAB色彩空间</strong>,表示为L<em>a</em>b*, 是CIE(国际照明委员会)在1976年定义的色彩空间.
<img src="https://sensing.konicaminolta.asia/wp-content/uploads/2018/09/3D-LAB.jpg" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>L</strong> :  表示亮度,取值[0%,100%],取值0%是黑色，取值100%是白色；
<strong>A</strong> :  表示在a轴上的坐标值
<strong>B</strong>：表示在b轴上的坐标值
a,b的值理论上是无限的，但是实际上是不会超过±160。</p>
<p>这个函数处于也是实验阶段。</p>
<h2 data-id="heading-10">lch()</h2>
<p>lch(lightness ,chroma ,hue),采用了和CIE L<em>a</em>b*相同的颜色空间, 不过表达的方式有不同。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4af543af1c64066b526475f1b907053~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>L：</strong> 代表亮度,取值[0%，100%];</p>
<p><strong>C:</strong> 色度，即色彩饱和程度，最小值为0，理论上没有最大值,</p>
<p><strong>h:</strong> 色调，即色彩的总体倾向，取值[0,360]。</p>
<p>这个函数处于实验阶段。</p>
<h2 data-id="heading-11">device-cmyk()</h2>
<p>device-cmyk()
device-cmyk函数用来表示<strong>印刷四分色模式（CMYK）</strong>,相对于RGB的加色混色模型，CMYK是减色混色模型，颜色混在一起，亮度会降低。之所以加入黑色是因为打印时由品红、黄、青构成的黑色不够纯粹。这个函数包含4个参数：</p>
<p><strong>C:</strong> Cyan,青色，取值[0-1],或者[0%,100%];</p>
<p><strong>M:</strong>  Magenta ,品红色，取值[0-1],或者[0%,100%];</p>
<p><strong>Y:</strong> Yellow ,黄色，取值[0-1],或者[0%,100%];</p>
<p><strong>K:</strong> Black,黑色，取值[0-1],或者[0%,100%];</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/205edcf89a5b41eea9fd83bd4037669b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个函数处于实验阶段。</p>
<h2 data-id="heading-12">总结</h2>
<p>目前浏览器已经能支持hsl,以及hsla这两个新的函数，其他的用来表示色彩的函数也已经在 CSS Color Module Level 4 的草案中了，写这篇文章提前先了解下这些色彩模型。</p>
<h2 data-id="heading-13">最后</h2>
<p>我最近在总结 css 函数相关的东西，这篇是系列文章的第六篇，目前已产出</p>
<ul>
<li>
<p><a href="https://juejin.cn/post/6898141267771801613" title="https://juejin.cn/post/6898141267771801613" target="_blank">CSS 函数那些事（一）比较函数</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6898945436988473358" title="https://juejin.cn/post/6898945436988473358" target="_blank">CSS 函数那些事（二）你不知道的 attr()</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6901848317823549454" title="https://juejin.cn/post/6901848317823549454" target="_blank">CSS 函数那些事（三）背景图片函数</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6907061355291869197" title="https://juejin.cn/post/6907061355291869197" target="_blank">CSS 函数那些事（四）网格函数</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6909709349183029256" title="https://juejin.cn/post/6909709349183029256" target="_blank">CSS 函数那些事（五）计数函数</a></p>
</li>
</ul>
<p>项目中会包含文章中的测试代码，都做好了相应的分类，欢迎各位持续关注，有帮助话可以点个赞哦！<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKerinlin%2FCSS-Function" title="https://github.com/Kerinlin/CSS-Function" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">项目地址戳这里</a></p>
<h2 data-id="heading-14">参考资料</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=http%3A%2F%2Fdev.w3.org%2Fcsswg%2Fcss-color%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://dev.w3.org/csswg/css-color/" ref="nofollow noopener noreferrer">CSS color</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F22077462" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/question/22077462" ref="nofollow noopener noreferrer">HLS原理</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdrafts.csswg.org%2Fcss-color" target="_blank" rel="nofollow noopener noreferrer" title="https://drafts.csswg.org/css-color" ref="nofollow noopener noreferrer">CSS Color Module Level 4 (CSS Color 4)</a></li>
</ol></div>  
</div>
            