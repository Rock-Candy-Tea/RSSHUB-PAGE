
---
title: '在WebGL场景中管理多个卡牌对象的实验'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7335e6e47b14457a1d581b8b9f97ceb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 27 May 2021 22:20:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7335e6e47b14457a1d581b8b9f97ceb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>　　这篇文章讨论如何在基于Babylon.js的WebGL场景中，实现多个简单卡牌类对象的显示、选择、分组、排序，同时建立一套实用的3D场景代码框架。由于作者美工能力有限，所以示例场景视觉效果可能欠佳，本文的重点在于对相关技术的探讨。</p>
<p>　　因为文章比较长，读者可以考虑将网页导出为mhtml格式，使用Word浏览。Chrome浏览器导出mhtml文件的方法见末尾。</p>
<p>一、显示效果：</p>
<p>1、访问https://ljzc002.github.io/CardSimulate/HTML/TEST2.html查看“卡牌模拟页面”：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7335e6e47b14457a1d581b8b9f97ceb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　场景中间是三个作为参照物的小球，视口平面的中间是一个用Babylon.js GUI制作的准星，默认鼠标与准星锁定在一起，直接移动鼠标即可改变相机视角，使用WASD Shift 空格键可以控制相机前、左、后、右、下、上运动（可能将Ctrl键设为向下更符合传统，但是没有找到禁用浏览器Ctrl+s快捷键的方法，只好用Shift代替）。因为光标被锁定，将这种浏览状态命名为“first_lock”。</p>
<p>2、按下Alt键，75张卡片通过动画移入相机视野，同时相机的位置被固定（但仍可以通过拖动鼠标改变视角）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b9a0629ad7a4af79a8daf17dde64e83~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　点击右侧的“向上两行”和“向下两行”按钮可以上下滚动卡片，再次按下Alt键将隐藏卡片，同时恢复相机的移动和光标的锁定。因为这种浏览状态主要用来点选场景中的物体，将它命名为“first_pick”。</p>
<p>3、鼠标左键单击一张卡片，卡片将处于“选中状态”（绿色边缘），再次左键单击处于选中状态的卡片，卡片将被放大拉近显示，再左键单击将恢复原位：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e72244e25a4c43d5a471aa4491f237bb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　执行动画时会禁用用户的控制，完全由动画控制视角，所以将这种浏览状态命名为“first_ani”。</p>
<p>4、模仿Windows的文件多选编写了卡片多选功能，按下Ctrl时可以点选多个卡片，按下Shift时可以选取首尾之间的所有卡片：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebb677f27575474faa178fa2c79f6137~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>5、选中若干张卡片后，按1-5键可以将被选中的卡片编为1-5队，被编队的卡片将按编队顺序显示在最高处，同时编队的前面会显示队号标记：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3eafb87800654e59bb7382f374a7df89~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>6、在first_pick状态可以使用上下左右方向键进行场景漫游，可以看到场景中的所有对象：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b15da6b380e4d0991f0fcfe8f0ee720~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> 二、代码实现：</p>
<p>1、文件结构：</p>
<p>CardSimulate工程的文件结构如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9eb0ae36680341e7af7f1ea5b7c29f09~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中LIB目录下是从网上下载的代码库</p>
<p>　　babylon.32.all.maxs.js是Babylon.js引擎库</p>
<p>　　earcut.dev.js是一个Babylon.js扩展，其功能是在网格上挖洞</p>
<p>　　stat.js是用来显示帧数的代码</p>
<p>MYLIB是自己编写的代码库</p>
<p>　　Events.js是一些用来处理事件的方法</p>
<p>　　FileText.js是与文件处理相关的代码</p>
<p>　　newland.js是自己编写的一些Babylon.js辅助类</p>
<p>　　View.js是html视图的一些相关方法</p>
<p>PAGE是直接操纵这个页面（WebGL场景）的代码库</p>
<p>　　Character.js是场景中出现的各种对象的类（比如卡牌网格、相机网格）</p>
<p>　　Control20180312.js是用来处理鼠标键盘输入的代码</p>
<p>　　DrawCard.js是用来绘制卡牌的代码</p>
<p>　　FullUI.js是用来绘制全局（全屏）UI的代码</p>
<p>　　Game.js是游戏类，存储用来调度整个场景的信息</p>
<p>　　HandleCard.js是用来处理已经绘制出的卡牌的代码，后期考虑和DrawCard.js整合在一起</p>
<p>　　HandleCard2.js是一个分枝修改版</p>
<p>　　Moves.js是运动计算代码</p>
<p>　　tab_carddata.js里是卡牌种类信息</p>
<p>　　tab_somedata.js里是其他辅助信息</p>
<p>2、代码入口与场景初始化：</p>
<p>　　A、代码由TEST2.html开始执行，其中一部分和前面几篇文章用到的相似：</p>
<pre><code class="copyable"> 1 <!DOCTYPE html>
 2 <html lang="en">
 3 <head>
 4     <meta charset="UTF-8">
 5     <title>第二个场景测试，手牌的显示、排列、分组排序，显示瓷砖地面</title>
 6     <link href="../CSS/newland.css" rel="stylesheet">
 7     <link href="../CSS/stat.css" rel="stylesheet">
 8     <script src="../JS/LIB/babylon.32.all.maxs.js"></script>
 9     <script src="../JS/LIB/stat.js"></script>
10     <script src="../JS/MYLIB/Events.js"></script>
11     <script src="../JS/MYLIB/FileText.js"></script>
12     <script src="../JS/MYLIB/newland.js"></script>
13     <script src="../JS/MYLIB/View.js"></script>
14     <script src="../JS/PAGE/Game.js"></script>
15     <script src="../JS/PAGE/Character.js"></script>
16     <script src="../JS/PAGE/Control20180312.js"></script>
17     <script src="../JS/PAGE/Moves.js"></script>
18     <script src="../JS/PAGE/DrawCard.js"></script>
19     <script src="../JS/PAGE/tab_carddata.js"></script>
20     <script src="../JS/PAGE/tab_somedata.js"></script>
21     <script src="../JS/PAGE/HandleCard2.js"></script>
22     <script src="../JS/PAGE/FullUI.js"></script>
23 </head>
24 <body>
25 <div id="div_allbase">
26     <canvas id="renderCanvas"></canvas>
27     <div id="fps" style="z-index: 301;"></div>
28 </div>
29 </body>
30 <script>
31     var VERSION=1.0,AUTHOR="lz_newland@163.com";
32     var machine,canvas,engine,scene,gl,MyGame=&#123;&#125;;
33     canvas = document.getElementById("renderCanvas");
34     engine = new BABYLON.Engine(canvas, true);
35     engine.displayLoadingUI();
36     gl=engine._gl;//决定在这里结合使用原生OpenGL和Babylon.js;
37     scene = new BABYLON.Scene(engine);
38     var divFps = document.getElementById("fps");
39 
40     var MyGame=&#123;&#125;;
41     window.onload=beforewebGL;
42     function beforewebGL()
43     &#123;
44         if(engine._webGLVersion==2.0)//输出ES版本
45         &#123;
46             console.log("ES3.0");
47         &#125;
48         else&#123;
49             console.log("ES2.0");
50         &#125;
51         MyGame=new Game(0,"first_pick","","http://127.0.0.1:8082/");//建立MyGame对象用来进行全局调度
52         /*0-startWebGL
53          * */
54         webGLStart();
55     &#125;
。。。

56 </script>
57 </html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　但与前面的简单场景将主要代码都写在webGLStart方法中不同，对于较为复杂的流程最好将流程的每个阶段写在单独的方法里，对于较多的对象则最好提取对象的共同点作为一个“类”，将每个对象作为类的实例。这样可以将程序的复杂度分解，每次只关注其中的一小部分，降低编程难度。（设计模式的本质是对变量名进行管理，理论上讲，如果编程者的记忆力足够强、编程者之间的沟通效率足够高，则这些所谓的“设计模式”都可以省略）</p>
<p>　　B、在webGLStart方法中对场景初始化流程进行了划分，各个流程如注释所示：</p>
<pre><code class="copyable"> 1 //对象框架架构
 2     function webGLStart()
 3     &#123;
 4         //initWebSocket();//如何确保上一环结成功才开启下一环节？
 5         initScene();//初始化场景，包括最初入门教程里的那些东西
 6         initArena();//初始化地形，包括天空盒，参照物等
 7         initEvent();//初始化事件
 8         initUI();//初始化场景UI
 9         initObj();//初始化一开始存在的可交互的物体
10         initLoop();//初始化渲染循环
11         MyGame.init_state=1;//更新初始化状态
12         engine.hideLoadingUI();//隐藏载入UI
13         //MyGame.flag_startr=1;//这个是通过nohurry计时器自动启动的，不需要手动启动
14     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　C、初始化场景</p>
<pre><code class="copyable"> 1 function initScene()
 2     &#123;//光照
 3         var light0 = new BABYLON.HemisphericLight("light0", new BABYLON.Vector3(0, 1, 0), scene);
 4         light0.diffuse = new BABYLON.Color3(1,1,1);//这道“颜色”是从上向下的，底部收到100%，侧方收到50%，顶部没有
 5         light0.specular = new BABYLON.Color3(0,0,0);
 6         light0.groundColor = new BABYLON.Color3(1,1,1);//这个与第一道正相反
 7         MyGame.lights.light0=light0;//将光照变量交给MyGame对象管理
 8         mesh_arr_cards=new BABYLON.Mesh("mesh_arr_cards", scene);
 9         //相机对象
