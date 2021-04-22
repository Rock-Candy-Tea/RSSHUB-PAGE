
---
title: 'canvas旋转跟随鼠标线条 html+css+js'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6cdd18609184dd0a621bf6b2991c56c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Apr 2021 02:37:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6cdd18609184dd0a621bf6b2991c56c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">先看效果（完整代码在底部）：</h2>
<p><img alt="888.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6cdd18609184dd0a621bf6b2991c56c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">实现过程（可一步一步实现）：</h2>
<p><strong>1.定义标签与基本css样式：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvas"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">canvas</span>&#123;
          <span class="hljs-attribute">display</span>: block;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2. 开始正式js部分，先获取画布：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-keyword">var</span> canvas = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#canvas"</span>);
 <span class="hljs-keyword">var</span> ctx = canvas.getContext(<span class="hljs-string">"2d"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3.定义基本变量：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">       <span class="hljs-comment">// 画布宽与高</span>
        <span class="hljs-keyword">var</span> kuan=<span class="hljs-number">0</span>,gao=<span class="hljs-number">0</span>;
       <span class="hljs-comment">// 线条数量    </span>
        <span class="hljs-keyword">var</span> num=<span class="hljs-number">25</span>;
        <span class="hljs-comment">//数组，存储每条线的基本信息</span>
        <span class="hljs-keyword">var</span> arr=[];
        <span class="hljs-comment">// 存几个喜欢的颜色后面给线条</span>
        <span class="hljs-keyword">var</span> colors = [<span class="hljs-string">"#2196F3"</span>,<span class="hljs-string">"#1976D2"</span>,<span class="hljs-string">"#00BCD4"</span>,<span class="hljs-string">"#4CAF50"</span>,<span class="hljs-string">"#FF5252"</span>,<span class="hljs-string">"#E040FB"</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4. 使得画布动态与窗口一样大小，直接copy该方法就行，顺便定义初始鼠标位置变量为画布的中间位置：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-built_in">window</span>.onresize=resizeCanvas;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resizeCanvas</span>(<span class="hljs-params"></span>)</span>&#123;
            kuan=canvas.width=<span class="hljs-built_in">window</span>.innerWidth;
            gao=canvas.height=<span class="hljs-built_in">window</span>.innerHeight;
        &#125;
        resizeCanvas(); 

  <span class="hljs-keyword">var</span> mouseX = kuan/<span class="hljs-number">2</span>,mouseY = gao/<span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>5. 初始化数组，初始化每条线条的基本信息：</strong></p>
<p>注：Math.random()*(max-min) + min 为随机获取min到max间的一个数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<num;i++)&#123;
            arr.push(&#123;
              <span class="hljs-comment">// 线条的宽度</span>
                <span class="hljs-attr">r</span>: <span class="hljs-built_in">Math</span>.random()*(<span class="hljs-number">5</span>-<span class="hljs-number">3</span>) + <span class="hljs-number">3</span>,
              <span class="hljs-comment">// 线条的颜色  </span>
                <span class="hljs-attr">color</span>: colors[<span class="hljs-built_in">parseInt</span>(<span class="hljs-built_in">Math</span>.random()*<span class="hljs-number">6</span>)],
                 <span class="hljs-comment">/* 线条最初始小点所在旋转圆上的位置，就是在旋转开始的角度 */</span>
                <span class="hljs-attr">rot</span>: <span class="hljs-built_in">Math</span>.random()*<span class="hljs-number">2</span>*<span class="hljs-built_in">Math</span>.PI,
                <span class="hljs-comment">/* 线条与旋转圆中心的距离 */</span>
                <span class="hljs-attr">distance</span>: <span class="hljs-built_in">Math</span>.random() * (<span class="hljs-number">75</span> - <span class="hljs-number">40</span>) + <span class="hljs-number">40</span>,
                <span class="hljs-comment">/* 记录初始位置，后面鼠标拖拽时做缓动动画用 */</span>
                <span class="hljs-attr">lastMouse</span>:&#123;
                    <span class="hljs-attr">x</span>:kuan/<span class="hljs-number">2</span>,
                    <span class="hljs-attr">y</span>:gao/<span class="hljs-number">2</span>
                &#125;
            &#125;)
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.绑定鼠标移动事件：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'mousemove'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
               mouseX = event.clientX;
               mouseY = event.clientY;               
         &#125;)   
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>7.执行更新操作，在更新里调用绘制：</strong></p>
<p>注意：在一个圆上，坐标 x=cos（..）× r，y = sin（..）× r 。
cos（.）与sin（.）取值范围为【-1,1】。细品。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span> (<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<num;i++)&#123;
                <span class="hljs-comment">//先保存上一帧的位置与i值</span>
               <span class="hljs-keyword">let</span> last =&#123;<span class="hljs-attr">x</span>:arr[i].x,<span class="hljs-attr">y</span>:arr[i].y,<span class="hljs-attr">i</span>:i&#125;;             
            <span class="hljs-comment">// 移动后位置 = 当前位置 + （移动后位置-当前位置）*0.05 缓动动画原理 </span>
                arr[i].lastMouse.x+=(mouseX-arr[i].lastMouse.x)*<span class="hljs-number">0.05</span>;
                arr[i].lastMouse.y+=(mouseY-arr[i].lastMouse.y)*<span class="hljs-number">0.05</span>;
             <span class="hljs-comment">// 角度改变，就是进行旋转</span>
               arr[i].rot+=<span class="hljs-number">0.1</span>;
               <span class="hljs-comment">// 坐标X改变</span>
                arr[i].x = arr[i].lastMouse.x + <span class="hljs-built_in">Math</span>.cos(arr[i].rot)*arr[i].distance;
                <span class="hljs-comment">// 坐标y改变</span>
                arr[i].y = arr[i].lastMouse.y + <span class="hljs-built_in">Math</span>.sin(arr[i].rot)*arr[i].distance;
                 <span class="hljs-comment">/* 位置改变了，把last传给draw，得到不同两点后绘制画线 */</span>
                draw(last);
            &#125;
         &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>8. 绘制：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">draw</span>(<span class="hljs-params">last</span>) </span>&#123;
            <span class="hljs-keyword">var</span> yuan = arr[last.i]; 
            <span class="hljs-comment">// 开始绘制</span>
            ctx.beginPath();
            <span class="hljs-comment">//颜色</span>
            ctx.strokeStyle = yuan.color;
            <span class="hljs-comment">// 宽度</span>
            ctx.lineWidth = yuan.r;
            ctx.moveTo(last.x,last.y);
            ctx.lineTo(yuan.x,yuan.y);
            ctx.stroke();
            ctx.closePath();
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>9. 设置定时器，同时实现线条尾部慢慢消失效果：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
             <span class="hljs-comment">/*  ctx.clearRect(0,0,kuan,gao); */</span>
             <span class="hljs-comment">/* 不直接用clearRect让上一帧内容全部变透明，而是逐渐给上一帧
             蒙上一层有点透明的当前背景色，这样一帧一帧的叠加，最开始的线段
             会逐渐与背景融合变得相当与消失 */</span>
             ctx.fillStyle = <span class="hljs-string">"rgba(0,0,0,0.1)"</span>; 
             ctx.fillRect(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,kuan,gao); 
             update(); 
          <span class="hljs-comment">/*  draw(); */</span> 
        &#125;,<span class="hljs-number">20</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">完整代码：</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"zh-CN"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        *&#123;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">box-sizing</span>: border-box;
        &#125;
      <span class="hljs-selector-tag">body</span>&#123;
          <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
        
      &#125;
      <span class="hljs-selector-tag">canvas</span>&#123;
          <span class="hljs-attribute">display</span>: block;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvas"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
         <span class="hljs-keyword">var</span> canvas = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#canvas"</span>);
         <span class="hljs-keyword">var</span> ctx = canvas.getContext(<span class="hljs-string">"2d"</span>);
       <span class="hljs-comment">// 画布宽与高</span>
        <span class="hljs-keyword">var</span> kuan=<span class="hljs-number">0</span>,gao=<span class="hljs-number">0</span>;    
        <span class="hljs-keyword">var</span> num=<span class="hljs-number">25</span>;
        <span class="hljs-keyword">var</span> arr=[];
        <span class="hljs-keyword">var</span> colors = [<span class="hljs-string">"#2196F3"</span>,<span class="hljs-string">"#1976D2"</span>,<span class="hljs-string">"#00BCD4"</span>,<span class="hljs-string">"#4CAF50"</span>,<span class="hljs-string">"#FF5252"</span>,<span class="hljs-string">"#E040FB"</span>];
        <span class="hljs-built_in">window</span>.onresize=resizeCanvas;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resizeCanvas</span>(<span class="hljs-params"></span>)</span>&#123;
            kuan=canvas.width=<span class="hljs-built_in">window</span>.innerWidth;
            gao=canvas.height=<span class="hljs-built_in">window</span>.innerHeight;
        &#125;
        resizeCanvas(); 
        <span class="hljs-keyword">var</span> mouseX = kuan/<span class="hljs-number">2</span>,mouseY = gao/<span class="hljs-number">2</span>;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<num;i++)&#123;
            arr.push(&#123;
               <span class="hljs-comment">/*  x: kuan/2,
                y: gao/2, */</span>
                <span class="hljs-attr">r</span>: <span class="hljs-built_in">Math</span>.random()*(<span class="hljs-number">5</span>-<span class="hljs-number">3</span>) + <span class="hljs-number">3</span>,
                <span class="hljs-attr">color</span>: colors[<span class="hljs-built_in">parseInt</span>(<span class="hljs-built_in">Math</span>.random()*<span class="hljs-number">6</span>)],
                 <span class="hljs-comment">/* 旋转开始角度 */</span>
                <span class="hljs-attr">rot</span>: <span class="hljs-built_in">Math</span>.random()*<span class="hljs-number">2</span>*<span class="hljs-built_in">Math</span>.PI,
                <span class="hljs-comment">/* 旋转小球距离中心距离 */</span>
                <span class="hljs-attr">distance</span>: <span class="hljs-built_in">Math</span>.random() * (<span class="hljs-number">75</span> - <span class="hljs-number">40</span>) + <span class="hljs-number">40</span>,
                <span class="hljs-comment">/* 记录初始位置，鼠标拖拽时做缓动动画用 */</span>
                <span class="hljs-attr">lastMouse</span>:&#123;
                    <span class="hljs-attr">x</span>:kuan/<span class="hljs-number">2</span>,
                    <span class="hljs-attr">y</span>:gao/<span class="hljs-number">2</span>
                &#125;
            &#125;)
        &#125;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">draw</span>(<span class="hljs-params">last</span>) </span>&#123;
           <span class="hljs-comment">/*  for(let i=0;i<num;i++)&#123; */</span> 
            <span class="hljs-keyword">var</span> yuan = arr[last.i]; 
            ctx.beginPath();
            <span class="hljs-comment">/* ctx.fillStyle = yuan.color; 
            ctx.arc(yuan.x,yuan.y,yuan.r, 0,Math.PI* 2, false);
            ctx.fill(); */</span>
            ctx.strokeStyle = yuan.color;
            ctx.lineWidth = yuan.r;
            ctx.moveTo(last.x,last.y);
            ctx.lineTo(yuan.x,yuan.y);
            ctx.stroke();
            ctx.closePath();
           <span class="hljs-comment">/*  &#125; */</span> 
        &#125;
          
         <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'mousemove'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
               mouseX = event.clientX;
               mouseY = event.clientY;               
         &#125;)       
        <span class="hljs-comment">/*  var moveX=kuan/2,moveY=gao/2; */</span>
         <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span> (<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<num;i++)&#123;
                <span class="hljs-comment">/* 传当前绘制的第i个的线的绘制前一帧的位置和当前i保存 */</span>
               <span class="hljs-keyword">let</span> last =&#123;<span class="hljs-attr">x</span>:arr[i].x,<span class="hljs-attr">y</span>:arr[i].y,<span class="hljs-attr">i</span>:i&#125;;             
            <span class="hljs-comment">/* 移动后位置 = 当前位置 + （移动后位置-当前位置）*0.05 缓动动画原理 */</span>
                arr[i].lastMouse.x+=(mouseX-arr[i].lastMouse.x)*<span class="hljs-number">0.05</span>;
                arr[i].lastMouse.y+=(mouseY-arr[i].lastMouse.y)*<span class="hljs-number">0.05</span>;
               arr[i].rot+=<span class="hljs-number">0.1</span>;
                arr[i].x = arr[i].lastMouse.x + <span class="hljs-built_in">Math</span>.cos(arr[i].rot)*arr[i].distance;
                arr[i].y = arr[i].lastMouse.y + <span class="hljs-built_in">Math</span>.sin(arr[i].rot)*arr[i].distance;
                 <span class="hljs-comment">/* 位置改变，把last传给draw，画线 */</span>
                draw(last);
            &#125;
         &#125;
        <span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
             <span class="hljs-comment">/*  ctx.clearRect(0,0,kuan,gao); */</span>
             <span class="hljs-comment">/* 不直接用clearRect让上一帧内容全部变透明，而是逐渐给上一帧
             蒙上一层有点透明的当前背景色，这样一帧一帧的叠加，最开始的小球
             会逐渐与背景融合变得相当与消失 */</span>
             ctx.fillStyle = <span class="hljs-string">"rgba(0,0,0,0.1)"</span>; 
             ctx.fillRect(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,kuan,gao); 
             update(); 
          <span class="hljs-comment">/*  draw(); */</span> 
        &#125;,<span class="hljs-number">20</span>)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">总结：</h2>
<p><img alt="Snipaste_2021-04-22_18-13-51.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/857d7b32f921430f955e40e147f2b479~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            