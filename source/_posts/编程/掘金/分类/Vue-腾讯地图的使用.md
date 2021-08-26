
---
title: 'Vue-腾讯地图的使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d388a99d8d44183bc9c89aac2a09ba8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 18:05:58 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d388a99d8d44183bc9c89aac2a09ba8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<blockquote>
<p>最近项目中遇到了需要在地图上规划线路，修改线路，查看线路，标注点，修改点，查看点的需求，认真研究了<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.qq.com%2FwebApi%2FjavascriptGL%2FglGuide%2FglOverview" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.qq.com/webApi/javascriptGL/glGuide/glOverview" ref="nofollow noopener noreferrer">腾讯地图官网</a>之后，有了一点心得，总结一下，（本文只说实战经验，具体的文档属性，官网很清楚的），温故而知新！</p>
</blockquote>
<p>要实现如下的地图，包括了：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d388a99d8d44183bc9c89aac2a09ba8~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">一.绘制线</h1>
<h2 data-id="heading-1">1.绘制线路，拖动线路可编辑，双击可删除节点</h2>
<ul>
<li>html部分</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mapContainer"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>公里：&#123;&#123;distanceDraw&#125;&#125;公里<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"delPolygon"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"!disabled"</span>></span>重新绘制<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"mapItem"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mapBox"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;
            width: mapStyle.width,
            height: mapStyle.height,
         &#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>js部分，定义变量</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">paths</span>: [],<span class="hljs-comment">// 线路节点</span>
        <span class="hljs-attr">longitude</span>: <span class="hljs-string">'118.90581786632538'</span>,<span class="hljs-comment">// 经度</span>
        <span class="hljs-attr">latitude</span>: <span class="hljs-string">'31.912693393211505'</span>,<span class="hljs-comment">// 纬度</span>
        <span class="hljs-attr">lngLatData</span>: [], <span class="hljs-comment">// 绘制多边形坐标点</span>
        <span class="hljs-attr">distanceDraw</span>: <span class="hljs-number">0</span>,<span class="hljs-comment">// 绘制距离</span>
        <span class="hljs-attr">lines</span>: <span class="hljs-string">''</span>,
    &#125;;
