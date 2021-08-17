
---
title: 'tailwind使用指南——配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc8e8a6100d64734be18b899a8d23dc2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 02:24:53 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc8e8a6100d64734be18b899a8d23dc2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">配置篇</h2>
<p>通过tailwind.config.js可以进行自定义主题配置</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc8e8a6100d64734be18b899a8d23dc2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">purge</h3>
<p>仅在production环境下生效，用于删除没有使用的样式</p>
<h3 data-id="heading-2">darkMode</h3>
<p>为颜色类样式生成dark变体（dark前缀的原子样式）</p>
<h3 data-id="heading-3">theme</h3>
<p>自定义主题</p>
<ul>
<li>spacing</li>
</ul>
<pre><code class="copyable">const spacings = [0, 8, 10, 12, 16, 20, 32, 40, 56, 64, 96, 128, 240, 480];
...
&#123;
    theme:&#123;
        spacing: &#123;
          px: '1px',
          ...spacings.reduce((pre, cur) => &#123; pre[cur] = cur + 'px'; return pre &#125;, &#123;&#125;)
        &#125;,
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认情况下，间距比例会被 <code>padding</code>、 <code>margin</code>、 <code>width</code>、 <code>height</code>、 <code>maxHeight</code>、 <code>gap</code>、 <code>inset</code>、 <code>space</code> 和 <code>translate</code> 。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40637a4f03594f4fb273c6a39ca04b62~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>width、heights</li>
</ul>
<p>很多情况下，w和h的设置与spacing的分级是不一样的，因此有必要为他们单独设置</p>
<pre><code class="copyable">const widths = [44, 240, 400, 480];
const heights = [200, 300];
...
&#123;
...
    theme: &#123;
        width: &#123;
          ...widths.reduce((pre, cur) => &#123; pre[cur] = cur + 'px'; return pre &#125;, &#123;&#125;)
        &#125;,
        heights: &#123;
          ...heights.reduce((pre, cur) => &#123; pre[cur] = cur + 'px'; return pre &#125;, &#123;&#125;)
        &#125;,
    &#125;
&#125;
  
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>colors</li>
</ul>
<p>一般情况下，颜色也是需要修改的</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c83d1f4b443f480f8c579f6ad5651e88~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>默认情况下，这些颜色会被所有颜色驱动的功能类自动共享，如 <code>textColor</code>、<code>backgroundColor</code>、<code>borderColor</code> 等。<br></p>
<p>这个配置生成类似下面的样式</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/584137cb90ef45a98d2887a4fe5579e8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>fontSize</li>
</ul>
<p>推荐配置一个数组，第一位是字号，第二位是行高</p>
<pre><code class="copyable">const fontSizes = [0, 36, 40, 48, 56, 64]; 
...
&#123;
    theme: &#123;
        fontSize: &#123;
          //字号和行高，12号字体1行高
          sm: ["24px", "24px"], //最小12，12一下不能保证
          base: ["28px", "40px"],
          lg: ["32px", "48px"], // 以上三种为项目中主要字号，不以数字命名，其他特殊字号以数字命名
          ...fontSizes.reduce((pre, cur) => &#123;
            pre[cur] = [cur + "px", 1];
            return pre;
          &#125;, &#123;&#125;),
        &#125;,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>extend:不覆盖原有样式</li>
</ul>
<p>上面配置的colors等都会覆盖掉原来的配置，通常文字的颜色与其他填充颜色有很多重叠，因此可以在继承colors的基础上，单独为某些用途的文字单独配置颜色</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5a73937beb048adb64124aa285ec196~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">plugins</h3>
<p>当需要新增一些自定义样式时就可以使用这个api，比如设置基础样式（Preflight）、组件样式等</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0903e080715f42c49aa2e3dc4be85594~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">变体</h3>
<p>变体可以理解为某些场景下的前缀，比如hover、focus,当然也可以根据文档配置自定义变体</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18409a0a70274ab69df4664311f0aa93~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
（需要注意当变体使用transform时，必须设置transform）</p>
<h2 data-id="heading-6">在css中自定义样式</h2>
<p>除了在tailwind.config.js中进行样式的扩展，还支持在css中使用函数与指令进行扩展，写法更简单</p>
<h3 data-id="heading-7">@layer</h3>
<p>添加基础样式，与plugins的addBase,addComponents等价</p>
<pre><code class="copyable">@layer base &#123;
  h1 &#123;
    @apply text-2xl;
  &#125;
  h2 &#123;
    @apply text-xl;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">@layer components &#123;
  .btn-blue &#123;
    @apply bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">@variants、@screen、@responsive</h3>
<p>这三个都是为你的自定义样式增加一些额外功能，比如focus等某些变体、媒体查询的某个断电、生成对应的一系列列响应式样式</p></div>  
</div>
            