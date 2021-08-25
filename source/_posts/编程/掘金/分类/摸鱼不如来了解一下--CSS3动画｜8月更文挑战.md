
---
title: '摸鱼不如来了解一下--CSS3动画｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c316e54d37e4a79aaa92bec31d60d78~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 18:52:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c316e54d37e4a79aaa92bec31d60d78~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与8月更文挑战的第23天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>”</p>
<h1 data-id="heading-0">CSS动画</h1>
<h2 data-id="heading-1">制作动画分两步(相当于类选择器，先定义好样式，再通过类名调用)</h2>
<p>●   1.定义动画</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c316e54d37e4a79aaa92bec31d60d78~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>●   keyframes意为关键帧。动画序列0%~100%也可以写成from···和to···。此外，动画序列不仅只能设置两个状态，可以实现多个状态变化，如：0%~25%~50%~75%~100%，这里的百分比是对总时间的划分</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59c3c5d5ef204665abff221407f2cea3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98eeefb2cbb24f62b29b73a65e7f7dee~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>●   2.使用(调用)动画</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99e3be9785da46089605a16c85a7f6b0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">动画的常见属性</h2>
<h3 data-id="heading-3"><strong>animation-name</strong> <strong>规定动画的名称(必须)</strong></h3>
<h3 data-id="heading-4"><strong>animation-duration</strong> <strong>规定动画完成一个周期的时间(秒/毫秒)(必须)</strong></h3>
<h3 data-id="heading-5">animation-timing-function规定动画的速度曲线，默认值为ease</h3>
<blockquote>
<p>●   ease低速开始，然后加快，结束时变慢</p>
<p>●   linear匀速</p>
<p>●   ease-in低速开始</p>
<p>●   ease-out低速结束</p>
<p>●   ease-in-out低速开始和结束</p>
<p>●   <strong>steps()</strong> <strong>指定时间函数中的间隔数量(步长)</strong></p>
<p>●   如设置steps(5)，则动画将分5部完成</p>
</blockquote>
<p>●   animation-delay规定动画何时开始，默认为0</p>
<p>●   <strong>animation-iteration-count</strong> <strong>规定动画的重复次数，默认为1，设置为infinite则无限循环</strong></p>
<p>●   animation-direction规定动画是否反方向播放，默认为normal，设置为alternate则逆向播放</p>
<p>●   animation-fill-mode规定动画结束后的状态，默认为backwards回到初始状态，设置为forwards则保持在结束状态</p>
<p>●   <strong>animation-play-state</strong> <strong>规定动画是否正在进行或者暂停，默认是running。若设置paused，则动画停止不动，可以配合:hover来设置鼠标悬浮则停止</strong></p>
<p>●   <strong>动画属性的简写-->animation: 动画名称 持续时间 运动曲线 何时开始播放次数 是否反方向 是否保持结束的状态</strong></p>
<p>●   例：animation: move 1s linear 0s 1 alternate forwards</p>
<p>●   <strong>这其中动画名称和持续时间是必须写的属性，其他的可以保持默认</strong></p>
<h1 data-id="heading-6">3D转换</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b784592b6084fbbb132dc06be066715~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da8ad2492f7c4a69967743a8c26ce2f8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">3D位移translate3d(x,y,z)，也可以对应坐标轴设置transform: translateX() translateY() translateZ(); 注意每个方向用空格隔开，但是不能分开单独写三个transform，以为后写的会覆盖前面的</h2>
<p>●   <strong>注意：z轴的位移是看不到的，要加入透视perspective属性才能看到</strong></p>
<h2 data-id="heading-8">3D旋转rotate3d(x,y,z,旋转角度)，可以让元素在三维平面内沿着x轴、y轴、z轴或者自定义轴来旋转。<strong>x,y,z是旋转轴的矢量，表示是否沿着这条轴旋转(如 transform: rotate3d(1,0,0,45deg)表示沿着x轴旋转45度; transform: rotate3d(1,1,0,45deg)表示沿着对角线旋转45度)</strong></h2>
<p>    
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58667a1b298441228dcd496b6512e3e3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://juejin.cn/post/6999823925869805582" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0de28a0421034ba9886b0b11fd0859a6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
●   判断元素沿x轴旋转时的正方向</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d39f33d1e7364e49a4fd7476611a230b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>●   判断元素沿y轴旋转时的正方向</p>
<p><img src="https://juejin.cn/post/6999823925869805582" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/540e0302942d422f9b38ad28ada9a954~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">透视perspective(单位为px)，也叫视距，<strong>加了透视的页面元素在变化时就会呈现立体感(非常中要)</strong></h3>
<blockquote>
<p>●   <strong>注意：透视要写在被观察元素的父盒子上面(通常写在body里)</strong></p>
<p>●   <strong>透视是模拟人的眼睛，有近大远小的效果。当透视(视距)越小，元素到人眼的距离越小(越近)，看到的元素就越大；视距越大，元素到人眼的距离越大(越远)，看到的元素就越小。</strong></p>
<p>●   当视距固定时，元素向z轴正向移动，就越来越大；元素向z轴负方向移动就越来越小</p>
</blockquote>
<h3 data-id="heading-10"><strong>3D</strong> <strong>呈现transform-style(非常重要)</strong></h3>
<h4 data-id="heading-11">控制子元素是否开启三维立体环境</h4>
<blockquote>
<p>●   transform-style: flat; 默认值，不开启三维立体环境</p>
<p>●   transform-style: preserve-3d;开启子元素三维立体环境</p>
<p>●   <strong>注意：transform-style属性要写在父盒子内，影响的是子元素</strong></p>
</blockquote>
<h4 data-id="heading-12"><strong>做3D时，透视perspective和3D呈现transform-style: preserve-3d;必不可少！！！</strong></h4>
<p><strong>注意！！！只要是写transform属性不管是2D还是3D，在同一个元素上使用时一定要用简写！如: transform: translate(x,y) rotate3d(x,y,z,deg);同时实现两种变化，不能拆开写两个transform，这样后面的transform会覆盖前面的，导致前面的失效</strong></p></div>  
</div>
            