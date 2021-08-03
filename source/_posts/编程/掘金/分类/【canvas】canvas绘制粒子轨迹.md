
---
title: '【canvas】canvas绘制粒子轨迹'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ae0ed0263294d1bba31f1f1fce75a31~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 08:39:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ae0ed0263294d1bba31f1f1fce75a31~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>不经意搜canvas特效，看到有个还不错，改了改实现了一下，觉得挺有意思，加工分享一下。</p>
<h2 data-id="heading-1">效果</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ae0ed0263294d1bba31f1f1fce75a31~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b24623deb3245cc9b0877f68633239c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外一个效果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f181008497e8451da44cf3add0b55028~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">原理和代码</h2>
<ul>
<li>
<ol>
<li>先创建一个副画布，写好自己想写的文字，然后通过像素读点的方法获取目标每个像素点的位置</li>
</ol>
</li>
</ul>
<hr>
<pre><code class="copyable">const viceCanvas = document.createElement('canvas')
viceCanvas.width = WIDTH;
viceCanvas.height = HEIGHT;
let viceCxt = viceCanvas.getContext('2d')
// 绘制最终结果文字
const font = '九三'
viceCxt.font = '200px Arial';
const measure = viceCxt.measureText(font)
viceCxt.fillText(font, (WIDTH - measure.width) / 2, HEIGHT / 2);
return getFontInfo(viceCxt);
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>其中getFontInfo就是通过遍历像素读点的方法</p>
<hr>
<pre><code class="copyable">    // 辅助，通过取像素获取像素点信息
    function getFontInfo(ctx) &#123;
        let imageData = ctx.getImageData(0, 0, WIDTH, HEIGHT).data;
        const particles = [];
        for (let x = 0; x < WIDTH; x += 4) &#123;
            for (let y = 0; y < HEIGHT; y += 4) &#123;
                const fontIndex = (x + y * WIDTH) * 4 + 3;
                if (imageData[fontIndex] > 0) &#123;
                    particles.push(new Particle(&#123;
                        x,
                        y,
                    &#125;))
                &#125;
            &#125;
        &#125;
        return particles;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>这里面Particle是自己定义的一个类，表示的每个点的轨迹。
他的constructor中有初始点（随机）和目标位置（前面读副本获取到且传入的）和速度。</p>
<hr>
<pre><code class="copyable">constructor(center) &#123;
    this.x = center.x; // 记录点位最终应该停留在的x轴位置
    this.y = center.y; // 记录点位最终应该停留在的y轴位置
    this.item = 0;     // 贝塞尔曲线系数
    this.vx = 20;      // 点位在x轴的移动速度
    this.vy = 16;       // 点位在y轴的移动速度
    this.initX = Math.random() * WIDTH; // 点位随机在画布中的x坐标
    this.initY = Math.random() * HEIGHT; // 点位随机在画布中的y坐标                
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<ul>
<li>2 创建主画布，然后就是render的过程了</li>
</ul>
<hr>
<pre><code class="copyable">    let WIDTH, HEIGHT, cxt, raf, points;
    // init
    window.onload = () => &#123;
        WIDTH = document.body.clientWidth;
        HEIGHT = document.body.clientHeight;
        const canvas = document.getElementById('canvas');
        canvas.width = WIDTH;
        canvas.height = HEIGHT;
        ctx = canvas.getContext('2d');
        points = createViceCanvas();
        render()
    &#125;
    function render() &#123;
        ctx.clearRect(0, 0, WIDTH, HEIGHT)
        points.forEach((value) => &#123; //
            value.draw(); // 每一条点单独绘制一个随机到目标位置的曲线
        &#125;)
        raf = window.requestAnimationFrame(render)
        if(points[0].item>=1)&#123;
            window.cancelAnimationFrame(raf)
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>特别注意requestAnimationFrame和cancelAnimationFrame。
points就是从副本中读出的目标点的集合。
每一次render都要绘制一小步。调用Particle类draw方法。</p>
<ul>
<li>
<ol start="3">
<li>render时的绘制</li>
</ol>
</li>
</ul>
<p>draw的两个版本，版本一
贝塞尔曲线，原文作者就用的是这个。</p>
<hr>
<pre><code class="copyable">        draw() &#123; // 绘制点位
            ctx.beginPath();
            const &#123; x, y &#125; = threeBezier( // 贝塞尔曲线，获取每一个tick点位所在位置
                this.item,
                [this.initX, this.initY],
                [this.x, this.y],
                [this.x, this.y],
                [this.x, this.y]
            )
            ctx.arc(x, y, 2, 0, 2 * Math.PI, true);
            ctx.fillStyle = randomHexColor()
            ctx.fill();
            ctx.closePath();
            this.speed(); // 点位下次tick绘制时的坐标
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>贝塞尔曲线么，就是曲线美观一点，每一次根据时刻t，去算下一个点的位置，然后去做一个arc<br>
贝塞尔曲线也封装了一个方法。
其实就是一个数学公式。</p>
<hr>
<pre><code class="copyable">    const threeBezier = (t, p1, p2, cp1, cp2) => &#123;
        const [startX, startY] = p1;
        const [endX, endY] = p2;
        const [cpX1, cpY1] = cp1;
        const [cpX2, cpY2] = cp2
        let x = startX * Math.pow(1 - t, 3) +
            3 * cpX1 * t * Math.pow(1 - t, 2) +
            3 * cpX2 * Math.pow(t, 2) * (1 - t) +
            endX * Math.pow(t, 3);
        let y = startY * Math.pow(1 - t, 3) +
            3 * cpY1 * Math.pow(1 - t, 2) * t +
            3 * cpY2 * (1 - t) * Math.pow(t, 2) +
            endY * Math.pow(t, 3)
        return &#123;
            x,
            y,
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>然后就是版本二，不理解贝塞尔公式，我画直线行不行。
也行。</p>
<hr>
<pre><code class="copyable">    const &#123; x, y &#125; = lineAAA( // 贝塞尔曲线，获取每一个tick点位所在位置
        this.item,
        [this.initX, this.initY],
        [this.x, this.y],
        [this.x, this.y],
        [this.x, this.y]
    )
    ctx.moveTo(x, y)
    ctx.lineTo(this.x, this.y)
    ctx.strokeStyle = randomHexColor()
    ctx.stroke()
            

    const lineAAA = (t, p1, p2, cp1, cp2) => &#123;
        const [startX, startY] = p1;
        const [endX, endY] = p2;
        let x = startX + (endX - startX) * t
        let y = startY + (endY - startY) * t
        return &#123;
            x,
            y,
        &#125;
    &#125;
    
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<ul>
<li>
<ol start="4">
<li>到上面，所有的都讲完了，对于单个粒子，他有一个随机的初始点，和一个明确的目标点，然后每一次render的过程中，都会计算得到它应该经过的点。如上，就做好了一个粒子轨迹。</li>
</ol>
</li>
<li>
<ol start="5">
<li>颜色随机</li>
</ol>
</li>
</ul>
<p>这个就很easy</p>
<hr>
<pre><code class="copyable">    function randomHexColor() &#123; //随机生成十六进制颜色
        return '#' + ('00000' + (Math.random() * 0x1000000 << 0).toString(16)).substr(-6);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-3">源码</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fwangsong1299%2Fcanvas-open%2Fblob%2Fmaster%2Flocus%2Fdemo.html" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/wangsong1299/canvas-open/blob/master/locus/demo.html" ref="nofollow noopener noreferrer">源码</a></p></div>  
</div>
            