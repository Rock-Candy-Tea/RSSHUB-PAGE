
---
title: 'OpenGL_JS-transformations'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3485'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 23:34:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=3485'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ul>
<li>顶点着色器</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> vs_transform = <span class="hljs-string">`#version 300 es
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec2 aTexCoord;
out vec2 TexCoord;
uniform mat4 transform;
void main()
&#123;
gl_Position = transform * vec4(aPos, 1.0);
TexCoord = vec2(aTexCoord.x, aTexCoord.y);
&#125;`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>片元着色器</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> fs_transform = <span class="hljs-string">`#version 300 es 
precision mediump float;
out vec4 FragColor;
in vec2 TexCoord;
// texture samplers
uniform sampler2D texture1;
uniform sampler2D texture2;
void main()
&#123;
// linearly interpolate between both textures (80% container, 20% awesomeface)
FragColor = mix(texture(texture1, TexCoord), texture(texture2, TexCoord), 0.2);
&#125;`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>createVertexArray bindVertexArray</li>
<li>createBuffer bindBuffer bufferData vertexAttribPointer enableVertexAttribArray</li>
<li>createBuffer bufferData</li>
</ul>
<pre><code class="copyable">ourShader = new Shader(gl, vs_transform, fs_transform);
let vertices = new Float32Array([
    0.5, 0.5, 0.0, 1.0, 1.0,
    0.5, -0.5, 0.0, 1.0, 0.0,
    -0.5, -0.5, 0.0, 0.0, 0.0,
    -0.5, 0.5, 0.0, 0.0, 1.0
]);
let indices = new Uint16Array([
    0, 1, 3,
    1, 2, 3
]);
VAO = gl.createVertexArray();
let VBO = gl.createBuffer();
let EBO = gl.createBuffer();
gl.bindVertexArray(VAO);
gl.bindBuffer(gl.ARRAY_BUFFER, VBO);
gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);
gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, EBO);
gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indices, gl.STATIC_DRAW);
gl.vertexAttribPointer(0, 3, gl.FLOAT, false, 5 * sizeFloat, 0);
gl.enableVertexAttribArray(0);
gl.vertexAttribPointer(1, 2, gl.FLOAT, false, 5 * sizeFloat, (3 * sizeFloat));
gl.enableVertexAttribArray(1);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>createTexture bindTexture texParameteri texImage2D</li>
</ul>
<pre><code class="copyable">texture1 = gl.createTexture();
initTexture(gl, texture1);
const image1 = new Image();
image1.onload = function () &#123;
    gl.bindTexture(gl.TEXTURE_2D, texture1);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB, gl.RGB, gl.UNSIGNED_BYTE, image1);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.REPEAT);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.REPEAT);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.generateMipmap(gl.TEXTURE_2D);
&#125;;
image1.src = "../../textures/container.jpg";
texture2 = gl.createTexture();
initTexture(gl, texture2);
const image2 = new Image();
image2.onload = function () &#123;
    gl.bindTexture(gl.TEXTURE_2D, texture2);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image2);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.REPEAT);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.REPEAT);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.generateMipmap(gl.TEXTURE_2D);
&#125;;
image2.src = "../../textures/awesomeface.png";
ourShader.use(gl);
ourShader.setInt(gl, "texture1", 0);
ourShader.setInt(gl, "texture2", 1);
requestAnimationFrame(render);
function initTexture(gl, texture) &#123;
    gl.bindTexture(gl.TEXTURE_2D, texture);
    const width = 1;
    const height = 1;
    const pixel = new Uint8Array([0, 0, 255]);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB, width, height, 0, gl.RGB, gl.UNSIGNED_BYTE, pixel);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>activeTexture bindTexture</li>
<li>getUniformLocation uniformMatrix4fv</li>
<li>bindVertexArray</li>
</ul>
<pre><code class="copyable">function render() &#123;
    processInput();
    gl.clearColor(0.2, 0.3, 0.3, 1.0);
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.activeTexture(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, texture1);
    gl.activeTexture(gl.TEXTURE1);
    gl.bindTexture(gl.TEXTURE_2D, texture2);
    let transform = mat4.create();
    mat4.translate(transform, transform, vec3.fromValues(0.5, -0.5, 0.0));
    mat4.rotateZ(transform, transform, performance.now() / 1000);
    ourShader.use(gl);
    let transformLoc = gl.getUniformLocation(ourShader.programId, "transform");
    gl.uniformMatrix4fv(transformLoc, false, transform);
    gl.bindVertexArray(VAO);
    gl.drawElements(gl.TRIANGLES, 6, gl.UNSIGNED_SHORT, 0);
    requestAnimationFrame(render);
&#125;
function processInput() &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            