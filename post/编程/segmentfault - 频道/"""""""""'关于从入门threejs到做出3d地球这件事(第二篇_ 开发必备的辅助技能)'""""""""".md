
---
title: """""""""'关于从入门three.js到做出3d地球这件事(第二篇_ 开发必备的辅助技能)'"""""""""
categories: 
    - 编程
    - segmentfault - 频道
author: segmentfault - 频道
comments: false
date: 2021-03-22 04:44:36
thumbnail: 'https://segmentfault.com/img/bVcQzEW'
---

<div>   
<h2>关于从入门three.js到做出3d地球这件事(第二篇: 开发必备的辅助技能)</h2><h3>本篇介绍</h3><p>     开发<code>3d</code>效果的时候, 不能每次都通过刷新页面来更新图像, 我们工程师当然会发明出相应的工具辅助开发工作, 这一篇我们一起学习三个好用的工具, 让我们的开发更畅快。</p><p>     上篇我们讲解了<code>three.js</code>的基本配置代码, 想看的同学可以访问这个链接: <a href="https://segmentfault.com/a/1190000039647481">关于从入门three.js到做出3d地球这件事(第一篇: 通俗易懂的入门)</a></p><h3>一. 相机的配置</h3><ul><li><strong>这里介绍的是<code>透视相机</code></strong></li></ul><p>     介绍工具之前我们先把相机的关键概念系统的学一遍, 因为以后我们要利用相机做很多有趣的事。<br>     这里以上一篇绘制的最基本的坐标系为例进行说明, 如下图:<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQzEW" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><h6>第一: <code>position</code> 相机位置</h6><p>     位置属性很重要很常用, 不同的位置呈现出不同的景色, 我们可以把相机理解为我们在3d世界中的眼睛, 而调整相机的位置就相当于我们走到不同的角度去看这个3d世界。<br>     看过上一篇你会知道我们的相机实例叫<code>camera</code>, 我们对他的<code>position</code>属性进行设置就可以调整位置。</p><ul><li><strong>第一种设置方式</strong></li></ul><pre><code>    camera.position.x = 2;
    camera.position.y = 2;
    camera.position.z = 10;</code></pre><p>上面就是分别调节了相机的x, y, z轴的距离, 我们看到的景象变成了下面的样子。<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQzFn" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><ul><li><strong>第二种设置方式</strong></li></ul><p>     <code>position</code>身上有<code>set</code>方法可以设置, 三个参数对应的是x, y, z。</p><pre><code>camera.position.set(2, 2, 10)</code></pre><p>     效果与上面的一样。</p><ul><li><strong>第三种设置方式</strong></li></ul><p>     <code>position</code>可以直接设置x, y, z属性, 本身又有<code>set</code>方法, 那么<code>position</code>属性本身到底是个什么那? 让我们打印出来看看。<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQzFv" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span><br><code>isVector3: true</code>也就是说它是一个<code>Vector</code>实例, 那么<code>Vector</code>是什么?<br>我们以后会经常和这个单词打交道, 让我们一起记住它。<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQBFg" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><ul><li><strong>先不细聊向量</strong></li></ul><p>因为<code>向量</code>是个很重要的概念, 我们后面会单独大篇幅的详谈, 这里咱们单纯的理解为<code>new THREE.Vector3(2, 2, 10)</code>是生成了一个<code>点</code>, 参数就是这个点的xyz坐标, 而我们相机的position属性就是这样一个对象。</p><ul><li><strong>注意: 直接赋值是无效的</strong></li></ul><p><code>camera.position = new THREE.Vector3(2, 2, 10)</code> 无效</p><p>需要利用add方法来实现<br><code>camera.position.add(new THREE.Vector3(2, 2, 10))</code> 有效</p><ul><li><strong>别被唬住</strong></li></ul><p>上面展示了大部分常用的设置<code>position</code>的方法, 我在初学<code>three.js</code>的时候被网上各种写法弄晕了所以这里特意列出大部分写法, 希望当你再看其它资料的时候就不会被乱七八糟的写法唬住了。</p><h6>第二: <code>lookAt</code> 相机看向哪里</h6><p>     这个概念简直太重要了, 如其字面意思就是看向哪里, 上面相机位置已经调整完毕, 那么我们要调整相机拍摄哪里了。</p><p>默认是(0,0,0)的位置如下图:<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQBGR" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>当我们看向坐标系的 (3, 3, 0)位置也就是右上角:<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQBG0" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>     从它的效果我们可以发现, 这个属性非常适合在3d游戏中调整人物的方向时改变图像, 如果你要做<code>第一人称游戏</code>一个人在城市里奔跑的效果, 那无非就是不断的改变相机的<code>position</code>与<code>lookAt</code>就能做到了。</p><ul><li><strong>设置方式</strong></li></ul><p>这里可以直接设置: <code>camera.lookAt(3, 3, 0)</code>;<br>还可以利用<code>向量</code>来设置: <code>camera.lookAt(new THREE.Vector3(3, 3, 0))</code>;</p><h6>第三: <code>up</code> 谁为相机上方</h6><p>先来一张默认的情况, 不难看出绿的是y, 红的是x, z正对着我们所以暂时看不到:<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQBId" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>我们设置一下<code>camera.up.set(1, 0, 0);</code><br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQBIv" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>上面x的值成为了最大, 所以他变成了<code>上方</code>的坐标轴, 当然如我们设一个乱乱的值<code>camera.up.set(1, 0.5, 0);</code> 那么效果如下:<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQBIA" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>这个属性的设置方式就是<code>set</code>方法或者<code>camera.up = new THREE.Vector3(1, 0.5, 0)</code>;</p><p>可以利用这个属性模拟<code>第一人称</code>游戏里任务摔倒了看这个世界....</p><h6>坑点</h6><p>我当前版本的<code>three.js</code>想要up属性生效需要在设置完up属性之后再主动指定一下<code>camera.lookAt(0, 0, 0);</code>否则up属性不生效;</p><h3>二. GUI的使用</h3><p>     上面讲了这么多, 我们现在想让场景动起来, 所以需要不断的渲染出3d图像, 我们利用<code>requestAnimationFrame</code>反复调用渲染函数就能实现动画效果了。</p><pre><code>const animate = function () &#123;
        requestAnimationFrame(animate);
        renderer.render(scene, camera);
    &#125;;
