
---
title: 'PBR GGX  Specular G 几何函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afa46b8c45eb43158b8edfcf5cd645d6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 16:30:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afa46b8c45eb43158b8edfcf5cd645d6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">几何函数</h2>
<ul>
<li>几何函数从统计学上近似的求得了微平面间相互遮蔽的比率，这种相互遮蔽会损耗光线的能量。</li>
<li>几何函数是一个值域为[0.0, 1.0]的乘数，其中白色或者说1.0表示没有微平面阴影，而黑色或者说0.0则表示微平面彻底被遮蔽。</li>
<li>几何项的影响可以间接地看作其对方向反射率（directional albedo）的影响</li>
<li>大多数材质的方向反射率（directional albedo）对于前70度是相对平坦的，并且切线入射处的反射率与表面粗糙度密切相关。</li>
<li>几何项的选择会对反射率产生影响，反过来又会对表面外观产生影响。</li>
<li>完全省略G项和1/cosθl cosθv项的模型，被称为“No G”模型，会导致在掠射角处过暗的响应。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afa46b8c45eb43158b8edfcf5cd645d6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
图 几种镜面反射几何模型的反射率图示。 所有图中都使用相同的D（GGX / TR）项和F项。 左图：光滑表面（α= 0.02）; 右图：粗糙表面（α= 0.5）。 其中，“No G”模型已去除G和1/cosθl cosθv项的计算。</p>
<h2 data-id="heading-1">示意图</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdc36871fe1b4cdf9d913bae2461ac37~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">公式</h2>
<h3 data-id="heading-3">公式1</h3>
<ul>
<li><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/deb6e133bd7f4b05b66503ea241eb7ac~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li>G函数 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/125b5add80fb453b93fa658c814d13e8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>K变量
<ul>
<li>直接光照<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b137b8b475034a1eaa50033a434a8853~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>IBL环境光<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe10eb98421543069c39f2e75b16e48f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
</li>
</ul>
</li>
<li>几何函数GLSL</li>
</ul>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-type">float</span> GeometrySchlickGGX(<span class="hljs-type">float</span> NdotV, <span class="hljs-type">float</span> k)
&#123;
    <span class="hljs-type">float</span> nom   = NdotV;
    <span class="hljs-type">float</span> denom = NdotV * (<span class="hljs-number">1.0</span> - k) + k;

    <span class="hljs-keyword">return</span> nom / denom;
&#125;

<span class="hljs-type">float</span> GeometrySmith(<span class="hljs-type">vec3</span> N, <span class="hljs-type">vec3</span> V, <span class="hljs-type">vec3</span> L, <span class="hljs-type">float</span> k)
&#123;
    <span class="hljs-type">float</span> NdotV = <span class="hljs-built_in">max</span>(<span class="hljs-built_in">dot</span>(N, V), <span class="hljs-number">0.0</span>);
    <span class="hljs-type">float</span> NdotL = <span class="hljs-built_in">max</span>(<span class="hljs-built_in">dot</span>(N, L), <span class="hljs-number">0.0</span>);
    <span class="hljs-type">float</span> ggx1 = GeometrySchlickGGX(NdotV, k);
    <span class="hljs-type">float</span> ggx2 = GeometrySchlickGGX(NdotL, k);

    <span class="hljs-keyword">return</span> ggx1 * ggx2;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">公式2</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f2c7c38678c4f6dbea10d3512a37db1~tplv-k3u1fbpfcp-watermark.image" alt="[公式]" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>将粗糙度参数进行重映射以减少光泽表面的极端增益，即将α 从[0, 1]重映射到[0.5, 1]，α的值为(0.5 + roughness/2)^2。从而使几何项的粗糙度变化更加平滑</li>
</ul>
<pre><code class="hljs language-GLSL copyable" lang="GLSL"><span class="hljs-comment">// Smith GGX G项，各项同性版本</span>
<span class="hljs-type">float</span> smithG_GGX(<span class="hljs-type">float</span> NdotV, <span class="hljs-type">float</span> alphaG)
&#123;
    <span class="hljs-type">float</span> a = alphaG * alphaG;
    <span class="hljs-type">float</span> b = NdotV * NdotV;
    <span class="hljs-keyword">return</span> <span class="hljs-number">1</span> / (NdotV + <span class="hljs-built_in">sqrt</span>(a + b - a * b));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">公式3</h2>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-comment">// Smith GGX G项，各项异性版本</span>
<span class="hljs-comment">// Derived G function for GGX</span>
<span class="hljs-type">float</span> smithG_GGX_aniso(<span class="hljs-type">float</span> dotVN, <span class="hljs-type">float</span> dotVX, <span class="hljs-type">float</span> dotVY, <span class="hljs-type">float</span> ax, <span class="hljs-type">float</span> ay)
&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">1.0</span> / (dotVN + <span class="hljs-built_in">sqrt</span>(<span class="hljs-built_in">pow</span>(dotVX * ax, <span class="hljs-number">2.0</span>) + <span class="hljs-built_in">pow</span>(dotVY * ay, <span class="hljs-number">2.0</span>) + <span class="hljs-built_in">pow</span>(dotVN, <span class="hljs-number">2.0</span>)));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">公式4</h2>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-comment">// GGX清漆几何项</span>
<span class="hljs-comment">// G GGX function for clearcoat</span>
<span class="hljs-type">float</span> G_GGX(<span class="hljs-type">float</span> dotVN, <span class="hljs-type">float</span> alphag)
&#123;
    <span class="hljs-type">float</span> a = alphag * alphag;
    <span class="hljs-type">float</span> b = dotVN * dotVN;
    <span class="hljs-keyword">return</span> <span class="hljs-number">1.0</span> / (dotVN + <span class="hljs-built_in">sqrt</span>(a + b - a * b));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>对于对清漆层进行处理的次级波瓣（secondary lobe），Disney没有使用Smith G推导，而是直接使用固定粗糙度为0.25的GGX的 G项，便可以得到合理且很好的视觉效果。</li>
</ul>
<hr></div>  
</div>
            