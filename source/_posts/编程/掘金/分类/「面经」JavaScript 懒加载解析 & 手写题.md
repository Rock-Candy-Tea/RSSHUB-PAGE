
---
title: '「面经」JavaScript 懒加载解析 & 手写题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/353c94b7715542c89c6ad2054732736e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 02:31:16 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/353c94b7715542c89c6ad2054732736e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与新手入门的第 1 篇文章</p>
</blockquote>
<h1 data-id="heading-0">图片懒加载</h1>
<h2 data-id="heading-1">前置知识</h2>
<p>大多数 JavaScript 处理的是以下坐标系其中一种：</p>
<ul>
<li><strong>相对于窗口</strong>：类似于 <code>position: fixed</code>，从 <strong>窗口</strong> 的顶部和两侧计算得出，用 <code>clientX</code> / <code>clientY</code> 表示</li>
<li><strong>相对于文档</strong>：类似于 <code>position: absolute</code>，从 <strong>文档</strong> 的顶部和两侧计算得出，用 <code>pageX</code> / <code>pageY</code> 表示</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/353c94b7715542c89c6ad2054732736e~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-03 11.11.35.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">元素坐标</h3>
<p><code>ele.getBoundingClientRect()</code> 获取窗口坐标，<code>ele</code> 是 <code>DOMRect</code> 对象，具有如下属性：</p>
<ul>
<li><code>x</code> / <code>y</code> 是 <strong>矩形原点</strong> 相对于 <strong>窗口</strong> 的坐标</li>
<li><code>width</code> / <code>height</code> 是矩形的宽高</li>
<li><code>top</code> / <code>bottom</code> 是顶部/底部矩形边缘的 Y 坐标</li>
<li><code>left</code> / <code>right</code> 是左/右矩形边缘的 X 坐标</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc6547017032480c985d93a3da92235b~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-03 11.37.36.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中可以得出：</p>
<ul>
<li><code>left = x</code></li>
<li><code>top = y</code></li>
<li><code>right = x + width</code></li>
<li><code>bottom = y + height</code></li>
</ul>
<h4 data-id="heading-3">为什么需要 <code>top</code> / <code>left</code> 这种看起来重复的属性？</h4>
<p>原点不一定是矩形的左上角，当原点变成例如右下角的时候 <code>left !== x</code>，<code>top !== y</code></p>
<p><code>width</code> 和 <code>height</code> 从右下角开始「增长」，也就变成了负值</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844caab5353e4439bb6cce92cc4fbd21~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-03 11.46.34.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4"><code>IE</code> 不支持 <code>x</code> / <code>y</code></h4>
<p>可以自己写一个 <code>polyfill</code>（在 <code>DomRect.prototype</code> 中添加一个 <code>getter</code>），或者使用 <code>left</code> / <code>top</code></p>
<h4 data-id="heading-5">坐标的 <code>right</code> / <code>bottom</code> 与 <code>CSS position</code> 属性不同</h4>
<p>相对于窗口（window）的坐标和 CSS position:fixed 之间有明显的相似之处。
但是在 CSS 定位中，right 属性表示距右边缘的距离，而 bottom 属性表示距下边缘的距离。
如果我们再看一下上面的图片，我们可以看到在 JavaScript 中并非如此。窗口的所有坐标都从左上角开始计数，包括这些坐标。</p>
<p>但是我目前不是很理解</p>
<h3 data-id="heading-6">文档坐标</h3>
<p>获取文档坐标的方式：</p>
<ul>
<li><code>pageY</code> = <code>clientY</code> + 文档的垂直滚动出的部分的高度</li>
<li><code>pageX</code> = <code>clientX</code> + 文档的水平滚动出的部分的宽度</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getCoords</span>(<span class="hljs-params">ele</span>) </span>&#123;
  <span class="hljs-keyword">let</span> rect = ele.getBoundingClientRect()

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">top</span>: rect.top + <span class="hljs-built_in">window</span>.pageYOffset,
    <span class="hljs-attr">right</span>: rect.right + <span class="hljs-built_in">window</span>.pageXOffset,
    <span class="hljs-attr">bottom</span>: rect.bottom + <span class="hljs-built_in">window</span>.pageYOffset,
    <span class="hljs-attr">left</span>: rect.left + <span class="hljs-built_in">window</span>.pageXOffset
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">图片懒加载代码</h2>
<p><code>rect.top</code> 是相对于当前窗口 <strong>上边</strong> 的数值，也就是说当图片在文档的下方时 <code>rect.top > window.innerHeight</code>，只有当图片经过视窗时才会 <code>rect.top <= window.innerHeight</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> img_list = [...document.querySelectorAll(<span class="hljs-string">'img'</span>)]
<span class="hljs-keyword">const</span> num = img_list.length

