
---
title: 'canvas绘制图像轮廓效果'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0ec2f32e0b84431ae3f8b499a8ca9bf~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 30 Mar 2021 23:20:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0ec2f32e0b84431ae3f8b499a8ca9bf~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在2d图形可视化开发中，经常要绘制对象的选中效果。 一般来说，表达对象选中可以使用边框，轮廓或者发光的效果。  发光的效果，可以使用canvas的阴影功能，比较容易实现，此处不在赘述。</p>
<h1 data-id="heading-0">绘制边框</h1>
<p>绘制边框是最容易实现的效果，比如下面的图片
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0ec2f32e0b84431ae3f8b499a8ca9bf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>要绘制边框，只需要使用strokeRect的方式即可。效果如下图所示：
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90820249311e4ad1a5ca99442c71a399~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这个代码也很简单，如下所示：</p>
<pre><code class="copyable">     ctx1.strokeStyle = "red";
     ctx1.lineWidth = 2;
     ctx1.drawImage(img, 1, 1,img.width ,img.height)
     ctx1.strokeRect(1,1,img.width,img.height);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">绘制轮廓</h1>
<p>问题是，简单粗暴的加一个边框，并不能满足需求。很多时候，人们需要的是轮廓的效果，也就是图片的有像素和无像素的边缘处。如下图的效果所示：
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b3638a679084dc5a3f1afc27f224b8b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>要实现上述效果，最容易想到的思路就是通过像素的计算来判断边缘，并对边缘进行特定颜色的像素填充。但是像素的计算算法并不容易，简单的算法又很难达到预期的效果，而且由于逐像素操作，效率不高。</p>
<p>考虑到在三维webgl中，计算轮廓的算法思路是这样的：</p>
<ol>
<li>先绘制三维模型自身，并在绘制的时候启动模板测试，把三维图像保存到模板缓冲中。</li>
<li>把模型适当放大，用纯属绘制模型，并在绘制的时候启用模板测试，和之前的模板缓冲区中的像素进行比较，如果对应的坐标处在之前模板缓冲区中有像素，就不绘制纯色。</li>
</ol>
<p>依据上述的原理，就可以绘制处三维对象的轮廓了。下面是一个示例效果，（参考<a href="https://stemkoski.github.io/Three.js/Outline.html" target="_blank" rel="nofollow noopener noreferrer">stemkoski.github.io/Three.js/Ou…</a>）
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/356894050ab24c99a1f4e1844c3521d6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在2d canvas里面有类似的原理可以实现轮廓效果，就是使用globalCompositeOperation了。 大体思路是这样的：</p>
<ol>
<li>首先绘制放大一些的图片。</li>
<li>然后开启globalCompositeOperation = 'source-in', 并用纯色填充整个canvas区域，由于source-in的效果，纯色会填充放大图片有像素的区域。</li>
<li>使用默认的globalCompositeOperation（source-over），用原始尺寸绘制图片。</li>
</ol>
<h2 data-id="heading-2">绘制放大一些的图片</h2>
<p>通过drawImage的参数可以控制绘制图片的大小，如下所示，drawImage有几个形式：</p>
<pre><code class="copyable">1  void ctx.drawImage(image, dx, dy);
2  void ctx.drawImage(image, dx, dy, dWidth, dHeight);
3  void ctx.drawImage(image, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中dx，dy 代表绘制的起始位置，一般绘制的时候使用第一个方法，代表绘制的大小就是原本图片的大小。而使用第二个方法，我们可以指定绘制的尺寸，我们可以使用第二个方法绘制放大的图片，代码如所示：</p>
<pre><code class="copyable">ctx.drawImage(img, p - s, p  - s, w + 2 * s, h+ 2 * s);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中p代表图片本身的绘制位置，s代表向左，向上的偏移量，同时图片的宽和高都增加 2 * s</p>
<h2 data-id="heading-3">用纯色填充放大图片的区域</h2>
<p>在上一步绘制的基础上，开启globalCompositeOperation = 'source-in', 并用纯色填充整个canvas区域。 代码如下所示：</p>
<pre><code class="copyable"> // fill with color
        ctx.globalCompositeOperation = "source-in";
        ctx.fillStyle = "#FF0000";
        ctx.fillRect(0, 0, cw, ch);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终的效果如下图所示：
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/773404e7f144411d9f388afe28da9e2d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>为什么会出现这种效果是因为使用了globalCompositeOperation = 'source-in',具体原理可以参考本人的其他文章。</p>
<h2 data-id="heading-4">绘制原始图片</h2>
<p>最后一步就是绘制原始图片，代码如下所示：</p>
<pre><code class="copyable">  ctx.globalCompositeOperation = "source-over"；
  ctx.drawImage(img, p, p, w, h);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先恢复globalCompositeOperation为默认值 "source-over"，然后按照原本的大小绘制图片。</p>
<p>经过以上步骤，最终的效果如下图所示：
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/828bf29141304d669f0dc84866232366~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以看出最终获得了我们要的效果。</p>
<h2 data-id="heading-5">只显示轮廓</h2>
<p>如果我们只想得到图片的轮廓，则可以在最后绘制的时候，globalCompositeOperation 设置为“destination-out”，代码如下：</p>
<pre><code class="copyable">        ctx.globalCompositeOperation = "destination-out";
        ctx.drawImage(img, p, p, w, h);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下：
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41923b73d1094cd9a646a8e3f72d8cd0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">轮廓粗细不一致的问题</h2>
<p>上面的算法实现，是在图片的有像素值区域中心和图片本身的几何中心基本一直，如果图片的有像素值的中心和图片本身的几何中心相差比较大，则会出现轮廓粗细不一致的情况，比如下面这张图：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8554d81ed23e4e15925644e4a5713c69~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>上半部分是透明的，下半部分是非透明的，像素的中心在3/4出，而几何中心在1/2处。使用上面的算法，该图片的轮廓如下：
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/286cd10773d949c595632f01d11e211c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以发现上边缘的轮廓宽度变成了0。</p>
<p>在比如下图，
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/074b7e35bd454c2fa71b116dd6a62858~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>绘制后上边缘的轮廓比其他边缘的细。
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab17dbf9667545de8b25ddb206f90fd9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>怎么处理这种情况呢？可以在绘制放大图片的时候，不直接使用缩放，而是在上下左右，上左，上右，下左，下右几个方向进行偏移绘制，多次绘制，代码如下：</p>
<pre><code class="copyable">  var dArr = [-1, -1, 0, -1, 1, -1, -1, 0, 1, 0, -1, 1, 0, 1, 1, 1], // offset array
 // draw images at offsets from the array scaled by s
 for (var i = 0; i < dArr.length; i += 2) &#123;
     ctx.drawImage(img, p + dArr[i] * s, p + dArr[i + 1] * s, w, h);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看上面图片的轮廓效果，如下所示：
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53e95443c89b4e8c95f7068ed3a90b64~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">半透明的情况</h2>
<p>我在其他文章中说过，globalCompositeOperation为"source-in"的时候，source图形的透明度，会影响到目标绘制图形的透明度。所以会导致轮廓的像素值会乘以透明度。比如，我们在绘制放大图的时候，设置globalAlpha = 0.5进行模拟。
最后的绘制效果如下：
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2429f3b67b549c4a83bf5788bb1a755~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以看到轮廓的颜色变浅了，解决办法就是多绘制几次放大图。比如：</p>
<pre><code class="copyable">ctx.globalAlpha = 0.5;
ctx.drawImage(img, p - s, p  - s, w + 2 * s, h+ 2 * s);
ctx.drawImage(img, p - s, p  - s, w + 2 * s, h+ 2 * s);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而上面通过偏移的方式绘制的时候，本身都绘制了好多遍，所以不存在这个问题。如下：</p>
<pre><code class="copyable">  ctx.globalAlpha = 0.5;
  for (var i = 0; i < dArr.length; i += 2) &#123;
     ctx.drawImage(img, p + dArr[i] * s, p + dArr[i + 1] * s, w, h);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下图所示：
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfe45a37a17f4ca6916d361ae767bfc9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当然，在透明度很低的情况下，使用绘制很多遍的方式，不是很好的解决方案。</p>
<p>#　使用算法（marching-squares-algorithm）
上面的方法对于有些图片效果就很不好，比如这张图片：
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffd60806344c4eed979be984f02d50d0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>由于其有很多中空的效果，所以其最终效果如下图所示：
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01b225ee1e8045f88ac87d24426d88cd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>但是想要的只是外部的轮廓，而不需要中空部分也绘制上轮廓效果。此时需要使用其他的算法。 直接使用marching squares algorithm 可以获取图片的边缘。这一块的算法具体实现本文不再讲解，后续有机会单独一篇文章进行讲解。 此处直接使用开源的实现。比如可以使用  <a href="https://github.com/sakri/MarchingSquaresJS" target="_blank" rel="nofollow noopener noreferrer">github.com/sakri/March…</a>，代码如下：</p>
<pre><code class="copyable"> function drawOuttline2()&#123;
        var canvas = document.createElement('canvas');
        var ctx = canvas.getContext('2d');
        var w = img.width;
        var h = img.height;
        canvas.width = w;
        canvas.height = h;
        ctx.drawImage(img, 0, 0, w, h);
        var pathPoints = MarchingSquares.getBlobOutlinePoints(canvas);
        var points = [];
       
        for(var i = 0;i < pathPoints.length;i += 2)&#123;
          points.push(&#123;
            x:pathPoints[i],
            y:pathPoints[i + 1],
          &#125;)
        &#125;


        // ctx.clearRect(0, 0, w, h);
        ctx.beginPath();
        ctx.lineWidth = 2;
        ctx.strokeStyle = '#00CCFF';
        ctx.moveTo(points[0].x, points[0].y);
        for (var i = 1; i < points.length; i += 1) &#123;
          var point = points[i];
          ctx.lineTo(point.x,point.y);
        &#125;
        ctx.closePath();
        ctx.stroke();
        
        ctx1.drawImage(canvas,0,0);
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先使用调用MarchingSquaresJS的方法获取img图像的轮廓点的集合，然后把所有的点连接起来。形成轮廓图，最终效果如下：
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87977f32342343908f5edec3310b7d16~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>不过可以看出，MarchingSquares 算法获得的轮廓效果锯齿相对较多的。有光这块算法的优化，本文不讲解。</p>
<h1 data-id="heading-8">总结</h1>
<p>对于没有中空效果的图片，我们一般不采用MarchingSquares算法，而采用前面的一种方式来实现，效率高，而且效果相对更好。 而对于有中空，就会使用MarchingSquares算法，效果相对差，效率也相对低一些，实际应用中，可以通过缓存来降低性能的损耗。</p>
<p>本文的起源来资源一个2.5D项目，上一张项目图吧：
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68630de38d9c4c7f9a24677a86f772a7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">参考文档</h1>
<p><a href="https://www.emanueleferonato.com/2013/03/01/using-marching-squares-algorithm-to-trace-the-contour-of-an-image/" target="_blank" rel="nofollow noopener noreferrer">www.emanueleferonato.com/2013/03/01/…</a>
<a href="https://github.com/sakri/MarchingSquaresJS" target="_blank" rel="nofollow noopener noreferrer">github.com/sakri/March…</a>
<a href="https://github.com/OSUblake/msqr" target="_blank" rel="nofollow noopener noreferrer">github.com/OSUblake/ms…</a>
<a href="http://users.polytech.unice.fr/~lingrand/MarchingCubes/algo.html#squar" target="_blank" rel="nofollow noopener noreferrer">users.polytech.unice.fr/~lingrand/M…</a></p>
<p>如果对可视化感兴趣,  关注公号“ITMan彪叔” 可以及时收到更多有价值的文章。也可以加微信541002349进行交流。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            