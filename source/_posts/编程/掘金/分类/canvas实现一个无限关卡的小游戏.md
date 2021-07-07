
---
title: 'canvas实现一个无限关卡的小游戏'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3965a36c8df54765adb325ae15249bf3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 18:12:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3965a36c8df54765adb325ae15249bf3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>「本文已参与好文召集令活动，点击查看：后端、大前端双赛道投稿，2万元奖池等你挑战！」</p>
<h2 data-id="heading-0">知识储备</h2>
<p>canvas API， 简单的js语法， 前端动画的一些小知识</p>
<h2 data-id="heading-1">最终效果</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3965a36c8df54765adb325ae15249bf3~tplv-k3u1fbpfcp-watermark.image" alt="微信截图_20210706095352.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fherohql521.github.io%2Fblog-demos%2Fmoving%2Findex.htm" target="_blank" rel="nofollow noopener noreferrer" title="https://herohql521.github.io/blog-demos/moving/index.htm" ref="nofollow noopener noreferrer">新窗口打开</a></p>
<h2 data-id="heading-2">关键点</h2>
<ul>
<li>1 定义怪物属性：坐标 &#123;x,y&#125;及速度&#123;vx,vy&#125;,每个都是一个对象，存于数组中</li>
<li>2 canvas绘制</li>
<li>3 requestAnimationFrame 重复绘制每帧画面</li>
<li>4 边界检测，反向运动</li>
<li>5 点击检测</li>
<li>6 显示对话，长大动画</li>
<li>7 关卡入场动画</li>
<li>8 游戏数据的维护和绘制</li>
</ul>
<p>下面会对这几个关键点用代码示例进行拆分讲解</p>
<h2 data-id="heading-3">拆解</h2>
<h4 data-id="heading-4">为了更好的理解1-4，做了个简化的demo如下</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a70f69c877e4a099f4d67d0cfac411e~tplv-k3u1fbpfcp-watermark.image" alt="微信截图_20210706095735.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fherohql521.github.io%2Fblog-demos%2Fmoving%2Findex2.htm" target="_blank" rel="nofollow noopener noreferrer" title="https://herohql521.github.io/blog-demos/moving/index2.htm" ref="nofollow noopener noreferrer">新窗口打开</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//喷射点坐标</span>
sx = w / <span class="hljs-number">2</span>;
sy = h / <span class="hljs-number">2</span>;

 <span class="hljs-comment">//放置圆点对象的数组</span>
<span class="hljs-keyword">var</span> circles = [];

<span class="hljs-comment">//初始速度</span>
<span class="hljs-keyword">var</span> vel = <span class="hljs-number">10</span>;

 <span class="hljs-comment">//创建新的圆点并加入数组</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createCircle</span>(<span class="hljs-params"></span>) </span>&#123;
  circles.push(&#123;
      <span class="hljs-attr">x</span>: sx,
      <span class="hljs-attr">y</span>: sy,
      <span class="hljs-attr">v</span>: &#123;
          <span class="hljs-attr">x</span>: vel * <span class="hljs-built_in">Math</span>.random(),
          <span class="hljs-attr">y</span>: vel * <span class="hljs-built_in">Math</span>.random()
      &#125;
  &#125;);
&#125;

<span class="hljs-comment">//清除画布内容</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clear</span>(<span class="hljs-params"></span>) </span>&#123;
    $.fillStyle = <span class="hljs-string">'black'</span>;
    $.fillRect(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,w,h);
&#125;

<span class="hljs-comment">//画圆点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">drawCircle</span>(<span class="hljs-params"></span>) </span>&#123;
  clear();

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i <span class="hljs-keyword">in</span> circles) &#123;
    <span class="hljs-keyword">if</span> (circles[i].x < <span class="hljs-number">5</span> || w - circles[i].x < <span class="hljs-number">5</span>) &#123;
        circles[i].v.x *= -<span class="hljs-number">1</span>;
        circles[i].v.y -= <span class="hljs-number">1</span>;
    &#125;
    <span class="hljs-keyword">if</span> (circles[i].y < <span class="hljs-number">5</span> || h - circles[i].y < <span class="hljs-number">5</span>) &#123;
        circles[i].v.y *= -<span class="hljs-number">1</span>;
        circles[i].v.x -= <span class="hljs-number">1</span>;
    &#125;

    circles[i].x += circles[i].v.x;
    circles[i].y += circles[i].v.y;

    $.fillStyle = <span class="hljs-string">'red'</span>;
    $.beginPath();
    $.arc(circles[i].x, circles[i].y, <span class="hljs-number">20</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">Math</span>.PI * <span class="hljs-number">2</span>, <span class="hljs-literal">true</span>);
    $.closePath();
    $.fill();
  &#125;
&#125;

<span class="hljs-comment">//设置动画的回调函数，使动画持续播放</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateCanvas</span>(<span class="hljs-params"></span>) </span>&#123;
    requestAnimationFrame(updateCanvas),
    drawCircle();
&#125;

<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'mousedown'</span>,createCircle);

<span class="hljs-comment">//页面载入后自行产生一个圆点</span>
createCircle();

