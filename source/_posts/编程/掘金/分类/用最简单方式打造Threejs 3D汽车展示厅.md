
---
title: '用最简单方式打造Three.js 3D汽车展示厅'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad04db4a175f4f5b9c69db30854f3b5d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 22:15:47 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad04db4a175f4f5b9c69db30854f3b5d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>在上一篇文章简单粗略的描述了开发3D汽车展厅，笔者再写一篇比较详细的教程。对于笔者来说Three.js说难不难，说简单也不简单。说简单因为他简化了对三维知识的理解，简化了很多操作。说难是因为api很多，要用熟也不是一朝半夕的时间。笔者在这给大家介绍一下以最简单方式打造一个3D汽车展示厅。这个3D汽车展厅实现出来也不算完整，主要想让同学们找找感觉，找些成就感，有感觉自己也有学下去的动力。^_^</p>
<h2 data-id="heading-1">简单粗略了解三维</h2>
<p>在2D里只有两个坐标,分别是X轴，和Y轴。在3D就多了一个Z轴。相信刚学3D的同学对X轴和Y轴都比较熟悉，Z轴是比较陌生，笔者建议大家可以上<a href="https://link.juejin.cn/?target=https%3A%2F%2Fthreejs.org%2Feditor%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://threejs.org/editor/" ref="nofollow noopener noreferrer"> three编辑器</a>的网站尝试创建一些几何物体，找找对3D理解。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad04db4a175f4f5b9c69db30854f3b5d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">完整效果</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e429461d3024f4cbdc621470c97ef83~tplv-k3u1fbpfcp-watermark.image" alt="屏幕录制2021-07-08 下午1.39.03.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">需要了解这几个概念</h2>
<p>笔者用舞台表演来比如:</p>
<ol>
<li>场景 <code>Sence</code> 相当于在一个舞台，在这里是布置场景物品和表演者表演的地方</li>
<li>相机 <code>Carma</code> 相当于观众的眼睛去观看</li>
<li>几何体 <code>Geometry</code> 相当于舞台的表演者</li>
<li>灯光 <code>light</code> 相当于舞台灯光照射</li>
<li>控制 <code>Controls</code> 相当于这出舞台剧的总导演</li>
</ol>
<p>既然知道这几个概念，我们就根据这几大概念以函数形式区分，就很好理解。在这个three程序我分别创建了:
<code>setScene</code>、<code>setCarma</code>、 <code>loadfile</code>、<code>setLight</code>、<code>setControls</code>分别对应以上几个概念</p>
<h2 data-id="heading-4">创建场景</h2>
<p>首先我们还是用vue3的setup方式编写，npm安装three包， 引入 <code>Scene</code>，<code>WebGLRenderer</code> 两个对象，创建两个变量 <code>scene</code>、<code>renderer</code>并赋值，这样就简单搭建了一个场景，场景背景默认是黑色。创建一个<code>init</code>初始化函数，并在<code>onMounted</code>调用</p>
<pre><code class="hljs language-js copyable" lang="js"><script setup>
  <span class="hljs-keyword">import</span> &#123;onMounted&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
  <span class="hljs-keyword">import</span> &#123; Scene,WebGLRenderer,PerspectiveCamera&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three'</span>
  <span class="hljs-keyword">let</span> scene,renderer
  <span class="hljs-comment">//创建场景</span>
  <span class="hljs-keyword">const</span> setScene = <span class="hljs-function">()=></span>&#123;
        scene = <span class="hljs-keyword">new</span> Scene()
        renderer = <span class="hljs-keyword">new</span> WebGLRenderer()
        renderer.setSize(innerWidth, innerHeight)
        <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.boxs'</span>).appendChild(renderer.domElement)
    &#125;
   <span class="hljs-comment">//初始化所有函数 </span>
   <span class="hljs-keyword">const</span> init = <span class="hljs-function">() =></span> &#123;
        setScene()
    &#125;
    <span class="hljs-comment">//用vue钩子函数调用</span>
    onMounted(init)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">创建相机</h2>
