
---
title: 'canvas绘制折线路径动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddb61948125d4e1283662d63f9f9dd97~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 08 May 2021 18:55:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddb61948125d4e1283662d63f9f9dd97~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近有读者加我微信咨询这个问题：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddb61948125d4e1283662d63f9f9dd97~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中的效果是一个折线路径动画效果，如下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/784e46ae3fe04e1782e8f1f8b87d5f18~tplv-k3u1fbpfcp-zoom-1.image" alt="动画.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>要实现以上路径动画，一般可以使用svg的动画功能。或者使用canvas绘制，结合路径数学计算来实现。</p>
<p>如果用canvas来绘制，其中的难点在于：</p>
<ul>
<li>需要计算子路径，这块计算比较复杂。（当然是可以实现的）</li>
<li>渐变的计算， 从图中可以看出，动画的子路径是有渐变效果的，如果要分段计算渐变也很复杂。</li>
</ul>
<p>本文介绍一种思路，使用clip方法，动态移动clip的区域，来达到近似的效果。具体怎么做。</p>
<h2 data-id="heading-0">绘制灰色路径</h2>
<p>绘制路径的代码比较简单，此处就不详细说明，下面代码就模拟了了一个折线路径的绘制：</p>
<pre><code class="copyable"> ctx.beginPath();    
 ctx.moveTo(100,100);
 ctx.lineTo(200,100);
 ctx.lineTo(230,200);
 ctx.lineTo(250,50);
 ctx.lineTo(270,180);
 ctx.lineTo(300,60);
 ctx.lineTo(330,160);
 ctx.lineTo(350,60);
 ctx.lineTo(380,100);
 ctx.lineTo(480,100);
 ctx.strokeStyle = "gray";
 ctx.lineJoin = "round";
 ctx.stroke(); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/854a9485750d434788ba123a1ebd99b3~tplv-k3u1fbpfcp-zoom-1.image" alt="gray" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">绘制亮色路径</h2>
<p>绘制亮色路径的代码和绘制灰色路径的代码一样，只是样式是一个亮的颜色：</p>
<pre><code class="copyable">ctx.save();
            ctx.beginPath();    
            ctx.moveTo(100,100);
            ctx.lineTo(200,100);
            ctx.lineTo(230,200);
            ctx.lineTo(250,50);
            ctx.lineTo(270,180);
            ctx.lineTo(300,60);
            ctx.lineTo(330,160);
            ctx.lineTo(350,60);
            ctx.lineTo(380,100);
            ctx.lineTo(480,100);
            ctx.strokeStyle = "gray";
            ctx.lineJoin = "round";
            ctx.stroke(); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b103d21cfb646519a345b2b34edd2c5~tplv-k3u1fbpfcp-zoom-1.image" alt="bright" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">clip控制亮色路径的绘制区域</h2>
<p>canvas的clip方法可以控制绘制的区域，通过该方法，可以控制智绘制路径的一部分：</p>
<pre><code class="copyable">        ctx.beginPath();
        ctx.rect(offset,0,100,500); // offset 等于0
        ctx.clip();
           ...
        ctx.stroke(); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>clip之后，亮色路径就只会绘制一部分,如下图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f934091b9be440498a404efce887f1f2~tplv-k3u1fbpfcp-zoom-1.image" alt="clip" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">动画效果</h2>
<p>通过不断变化offset的值，就可以大道亮色路径移动的效果，代码如下：</p>
<pre><code class="copyable"> offset += 2;
 if(offset > 600)&#123;
       offset = 100;
 &#125;
requestAnimationFrame(animate);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6b2247b73554225b7b538f73e36c6d0~tplv-k3u1fbpfcp-zoom-1.image" alt="动画1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">渐变</h2>
<p>我们知道渐变没法沿着任意路径，如果计算折线，分段计算渐变又很麻烦。 其实在本案例中，虽然是折线，但是整体的运动方向总是从左往右的，所以可以用从左往右的渐变来近似模拟既可以：</p>
<pre><code class="copyable">function createGradient(ctx,x0,y0,x1,y1)&#123;
          var grd = ctx.createLinearGradient(x0,y0,x1,y1);
           grd.addColorStop(0,'#129ab3');
           grd.addColorStop(1,"#19b5fe");
           return grd;
