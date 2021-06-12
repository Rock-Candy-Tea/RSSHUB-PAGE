
---
title: 'Canvas 基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/525f11b2bfd74ec8ba3762636bbda56e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 00:46:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/525f11b2bfd74ec8ba3762636bbda56e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第6天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">基本用法</h2>
<ul>
<li><code>canvas</code> 看起来和 <code>img</code> 很像，不同在于
<ul>
<li>没有 <code>src alt</code> 属性</li>
<li>需要结束标签 <code></canvas></code> 不可省略</li>
</ul>
</li>
<li>只有两个属性 <code>width height</code>，没有设置的时候默认值为 <code>width:300px height:150px</code></li>
<li><code>id</code> 不是 <code>canvas</code> 特有，每个标签都有</li>
</ul>
<h3 data-id="heading-1">渲染上下文</h3>
<p><code>canvas</code> 创造了一个大小固定的画布，通过其渲染上下文可以用来绘制和处理需要展示的内容（主要是 <code>2D</code>，<code>WebGl</code> 处理 <code>3D</code>）</p>
<p>获取渲染上下文：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"tutorial"</span>);
<span class="hljs-keyword">var</span> ctx = canvas.getContext(<span class="hljs-string">"2d"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">检查支持性</h3>
<p>通过 <code>getContext</code> 检查是否支持 <code>canvas</code> ，不支持则显示替代内容：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"tutorial"</span>);

<span class="hljs-keyword">if</span> (canvas.getContext) &#123;
  <span class="hljs-keyword">var</span> ctx = canvas.getContext(<span class="hljs-string">"2d"</span>);
  <span class="hljs-comment">// drawing code here</span>
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// canvas-unsupported code here</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">例子</h3>
<p>下面绘制两个正方形：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/525f11b2bfd74ec8ba3762636bbda56e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <canvas id="canvas-t-1" width="150" height="150"></canvas>
</template>

<script>
export default &#123;
  data() &#123;
    return &#123;&#125;;
  &#125;,
  methods: &#123;
    draw() &#123;
      let canvas = document.getElementById("canvas-t-1");
      if (canvas.getContext) &#123;
        // 获取渲染上下文
        var ctx = canvas.getContext("2d");

        // 设置正方形1
        ctx.fillStyle = "rgb(200,0,0)"; // 颜色
        ctx.fillRect(10, 10, 50, 50); // 坐标 x,y 长宽

        // 设置正方形2
        ctx.fillStyle = "rgb(0,0,200,0.5)"; // 颜色
        ctx.fillRect(30, 30, 50, 50); // 坐标 x,y 长宽
      &#125;
    &#125;
  &#125;,
  mounted() &#123;
    this.draw();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">绘制基本图形</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5258374a17004941815f3d8de27b4df2~tplv-k3u1fbpfcp-watermark.image" alt="canvas_t_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>canvas</code> 元素默认被网格所覆盖。通常来说网格中的一个单元相当于<code>canvas</code> 元素中的一像素。栅格的起点为左上角（坐标为（<code>0,0</code>））。所有元素的位置都相对于原点定位。所以图中蓝色方形左上角的坐标为距离左边（<code>X 轴</code>）x 像素，距离上边（<code>Y 轴</code>）y 像素（坐标为（<code>x,y</code>））</p>
<h3 data-id="heading-5">绘制矩形</h3>
<p>相关 <code>API</code>：</p>
<ul>
<li>填充矩形 <code>fillRect(x,y,width,height)</code></li>
<li>矩形边框 <code>strokeRect(x,y,width,height)</code></li>
<li>清除矩形 <code>clearRect(x,y,width,height)</code></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54732d78c9e74509abd7ce48652de5c7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>
    <canvas id="canvas-t-2-rect" width="150" height="150"> </canvas>
    <button @click="drawArea">绘制填充矩形</button>
    <button @click="drawStroke">绘制矩形边框</button>
    <button @click="clearRect">清除矩形</button>
  </div>
</template>