<span class="hljs-comment">/**
 * 图片懒加载
 */</span>
<span class="hljs-keyword">const</span> img_lazy_load = (<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">let</span> cnt = <span class="hljs-number">0</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">let</span> deleteIndexList = []
    img_list.forEach(<span class="hljs-function">(<span class="hljs-params">img, index</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> rect = img.getBoundingClientRect()
      <span class="hljs-built_in">console</span>.log(rect.top, <span class="hljs-built_in">window</span>.innerHeight)
      <span class="hljs-keyword">if</span> (rect.top < <span class="hljs-built_in">window</span>.innerHeight) &#123;
        img.src = img.dataset.src
        deleteIndexList.push(index)
        cnt++
        <span class="hljs-keyword">if</span> (cnt === num) &#123;
          <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'scroll'</span>, img_lazy_load)
        &#125;
      &#125;
    &#125;)
    img_list = img_list.filter(<span class="hljs-function">(<span class="hljs-params">_, index</span>) =></span> !deleteIndexList.includes(index))
  &#125;
&#125;)()

<span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'scroll'</span>, img_lazy_load)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">数据类型判断</h1>
<p><code>typeof</code> 可以正确识别：</p>
<ul>
<li>undefined</li>
<li>boolean</li>
<li>number</li>
<li>string</li>
<li>symbol</li>
<li>function</li>
</ul>
<p>但是对于别的类型都会识别成 <code>object</code>，利用 <code>Object.prototype.toString</code> 来正确判断类型，截取 <code>[object xxxxx]</code> 中 <code>object</code> 后边到 <code>]</code> 的文本并且统一转小写：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> type_of = <span class="hljs-function">(<span class="hljs-params">obj</span>) =></span> <span class="hljs-built_in">Object</span>.prototype.toString.call(obj).slice(<span class="hljs-number">8</span>, -<span class="hljs-number">1</span>).toLowerCase()

type_of(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()) <span class="hljs-comment">// date</span>
type_of(&#123;&#125;) <span class="hljs-comment">// object</span>
type_of(<span class="hljs-literal">null</span>) <span class="hljs-comment">// null</span>
type_of([]) <span class="hljs-comment">// array</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">数组去重</h1>
<p><strong>es5</strong>，利用 <code>filter</code> 判断当前元素是否是第一次出现在数组中：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> unique = <span class="hljs-function">(<span class="hljs-params">arr: <span class="hljs-built_in">any</span>[]</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> arr.filter(<span class="hljs-function">(<span class="hljs-params">item, index, arr</span>) =></span> arr.indexOf(item) === index)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>es6</strong>，使用 <code>Set</code> 数据结构自动去重：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> unique_es6 = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> [...new <span class="hljs-built_in">Set</span>(arr)]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不使用 <code>Set</code>，用空间换时间，模拟 <code>Map</code> 存键值对，时间复杂度 <strong>O(n)</strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> get_type_and_val = <span class="hljs-function">(<span class="hljs-params">obj</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> obj === <span class="hljs-string">'object'</span> && obj) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.toString.call(obj) + <span class="hljs-built_in">JSON</span>.stringify(obj)
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.toString.call(obj) + obj.toString()
&#125;

<span class="hljs-keyword">const</span> unique_on = <span class="hljs-function">(<span class="hljs-params">arr: <span class="hljs-built_in">any</span>[]</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> temp = &#123;&#125;
  <span class="hljs-keyword">const</span> result = []
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> arr) &#123;
    <span class="hljs-keyword">const</span> key = get_type_and_val(item)
    <span class="hljs-keyword">if</span> (!temp.hasOwnProperty(key)) &#123;
      result.push(item)
      temp[key] = <span class="hljs-literal">true</span>
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">字符串反转</h1>
<p>主要利用数组的 <code>join()</code> 方法，反向遍历，最后一种采用 <strong>es6 解构</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> reverse_1 = <span class="hljs-function">(<span class="hljs-params">str: <span class="hljs-built_in">string</span></span>) =></span> str.split(<span class="hljs-string">''</span>).reverse().join(<span class="hljs-string">''</span>)

<span class="hljs-keyword">const</span> reverse_2 = <span class="hljs-function">(<span class="hljs-params">str: <span class="hljs-built_in">string</span></span>) =></span> &#123;
  <span class="hljs-keyword">let</span> result = <span class="hljs-string">''</span>
  <span class="hljs-keyword">const</span> len = str.length
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = len - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; i--) &#123;
    result += str[i]
  &#125;
  <span class="hljs-keyword">return</span> result
&#125;

<span class="hljs-keyword">const</span> reverse_3 = <span class="hljs-function">(<span class="hljs-params">str: <span class="hljs-built_in">string</span></span>) =></span> &#123;
  <span class="hljs-keyword">const</span> result = []
  <span class="hljs-keyword">const</span> len = str.length
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = len - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; i--) &#123;
    result.push(str[i])
  &#125;
  <span class="hljs-keyword">return</span> result.join(<span class="hljs-string">''</span>)
