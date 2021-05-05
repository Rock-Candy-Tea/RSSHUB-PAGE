
---
title: '假如只剩下canvas标签'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/780f76521af74f218a9278287beb3e84~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 04 May 2021 16:43:27 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/780f76521af74f218a9278287beb3e84~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>关注公众号“执鸢者”，回复“canvas”获取对应源码，回复“资料”获取500G资料（各“兵种”均有），还有专业交流群等你一起来潇洒。</p>
</blockquote>
<h2 data-id="heading-0">一、背景</h2>
<blockquote>
<p>如果只剩下canvas标签，该如何去绘制页面中的内容呢？这也许是一个伪命题，但是用canvas确事能够帮助完成很多事。今天就用canvas+AST语法树构建一个信息流样式。</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/780f76521af74f218a9278287beb3e84~tplv-k3u1fbpfcp-watermark.image" alt="canvas信息流.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">二、绘制流程</h2>
<blockquote>
<p>将整个绘制流程分为三部分：基本元素、AST语法树、主函数类。基本元素指的是图片、文字、矩形、圆等；AST语法树在本处值得就是包含一些属性的js对象；主函数类指对外暴露的接口，通过调用实现最终绘制。</p>
</blockquote>
<h3 data-id="heading-2">2.1 基本元素</h3>
<blockquote>
<p>不管多么复杂的事物肯定都是由一系列简单的元素组成，例如汽车肯定是通过一些简单的机械零配件组成；电脑也是通过电阻、电容等零配件组成。网页也不例外，也是通过文字、图片、矩形等组成。</p>
</blockquote>
<h4 data-id="heading-3">2.1.1 加载图片</h4>
<blockquote>
<p>图片是一个页面中的灵魂元素，在页面中占据绝大部分空间。</p>
</blockquote>
<pre><code class="copyable">class DrawImage &#123;
    constructor(ctx, imageObj) &#123;
        this.ctx = ctx;
        this.imageObj = imageObj;
    &#125;

    draw() &#123;
        const &#123;centerX, centerY, src, sx = 1, sy = 1&#125; = this.imageObj;
        const img = new Image();
        img.onload = () => &#123;
            const imgWidth = img.width;
            const imgHeight = img.height;
            this.ctx.save();
            this.ctx.scale(sx, sy);
            this.ctx.drawImage(img, centerX - imgWidth * sx / 2, centerY - imgHeight * sy / 2);
            this.ctx.restore();
        &#125;;
        img.src = src;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">2.1.2 绘制文字</h4>