<script>
export default &#123;
  data() &#123;
    return &#123;&#125;;
  &#125;,
  methods: &#123;
    drawArea() &#123;
      let canvas = document.getElementById("canvas-t-2-rect");
      if (canvas.getContext) &#123;
        var ctx = canvas.getContext("2d");
        ctx.fillStyle = "rgb(0,0,200,0.5)"; // 颜色
        ctx.fillRect(30, 30, 50, 50); // 坐标 x,y 长宽
      &#125;
    &#125;,
    drawStroke() &#123;
      let canvas = document.getElementById("canvas-t-2-rect");
      if (canvas.getContext) &#123;
        var ctx = canvas.getContext("2d");
        ctx.strokeStyle = "green"; // 颜色
        ctx.strokeRect(20, 20, 70, 70); // 坐标 x,y 长宽
      &#125;
    &#125;,
    clearRect() &#123;
      let canvas = document.getElementById("canvas-t-2-rect");
      if (canvas.getContext) &#123;
        var ctx = canvas.getContext("2d");
        ctx.clearRect(19, 19, 72, 72); // 坐标 x,y 长宽
      &#125;
    &#125;
  &#125;,
  mounted() &#123;
    this.drawArea();
    this.drawStroke();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">绘制路径</h3>
<p>图形的基本元素是路径。路径是通过不同颜色和宽度的线段或曲线相连形成的不同形状的点的集合。一个路径，甚至一个子路径，都是闭合的。使用路径绘制图形需要一些额外的步骤：</p>
<ol>
<li>首先，你需要创建路径起始点。</li>
<li>然后你使用画图命令去画出路径。</li>
<li>之后你把路径封闭。</li>
<li>一旦路径生成，你就能通过描边或填充路径区域来渲染图形</li>
</ol>
<p>相关 <code>API</code>:</p>
<ul>
<li>
<p>新建路径 <code>beginPath</code></p>
</li>
<li>
<p>闭合路径 <code>closePath</code></p>
</li>
<li>
<p>绘制轮廓 <code>stroke</code></p>
</li>
<li>
<p>填充 <code>fill</code></p>
</li>
<li>
<p>移动笔触 <code>moveTo(x,y)</code></p>
</li>
<li>
<p>绘制直线 <code>lineTo(x,y)</code></p>
</li>
<li>
<p>圆弧</p>
<ul>
<li><code>arc(x, y, radius, startAngle, endAngle, anticlockwise)</code>：<code>x,y</code> 为圆心的以 <code>radius</code> 为半径的圆弧 从 <code>startAngle</code>弧度到 <code>endAngle</code> 按照 <code>anticlockwise</code> 给定（默认顺时针）方向生成</li>
<li><code>arcTo(x1, y1, x2, y2, radius)</code>：根据给定控制点和半径画圆弧，再以直线连接两个控制点</li>
</ul>
</li>
<li>
<p>贝塞尔曲线</p>
<ul>
<li><code>quadraticCurveTo(cp1x, cp1y, x, y)</code>：绘制二次贝塞尔曲线，<code>cp1x,cp1y</code> 为一个控制点，<code>x,y</code> 为结束点</li>
<li><code>bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y)</code>：绘制三次贝塞尔曲线，<code>cp1x,cp1y</code> 为控制点一，<code>cp2x,cp2y</code> 为控制点二，<code>x,y</code> 为结束点</li>
</ul>
</li>
</ul>
<p><strong>注</strong></p>
<ul>
<li>新建路径之后 <code>beginPath</code> 调用之后，第一条路径构造命令通常是 <code>moveTo</code></li>
<li>调用 <code>fill</code> 所有没有闭合的形状都会闭合，就不需要调用 <code>closePath</code>，但是调用 <code>stroke</code> 就不会自动闭合</li>
<li><code>弧度=(Math.PI/180)*角度</code></li>
</ul>
<p>绘制三角形：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a67a6877dde14575ba378664c5770de2~tplv-k3u1fbpfcp-watermark.image" alt="捕获.PNG" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>
    <canvas id="canvas-t-2-triangle" width="150" height="150"> </canvas>
  </div>
</template>

<script>
export default &#123;
  data() &#123;
    return &#123;&#125;;
  &#125;,
  methods: &#123;
    drawTFill() &#123;
      let canvas = document.getElementById("canvas-t-2-triangle");
      if (canvas.getContext) &#123;
        var ctx = canvas.getContext("2d");
        // 填充三角形
        ctx.beginPath();
        ctx.moveTo(25, 25);
        ctx.lineTo(105, 25);
        ctx.lineTo(25, 105);
        ctx.fill();
      &#125;
    &#125;,
    drawTStroke() &#123;
      let canvas = document.getElementById("canvas-t-2-triangle");
      if (canvas.getContext) &#123;
        var ctx = canvas.getContext("2d");
        // 描边三角形
        ctx.beginPath();
        ctx.moveTo(125, 125);
        ctx.lineTo(125, 45);
        ctx.lineTo(45, 125);
        ctx.closePath();
        ctx.stroke();
      &#125;
    &#125;
  &#125;,
  mounted() &#123;
    this.drawTFill();
    this.drawTStroke();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>绘制笑脸（圆弧）：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/372b435902db40be94fe121558072275~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>
    <canvas id="canvas-t-2-arc" width="150" height="150"> </canvas>
  </div>
