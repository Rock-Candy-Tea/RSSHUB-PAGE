
---
title: 'threeJS做web端3D模型展示'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e89c15ed5e6845ccb54ff68f22ee1232~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 19:07:03 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e89c15ed5e6845ccb54ff68f22ee1232~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">先看看效果</h3>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e89c15ed5e6845ccb54ff68f22ee1232~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">引入threeJS</h3>
<pre><code class="copyable"><script src="./js/three.js" type="text/javascript" charset="utf-8"></script>
//手势控制器
<script src="./js/controls.js" type="text/javascript" charset="utf-8"></script>
//模型加载器，还有其他类型如：OBJ,自行更换模型加载器
<script src="./js/FBXLoader.js" type="text/javascript" charset="utf-8"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不建议使用模块得方式导入threeJS，会导致未知得问题</p>
<h3 data-id="heading-2">承载模型标签设置宽高</h3>
<pre><code class="copyable"><div 
    class="three" 
    ref="three"
>
</div>

.three &#123;
width: 100vw;
height: 100vh;&#125;
//我这里设置的是全屏
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">threeJS JS部分</h3>
<pre><code class="copyable">如果使用vue的话先简化下赋值
const THREE = window.THREE;
init() &#123;
var that = this;

//场景
var scene = new THREE.Scene();

//相机视角
var camera = new THREE.PerspectiveCamera(
    30, 
    this.$refs.three.clientWidth / this.$refs.three.clientHeight, 
    0.1, 
    2000
);

//渲染器
var renderer = new THREE.WebGLRenderer( &#123; antialias: true, alpha: true &#125; );
that.renderer=renderer;renderer.setPixelRatio(devicePixelRatio);
renderer.setSize(this.$refs.three.clientWidth, this.$refs.three.clientHeight);

//设置背景为透明，这样就可以自己加背景图片了
renderer.setClearAlpha(0);this.$refs.three.appendChild(renderer.domElement);

//材质
let sphereGeometry = new THREE.SphereGeometry(30, 50, 50);
let meshMaterial  = new THREE.MeshPhongMaterial(&#123;  
    color:0x0000ff,  
    specular:0x4488ee,  
    shininess:12&#125;);
meshMaterial.shininess = 100;
let sphere = new THREE.Mesh(sphereGeometry, meshMaterial);
sphere.castShadow = true;scene.add(sphere);

//光源
var ambientLight = new THREE.AmbientLight(0xffffff,1.5);
scene.add(ambientLight);

// 平行光
var directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(80, 100, 50);
scene.add(directionalLight);

//手势控制器
var controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.autoRotate = true;
controls.enablePan = false;
controls.maxDistance = 2;
controls.minDistance = 0.5;
controls.update();

//加载模型
var loader = new THREE.FBXLoader();
loader.load(
    //模型的链接地址，这里的地址必须使用线上地址或者使用本地服务器
    'obj-url.com',
    object => &#123;      
        // object.traverse(function(child) &#123;      
        //   if (child instanceof THREE.Mesh) &#123;      
        //     child.material.emissive = new THREE.Color(1,1,1);      
        //     child.material.emissiveIntensity=1;      
        //     child.material.emissiveMap=child.material.map;      
        //   &#125;      
        // &#125;);      
        scene.add(object);      
        camera.position.z = 1;    
    &#125;,
    //加载进度
    xhr => &#123;      
        that.progress = parseInt(( xhr.loaded / xhr.total * 100 ));    
    &#125;,    
    error => &#123;      
        console.error(error);    
    &#125;
);

//60帧动画，360°自动旋转模型
(function animate() &#123;  
    requestAnimationFrame(animate);  
    controls.update();  
    renderer.render(scene, camera);
&#125;)()&#125;

//页面卸载的时候清掉缓存和模型数据
beforeDestroy() &#123;  
    THREE.Cache.clear();  
    this.renderer.dispose();  
    this.renderer.forceContextLoss();  
    this.renderer.domElement = null;  
    this.renderer = null;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后面会完善这篇文章。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            