10         var camera0= new BABYLON.FreeCamera("FreeCamera", new BABYLON.Vector3(0, 0, 0), scene);
11         //camera0.layerMask = 2;
12         //camera0.position=new BABYLON.Vector3(0, 0, -20);
13         camera0.minZ=0.001;
14         scene.activeCameras.push(camera0);
15         
16         //用BallMan作为CameraMesh的mesh
17         var player = new BallMan();
18         var obj_p=&#123;&#125;;//初始化参数
19         //计划不使用物理引擎
20         var mesh_ballman=new BABYLON.Mesh("mesh_ballman",scene);
21         obj_p.mesh=mesh_ballman;
22         obj_p.name="本机";//显示的名字
23         obj_p.id="本机";//WebSocket Sessionid
24         obj_p.image="../ASSETS/IMAGE/Rainbow.jpg";
25         player.init(
26                 obj_p,scene
27         );
28 
29         var cameramesh=new CameraMesh();
30         var obj_p=&#123;&#125;;//初始化参数
31         obj_p.mesh=mesh_ballman;
32         obj_p.mesh.isVisible=false;
33         obj_p.mesh.position=new BABYLON.Vector3(0,0,-20);
34         if(obj_p.mesh.ballman)
35         &#123;
36             obj_p.mesh.ballman.head.position=obj_p.mesh.position.clone();
37         &#125;
38         obj_p.methodofmove="host20171018";
39         obj_p.name="FreeCamera";//显示的名字
40         obj_p.id="FreeCamera";//WebSocket Sessionid
41         obj_p.camera=camera0;
42         //obj_p.image="assets/image/play.png";
43         obj_p.flag_objfast=5;
44         cameramesh.init(
45                 obj_p,scene
46         );
47         MyGame.arr_myplayers[obj_p.name]=cameramesh;
48         MyGame.player=cameramesh;
49         MyGame.Cameras.camera0=camera0;
50         camera0.position=cameramesh.mesh.position.clone();
51         cameramesh.mesh.rotation=camera0.rotation.clone();
52         mesh_arr_cards.position=MyGame.player.mesh.ballman.backview._absolutePosition.clone();
53     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　其中mesh_arr_cards是所有手牌的父网格，用来对手牌进行定位，事实上这个对象放在initArena或者initObj阶段更加合理，但是因为相机对象的一些事件和这个网格有关，只好放在场景初始化阶段。BallMan的外观是一个球体网格，用来代表场景中的玩家，其用法可以参考https://www.cnblogs.com/ljzc002/p/7274455.html；CameraMesh是一个网格与相机的结合体，在第三人称时用户将能看见自己操纵的单位（关于BallMan和CameraMesh类的参数将在后面详细介绍）。最后把各种对象都交给MyGame统一管理。</p>
<p>　　D、初始化环境</p>
<pre><code class="copyable"> 1 function initArena()
 2     &#123;
 3         var mesh_base=new BABYLON.MeshBuilder.CreateSphere("mesh_base",&#123;diameter:1&#125;,scene);
 4         mesh_base.material=MyGame.materials.mat_green;
 5         mesh_base.position.x=0;
 6         mesh_base.renderingGroupId=2;
 7         //mesh_base.layerMask=2;
 8         var mesh_base1=new BABYLON.MeshBuilder.CreateSphere("mesh_base1",&#123;diameter:1&#125;,scene);
 9         mesh_base1.position.y=10;
10         mesh_base1.position.x=0;
11         mesh_base1.material=MyGame.materials.mat_green;
12         mesh_base1.renderingGroupId=2;
13         //mesh_base1.layerMask=2;
14         var mesh_base2=new BABYLON.MeshBuilder.CreateSphere("mesh_base2",&#123;diameter:1&#125;,scene);
15         mesh_base2.position.y=-10;
16         mesh_base2.position.x=0;
17         mesh_base2.material=MyGame.materials.mat_green;
18         mesh_base2.renderingGroupId=2;
19         //mesh_base2.layerMask=2;
20         for(var i=0;i<5;i++)//建立五个标示组号的标记网格，标记从一（而不是零）开始
21         &#123;
22             var plane=new BABYLON.MeshBuilder.CreatePlane("mesh_groupicon"+(i+1),&#123;size:5&#125;,scene);
23             var mat_plane = new BABYLON.StandardMaterial("mat_plane"+(i+1), scene);
24             var texture_plane= new BABYLON.DynamicTexture("texture_plane"+(i+1), &#123;width:100, height:100&#125;, scene);
25             mat_plane.diffuseTexture =texture_plane;
26             plane.material=mat_plane;
27             var font = "bold 60px monospace";
28             texture_plane.drawText((i+1), 40, 70, font, "white", "green", true, true);//第一个是文字颜色，第二个则是完全填充的背景色
29             plane.position.x=-16;
30             plane.position.z=-2;
31             plane.renderingGroupId=2;
32             //plane.rotation.x=-Math.PI/2;//这会导致自由相机的视角发生bug？？Y与Z轴混淆？
33             plane.isPickable=false;
34             plane.isVisible=false;
35             arr_mesh_groupicon.push(plane);
36             //plane.parent=mesh_arr_cards;
37         &#125;
38     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　建立了三个小绿球作为场景的参照物，建立了五个小平面作为分组标记，这五个标记暂时不可见（在调试分组标记的过程中Babylon.js发生了bug，相机输入的Y轴和Z轴发生混淆，但没有深入分析原因）。</p>
<p>　　E、初始化事件</p>
<pre><code class="copyable"> 1 function initEvent()
 2     &#123;
 3         InitMouse();
 4         window.addEventListener("keydown", onKeyDown, false);//按键按下
 5         window.addEventListener("keyup", onKeyUp, false);//按键抬起
 6         window.addEventListener("resize", function () &#123;
 7             if (engine) &#123;
 8                 engine.resize();
 9             &#125;
10         &#125;,false);
11     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　InitMouse中是对鼠标的四种事件监听，具体代码在Control20180312.js文件中，接下来监听了按键按下、按键抬起、窗口尺寸变化。</p>
<p>　　F、初始化UI</p>
<pre><code class="copyable">1 function initUI()
2     &#123;
3         MakeFullUI();
4         //var advancedTexture = MyGame.fsUI;
5 
6     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　代码主体在FullUI.js文件中</p>
<p>　　G、初始化对象</p>
<pre><code class="copyable">1 function initObj()
2     &#123;//添加75个（？）实验对象
3 
4         DrawCard4();
5         SortCard();
6     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　具体代码在DrawCard.js中</p>
<p>　　H、初始化渲染循环（也是逻辑循环）</p>
<pre><code class="copyable"> 1 function initLoop()
 2     &#123;
 3         var _this=MyGame;
 4         scene.registerBeforeRender(function() &#123;     //比runRenderLoop更早
 5         &#125;);
 6         scene.registerAfterRender(
 7                 function() &#123;
 8                     if(MyGame.flag_startr==1)//如果开始渲染了
 9                     &#123;//如果正在使用相机网格进行漫游
10                         if(MyGame.player.prototype=CameraMesh&&MyGame.flag_view=="first_lock")
11                         &#123;
12                             host20171018(MyGame.player);
13                         &#125;
14                     &#125;
15                 &#125;
16         );
17 
18         engine.runRenderLoop(function ()        //场景逻辑和AI也从这里引入
19         &#123;
20             if (divFps) &#123;
21                 // Fps
22                 divFps.innerHTML = engine.getFps().toFixed() + " fps";
23             &#125;
24             MyGame.HandleNoHurry();//这里包含了运动使用的计时器
25             if(_this.flag_startr==1||_this.flag_view!="first_pick")
26             &#123;
27                 //主相机和小地图相机都随着玩家的位置变化
28                 CamerasFollowActor(_this.player);
29             &#125;
30 
31             _this.scene.render();
32 
33         &#125;);
34     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 　　其中registerBeforeRender是在每一帧渲染之前执行的代码，registerAfterRender是在每一帧渲染之后执行的代码，除了scene之外mesh类对象也可以使用这样的方法，这也意味着可以将渲染前后的代码分散写在多个地方，但这里为了方便管理统一写在一处。host20171018是根据按键状态和视角计算player运动的方法，具体代码在Moves.js文件中。</p>
<p>　　runRenderLoop里是每一帧渲染时执行的代码，这里首先更新了当前帧数显示，然后通过HandleNoHurry（代码在Game类中）执行一些“需要周期性执行，但没有必要每一帧都执行的代码”，接下来通过CamerasFollowActor（Moves.js文件中）让“和player关联但不是player子元素”的其他对象跟随player运动，最后调用场景的渲染方法。</p>
<p> </p>
<p>　　关于运动，上述代码的计算流程是这样的：</p>
<p>　　player的position-》计算出player的_absolutePosition(?)-》registerBeforeRender-》根据player的_absolutePosition计算关联对象的新位置-》渲染-》registerAfterRender-》host20171018更新player的position。</p>
<p>　　考虑到player也许是其他元素的子元素，其position（位置）和_absolutePosition（绝对位置）可能不同（相差物体的世界矩阵），需要使用_absolutePosition来定位关联对象；而Babylon.js根据position计算_absolutePosition的操作发生在registerBeforeRender之前，所以如果我们把host20171018放在registerBeforeRender中则会导致position更新而_absolutePosition仍为旧的，表现的效果就是相机运动时对象抖动。所以我们把host20171018放在registerAfterRender中，当然如果position和_absolutePosition完全相同，则从理论上讲不存在这种限制，但并未测试过。</p>
<p>3、Game类</p>
<p>　　A、初始化方法：</p>
<pre><code class="copyable"> 1 Game=function(init_state,flag_view,wsUri,h2Uri)
 2 &#123;//参数：初始化时的状态代号，初始化时的浏览模式，webSocket的服务器地址，h2数据库地址
 3     var _this = this;
 4     this.scene=scene;
 5     this.loader =  new BABYLON.AssetsManager(scene);//资源管理器，用于预先加载资源
 6     //控制者数组
 7     this.arr_myplayers=&#123;&#125;;
 8     this.arr_npcs=&#123;&#125;;//NPC数组
 9     this.count=&#123;&#125;;//综合计数器对象
10     this.count.count_name_npcs=0;//NPC命名计数器，每产生一个NPC则加一，避免NPCID重复
11     this.Cameras=&#123;&#125;;//scene里也有？，综合相机对象
12     this.websocket;
13     this.lights=&#123;&#125;;//综合光源对象
14     this.fsUI=BABYLON.GUI.AdvancedDynamicTexture.CreateFullscreenUI("ui1");//全屏GUI对象
15     this.hl=new BABYLON.HighlightLayer("hl1", scene);//高光层对象，下面是高光层的一些参数
16     this.hl.blurVerticalSize = 1.0;//这个影响的并不是高光的粗细程度，而是将它分成 多条以产生模糊效果，数值表示多条间的间隙尺寸
17     this.hl.blurHorizontalSize =1.0;
18     this.hl.innerGlow = false;//取消内部光晕
19     this.hl.alphaBlendingMode=3;
20     //this.hl.isStroke=true;
21     //this.hl.blurTextureSizeRatio=2;
22     //this.hl.mainTextureFixedSize=100;
23     //this.hl.renderingGroupId=3;
24     //this.hl._options.mainTextureRatio=1000;
25 
26     this.wsUri=wsUri;
27     this.init_state=init_state;//当前运行状态
28     /*0-startWebGL
29     1-WebGLStarted
30     2-PlanetDrawed
31      * */
32     this.h2Uri=h2Uri;
33     //我是谁
34     this.WhoAmI=newland.randomString(8);
35 
36     this.materials=&#123;&#125;;//综合材质对象，下面初始化了几种常用的材质
37     var mat_frame = new BABYLON.StandardMaterial("mat_frame", scene);
38     mat_frame.wireframe = true;
39     this.materials.mat_frame=mat_frame;
40     var mat_red=new BABYLON.StandardMaterial("mat_red", scene);
41     mat_red.diffuseColor = new BABYLON.Color3(1, 0, 0);
42     var mat_green=new BABYLON.StandardMaterial("mat_green", scene);
43     mat_green.diffuseColor = new BABYLON.Color3(0, 1, 0);
44     var mat_blue=new BABYLON.StandardMaterial("mat_blue", scene);
45     mat_blue.diffuseColor = new BABYLON.Color3(0, 0, 1);
46     this.materials.mat_red=mat_red;
47     this.materials.mat_green=mat_green;
48     this.materials.mat_blue=mat_blue;
49 
50     this.models=&#123;&#125;;//综合模型对象
51     this.textures=&#123;&#125;;//综合纹理对象
52     this.texts=&#123;&#125;;//综合文本对象
53 
54     this.flag_startr=0;//开始渲染并且地形初始化完毕
55     this.flag_starta=0;//开始执行NPC的AI逻辑
56     this.list_nohurry=[];//需要周期性进行的工作
57     this.nohurry=0;//一个计时器，让一些计算不要太频繁
58     this.flag_online=false;//是否是在线场景
59     this.flag_view=flag_view;//first/third/input/free
60     this.flag_controlEnabled = false;
61     this.arr_keystate=[];//按键状态数组
62 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这段代码中初始化了一些场景中可能会用到的变量，最整洁的情况是把所有的全局变量都作为MyGame的属性加以管理，但很难做到。</p>
<p>　　B、原型方法：</p>
<p>　　　　每个Game类的实例都会继承这些方法：</p>
<pre><code class="copyable"> 1 Game.prototype=&#123;
 2     AddNohurry:function(name,delay,lastt,todo,count)
 3     &#123;//名字，每次执行之间的间隔（最小间隔），上一次执行时间，要执行的函数名，已经执行的次数
 4         if(this.list_nohurry[name])//如果已经有叫做这个名字的任务
 5         &#123;
 6             return;
 7         &#125;
 8         this.list_nohurry[name]=&#123;delay:delay,lastt:lastt,todo:todo
 9             ,count:count&#125;;
10     &#125;,
11     RemoveNohurry:function(name)
12     &#123;
13         delete this.list_nohurry[name];
14     &#125;,
15     HandleNoHurry:function()
16     &#123;
17         var _this=this;
18         if( _this.flag_startr==0)//开始渲染并且地形初始化完毕！！
19         &#123;
20             engine.hideLoadingUI();//隐藏载入UI
21             _this.flag_startr=1;//标志开始渲染
22             _this.lastframet=new Date().getTime();
23             _this.firstframet=_this.lastframet;
24             _this.DeltaTime=0;
25         &#125;
26         else
27         &#123;//如果已经开始渲染
28             _this.currentframet=new Date().getTime();//当前帧的时间
29             _this.DeltaTime=_this.currentframet-_this.lastframet;//取得两帧之间的时间
30             _this.lastframet=_this.currentframet;
31             /*_this.nohurry+=_this.DeltaTime;//这个代码用于只执行一个定时任务的情况
32 
33             if(MyGame&&_this.nohurry>1000)//每一秒进行一次
34             &#123;
35                 _this.nohurry=0;
36 
37             &#125;*/
38             //var time_start=_this.currentframet-_this.firstframet;//当前时间到最初过了多久
39             for(var i=0;i<_this.list_nohurry.length;i++)//对于每一个定时任务
40             &#123;
41                 var obj_nohurry=_this.list_nohurry[i];
42                 if(obj_nohurry.lastt==0)//如果上次执行时间是0，则以当前时间作为上次执行时间
43                 &#123;
44                     obj_nohurry.lastt=new Date().getTime();
45                 &#125;
46                 else
47                 &#123;
48                     var time_start=_this.currentframet-obj_nohurry.lastt;//当前帧到上次执行经过的时间
49                     if(time_start>obj_nohurry.delay)//如果经过的时间超过了每次执行周期乘以执行次数加一，则执行一次
50                     &#123;
51                         obj_nohurry.todo();
52                         obj_nohurry.count++;
53                         obj_nohurry.lastt=_this.currentframet;
54                         break;//每一帧最多只做一个费时任务，周期更短的任务放在list_nohurry队列前面，获得更多执行机会
55                     &#125;
56                 &#125;
57 
58             &#125;
59             if(_this.flag_starta==1)//除非开始进行ai计算，否则只处理和基本ui有关的内容
60             &#123;
61 
62             &#125;
63         &#125;
64     &#125;
65 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 　　这里的三个方法都是和定时任务有关的，将需要执行的定时任务放在list_nohurry中，在引擎每一次渲染循环时检测是否需要执行队列中的任务，因为要尽量减少每一帧的时间差异，规定每一帧最多只执行一个任务，到时但未执行的任务需要延后到下一帧判断是否执行，队列中越靠前的任务被及时执行的可能性越高。</p>
<p>　　上述方法并没有实际使用过，一个类似的执行定时任务的例子可以在https://www.cnblogs.com/ljzc002/p/7373046.html查看。</p>
<p>4、object类：</p>
<p>　　object类是场景中所有受控物体的基类，包含运动控制和姿态控制所需的一些信息，其代码位于newland.js文件中。</p>
<p>　　A、初始化代码：</p>
<pre><code class="copyable"> 1 newland.object=function()
 2 &#123;
 3 
 4 &#125;
 5 newland.object.prototype.init = function(param)
 6 &#123;
 7     //启用物理引擎后这一部分可能用不上，但暂时保留
 8     this.keys=&#123;w:0,s:0,a:0,d:0,space:0,ctrl:0,shift:0&#125;;//按键是否保持按下，已经改为由MyGame管理
 9     this.witha0=&#123;forward:0,right:0,up:-9.82&#125;;//非键盘控制产生的加速度
10     this.witha=&#123;forward:0,right:0,up:-9.82&#125;;//环境加速度，包括地面阻力和重力，现在还没有风力
11     this.witha2=&#123;forward:0,right:0,up:0&#125;;//键盘控制加速度与物体本身加速度和非键盘控制产生的加速度合并后的最终加速度
12     this.v0=&#123;forward:0,right:0,up:0&#125;;//上一时刻的速度
13     this.vt=&#123;forward:0,right:0,up:0&#125;;//下一时刻的速度
14     this.vm=&#123;forward:15,backwards:5,left:5,right:5,up:100,down:100&#125;;//各个方向的最大速度
15     this.fm=&#123;forward:2,backwards:1,left:1,right:1,up:10,down:10&#125;;//各个方向的最大发力
16     this.ff=0.05;//在地面不做任何发力时的阻力效果
17     //this.flag_runfast=1;//速度系数
18     this.ry0=0;//上一时刻的y轴转角
19     this.ryt=0;//下一时刻的y轴转角
20     this.rychange=0;//y轴转角差
21     this.mchange=&#123;forward:0,right:0,up:0&#125;;//物体自身坐标系上的位移
22     this.vmove=new BABYLON.Vector3(0,0,0);//世界坐标系中每一时刻的位移和量
23     this.py0=0;//记录上一时刻的y轴位置，和下一时刻比较确定物体有没有继续向下运动！！，用于判断物体是否接触地面
24 
25     param = param || &#123;&#125;;
26     this.mesh=param.mesh;
27     this.meshname=this.mesh.name;
28     this.skeletonsPlayer=param.skeletonsPlayer||[];//如果和某个Babylon.js模型关联，则提取模型的骨骼动画
29     this.submeshs=param.submeshs;//提取子网格
30     this.ry0=param.mesh.rotation.y;
31     this.py0=param.mesh.position.y;
32     this.flag_runfast=param.flag_runfast ||1;//速度系数，最终位移要乘以速度系数
33     this.standonTheGround=0;//一开始在空中，落到地上，是否接触地面
34     //this.flag_objfast=param.flag_objfast ||1;
35     this.countstop=0;//记录物体静止了几次，如果物体一直静止就停止发送运动信息，在联网情况下减少数据传输
36 
37     this.PlayAnnimation = false;//是否在执行动画
38     this.methodofmove=param.methodofmove||"";//运动算法
39     this.path_goto="sleep";//这个物体接到指令要去哪里,是一个向量数组（路径），在寻路算法中使用
40 
41     //window.addEventListener("keydown", onKeyDown, false);//按键按下
42     //window.addEventListener("keyup", onKeyUp, false);//按键抬起
43 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这里将一些物体可能用到的变量保存在基类中，减化了子类物体的创建代码。</p>
<p>　　B、其他原型方法</p>
<pre><code class="copyable"> 1 //骨骼动画
 2 newland.object.prototype.beginSP=function(num_type)//执行骨骼动画列表里的某一个骨骼动画
 3 &#123;
 4     if(this.skeletonsPlayer.length>0)
 5     &#123;
 6         this.sp = this.skeletonsPlayer[num_type];
 7 
 8         this.totalFrame = this.skeletonsPlayer[0]._scene._activeSkeletons.data.length;//总帧数
 9         this.start = 0;
10         this.end = 100;
11         this.VitesseAnim = parseFloat(100 / 100);//动画的速度比
12         scene.beginAnimation(this.sp, (100 * this.start) / this.totalFrame, (100 * this.end) / this.totalFrame, true, this.VitesseAnim);//启动动画，skeletonsPlayer是一个骨骼动画对象
13         this.PlayAnnimation = true;
14     &#125;
15     else
16     &#123;//本体不能启动骨骼动画，则直接启动其子元素的骨骼动画
17         var len=this.submeshs.length;
18         for(var i=0;i<len;i++)
19         &#123;
20             var skeleton=this.submeshs[i].skeleton;
21             var totalFrame = skeleton._scene._activeSkeletons.data.length;//总帧数
22             var start = 0;
23             var end = 100;
24             var VitesseAnim = parseFloat(100 / 100);//动画的速度比
25             scene.beginAnimation(skeleton, (100 * start) / totalFrame, (100 * end) / totalFrame, true, VitesseAnim);
26         &#125;
27         this.PlayAnnimation = true;
28     &#125;
29 &#125;
30 newland.object.prototype.stopSP=function(num_type)
31 &#123;
32     this.PlayAnnimation = false;
33     if(this.skeletonsPlayer.length>0)
34     &#123;
35         scene.stopAnimation(this.skeletonsPlayer[0]);
36     &#125;
37     else
38     &#123;
39         var len=this.submeshs.length;
40         for(var i=0;i<len;i++)
41         &#123;
42             var skeleton=this.submeshs[i].skeleton;
43             scene.stopAnimation(skeleton);
44         &#125;
45     &#125;
46 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　object类具有两个和骨骼动画相关的原型方法，用来控制骨骼动画的启停（方法编程时间较早，在新版Babylon.js中也许会有错误）</p>
<p>5、BallMan类：</p>
<p>　　BallMan类是object类的一个子类，主要用来在不载入模型的情况下，用简单的球体网格进行物体移动、视角变化、对象拾取等试验。代码位于Character.js文件中。</p>
<p>　　A、初始化代码：</p>
<pre><code class="copyable"> 1 BallMan=function()//只用来显示其他玩家？-》自己也要显示
 2 &#123;
 3     newland.object.call(this);//调用父类的构造方法
 4 &#125;
 5 BallMan.prototype=new newland.object();//继承父类的属性
 6 BallMan.prototype.init=function(param,scene)
 7 &#123;
 8     param = param || &#123;&#125;;
 9     newland.object.prototype.init.call(this,param);//调用父类的初始化方法
10     this.name=param.name;
11     this.id=param.id;
12     //this.vd=&#123;forward:10.0,backwards:10.0,left:10.0,right:10.0,up:10.0,down:10.0&#125;;//简单运动时各个方向的默认速度
13     //this.flag_objfast=param.flag_objfast ||1;//使用这种机体移动物体的默认速度
14 
15     var mat_head=new BABYLON.StandardMaterial("mat_head", scene);//球体（头部）的材质
16     mat_head.diffuseTexture =new BABYLON.Texture(param.image,scene);//将球体材质的漫反射纹理设置为一张图片
17     mat_head.freeze();//冻结材质，减少向显卡传递数据，据说能提升性能
18     var mesh_head=BABYLON.Mesh.CreateSphere(this.name+"head", 10,  2.0, scene);//建立一个球体
19     mesh_head.renderingGroupId=2;//渲染组设为2，这里规定隐形物体渲染组为0，远处的背景物体渲染组为1，普通物体行为2，特别强调的物体为3
20     mesh_head.layerMask=2;
21     //mesh_head.rotation.y=Math.PI*0.5;
22     mesh_head.material=mat_head;
23     //mesh_head.parent=this.mesh;//想让head随着ghost一起位移，又不想让它随着ghost滚动！！
24     //this.mesh.setPhysicsLinkWith(mesh_head,new BABYLON.Vector3(0,0,0),new BABYLON.Vector3(0,0,0));//枢轴链接
25     mesh_head.position=this.mesh.position.clone();//不克隆直接赋值有抖动
26     mesh_head.isPickable=false;//不可被选取
27     this.head=mesh_head;
28     this.mesh.ballman=this;
29 
30     //改用gui？显示名字
31     if(this.lab)
32     &#123;
33         this.lab.dispose();
34         this.lab=null;
35     &#125;
36     var label = new BABYLON.GUI.Rectangle(this.name);
37     label.background = "black";
38     label.height = "30px";
39     label.alpha = 0.5;
40     label.width = "100px";
41     label.cornerRadius = 20;
42     label.thickness = 1;
43     label.linkOffsetY = 30;//位置偏移量？？
44     MyGame.fsUI.addControl(label);
45     label.linkWithMesh(this.head);
46     var text1 = new BABYLON.GUI.TextBlock();
47     text1.text = this.name;
48     text1.color = "white";
49     label.addControl(text1);
50     label.isVisible=true;
51     label.layerMask=2;
52     this.lab=label;
53 
54     //定位第一人称视角的位置
55     var headview=new BABYLON.Mesh(this.name+"headview",scene);//用网格定义一个位置，位于这个位置的物体可以是headview的子元素，这样它将随着BallMan一起移动
56     headview.parent=this.head;
57     headview.position=new BABYLON.Vector3(0,0,2.0);
58     this.headview=headview;
59     //定位第三人称视角的位置
60     var backview=new BABYLON.Mesh(this.name+"backview",scene);
61     backview.parent=this.head;
62     backview.position=new BABYLON.Vector3(0,2,-6);
63     this.backview=backview;
64     var backview_right=new BABYLON.Mesh(this.name+"backview_right",scene);
65     backview_right.parent=this.head;
66     backview_right.position=new BABYLON.Vector3(2.6,2,-6);
67     this.backview_right=backview_right;
68     //定位手持物体的位置
69     var handpoint=new BABYLON.Mesh(this.name+"handpoint",scene);
70     handpoint.parent=this.head;
71     handpoint.position=new BABYLON.Vector3(0,0,10);
72     this.handpoint=handpoint;
73     //左手和右手
74     var lefthand=new BABYLON.Mesh(this.name+"lefthand",scene);
75     lefthand.parent=this.head;
76     lefthand.position=new BABYLON.Vector3(-1,0.2,3.0);
77     lefthand.lookAt(lefthand.position.negate().add(headview.position));
78     this.lefthand=lefthand;
79     var righthand=new BABYLON.Mesh(this.name+"righthand",scene);
80     righthand.parent=this.head;
81     righthand.position=new BABYLON.Vector3(1,0.2,3.0);
82     righthand.lookAt(righthand.position.negate().add(headview.position));
83     this.righthand=righthand;
84 
85     //暂时不使用抬头显示器
86     console.log("Player初始化完毕");
87 
88 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　关于渲染组的材料可以查看Babylon.js官网关于网格渲染顺序的文档（Transparency and How Meshes Are Rendered），可以在这里下载简单的中英对照http://down.51cto.com/data/2452124</p>
<p>　　代码的中部用GUI绘制了一个显示玩家名字的文本框，并设置文本框跟随BallMan（关于2DGUI资料可以查看https://www.cnblogs.com/ljzc002/p/7699162.html，前段时间Babylon.js官方推出了新的3DGUI，但是仍然以2DGUI为基础，并没有突破性的进展）。</p>
<p>　　代码后部为BallMan的头部（需要注意BallMan的头部是网格，而BallMan对象并不是）添加了一系列子元素（这里的_children不叫做“子网格”是为了防止和前面的subMesh相区分，前者指子元素使用父网格的局部坐标系，后者则指将父网格分为不同的区块，每个区块使用不同的材质），用来表示BallMan身上的各个位置。</p>
<p>6、CameraMesh类</p>
<p>　　CameraMesh类也是object的子类，用来给相机绑定一个网格，这样一方面玩家可以在第三人称操作时看到自身，另一方面可以使用网格一些物理引擎方法。CameraMesh类的代码在Character.js文件中。在这个工程中我将一个BallMan网格绑定给了相机。</p>
<p>　　A、初始化方法：</p>
<pre><code class="copyable"> 1 /*20180613现在规定主相机在MyGame中对应三种状态：
 2 first_lock表示相机和相机网格绑定在一起并使用Control控制，
 3  4 first_ani表示由动画控制相机相机不可手动控制
 5 first_pick表示相机位置不可以移动，但是可以改变视角进行点击（是在没有锁定指针属性时的替代方法？？）*/
 6 CameraMesh=function()
 7 &#123;
 8     newland.object.call(this);
 9 &#125;
10 CameraMesh.prototype=new newland.object();
11 CameraMesh.prototype.init=function(param,scene)
12 &#123;
13     param = param || &#123;&#125;;
14     newland.object.prototype.init.call(this,param);//继承原型的方法
15     this.name=param.name;
16     this.id=param.id;
17     var num_v=0.001;
18     this.vd=&#123;forward:num_v*2,backwards:num_v,left:num_v,right:num_v,up:num_v,down:num_v&#125;;//简单运动时各个方向的默认速度，最慢的情况下每一毫秒移动多少
19     this.flag_objfast=param.flag_objfast ||1;//使用这种机体移动物体的默认速度
20     this.camera=param.camera;
21     this.mesh=param.mesh;//可以把这个mesh指定为BallMan！！！！
22     this.camera.mesh=this.mesh;
23     var _this = this;
24     //中间光标，准星
25     this.centercursor=this.CenterCursor();
26     this.centercursor.isVisible=false;
27     this._initPointerLock();//先不要锁定光标，等初始化地形完毕后再锁定？
28 
29     console.log("相机网格初始化完毕");
30 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">　　CameraMesh.prototype.handleUserMouse=function(evt, pickInfo)
　　&#123;
    　　//this.weapon.fire(pickInfo);//FPS和TPS的武器射击同样由这个类负责
　　&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　在25行附近使用GUI在窗口的中心绘制了一个准星：</p>
<pre><code class="copyable"> 1 //准心
 2 CameraMesh.prototype.CenterCursor=function()
 3 &#123;
 4     //在屏幕中心绘制一个光标
 5     var rect_centor=new BABYLON.GUI.Rectangle();
 6     rect_centor.width = "80px";
 7     rect_centor.height = "80px";
 8     rect_centor.alpha=0.5;
 9     rect_centor.color="blue";
10     MyGame.fsUI.addControl(rect_centor);
11 
12     var rect_line1=new BABYLON.GUI.Rectangle();//GUI不能直接绘制线段，所以用一个细长的矩形表示线段
13     rect_line1.width = "2px";
14     rect_line1.height = "20px";
15     rect_line1.color = "black";
16     rect_line1.thickness = 4;
17     rect_line1.alpha = 0.5;
18     rect_line1.verticalAlignment=BABYLON.GUI.Control.VERTICAL_ALIGNMENT_TOP;
19     rect_centor.addControl(rect_line1);
20     var rect_line2=new BABYLON.GUI.Rectangle();
21     rect_line2.width = "2px";
22     rect_line2.height = "20px";
23     rect_line2.color = "black";
24     rect_line2.thickness = 4;
25     rect_line2.alpha = 0.5;
26     rect_line2.verticalAlignment=BABYLON.GUI.Control.VERTICAL_ALIGNMENT_BOTTOM;
27     rect_centor.addControl(rect_line2);
28     var rect_line3=new BABYLON.GUI.Rectangle();
29     rect_line3.width = "20px";
30     rect_line3.height = "2px";
31     rect_line3.color = "black";
32     rect_line3.thickness = 4;
33     rect_line3.alpha = 0.5;
34     rect_line3.horizontalAlignment=BABYLON.GUI.Control.HORIZONTAL_ALIGNMENT_LEFT;
35     rect_centor.addControl(rect_line3);
36     var rect_line4=new BABYLON.GUI.Rectangle();
37     rect_line4.width = "20px";
38     rect_line4.height = "2px";
39     rect_line4.color = "black";
40     rect_line4.thickness = 4;
41     rect_line4.alpha = 0.5;
42     rect_line4.horizontalAlignment=BABYLON.GUI.Control.HORIZONTAL_ALIGNMENT_RIGHT;
43     rect_centor.addControl(rect_line4);
44     return rect_centor;
45 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　B、光标锁定</p>
<p>　　Babylon.js的默认相机要求用户一直按下鼠标拖拽，才能改变相机视角，显然这在FPS、TPS之类场景中是很不方便的，所以要使用浏览器的光标锁定功能将光标锁定在屏幕中心，并一直保持拖拽状态。</p>
<p>　　首先在相机网格初始化时直接进行光标锁定，并且设置为点击窗口则锁定光标（用于焦点离开浏览器后返回的情况）</p>
<pre><code class="copyable"> 1 //锁定光标
 2 CameraMesh.prototype._initPointerLock =function() &#123;
 3     var _this = this;
 4     //这个监听只是用来获取焦点的？从降低耦合的角度来讲，全局事件监听并不应该放在角色类里！！！！
 5     canvas.addEventListener("click", function(evt) &#123;//这个监听也会在点击GUI按钮时触发！！
 6         if(MyGame.init_state==1||MyGame.init_state==2)//点击canvas则锁定光标，在因为某种原因在first_lock状态脱离焦点后用来恢复焦点
 7         &#123;//不锁定指针时，这个监听什么也不做
 8             if(MyGame.flag_view!="first_pick")
 9             &#123;//不同浏览器中canvas锁定光标的方法不同
10                 canvas.requestPointerLock = canvas.requestPointerLock || canvas.msRequestPointerLock || canvas.mozRequestPointerLock || canvas.webkitRequestPointerLock;
11                 if (canvas.requestPointerLock) &#123;
12                     canvas.requestPointerLock();
13 
14                         MyGame.flag_view="first_lock";
15 
16                     _this.centercursor.isVisible=true;//将准星设为可见
17                 &#125;
18             &#125;
19             else//在非锁定光标时，click监听似乎不会被相机阻断
20             &#123;
21                 if(MyGame.flag_view=="first_ani")//由程序控制视角的动画时间
22                 &#123;
23                     cancelPropagation(evt);
24                     cancelEvent(evt);
25                     return;
26                 &#125;
27                 //var width = engine.getRenderWidth();
28                 //var height = engine.getRenderHeight();
29                 var pickInfo = scene.pick(scene.pointerX, scene.pointerY, null, false, MyGame.Cameras.camera0);//点击信息，取屏幕中心信息而不是鼠标信息！！
30                 if(MyGame.init_state==1&&MyGame.flag_view=="first_pick"
31                     &&pickInfo.hit&&pickInfo.pickedMesh.name.substr(0,5)=="card_"&&pickInfo.pickedMesh.card.belongto==MyGame.WhoAmI)//在一个卡片上按下鼠标，按下即被选中
32                 &#123;
33                     cancelPropagation(evt);
34                     cancelEvent(evt);
35                     //releaseKeyState();
36                     var mesh=pickInfo.pickedMesh;
37                     var card=mesh.card;
38                     PickCard(card);//相机会阻断鼠标按下，但不阻断鼠标点击
39                 &#125;
40             &#125;
41         &#125;
42 
43     &#125;, false);
44     //一开始直接锁定光标
45     canvas.requestPointerLock = canvas.requestPointerLock || canvas.msRequestPointerLock || canvas.mozRequestPointerLock || canvas.webkitRequestPointerLock;
46     if (canvas.requestPointerLock) &#123;
47         canvas.requestPointerLock();
48         MyGame.flag_view = "first_lock";
49         _this.centercursor.isVisible = true;
50         mesh_arr_cards.parent=this.mesh.ballman.backview;//一开始将所有手牌背在身后
51     &#125;
52 
53     // Event listener when the pointerlock is updated.当光标锁定状态发生改变时触发这一事件
54     var pointerlockchange = function (event) &#123;
55         //if(MyServer.flag_view=="first_lock")
56         //&#123;//不锁定指针时，这个监听什么也不做
57         _this.controlEnabled = (document.mozPointerLockElement === canvas || document.webkitPointerLockElement === canvas || document.msPointerLockElement === canvas || document.pointerLockElement === canvas);
58         if (!_this.controlEnabled) &#123;
59             //_this.camera.detachControl(canvas);//解除控制，在first_pick时还是要保持操纵性
60         &#125; else &#123;
61             _this.camera.attachControl(canvas,true);//将canvas的事件交给这个相机处理
62         &#125;
63         //&#125;
64     &#125;;
65     document.addEventListener("pointerlockchange", pointerlockchange, false);
66     document.addEventListener("mspointerlockchange", pointerlockchange, false);
67     document.addEventListener("mozpointerlockchange", pointerlockchange, false);
68     document.addEventListener("webkitpointerlockchange", pointerlockchange, false);
69 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这里将全局click监听放在了相机网格类里，事实上这个监听应该放在</p>
<p>Control20180312.js文件中更为合理。</p>
<p>　　另外在实验中发现Babylon.js的相机控制会拦截页面的“鼠标按下”事件（用来拖动视角），所以不能用鼠标按下事件来选取卡牌，所以使用click事件来选取卡牌。</p>
<p>　　另一方面在Control20180312.js中设置了按下Alt键切换浏览模式，浏览模式改变时光标锁定状态也要变化：</p>
<pre><code class="copyable"> 1 //执行时切换锁定状态和锁定状态的监听
 2 CameraMesh.prototype._changePointerLock =function() &#123;
 3     var _this = this;
 4     if(MyGame.flag_view=="first_lock")
 5     &#123;
 6         document.exitPointerLock = document.exitPointerLock    ||
 7             document.mozExitPointerLock ||
 8             document.webkitExitPointerLock;
 9 
10         if (document.exitPointerLock) &#123;
11             document.exitPointerLock();//重复执行它能改变锁定状态吗？在非调试模式下不行（和焦点的变化有关？）改用专用的退出锁定方法
12         &#125;
13         //stopListening(canvas,"click",);//这里很难找到eventHandler
14         MyGame.flag_view="first_pick";
15         _this.camera.attachControl(canvas,true);
16         _this.centercursor.isVisible=false;
17         var len=mesh_arr_cards._children.length;
18         //mesh_arr_cards.parent=null;
19 
20         HandCard(0);//用动画方式显示手牌
21         //mesh_arr_cards.parent=this.mesh.ballman.handpoint;
22 
23     &#125;
24     else if(MyGame.flag_view=="first_pick")
25     &#123;
26         canvas.requestPointerLock = canvas.requestPointerLock || canvas.msRequestPointerLock || canvas.mozRequestPointerLock || canvas.webkitRequestPointerLock;
27         if (canvas.requestPointerLock) &#123;
28             canvas.requestPointerLock();//但是如果这一句是在调试中运行的，就不能起作用了，因为光标在另一个页面中！！
29         &#125;
30         MyGame.flag_view="first_lock";
31         _this.camera.attachControl(canvas,true);
32         _this.centercursor.isVisible=true;
33         var len=mesh_arr_cards._children.length;
34         MyGame.UiPanelr.button1.isVisible=false;
35         MyGame.UiPanelr.button2.isVisible=false;
36         mesh_arr_cards.position.y=0;
37         HandCard(1);
38         //mesh_arr_cards.parent=this.mesh.ballman.backview;//把手牌隐藏起来
39     &#125;
40 
41 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　其中HandCard是用动画显示手牌的方法，严格来讲这些调用也不应该放在CameraMesh类的代码里。</p>
<p>7、Control20180312.js文件</p>
<p>　　Control20180312中设置了鼠标和键盘的事件响应（主要是调用其他文件里的方法）</p>
<pre><code class="copyable">  1 //这里是处理键盘鼠标等各种操作，并进行转发的代码
  2 function InitMouse()
  3 &#123;
  4     canvas.addEventListener("mousedown", function(evt) &#123;//发现只有在光标锁定的状态下，这个鼠标按下才会触发，解除光标锁定后被相机阻断了事件传播？
  5         var width = engine.getRenderWidth();//这种pick专用于first_lock锁定光标模式！！！！
  6         var height = engine.getRenderHeight();
  7         var pickInfo = scene.pick(width/2, height/2, null, false, MyGame.Cameras.camera0);//点击信息，取屏幕中心信息而不是鼠标信息！！
  8         
  9         if(MyGame.init_state==1&&MyGame.flag_view=="first_lock")//在用host方法移动相机时，部分禁用了原本的相机控制
 10         &#123;
 11             cancelPropagation(evt);//阻止事件的传播
 12             cancelEvent(evt);//阻止事件的默认响应
 13         &#125;
 14         
 15     &#125;, false);
 16     canvas.addEventListener("mousemove", function(evt)&#123;
 17         var width = engine.getRenderWidth();
 18         var height = engine.getRenderHeight();
 19         var pickInfo = scene.pick(width/2, height/2, null, false, MyGame.Cameras.camera0);//点击信息
 20         if(MyGame.flag_view=="first_ani")
 21         &#123;
 22             cancelPropagation(evt);
 23             cancelEvent(evt);
 24             return;
 25         &#125;
 26         if(MyGame.init_state==2&&MyGame.flag_view=="first_lock")//
 27         &#123;
 28         &#125;
 29     &#125;,false);
 30     canvas.addEventListener("blur",function(evt)&#123;//监听失去焦点
 31         releaseKeyState();
 32     &#125;)
 33     canvas.addEventListener("focus",function(evt)&#123;//改为监听获得焦点，因为调试失去焦点时事件的先后顺序不好说
 34         releaseKeyState();
 35     &#125;)
 36 
 37 &#125;
 38 function onKeyDown(event)
 39 &#123;//在播放动画时禁用所有的按键、鼠标效果
 40     if(MyGame.flag_view=="first_ani")
 41     &#123;
 42         cancelPropagation(event);
 43         cancelEvent(event);
 44         return;
 45     &#125;
 46     if(MyGame.flag_view=="first_lock"||MyGame.flag_view=="first_pick")//||MyGame.flag_view=="first_free")
 47     &#123;
 48         
 49             cancelEvent(event);//覆盖默认按键响应
 50         
 51         var keyCode = event.keyCode;
 52         var ch = String.fromCharCode(keyCode);//键码转字符
 53         MyGame.arr_keystate[keyCode]=1;
 54         /*按键响应有两种，一种是按下之后立即生效的，一种是保持按下随时间积累的，第一种放在这里调度，第二种放在相应的控制类里*/
 55         if(keyCode==88)//切换武器
 56         &#123;
 57 
 58         &#125;
 59         else if(keyCode==18||keyCode==27)//alt切换释放锁定->改为切换view
 60         &#123;
 61             MyGame.player._changePointerLock();
 62             arr_pickedCards=[];
 63             card_firstpick=null;
 64             
 65         &#125;
 66         else if(keyCode>=49&&keyCode<=53)//如果按下数字键1-5
 67         &#123;
 68             if(MyGame.flag_view=="first_pick"&&arr_pickedCards.length>0)//如果这时选择了一些手牌
 69             &#123;
 70                 HandleGroup(keyCode);//对卡牌编组
 71 
 72             &#125;
 73         &#125;
 74     &#125;
 75 &#125;
 76 function onKeyUp()
 77 &#123;
 78     if(MyGame.flag_view=="first_ani")
 79     &#123;
 80         cancelPropagation(evt);
 81         cancelEvent(evt);
 82         return;
 83     &#125;
 84     if(MyGame.flag_view=="first_lock"||MyGame.flag_view=="first_pick")//||MyGame.flag_view=="first_free")//光标锁定情况下的第一人称移动
 85     &#123;
 86       
 87             cancelEvent(event);//覆盖默认按键响应
 88       
 89         var keyCode = event.keyCode;
 90         var ch = String.fromCharCode(keyCode);//键码转字符
 91         MyGame.arr_keystate[keyCode]=0;
 92     &#125;
 93 &#125;
 94 function releaseKeyState()//将所有激活的按键状态置为0
 95 &#123;
 96     for(key in MyGame.arr_keystate)
 97     &#123;
 98         MyGame.arr_keystate[key]=0;
 99     &#125;
100 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　因为不锁定光标时，Babylon.js相机会阻断鼠标按下事件，所以这里对鼠标按下的监听只能在first_lock浏览状态使用，目前还没有给它安排工作。需要注意的是在不锁定光标时，光标可以自由移动所以使用光标在窗口中的位置生成pickInfo，而锁定光标时则直接使用窗口的中心点生成pickInfo。</p>
<p>　　键盘按键的效果分为两种，一是按下则立即生效，比如按下空格角色立即跳起，一种则是按住时一直生效，比如按住空格角色持续向上飞行，前者直接调用相应的方法，后者则是改变按键状态数组的内容，然后由Moves.js里的代码对按键状态数组进行检查，以此计算相应的运动效果。</p>
<p>　　这段代码还监听了鼠标离开和移入浏览器的事件，这时所有按键的状态将被归零。</p>
<p>8、FullUI.js文件</p>
<p>　　在这个文件中使用GUI定义一些控制按钮，目前只有“向上两行”和“向下两行”两个按钮，未来应该会添加更多按钮。</p>
<pre><code class="copyable"> 1 //在这里详细设定全屏等级的UI效果
 2 function MakeFullUI()
 3 &#123;
 4     var advancedTexture = MyGame.fsUI;
 5     var UiPanel = new BABYLON.GUI.StackPanel();
 6     UiPanel.width = "220px";
 7     UiPanel.fontSize = "14px";
 8     UiPanel.horizontalAlignment = BABYLON.GUI.Control.HORIZONTAL_ALIGNMENT_RIGHT;
 9     UiPanel.verticalAlignment = BABYLON.GUI.Control.VERTICAL_ALIGNMENT_CENTER;
10     UiPanel.color = "white";
11     advancedTexture.addControl(UiPanel);
12     // ..
13     var button1 = BABYLON.GUI.Button.CreateSimpleButton("button1", "向上两行");
14     button1.paddingTop = "10px";
15     button1.width = "100px";
16     button1.height = "50px";
17     button1.background = "green";
18     button1.isVisible=false;
19     button1.onPointerDownObservable.add(function(state,info,coordinates) &#123;
20         if(MyGame.init_state==1)//如果完成了场景的初始化
21         &#123;
22             ScrollUporDown(0,1.8,2);//上下滚动
23         &#125;
24     &#125;);
25     UiPanel.addControl(button1);
26     UiPanel.button1=button1;
27     var button2 = BABYLON.GUI.Button.CreateSimpleButton("button2", "向下两行");
28     button2.paddingTop = "10px";
29     button2.width = "100px";
30     button2.height = "50px";
31     button2.background = "green";
32     button2.isVisible=false;
33     button2.onPointerDownObservable.add(function(state,info,coordinates) &#123;
34         if(MyGame.init_state==1)//如果完成了场景的初始化
35         &#123;
36             ScrollUporDown(1,1.8,2);
37         &#125;
38     &#125;);
39     UiPanel.addControl(button2);
40     UiPanel.button2=button2;
41     MyGame.UiPanelr=UiPanel;
42 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　需要注意的是Babylon.js并不支持父子元素之间isVisible属性的传递，虽然button1和button2都在UiPanel内部，但改变UiPanel的可见性并不会影响两个按钮。</p>
<p>9、Moves.js文件</p>
<p>　　A、计算运动效果</p>
<pre><code class="copyable"> 1 function host20171018(obj)//这里的obj是一个CameraMesh对象
 2 &#123;
 3     //MyGame.player.flag_objfast=Math.max(1,Math.abs(MyGame.Cameras.camera0.position.y/5));
 4     var arr_state=MyGame.arr_keystate;//键盘状态数组
 5     var rad_y=parseFloat(obj.mesh.rotation.y);
 6     var v_obj=&#123;x:0,z:0,y:0&#125;;//物理模型在自身坐标系中的线速度
 7     //var num_tempx= 0,num_tempz= 0,num_tempy=0;//认为这个是各个方向的分量
 8     if((arr_state[68]-arr_state[65])==0)//同时按下了左右键，或者什么也没按
 9     &#123;
10 
11     &#125;
12     else if(arr_state[65]==1)//向左
13     &#123;
14         v_obj.x=-obj.vd.left;//采用obj的在这个方向上设定的速度，obj.vd.left是一个标量
15     &#125;
16     else if(arr_state[68]==1)
17     &#123;
18         v_obj.x=obj.vd.right;
19     &#125;
20     if((arr_state[87]-arr_state[83])==0)//同时按下了前后键，或者什么也没按
21     &#123;
22 
23     &#125;
24     else if(arr_state[87]==1)//向前
25     &#123;
26         v_obj.z=obj.vd.forward;
27     &#125;
28     else if(arr_state[83]==1)
29     &#123;
30         v_obj.z=-obj.vd.backwards;
31     &#125;
32     if((arr_state[32]-arr_state[16])==0)//同时按下了上下键，或者什么也没按
33     &#123;
34 
35     &#125;
36     else if(arr_state[32]==1)//空格
37     &#123;
38         v_obj.y=obj.vd.up;
39     &#125;
40     else if(arr_state[16]==1)//shift
41     &#123;
42         v_obj.y=-obj.vd.down;
43     &#125;
44     //var v_obj0=v_obj.clone();
45     var v_x=Math.sin(rad_y)*v_obj.z+Math.cos(rad_y)*v_obj.x;//使用高中数学知识进行计算
46     var v_z=Math.cos(rad_y)*v_obj.z-Math.sin(rad_y)*v_obj.x;
47     var num_temp=MyGame.DeltaTime*obj.flag_objfast;//两帧之间的时间量乘以速度系数
48     var v_add=new BABYLON.Vector3(v_x*num_temp,v_obj.y*num_temp,v_z*num_temp);//这一帧内的位移
49     //console.log(v_add);
50     obj.mesh.position.addInPlace(v_add);//修改对象位置
51 
52 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这里是一个简单的按住方向键则不断向某一方向匀速运动的算法，相机的俯仰姿态并不影响运动效果，相机左右旋转对运动效果的影响使用三角函数计算，具体计算过程不再赘述。在以前的文章里还有一些其他的运动计算方法，比如带有加速度的计算、寻路计算、带有物理引擎效果的计算，如果感兴趣可以自己查看。</p>
<p>　　B、统一CameraMesh相关的对象的姿态：</p>
<pre><code class="copyable"> 1 function CamerasFollowActor(object)
 2 &#123;
 3     if(object.prototype=CameraMesh)
 4     &#123;
 5         var camera0=MyGame.Cameras.camera0;
 6         if(MyGame.flag_view=="first_lock"||MyGame.flag_view=="first_ani")//动画时相机也要跟随
 7         &#123;
 8             object.mesh.rotation.y = 0+camera0.rotation.y;//CameraMesh的姿态由相机的姿态决定，因为视角调整方法不好编，所以借用Babylon.js的相机控制方法
 9             object.mesh.rotation.x=0+camera0.rotation.x;//而相机的位置则由CameraMesh的位置决定
10             camera0.position=object.mesh.position.clone()//这里的player没有父元素所以_absolutePosition和position相等
11             object.mesh.ballman.head.position=object.mesh.position.clone();//我没有设置head是ballman的子元素，所以位置和姿态要手动修改
12             object.mesh.ballman.head.rotation=object.mesh.rotation.clone();//因为要保留添加物理外壳的可能性
13             
14             if(MyGame.init_state==2&&MyGame.flag_view=="first_lock")
15             &#123;//在鼠标不动时实现MouseMove的功能
16                 var width = engine.getRenderWidth();
17                 var height = engine.getRenderHeight();
18                 var pickInfo = scene.pick(width/2, height/2, null, false, MyGame.Cameras.camera0);
19                 
20             &#125;
21         &#125;
22         else if(MyGame.flag_view=="third")
23         &#123;
24 
25         &#125;
26         else if(MyGame.flag_view=="free")
27         &#123;
28 
29         &#125;
30     &#125;
31 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　为了保留对BallMan使用物理引擎的可能，object.mesh.ballman.head并不是object.mesh的子元素，所以还要手动设置object.mesh.ballman.head的位置和姿态。</p>
<p>　　在十四行进行了一次鼠标拾取计算，这在鼠标不动但场景内物体移动，导致准心所指对象发生变化时起到作用。</p>
<p>三、卡牌设计</p>
<p>1、卡牌类CardMesh</p>
<p>　　CardMesh类是object类的子类，代码位于Character.js文件中。</p>
<p>　　A、卡牌对象的实例化，以下的代码实例化了75个卡牌对象</p>
<pre><code class="copyable"> 1 function DrawCard4()
 2 &#123;
 3     for(var i=0;i<75;i++)
 4     &#123;
 5         var card_test=new CardMesh();
 6         var obj_p=&#123;name:"cardname"+count_cardname,point_x:point_x,point_y:point_y
 7             ,card:arr_carddata["test"]//从卡牌数据列表里提取名为“test”的卡牌信息
 8             ,linecolor:new BABYLON.Color3(0, 1, 0) //边线颜色
 9             ,scene:scene
10             ,position:new BABYLON.Vector3(0,0,0)
11             ,rotation:new BABYLON.Vector3(0,0,0)
12             ,scaling:new BABYLON.Vector3(0.1,0.1,0.1)
13             ,belongto:MyGame.WhoAmI//属于哪个玩家
14         &#125;;
15         card_test.init(obj_p,scene);
16         card_test.mesh.parent=mesh_arr_cards;
17         count_cardname++;//命名计数器自增
18     &#125;
19 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　其中arr_carddata是一个存储卡牌种类的数组，位于tab_carddata.js文件中，其格式如下：</p>
<pre><code class="copyable"> 1 //卡牌数据
 2 arr_carddata=&#123;
 3     test:&#123;
 4         imageb:"flower"//卡背种类
 5         ,imagemain:"../ASSETS/IMAGE/play.png"//正面的主要图片
 6         ,background:"Cu"//卡片正面的背景边框种类
 7         ,attack:3,hp:4,cost:2,range:3,speed:5
　　　　　　　　//下面是卡片的主要文字
 8         ,str_comment:"通过canvas排布生成动态纹理，（或者加入html2canvas，将dom排版转为dataurl？）"
 9         ,str_title:"测试卡片"//卡片上显示的卡片名称
10     &#125;
11 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　其中卡背种类和卡片边框种类的信息保存在tab_somedata.js文件中：</p>
<pre><code class="copyable"> 1 //存放一些通用的数据
 2 var arr_icontypes=&#123;test1:"../ASSETS/IMAGE/CURSOR/cursor1.png"//显示在卡片上的一些小图标，表示特殊的状态
 3     ,test2:"../ASSETS/IMAGE/CURSOR/cursor2.png"
 4     ,test3:"../ASSETS/IMAGE/CURSOR/cursor3.png"&#125;
 5 
 6 var arr_fronttypes=&#123;Cu:"../ASSETS/IMAGE/FRONTTYPE/cu.png"//要把这里的图片纹理设计成只实例化一次
 7     ,Ag:"../ASSETS/IMAGE/FRONTTYPE/ag.png"//正面边框种类，分别是铜、银、金
 8     ,Au:"../ASSETS/IMAGE/FRONTTYPE/au.png"
 9     ,pt:""
10 &#125;
11 var arr_backtypes=&#123;flower:"../ASSETS/IMAGE/flower.png"//卡背图片
12 
13 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　初始化时设置的属性的部分代码如下：</p>
<pre><code class="copyable"> 1 CardMesh=function()
 2 &#123;
 3     newland.object.call(this);
 4 &#125;
 5 CardMesh.prototype=new newland.object();
 6 CardMesh.prototype.init=function(param,scene)
 7 &#123;
 8     //param = param || &#123;&#125;;
 9     if(!param||!param.card)//如果输入的卡牌参数有误
10     &#123;
11         alert("卡牌初始化失败");
12         return;
13     &#125;
14     this.name = param.name;//名称
15     this.point_x = param.point_x;//x方向有几个点
16     this.point_y = param.point_y;//y方向有几个点
17     this.imagemain=param.card.imagemain;
18     this.background=param.card.background;
19     this.attack=param.card.attack;
20     this.hp=param.card.hp;
21     this.cost=param.card.cost;
22     this.str_comment=param.card.str_comment;
23     this.str_title=param.card.str_title;
24     this.range=param.card.range;
25     this.speed=param.card.speed;
26     //this.imagef = this.make_imagef();//正面纹理图片使用canvas生成——》还是用多层图片吧
27     this.imageb = param.card.imageb;//背面纹理图片
28     this.linecolor = param.linecolor;//未选中时显示边线，选中时用发光边线
29     this.scene = param.scene;
30     this.belongto=param.belongto;//表明该卡牌现在由哪个玩家掌控
31     this.isPicked=false;//这个卡片是否被选中
32     this.num_group=999;//这个卡片的编队数字，编队越靠前显示越靠前，999表示最大，意为没有编队，显示在列表的最后面
33     this.pickindex=0;//在被选中卡片数组中的索引，需要不断刷新？
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　B、卡牌的网格</p>
<p>　　为了赋予卡牌扭曲形变的可能性，我使用了更多的顶点来构成卡牌网格，而不是使用最简单的四个顶点组成矩形面。生成卡牌顶点数据的方法如下：</p>
<pre><code class="copyable">1 //正反表面顶点
2     this.vertexData = new BABYLON.VertexData();//每一张卡片都要有自己的顶点数组对象，正反两面复用。这个对象要一直保持不变！！
3     this.make_vertex(this.point_x, this.point_y);//参数是xy方向各有几个顶点，顶点越多可能的变形越细致，但性能消耗也越大
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"> 1 //生成通用的顶点数组和纹理映射数组
 2 CardMesh.prototype.make_vertex=function(x,y)
 3 &#123;
 4     var positions=[];//顶点位置数组
 5     var uvs=[];//纹理坐标数组
 6     var normals=[];//法线数组
 7     var indices=[];//索引数组
 8     for(var i=0;i<y;i++)//对于每一行顶点
 9     &#123;
10         for(var j=0;j<x;j++)//对于这一行里的每一个顶点
11         &#123;
12             positions.push(j);
13             positions.push(i);
14             positions.push(0);//顶点位置
15 
16             uvs.push((j/(x-1)));
17             uvs.push((i/(y-1)));//纹理映射位置
18 
19         &#125;
20     &#125;
21     for(var i=0;i<y-1;i++)
22     &#123;
23         for(var j=0;j<x-1;j++)
24         &#123;
25             var int_point=j+x*i;//第一个点的数字索引
26             indices.push(int_point);
27             indices.push(int_point+1);
28             indices.push(int_point+x);
29             indices.push(int_point+1);
30             indices.push(int_point+x+1);
31             indices.push(int_point+x);//画出两个三角形组成一个矩形
32         &#125;
33     &#125;
34     BABYLON.VertexData.ComputeNormals(positions, indices, normals);//计算法线
35     BABYLON.VertexData._ComputeSides(0, positions, indices, normals, uvs);
36     this.vertexData.indices = indices.concat();//索引
37     this.vertexData.positions = positions.concat();
38     this.vertexData.normals = normals.concat();//position改变法线也要改变！！！！
39     this.vertexData.uvs = uvs.concat();
40 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　上面遍历了卡片的每一个区域，并生成了对应的三角形，关于顶点位置、纹理坐标、法线、索引的关系，可以查看我的3D编程入门视频教程，或者其他的WebGL资料。</p>
<p>　　为了方便的将卡背和卡面设为不同的纹理，我使用这里生成的顶点数据创建了两个相同的网格，一个作为卡背，一个作为卡面，具体设置方法在接下来的材质部分讨论。</p>
<p>　　C、卡面材质构成方法</p>
<p>　　为了让卡牌的层次感更强，卡面需要由多种不同的材质构成，比如边框（将卡牌的外边缘定义为“边线”，将图片和边线之间的区域定义为“边框”）可能需要金属闪光，图片中要有火焰燃烧或者水波荡漾之类的特效，我找到了两种设计思路：</p>
<p>　　方案A是使用自定义着色器对卡牌网格进行渲染，在自定义着色器中用条件判断语句产生多个分支，每个分支使用一种颜色算法，然后将判断条件放在卡面图片一般用不到的透明度通道里，图片不同像素的透明度值不同，则在着色器中导向不同的算法，这种算法应该是当前卡牌材质构成的主流算法。</p>
<p>　　其优点在于只需要对一张图片进行操作（这在专业图片处理工具中并不难做），并且自定义着色器的功能精确可控，可以实现非常复杂的特殊效果，同时在卡牌发生弯曲时特效能够伴随卡牌一同弯曲。但这种算法也存在缺陷，比如卡牌中的内容无法灵活的动态变化，每次变化都要重新生成整个图片；同时因为卡面是一个整体，如果操作者想要和卡面上的不同区域做不同互动，则需要设计一套计算光标在卡牌上精确位置的算法；第三则是Babylon.js内置的光照、阴影等功能不支持自定义着色器。</p>
<p>　　方案B则是在卡面的不同部分放置多个网格，每个网格使用不同的材质，这样能够提供更高的灵活度和更好的Babylon.js引擎兼容性，但图片与网格一同变形的操作将很难做到。</p>
<p>　　两种方案的示意图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc2908330afa4378b3bad30ab661634e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　　考虑到B方案更容易实现，决定使用采用B方案生成卡面，以后有机会再向A方案方向迭代。</p>
<p>　　D、卡牌网格、纹理的组合：</p>
<pre><code class="copyable">  1 //正面纹理
  2     var materialf = new BABYLON.StandardMaterial(this.name+"cardf", this.scene);//测试用卡片纹理
  3     if(MyGame.textures[param.card.background])//如果已经初始化过这种纹理，则使用已经初始化完毕的
  4     &#123;
  5         materialf.diffuseTexture=MyGame.textures[param.card.background];
  6     &#125;
  7     else
  8     &#123;
  9         materialf.diffuseTexture = new BABYLON.Texture(arr_fronttypes[param.card.background], this.scene);
 10         materialf.diffuseTexture.hasAlpha = false;
 11         MyGame.textures[param.card.background]=materialf.diffuseTexture;
 12     &#125;
 13     materialf.backFaceCulling = true;
 14     materialf.bumpTexture = new BABYLON.Texture("../ASSETS/IMAGE/grained_uv.png", scene);//磨砂表面
 15     materialf.useLogarithmicDepth=true;
 16     //背面纹理
 17     var materialb = new BABYLON.StandardMaterial(this.name+"cardb", this.scene);//测试用卡片纹理
 18     if(MyGame.textures[param.card.imageb])//如果已经初始化过这种纹理，则使用已经初始化完毕的
 19     &#123;
 20         materialb.diffuseTexture=MyGame.textures[param.card.imageb];
 21     &#125;
 22     else
 23     &#123;
 24         materialb.diffuseTexture = new BABYLON.Texture(arr_backtypes[param.card.imageb], this.scene);
 25         materialb.diffuseTexture.hasAlpha = false;
 26         MyGame.textures[param.card.imageb]=materialb.diffuseTexture;
 27     &#125;
 28     materialb.backFaceCulling = false;
 29     //materialb.sideOrientation=BABYLON.Mesh.BACKSIDE;
 30 
 31 
 32     var x=this.point_x;
 33     var y=this.point_y;
 34 
 35     //还是将正反两面作为不同的mesh更直观？
 36     //背面网格
 37     var cardb = new BABYLON.Mesh(this.name + "b", this.scene);
 38     this.vertexData.applyToMesh(cardb, true);//通过顶点数据生成网格
 39     cardb.material = materialb;
 40     cardb.renderingGroupId = 2;
 41     //cardb.position.x+=(x-1);
 42     //cardb.rotation.y=Math.PI;
 43     cardb.sideOrientation = BABYLON.Mesh.BACKSIDE;
 44     cardb.position.y -= (y - 1) / 2;
 45     cardb.position.x -= (x - 1) / 2;
 46     cardb.isPickable=false;
 47     //正面网格
 48     var cardf = new BABYLON.Mesh(this.name + "f", this.scene);
 49     this.vertexData.applyToMesh(cardf, true);
 50     cardf.material = materialf;
 51     cardf.renderingGroupId = 2;
 52     cardf.sideOrientation = BABYLON.Mesh.FRONTSIDE;
 53     cardf.position.y -= (y - 1) / 2;//定义的顶点把左下角设为了零点，而默认的网格则是把中心点设为零点
 54     cardf.position.x -= (x - 1) / 2;
 55     cardf.isPickable=false;
 56     //边线
 57     var path_line = this.make_line(this.vertexData, x, y);//这里是四个顶点，能否自动封口？改用细线+高亮辉光？？!!用可见性控制
 58     this.path_line=path_line;
 59     //Mesh的Create方法事实上在调用MeshBuilder的对应Create方法，MeshBuilder的Create方法也可以实现对现有Mesh的变形功能
 60     //var line = new BABYLON.Mesh.CreateLines("line", path_line, this.scene, true);
 61     //Babylon.js不支持调整3D线段的线宽，为了能够调整宽度，将线改为圆柱体
 62     var line =BABYLON.MeshBuilder.CreateTube("line_"+this.name, &#123;path: path_line, radius: 0.05,updatable:false&#125;, scene);
 63     //边线纹理
 64     var materialline = new BABYLON.StandardMaterial("mat_line", this.scene);
 65     materialline.diffuseColor = this.linecolor;
 66     line.material = materialline;
 67     //line.color = new BABYLON.Color3(1, 0, 0);//这个颜色表示方式各个分量在0到1之间
 68     line.renderingGroupId = 2;
 69     line.position.y -= (y - 1) / 2;
 70     line.position.x -= (x - 1) / 2;
 71     line.isVisible=false//非选中状态边线不可见
 72 
 73     this.mesh=new BABYLON.MeshBuilder.CreateBox(("card_" +this.name),&#123;width:x-1,height:y-1,depth:0.005&#125;,this.scene);
 74     this.mesh.renderingGroupId = 0;//建立一个隐形的盒子作为卡牌正反面网格的父网格
 75     this.mesh.position=param.position;//可以通过点击这个盒子来选择卡片，也可以为这个盒子绑定物理引擎
 76     this.mesh.rotation=param.rotation;
 77     this.mesh.scaling=param.scaling;
 78     this.cardf = cardf;
 79     this.cardb = cardb;
 80     this.line = line;
 81     this.path_line=path_line;
 82     this.arr_path_line=line.getVerticesData(BABYLON.VertexBuffer.PositionKind,false);
 83     cardf.parent = this.mesh;
 84     cardb.parent = this.mesh;
 85     line.parent = this.mesh;
 86     this.mesh.card = this;
 87     //this.mesh.parent=mesh_arr_cards;//按照高内聚低耦合的规则，这个设定不应该放在角色类内部
 88     //暂时使用16:9的高宽设计
 89     var mesh_mainpic=new BABYLON.MeshBuilder.CreateGround(this.name+"mesh_mainpic",&#123;width:8.4,height:9&#125;,scene);
 90     mesh_mainpic.parent=this.mesh;//承载正面图片的网格
 91     mesh_mainpic.position=new BABYLON.Vector3(0,2.8,-0.01);
 92     var mat_mainpic = new BABYLON.StandardMaterial(this.name+"mat_mainpic", this.scene);//测试用卡片纹理
 93     mat_mainpic.diffuseTexture = new BABYLON.Texture(this.imagemain, this.scene);//地面的纹理贴图
 94     mat_mainpic.diffuseTexture.hasAlpha = false;
 95     mat_mainpic.backFaceCulling = true;
 96     mat_mainpic.useLogarithmicDepth=true;//虽然还不完全理解为什么，但是这种深度测试方式能够避免“Z-fighting”
 97     mat_mainpic.freeze();
 98     mesh_mainpic.material=mat_mainpic;
 99     mesh_mainpic.renderingGroupId=2;
100     mesh_mainpic.rotation.x=-Math.PI/2;
101     mesh_mainpic.isPickable=false;
102 
103     var mesh_comment=new BABYLON.MeshBuilder.CreateGround(this.name+"mesh_comment",&#123;width:6,height:4.8&#125;,scene);
104     mesh_comment.parent=this.mesh;//承载正面文字的网格
105     mesh_comment.position=new BABYLON.Vector3(0,-4.6,-0.01);
106     mesh_comment.renderingGroupId=2;
107     var mat_comment = new BABYLON.StandardMaterial(this.name+"mat_comment", scene);
108     var texture_comment= new BABYLON.DynamicTexture(this.name+"texture_comment", &#123;width:300, height:240&#125;, scene);
109     mat_comment.diffuseTexture =texture_comment;//使用基于canvas的动态纹理显示文字
110     mat_comment.useLogarithmicDepth=true;
111     mesh_comment.material = mat_comment;
112     mesh_comment.rotation.x=-Math.PI/2;
113     mesh_comment.isPickable=false;
114     var context_comment = texture_comment.getContext();//获取canvas的上下文
115     context_comment.fillStyle="#0000ff";//使用html5canvas方法
116     context_comment.fillRect(1,1,150,120);
117     context_comment.fillStyle="#ffffff";
118     context_comment.font="bold 32px monospace";
119     newland.canvasTextAutoLine(this.str_comment,context_comment,1,30,35,34);
120     texture_comment.update();//修改canvas后更新动态纹理
121 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　在绘制卡面时遇到几个问题：</p>
<p>　　a、卡牌的边线与被选中效果设计</p>
<p>　　原计划使用Babylon.js内置的线段系统绘制卡牌边线，然后对卡牌的正面使用内置的“边缘高光”功能表示卡片被选中。但实际测试时发现内置的3D线段无法修改线宽（锁定为1像素），所以改用细长的圆柱体网格（管道网格）代表线段。（边缘高光和动态纹理的官方文档中英对照可以在http://down.51cto.com/data/2450646下载）</p>
<p>　　生成边线路径的代码如下：</p>
<pre><code class="copyable"> 1 //边线轨迹
 2 CardMesh.prototype.make_line=function(vertexData,x,y)
 3 &#123;
 4     var path_line=[];
 5     //找边线上的所有点
 6     for(var i=0;i<x-1;i++)
 7     &#123;
 8         path_line.push(new BABYLON.Vector3(vertexData.positions[i*3],vertexData.positions[i*3+1],vertexData.positions[i*3+2]));
 9     &#125;
10     for(var i=0;i<y-1;i++)
11     &#123;
12         path_line.push(new BABYLON.Vector3(vertexData.positions[3*(x-1)+i*x*3],vertexData.positions[3*(x-1)+i*x*3+1],vertexData.positions[3*(x-1)+i*x*3+2]));
13     &#125;
14     for(var i=x-1;i>0;i--)
15     &#123;
16         path_line.push(new BABYLON.Vector3(vertexData.positions[(y-1)*x*3+i*3],vertexData.positions[(y-1)*x*3+i*3+1],vertexData.positions[(y-1)*x*3+i*3+2]));
17     &#125;
18     for(var i=y-1;i>=0;i--)
19     &#123;
20         path_line.push(new BABYLON.Vector3(vertexData.positions[i*x*3],vertexData.positions[i*x*3+1],vertexData.positions[i*x*3+2]));
21     &#125;
22     return path_line;
23 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<p>　　Babylon.js内置的边缘高光功能也不尽如人意，一是内部图片网格和文字网格遮挡铜片（边框）的边缘也出现了高光，二是高光层与图片网格和文字网格发生类似深度缓存异常（z-fighting）（后面讨论）的现象。</p>
<p>　　内部网格的边缘也出现了高亮：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fb1698d75cc48659325da6319e26fd7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　z-fighting效果：</p>
<p> <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e54b034aa3b6455e9952edf4cf5bde76~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　所以改为对作为边框的管道网格设置边缘高亮，但是不太清楚如何控制高亮范围的大小。</p>
<p>　　b、深度缓存异常</p>
<p>　　OpenGL使用深度缓存保存屏幕上的每个像素距视点的距离，如果一个像素的位置有多个图元（三角形）存在，则会用三角形距视点的距离与深度缓存比较，如果图元的距离更近则使用这个图元的颜色，并修改深度缓存为这个图元的距离，通过这种方式OpenGL可以实现“前面的物体遮挡后面的物体”这种效果。</p>
<p>　　然而这种方法存在问题，一方面因为浮点数精度限制，距离过近的图元会被认为处于同一深度层次甚至相反，这时前后两个表面会交替闪烁显示，这种异常称为“z-fighting”，比如上面的正面网格和图片网格、文字网格之间就可能发生z-fighting；另一方面因为浮点数大小限制，过于遥远的图元所在的深度层次可能超过浮点数上限，产生“深度缓存溢出”，比如同时存在近景物体和宇宙星空的情况。</p>
<p>　　为了避免这两种深度缓存异常，对正面和图片网格、文字网格的材质设置了“materialf.useLogarithmicDepth=true;”，这种“对数深度缓存”，将原来图元距离和深度线性对应的计算方式，改为在对数计算方式，这样就在较近的地方建立了很多距离相差很小的深度分层，而在很远的地方则是数量较少的距离相差很大的深度分层。需要注意的是，并不是所有浏览器都支持对数深度缓存，设置了这个属性后Babylon.js会尝试使用对数深度缓存，如果失败则仍使用默认的线性深度缓存。</p>
<p>　　c、动态纹理</p>
<p>　　上述代码使用Babylon.js的动态纹理功能为文字网格设置了可以动态变化的纹理，这种动态纹理是基于canvas实现的，你可以获取这个canvas的上下文并使用各种html5 canvas方法生成图像。另外Babylon.js也提供了一些封装的操作动态纹理的方法，比如initArena中的数字标签，这种封装的方法不需要调用texture_comment.update()来更新动态纹理，但存在文字定位不准的问题，需要反复调试</p>
<p>　　newland.canvasTextAutoLine是根据网上的代码修改而成的，在canvas中自动换行书写文字的方法：　　</p>
<pre><code class="copyable"> 1 //向一个canvas上下文里自动换行的插入文字（来自网上）
 2 newland.canvasTextAutoLine=function(str,ctx,initX,initX2,initY,lineHeight)&#123;
 3     //var ctx = canvas.getContext("2d");
 4     var lineWidth = 0;
 5     var canvasWidth = ctx.canvas.width;
 6     var lastSubStrIndex= 0;
 7     for(let i=0;i<str.length;i++)&#123;
 8         lineWidth+=ctx.measureText(str[i]).width;
 9         if(lineWidth>canvasWidth-initX2)&#123;//减去initX,防止边界出现的问题
10             ctx.fillText(str.substring(lastSubStrIndex,i),initX,initY);
11             initY+=lineHeight;
12             lineWidth=0;
13             lastSubStrIndex=i;
14         &#125;
15         if(i==str.length-1)&#123;
16             ctx.fillText(str.substring(lastSubStrIndex,i+1),initX,initY);
17         &#125;
18     &#125;
19 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　不知道是什么原因，这个方法运行的效果和网上的例子存在偏差，只好加一些偏移量手动微调。</p>
<p>2、卡牌的处理</p>
<p>　　A、按下Alt键时卡牌的移入和移除动画（代码位于HandleCard2.js文件中）</p>
<p>　　这里的设计是以mesh_arr_cards作为所有CardMesh对象的父网格，在first_lock状态下mesh_arr_cards的父网格为BallMan的backview且position为0，这意味着卡牌将一直在操作者背后跟随操作者移动，所以操作者看不到卡牌。</p>
<p>　　在按下Alt键时，浏览模式变为first_ani，卡牌的位置跟随动画从后向前移动，移动到BallMan的handpoint位置时卡牌的position置为0，父元素改为handpoint，同时浏览模式变为first_pick。</p>
<p>　　从first_pick变为first_lock的过程与此相反。</p>
<pre><code class="copyable"> 1 function HandCard(flag)//用动画方式表现手牌的“展开和收拢”
 2 &#123;
 3     var pos1,pos2;
 4     MyGame.flag_view="first_pick";
 5     if(flag==0)//将手牌从后面推到前面
 6     &#123;
 7         pos1=new BABYLON.Vector3(0,0,0);
 8         pos2=new BABYLON.Vector3(0,-2,16);
 9         var animation3=new BABYLON.Animation("ani_HandCard0","position",30,BABYLON.Animation.ANIMATIONTYPE_VECTOR3,BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT);
10         var keys1=[&#123;frame:0,value:pos1&#125;,&#123;frame:15,value:pos2&#125;];
11         animation3.setKeys(keys1);
12         mesh_arr_cards.animations.push(animation3);
13         scene.beginAnimation(mesh_arr_cards, 0, 15, false,1,function()&#123;
14             mesh_arr_cards.position=new BABYLON.Vector3(0,0,0);//动画执行结束时执行的函数
15             mesh_arr_cards.parent=MyGame.player.mesh.ballman.handpoint;
16             MyGame.flag_view="first_pick";
17             MyGame.UiPanelr.button1.isVisible=true;
18             MyGame.UiPanelr.button2.isVisible=true;
19         &#125;);
20     &#125;
21     else if(flag==1)//将手牌从前面拉到后面
22     &#123;
23         pos1=new BABYLON.Vector3(0,0,0);
24         pos2=new BABYLON.Vector3(0,2,-16);
25         var animation3=new BABYLON.Animation("ani_HandCard1","position",30,BABYLON.Animation.ANIMATIONTYPE_VECTOR3,BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT);
26         var keys1=[&#123;frame:0,value:pos1&#125;,&#123;frame:15,value:pos2&#125;];
27         animation3.setKeys(keys1);
28         mesh_arr_cards.animations.push(animation3);
29         scene.beginAnimation(mesh_arr_cards, 0, 15, false,1,function()&#123;
30             mesh_arr_cards.position=new BABYLON.Vector3(0,0,0);
31             mesh_arr_cards.parent=MyGame.player.mesh.ballman.backview;
32             MyGame.flag_view="first_lock";
33         &#125;);
34     &#125;
35 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　B、卡牌的分组和排序</p>
<p>　　可以将选取的一些卡牌编成一队，被编队的卡牌将显示在所有卡牌之前。</p>
<p>　　编队：</p>
<pre><code class="copyable">function HandleGroup(keyCode)//按1到5时处理手牌分组
&#123;
    var len =arr_pickedCards.length;//所有选中的卡片
    var group=arr_cardgroup[keyCode-49];//取按下的按键对应的这一组
    for(var key in group)
    &#123;//如果这一组里已经有成员
        group[key].num_group=999;//将这些成员设为未分组状态
    &#125;
    arr_cardgroup[keyCode-49]=&#123;&#125;;//清空原来的分组
    for(var i=0;i<len;i++)//对于每一张选中的卡片
    &#123;
        var card=arr_pickedCards[i];
        if(card.num_group!=999)//解除原来的绑定
        &#123;
            delete arr_cardgroup[card.num_group][card.mesh.name];//将卡牌移出原来的分组
        &#125;
            //arr_cardgroup[card.num_group].delete(card.mesh.name);
        card.num_group=keyCode-49;//双向绑定，第一队要对应索引0！！
        arr_cardgroup[keyCode-49][card.mesh.name]=card;
        noPicked(card);//分入小队后，取消这张卡牌的选中效果
    &#125;
    //重绘前要清空已选中手牌
    arr_pickedCards=[];
    SortCard()//根据分组情况将手牌重新排序
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　在初始化卡牌（DrawCard4()）和卡牌分组之后执行SortCard()为每张卡牌安排新的位置：</p>
<pre><code class="copyable"> 1 var arr_cardgroup=[&#123;&#125;,&#123;&#125;,&#123;&#125;,&#123;&#125;,&#123;&#125;];//五个分组的成员情况
 2 var arr_mesh_groupicon=[];//在每一组分组元素前显示组号
 3 //根据mesh_arr_cards._children和arr_cardgroup进行排序
 4 function SortCard()
 5 &#123;
 6     var arr_mycards=mesh_arr_cards._children;
 7     var len=arr_mycards.length;
 8     var lenx = 10;//每一行的元素个数
 9     var leny = 4;//一页显示的最多有2行
10     var count=0;//记录元素位置占用了多少个
11     var widthp = 0.9;//每个卡片经过缩放后的实际宽度
12     var heightp = 1.6;//每一张卡牌的实际高度
13     var marginx = 0.2;//x方向间隙大小
14     var marginy = 0.2;//y方向间隙大小
15     var len2=arr_cardgroup.length;
16     for(var i=0;i<len2;i++)//先绘制分组的元素
17     &#123;
18         var obj=arr_cardgroup[i];
19         var flag_icon=0;//是否已经放置了标记
20         var x=0,y=0;
21         for(key in obj)
22         &#123;
23             x = count % lenx;//从左往右数的索引
24             y = Math.floor(count / lenx);//从上往下数的索引
25             var posx = (x - lenx / 2) * (widthp + marginx);//根据索引算出位置
26             var posy = -(y - leny / 2) * (heightp + marginy) - 0.2;
27             if(flag_icon==0)//还未放置标记
28             &#123;//则将这个小组的标记设为这个小组的第一张卡牌的子元素
29                 //arr_mesh_groupicon[i].position=new BABYLON.Vector3(posx-1.5,posy,0);
30                 arr_mesh_groupicon[i].parent=obj[key].mesh;
31                 arr_mesh_groupicon[i].isVisible=true;
32                 flag_icon=1;
33             &#125;
34             obj[key].mesh.position=new BABYLON.Vector3(posx,posy,0);
35             count++;//表示又占用了一个空位
36         &#125;
37         if(flag_icon==0)//如果最后也每放置标记，说明这个分组没有元素，将分组标记撤除
38         &#123;
39             arr_mesh_groupicon[i].isVisible=false;
40         &#125;
41         else
42         &#123;//如果用到了这个分组
43             count=(y+1)* lenx;//空位补齐，每个分组都另起一行
44         &#125;
45     &#125;
46     for(var i=0;i<len;i++)//处理小队以外的其他卡牌
47     &#123;
48         var mesh=arr_mycards[i];
49         if(mesh.card.num_group==999)//处理没有分组的元素
50         &#123;
51             var x = count % lenx;//从左往右数的索引
52             var y = Math.floor(count / lenx);//从上往下数的索引
53             var posx = (x - lenx / 2) * (widthp + marginx);
54             var posy = -(y - leny / 2) * (heightp + marginy) - 0.2;
55             mesh.position=new BABYLON.Vector3(posx,posy,0);
56             count++;
57         &#125;
58 
59     &#125;
60 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　C、卡牌的选取效果</p>
<p>　　卡牌被选中时需要高亮边缘，取消选中时解除高亮：</p>
<pre><code class="copyable"> 1 function getPicked(card)
 2 &#123;//将卡片标识为选中状态，设置高亮边框，并且将它作为第一个选中点
 3     card.line.isVisible=true;
 4     MyGame.hl.addMesh(card.line,card.linecolor);
 5     MyGame.hl.addMesh(card.mesh,card.linecolor);//mesh不可见则不会生成对应高光层
 6     //card.line.width=1000;
 7     //card.line=BABYLON.MeshBuilder.CreateTube(card.line.name, &#123;path: card.path_line, radius:0.2,updatable:true,instance:card.line&#125;, scene);
 8     card.isPicked=true;
 9     //card.pickindex=arr_pickedCards.length;//
10 &#125;
11 function noPicked(card)
12 &#123;
13     card.line.isVisible=false;
14     MyGame.hl.removeMesh(card.line);
15     MyGame.hl.removeMesh(card.mesh);
16     //card.line.width=100;
17     //card.line=BABYLON.MeshBuilder.CreateTube(card.line.name, &#123;path: card.path_line, radius:0.05,updatable:true,instance:card.line&#125;, scene);
18     card.isPicked=false;
19 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　点击被选中的卡牌则把卡牌放大，其原理与前面的移入移出手牌相同：</p>
<pre><code class="copyable"> 1 var card_Closed=null;
 2 function GetCardClose(card)//将卡牌拉近
 3 &#123;
 4     MyGame.flag_view="first_ani";
 5     if(card_Closed)//如果已经有一个拉近的卡片
 6     &#123;
 7         var animation1=new BABYLON.Animation("animation1","position",30,BABYLON.Animation.ANIMATIONTYPE_VECTOR3,BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT);
 8         var keys1=[&#123;frame:0,value:card_Closed.mesh.position.clone()&#125;,&#123;frame:15,value:card_Closed.oldpositon&#125;];
 9         animation1.setKeys(keys1);
10         card_Closed.mesh.animations.push(animation1);
11         var animation2=new BABYLON.Animation("animation2","scaling",30,BABYLON.Animation.ANIMATIONTYPE_VECTOR3,BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT);
12         var keys2=[&#123;frame:0,value:new BABYLON.Vector3(0.5,0.5,0.5)&#125;,&#123;frame:15,value:new BABYLON.Vector3(0.1,0.1,0.1)&#125;];
13         animation2.setKeys(keys2);
14         card_Closed.mesh.animations.push(animation2);
15         scene.beginAnimation(card_Closed.mesh, 0, 15, false,1,function()&#123;//可以在一个动画结束时再启动另一个动画
16             card_Closed=card;
17             card.oldpositon=card.mesh.position.clone();
18             var animation3=new BABYLON.Animation("animation3","position",30,BABYLON.Animation.ANIMATIONTYPE_VECTOR3,BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT);
19             var keys1=[&#123;frame:0,value:card_Closed.mesh.position.clone()&#125;,&#123;frame:15,value:new BABYLON.Vector3(0,0,-0.5)&#125;];
20             animation3.setKeys(keys1);
21             card_Closed.mesh.animations.push(animation3);
22             var animation4=new BABYLON.Animation("animation4","scaling",30,BABYLON.Animation.ANIMATIONTYPE_VECTOR3,BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT);
23             var keys2=[&#123;frame:0,value:new BABYLON.Vector3(0.1,0.1,0.1)&#125;,&#123;frame:15,value:new BABYLON.Vector3(0.5,0.5,0.5)&#125;];
24             animation4.setKeys(keys2);
25             card_Closed.mesh.animations.push(animation4);
26             scene.beginAnimation(card_Closed.mesh, 0, 15, false,1,function()&#123;
27 
28                 MyGame.flag_view="first_pick";
29             &#125;);
30         &#125;);
31 
32     &#125;
33     else
34     &#123;
35         card_Closed=card;
36         card.oldpositon=card.mesh.position.clone();
37         var animation3=new BABYLON.Animation("animation3","position",30,BABYLON.Animation.ANIMATIONTYPE_VECTOR3,BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT);
38         var keys1=[&#123;frame:0,value:card_Closed.mesh.position.clone()&#125;,&#123;frame:15,value:new BABYLON.Vector3(0,0,-0.5)&#125;];
39         animation3.setKeys(keys1);
40         card_Closed.mesh.animations.push(animation3);
41         var animation4=new BABYLON.Animation("animation4","scaling",30,BABYLON.Animation.ANIMATIONTYPE_VECTOR3,BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT);
42         var keys2=[&#123;frame:0,value:new BABYLON.Vector3(0.1,0.1,0.1)&#125;,&#123;frame:15,value:new BABYLON.Vector3(0.5,0.5,0.5)&#125;];
43         animation4.setKeys(keys2);
44         card_Closed.mesh.animations.push(animation4);
45         scene.beginAnimation(card_Closed.mesh, 0, 15, false,1,function()&#123;
46             MyGame.flag_view="first_pick";
47         &#125;);
48     &#125;
49 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　D、卡牌的多选</p>
<p>　　参考Windows系统的文件多选编写了卡牌多选功能：</p>
<pre><code class="copyable">  1 //对已经建立的卡片的各种处理方法放在这里
  2 var arr_pickedCards=[];
  3 function PickCard(card)
  4 &#123;
  5     if(card_Closed)//如果有拉近显示的卡片，则先把他恢复原样
  6     &#123;
  7         MyGame.flag_view="first_ani";
  8         var animation1=new BABYLON.Animation("animation1","position",30,BABYLON.Animation.ANIMATIONTYPE_VECTOR3,BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT);
  9         var keys1=[&#123;frame:0,value:card_Closed.mesh.position.clone()&#125;,&#123;frame:15,value:card_Closed.oldpositon&#125;];
 10         animation1.setKeys(keys1);
 11         card_Closed.mesh.animations.push(animation1);
 12         var animation2=new BABYLON.Animation("animation2","scaling",30,BABYLON.Animation.ANIMATIONTYPE_VECTOR3,BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT);
 13         var keys2=[&#123;frame:0,value:new BABYLON.Vector3(0.5,0.5,0.5)&#125;,&#123;frame:15,value:new BABYLON.Vector3(0.1,0.1,0.1)&#125;];
 14         animation2.setKeys(keys2);
 15         card_Closed.mesh.animations.push(animation2);
 16         scene.beginAnimation(card_Closed.mesh, 0, 15, false,1,function()&#123;
 17             card_Closed=null;
 18             MyGame.flag_view="first_pick";
 19         &#125;);
 20         return;
 21     &#125;
 22 
 23     var len=arr_pickedCards.length;
 24     var arr_state=MyGame.arr_keystate;
 25     var arr_mycards=mesh_arr_cards._children;//这个数组里的元素都是网格
 26     var len2=arr_mycards.length;
 27     var count=0;//加入分组特性后排序也要修改一下
 28     var len3=arr_cardgroup;
 29     for(var i=0;i<len3;i++)//在开始选择之前根据排序结果，为每张卡牌分配一个索引
 30     &#123;
 31         for(key in arr_cardgroup[i])
 32         &#123;
 33             arr_cardgroup[i][key].index=count;
 34             count++;
 35         &#125;
 36     &#125;
 37     for(var i=0;i<len2;i++)
 38     &#123;
 39         arr_mycards[i].card.index=count;
 40         count++;
 41     &#125;
 42 
 43     if(card.isPicked)
 44     //如果目前已经选中这个卡片，
 45         // 如果有多个选中卡片，如果当前按住了Ctrl，则取消它的选中（alt留着用来切换视角）
 46             //如果按住了shift，则将shift选择的区域截断到这里（允许同时按下？）
 47             // ，如果没有按住space或shift，则取消除它以外的所有选中并拉近
 48     // 如果只有这一个选中卡片，则放大它
 49     &#123;
 50         if(len>1)
 51         &#123;
 52             if(arr_state[16]==1)//按着shift
 53             &#123;
 54                 if(card_firstpick)//如果已经选定过一个卡片，将首选卡片和这个卡片之间的所有卡片选定
 55                 &#123;//card_firstpick是“第一个被选中的卡片”也称为“首选卡片”
 56                     if(card_firstpick.index>card.index)
 57                     &#123;
 58                         for(var i=0;i<len2;i++)
 59                         &#123;
 60                             var card0=arr_mycards[i].card;
 61                             if(i<=card_firstpick.index&&i>=card.index)
 62                             &#123;
 63                                 if(i!=card_firstpick.index)//首选元素就不向选取数组里放了
 64                                 &#123;
 65                                     //选中选取范围内的所有元素
 66                                     getPicked(card0);
 67                                     //card_firstpick=card;
 68                                     arr_pickedCards.push(card0);
 69                                 &#125;
 70                             &#125;
 71                             else
 72                             &#123;//删除选取范围外的所有已选中元素
 73                                 if(card0.isPicked)
 74                                 &#123;
 75                                     noPicked(card0);//
 76                                     var len3=arr_pickedCards.length;
 77                                     for(var j=0;j<len3;j++)&#123;//从选取数组中找到这个元素，并删除它
 78                                         if(arr_pickedCards[j].mesh.name==card0.mesh.name)
 79                                         &#123;
 80                                             arr_pickedCards.splice(j,1);
 81                                             break;
 82                                         &#125;
 83                                     &#125;
 84                                 &#125;
 85                             &#125;
 86                         &#125;
 87                     &#125;
 88                     else if(card_firstpick.index<card.index)//
 89                     &#123;
 90                         for(var i=0;i<len2;i++)
 91                         &#123;
 92                             var card0=arr_mycards[i].card;
 93                             if(i>=card_firstpick.index&&i<=card.index)
 94                             &#123;
 95                                 if(i!=card_firstpick.index)//首选元素就不向选取数组里放了
 96                                 &#123;
 97                                     //选中选取范围内的所有元素
 98                                     getPicked(card0);
 99                                     //card_firstpick=card;
100                                     arr_pickedCards.push(card0);
101                                 &#125;
102                             &#125;
103                             else
104                             &#123;//删除选取范围外的所有已选中元素
105                                 if(card0.isPicked)
106                                 &#123;
107                                     noPicked(card0);//
108                                     var len3=arr_pickedCards.length;
109                                     for(var j=0;j<len3;j++)&#123;//从选取数组中找到这个元素，并删除它
110                                         if(arr_pickedCards[j].mesh.name==card0.mesh.name)
111                                         &#123;
112                                             arr_pickedCards.splice(j,1);
113                                             break;
114                                         &#125;
115                                     &#125;
116                                 &#125;
117                             &#125;
118                         &#125;
119                     &#125;
120                     else if(card_firstpick.index==card.index)
121                     &#123;
122                         GetCardClose(card);//将这张卡片拿近
123                         //同时释放掉所有被选中的卡片
124                         for(var i=0;i<len;i++)
125                         &#123;
126                             var card0=arr_pickedCards[i];
127                             noPicked(card0);
128                         &#125;
129                         arr_pickedCards=[];
130                         card_firstpick=null;
131                     &#125;
132                 &#125;
133             &#125;
134             if(arr_state[17]==1)//ctrl
135             &#123;//取消这张卡片的选中
136                 noPicked(card);
137                 //var len3=arr_pickedCards.length;
138                 for(var j=0;j<len;j++)&#123;//从选取数组中找到这个元素，并删除它
139                     if(arr_pickedCards[j].mesh.name==card.mesh.name)
140                     &#123;
141                         arr_pickedCards.splice(j,1);
142                         break;
143                     &#125;
144                 &#125;
145                 card_firstpick=arr_pickedCards[arr_pickedCards.length-1];
146             &#125;
147             if(arr_state[17]!=1&&arr_state[16]!=1)
148             &#123;
149                 GetCardClose(card);//将这张卡片拿近
150                 //同时释放掉所有被选中的卡片
151                 for(var i=0;i<len;i++)
152                 &#123;
153                     var card0=arr_pickedCards[i];
154                     noPicked(card0);
155                 &#125;
156                 arr_pickedCards=[];
157                 card_firstpick=null;
158             &#125;
159         &#125;
160         else//目前只有这一张卡片被选中，然后点击了他
161         &#123;
162             GetCardClose(card);
163             noPicked(card);
164             arr_pickedCards=[];
165             card_firstpick=null;
166         &#125;
167     &#125;
168     else    //这张卡片还没有被选中
169     &#123;
170         if(len>0)//还有其他被选中的卡片
171         &#123;
172             if(arr_state[16]==1)//按着shift
173             &#123;
174                 if(card_firstpick)//如果已经选定过一个卡片，将首选卡片和这个卡片之间的所有卡片选定
175                 &#123;//如果选取数组不空则一定有首选元素？？
176 
177                     if(card_firstpick.index>card.index)
178                     &#123;
179                         for(var i=0;i<len2;i++)
180                         &#123;
181                             var card0=arr_mycards[i].card;
182                             if(i<=card_firstpick.index&&i>=card.index)
183                             &#123;
184                                 if(i!=card_firstpick.index)//首选元素就不向选取数组里放了
185                                 &#123;
186                                     //选中选取范围内的所有元素
187                                     getPicked(card0);
188                                     //card_firstpick=card;
189                                     arr_pickedCards.push(card0);
190                                 &#125;
191                             &#125;
192                             else
193                             &#123;//删除选取范围外的所有已选中元素
194                                 if(card0.isPicked)
195                                 &#123;
196                                     noPicked(card0);//
197                                     var len3=arr_pickedCards.length;
198                                     for(var j=0;j<len3;j++)&#123;//从选取数组中找到这个元素，并删除它
199                                         if(arr_pickedCards[j].mesh.name==card0.mesh.name)
200                                         &#123;
201                                             arr_pickedCards.splice(j,1);
202                                             break;
203                                         &#125;
204                                     &#125;
205                                 &#125;
206                             &#125;
207                         &#125;
208                     &#125;
209                     else if(card_firstpick.index<card.index)//因为card是未选中的所以card_firstpick.index与card.index不会相等
210                     &#123;
211                         for(var i=0;i<len2;i++)
212                         &#123;
213                             var card0=arr_mycards[i].card;
214                             if(i>=card_firstpick.index&&i<=card.index)
215                             &#123;
216                                 if(i!=card_firstpick.index)//首选元素就不向选取数组里放了
217                                 &#123;
218                                     //选中选取范围内的所有元素
219                                     getPicked(card0);
220                                     //card_firstpick=card;
221                                     arr_pickedCards.push(card0);
222                                 &#125;
223                             &#125;
224                             else
225                             &#123;//删除选取范围外的所有已选中元素
226                                 if(card0.isPicked)
227                                 &#123;
228                                     noPicked(card0);//
229                                     var len3=arr_pickedCards.length;
230                                     for(var j=0;j<len3;j++)&#123;//从选取数组中找到这个元素，并删除它
231                                         if(arr_pickedCards[j].mesh.name==card0.mesh.name)
232                                         &#123;
233                                             arr_pickedCards.splice(j,1);
234                                             break;
235                                         &#125;
236                                     &#125;
237                                 &#125;
238                             &#125;
239                         &#125;
240                     &#125;
241                 &#125;
242                 else
243                 &#123;//理论上讲，这里不会进入
244                     getPicked(card);
245                     card_firstpick=card;
246                     arr_pickedCards.push(card);
247                 &#125;
248             &#125;
249             if(arr_state[17]==1)//Ctrl
250             &#123;
251                 getPicked(card);
252                 card_firstpick=card;
253                 arr_pickedCards.push(card);
254             &#125;
255             if(arr_state[17]!=1&&arr_state[16]!=1)
256             &#123;//在没有按下shift或者Ctrl时，点击一个未选中的卡片，则释放以前选中的所有卡片，然后选中这个
257                 for(var i=0;i<len;i++)
258                 &#123;
259                     var card0=arr_pickedCards[i];
260                     noPicked(card0);
261                 &#125;
262                 arr_pickedCards=[];
263                 card_firstpick=null;
264                 getPicked(card);
265                 card_firstpick=card;
266                 arr_pickedCards.push(card);
267             &#125;
268         &#125;
269         else//没有其他被选中的卡片，这应该是最简单的情况？
270         &#123;
271             //card.getPicked();
272             getPicked(card);
273             card_firstpick=card;
274             arr_pickedCards.push(card);
275         &#125;
276     &#125;
277 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　E、卡牌的上下滚动</p>
<p>　　只是给FullUI.js中的两个按钮添加了响应方法：</p>
<pre><code class="copyable"> 1 function ScrollUporDown(flag,heightp,row)//flag0表示向上，1表示向下，heightp表示每行滚动距离，row表示滚动行数
 2 &#123;
 3     //var poshand=MyGame.player.mesh.ballman.handpoint._absolutePosition;//此时手的位置
 4     if(flag==0)
 5     &#123;
 6         var arr_mycards=mesh_arr_cards._children;
 7         var posy=arr_mycards[arr_mycards.length-1].position.y;//找到位置最低的卡牌
 8         if(mesh_arr_cards.position.y<(0-posy-row*heightp))//不能向上滚动太多，不完全精确的限定，但也够了
 9         &#123;
10             mesh_arr_cards.position.y+=row*heightp;
11         &#125;
12 
13     &#125;
14     else if(flag==1)
15     &#123;
16         if(mesh_arr_cards.position.y>=row*heightp)
17         &#123;
18             mesh_arr_cards.position.y-=row*heightp
19         &#125;
20 
21     &#125;
22 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 　　于是完成了最初演示的功能。</p>
<p>四、总结</p>
<p>　　文中的框架代码部分参考了Tony Parisi（Three.js入门书《WebGL入门指南》的作者）的sim.js库（<a href="https://github.com/tparisi/WebGLBook/tree/master/sim%EF%BC%89%E5%92%8C%C2%A0Julian" target="_blank" rel="nofollow noopener noreferrer">github.com/tparisi/Web…</a> Chenard（a French 30 years-old engineer currently working as WebGL developer in Rouen (not so far from Paris)）的FPS例程（http://www.pixelcodr.com/projects.html），再加上一些WebGL书籍和网络资料综合而来。整个框架命名为newland，意为探索新的领域，基于MIT协议发布。</p>
<p>　　卡牌设计部分因为作者美工才能有限而并不好看，但提供了一定的可扩展性，欢迎使用者自行扩展。接下来计划在场景中加入Babylon.js的瓷砖（棋盘）网格，并添加卡牌的移动和影响范围计算，以及技能效果计算。</p>
<p>　　因为精力有限，这篇文章没有经过充分的校对和修改，如果您发现有错误或者没说清楚的地方，请留言提醒，谢谢。</p>
<p> </p>
<p>附用谷歌浏览器将网页保存为mhtml格式的方法（修改自百度经验）：</p>
<p>　　1、打开chrome浏览器，地址栏输入：chrome://flags/ 后回车</p>
<p>　　2、Ctrl+F 搜索 MHTML,并找到 将网页另存为MHTML，点击 启动</p>
<p>　　3、启用后，重启chrome，Ctrl+S即可选择保存为mhtml格式</p>
<p>　　</p></div>  
</div>
            