</template>

<script>
export default &#123;
  data() &#123;
    return &#123;&#125;;
  &#125;,
  methods: &#123;
    drawArc() &#123;
      let canvas = document.getElementById("canvas-t-2-arc");
      if (canvas.getContext) &#123;
        var ctx = canvas.getContext("2d");

        ctx.beginPath();
        ctx.arc(75, 75, 50, 0, Math.PI * 2, true); // 脸
        ctx.moveTo(110, 75);
        ctx.arc(75, 75, 35, 0, Math.PI, false); // 口(顺时针)
        ctx.moveTo(65, 65);
        ctx.arc(60, 65, 5, 0, Math.PI * 2, true); // 左眼
        ctx.moveTo(95, 65);
        ctx.arc(90, 65, 5, 0, Math.PI * 2, true); // 右眼
        ctx.stroke();
      &#125;
    &#125;
  &#125;,
  mounted() &#123;
    this.drawArc();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>绘制对话气泡（二次贝塞尔）：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bf987e79580496dba2379e258182c78~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>
    <canvas id="canvas-t-2-quadraticCurve" width="150" height="150"> </canvas>
  </div>
</template>

<script>
export default &#123;
  data() &#123;
    return &#123;&#125;;
  &#125;,
  methods: &#123;
    drawQC() &#123;
      let canvas = document.getElementById("canvas-t-2-quadraticCurve");
      if (canvas.getContext) &#123;
        var ctx = canvas.getContext("2d");

        // 二次贝塞尔曲线
        ctx.beginPath();
        ctx.moveTo(75, 25);
        ctx.quadraticCurveTo(25, 25, 25, 62.5);
        ctx.quadraticCurveTo(25, 100, 50, 100);
        ctx.quadraticCurveTo(50, 120, 30, 125);
        ctx.quadraticCurveTo(60, 120, 65, 100);
        ctx.quadraticCurveTo(125, 100, 125, 62.5);
        ctx.quadraticCurveTo(125, 25, 75, 25);
        ctx.stroke();
      &#125;
    &#125;
  &#125;,
  mounted() &#123;
    this.drawQC();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>绘制心形（三次贝塞尔）：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/354f648b6a4446d2867ba94a996eda54~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>
    <canvas id="canvas-t-2-bezierCurve" width="150" height="150"> </canvas>
  </div>
</template>

<script>
export default &#123;
  data() &#123;
    return &#123;&#125;;
  &#125;,
  methods: &#123;
    drawBC() &#123;
      let canvas = document.getElementById("canvas-t-2-bezierCurve");
      if (canvas.getContext) &#123;
        var ctx = canvas.getContext("2d");

        //三次贝塞尔曲线
        ctx.beginPath();
        ctx.moveTo(75, 40);
        ctx.bezierCurveTo(75, 37, 70, 25, 50, 25);
        ctx.bezierCurveTo(20, 25, 20, 62.5, 20, 62.5);
        ctx.bezierCurveTo(20, 80, 40, 102, 75, 120);
        ctx.bezierCurveTo(110, 102, 130, 80, 130, 62.5);
        ctx.bezierCurveTo(130, 62.5, 130, 25, 100, 25);
        ctx.bezierCurveTo(85, 25, 75, 37, 75, 40);
        ctx.fill();
      &#125;
    &#125;
  &#125;,
  mounted() &#123;
    this.drawBC();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7"><code>Path2D</code> 对象</h3>
<blockquote>
<p>为了简化代码和提高性能，可以使用 <code>Path2D</code> 用来缓存或记录绘画命令</p>
</blockquote>
<p>常用 <code>API</code>：</p>
<ul>
<li><code>Path2D(path)</code>：返回一个 <code>Path2D</code> 对象，用一个路径或者一个 <code>svg path</code> 的字符串来初始化</li>
<li><code>Path2D.addPath(path,transform)</code>：添加一条路径或者变换矩阵</li>
</ul>
<p>示例：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57e2f9c0134940ee95f600471b8e40b1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <canvas id="canvas-t-2-path2d"> </canvas>
</template>