&#125;

ctx.strokeStyle = createGradient(ctx,offset,0,offset + 100,0);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终效果如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ad66ae237c74b2e8d8c81444eb7d826~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">全部代码</h2>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>line animate</title>
    <style>
        canvas &#123;
            border: 1px solid #000;
        &#125;
    </style>
</head>
<body>
    <canvas id="canvas" width="600" height="400"></canvas>
    <script>
        var ctx = document.getElementById( 'canvas' ).getContext( '2d' );
        var w = canvas.width,
                h = canvas.height;

        var x = w / 2,y = h / 2;

        function setupCanvas(canvas) &#123;
            let width = canvas.width,
            height = canvas.height,
            dpr = window.devicePixelRatio || 1.0;
            if (dpr != 1.0 ) &#123;
            canvas.style.width = width + "px";
            canvas.style.height = height + "px";
            canvas.height = height * dpr;
            canvas.width = width * dpr;
            ctx.scale(dpr, dpr);
            &#125;
        &#125;
        setupCanvas(canvas);
        var offset = 100;
        function createGradient(ctx,x0,y0,x1,y1)&#123;
           var grd = ctx.createLinearGradient(x0,y0,x1,y1);
           grd.addColorStop(0,'#9a12b3');
           grd.addColorStop(1,"#19b5fe");
           return grd;
        &#125;

        function animate()&#123;
            ctx.fillStyle = "black";
            ctx.fillRect(0,0,canvas.width,canvas.height);
            ctx.lineWidth = 3;
            ctx.save();
            ctx.beginPath();    
            ctx.moveTo(100,100);
            ctx.lineTo(200,100);
            ctx.lineTo(230,200);
            ctx.lineTo(250,50);
            ctx.lineTo(270,180);
            ctx.lineTo(300,60);
            ctx.lineTo(330,160);
            ctx.lineTo(350,60);
            ctx.lineTo(380,100);
            ctx.lineTo(480,100);
            ctx.strokeStyle = "gray";
            ctx.lineJoin = "round";
            ctx.stroke(); 

            ctx.beginPath();
            ctx.rect(offset,0,150,500);
            ctx.clip();
            ctx.beginPath();
            ctx.moveTo(100,100);
            ctx.lineTo(200,100);
            ctx.lineTo(230,200);
            ctx.lineTo(250,50);
            ctx.lineTo(270,180);
            ctx.lineTo(300,60);
            ctx.lineTo(330,160);
            ctx.lineTo(350,60);
            ctx.lineTo(380,100);
            ctx.lineTo(480,100);
            ctx.lineWidth = 4;
            ctx.strokeStyle = createGradient(ctx,offset,0,offset + 150,0);
            ctx.lineCap = "round";
            // ctx.globalCompositeOperation = 'lighter';
            ctx.lineJoin = "round";
            ctx.stroke(); 

            ctx.restore();

            offset += 2;
            if(offset > 600)&#123;
                offset = 100;
            &#125;

            requestAnimationFrame(animate);
        &#125;

        animate();
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">总结</h2>
<p>其实整体思路是用了近似，而不是严格的控制路径长度和渐变效果，这样可以更方便实现以上功能。  其实人眼有时候是分辨不出来一些细节，可视化，有的时候只有能够达到让人“觉得”是那么回事，其实目的也就达到了。</p>
<p>以上方案只能适用于，折线路径的整体方向是一致的。如果整体方向是先水平向右，然后在垂直向下，或者甚至出现往回拐的情况，就不适合了。</p>
<p>关注公众号“ITMan彪叔” 可以及时收到更多有价值的文章。另外如果对可视化感兴趣，可以和我交流，微信541002349.</p></div>  
</div>
            