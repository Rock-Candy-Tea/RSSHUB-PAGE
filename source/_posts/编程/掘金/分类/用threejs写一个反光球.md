
---
title: '用three.js写一个反光球'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30d486eeba0b46debfc9567d098126b1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 21:54:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30d486eeba0b46debfc9567d098126b1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>本文我们将用three.js来模拟出一个反光球。效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30d486eeba0b46debfc9567d098126b1~tplv-k3u1fbpfcp-watermark.image" alt="reflection.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">前置知识</h1>
<p>这是学习<code>three.js系列</code>的第三篇，前两篇是：</p>
<p><a href="https://juejin.cn/post/6940542710709223432#heading-0" target="_blank" title="https://juejin.cn/post/6940542710709223432#heading-0">用three.js写一个下雨动画</a></p>
<p><a href="https://juejin.cn/post/6942910177347633165" target="_blank" title="https://juejin.cn/post/6942910177347633165">用three.js写一个小场景</a></p>
<p>关于<code>three.js</code>基础知识的讲解，是放在了第一篇： <a href="https://juejin.cn/post/6940542710709223432#heading-0" target="_blank" title="https://juejin.cn/post/6940542710709223432#heading-0">用three.js写一个下雨动画</a>，可前往查看，后面的案例都不再重复。</p>
<h1 data-id="heading-2">几何体与材质</h1>
<p>在基础知识篇中，我们了解了渲染器（Renderer）、场景（Scene）、照相机（Camera），坐标系，物体，光照等的基础使用，这里我们主要探讨物体相关。</p>
<p>在<code>three.js</code>中，创建物体时，需要传入两个参数，一个是几何形状（Geometry），另一个是材质（Material）。</p>
<pre><code class="copyable">const object = new THREE.Mesh(geometry, material)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">几何体</h2>
<p>几何体（Geometry）的功能是储存一个物体的顶点信息，这些顶点信息决定了物体的形状。在空间中绘制一个物体，如果使用<code>WebGL</code>，需要程序员指定每个顶点的位置，而在<code>three.js</code>中，你可以直接声明几何形状，比如立方体、平面、球体、圆柱体、四面体、八面体等，你只需要按照文档传入定义这些几何形状需要的参数即可。</p>
<p>一些例子：</p>
<pre><code class="copyable">const floorGeometry = new THREE.PlaneGeometry( 800, 1000 )  //创建一个平面几何体，传入宽高
const sphereGeometry = new THREE.SphereGeometry(350, 50, 50)     //创建一个球体，传入半径和经度、纬度的分片
const doorGeometry = new THREE.BoxGeometry(100,210,40)      //创建一个立方体，传入长、宽、高
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">材质</h2>
<blockquote>
<p>材质就像物体的皮肤，决定了几何体的外表。例如，皮肤定义了一个几何体看起来是否像金属、透明与否，或者显示为线框。</p>
</blockquote>
<p>材质（Material）的应用非常灵活，很多酷炫的3D效果都是因为材质。材质的类型有很多种，例如：</p>
<ul>
<li><code>MeshBasicMaterial</code>：渲染后物体的颜色始终为该材质的颜色，不对光照产生反应，不会由于光照产生明暗、阴影效果。</li>
</ul>
<pre><code class="copyable">const geometry = new THREE.BoxGeometry();    //不传入参数，则使用长宽高的默认值：1
const material = new THREE.MeshBasicMaterial(&#123;       //创建Basic材质
  color: 0x00ff00
&#125;)
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0eb708b09e144733bb1bbe91bc3e2029~tplv-k3u1fbpfcp-watermark.image" alt="图片替换文本" width="400" height="110" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li><code>MeshLambertMaterial</code>：只考虑漫反射，而不考虑镜面反射的效果，不适用于金属、玻璃等物体。<strong>如果物体使用<code>MeshLambertMaterial</code>，则必须在场景中加入光照，否则物体不会显示。并且，物体最终的显示颜色由材质的<code>color参数</code>和光照颜色共同决定。</strong> 下图是一些光照类型：</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7153626ed7f4f5fa3d054b0e4cda2b2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
下面是平行光（directionLight）和Lambert材质的结合，可以看到立方体每个面有了不同的明暗程度。</p>
<pre><code class="copyable">const material = new THREE.MeshLambertMaterial(&#123; color: 0x00ff00 &#125;);    //创建Lambert材质

const directionLight = new THREE.DirectionalLight(0xffffff)  //创建平行光，参数是光的颜色
directionLight.position.set(10,10,10)                        //定义平行光方向
scene.add(directionLight)                                    //将平行光添加到场景中
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/629e0792e19040c8972a6a21c877c063~tplv-k3u1fbpfcp-watermark.image" alt="图片替换文本" width="400" height="110" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li><code>MeshPhongMaterial</code>：考虑了镜面反射的效果，适合于金属、玻璃等。在同样的平行光环境下，将立方体的材质设为<code>MeshPhongMaterial</code>，效果如下，可以看到，立方体会对光照产生镜面反射。</li>
</ul>
<pre><code class="copyable">const material = new THREE.MeshPhongMaterial(&#123; 
  color: 0x00ff00,
  shininess: 100                      //决定Phong材质的高光度，当shininess值为0时，表现和MeshLambertMaterial材质一样
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04701778093d4593b80456ef06739f5f~tplv-k3u1fbpfcp-watermark.image" alt="图片替换文本" width="400" height="105" loading="lazy" referrerpolicy="no-referrer">
<p>以上是一些比较基本的材质创建方式，更多的材质和材质参数参考官方文档。</p>
<h2 data-id="heading-5">纹理</h2>
<p>之前，我们都是在创建的材质时传入<code>color</code>值，这样创建的材质是单一颜色的。然而在更多时候，我们需要基于图像来生成材质。</p>
<p>下面我们创建一个六面都贴上图像的立方体。这里我们不考虑光照阴影等影响，使用<code>MeshBasicMaterial</code></p>
<pre><code class="copyable">const geometry = new THREE.BoxGeometry();
const texture = new THREE.TextureLoader().load( `./images/pic1.jpg` )   //用TextureLoader加载图像文件
const material = new THREE.MeshBasicMaterial( &#123; 
  map: texture     // 将加载好的图像作为map传给材质
&#125; )
const cube = new THREE.Mesh(geometry, material);
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/194574c4486a4dbca12e0674c2bae049~tplv-k3u1fbpfcp-watermark.image" alt="图片替换文本" width="400" height="95" loading="lazy" referrerpolicy="no-referrer">
<p><strong>注意，使用纹理加载器<code>TextureLoader</code>来加载图像会有跨域限制，如果图像文件和当前html不在同域，且不允许跨域，加载图像文件就会失败。</strong></p>
<p>所以以访问本地文件的方式<code>（file://xxx)</code> 打开html就不可行啦，可以用<code>live-server</code>或者<code>webpack-dev-server</code>搭建一个服务器。</p>
<p><code>live-server</code>搭建服务器的步骤：<a href="https://juejin.cn/post/6907904333950484493#heading-0" target="_blank" title="https://juejin.cn/post/6907904333950484493#heading-0">如何用<code>live-server</code>搭建一个简易的服务器</a></p>
<p>本项目将使用<code>webpack-dev-server</code>搭建服务器，有需要的童鞋可查看源码。</p>
<h3 data-id="heading-6">立方体每个面贴不同的图片</h3>
<p>要为立方体每个面贴不同的图片，首先，准备6张图片。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63969ec14a1f4b008aae4f04e3c82b87~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
使用纹理加载器<code>TextureLoader</code>分别加载6张图片，并设置到六个材质中：</p>
<pre><code class="copyable">const geometry = new THREE.BoxGeometry()
const materials = []   //材质数组
for( let i = 0; i < 6; i ++) &#123;
  //使用TextureLoader加载每一张图片
  const texture = new THREE.TextureLoader().load( `../../images/reflection-sphere/$&#123;i+1&#125;.jpg` );
  //根据纹理生成材质，并加入材质数组中
  materials.push( new THREE.MeshBasicMaterial(&#123; 
    map: texture
  &#125;));
&#125;
//根据几何形状和材质数组生成物体
const cube = new THREE.Mesh(geometry, materials)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：（ 红色代表 X 轴，绿色代表 Y 轴，蓝色代表 Z 轴，使用 AxesHelper 生成 ）</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2be19b1c0fd42acb131d9bc0dc88264~tplv-k3u1fbpfcp-watermark.image" alt="图片替换文本" width="400" height="180" loading="lazy" referrerpolicy="no-referrer">
<p>可以看出，材质数组中的材质会按照 <code>X轴正方向、X轴负方向、Y轴正方向、Y轴负方向、Z轴正方向、Z轴负方向</code> 的顺序，对立方体的面进行贴图。</p>
<p>纹理最基础的用法是作为贴图被添加在材质上（纹理映射），当你使用这样的材质创建物体（Mesh）时，物体的颜色来源于纹理。相较于纯颜色，基于纹理的材质可以更好地模拟现实世界。</p>
<h1 data-id="heading-7">实现 360 全景</h1>
<p>回到我们这个小例子，我们的第一步是实现一个 360 全景。</p>
<h2 data-id="heading-8">boxGeometry方案</h2>
<p>全景的实现原理：创造一个容器，通常是球体或正方体，在其内表面贴上图片，然后将相机放在容器的中心。</p>
<p>对比上面的例子，我们进行两步：</p>
<ol>
<li>内表面贴图。我们只要需将<code>geometry</code>的<code>scale</code>的一个属性设置为负值，材质就会应用在几何体的内表面。</li>
</ol>
<pre><code class="copyable">const geometry = new THREE.BoxGeometry(10,10,10)
geometry.scale(-1, 1, 1)  // 设置scale.x
// geometry.scale(1, -1, 1)  设置scale.y，会导致画面上下颠倒，所以通常都设置scale.x或者scale.z
// geometry.scale(1, 1, -1)  设置scale.z

const materials = []
for( let i = 0; i < 6; i ++) &#123;
  const texture = new TextureLoader().load( `../../images/reflection-sphere/$&#123;i+1&#125;.jpg` );
  materials.push( new MeshBasicMaterial(&#123; 
    map: texture&#125; 
  ));
&#125;
  
const cube = new Mesh(geometry, materials)
cube.position.set(0, 0, 0)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>将相机放在容器的中心。</li>
</ol>
<pre><code class="copyable">camera.position.set(0, 0, 0.01)
camera.lookAt(0,0,0)
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e8197de2ead48cdaaf089349c687f45~tplv-k3u1fbpfcp-watermark.image" alt="图片替换文本" width="400" height="280" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-9">scene.background方案</h2>
<p>另外一种实现全景的方案，就是使用<code>THREE.CubeTextureLoader</code>加载6个图片，然后将加载好的图像纹理作为整个场景<code>Scene</code>的背景，这样也能形成360度全景。</p>
<pre><code class="copyable">//准备6张图片，实现全景的图片也需要满足以下的顺序:
//X轴正方向、X轴负方向、Y轴正方向、Y轴负方向、Z轴正方向、Z轴负方向
const urls = [   
  'posx.jpg',
  'negx.jpg',
  'posy.jpg',
  'negy.jpg',
  'posz.jpg',
  'negz.jpg'
]
  
//实例化CubeTextureLoader
const loader = new THREE.CubeTextureLoader()    
  
//加载6个图像
const cubeMap = loader.setPath('../../images/reflection-sphere/').load(urls)
  
//将图像纹理作为场景的背景
scene.background = cubeMap  、
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2cf845c9994a44cb8d33ef05df5e5ae6~tplv-k3u1fbpfcp-watermark.image" alt="图片替换文本" width="400" height="280" loading="lazy" referrerpolicy="no-referrer">
<p>可以看出，和第一种方案有着相同的效果。</p>
<p>两种方案的适用场景：第一种方案基于BoxGeometry，可以更好地控制在全景中特定坐标位置添加物体，适用于3d看房等室内场景，可以更好满足全景中物体点击、选中等需求。</p>
<p>第二种方案中，想要创建物体与全景中某一处进行坐标绑定比较困难，所以更适用于作为纯粹的环境全景。但只要不涉及全景中的坐标，这种方案对整个场景和相机的操作更加自由。在我们这个案例中，就将采用第二种方式实现全景。</p>
<h1 data-id="heading-10">实现反光球</h1>
<h2 data-id="heading-11">添加球体</h2>
<pre><code class="copyable">//创建球体形状
const sphereGeometry = new THREE.SphereGeometry(20, 30, 30)
//创建球体材质
const sphereMaterial = new THREE.MeshBasicMaterial(&#123;
  color: 0xff00ff
&#125;)
//生成球体
const sphere = new THREE.Mesh(sphereGeometry, sphereMaterial)
//设置球体位置
sphere.position.set(0, 0, 0)
//将球体添加到场景中
scene.add(sphere)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f7dee12ecad452391e05ca7c945d293~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">贴图实现反光</h2>
<p>计算镜面反射效果对CPU的耗费是非常大的，而且通常会使用光线追踪算法。在<code>Three.js</code>中你依然可以实现镜面反射效果，只不过是做一个假的。你可以通过创建一个<strong>物体所处环境的纹理</strong>来伪装镜面反射，并将它应用到指定的对象上。</p>
<h3 data-id="heading-13">envMap</h3>
<p>在上面，我们分别用<code>color</code>和<code>map</code>创建了材质，这里我们将使用envMap（环境贴图）.<code>envMap</code>字面意思就是物体周边环境，比如你渲染一个有反光特点的物体，物体周边的环境肯定影响物体的渲染效果。</p>
<p>这里，我们就将全景纹理赋值给envMap，来模拟对四周环境的镜面反射。</p>
<p>之前实现360全景，使用了<code>THREE.CubeTextureLoader</code>加载6张图片，Three.js会将这些图片整合到一起来创建一个无缝的纹理，上面全景是将这个纹理作为场景背景，而这里我们将这个纹理作为球体的环境贴图（envMap）。</p>
<pre><code class="copyable">//创建球体形状
const sphereGeometry = new THREE.SphereGeometry(20, 30, 30)
//将图像纹理作为球体的环境贴图（cubeMap为实现全景时用CubeTextureLoader加载的纹理）
const sphereMaterial = new THREE.MeshBasicMaterial(&#123;
  envMap: cubeMap
&#125;)

const sphere = new THREE.Mesh(sphereGeometry, sphereMaterial)
sphere.position.set(0, 0, 0)
scene.add(sphere)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的模拟只能反射指定的背景，如果场景中有其他物体，并不会出现在反光球中。</p>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a79012f22a1e4c7483db045c49d11665~tplv-k3u1fbpfcp-watermark.image" alt="图片替换文本" width="400" height="290" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-14">cubeCamera</h3>
<p>要实时反射任何物体，可以借助<code>cubeCamera</code>。</p>
<p><code>cubeCamera</code>会构造一个包含6个<code>PerspectiveCameras</code>（透视摄像机）的立方摄像机， 并将其拍摄的场景渲染到一个<code>WebGLCubeRenderTarget</code>上。</p>
<p>也就是说，我们可以使用<code>cubeCamera</code>实时为场景中的物体拍摄照片，然后使用这些实时照片创建纹理。将这些纹理作为球体的环境贴图（envMap）就可以模拟实时的反射了。</p>
<pre><code class="copyable">//将要创建的纹理对象，定义目标纹理的一些参数
const cubeRenderTarget = new THREE.WebGLCubeRenderTarget( 128, &#123; 
  format: RGBFormat, 
  generateMipmaps: true,
  minFilter: LinearMipmapLinearFilter
&#125;);

//创建cubeCamera
//1：近剪切面的距离；1000：远剪切面的距离；cubeRenderTarget:将要创建的纹理对象
const cubeCamera = new THREE.CubeCamera(1, 1000, cubeRenderTarget)

cubeCamera.position.set(0, 0, 0)
scene.add(cubeCamera)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，将生成的纹理作为球体的envMap：</p>
<pre><code class="copyable">const sphereMaterial = new THREE.MeshBasicMaterial(&#123;
   envMap: cubeCamera.renderTarget  //cubeCamera生成的纹理作为球体的环境贴图
&#125;)
const sphereGeometry = new THREE.SphereGeometry(20, 30, 30)
const sphere = new THREE.Mesh(sphereGeometry, sphereMaterial)
phere.position.set(0, 0, 0)
scene.add(sphere)
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58ef13ead4a242a09487aa1dcac0dc44~tplv-k3u1fbpfcp-watermark.image" alt="图片替换文本" width="400" height="200" loading="lazy" referrerpolicy="no-referrer"></div>  
</div>
            