<script>
export default &#123;
  methods: &#123;
    drawPath2D() &#123;
      let canvas = document.getElementById("canvas-t-2-path2d");
      if (canvas.getContext) &#123;
        let ctx = canvas.getContext("2d");

        // 缓存正方形
        let rectIns = new Path2D();
        rectIns.rect(10, 10, 50, 50);
        ctx.strokeStyle = "green";
        ctx.stroke(rectIns);

        // 缓存圆形
        let circle = new Path2D();
        circle.moveTo(125, 35);
        circle.arc(100, 35, 25, 0, 2 * Math.PI);
        ctx.fillStyle = "red";
        ctx.fill(circle);

        // 缓存 svg path 字符串
        let p = new Path2D("M5 5 h 80 v 80 h -80 Z");
        ctx.strokeStyle = "blue";
        ctx.stroke(p);
      &#125;
    &#125;
  &#125;,
  mounted() &#123;
    this.drawPath2D();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">设置样式</h2>
<blockquote>
<p>通过设置 <strong>绘制上下文</strong> 对应属性来修改样式，绘制图形的样式由最近一次设置决定</p>
</blockquote>
<h3 data-id="heading-9">颜色</h3>
<p>通过两个属性来设置：</p>
<ul>
<li><code>fillStyle = color</code>：填充颜色</li>
<li><code>strokeStyle = color</code>：描边颜色</li>
</ul>
<p><code>color</code> 可以是：</p>
<ul>
<li><code>orange</code></li>
<li><code>#fff</code></li>
<li><code>rgb(255,255,0)</code></li>
<li><code>rgba(255,255,0,0.1)</code></li>
</ul>
<p><code>fillStyle</code> 示例：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e573aa3fdd6f46c3b42fba2110ccb31f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <canvas id="canvas-t-3-fill"></canvas>
</template>

<script>
export default &#123;
  methods: &#123;
    drawFillStyle() &#123;
      var ctx = document.getElementById("canvas-t-3-fill").getContext("2d");
      for (var i = 0; i < 6; i++) &#123;
        for (var j = 0; j < 6; j++) &#123;
          ctx.fillStyle =
            "rgb(" +
            Math.floor(255 - 42.5 * i) +
            "," +
            Math.floor(255 - 42.5 * j) +
            ",0)";
          ctx.fillRect(j * 25, i * 25, 25, 25);
        &#125;
      &#125;
    &#125;
  &#125;,
  mounted() &#123;
    this.drawFillStyle();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>strokeStyle</code> 示例：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/181e95d384a5413b98e90195b36c7f55~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <canvas id="canvas-t-3-stroke"></canvas>
</template>

<script>
export default &#123;
  methods: &#123;
    drawStrokeStyle() &#123;
      var ctx = document.getElementById("canvas-t-3-stroke").getContext("2d");
      for (var i = 0; i < 6; i++) &#123;
        for (var j = 0; j < 6; j++) &#123;
          ctx.strokeStyle =
            "rgb(0," +
            Math.floor(255 - 42.5 * i) +
            "," +
            Math.floor(255 - 42.5 * j) +
            ")";
          ctx.beginPath();
          ctx.arc(12.5 + j * 25, 12.5 + i * 25, 10, 0, Math.PI * 2, true);
          ctx.stroke();
        &#125;
      &#125;
    &#125;
  &#125;,
  mounted() &#123;
    this.drawStrokeStyle();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">透明度</h3>
<blockquote>
<p><code>globalAlpha = transparencyValue</code> 设置透明度</p>
</blockquote>
<p>这样设置更灵活，可以单独设置轮廓和填充透明度：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 指定透明颜色，用于描边和填充样式</span>
ctx.strokeStyle = <span class="hljs-string">"rgba(255,0,0,0.5)"</span>;
ctx.fillStyle = <span class="hljs-string">"rgba(255,0,0,0.5)"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例子：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f772f6e6ec641aca0c0407f1fe6d413~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <canvas id="canvas-t-3-globalAlpha"></canvas>
</template>

