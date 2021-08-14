
---
title: 'OpenGL入门基础(二)--图形渲染管线（Graphics Pipeline）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b10c683a6a10413fa30f8f6110152091~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 00:02:21 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b10c683a6a10413fa30f8f6110152091~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在OpenGL中，任何事物都在3D空间中，而屏幕和窗口却是2D像素数组，这导致OpenGL的大部分工作都是关于把3D坐标转变为适应你屏幕的2D像素。3D坐标转为2D坐标的处理过程是<code>由OpenGL的图形渲染管线</code>管理的。</p>
<h2 data-id="heading-0">学习目标：</h2>
<ul>
<li>图形渲染管线基础知识；</li>
<li>图形渲染管线的工作流程;</li>
</ul>
<hr>
<h5 data-id="heading-1">图形渲染管线基础知识</h5>
<p>在OpenGL中,任何事物都在3D空间中，而屏幕和窗口等都是2D像素组，所以需要进行转换。</p>
<ul>
<li>
<p>概念：</p>
<ul>
<li>一堆原始图形数据途经<code>一个输送管道</code>，期间经过各种变化处理 最终出现在屏幕的过程.</li>
<li>（图形渲染管线接受一组3D坐标，然后把它们转变为你屏幕上的有色2D像素输出。）</li>
</ul>
</li>
<li>
<p>图形渲染管线主要有两方面工作：</p>
<ul>
<li>把3D坐标转换为2D坐标;</li>
<li>把2D坐标转变为实际的有颜色的像素;</li>
</ul>
</li>
</ul>
<hr>
<h5 data-id="heading-2">图形渲染管线的工作流程</h5>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b10c683a6a10413fa30f8f6110152091~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>图形渲染管线的主要流程分为<code>6</code>大步骤：
<ol>
<li>顶点输入</li>
<li>顶点着色器</li>
<li>编译着色器</li>
<li>片段着色器</li>
<li>链接顶点属性</li>
<li>索引缓冲对象</li>
</ol>
</li>
</ul>
<p>接下来我们一起一一学习里面具体的步骤，并且了解每一步骤主要职能。</p>
<ul>
<li>顶点输入</li>
</ul>
<ol>
<li>
<p>定义<code>顶点数据 (vertext data)</code>（3D坐标），将顶点数据坐标进行<code>标准化设备坐标(有效范围内 --OpenGL的可见区域)</code>；</p>
<ul>
<li>标准化设备坐标（Normalized Device Coordnates,NDC）
<ul>
<li>任何坐落在范围外的坐标都会被丢弃/裁剪，不会显示在屏幕上。</li>
<li>标准化设备坐标接着会变换为屏幕空间坐标（Screen -space Coordinates）-- [通过glViewport函数提供的数据，进行视口变换（viewport transform）完成的]</li>
</ul>
</li>
</ul>
</li>
<li>
<p>将<code>顶点数据</code>作为输入发送给图形渲染管线的第一个处理阶段:顶点着色器。</p>
</li>
<li>
<p>把顶点数据 存储在显卡内存中，使用VBO（顶点缓冲对象）管理。</p>
<ul>
<li>使用顶点缓冲对象管理内存的原因是一次性可以发送大量数据到显卡上。</li>
<li>顶点缓冲对象（vertex buffer objects，VBO）管理内存-- 在GPU中存储大量的顶点数据。</li>
</ul>
<ul>
<li>
<p>顶点缓冲对象的创建步骤：</p>
<ol>
<li>创建VBO对象;glGenBuffer()</li>
<li>将VBO对象绑定到顶点缓冲对象中; glBindBuffer()</li>
<li>将用户输入的顶点数据复制到缓冲内存中; glBufferData()</li>
</ol>
<ul>
<li>要点：
<ul>
<li>
<p>OpenGL有很多缓冲对象类型，其中顶点缓冲对象类型是GL_ARRAY_BUFFER</p>
</li>
<li>
<p>glBufferData函数--把顶点数据(用户定义的数据) 复制到 缓冲的内存 中。</p>
</li>
<li>
<p>glBufferData：第四个参数，指名显卡如何管理给定的数据：</p>
<ol>
<li>GL_STATIC_DRAW:数据不会或者几乎不变;</li>
<li>GL_DYNAMIC_DRAW:数据会被改变多次;</li>
<li>GL_STREAM_DRAW：数据每次绘制时都会改变;</li>
</ol>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">// 创建vbo对象</span>
<span class="hljs-keyword">unsigned</span> <span class="hljs-keyword">int</span> VBO;<span class="hljs-comment">//VBO对象id</span>
glGenBuffer(<span class="hljs-number">1</span>,&VBO);

