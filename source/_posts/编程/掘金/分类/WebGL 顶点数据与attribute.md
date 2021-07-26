
---
title: 'WebGL 顶点数据与attribute'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4817'
author: 掘金
comments: false
date: Sat, 24 Jul 2021 17:38:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=4817'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">需要顶点着色器处理</h2>
<ul>
<li>uv</li>
<li>position</li>
<li>normal</li>
<li>color</li>
<li>targent</li>
</ul>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-keyword">attribute</span> <span class="hljs-type">vec3</span> position;
<span class="hljs-keyword">attribute</span> <span class="hljs-type">vec2</span> uv;
<span class="hljs-keyword">attribute</span> <span class="hljs-type">vec3</span> normal;

<span class="hljs-keyword">uniform</span> <span class="hljs-type">mat4</span> model;

<span class="hljs-keyword">varying</span> <span class="hljs-type">vec2</span> vUv;
<span class="hljs-keyword">varying</span> <span class="hljs-type">vec3</span> vNormal;
<span class="hljs-type">void</span> main() &#123;
    vUv = uv;
    vNormal = <span class="hljs-type">mat3</span>(<span class="hljs-built_in">transpose</span>(<span class="hljs-built_in">inverse</span>(model))) * normal;  
    <span class="hljs-built_in">gl_Position</span> = projectionMatrix * modelViewMatrix * <span class="hljs-type">vec4</span>( position, <span class="hljs-number">1.0</span> );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> vertexColorBuffer = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, vertexColorBuffer);
gl.bufferData(gl.ARRAY_BUFFER, verticesColors, gl.STATIC_DRAW);
<span class="hljs-keyword">var</span> FSIZE = verticesColors.BYTES_PER_ELEMENT;
<span class="hljs-keyword">var</span> a_Position = gl.getAttribLocation(gl.program, <span class="hljs-string">"a_Position"</span>);
gl.vertexAttribPointer(a_Position, <span class="hljs-number">3</span>, gl.FLOAT, <span class="hljs-literal">false</span>, FSIZE * <span class="hljs-number">6</span>, <span class="hljs-number">0</span>);
gl.enableVertexAttribArray(a_Position);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用方式2</li>
</ul>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-keyword">layout</span> (<span class="hljs-keyword">location</span> = <span class="hljs-number">0</span>) <span class="hljs-keyword">in</span> <span class="hljs-type">vec3</span> position;
<span class="hljs-keyword">layout</span> (<span class="hljs-keyword">location</span> = <span class="hljs-number">1</span>) <span class="hljs-keyword">in</span> <span class="hljs-type">vec3</span> normal;
<span class="hljs-keyword">layout</span> (<span class="hljs-keyword">location</span> = <span class="hljs-number">2</span>) <span class="hljs-keyword">in</span> <span class="hljs-type">vec2</span> uv;

<span class="hljs-keyword">out</span> <span class="hljs-type">vec2</span> vUv;
<span class="hljs-keyword">out</span> <span class="hljs-type">vec3</span> vNormal;
<span class="hljs-type">void</span> main() &#123;
    vUv = uv;
    vNormal = normal;
    <span class="hljs-built_in">gl_Position</span> = projectionMatrix * modelViewMatrix * <span class="hljs-type">vec4</span>( position, <span class="hljs-number">1.0</span> );
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> POSITION_LOCATION = <span class="hljs-number">0</span>;
<span class="hljs-keyword">const</span> NORMAL_LOCATION = <span class="hljs-number">1</span>;
<span class="hljs-keyword">const</span> TEXCOORD_0_LOCATION = <span class="hljs-number">2</span>;
glPlaneVAO = gl.createVertexArray();
<span class="hljs-keyword">let</span> planeVBO = gl.createBuffer();
gl.bindVertexArray(glPlaneVAO);
gl.bindBuffer(gl.ARRAY_BUFFER, planeVBO);
gl.bufferData(gl.ARRAY_BUFFER, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>(planeVertices), gl.STATIC_DRAW);
gl.enableVertexAttribArray(POSITION_LOCATION);
gl.vertexAttribPointer(POSITION_LOCATION, <span class="hljs-number">3</span>, gl.FLOAT, <span class="hljs-literal">false</span>, <span class="hljs-number">8</span> * sizeFloat, <span class="hljs-number">0</span>);
gl.enableVertexAttribArray(NORMAL_LOCATION);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">不需要顶点着色器处理的</h2>
<ul>
<li>indices</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Indices of the vertices</span>
<span class="hljs-keyword">var</span> indices = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>([<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">0</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>, <span class="hljs-comment">// front</span>
  <span class="hljs-number">0</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">0</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>, <span class="hljs-comment">// right</span>
  <span class="hljs-number">0</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">0</span>,<span class="hljs-number">6</span>,<span class="hljs-number">1</span>, <span class="hljs-comment">// up</span>
  <span class="hljs-number">1</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">1</span>,<span class="hljs-number">7</span>,<span class="hljs-number">2</span>, <span class="hljs-comment">// left</span>
  <span class="hljs-number">7</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">7</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>, <span class="hljs-comment">// down</span>
  <span class="hljs-number">4</span>,<span class="hljs-number">7</span>,<span class="hljs-number">6</span>,<span class="hljs-number">4</span>,<span class="hljs-number">6</span>,<span class="hljs-number">5</span> <span class="hljs-comment">// back</span>
]);
<span class="hljs-comment">//index的话 必须经过这个api</span>
<span class="hljs-keyword">var</span> indexBuffer = gl.createBuffer(); <span class="hljs-comment">//index </span>
gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer); <span class="hljs-comment">//bind buffer</span>
gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indices, gl.STATIC_DRAW); <span class="hljs-comment">// bufferdata</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            