<script>
export default &#123;
  methods: &#123;
    drawGlobalAlpha() &#123;
      var ctx = document
        .getElementById("canvas-t-3-globalAlpha")
        .getContext("2d");
      // 画背景
      ctx.fillStyle = "#FD0";
      ctx.fillRect(0, 0, 75, 75);
      ctx.fillStyle = "#6C0";
      ctx.fillRect(75, 0, 75, 75);
      ctx.fillStyle = "#09F";
      ctx.fillRect(0, 75, 75, 75);
      ctx.fillStyle = "#F30";
      ctx.fillRect(75, 75, 75, 75);
      ctx.fillStyle = "#FFF";

      // 设置透明度值
      ctx.globalAlpha = 0.2;

      // 画半透明圆
      for (var i = 0; i < 7; i++) &#123;
        ctx.beginPath();
        ctx.arc(75, 75, 10 + 10 * i, 0, Math.PI * 2, true);
        ctx.fill();
      &#125;
    &#125;
  &#125;,
  mounted() &#123;
    this.drawGlobalAlpha();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">线</h3>
<p>线的样式属性：</p>
<ul>
<li><code>lineWidth</code>：线条宽度</li>
<li><code>lineCap</code>：线条末端样式</li>
<li><code>lineJoin</code>：线条之间结合处样式</li>
<li><code>miterLimit</code>：限制当两条线相交时交接处最大长度</li>
</ul>
<p>虚线：</p>
<ul>
<li><code>getLineDash()</code>：获取当前虚线样式</li>
<li><code>setLineDash()</code>：设置当前虚线样式</li>
<li><code>lineDashOffset</code>：设置虚线样式的起始偏移</li>
</ul>
<p>像素边缘：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e296fc2ea72541a1bbc2188c8a9ac507~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <canvas id="canvas-t-3-line"></canvas>
</template>

<script>
export default &#123;
  methods: &#123;
    drawLine() &#123;
      var ctx = document.getElementById("canvas-t-3-line").getContext("2d");
      ctx.lineWidth = 1;
      ctx.beginPath();
      // 边界不在像素边缘上
      ctx.moveTo(5, 5);
      ctx.lineTo(5, 100);

      // 边界在像素边缘上
      ctx.moveTo(25.5, 5);
      ctx.lineTo(25.5, 100);
      ctx.stroke();
    &#125;
  &#125;,
  mounted() &#123;
    this.drawLine();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/120f23e87ca14a6b842ef6f9f66cd2bd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果线条的边缘不在像素边界上，如左图就会导致渲染不精确，在像素边缘上就如右图，上面例子第一个线条边缘不在边界上，第二个在，明显第一个绘制不精确</p>
<h3 data-id="heading-12">渐变</h3>
<ul>
<li><code>createLinearGradient(x1, y1, x2, y2)</code> 线性渐变</li>
<li><code>createRadialGradient(x1, y1, r1, x2, y2, r2)</code> 径向渐变</li>
<li><code>gradient.addColorStop(position, color)</code> 添加色标</li>
</ul>
<p><code>createLinearGradient</code> 例子:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d28337affe0e4ee586f6c30466542031~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <canvas id="canvas-t-3-linerGradients"></canvas>
</template>

<script>
export default &#123;
  methods: &#123;
    drawLinerGradients() &#123;
      var ctx = document
        .getElementById("canvas-t-3-linerGradients")
        .getContext("2d");
      // Create gradients
      var lingrad = ctx.createLinearGradient(0, 0, 0, 150);
      lingrad.addColorStop(0, "#00ABEB");
      lingrad.addColorStop(0.5, "#fff");
      lingrad.addColorStop(0.5, "#26C000");
      lingrad.addColorStop(1, "#fff");

      var lingrad2 = ctx.createLinearGradient(0, 50, 0, 95);
      lingrad2.addColorStop(0.5, "#000");
      lingrad2.addColorStop(1, "rgba(0,0,0,0)");

      // assign gradients to fill and stroke styles
      ctx.fillStyle = lingrad;
      ctx.strokeStyle = lingrad2;

      // draw shapes
      ctx.fillRect(10, 10, 130, 130);
      ctx.strokeRect(50, 50, 50, 50);
    &#125;
  &#125;,
  mounted() &#123;
    this.drawLinerGradients();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>createRadialGradient</code> 例子:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c4deed3837c4c36bebc3f9506363130~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <canvas id="canvas-t-3-radialGradient"></canvas>
