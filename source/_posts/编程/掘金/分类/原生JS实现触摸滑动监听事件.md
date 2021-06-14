
---
title: '原生JS实现触摸滑动监听事件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3afbd79b3ef74983a6f8406bdbf07a07~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 23:07:42 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3afbd79b3ef74983a6f8406bdbf07a07~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;color:rgba(46,36,36,.87);overflow-x:hidden&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;margin-bottom:5px;font-size:30px;font-weight:500&#125;.markdown-body h1:before&#123;content:"#";margin-right:10px;color:#1976d2&#125;.markdown-body h2&#123;font-size:28px;font-weight:400;border-left:5px solid #454545;margin-top:20px;padding-left:10px;transition:all .3s ease-in-out&#125;.markdown-body h2:hover&#123;border-color:#1976d2&#125;.markdown-body h3&#123;font-size:24px;font-weight:400;margin-top:15px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:20px;font-weight:500&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body h2:first-letter,.markdown-body h3:first-letter,.markdown-body p:first-letter&#123;text-transform:capitalize&#125;.markdown-body em&#123;text-emphasis:dot;text-emphasis-position:under&#125;.markdown-body img&#123;display:block;margin:0 auto!important;max-width:100%;border-radius:2px;box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)!important&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#ddd,#999,#ddd);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;font-weight:900;word-break:break-word;border-radius:2px;overflow-x:auto;font-size:.87em;padding:.065em .4em;background-color:#fbe5e1;color:#c0341d&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:0 4px&#125;.markdown-body pre>code&#123;font-weight:400;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#027fff;transition:all .3s ease-in-out;padding-bottom:4px;border-bottom:2px solid transparent&#125;.markdown-body a:after&#123;content:"";display:inline-block;width:18px;height:18px;margin-left:4px;vertical-align:middle;background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMiIgaGVpZ2h0PSIyMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiMwMjdGRkYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PHBhdGggZD0iTTkuODE1IDYuNDQ4bDEuOTM2LTEuOTM2YzEuMzM3LTEuMzM2IDMuNTgtMS4yNTkgNS4wMTMuMTczIDEuNDMyIDEuNDMyIDEuNTEgMy42NzYuMTczIDUuMDEzbC0xLjQ1MiAxLjQ1Mi0uOTY4Ljk2OGMtMS4zMzcgMS4zMzYtMy41ODEgMS4yNTktNS4wMTMtLjE3MyIvPjxwYXRoIGQ9Ik0xMS4yNjcgMTUuMzY3bC0xLjkzNiAxLjkzNmMtMS4zMzYgMS4zMzctMy41OCAxLjI2LTUuMDEyLS4xNzMtMS40MzItMS40MzItMS41MS0zLjY3Ni0uMTczLTUuMDEybDEuNDUyLTEuNDUyLjk2OC0uOTY4YzEuMzM2LTEuMzM3IDMuNTgtMS4yNiA1LjAxMi4xNzMiLz48L2c+PC9zdmc+);background-size:cover;background-repeat:no-repeat&#125;.markdown-body a:hover&#123;border-color:#027fff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body a.footnote-backref:after,.markdown-body a.footnote-ref:after,.markdown-body sup a:after&#123;display:none!important&#125;.markdown-body table&#123;margin:0 auto 10px;font-size:12px;width:auto;max-width:100%;overflow:auto;border:2px solid #c6c6c6&#125;.markdown-body table img&#123;box-shadow:none!important&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body del&#123;color:rgba(0,0,0,.6)&#125;.markdown-body blockquote&#123;position:relative;color:#666;padding:5px 23px 1px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:hsla(0,0%,78.4%,.12);transition:all .2s ease-in-out&#125;.markdown-body blockquote:hover&#123;border-color:#1976d2&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;font-size:24px;font-weight:800;line-height:24px;color:#cbcbcb;opacity:.6&#125;.markdown-body blockquote:before&#123;content:"“";top:4px;left:6px&#125;.markdown-body blockquote:after&#123;content:"”";right:8px;bottom:-8px&#125;.markdown-body blockquote>p,.markdown-body blockquote blockquote&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #1976d2;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary:hover::-webkit-details-marker&#123;color:#1976d2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第14天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>今天写一个小Demo，有个地方涉及到了左滑右滑的逻辑，本来想着用插件来着，但是想到自己好久没用原生JS写滑动的监听了，所以试着用原生JS来实现了一下，毕竟温故而知新嘛，同时做个记录。先把实现的效果贴出来：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3afbd79b3ef74983a6f8406bdbf07a07~tplv-k3u1fbpfcp-watermark.image" alt="GIF 2021-6-14 14-20-39.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">构思</h2>
<p>想要写出丝滑的触摸滑动事件的监听，要考虑以下3个方面的逻辑：</p>
<ul>
<li><strong>距离：</strong> 滑动距离要大于40</li>
<li><strong>时间：</strong> 滑动时间小于在0.5秒，即500毫秒内完成手指按下，拖动，离开（避免只是手指在屏幕就触发）</li>
<li><strong>滑动方向：</strong>
<ol>
<li>左右滑动的条件是：X轴移动的距离大于Y轴移动的距离，为正则向左，为负则向右</li>
<li>上下滑动的条件是Y轴移动的距离大于X轴移动的距离，为正则向上，为负则向下</li>
</ol>
</li>
</ul>
<p>有了基础的构思，我们就可以根据这个思路来完成代码了~</p>
<h2 data-id="heading-2">监听的事件</h2>
<p>说到监听触摸滑动，要用到的自然就是下面这<strong>三个触摸事件</strong>了：</p>
<pre><code class="copyable">1. touchstart 触摸开始，手指点击屏幕时触发（可监听多点触控，后面的手指也同样会触发）
2. touchmove 接触点改变，滑动时持续触发
3. touchend 触摸结束，手指离开屏幕时触发
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这三个触摸事件每个都包括了<strong>三个触摸对象列表</strong>（可根据触摸点实现多点触控）：</p>
<pre><code class="copyable">1. touches：当前屏幕上的所有手指触摸点的列表
2. targetTouches：当前DOM元素上手指的列表
3. changedTouches：当前事件手指的列表
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时每个触摸对象Touch包含的属性如下：</p>
<pre><code class="copyable">- identifier：标识触摸的唯一ID
- pageX：触摸点在页面中的x坐标
- pageY：触摸点在页面中的y坐标
- screenX：触摸点在屏幕中的x坐标
- screenY：触摸点在屏幕中的y坐标
- clientX：触摸点在视口中的x坐标
- clientY：触摸点在视口中的y坐标
- target：触摸的DOM节点
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">代码实现</h2>
<p>有了上面的构思和触摸事件的基础，我们很容易就能把代码敲出来啦~</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> box = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'body'</span>) <span class="hljs-comment">// 监听对象</span>
<span class="hljs-keyword">let</span> startTime = <span class="hljs-string">''</span> <span class="hljs-comment">// 触摸开始时间</span>
<span class="hljs-keyword">let</span> startDistanceX = <span class="hljs-string">''</span> <span class="hljs-comment">// 触摸开始X轴位置</span>
<span class="hljs-keyword">let</span> startDistanceY = <span class="hljs-string">''</span> <span class="hljs-comment">// 触摸开始Y轴位置</span>
<span class="hljs-keyword">let</span> endTime = <span class="hljs-string">''</span> <span class="hljs-comment">// 触摸结束时间</span>
<span class="hljs-keyword">let</span> endDistanceX = <span class="hljs-string">''</span> <span class="hljs-comment">// 触摸结束X轴位置</span>
<span class="hljs-keyword">let</span> endDistanceY = <span class="hljs-string">''</span> <span class="hljs-comment">// 触摸结束Y轴位置</span>
<span class="hljs-keyword">let</span> moveTime = <span class="hljs-string">''</span> <span class="hljs-comment">// 触摸时间</span>
<span class="hljs-keyword">let</span> moveDistanceX = <span class="hljs-string">''</span> <span class="hljs-comment">// 触摸移动X轴距离</span>
<span class="hljs-keyword">let</span> moveDistanceY = <span class="hljs-string">''</span> <span class="hljs-comment">// 触摸移动Y轴距离</span>
box.addEventListener(<span class="hljs-string">"touchstart"</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    startTime = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()
    startDistanceX = e.touches[<span class="hljs-number">0</span>].screenX
    startDistanceY = e.touches[<span class="hljs-number">0</span>].screenY
&#125;)
box.addEventListener(<span class="hljs-string">"touchend"</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    endTime = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()
    endDistanceX = e.changedTouches[<span class="hljs-number">0</span>].screenX
    endDistanceY = e.changedTouches[<span class="hljs-number">0</span>].screenY
    moveTime = endTime - startTime
    moveDistanceX = startDistanceX - endDistanceX
    moveDistanceY = startDistanceY - endDistanceY
    <span class="hljs-built_in">console</span>.log(moveDistanceX, moveDistanceY)
    <span class="hljs-comment">// 判断滑动距离超过40 且 时间小于500毫秒</span>
    <span class="hljs-keyword">if</span> ((<span class="hljs-built_in">Math</span>.abs(moveDistanceX) > <span class="hljs-number">40</span> || <span class="hljs-built_in">Math</span>.abs(moveDistanceY) > <span class="hljs-number">40</span>) && moveTime < <span class="hljs-number">500</span>) &#123;
        <span class="hljs-comment">// 判断X轴移动的距离是否大于Y轴移动的距离</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Math</span>.abs(moveDistanceX) > <span class="hljs-built_in">Math</span>.abs(moveDistanceY)) &#123;
        <span class="hljs-comment">// 左右</span>
        <span class="hljs-built_in">console</span>.log(moveDistanceX > <span class="hljs-number">0</span> ? <span class="hljs-string">'左'</span> : <span class="hljs-string">'右'</span>)
        &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 上下</span>
        <span class="hljs-built_in">console</span>.log(moveDistanceY > <span class="hljs-number">0</span> ? <span class="hljs-string">'上'</span> : <span class="hljs-string">'下'</span>)
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行一下看看吧：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59026c6739394197b265139c3b2b773d~tplv-k3u1fbpfcp-watermark.image" alt="GIF 2021-6-14 14-54-55.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出，触摸时间大于500ms不会触发，滑动距离小于40也不会触发，如果是有角度的滑动，则会以XY轴移动距离最远的为准。完美实现！</p>
<h2 data-id="heading-4">后记</h2>
<p>前端框架发展日益迅猛，很多人直接上手学习框架也毫无压力，对原生JS的学习就不那么重视了。但万变不离其宗，框架的优势在于它的设计思想和模式，想要深刻的理解还是要有原生JS做基础，想要走得远，还是要把基础夯实，毕竟万丈高楼平地起不是？</p>
<blockquote>
<p>PS: 今天是我参加掘金更文挑战的第14天，端午节依旧努力淦文章，目前已经坚持14天，马上半个月啦，可喜可贺~ 有志者，事竟成。大家一起加油呀~</p>
<p>附更文挑战的文章目录如下：</p>
</blockquote>
<ul>
<li>2021.06.01  <a href="https://juejin.cn/post/6968816441801998349" target="_blank">《多图预警！详细谈谈Flex布局的容器元素和项目元素的属性~》</a></li>
<li>2021.06.02  <a href="https://juejin.cn/post/6969128755067355143" target="_blank">《如何把css渐变背景玩出花样来》</a></li>
<li>2021.06.03  <a href="https://juejin.cn/post/6969449102882897950" target="_blank">《如何使用SVG制作沿任意路径排布的文字效果》</a></li>
<li>2021.06.04  <a href="https://juejin.cn/post/6969839212069650462" target="_blank">《3大类15小类前端代码规范，让团队代码统一规范起来！》</a></li>
<li>2021.06.05  <a href="https://juejin.cn/post/6970275680047071240" target="_blank">《团队管理之git提交规范：大家竟然都不会写commit记录？｜ 周末学习》</a></li>
<li>2021.06.06  <a href="https://juejin.cn/post/6970694281447079944" target="_blank">《如何控制css鼠标样式以及扩大鼠标点击区域 ｜ 周末学习》</a></li>
<li>2021.06.07  <a href="https://juejin.cn/post/6970979674092634120" target="_blank">《纯css实现：仿掘金账户密码登录时，小熊猫捂眼动作切换的小彩蛋》</a></li>
<li>2021.06.08  <a href="https://juejin.cn/post/6971451608135630862" target="_blank">《从11个方面详细谈谈原型和原型链》</a></li>
<li>2021.06.09  <a href="https://juejin.cn/post/6971804688656105485" target="_blank">《深入谈谈JavaScript的作用域及作用域链》</a></li>
<li>2021.06.10  <a href="https://juejin.cn/post/6972067390045552654" target="_blank">《JavaScript中的闭包究竟是什么》</a></li>
<li>2021.06.11  <a href="https://juejin.cn/post/6972551777795178509" target="_blank">《纯css实现：炫酷的视频文本蒙版效果》</a></li>
<li>2021.06.12  <a href="https://juejin.cn/post/6972935210702733319" target="_blank">《申请一个免费的毒鸡汤api，并且用原生JS实现竖行文本的打字机效果》</a></li>
<li>2021.06.13  <a href="https://juejin.cn/post/6973225625708396558" target="_blank">《纯css实现：多行文本框内的斑马条纹效果》</a></li>
</ul></div>  
</div>
            