&#125;

<span class="hljs-keyword">const</span> reverse_4 = <span class="hljs-function">(<span class="hljs-params">str: <span class="hljs-built_in">string</span></span>) =></span> &#123;
  <span class="hljs-keyword">const</span> result = str.split(<span class="hljs-string">''</span>)
  <span class="hljs-keyword">const</span> len = str.length
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len >> <span class="hljs-number">1</span>; i++) &#123;
    [result[i], result[len - i - <span class="hljs-number">1</span>]] = [result[len - i - <span class="hljs-number">1</span>], result[i]]
  &#125;
  <span class="hljs-keyword">return</span> result.join(<span class="hljs-string">''</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">数组扁平化</h1>
<p>将数组拍平成一层，并且添加参数控制拍平层数更加符合设计</p>
<pre><code class="hljs language-ts copyable" lang="ts">[<span class="hljs-number">1</span>, [<span class="hljs-number">2</span>], [<span class="hljs-number">3</span>, [<span class="hljs-number">4</span>]]].flat(<span class="hljs-number">1</span>) <span class="hljs-comment">// [ 1, 2, 3, [ 4 ] ]</span>
[<span class="hljs-number">1</span>, [<span class="hljs-number">2</span>], [<span class="hljs-number">3</span>, [<span class="hljs-number">4</span>]]].flat(<span class="hljs-number">2</span>) <span class="hljs-comment">// [ 1, 2, 3, 4 ]</span>

<span class="hljs-keyword">const</span> flat_es6 = <span class="hljs-function">(<span class="hljs-params">arr: <span class="hljs-built_in">any</span>[], depth?: <span class="hljs-built_in">number</span></span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (depth) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < depth; i++) &#123;
      <span class="hljs-keyword">if</span> (!arr.some(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> <span class="hljs-built_in">Array</span>.isArray(item))) <span class="hljs-keyword">break</span>
      arr = [].concat(...arr)
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">while</span> (arr.some(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> <span class="hljs-built_in">Array</span>.isArray(item))) &#123;
      arr = [].concat(...arr)
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> arr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">写在最后</h1>
<p>这是我发布的第一篇文章，但其实它已经躺在我的草稿箱里很久了，我一直纠结于是否应该发这种前辈称作「水文」的文章，但其实它也是我技术成长的一部分，同时也是我准备秋招必经的道路，借此掘金的活动我发布了它，也希望大佬们能给些意见，我最近正在学习 <code>Dart</code> 和 <code>Flutter</code>，应该会记录下来我学习的心路历程，敬请期待。</p>
<blockquote>
<p>参考 <a href="https://javascript.info/" target="_blank" rel="nofollow noopener noreferrer">javascript.info</a></p>
</blockquote></div>  
</div>
            