</template>

<script>
export default &#123;
  methods: &#123;
    drawRadialGradient() &#123;
      var ctx = document
        .getElementById("canvas-t-3-radialGradient")
        .getContext("2d");
      // Create gradients
      var radgrad = ctx.createRadialGradient(45, 45, 10, 52, 50, 30);
      radgrad.addColorStop(0, "#A7D30C");
      radgrad.addColorStop(0.9, "#019F62");
      radgrad.addColorStop(1, "rgba(1,159,98,0)");

      var radgrad2 = ctx.createRadialGradient(105, 105, 20, 112, 120, 50);
      radgrad2.addColorStop(0, "#FF5F98");
      radgrad2.addColorStop(0.75, "#FF0188");
      radgrad2.addColorStop(1, "rgba(255,1,136,0)");

      var radgrad3 = ctx.createRadialGradient(95, 15, 15, 102, 20, 40);
      radgrad3.addColorStop(0, "#00C9FF");
      radgrad3.addColorStop(0.8, "#00B5E2");
      radgrad3.addColorStop(1, "rgba(0,201,255,0)");

      var radgrad4 = ctx.createRadialGradient(0, 150, 50, 0, 140, 90);
      radgrad4.addColorStop(0, "#F4F201");
      radgrad4.addColorStop(0.8, "#E4C700");
      radgrad4.addColorStop(1, "rgba(228,199,0,0)");

      // 画图形
      ctx.fillStyle = radgrad4;
      ctx.fillRect(0, 0, 150, 150);
      ctx.fillStyle = radgrad3;
      ctx.fillRect(0, 0, 150, 150);
      ctx.fillStyle = radgrad2;
      ctx.fillRect(0, 0, 150, 150);
      ctx.fillStyle = radgrad;
      ctx.fillRect(0, 0, 150, 150);
    &#125;
  &#125;,
  mounted() &#123;
    this.drawRadialGradient();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">图案</h3>
<p><code>createPattern(image, type)</code>:</p>
<ul>
<li><code>Image</code> 可以是一个 <code>Image</code> 对象的引用，或者另一个 <code>canvas</code> 对象</li>
<li><code>Type</code>：<code>repeat，repeat-x，repeat-y 和 no-repeat</code></li>
</ul>
<p>例：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <canvas id="canvas-t-3-Patterns"></canvas>
</template>

<script>
export default &#123;
  methods: &#123;
    drawPatterns() &#123;
      var ctx = document.getElementById("canvas-t-3-Patterns").getContext("2d");
      // 创建新 image 对象，用作图案
      var img = new Image();
      img.src = "/Grimoire/css_amazing_1.png";
      img.onload = function() &#123;
        // 创建图案
        var ptrn = ctx.createPattern(img, "repeat");
        ctx.fillStyle = ptrn;
        ctx.fillRect(0, 0, 150, 150);
      &#125;;
    &#125;
  &#125;,
  mounted() &#123;
    this.drawPatterns();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">阴影</h3>
<ul>
<li><code>shadowOffsetX = float</code> x 轴延伸距离</li>
<li><code>shadowOffsetY = float</code> y 轴延伸距离</li>
<li><code>shadowBlur = float</code> 阴影模糊程度</li>
<li><code>shadowColor = color</code> 阴影颜色</li>
</ul>
<p>文字阴影：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15f1c7e59f7b49938ed50e23bf67ef5d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <canvas id="canvas-t-3-Shadows"></canvas>
</template>

<script>
export default &#123;
  methods: &#123;
    drawShadows() &#123;
      var ctx = document.getElementById("canvas-t-3-Shadows").getContext("2d");
      ctx.shadowOffsetX = 2;
      ctx.shadowOffsetY = 2;
      ctx.shadowBlur = 2;
      ctx.shadowColor = "rgba(0, 0, 0, 0.5)";

      ctx.font = "20px Times New Roman";
      ctx.fillStyle = "Black";
      ctx.fillText("Sample String", 5, 30);
      ctx.strokeText("Sample String", 150, 30);
    &#125;
  &#125;,
  mounted() &#123;
    this.drawShadows();
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">参考</h2>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Canvas_API/Tutorial" target="_blank" rel="nofollow noopener noreferrer">mdn canvas 教程</a></li>
</ul></div>  
</div>
            