<p>有了场景就要加相机，相机相当于人的眼睛去观察几何物体,引入<code>PerspectiveCamera</code>，
参数有4个，具体可以看看官网文档。然后通过实例方法<code>position.set</code>设置相机坐标</p>
<pre><code class="hljs language-js copyable" lang="js"><script setup>
  <span class="hljs-keyword">import</span> &#123; Scene,WebGLRenderer,PerspectiveCamera&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three'</span>
  <span class="hljs-keyword">let</span> scene,renderer,camera
  <span class="hljs-comment">//相机的默认坐标</span>
  <span class="hljs-keyword">const</span> defaultMap = &#123;
        <span class="hljs-attr">x</span>: <span class="hljs-number">510</span>,
        <span class="hljs-attr">y</span>: <span class="hljs-number">128</span>,
        <span class="hljs-attr">z</span>: <span class="hljs-number">0</span>,
    &#125;
  <span class="hljs-comment">//创建场景</span>
  <span class="hljs-keyword">const</span> setScene = <span class="hljs-function">()=></span>&#123;
        scene = <span class="hljs-keyword">new</span> Scene()
        renderer = <span class="hljs-keyword">new</span> WebGLRenderer()
        renderer.setSize(innerWidth, innerHeight)
        <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.boxs'</span>).appendChild(renderer.domElement)
    &#125;
  <span class="hljs-comment">//创建相机  </span>
  <span class="hljs-keyword">const</span> setCamera = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> &#123;x, y, z&#125; = defaultMap
        camera = <span class="hljs-keyword">new</span> PerspectiveCamera(<span class="hljs-number">60</span>, innerWidth / innerHeight, <span class="hljs-number">1</span>, <span class="hljs-number">1000</span>)
        camera.position.set(x, y, z)
    &#125;
   <span class="hljs-comment">//初始化所有函数 </span>
   <span class="hljs-keyword">const</span> init = <span class="hljs-function">() =></span> &#123;
        setScene()
        setCamera()
    &#125;
    <span class="hljs-comment">//用vue钩子函数调用</span>
    onMounted(init)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">引入特斯拉模型</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3f09a6cf48b4497940c2491b76e4f22~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在three我们除了可以通过api创建几何物体，还可以引入第三方3d模型，具体可以上<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsketchfab.com%2Ffeed" target="_blank" rel="nofollow noopener noreferrer" title="https://sketchfab.com/feed" ref="nofollow noopener noreferrer"> sketchfab </a>，国外一个3d模型下载网站，里面有很多免费的模型下载，这次用特斯拉汽车模型为例，下载一个<code>gltf</code>格式的3D模型。引入<code>GLTFLoader</code> 创建一个<code>loadfile</code>函数并通过Promise返回模型数据，在<code>init</code>函数加上<code>async</code>调用<code>loadfile</code>得到返回模型数据并添加到场景<code>scene</code></p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">import</span> &#123;GLTFLoader&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three/examples/jsm/loaders/GLTFLoader'</span>
  <span class="hljs-keyword">import</span> &#123; Scene,WebGLRenderer,PerspectiveCamera&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three'</span>
  <span class="hljs-keyword">let</span> scene,renderer,camera,directionalLight,dhelper
  <span class="hljs-keyword">let</span> isLoading = ref(<span class="hljs-literal">true</span>)
  <span class="hljs-keyword">let</span> loadingWidth = ref(<span class="hljs-number">0</span>)
  <span class="hljs-comment">//相机的默认坐标</span>
  <span class="hljs-keyword">const</span> defaultMap = &#123;
        <span class="hljs-attr">x</span>: <span class="hljs-number">510</span>,
        <span class="hljs-attr">y</span>: <span class="hljs-number">128</span>,
        <span class="hljs-attr">z</span>: <span class="hljs-number">0</span>,
    &#125;
  <span class="hljs-comment">//创建场景</span>
  <span class="hljs-keyword">const</span> setScene = <span class="hljs-function">()=></span>&#123;
        scene = <span class="hljs-keyword">new</span> Scene()
        renderer = <span class="hljs-keyword">new</span> WebGLRenderer()
        renderer.setSize(innerWidth, innerHeight)
        <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.boxs'</span>).appendChild(renderer.domElement)
    &#125;
  <span class="hljs-comment">//创建相机  </span>
  <span class="hljs-keyword">const</span> setCamera = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> &#123;x, y, z&#125; = defaultMap
        camera = <span class="hljs-keyword">new</span> PerspectiveCamera(<span class="hljs-number">60</span>, innerWidth / innerHeight, <span class="hljs-number">1</span>, <span class="hljs-number">1000</span>)
        camera.position.set(x, y, z)
    &#125;
    <span class="hljs-comment">//通过Promise处理一下loadfile函数</span>
     <span class="hljs-keyword">const</span> loadFile = <span class="hljs-function">(<span class="hljs-params">url</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>((<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            loader.load(url,
                <span class="hljs-function">(<span class="hljs-params">gltf</span>) =></span> &#123;
                    resolve(gltf)
                &#125;, <span class="hljs-function">(<span class="hljs-params">&#123;loaded, total&#125;</span>) =></span> &#123;
                    <span class="hljs-keyword">let</span> load = <span class="hljs-built_in">Math</span>.abs(loaded / total * <span class="hljs-number">100</span>)
                    loadingWidth.value = load
                    <span class="hljs-keyword">if</span> (load >= <span class="hljs-number">100</span>) &#123;
                        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                            isLoading.value = <span class="hljs-literal">false</span>
                        &#125;, <span class="hljs-number">1000</span>)
                    &#125;
                    <span class="hljs-built_in">console</span>.log((loaded / total * <span class="hljs-number">100</span>) + <span class="hljs-string">'% loaded'</span>)
                &#125;,
                <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
                    reject(err)
                &#125;
            )
        &#125;))
    &#125;
    
    <span class="hljs-comment">//初始化所有函数 </span>
   <span class="hljs-keyword">const</span> init = <span class="hljs-keyword">async</span>() => &#123;
        <span class="hljs-keyword">const</span> gltf =<span class="hljs-keyword">await</span> loadFile(<span class="hljs-string">'src/assets/3d/tesla_2018_model_3/scene.gltf'</span>)
        setScene()
        setCamera()
        scene.add(gltf.scene)
    &#125;
    <span class="hljs-comment">//用vue钩子函数调用</span>
    onMounted(init) 

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">创建灯光</h2>
<p>汽车模型还看不见，所以我们要给它设置灯光，引入<code>DirectionalLight</code>,<code>DirectionalLightHelper</code>,<code>HemisphereLight</code>,<code>HemisphereLightHelper</code>,并设置灯光的参数，使模型可见，并有些反射光面,阴影的效果，然后也在<code>init</code>函数调用 <code>setLight</code>，再增加<code>loop</code>函数，使场景、照相机、模型不停循环调用。然后车模型就能看见啦,看到车出现的那一刻，好像自己的新买的一样，^_^</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80818664b80641aab32ae95443e40d08~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">import</span> &#123;GLTFLoader&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three/examples/jsm/loaders/GLTFLoader'</span>
 <span class="hljs-keyword">import</span> &#123; Scene,WebGLRenderer,PerspectiveCamera,   DirectionalLight,
        DirectionalLightHelper,
        HemisphereLight,
        HemisphereLightHelper&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three'</span>
  <span class="hljs-keyword">let</span> scene,renderer,camera,directionalLight,hemisphereLight,dhelper,hHelper
  <span class="hljs-keyword">let</span> isLoading = ref(<span class="hljs-literal">true</span>)
  <span class="hljs-keyword">let</span> loadingWidth = ref(<span class="hljs-number">0</span>)
  <span class="hljs-comment">//相机的默认坐标</span>
  <span class="hljs-keyword">const</span> defaultMap = &#123;
        <span class="hljs-attr">x</span>: <span class="hljs-number">510</span>,
        <span class="hljs-attr">y</span>: <span class="hljs-number">128</span>,
        <span class="hljs-attr">z</span>: <span class="hljs-number">0</span>,
    &#125;
  <span class="hljs-comment">//创建场景</span>
  <span class="hljs-keyword">const</span> setScene = <span class="hljs-function">()=></span>&#123;
        scene = <span class="hljs-keyword">new</span> Scene()
        renderer = <span class="hljs-keyword">new</span> WebGLRenderer()
        renderer.setSize(innerWidth, innerHeight)
        <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.boxs'</span>).appendChild(renderer.domElement)
    &#125;
  <span class="hljs-comment">//创建相机  </span>
  <span class="hljs-keyword">const</span> setCamera = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> &#123;x, y, z&#125; = defaultMap
        camera = <span class="hljs-keyword">new</span> PerspectiveCamera(<span class="hljs-number">60</span>, innerWidth / innerHeight, <span class="hljs-number">1</span>, <span class="hljs-number">1000</span>)
        camera.position.set(x, y, z)
    &#125;
    <span class="hljs-comment">//通过Promise处理一下loadfile函数</span>
     <span class="hljs-keyword">const</span> loadFile = <span class="hljs-function">(<span class="hljs-params">url</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>((<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            loader.load(url,
                <span class="hljs-function">(<span class="hljs-params">gltf</span>) =></span> &#123;
                    resolve(gltf)
                &#125;, <span class="hljs-function">(<span class="hljs-params">&#123;loaded, total&#125;</span>) =></span> &#123;
                    <span class="hljs-keyword">let</span> load = <span class="hljs-built_in">Math</span>.abs(loaded / total * <span class="hljs-number">100</span>)
                    loadingWidth.value = load
                    <span class="hljs-keyword">if</span> (load >= <span class="hljs-number">100</span>) &#123;
                        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                            isLoading.value = <span class="hljs-literal">false</span>
                        &#125;, <span class="hljs-number">1000</span>)
                    &#125;
                    <span class="hljs-built_in">console</span>.log((loaded / total * <span class="hljs-number">100</span>) + <span class="hljs-string">'% loaded'</span>)
                &#125;,
                <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
                    reject(err)
                &#125;
            )
        &#125;))
    &#125;
    <span class="hljs-comment">// 设置灯光</span>
     <span class="hljs-keyword">const</span> setLight = <span class="hljs-function">() =></span> &#123;
        directionalLight = <span class="hljs-keyword">new</span> DirectionalLight(<span class="hljs-number">0xffffff</span>, <span class="hljs-number">0.5</span>)
        directionalLight.position.set(-<span class="hljs-number">4</span>, <span class="hljs-number">8</span>, <span class="hljs-number">4</span>)
        dhelper = <span class="hljs-keyword">new</span> DirectionalLightHelper(directionalLight, <span class="hljs-number">5</span>, <span class="hljs-number">0xff0000</span>)
        hemisphereLight = <span class="hljs-keyword">new</span> HemisphereLight(<span class="hljs-number">0xffffff</span>, <span class="hljs-number">0xffffff</span>, <span class="hljs-number">0.4</span>)
        hemisphereLight.position.set(<span class="hljs-number">0</span>, <span class="hljs-number">8</span>, <span class="hljs-number">0</span>)
        hHelper = <span class="hljs-keyword">new</span> HemisphereLightHelper(hemisphereLight, <span class="hljs-number">5</span>)
        scene.add(directionalLight)
        scene.add(hemisphereLight)
    &#125;
    <span class="hljs-comment">//初始化所有函数 </span>
   <span class="hljs-keyword">const</span> init = <span class="hljs-keyword">async</span>() => &#123;
        <span class="hljs-keyword">const</span> gltf = <span class="hljs-keyword">await</span> loadFile(<span class="hljs-string">'src/assets/3d/tesla_2018_model_3/scene.gltf'</span>)
        setScene()
        setCamera()
        setLight()
        scene.add(gltf.scene)
       loop()
    &#125;
    <span class="hljs-comment">//使场景、照相机、模型不停调用</span>
     <span class="hljs-keyword">const</span> loop = <span class="hljs-function">() =></span> &#123;
        requestAnimationFrame(loop)
        renderer.render(scene, camera)
    &#125;
    <span class="hljs-comment">//用vue钩子函数调用</span>
    onMounted(init) 

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">控制模型</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60234cae15084f1ab308da2cc4718497~tplv-k3u1fbpfcp-watermark.image" alt="屏幕录制2021-07-08 下午12.04.36.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>想用鼠标自由旋转，或者自动旋转，就要引用 <code>OrbitControls</code>对象，创建<code>setControls</code>函数也是在<code>init</code>调用，通过绑定<code>change</code>还可以监听坐标变化，另外也要在<code>loop</code>函数增加
<code>controls.update()</code>才可以更新位置变化</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">import</span> &#123; Scene,WebGLRenderer,PerspectiveCamera&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three'</span>
  <span class="hljs-keyword">import</span> &#123;GLTFLoader&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three/examples/jsm/loaders/GLTFLoader'</span>
  <span class="hljs-keyword">import</span> &#123;OrbitControls&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three/examples/jsm/controls/OrbitControls.js'</span>

  <span class="hljs-keyword">let</span> scene,renderer,camera,directionalLight,hemisphereLight,dhelper,hHelper,controls
  <span class="hljs-keyword">let</span> isLoading = ref(<span class="hljs-literal">true</span>)
  <span class="hljs-keyword">let</span> loadingWidth = ref(<span class="hljs-number">0</span>)
  <span class="hljs-comment">//相机的默认坐标</span>
  <span class="hljs-keyword">const</span> defaultMap = &#123;
        <span class="hljs-attr">x</span>: <span class="hljs-number">510</span>,
        <span class="hljs-attr">y</span>: <span class="hljs-number">128</span>,
        <span class="hljs-attr">z</span>: <span class="hljs-number">0</span>,
    &#125;
  <span class="hljs-comment">//创建场景</span>
  <span class="hljs-keyword">const</span> setScene = <span class="hljs-function">()=></span>&#123;
        scene = <span class="hljs-keyword">new</span> Scene()
        renderer = <span class="hljs-keyword">new</span> WebGLRenderer()
        renderer.setSize(innerWidth, innerHeight)
        <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.boxs'</span>).appendChild(renderer.domElement)
    &#125;
  <span class="hljs-comment">//创建相机  </span>
  <span class="hljs-keyword">const</span> setCamera = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> &#123;x, y, z&#125; = defaultMap
        camera = <span class="hljs-keyword">new</span> PerspectiveCamera(<span class="hljs-number">60</span>, innerWidth / innerHeight, <span class="hljs-number">1</span>, <span class="hljs-number">1000</span>)
        camera.position.set(x, y, z)
    &#125;
    <span class="hljs-comment">//通过Promise处理一下loadfile函数</span>
     <span class="hljs-keyword">const</span> loadFile = <span class="hljs-function">(<span class="hljs-params">url</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>((<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            loader.load(url,
                <span class="hljs-function">(<span class="hljs-params">gltf</span>) =></span> &#123;
                    resolve(gltf)
                &#125;, <span class="hljs-function">(<span class="hljs-params">&#123;loaded, total&#125;</span>) =></span> &#123;
                    <span class="hljs-keyword">let</span> load = <span class="hljs-built_in">Math</span>.abs(loaded / total * <span class="hljs-number">100</span>)
                    loadingWidth.value = load
                    <span class="hljs-keyword">if</span> (load >= <span class="hljs-number">100</span>) &#123;
                        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                            isLoading.value = <span class="hljs-literal">false</span>
                        &#125;, <span class="hljs-number">1000</span>)
                    &#125;
                    <span class="hljs-built_in">console</span>.log((loaded / total * <span class="hljs-number">100</span>) + <span class="hljs-string">'% loaded'</span>)
                &#125;,
                <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
                    reject(err)
                &#125;
            )
        &#125;))
    &#125;
    <span class="hljs-comment">// 设置灯光</span>
     <span class="hljs-keyword">const</span> setLight = <span class="hljs-function">() =></span> &#123;
        directionalLight = <span class="hljs-keyword">new</span> DirectionalLight(<span class="hljs-number">0xffffff</span>, <span class="hljs-number">0.5</span>)
        directionalLight.position.set(-<span class="hljs-number">4</span>, <span class="hljs-number">8</span>, <span class="hljs-number">4</span>)
        dhelper = <span class="hljs-keyword">new</span> DirectionalLightHelper(directionalLight, <span class="hljs-number">5</span>, <span class="hljs-number">0xff0000</span>)
        hemisphereLight = <span class="hljs-keyword">new</span> HemisphereLight(<span class="hljs-number">0xffffff</span>, <span class="hljs-number">0xffffff</span>, <span class="hljs-number">0.4</span>)
        hemisphereLight.position.set(<span class="hljs-number">0</span>, <span class="hljs-number">8</span>, <span class="hljs-number">0</span>)
        hHelper = <span class="hljs-keyword">new</span> HemisphereLightHelper(hemisphereLight, <span class="hljs-number">5</span>)
        scene.add(directionalLight)
        scene.add(hemisphereLight)
    &#125;
    <span class="hljs-comment">// 设置模型控制</span>
    <span class="hljs-keyword">const</span> setControls = <span class="hljs-function">() =></span> &#123;
        controls = <span class="hljs-keyword">new</span> OrbitControls(camera, renderer.domElement)
        controls.maxPolarAngle = <span class="hljs-number">0.9</span> * <span class="hljs-built_in">Math</span>.PI / <span class="hljs-number">2</span>
        controls.enableZoom = <span class="hljs-literal">true</span>
        controls.addEventListener(<span class="hljs-string">'change'</span>, render)
    &#125;
    <span class="hljs-keyword">const</span> render = <span class="hljs-function">() =></span> &#123;
        map.x = <span class="hljs-built_in">Number</span>.parseInt(camera.position.x)
        map.y = <span class="hljs-built_in">Number</span>.parseInt(camera.position.y)
        map.z = <span class="hljs-built_in">Number</span>.parseInt(camera.position.z)
    &#125;
    <span class="hljs-comment">//初始化所有函数 </span>
   <span class="hljs-keyword">const</span> init = <span class="hljs-keyword">async</span>() => &#123;
        <span class="hljs-keyword">const</span> gltf =<span class="hljs-keyword">await</span> loadFile(<span class="hljs-string">'src/assets/3d/tesla_2018_model_3/scene.gltf'</span>)
        setScene()
        setCamera()
        setLight()
        setControls()
        scene.add(gltf.scene)
    &#125;
    
   <span class="hljs-comment">//使场景、照相机、模型不停调用和更新位置数据</span>
     <span class="hljs-keyword">const</span> loop = <span class="hljs-function">() =></span> &#123;
        requestAnimationFrame(loop)
        renderer.render(scene, camera)
        controls.update()

    &#125;
    
    <span class="hljs-comment">//用vue钩子函数调用</span>
    onMounted(init) 

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">改变车身</h2>
<p>到这里基础的已经搭建好了,接下来我们再加一个功能改变汽车车身颜色,也是展厅展示一个比较基础的功能.创建一个<code>setColor</code> 这里说一下实例<code>scene</code> 有一个<code>traverse</code>函数，它回调了所有模型的子模型信息，只要我们找到对应name属性，就可以更改颜色，和增加贴图等等，
因为对模型结构不怎熟悉,所以根据名字来猜了一下 找到<code>door_</code>前序的名字大概应该就车身的套件。当然如果细分到我只想改引擎盖的颜色就要找出引擎盖套件。当然这个就要很熟悉这个模型结构了</p>
<pre><code class="hljs language-js copyable" lang="js"> 
    <span class="hljs-comment">//设置车身颜色</span>
      <span class="hljs-keyword">const</span> setCarColor = <span class="hljs-function">(<span class="hljs-params">index</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> currentColor = <span class="hljs-keyword">new</span> Color(colorAry[index])
        scene.traverse(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (child.isMesh) &#123;
                <span class="hljs-built_in">console</span>.log(child.name)
                <span class="hljs-keyword">if</span> (child.name.includes(<span class="hljs-string">'door_'</span>)) &#123;
                    child.material.color.set(currentColor)
                &#125;
            &#125;
        &#125;)
    &#125;
   
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">上完整代码</h3>
<p>其他操作都是交给vue控制，包括设置车身颜色、是否自动转动等等。大家运行以下代码的时候记得用<code>vite</code>打包工具创建vue3模板</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"boxs"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"maskLoading"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"isLoading"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"loading"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;width : loadingWidth +'%' &#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"padding-left: 10px;"</span>></span>&#123;&#123;parseInt(loadingWidth)&#125;&#125;%<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mask"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">p</span>></span>x : &#123;&#123;x&#125;&#125; y:&#123;&#123;y&#125;&#125; z :&#123;&#123;z&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"isAutoFun"</span>></span>转动车<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"stop"</span>></span>停止<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"flex"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"setCarColor(index)"</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item,index) in colorAry"</span>
                     <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;backgroundColor : item&#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123;onMounted, reactive, ref, toRefs&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
    <span class="hljs-keyword">import</span> &#123;
        Color,
        DirectionalLight,
        DirectionalLightHelper,
        HemisphereLight,
        HemisphereLightHelper,
        PerspectiveCamera,
        Scene,
        WebGLRenderer
    &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three'</span>
    <span class="hljs-keyword">import</span> &#123;OrbitControls&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three/examples/jsm/controls/OrbitControls.js'</span>
    <span class="hljs-keyword">import</span> &#123;GLTFLoader&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three/examples/jsm/loaders/GLTFLoader'</span>
    <span class="hljs-comment">//车身颜色数组</span>
    <span class="hljs-keyword">const</span> colorAry = [
        <span class="hljs-string">"rgb(216, 27, 67)"</span>, <span class="hljs-string">"rgb(142, 36, 170)"</span>, <span class="hljs-string">"rgb(81, 45, 168)"</span>, <span class="hljs-string">"rgb(48, 63, 159)"</span>, <span class="hljs-string">"rgb(30, 136, 229)"</span>, <span class="hljs-string">"rgb(0, 137, 123)"</span>,
        <span class="hljs-string">"rgb(67, 160, 71)"</span>, <span class="hljs-string">"rgb(251, 192, 45)"</span>, <span class="hljs-string">"rgb(245, 124, 0)"</span>, <span class="hljs-string">"rgb(230, 74, 25)"</span>, <span class="hljs-string">"rgb(233, 30, 78)"</span>, <span class="hljs-string">"rgb(156, 39, 176)"</span>,
        <span class="hljs-string">"rgb(0, 0, 0)"</span>] <span class="hljs-comment">// 车身颜色数组 </span>
    <span class="hljs-keyword">const</span> loader = <span class="hljs-keyword">new</span> GLTFLoader() <span class="hljs-comment">//引入模型的loader实例</span>
    <span class="hljs-keyword">const</span> defaultMap = &#123;
        <span class="hljs-attr">x</span>: <span class="hljs-number">510</span>,
        <span class="hljs-attr">y</span>: <span class="hljs-number">128</span>,
        <span class="hljs-attr">z</span>: <span class="hljs-number">0</span>,
    &#125;<span class="hljs-comment">// 相机的默认坐标</span>
    <span class="hljs-keyword">const</span> map = reactive(defaultMap)<span class="hljs-comment">//把相机坐标设置成可观察对象</span>
    <span class="hljs-keyword">const</span> &#123;x, y, z&#125; = toRefs(map)<span class="hljs-comment">//输出坐标给模板使用</span>
    <span class="hljs-keyword">let</span> scene, camera, renderer, controls, floor, dhelper, hHelper, directionalLight, hemisphereLight <span class="hljs-comment">// 定义所有three实例变量</span>
    <span class="hljs-keyword">let</span> isLoading = ref(<span class="hljs-literal">true</span>) <span class="hljs-comment">//是否显示loading  这个load模型监听的进度</span>
    <span class="hljs-keyword">let</span> loadingWidth = ref(<span class="hljs-number">0</span>)<span class="hljs-comment">// loading的进度</span>

    <span class="hljs-comment">//创建灯光</span>
    <span class="hljs-keyword">const</span> setLight = <span class="hljs-function">() =></span> &#123;
        directionalLight = <span class="hljs-keyword">new</span> DirectionalLight(<span class="hljs-number">0xffffff</span>, <span class="hljs-number">0.5</span>)
        directionalLight.position.set(-<span class="hljs-number">4</span>, <span class="hljs-number">8</span>, <span class="hljs-number">4</span>)
        dhelper = <span class="hljs-keyword">new</span> DirectionalLightHelper(directionalLight, <span class="hljs-number">5</span>, <span class="hljs-number">0xff0000</span>)
        hemisphereLight = <span class="hljs-keyword">new</span> HemisphereLight(<span class="hljs-number">0xffffff</span>, <span class="hljs-number">0xffffff</span>, <span class="hljs-number">0.4</span>)
        hemisphereLight.position.set(<span class="hljs-number">0</span>, <span class="hljs-number">8</span>, <span class="hljs-number">0</span>)
        hHelper = <span class="hljs-keyword">new</span> HemisphereLightHelper(hemisphereLight, <span class="hljs-number">5</span>)
        scene.add(directionalLight)
        scene.add(hemisphereLight)
    &#125;

    <span class="hljs-comment">// 创建场景</span>
    <span class="hljs-keyword">const</span> setScene = <span class="hljs-function">() =></span> &#123;
        scene = <span class="hljs-keyword">new</span> Scene()
        renderer = <span class="hljs-keyword">new</span> WebGLRenderer()
        renderer.setSize(innerWidth, innerHeight)
        <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.boxs'</span>).appendChild(renderer.domElement)

    &#125;
    
    <span class="hljs-comment">// 创建相机</span>
    <span class="hljs-keyword">const</span> setCamera = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> &#123;x, y, z&#125; = defaultMap
        camera = <span class="hljs-keyword">new</span> PerspectiveCamera(<span class="hljs-number">60</span>, innerWidth / innerHeight, <span class="hljs-number">1</span>, <span class="hljs-number">1000</span>)
        camera.position.set(x, y, z)
    &#125;
    
    <span class="hljs-comment">// 设置模型控制</span>
    <span class="hljs-keyword">const</span> setControls = <span class="hljs-function">() =></span> &#123;
        controls = <span class="hljs-keyword">new</span> OrbitControls(camera, renderer.domElement)
        controls.maxPolarAngle = <span class="hljs-number">0.9</span> * <span class="hljs-built_in">Math</span>.PI / <span class="hljs-number">2</span>
        controls.enableZoom = <span class="hljs-literal">true</span>
        controls.addEventListener(<span class="hljs-string">'change'</span>, render)
    &#125;
    
    <span class="hljs-comment">//返回坐标信息</span>
     <span class="hljs-keyword">const</span> render = <span class="hljs-function">() =></span> &#123;
        map.x = <span class="hljs-built_in">Number</span>.parseInt(camera.position.x)
        map.y = <span class="hljs-built_in">Number</span>.parseInt(camera.position.y)
        map.z = <span class="hljs-built_in">Number</span>.parseInt(camera.position.z)
    &#125;
    
    
 
    <span class="hljs-comment">// 循环场景 、相机、 位置更新</span>
    <span class="hljs-keyword">const</span> loop = <span class="hljs-function">() =></span> &#123;
        requestAnimationFrame(loop)
        renderer.render(scene, camera)
        controls.update()
    &#125;
    
 
    <span class="hljs-comment">//是否自动转动</span>
    <span class="hljs-keyword">const</span> isAutoFun = <span class="hljs-function">() =></span> &#123;
        controls.autoRotate = <span class="hljs-literal">true</span>
    &#125;
    <span class="hljs-comment">//停止转动</span>
    <span class="hljs-keyword">const</span> stop = <span class="hljs-function">() =></span> &#123;
        controls.autoRotate = <span class="hljs-literal">false</span>
    &#125;

    <span class="hljs-comment">//设置车身颜色</span>
    <span class="hljs-keyword">const</span> setCarColor = <span class="hljs-function">(<span class="hljs-params">index</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> currentColor = <span class="hljs-keyword">new</span> Color(colorAry[index])
        scene.traverse(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (child.isMesh) &#123;
                <span class="hljs-built_in">console</span>.log(child.name)
                <span class="hljs-keyword">if</span> (child.name.includes(<span class="hljs-string">'door_'</span>)) &#123;
                    child.material.color.set(currentColor)
                &#125;
            &#125;
        &#125;)
    &#125;
    
    <span class="hljs-keyword">const</span> loadFile = <span class="hljs-function">(<span class="hljs-params">url</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>((<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            loader.load(url,
                <span class="hljs-function">(<span class="hljs-params">gltf</span>) =></span> &#123;
                    resolve(gltf)
                &#125;, <span class="hljs-function">(<span class="hljs-params">&#123;loaded, total&#125;</span>) =></span> &#123;
                    <span class="hljs-keyword">let</span> load = <span class="hljs-built_in">Math</span>.abs(loaded / total * <span class="hljs-number">100</span>)
                    loadingWidth.value = load
                    <span class="hljs-keyword">if</span> (load >= <span class="hljs-number">100</span>) &#123;
                        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                            isLoading.value = <span class="hljs-literal">false</span>
                        &#125;, <span class="hljs-number">1000</span>)
                    &#125;
                    <span class="hljs-built_in">console</span>.log((loaded / total * <span class="hljs-number">100</span>) + <span class="hljs-string">'% loaded'</span>)
                &#125;,
                <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
                    reject(err)
                &#125;
            )
        &#125;))
    &#125;
    
    
       <span class="hljs-comment">//初始化所有函数</span>
    <span class="hljs-keyword">const</span> init = <span class="hljs-keyword">async</span> () => &#123;
        setScene()
        setCamera()
        setLight()
        setControls()
        <span class="hljs-keyword">const</span> gltf = <span class="hljs-keyword">await</span> loadFile(<span class="hljs-string">'src/assets/3d/tesla_2018_model_3/scene.gltf'</span>)
        scene.add(gltf.scene)
        loop()
    &#125;
      <span class="hljs-comment">//用vue钩子函数调用</span>
    onMounted(init) 
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-tag">body</span> &#123;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
    &#125;

    <span class="hljs-selector-class">.maskLoading</span> &#123;
        <span class="hljs-attribute">background</span>: <span class="hljs-number">#000</span>;
        <span class="hljs-attribute">position</span>: fixed;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">justify-content</span>: center;
        <span class="hljs-attribute">align-items</span>: center;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">z-index</span>: <span class="hljs-number">1111111</span>;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    &#125;

    <span class="hljs-selector-class">.maskLoading</span> <span class="hljs-selector-class">.loading</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">20px</span>;
        <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#fff</span>;
        <span class="hljs-attribute">background</span>: <span class="hljs-number">#000</span>;
        <span class="hljs-attribute">overflow</span>: hidden;
        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">10px</span>;

    &#125;

    <span class="hljs-selector-class">.maskLoading</span> <span class="hljs-selector-class">.loading</span> <span class="hljs-selector-tag">div</span> &#123;
        <span class="hljs-attribute">background</span>: <span class="hljs-number">#fff</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">20px</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">transition-duration</span>: <span class="hljs-number">500ms</span>;
        <span class="hljs-attribute">transition-timing-function</span>: ease-in;
    &#125;

    <span class="hljs-selector-tag">canvas</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">margin</span>: auto;
    &#125;

    <span class="hljs-selector-class">.mask</span> &#123;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    &#125;

    <span class="hljs-selector-class">.flex</span> &#123;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">flex-wrap</span>: wrap;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span>;

    &#125;

    <span class="hljs-selector-class">.flex</span> <span class="hljs-selector-tag">div</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">10px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">10px</span>;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">5px</span>;
        <span class="hljs-attribute">cursor</span>: pointer;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e429461d3024f4cbdc621470c97ef83~tplv-k3u1fbpfcp-watermark.image" alt="屏幕录制2021-07-08 下午1.39.03.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">最后</h2>
<p>在这个3D汽车展示厅笔者只是简单创建了一些基础功能，还有很多功能可以增加，比如创建背景、地板、一些阴影、定点显示车套件位置信息等等。掌握套路,这些功能实现也不难。<strong>另外笔者要冲二级啦，希望大家如果喜欢能给小弟点个赞，谢谢啦</strong> ^_^</p></div>  
</div>
            