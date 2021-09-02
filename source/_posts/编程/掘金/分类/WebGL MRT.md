
---
title: 'WebGL MRT'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5538af40d7f548fea03f0f1f52e398f4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 17:31:26 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5538af40d7f548fea03f0f1f52e398f4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fthreejs.org%2Fexamples%2F%3Fq%3Dmrt%23webgl2_multiple_rendertargets" target="_blank" rel="nofollow noopener noreferrer" title="https://threejs.org/examples/?q=mrt#webgl2_multiple_rendertargets" ref="nofollow noopener noreferrer">three.js examples (threejs.org)</a></p>
<h2 data-id="heading-0">MRT</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5538af40d7f548fea03f0f1f52e398f4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>顶点着色器</li>
</ul>
<pre><code class="hljs language-glsl copyable" lang="glsl">version <span class="hljs-number">300</span> es
<span class="hljs-keyword">in</span> <span class="hljs-type">vec3</span> position;
<span class="hljs-keyword">in</span> <span class="hljs-type">vec3</span> normal;
<span class="hljs-keyword">in</span> <span class="hljs-type">vec2</span> uv;
<span class="hljs-keyword">out</span> <span class="hljs-type">vec3</span> vNormal;
<span class="hljs-keyword">out</span> <span class="hljs-type">vec2</span> vUv;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">mat4</span> modelViewMatrix;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">mat4</span> projectionMatrix;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">mat3</span> normalMatrix;
<span class="hljs-type">void</span> main() &#123;
    vUv = uv;
    <span class="hljs-type">vec4</span> mvPosition = modelViewMatrix * <span class="hljs-type">vec4</span>( position, <span class="hljs-number">1.0</span> );
    <span class="hljs-type">vec3</span> transformedNormal = normalMatrix * normal;
    vNormal = <span class="hljs-built_in">normalize</span>( transformedNormal );
    <span class="hljs-built_in">gl_Position</span> = projectionMatrix * mvPosition;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>片元着色器</li>
</ul>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-meta">#version 300 es</span>
<span class="hljs-keyword">precision</span> <span class="hljs-keyword">highp</span> <span class="hljs-type">float</span>;
<span class="hljs-keyword">precision</span> <span class="hljs-keyword">highp</span> <span class="hljs-type">int</span>;
<span class="hljs-keyword">layout</span>(<span class="hljs-keyword">location</span> = <span class="hljs-number">0</span>) <span class="hljs-keyword">out</span> <span class="hljs-type">vec4</span> gColor;
<span class="hljs-keyword">layout</span>(<span class="hljs-keyword">location</span> = <span class="hljs-number">1</span>) <span class="hljs-keyword">out</span> <span class="hljs-type">vec4</span> gNormal;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">sampler2D</span> tDiffuse;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">vec2</span> repeat;
<span class="hljs-keyword">in</span> <span class="hljs-type">vec3</span> vNormal;
<span class="hljs-keyword">in</span> <span class="hljs-type">vec2</span> vUv;
<span class="hljs-type">void</span> main() &#123;
    <span class="hljs-comment">// write color to G-Buffer</span>
    gColor = <span class="hljs-built_in">texture</span>( tDiffuse, vUv * repeat );
    <span class="hljs-comment">// write normals to G-Buffer</span>
    gNormal = <span class="hljs-type">vec4</span>( <span class="hljs-built_in">normalize</span>( vNormal ), <span class="hljs-number">0.0</span> );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">使用MRT的贴图</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/389e98d5fabc46939f531c29895b33d8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6545f22313c34cac82459e5010243170~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>顶点着色器</li>
</ul>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-meta">#version 300 es</span>
<span class="hljs-keyword">in</span> <span class="hljs-type">vec3</span> position;
<span class="hljs-keyword">in</span> <span class="hljs-type">vec2</span> uv;
<span class="hljs-keyword">out</span> <span class="hljs-type">vec2</span> vUv;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">mat4</span> modelViewMatrix;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">mat4</span> projectionMatrix;
<span class="hljs-type">void</span> main() &#123;
    vUv = uv;
    <span class="hljs-built_in">gl_Position</span> = projectionMatrix * modelViewMatrix * <span class="hljs-type">vec4</span>( position, <span class="hljs-number">1.0</span> );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>片元着色器</li>
</ul>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-meta">#version 300 es</span>
<span class="hljs-keyword">precision</span> <span class="hljs-keyword">highp</span> <span class="hljs-type">float</span>;
<span class="hljs-keyword">precision</span> <span class="hljs-keyword">highp</span> <span class="hljs-type">int</span>;
<span class="hljs-keyword">layout</span>(<span class="hljs-keyword">location</span> = <span class="hljs-number">0</span>) <span class="hljs-keyword">out</span> <span class="hljs-type">vec4</span> pc_FragColor;
<span class="hljs-keyword">in</span> <span class="hljs-type">vec2</span> vUv;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">sampler2D</span> tDiffuse;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">sampler2D</span> tNormal;
<span class="hljs-type">void</span> main() &#123;
    <span class="hljs-type">vec3</span> diffuse = <span class="hljs-built_in">texture</span>( tDiffuse, vUv ).rgb;
    <span class="hljs-type">vec3</span> normal = <span class="hljs-built_in">texture</span>( tNormal, vUv ).rgb;
    pc_FragColor.rgb = <span class="hljs-built_in">mix</span>( diffuse, normal, <span class="hljs-built_in">step</span>( <span class="hljs-number">0.5</span>, vUv.x ) );
    pc_FragColor.a = <span class="hljs-number">1.0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            