animate();</code></pre><p>-<strong>全名dat.gui.js</strong><br>他的功能是为属性生成一个可调节值的面板, 方便我们不断修改数值而不用刷新页面如下图:<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQBJP" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span><br>鼠标拖动调节<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQDRU" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039683114" alt="image" title="image" referrerpolicy="no-referrer"></span><br>-<strong>引入GUI</strong><br><code><script src="https://cdn.bootcdn.net/ajax/libs/dat-gui/0.7.7/dat.gui.min.js"></script></code><br>引入之后我们全局多了一个<code>dat</code>属性。</p><pre><code>const gui = new dat.GUI();
// 1: 定义一个我们要改变的对象
const pames = &#123;
  x: 0
&#125;
// 2: 把这个值放入控制器
gui.add(pames, "x", 0, 5).name("x轴的距离")</code></pre><p>参数解答</p><ol><li>传入要改变的对象。</li><li>要改变这个对象身上的哪个属性。</li><li>最小值</li><li>最大值</li><li>.name('显示在调节栏的名称')</li></ol><p>在每次渲染的时候更新一下相机的x轴位置。</p><pre><code>const animate = function () &#123;
    camera.position.x = pames.x
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
&#125;
animate();</code></pre><p>知道上面这些就可以应付很多的场景了, 一个工具而已不用深究啦。</p><h6>全部代码</h6><pre><code><html>
    <script src="https://cdn.bootcdn.net/ajax/libs/three.js/r122/three.min.js"></script>
    <script src="https://cdn.bootcdn.net/ajax/libs/dat-gui/0.7.7/dat.gui.min.js"></script>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(35, window.innerWidth / window.innerHeight, 1, 1000);
        camera.position.z = 20;
        const renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setClearColor(0x00FFFF, .5);
        document.body.appendChild(renderer.domElement);
        const axisHelper = new THREE.AxisHelper(2)
        scene.add(axisHelper)
        const pames = &#123;
            x: 0
        &#125;
        function createUI() &#123;
            var gui = new dat.GUI();
            gui.add(pames, "x", 0, 5).name("x轴的距离")
        &#125;
        const animate = function () &#123;
            camera.position.x = pames.x
            requestAnimationFrame(animate);
            renderer.render(scene, camera);
        &#125;
        createUI()
        animate();
    </script>
