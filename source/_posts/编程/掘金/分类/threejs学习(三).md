
---
title: 'three.js学习(三)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7579'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 01:37:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=7579'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>第三天:</p>
<p>关于让自己创建的3D模型动起来的一些基础知识，毕竟动起来才会显得逼格很高，动的更快，更炫酷岂不是求职利器</p>
<p>每执行一次渲染器对象的<strong>render()方法</strong>，浏览器就会通过CPU把相关的图形数据发送到GPU和显存，然后渲染出一帧图像，这就是说你按照一定的周期调用该方法就可以不停地生成新的图像覆盖原来的图像， 这时要注意我为了产生立方体的旋转动画效果，每执行一次render()渲染方法，要把立方体绕一个坐标轴旋转一定的角度，立方体不停地旋转，相机不停地拍照自然就会形成动画的效果。</p>
<pre><code class="copyable">      function render() &#123;
          renderer.render(scene,camera);//执行渲染操作
          spereMesh.rotateY(0.01);//立方体每次绕y轴旋转0.01弧度
          boxMesh.rotateY(0.01);//球体每次绕y轴旋转0.01弧度
          requestAnimationFrame(render);//请求再次执行渲染函数render
      &#125;
      render();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里用到了一个用于动画的方法<strong>requestAnimationFrame()</strong>，该方法属于浏览器的window对象可以直接调用，参数是将要被调用函数的函数名，该方法调用函数不是立即调用而是向浏览器发起一个执行某函数的请求， 什么事会执行由浏览器决定，一般默认保持60FPS的频率，就是肉眼所见不会卡顿的一个频率</p>
<p>实际动画过程中会出现不均匀旋转的情况，这时候就需要用到时间戳来控制(当然代码是我复制来的，实际中出现不均匀情况就来复制代码吧)：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> T0 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();<span class="hljs-comment">//上次时间</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">let</span> T1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();<span class="hljs-comment">//本次时间</span>
        <span class="hljs-keyword">let</span> t = T1-T0;<span class="hljs-comment">//时间差</span>
        T0 = T1;<span class="hljs-comment">//把本次时间赋值给上次时间</span>
        requestAnimationFrame(render);
        renderer.render(scene,camera);<span class="hljs-comment">//执行渲染操作</span>
        mesh.rotateY(<span class="hljs-number">0.001</span>*t);<span class="hljs-comment">//旋转角速度0.001弧度每毫秒</span>
    &#125;
render();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就先写到旋转，下一篇就写如何用鼠标操作3D模型图</p></div>  
</div>
            