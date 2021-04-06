
---
title: 'JS实现鼠标点击爱心&绘制多边形&每日一言功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da17b3c0f8374b11bf92938a7cb32031~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 01:44:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da17b3c0f8374b11bf92938a7cb32031~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本篇文章主要介绍我的个人博客 <a href="https://liujian.cool/" target="_blank" rel="nofollow noopener noreferrer">程序猿刘川枫</a> 中页面使用的美化功能（基于JS实现）：</p>
<p>1.鼠标点击出现不同颜色爱心特效</p>
<p>2.页面浮动多边形跟随鼠标移动</p>
<p>3.每日一言功能</p>
</blockquote>
<h2 data-id="heading-0">1.鼠标点击出现爱心特效</h2>
<p>经常在博客园或者其他个人网站中看到点击鼠标能出现不同颜色的爱心，以及烟花特效，富强民主字体等等，觉得很有意思，便研究了一下，具体如下：</p>
<h3 data-id="heading-1">效果图预览</h3>
<p><img alt="image-20210406163010836" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da17b3c0f8374b11bf92938a7cb32031~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image-20210406164104525" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5015800b668b4f329c0c414283c79d5a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">JS代码实现</h3>
<p>鼠标点击出现不同颜色爱心：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//鼠标点击爱心</span>
!<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e, t, a</span>) </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">r</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> e = <span class="hljs-number">0</span>; e < s.length; e++) s[e].alpha <= <span class="hljs-number">0</span> ? (t.body.removeChild(s[e].el), s.splice(e, <span class="hljs-number">1</span>)) : (s[e].y--, s[e].scale += <span class="hljs-number">.004</span>, s[e].alpha -= <span class="hljs-number">.013</span>, s[e].el.style.cssText = <span class="hljs-string">"left:"</span> + s[e].x + <span class="hljs-string">"px;top:"</span> + s[e].y + <span class="hljs-string">"px;opacity:"</span> + s[e].alpha + <span class="hljs-string">";transform:scale("</span> + s[e].scale + <span class="hljs-string">","</span> + s[e].scale + <span class="hljs-string">") rotate(45deg);background:"</span> + s[e].color + <span class="hljs-string">";z-index:99999"</span>);
        requestAnimationFrame(r)
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">n</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">var</span> t = <span class="hljs-string">"function"</span> == <span class="hljs-keyword">typeof</span> e.onclick && e.onclick;
        e.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
            t && t(),
                o(e)
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">o</span>(<span class="hljs-params">e</span>) </span>&#123;
        <span class="hljs-keyword">var</span> a = t.createElement(<span class="hljs-string">"div"</span>);
        a.className = <span class="hljs-string">"heart"</span>,
            s.push(&#123;
                <span class="hljs-attr">el</span>: a,
                <span class="hljs-attr">x</span>: e.clientX - <span class="hljs-number">5</span>,
                <span class="hljs-attr">y</span>: e.clientY - <span class="hljs-number">5</span>,
                <span class="hljs-attr">scale</span>: <span class="hljs-number">1</span>,
                <span class="hljs-attr">alpha</span>: <span class="hljs-number">1</span>,
                <span class="hljs-attr">color</span>: c()
            &#125;),
            t.body.appendChild(a)
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">i</span>(<span class="hljs-params">e</span>) </span>&#123;
        <span class="hljs-keyword">var</span> a = t.createElement(<span class="hljs-string">"style"</span>);
        a.type = <span class="hljs-string">"text/css"</span>;
        <span class="hljs-keyword">try</span> &#123;
            a.appendChild(t.createTextNode(e))
        &#125; <span class="hljs-keyword">catch</span>(t) &#123;
            a.styleSheet.cssText = e
        &#125;
        t.getElementsByTagName(<span class="hljs-string">"head"</span>)[<span class="hljs-number">0</span>].appendChild(a)
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">c</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"rgb("</span> + ~~ (<span class="hljs-number">255</span> * <span class="hljs-built_in">Math</span>.random()) + <span class="hljs-string">","</span> + ~~ (<span class="hljs-number">255</span> * <span class="hljs-built_in">Math</span>.random()) + <span class="hljs-string">","</span> + ~~ (<span class="hljs-number">255</span> * <span class="hljs-built_in">Math</span>.random()) + <span class="hljs-string">")"</span>
    &#125;
    <span class="hljs-keyword">var</span> s = [];
    e.requestAnimationFrame = e.requestAnimationFrame || e.webkitRequestAnimationFrame || e.mozRequestAnimationFrame || e.oRequestAnimationFrame || e.msRequestAnimationFrame ||
        <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
            <span class="hljs-built_in">setTimeout</span>(e, <span class="hljs-number">1e3</span> / <span class="hljs-number">60</span>)
        &#125;,
        i(<span class="hljs-string">".heart&#123;width: 10px;height: 10px;position: fixed;background: #f00;transform: rotate(45deg);-webkit-transform: rotate(45deg);-moz-transform: rotate(45deg);&#125;.heart:after,.heart:before&#123;content: '';width: inherit;height: inherit;background: inherit;border-radius: 50%;-webkit-border-radius: 50%;-moz-border-radius: 50%;position: fixed;&#125;.heart:after&#123;top: -5px;&#125;.heart:before&#123;left: -5px;&#125;"</span>),
        n(),
        r()
&#125; (<span class="hljs-built_in">window</span>, <span class="hljs-built_in">document</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>鼠标点击特效"富强民主"字体：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> 
<script>
    <span class="hljs-comment">//定义获取词语下标</span>
<span class="hljs-keyword">var</span> a_idx = <span class="hljs-number">0</span>;
jQuery(<span class="hljs-built_in">document</span>).ready(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">$</span>) </span>&#123;
        <span class="hljs-comment">//点击body时触发事件</span>
    $(<span class="hljs-string">"body"</span>).click(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-comment">//需要显示的词语</span>
    <span class="hljs-keyword">var</span> a = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-string">"富强"</span>,<span class="hljs-string">"民主"</span>, <span class="hljs-string">"文明"</span>, <span class="hljs-string">"和谐"</span>,<span class="hljs-string">"自由"</span>, <span class="hljs-string">"平等"</span>, <span class="hljs-string">"公正"</span>,<span class="hljs-string">"法治"</span>, <span class="hljs-string">"爱国"</span>, <span class="hljs-string">"敬业"</span>,<span class="hljs-string">"诚信"</span>, <span class="hljs-string">"友善"</span>);
    <span class="hljs-comment">//设置词语给span标签</span>
    <span class="hljs-keyword">var</span> $i = $(<span class="hljs-string">"<span/>"</span>).text(a[a_idx]);
    <span class="hljs-comment">//下标等于原来下标+1  余 词语总数</span>
    a_idx = (a_idx + <span class="hljs-number">1</span>)% a.length;
    <span class="hljs-comment">//获取鼠标指针的位置，分别相对于文档的左和右边缘。</span>
    <span class="hljs-comment">//获取x和y的指针坐标</span>
    <span class="hljs-keyword">var</span> x = e.pageX, y = e.pageY;
    <span class="hljs-comment">//在鼠标的指针的位置给$i定义的span标签添加css样式</span>
    $i.css(&#123;<span class="hljs-string">"z-index"</span> : <span class="hljs-number">999999</span>,
        <span class="hljs-string">"top"</span> : y - <span class="hljs-number">20</span>,
        <span class="hljs-string">"left"</span> : x,
        <span class="hljs-string">"position"</span> : <span class="hljs-string">"absolute"</span>,
        <span class="hljs-string">"font-weight"</span> : <span class="hljs-string">"bold"</span>,
        <span class="hljs-string">"color"</span> : <span class="hljs-string">"#ff6651"</span>
        &#125;);
    <span class="hljs-comment">//在body添加这个标签</span>
    $(<span class="hljs-string">"body"</span>).append($i);
        <span class="hljs-comment">//animate() 方法执行 CSS 属性集的自定义动画。</span>
        <span class="hljs-comment">//该方法通过CSS样式将元素从一个状态改变为另一个状态。CSS属性值是逐渐改变的，这样就可以创建动画效果。</span>
        <span class="hljs-comment">//详情请看http://www.w3school.com.cn/jquery/effect_animate.asp</span>
        $i.animate(&#123;
        <span class="hljs-comment">//将原来的位置向上移动180</span>
            <span class="hljs-string">"top"</span> : y - <span class="hljs-number">180</span>,
                <span class="hljs-string">"opacity"</span> : <span class="hljs-number">0</span>
         <span class="hljs-comment">//1500动画的速度</span>
        &#125;, <span class="hljs-number">1500</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">//时间到了自动删除</span>
            $i.remove();
        &#125;);
    &#125;);
&#125;);
 
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">2.页面浮动多边形跟随鼠标移动</h2>
<h3 data-id="heading-4">效果预览图</h3>
<p><img alt="image-20210406165424067" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e635cd6c5a0d4086ad1c2edefeb44a4e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">JS代码实现</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//鼠标绘制多边形</span>
! <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">//封装方法，压缩之后减少文件大小</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get_attribute</span>(<span class="hljs-params">node, attr, default_value</span>) </span>&#123;
        <span class="hljs-keyword">return</span> node.getAttribute(attr) || default_value;
    &#125;
    <span class="hljs-comment">//封装方法，压缩之后减少文件大小</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get_by_tagname</span>(<span class="hljs-params">name</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.getElementsByTagName(name);
    &#125;
    <span class="hljs-comment">//获取配置参数</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get_config_option</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">var</span> scripts = get_by_tagname(<span class="hljs-string">"script"</span>),
            script_len = scripts.length,
            script = scripts[script_len - <span class="hljs-number">1</span>]; <span class="hljs-comment">//当前加载的script</span>
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">l</span>: script_len, <span class="hljs-comment">//长度，用于生成id用</span>
            <span class="hljs-attr">z</span>: get_attribute(script, <span class="hljs-string">"zIndex"</span>, -<span class="hljs-number">1</span>), <span class="hljs-comment">//z-index</span>
            <span class="hljs-attr">o</span>: get_attribute(script, <span class="hljs-string">"opacity"</span>, <span class="hljs-number">0.5</span>), <span class="hljs-comment">//opacity</span>
            <span class="hljs-attr">c</span>: get_attribute(script, <span class="hljs-string">"color"</span>, <span class="hljs-string">"0,0,0"</span>), <span class="hljs-comment">//color</span>
            <span class="hljs-attr">n</span>: get_attribute(script, <span class="hljs-string">"count"</span>, <span class="hljs-number">99</span>) <span class="hljs-comment">//count</span>
        &#125;;
    &#125;
    <span class="hljs-comment">//设置canvas的高宽</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">set_canvas_size</span>(<span class="hljs-params"></span>) </span>&#123;
        canvas_width = the_canvas.width = <span class="hljs-built_in">window</span>.innerWidth || <span class="hljs-built_in">document</span>.documentElement.clientWidth || <span class="hljs-built_in">document</span>.body.clientWidth,
            canvas_height = the_canvas.height = <span class="hljs-built_in">window</span>.innerHeight || <span class="hljs-built_in">document</span>.documentElement.clientHeight || <span class="hljs-built_in">document</span>.body.clientHeight;
    &#125;

    <span class="hljs-comment">//绘制过程</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">draw_canvas</span>(<span class="hljs-params"></span>) </span>&#123;
        context.clearRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, canvas_width, canvas_height);
        <span class="hljs-comment">//随机的线条和当前位置联合数组</span>
        <span class="hljs-keyword">var</span> e, i, d, x_dist, y_dist, dist; <span class="hljs-comment">//临时节点</span>
        <span class="hljs-comment">//遍历处理每一个点</span>
        random_points.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">r, idx</span>) </span>&#123;
            r.x += r.xa,
                r.y += r.ya, <span class="hljs-comment">//移动</span>
                r.xa *= r.x > canvas_width || r.x < <span class="hljs-number">0</span> ? -<span class="hljs-number">1</span> : <span class="hljs-number">1</span>,
                r.ya *= r.y > canvas_height || r.y < <span class="hljs-number">0</span> ? -<span class="hljs-number">1</span> : <span class="hljs-number">1</span>, <span class="hljs-comment">//碰到边界，反向反弹</span>
                context.fillRect(r.x - <span class="hljs-number">0.5</span>, r.y - <span class="hljs-number">0.5</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>); <span class="hljs-comment">//绘制一个宽高为1的点</span>
            <span class="hljs-comment">//从下一个点开始</span>
            <span class="hljs-keyword">for</span> (i = idx + <span class="hljs-number">1</span>; i < all_array.length; i++) &#123;
                e = all_array[i];
                <span class="hljs-comment">// 当前点存在</span>
                <span class="hljs-keyword">if</span> (<span class="hljs-literal">null</span> !== e.x && <span class="hljs-literal">null</span> !== e.y) &#123;
                    x_dist = r.x - e.x; <span class="hljs-comment">//x轴距离 l</span>
                    y_dist = r.y - e.y; <span class="hljs-comment">//y轴距离 n</span>
                    dist = x_dist * x_dist + y_dist * y_dist; <span class="hljs-comment">//总距离, m</span>

                    dist < e.max && (e === current_point && dist >= e.max / <span class="hljs-number">2</span> && (r.x -= <span class="hljs-number">0.03</span> * x_dist, r.y -= <span class="hljs-number">0.03</span> * y_dist), <span class="hljs-comment">//靠近的时候加速</span>
                        d = (e.max - dist) / e.max,
                        context.beginPath(),
                        context.lineWidth = d / <span class="hljs-number">2</span>,
                        context.strokeStyle = <span class="hljs-string">"rgba("</span> + config.c + <span class="hljs-string">","</span> + (d + <span class="hljs-number">0.2</span>) + <span class="hljs-string">")"</span>,
                        context.moveTo(r.x, r.y),
                        context.lineTo(e.x, e.y),
                        context.stroke());
                &#125;
            &#125;
        &#125;), frame_func(draw_canvas);
    &#125;
    <span class="hljs-comment">//创建画布，并添加到body中</span>
    <span class="hljs-keyword">var</span> the_canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"canvas"</span>), <span class="hljs-comment">//画布</span>
        config = get_config_option(), <span class="hljs-comment">//配置</span>
        canvas_id = <span class="hljs-string">"c_n"</span> + config.l, <span class="hljs-comment">//canvas id</span>
        context = the_canvas.getContext(<span class="hljs-string">"2d"</span>), canvas_width, canvas_height,
        frame_func = <span class="hljs-built_in">window</span>.requestAnimationFrame || <span class="hljs-built_in">window</span>.webkitRequestAnimationFrame || <span class="hljs-built_in">window</span>.mozRequestAnimationFrame || <span class="hljs-built_in">window</span>.oRequestAnimationFrame || <span class="hljs-built_in">window</span>.msRequestAnimationFrame || <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">func</span>) </span>&#123;
            <span class="hljs-built_in">window</span>.setTimeout(func, <span class="hljs-number">1000</span> / <span class="hljs-number">45</span>);
        &#125;, random = <span class="hljs-built_in">Math</span>.random,
        current_point = &#123;
            <span class="hljs-attr">x</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">//当前鼠标x</span>
            <span class="hljs-attr">y</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">//当前鼠标y</span>
            <span class="hljs-attr">max</span>: <span class="hljs-number">20000</span> <span class="hljs-comment">// 圈半径的平方</span>
        &#125;,
        all_array;
    the_canvas.id = canvas_id;
    the_canvas.style.cssText = <span class="hljs-string">"position:fixed;top:0;left:0;z-index:"</span> + config.z + <span class="hljs-string">";opacity:"</span> + config.o;
    get_by_tagname(<span class="hljs-string">"body"</span>)[<span class="hljs-number">0</span>].appendChild(the_canvas);

    <span class="hljs-comment">//初始化画布大小</span>
    set_canvas_size();
    <span class="hljs-built_in">window</span>.onresize = set_canvas_size;
    <span class="hljs-comment">//当时鼠标位置存储，离开的时候，释放当前位置信息</span>
    <span class="hljs-built_in">window</span>.onmousemove = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
        e = e || <span class="hljs-built_in">window</span>.event;
        current_point.x = e.clientX;
        current_point.y = e.clientY;
    &#125;, <span class="hljs-built_in">window</span>.onmouseout = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        current_point.x = <span class="hljs-literal">null</span>;
        current_point.y = <span class="hljs-literal">null</span>;
    &#125;;
    <span class="hljs-comment">//随机生成config.n条线位置信息</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> random_points = [], i = <span class="hljs-number">0</span>; config.n > i; i++) &#123;
        <span class="hljs-keyword">var</span> x = random() * canvas_width, <span class="hljs-comment">//随机位置</span>
            y = random() * canvas_height,
            xa = <span class="hljs-number">2</span> * random() - <span class="hljs-number">1</span>, <span class="hljs-comment">//随机运动方向</span>
            ya = <span class="hljs-number">2</span> * random() - <span class="hljs-number">1</span>;
        <span class="hljs-comment">// 随机点</span>
        random_points.push(&#123;
            <span class="hljs-attr">x</span>: x,
            <span class="hljs-attr">y</span>: y,
            <span class="hljs-attr">xa</span>: xa,
            <span class="hljs-attr">ya</span>: ya,
            <span class="hljs-attr">max</span>: <span class="hljs-number">6000</span> <span class="hljs-comment">//沾附距离</span>
        &#125;);
    &#125;
    all_array = random_points.concat([current_point]);
    <span class="hljs-comment">//0.1秒后绘制</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        draw_canvas();
    &#125;, <span class="hljs-number">100</span>);
&#125;();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">3.每日一言功能</h2>
<p>主要功能为每次刷新页面都会出现不同的句子，其中的句子来自于动漫，小说，网络等等。</p>
<p>每日一言官网：<a href="https://hitokoto.cn/" target="_blank" rel="nofollow noopener noreferrer">hitokoto.cn/</a></p>
<p>网站简介：</p>
<blockquote>
<p>动漫也好、小说也好、网络也好，不论在哪里，我们总会看到有那么一两个句子能穿透你的心。我们把这些句子汇聚起来，形成一言网络，以传递更多的感动。如果可以，我们希望我们没有停止服务的那一天。</p>
<p>简单来说，一言指的就是一句话，可以是动漫中的台词，也可以是网络上的各种小段子。 或是感动，或是开心，有或是单纯的回忆。来到这里，留下你所喜欢的那一句句话，与大家分享，这就是一言存在的目的。</p>
</blockquote>
<h3 data-id="heading-7">一言效果图预览</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b7a8b1a5b3e4577b1b67efee35b54ba~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image-20210406171025777" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/310329247c834d9da5c67ca5cb1b3f46~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">代码实现</h3>
<p>JS代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//每日一言</span>
$(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
    xhr.open(<span class="hljs-string">'get'</span>, <span class="hljs-string">'https://v1.hitokoto.cn'</span>);
    xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">if</span> (xhr.readyState === <span class="hljs-number">4</span>) &#123;
            <span class="hljs-keyword">var</span> data = <span class="hljs-built_in">JSON</span>.parse(xhr.responseText);
            <span class="hljs-keyword">var</span> hitokoto = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'hitokoto'</span>);
            hitokoto.innerText = data.hitokoto;
        &#125;
    &#125;
    xhr.send();
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>前端html代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">strong</span>></span><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"hitokoto"</span>></span>每日一言获取中...<span class="hljs-tag"></<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">strong</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">4.总结</h2>
<p>有兴趣的可以研究一下以上代码的逻辑和实现方法，还是很有意思的，如果想直接使用，则复制粘贴到页面JS模块中即可。</p>
<p> 更多精彩功能请关注我的个人博客网站：<a href="https://liujian.cool/" target="_blank" rel="nofollow noopener noreferrer">liujian.cool</a></p>
<p>  欢迎关注我的个人公众号：程序猿刘川枫</p>
<p>  <img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/915ad91efb9646809c90b327cbcb9f83~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            