</body>
</html></code></pre><h3>三. tween的使用</h3><p>     <code>tween.js</code>是用来做流畅动画的库, 比我们自己写动画方便多了<a href="http://www.createjs.cc/tweenjs/docs/classes/Ticker.html" rel="nofollow">tween官网地址</a>。</p><p>下面编写了一个相机平滑的向右上角移动的代码。</p><pre><code>const tween = new TWEEN.Tween(camera.position).to(&#123;
    x: 10,
    y: 10
&#125;, 2000).repeat(Infinity).start();

 // tween.stop() // 可以停止动画
 
const animate = function () &#123;
    TWEEN.update();
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
&#125;
animate();</code></pre><ol><li><code>new TWEEN.Tween("这里传入要改变的对象")</code>。</li><li><code>.to( x: 10 y: 10&#125;, 2000)</code>, 在2000毫秒时将x与y属性变成10。</li><li><code>.repeat(Infinity)</code>, 这个动无限循环。</li><li><code>.start();</code>, 开始执行动画。</li><li><code>.stop();</code>, 停止动画。</li><li><code>TWEEN.update();</code>, 每次调用渲染函数都要调用一下动画的更新函数。</li></ol><p>效果如下(思否暂时无法传gif图片, 但我已经向高老板反应了):<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQEoJ" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span><br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQEoM" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>下面是动图, 显示可能有问题。<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039683115" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p>这个库大概的原理就是每次调用<code>update</code>方法的时候判断一下该动画已经执行了多久时间, 然后算出当前时间<code>目标对象</code>的值应该变为多少, 当然它还会对性能有所优化。</p><h6>全部代码如下:</h6><pre><code><html>
<style>
    * &#123;
        padding: 0;
        margin: 0;
    &#125;
</style>

<body>
    <script src="https://cdn.bootcdn.net/ajax/libs/three.js/r122/three.min.js"></script>
    <script src="https://cdn.bootcdn.net/ajax/libs/tween.js/18.6.4/tween.umd.js"></script>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(35, window.innerWidth / window.innerHeight, 1, 1000);
        camera.position.z = 20;
        const renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setClearColor(0x00FFFF, .5);
        document.body.appendChild(renderer.domElement);
        const axisHelper = new THREE.AxisHelper(2)
        scene.add(axisHelper)

        const tween = new TWEEN.Tween(camera.position).to(&#123;
            x: 10,
            y: 10
        &#125;, 2000).repeat(Infinity).start()
        const animate = function () &#123;
            TWEEN.update()
            requestAnimationFrame(animate);
            renderer.render(scene, camera);
        &#125;
        animate();
    </script>
</body>

</html></code></pre><h3>四. 轨道控制器的使用</h3><p>     这个就厉害了, 让我们可以使用鼠标转动我们的相机, 仿若进入到3d世界一般。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039683113" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p>随着我们按住鼠标并且移动, 视角就随之变化仿佛身临其境一般。</p><pre><code>// 将轨道控制器的代码放在对应的文件夹里面, 如果你没找到就用下面我分享的文件。
<script src="./utils/OrbitControls.js"></script></code></pre><p>引入成功页面THREE身上会出现<code>OrbitControls</code>方法, 我们需要传入<code>相机</code>与渲染的容器。</p><pre><code>  const orbitControls = new THREE.OrbitControls(camera, renderer.domElement);
  orbitControls.target = new THREE.Vector3(0, 0, 0);//控制焦点</code></pre><p>     cdn上我没查到, 想要获取代码的同学可以复制我的笔记内容到项目中 <a href="https://segmentfault.com/n/1330000039676837">three.js轨道控制器</a></p><h6>直接在页面引入与通过npm包的方式引入有区别, 到了讲在vue里的使用的时候我们再详细说。</h6><h6>全部代码如下: (要有<code>./utils/OrbitControls.js</code>的代码, 没有的话来我笔记下载)</h6><pre><code><html>

<body>
    <script src="https://cdn.bootcdn.net/ajax/libs/three.js/r122/three.min.js"></script>
    <script src="./utils/OrbitControls.js"></script>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(35, window.innerWidth / window.innerHeight, 1, 1000);
        camera.position.z = 10;
        const renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setClearColor(0x00FFFF, .5)
        // 轨道控制器
        orbitControls = new THREE.OrbitControls(camera, renderer.domElement);
        // orbitControls.target = new THREE.Vector3(0, 0, 0);
        // 轨道控制器
        document.body.appendChild(renderer.domElement);
        const axisHelper = new THREE.AxisHelper(2)
        scene.add(axisHelper)
        var animate = function () &#123;
            requestAnimationFrame(animate);
            renderer.render(scene, camera);
        &#125;;
        animate();
    </script>
</body>

</html></code></pre><h3>end.</h3><p>下一篇将会介绍 <code>光源</code>, 与 <code>阴影</code>的玩法了, 希望与你一起进步。</p>  
</div>
            