<span class="hljs-comment">//触发循环回调，动画即可持续进行</span>
updateCanvas();

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">5点击检测</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//点击检测</span>
can.addEventListener(<span class="hljs-string">'mousedown'</span>,pickHandle)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pickHandle</span>(<span class="hljs-params">ev</span>)</span>&#123;
  <span class="hljs-comment">//console.log(ev.clientX,ev.clientY)</span>
  !data.gameOver && pool.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e,i</span>)</span>&#123;
    <span class="hljs-keyword">var</span> rules =  ev.clientX - e.x < spriteSize 
    &&  ev.clientX - e.x ><span class="hljs-number">0</span> &&   ev.clientY - e.y  ><span class="hljs-number">0</span>  &&  ev.clientY - e.y < spriteSize;
    <span class="hljs-keyword">if</span>(rules && e.silent== <span class="hljs-literal">undefined</span>)&#123;
      e.showDialogue = <span class="hljs-literal">true</span>;<span class="hljs-comment">//显示对话</span>
    &#125;
    <span class="hljs-keyword">if</span>(rules && e.silent==<span class="hljs-literal">true</span>)&#123;
      <span class="hljs-comment">//alert('被你找到了')</span>
      e.v.x = <span class="hljs-number">0</span>;
      e.v.y = <span class="hljs-number">0</span>;
      e.toSize  = <span class="hljs-number">80</span>;
      nextPassTimeOut = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        gameReset();<span class="hljs-comment">//下一关</span>
      &#125;,<span class="hljs-number">500</span>)
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中pool是怪物的数组池，检测方法是根据坐标判断，通过鼠标坐标和数组池坐标匹配。 如上rules成立的前提是绘制怪物以xy为左上角为原点绘制，0 < 点击位置-怪物位置 < 怪物尺寸</p>
<h4 data-id="heading-6">6显示对话，长大动画</h4>
<p>这两个功能需要在绘制时处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">draw</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-comment">//运动</span>
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i <span class="hljs-keyword">in</span> pool)&#123;
    <span class="hljs-keyword">if</span>(pool[i].x < <span class="hljs-number">5</span> ||  WIDTH - pool[i].x < <span class="hljs-number">5</span>)&#123;
      pool[i].v.x *= -<span class="hljs-number">1</span>;
    &#125;;
     <span class="hljs-keyword">if</span>(pool[i].y < <span class="hljs-number">5</span> ||  HEIGHT - pool[i].y < <span class="hljs-number">5</span>)&#123;
      pool[i].v.y *= -<span class="hljs-number">1</span>;
    &#125;;
    pool[i].x += pool[i].v.x;
    pool[i].y += pool[i].v.y;

   
    <span class="hljs-comment">//增长动画</span>
    <span class="hljs-keyword">if</span>(pool[i].toSize)&#123;
      <span class="hljs-keyword">if</span>( pool[i].growingSize == pool[i].toSize)&#123;
         pool[i].growingSize = pool[i].toSize;
      &#125;<span class="hljs-keyword">else</span>&#123;
         pool[i].growingSize+=<span class="hljs-number">1</span>;
      &#125;
      ctx.drawImage(img, pool[i].x, pool[i].y, pool[i].growingSize, pool[i].growingSize);
    &#125;<span class="hljs-keyword">else</span>&#123;
      ctx.drawImage(img, pool[i].x, pool[i].y, spriteSize, spriteSize);
    &#125;
    <span class="hljs-comment">//显示会话</span>
    <span class="hljs-keyword">if</span>(pool[i].showDialogue)&#123;
      ctx.save();
      ctx.font = <span class="hljs-string">'14px Verdana'</span>;
      ctx.fillText(pool[i].dialogue,  pool[i].x,  pool[i].y);
      ctx.restore();
      <span class="hljs-comment">//dialogueTime时间后，对话消失</span>
      pool[i].dialogueTime<=<span class="hljs-number">0</span> ? pool[i].showDialogue = <span class="hljs-literal">false</span>  :  pool[i].dialogueTime-= deltaTime;
    &#125;
    
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">7关卡入场动画</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//开场拉开帷幕动画</span>
<span class="hljs-keyword">var</span> Curtain = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">this</span>.width = WIDTH;
  <span class="hljs-built_in">this</span>.height = HEIGHT;
  <span class="hljs-built_in">this</span>.alpha = <span class="hljs-number">1</span>;
&#125;
Curtain.prototype.play = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;

  <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.width><span class="hljs-number">0</span> || <span class="hljs-built_in">this</span>.alpha > <span class="hljs-number">0</span>)&#123;
    <span class="hljs-built_in">this</span>.width < <span class="hljs-number">0</span> ? <span class="hljs-number">0</span> : <span class="hljs-built_in">this</span>.width -=<span class="hljs-number">15</span>; 
    <span class="hljs-built_in">this</span>.alpha < <span class="hljs-number">0.1</span> ? <span class="hljs-number">0</span> : <span class="hljs-built_in">this</span>.alpha -=<span class="hljs-number">0.002</span>; 
    ctx.save();
    ctx.fillStyle = <span class="hljs-string">'rgba(0,0,0,'</span>+ <span class="hljs-built_in">this</span>.alpha+<span class="hljs-string">')'</span>;
    ctx.fillRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">this</span>.width, <span class="hljs-built_in">this</span>.height);
    ctx.restore();
  &#125;
 
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loop</span>(<span class="hljs-params"></span>)</span>&#123;
curtain = <span class="hljs-keyword">new</span> Curtain();
curtain.play();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>8游戏数据的维护和绘制 同理</p>
<h2 data-id="heading-8">END</h2>
<blockquote>
<p>2d游戏比较简单，一般掌握一定的方法就可以举一反三</p>
</blockquote></div>  
</div>
            