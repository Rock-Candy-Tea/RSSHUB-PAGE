
---
title: 'three.js--camera-相机知识学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bec20748c9db456db600ea752fc05a9e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 23:33:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bec20748c9db456db600ea752fc05a9e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1 相机类的关系</h1>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
Object3D --> Camera
Camera --> PerspectiveCamera
Camera --> OrthographicCamera
</code></pre>
<h3 data-id="heading-1">常用设置api</h3>
<pre><code class="copyable">camera.position() 设置相机所在的位置
camera.up() 设置相机的方向，改变方向，产生相机旋转； default: (0,1,0) 
camera.lookat() 相机看向的位置
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于相机与世界坐标以及相机各个参数之间的关系，我是这样理解的：举个例子来说，我们要用手机拍一个物体，比如香蕉，那么我们会怎么做？首先是不是得把手机拿起来放到某个位置上去，你得拿你的手固定住手机才能拍出照片，对吧，这就对应是camera的三个position属性(位置)。其次，当你把手机放到那个位置上后，你要拍到香蕉，你是不是得把手机对准那个香蕉，不然你手机虽然在那个位置，但你向上，向下随便翻动手机，可能会拍到香蕉吗？当然不会，所以对准香蕉这个操作就对应camera的 looAt() 操作。最后，你手机也摆好了，香蕉也对准了，但你是不是还得考虑到底是横着拍还是竖着拍，或者斜着拍？因为你手机横着或者竖着拍出来的香蕉是不同的，所以你手机到底是横着还是竖着对应的就是camera的up属性，这个up指的就是你手机向上的方向。当这三个因素被确定下来后，相机才能够被确定，从而拍出确定的照片，“确定”这个条件对计算机是非常重要的，因为不确定的东西对计算机来说是无法被理解的，所以也就不可能被计算机呈现。参考链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_43379478%2Farticle%2Fdetails%2F83830613" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_43379478/article/details/83830613" ref="nofollow noopener noreferrer">blog.csdn.net/weixin_4337…</a></p>
<h1 data-id="heading-2">2 PerspectiveCamera 透视相机</h1>
<pre><code class="copyable">使用场景：模拟人眼看到的场景--近大远小
var camera = new THREE.PerspectiveCamera( 45, width / height, 1, 1000 ); 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">PerspectiveCamera( fov : Number, aspect : Number, near : Number, far : Number )</h3>
<pre><code class="copyable">fov — 摄像机视锥体垂直视野角度\ default:50
aspect — 摄像机视锥体长宽比\ default:1 -> 通常使用画布的宽/画布的高
near — 摄像机视锥体近端面\   default:0.1
far — 摄像机视锥体远端面     default:2000
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">3 OrthographicCamera 正交相机</h1>
<pre><code class="copyable">使用场景：渲染2D场景或者UI元素， 保持渲染物体的大小不变
var camera = new THREE.OrthographicCamera( width / - 2, width / 2, height / 2, height / - 2, 1, 1000 );
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">OrthographicCamera( left : Number, right : Number, top : Number, bottom : Number, near : Number, far : Number )</h3>
<pre><code class="copyable">left — 摄像机视锥体左侧面。\
right — 摄像机视锥体右侧面。\
top — 摄像机视锥体上侧面。\
bottom — 摄像机视锥体下侧面。\
near — 摄像机视锥体近端面。\    default:0.1
far — 摄像机视锥体远端面。      default:2000
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">4 视锥体</h1>
<p><strong>视锥</strong>指的是一个实体形状，看起来像是一个顶部被平行于地基切除的金字塔
实验有助于解释这个情况的成因。<br>
想象拿着一根直棍子（比如扫帚把手或者铅笔）的一端对着相机并拍照。如果棍子正对着照片的中心，垂直于相机镜片，那么相机上只会看到一个圆；除了棍子的断点其它部分会被遮挡。如果将棍子向上移，慢慢能看见棍子的远端，但是将棍子向上翘起又会将远端隐藏起来。继续向上移动并向上调整棍子角度，圆形的断电最终会到达照片的边缘。在这个点上，现实世界中所有在棍子所在线上方的物体在照片中都不会出现。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bec20748c9db456db600ea752fc05a9e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="alt text" loading="lazy" referrerpolicy="no-referrer"><br>
棍子也可以简单的像左、右、下或者水平垂直移动的任意组合。相应调整棍子的角度都可以将棍子在相机中隐藏起来。<br>
这个思考实验的意义在于，相机图片中的任何一个点最终对应于现实世界中的一条线，并且只会显示这条线上的一个点，这条线上所有在这个显示的点后面的物体都会被遮挡。图片的外边界由四个顶点对应的发散线定义。这四条线最终相交于相机位置所在的点。Unity中这个点就是相机的transform位置，被称为透视视图的中心。屏幕顶部和底部中心点汇集到透视视图中心点的连线形成的角度被称为视野（field of view FOV）。<br>
如上面介绍的，所有落在照片边界对应的发散线以外的事物在相机上是不可见的，同时还有两外两个限制。远近裁切平面平行于相机的XY平面，分别在相机的中心线上设置了一个确定的距离。所有于相机的距离小于近平面的距离或者大于远平面的距离的物体都不会被渲染。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f22780f2bbf4c428d449475377b370e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="ViewFrustum.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图片定点对应的发射线和两个裁切平面一起定义了一个截断的金字塔，也就是视锥。</p>
<p>参考链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fasasqwqw1212%2Farticle%2Fdetails%2F79364938" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/asasqwqw1212/article/details/79364938" ref="nofollow noopener noreferrer">blog.csdn.net/asasqwqw121…</a></p>
<p>以上仅为记录个人学习理解。</p></div>  
</div>
            