<span class="hljs-comment">//把新创建的缓冲 绑定到GL_ARRAY_BUFFER目标上</span>
<span class="hljs-comment">//GL_ARRAY_BUFFER--顶点缓冲对象的缓冲类型</span>
glBindBuffer(GL_ARRAY_BUFFER,VBO);

<span class="hljs-comment">//配置 当前绑定的缓冲(VBO) --调用glBufferData函数 </span>
glBufferData(GL_ARRAY_BUFFER,<span class="hljs-keyword">sizeof</span>(vertices),vertices,GL_STATIC_DRAW)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ol>
<ul>
<li>顶点着色器
<ul>
<li>
<p>在现代OpenGL中至少需要设置一个顶点和一个片段着色器。</p>
</li>
<li>
<p>使用GLSL（OpenGL Shading Language）编写顶点着色器，然后编译这个着色器，最后在程序中使用。</p>
</li>
</ul>
</li>
</ul>
<hr>
<pre><code class="copyable">- 创建顶点着色器
    ```c
    #version 330 core
    layout (location=0) in vec 3 aPos;
    void main()&#123;
        gl_Position=vec4(aPos.x,aPos.y,aPos.z,1.0)
    &#125;
    ```

    1. 着色器版本 OpenGL 3.3以及更高版本，使用核心模式。
    2. in关键字 --代表输入顶点属性(Input Vertex Attribute),数据位置location ( layout (location=0) ),使用vec3 三维浮点向量。
    3. 设置顶点着色器的输出；

- 编译着色器
```js
const char *vertexShaderSource = "#version 330 core\n" "layout (location = 0) in vec3 aPos;\n" "void main()\n" "&#123;\n" " gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);\n" "&#125;\0";
```
为了使用OpenGL使用它，必须在 运行时动态编译它的源代码。

- 编译步骤：
    1. 创建着色器对象，使用ID来引用； 
        -- glCreateShader(GL_VERTEX_SHADER);
    2. 把着色器源码 附加到这个着色器对象中；
        -- glShadderSource();
    3. 编译着色器
        -- glCompileShader(vertexShader);
    4. 检测编译状态 -- glGetShaderiv() 
      ```c
      unsigned int vertexShader;
      vertexShader=glClreateShader(GL_VERTEX_SHADER);

      glShaderSource(vertexShader,1,&vertexShader,NULL);

      glCompileShader(vertexShader);

        //检测编译着色器状态 --是否编译成功
        int  success;
        char infoLog[512];
        glGetShaderiv(vertexShader, GL_COMPILE_STATUS, &success);

        //如果编译失败 
        if(!success)
        &#123;
            glGetShaderInfoLog(vertexShader, 512, NULL, infoLog);
            std::cout << "ERROR::SHADER::VERTEX::COMPILATION_FAILED\n" << infoLog << std::endl;
        &#125;
      ```
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>片段着色器（Fragment Shader）
<ul>
<li>计算像素最后的颜色输出。</li>
<li>在计算机图形中颜色被表示为有4个元素的数组：红色、绿色、蓝色和alpha(透明度)分量，通常缩写为RGBA。当在OpenGL或GLSL中定义一个颜色的时候，我们把颜色每个分量的强度设置在0.0到1.0之间</li>
<li>三种颜色分量的不同调配可以生成超过1600万种不同的颜色！</li>
</ul>
创建步骤：
<ol>
<li>创建片段着色器源码</li>
</ol>
<pre><code class="hljs language-c copyable" lang="c">     <span class="hljs-meta">#version 330 core out vec4 FragColor; </span>
     <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">()</span> 
     </span>&#123; 
         FragColor = vec4(<span class="hljs-number">1.0f</span>, <span class="hljs-number">0.5f</span>, <span class="hljs-number">0.2f</span>, <span class="hljs-number">1.0f</span>); 
     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>编译片段着色器</li>
</ol>
<pre><code class="hljs language-c copyable" lang="c">   <span class="hljs-keyword">unsigned</span> <span class="hljs-keyword">int</span> fragmentShader;
   fragmentShader = glCreateShader(GL_FRAGMENT_SHADER); 
   glShaderSource(fragmentShader, <span class="hljs-number">1</span>, &fragmentShaderSource, <span class="hljs-literal">NULL</span>); 
   glCompileShader(fragmentShader);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-3">图形学基础目录</h4>
<ol>
<li><a href="https://juejin.cn/post/6995570312033075231" target="_blank" title="https://juejin.cn/post/6995570312033075231">OpenGL -- 入门笔记 (juejin.cn)</a></li>
<li><a href="https://juejin.cn/editor/drafts/6995775361334132744" target="_blank" title="https://juejin.cn/editor/drafts/6995775361334132744">OpenGL入门基础(二)--图形渲染管线</a></li>
</ol></div>  
</div>
            