&#125;,
<span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">latLng</span>: <span class="hljs-built_in">Array</span>,
    <span class="hljs-attr">distance</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
        <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>
    &#125;,
    <span class="hljs-attr">center</span>: <span class="hljs-built_in">Array</span>,
    <span class="hljs-attr">zoom</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
        <span class="hljs-attr">default</span>: <span class="hljs-number">13</span>,
    &#125;,
    <span class="hljs-attr">mapStyle</span>:&#123;
        <span class="hljs-attr">type</span>:<span class="hljs-built_in">Object</span>,
        <span class="hljs-function"><span class="hljs-title">default</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span>&#123;
                <span class="hljs-attr">width</span>: <span class="hljs-string">'100%'</span>,
                <span class="hljs-attr">height</span>: <span class="hljs-string">'550px'</span>,
            &#125;
        &#125;
    &#125;,
    <span class="hljs-attr">disabled</span>: <span class="hljs-built_in">Boolean</span>,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>引入所需js ，按需引入需要的js（key需要自己去申请一个）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">loadMap</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
        <span class="hljs-keyword">let</span> script = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"script"</span>);
        script.type = <span class="hljs-string">"text/javascript"</span>;
        script.src = <span class="hljs-string">"https://map.qq.com/api/gljs?libraries=geometry&v=2.exp&key="</span>+ baseMapKey;
        script.onerror = reject;
        <span class="hljs-built_in">document</span>.head.appendChild(script);
        <span class="hljs-keyword">let</span> script2 = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"script"</span>);
        script2.type = <span class="hljs-string">"text/javascript"</span>;
        script2.src = <span class="hljs-string">"https://map.qq.com/api/js?v=2.exp&libraries=drawing&key="</span>+ baseMapKey;
        script2.onerror = reject;
        <span class="hljs-built_in">document</span>.head.appendChild(script2);
        resolve();
    &#125;);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>地图初始化</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.center && <span class="hljs-built_in">this</span>.center.length > <span class="hljs-number">0</span>) &#123;
        <span class="hljs-built_in">this</span>.latitude = <span class="hljs-built_in">this</span>.center[<span class="hljs-number">0</span>];
        <span class="hljs-built_in">this</span>.longitude = <span class="hljs-built_in">this</span>.center[<span class="hljs-number">1</span>];
    &#125;
    <span class="hljs-built_in">this</span>.distanceDraw = <span class="hljs-built_in">this</span>.distance || <span class="hljs-number">0</span>;
    zoomLevel = <span class="hljs-built_in">this</span>.zoom || <span class="hljs-number">13</span>;
    <span class="hljs-comment">// 地图初始化</span>
    map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.qq.maps.Map(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'mapItem'</span>), &#123;
        <span class="hljs-attr">center</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.qq.maps.LatLng(<span class="hljs-built_in">this</span>.latitude,<span class="hljs-built_in">this</span>.longitude),
        <span class="hljs-attr">zoom</span>: <span class="hljs-built_in">this</span>.zoom, <span class="hljs-comment">// 设置地图缩放级别</span>
        <span class="hljs-attr">scrollwheel</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">scaleControl</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">//启用比例尺</span>
        <span class="hljs-attr">scaleControlOptions</span>: &#123;
            <span class="hljs-comment">//设置控件位置相对右下角对齐，向左排列</span>
            <span class="hljs-attr">position</span>: <span class="hljs-built_in">window</span>.qq.maps.ControlPosition.BOTTOM_RIGHT
        &#125;,
        <span class="hljs-attr">zoomControl</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">//设置缩放控件的位置和样式</span>
        <span class="hljs-attr">zoomControlOptions</span>: &#123;
            <span class="hljs-comment">//设置缩放控件的位置为相对左方中间位置对齐.</span>
            <span class="hljs-attr">position</span>: <span class="hljs-built_in">window</span>.qq.maps.ControlPosition.TOP_LEFT,
            <span class="hljs-comment">//设置缩放控件样式为仅包含放大缩小两个按钮</span>
            <span class="hljs-attr">style</span>: <span class="hljs-built_in">window</span>.qq.maps.ZoomControlStyle.LARGE
        &#125;,
        <span class="hljs-attr">panControl</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">// 平移控件</span>
        <span class="hljs-attr">mapTypeControl</span>: <span class="hljs-literal">false</span>,<span class="hljs-comment">// 默认是地图和卫星</span>
    &#125;);
    <span class="hljs-keyword">let</span> that = <span class="hljs-built_in">this</span>;
    <span class="hljs-built_in">window</span>.qq.maps.event.addListener(map,<span class="hljs-string">'zoom_changed'</span>,<span class="hljs-function">()=></span> &#123;
        zoomLevel = map.getZoom();
        that.$emit(<span class="hljs-string">'saveLatLng'</span>, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, zoomLevel);
    &#125;);

    <span class="hljs-comment">// 回显线路</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.latLng && <span class="hljs-built_in">this</span>.latLng.length > <span class="hljs-number">0</span>)&#123;
        <span class="hljs-keyword">let</span> path = [];
        <span class="hljs-built_in">this</span>.latLng.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
            path.push(<span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.qq.maps.LatLng(item.lat,item.lng));
        &#125;);
        <span class="hljs-built_in">this</span>.getLine(path);
    &#125;<span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 绘图工具</span>
        <span class="hljs-built_in">this</span>.getDrawMan();
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>获取绘图工具，设置绘图属性</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">getDrawMan</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 绘图工具</span>
    drawingManager = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.qq.maps.drawing.DrawingManager(&#123;
        <span class="hljs-attr">drawingMode</span>: <span class="hljs-built_in">window</span>.qq.maps.drawing.OverlayType.POLYLINE,
        <span class="hljs-comment">// 是否启用DrawingManager地图控件，默认为false</span>
        <span class="hljs-comment">// drawingControl: true,</span>
        <span class="hljs-comment">// 设置DrawingManager地图控件的参数</span>
        <span class="hljs-attr">drawingControlOptions</span>: &#123;
            <span class="hljs-attr">position</span>: <span class="hljs-built_in">window</span>.qq.maps.ControlPosition.TOP_CENTER,
            <span class="hljs-attr">drawingModes</span>: [
                <span class="hljs-built_in">window</span>.qq.maps.drawing.OverlayType.POLYLINE,
            ]
        &#125;,
        <span class="hljs-comment">// 绘制polyline的属性</span>
        <span class="hljs-attr">polylineOptions</span>: &#123;
            <span class="hljs-attr">strokeLinecap</span>: <span class="hljs-string">'square'</span>,<span class="hljs-comment">// 折线末端线帽的样式，圆形为round（默认），方形为square，平直为butt。</span>
            <span class="hljs-attr">strokeColor</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.qq.maps.Color(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">1</span>),
            <span class="hljs-attr">strokeWeight</span>: <span class="hljs-number">5</span>,
            <span class="hljs-attr">strokeDashStyle</span>: <span class="hljs-string">'solid'</span>,<span class="hljs-comment">// 折线的形状。实线是solid，虚线是dash。</span>
            <span class="hljs-attr">clickable</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">// 折线是否可点击</span>
            <span class="hljs-attr">editable</span>: <span class="hljs-literal">true</span>,
        &#125;,
        <span class="hljs-attr">snapMode</span>: <span class="hljs-literal">true</span>,
    &#125;);
    drawingManager.setMap(map);
    <span class="hljs-comment">// 绘制完成</span>
    <span class="hljs-built_in">window</span>.qq.maps.event.addListener(drawingManager, <span class="hljs-string">'polylinecomplete'</span>, <span class="hljs-function">(<span class="hljs-params">event</span>)=></span> &#123;
        <span class="hljs-built_in">this</span>.getDistance(event.getPath().elems);
        <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'saveLatLng'</span>,event.getPath().elems, <span class="hljs-built_in">this</span>.distanceDraw, zoomLevel);
        drawingManager.setDrawingMode(<span class="hljs-literal">null</span>);<span class="hljs-comment">// 清除绘制模式</span>
        <span class="hljs-built_in">this</span>.lines = event;
        polyline = <span class="hljs-literal">null</span>;
    &#125;)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>计算路径的实际距离</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">getDistance</span>(<span class="hljs-params">paths</span>)</span> &#123;
    <span class="hljs-keyword">let</span> distance = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> startPoint = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.TMap.LatLng(paths[<span class="hljs-number">0</span>].lat, paths[<span class="hljs-number">0</span>].lng);
    <span class="hljs-keyword">let</span> endPoint = <span class="hljs-string">''</span>;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>;i < paths.length; i++)&#123;
        endPoint = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.TMap.LatLng(paths[i].lat, paths[i].lng);
        <span class="hljs-keyword">let</span> path = [startPoint, endPoint];
        distance += <span class="hljs-built_in">window</span>.TMap.geometry.computeDistance(path);
        startPoint = endPoint;
    &#125;
    <span class="hljs-built_in">this</span>.distanceDraw = (distance / <span class="hljs-number">1000</span>).toFixed(<span class="hljs-number">2</span>);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">2.重新绘制</h2>
<ul>
<li>删除初始化多边形，即重新绘制</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">delPolygon</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span>(polyline)&#123;
        polyline.setMap(<span class="hljs-literal">null</span>);
    &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-built_in">this</span>.lines.setMap(<span class="hljs-literal">null</span>);
    &#125;
    <span class="hljs-built_in">this</span>.getDrawMan();
    <span class="hljs-built_in">this</span>.distanceDraw = <span class="hljs-number">0</span>;
    <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'saveLatLng'</span>,[], <span class="hljs-string">'0'</span>, zoomLevel);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">3.编辑回显线路，修改线路</h2>
<ul>
<li>绘制线路，新增，修改，删除节点</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">getLine</span>(<span class="hljs-params">path</span>)</span>&#123;
    polyline = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.qq.maps.Polyline(&#123;
        <span class="hljs-attr">path</span>: path,<span class="hljs-comment">// 折线的路径，以经纬度坐标数组构成</span>
        <span class="hljs-attr">strokeColor</span>: <span class="hljs-string">'#000'</span>,
        <span class="hljs-attr">strokeWeight</span>: <span class="hljs-number">5</span>,
        <span class="hljs-attr">map</span>: map,<span class="hljs-comment">// 要显示折线的地图</span>
        <span class="hljs-attr">clickable</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">// 折线是否可点击</span>
        <span class="hljs-attr">editable</span>: !<span class="hljs-built_in">this</span>.disabled,<span class="hljs-comment">// 启动编辑功能后，可拖动端点对折线进行调整，双击节点可删除</span>
        <span class="hljs-attr">zIndex</span>: <span class="hljs-number">1000</span>,
    &#125;);
    <span class="hljs-keyword">let</span> _this = <span class="hljs-built_in">this</span>;
    <span class="hljs-comment">// 新增节点</span>
    <span class="hljs-built_in">window</span>.qq.maps.event.addListener(polyline,<span class="hljs-string">"insertNode"</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
        _this.getDistance(event.path.elems);
        _this.$emit(<span class="hljs-string">'saveLatLng'</span>,event.path.elems, <span class="hljs-built_in">this</span>.distanceDraw, zoomLevel);
    &#125;);
    <span class="hljs-comment">// 移动节点</span>
    <span class="hljs-built_in">window</span>.qq.maps.event.addListener(polyline,<span class="hljs-string">"adjustNode"</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
        _this.getDistance(event.path.elems);
        _this.$emit(<span class="hljs-string">'saveLatLng'</span>,event.path.elems, <span class="hljs-built_in">this</span>.distanceDraw, zoomLevel);
    &#125;);
    <span class="hljs-comment">// 删除节点</span>
    <span class="hljs-built_in">window</span>.qq.maps.event.addListener(polyline,<span class="hljs-string">"removeNode"</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
        _this.getDistance(event.path.elems);
        _this.$emit(<span class="hljs-string">'saveLatLng'</span>,event.path.elems, <span class="hljs-built_in">this</span>.distanceDraw, zoomLevel);
    &#125;);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">二.绘制点</h1>
<p><strong>其中html，js属性，引入js如上线的，下面说一下不一样的地方</strong></p>
<h2 data-id="heading-5">1.绘制点</h2>
<ul>
<li>地图初始化</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params"></span>)</span> &#123;
    map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.qq.maps.Map(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'mapItem'</span>), &#123;
        <span class="hljs-attr">center</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.qq.maps.LatLng(<span class="hljs-built_in">this</span>.latitude,<span class="hljs-built_in">this</span>.longitude),
        <span class="hljs-attr">zoom</span>: <span class="hljs-number">13</span>, <span class="hljs-comment">// 设置地图缩放级别</span>
        <span class="hljs-attr">scaleControl</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">//启用比例尺</span>
        <span class="hljs-attr">scaleControlOptions</span>: &#123;
            <span class="hljs-comment">// 设置控件位置相对右下角对齐，向左排列</span>
            <span class="hljs-attr">position</span>: <span class="hljs-built_in">window</span>.qq.maps.ControlPosition.BOTTOM_RIGHT
        &#125;,
        <span class="hljs-attr">scrollwheel</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">zoomControl</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 设置缩放控件的位置和样式</span>
        <span class="hljs-attr">zoomControlOptions</span>: &#123;
            <span class="hljs-comment">// 设置缩放控件的位置为相对左方中间位置对齐.</span>
            <span class="hljs-attr">position</span>: <span class="hljs-built_in">window</span>.qq.maps.ControlPosition.TOP_LEFT,
            <span class="hljs-comment">// 设置缩放控件样式为仅包含放大缩小两个按钮</span>
            <span class="hljs-attr">style</span>: <span class="hljs-built_in">window</span>.qq.maps.ZoomControlStyle.LARGE
        &#125;,
        <span class="hljs-attr">panControl</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">// 平移控件</span>
        <span class="hljs-attr">mapTypeControl</span>: <span class="hljs-literal">false</span>,<span class="hljs-comment">// 默认是地图和卫星</span>
    &#125;);
    <span class="hljs-built_in">window</span>.qq.maps.event.addListener(map,<span class="hljs-string">'zoom_changed'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        zoomLevel = map.getZoom();
    &#125;);
    <span class="hljs-comment">// 添加dom监听事件</span>
    <span class="hljs-built_in">window</span>.qq.maps.event.addListener(map, <span class="hljs-string">'click'</span>, <span class="hljs-function">(<span class="hljs-params">event</span>)=></span> &#123;
        <span class="hljs-keyword">if</span>(!marker)&#123;
            <span class="hljs-built_in">this</span>.addMarker(event.latLng, <span class="hljs-number">1</span>);
        &#125;
        marker.setPosition(event.latLng);
        <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'saveLatLng'</span>,event.latLng, zoomLevel);
    &#125;);
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.latLng.latitude !== <span class="hljs-string">''</span> && <span class="hljs-built_in">this</span>.latLng.latitude !== <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">let</span> location = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.qq.maps.LatLng(<span class="hljs-built_in">this</span>.latLng.latitude,<span class="hljs-built_in">this</span>.latLng.longitude);
        <span class="hljs-built_in">this</span>.addMarker(location);
        marker.setPosition(location);
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">2.重新绘制</h2>
<ul>
<li>删除标记</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 删除标记</span>
<span class="hljs-function"><span class="hljs-title">deleteOverlays</span>(<span class="hljs-params">flag</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (markerArray) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">in</span> markerArray) &#123;
            markerArray[i].setMap(<span class="hljs-literal">null</span>);
        &#125;
        marker = <span class="hljs-literal">null</span>;
        markerArray.length = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">if</span>(flag == <span class="hljs-number">1</span>)&#123;
            <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'saveLatLng'</span>,<span class="hljs-literal">null</span>, zoomLevel);
        &#125;
    &#125;<span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">this</span>.$message(&#123;
            <span class="hljs-attr">message</span>: <span class="hljs-string">'删除失败，请先标记一个位置'</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'error'</span>,
        &#125;);
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">3.编辑回显点，修改点</h2>
<ul>
<li>添加标记</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 添加标记</span>
<span class="hljs-function"><span class="hljs-title">addMarker</span>(<span class="hljs-params">location</span>)</span> &#123;
    marker = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.qq.maps.Marker(&#123;
        <span class="hljs-attr">icon</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.qq.maps.MarkerImage(
        <span class="hljs-built_in">require</span>(<span class="hljs-string">'@/assets/images/marker_blue.png'</span>),<span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.qq.maps.Size(<span class="hljs-number">50</span>, <span class="hljs-number">50</span>)),
        <span class="hljs-attr">position</span>: location,
        <span class="hljs-attr">map</span>: map
    &#125;);
    markerArray = [marker];
&#125;,

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>文章最后，送给大家一颗小心心！</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1144d490daa34973a43a86cd0ee36d9b~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>如上就是在项目中使用腾讯地图的全部代码了，谢谢观看！</p>
</blockquote></div>  
</div>
            