<blockquote>
<p>文字能够提高页面的可读性，让观察该页面的每一个人都能够快速了解该页面的思想。</p>
</blockquote>
<pre><code class="copyable">class DrawText &#123;
    constructor(ctx, textObj) &#123;
        this.ctx = ctx;
        this.textObj = textObj;
    &#125;

    draw() &#123;
        const &#123;x, y, font, content, lineHeight = 20, width, fillStyle = '#000000', textAlign = 'start', textBaseline = 'middle'&#125; = this.textObj;
        const branchsContent = this.getBranchsContent(content, width);
        this.ctx.save();
        this.ctx.fillStyle = fillStyle;
        this.ctx.textAlign = textAlign;
        this.ctx.textBaseline = textBaseline;
        this.ctx.font = font;
        branchsContent.forEach((branchContent, index) => &#123;
            this.ctx.fillText(branchContent, x, y + index * lineHeight);
        &#125;);
        this.ctx.restore();
    &#125;

    getBranchsContent(content, width) &#123;
        if (!width) &#123;
            return [content];
        &#125;
        const charArr = content.split('');
        const branchsContent = [];
        let tempContent = '';
        charArr.forEach(char => &#123;
            if (this.ctx.measureText(tempContent).width < width && this.ctx.measureText(tempContent + char).width <= width) &#123;
                tempContent += char;
            &#125;
            else &#123;
                branchsContent.push(tempContent);
                tempContent = '';
            &#125;
        &#125;);
        branchsContent.push(tempContent);
        return branchsContent;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">2.1.3 绘制矩形</h4>
<blockquote>
<p>通过矩形元素能够与文字等元素配合达到意想不到的效果。</p>
</blockquote>
<pre><code class="copyable">class DrawRect &#123;
    constructor(ctx, rectObj) &#123;
        this.ctx = ctx;
        this.rectObj = rectObj;
    &#125;

    draw() &#123;
        const &#123;x, y, width, height, fillStyle, lineWidth = 1&#125; = this.rectObj;
        this.ctx.save();
        this.ctx.fillStyle = fillStyle;
        this.ctx.lineWidth = lineWidth;
        this.ctx.fillRect(x, y, width, height);
        this.ctx.restore();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.1.4 绘制圆</h3>
<blockquote>
<p>圆与矩形承担的角色一致，也是在页面中比较重要的角色。</p>
</blockquote>
<pre><code class="copyable">class DrawCircle &#123;
    constructor(ctx, circleObj) &#123;
        this.ctx = ctx;
        this.circleObj = circleObj;
    &#125;

    draw() &#123;
        const &#123;x, y, R, startAngle = 0, endAngle = Math.PI * 2, lineWidth = 1, fillStyle&#125; = this.circleObj;
        this.ctx.save();
        this.ctx.lineWidth = lineWidth;
        this.ctx.fillStyle = fillStyle;
        this.ctx.beginPath();
        this.ctx.arc(x, y, R, startAngle, endAngle);
        this.ctx.closePath();
        this.ctx.fill();
        this.ctx.restore();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">2.2 AST树</h3>
<blockquote>
<p>AST抽象语法树是源代码语法结构的一种抽象表示。它以树状的形式表现编程语言的语法结构，树上的每个节点都表示源代码中的一种结构。例如，在Vue中，将模板语法转换为AST抽象语法树，然后再将抽象语法树转换为HTML结构，咱们在利用canvas绘制页面时也利用AST抽象语法树来表示页面中的内容，实现的类型有rect（矩形）、img（图片）、text（文字）、circle（圆）。</p>
</blockquote>
<blockquote>
<p>本次将绘制的内容包含静态页面部分和动画部分，所以将利用两个canvas实现，每个canvas将对应一个AST树，分别为静态部分AST树和动态部分AST树。</p>
</blockquote>
<h4 data-id="heading-8">2.2.1 静态部分AST树</h4>
<blockquote>
<p>本次绘制的页面中静态部分的AST树如下所示，包含矩形、图片、文字。</p>
</blockquote>
<pre><code class="copyable">const graphicAst = [
    &#123;
        type: 'rect',
        x: 0,
        y: 0,
        width: 1400,
        height: 400,
        fillStyle: '#cec9ae'
    &#125;,
    &#123;
        type: 'img',
        centerX: 290,
        centerY: 200,
        sx: 0.9,
        sy: 0.9,
        src: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_match%2F0%2F11858683821%2F0.jpg&refer=http%3A%2F%2Finews.gtimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1622015341&t=cc1bd95777dfa37d88c48bb6e179778e'
    &#125;,
    &#123;
        type: 'text',
        x: 600,
        y: 60,
        textAlign: 'start',
        textBaseline: 'middle',
        font: 'normal 40px serif',
        lineHeight: 50,
        width: 180,
        fillStyle: '#000000',
        content: '灰太狼是最好的一头狼，它每天都在梦想着吃羊，一直没有实现，但是从不气馁。'
    &#125;,
    &#123;
        type: 'text',
        x: 600,
        y: 170,
        textAlign: 'start',
        textBaseline: 'middle',
        font: 'normal 30px serif',
        lineHeight: 50,
        width: 180,
        fillStyle: '#7F7F7F',
        content: '为灰太狼加油、为灰太狼喝彩，😄'
    &#125;,
    &#123;
        type: 'text',
        x: 1200,
        y: 360,
        textAlign: 'start',
        textBaseline: 'ideographic',
        font: 'normal 30px serif',
        lineHeight: 50,
        width: 180,
        fillStyle: '#949494',
        content: '阅读'
    &#125;,
    &#123;
        type: 'text',
        x: 1260,
        y: 363,
        textAlign: 'start',
        textBaseline: 'ideographic',
        font: 'normal 30px serif',
        lineHeight: 50,
        width: 180,
        fillStyle: '#949494',
        content: '520'
    &#125;
];
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">2.2.2 动态部分AST树</h4>
<blockquote>
<p>本次绘制的页面中动画部分的AST树动态生成，由一系列动态颜色的圆组成。</p>
</blockquote>
<pre><code class="copyable">function getMarqueeAst(startX, endX, count, options = &#123;&#125;) &#123;
    const &#123;y = 15, R = 15&#125; = options;
    if (!(endX >= startX && count > 0)) &#123;
        return [];
    &#125;
    const interval = (endX - startX) / count;
    const marqueeAstArr = [];
    for (let i = 0; i < count; i++) &#123;
        const RValue = Math.random() * 255;
        const GValue = Math.random() * 255;
        const BValue = Math.random() * 255;
        const fillStyle = `rgb($&#123;RValue&#125;, $&#123;GValue&#125;, $&#123;BValue&#125;)`;
        marqueeAstArr.push(&#123;
            type: 'circle',
            x: startX + i * interval,
            y,
            R,
            fillStyle
        &#125;);
    &#125;

    return marqueeAstArr;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2.3 主函数类</h3>
<blockquote>
<p>除了上述一些基本元素类，将通过一个主函数类对外进行暴露。</p>
</blockquote>
<pre><code class="copyable">class Draw &#123;
    constructor(canvasDom) &#123;
        this._canvasDom = canvasDom;
        this.ctx = this._canvasDom.getContext('2d');
        this.width = this._canvasDom.width;
        this.height = this._canvasDom.height;
    &#125;

    // 绘制函数
    draw(ast) &#123;
        ast.forEach(elementObj => &#123;
            this.drawFactory(elementObj);
            const &#123;children&#125; = elementObj;
            // 递归调用
            if (children && Array.isArray(children)) &#123;
                this.draw(children);
            &#125;
        &#125;);
    &#125;

    // 工厂模型绘制对应基本元素
    drawFactory(elementObj) &#123;
        const &#123;type&#125; = elementObj;
        switch(type) &#123;
            case 'img': &#123;
                this.drawImage(elementObj);
                break;
            &#125;
            case 'text': &#123;
                this.drawText(elementObj);
                break;
            &#125;
            case 'rect': &#123;
                this.drawRect(elementObj);
                break;
            &#125;
            case 'circle': &#123;
                this.drawCircle(elementObj);
                break;
            &#125;
        &#125;
    &#125;

    drawImage(imageObj) &#123;
        const drawImage = new DrawImage(this.ctx, imageObj);
        drawImage.draw();
    &#125;

    drawText(textObj) &#123;
        const drawText = new DrawText(this.ctx, textObj);
        drawText.draw();
    &#125;

    drawRect(rectObj) &#123;
        const drawRect = new DrawRect(this.ctx, rectObj);
        drawRect.draw();
    &#125;

    drawCircle(circleObj) &#123;
        const drawCircle = new DrawCircle(this.ctx, circleObj);
        drawCircle.draw();
    &#125;

    clearCanvas() &#123;
        this.ctx.clearRect(0, 0, this.width, this.height);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">2.4 内容绘制</h3>
<blockquote>
<p>前面的准备工作已经完成，下面将各个函数和AST树联动起来，达到想要的效果。</p>
</blockquote>
<h4 data-id="heading-12">2.4.1 静态内容绘制</h4>
<blockquote>
<p>先将静态部分的内容绘制好，作为页面的基石。</p>
</blockquote>
<pre><code class="copyable">const basicCanvasDom = document.getElementById('basicCanvas');
const drawBasicInstance = new Draw(basicCanvasDom);
drawBasicInstance.draw(graphicAst);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78ac1f956f6d4fe5a02b928d3c5e2ccf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">2.4.2 绘制动画跑马灯</h4>
<blockquote>
<p>再给该部分内容来点动画效果，更加激动人心。</p>
</blockquote>
<pre><code class="copyable">const animationCanvasDom = document.getElementById('animationCanvas');
const drawAnimationInstance = new Draw(animationCanvasDom);

let renderCount = 0;
function animate() &#123;
    if (renderCount % 5 === 0) &#123;
        drawAnimationInstance.clearCanvas();
        drawAnimationInstance.draw(getMarqueeAst(20, 1440, 22));
        drawAnimationInstance.draw(getMarqueeAst(20, 1440, 22, &#123;
            y: 380
        &#125;));
    &#125;
    window.requestAnimationFrame(animate);
    renderCount++;
&#125;
animate();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/780f76521af74f218a9278287beb3e84~tplv-k3u1fbpfcp-watermark.image" alt="canvas信息流.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>本文对应源码，关注公众号“执鸢者”，回复“canvas”获取</p>
</li>
<li>
<p>如果觉得这篇文章还不错，来个分享、点赞吧，让更多的人也看到</p>
</li>
</ol></div>  
</div>
            