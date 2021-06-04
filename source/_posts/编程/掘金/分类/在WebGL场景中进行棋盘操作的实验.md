
---
title: '在WebGL场景中进行棋盘操作的实验'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3ce16ce0643498b88d38f583b8b496c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 27 May 2021 22:20:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3ce16ce0643498b88d38f583b8b496c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>　　这篇文章讨论如何在基于Babylon.js的WebGL场景中，建立棋盘状的地块和多个可选择的棋子对象，在点选棋子时显示棋子的移动范围，并且在点击移动范围内的空白地块时向目标地块移动棋子。在这一过程中要考虑不同棋子的移动力和影响范围不同，以及不同地块的移动力消耗不同。</p>
<p>　　一、显示效果：</p>
<p>1、访问https://ljzc002.github.io/CardSimulate/HTML/TEST3tiled.html查看“棋盘测试页面”：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3ce16ce0643498b88d38f583b8b496c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　场景中是一个20*20的棋盘，地块随机为草地、土地、雪地，棋盘中央是四个“棋子”（用卡牌网格对象客串）。使用鼠标和wasd、Shift、空格键控制相机网格对象在场景中漫游，4个棋子会努力让自己面朝相机。</p>
<p>2、点击一个棋子或棋子所在的地块，棋子将被选中并显示棋子的可移动范围和影响范围：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b4f52d7a9064dcca9e5db250aa97c30~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> 　　棋子可以到达的地块覆盖蓝色半透明遮罩，棋子不能到达但可以影响的地块覆盖红色半透明遮罩。这里规定“铜卡”的移动力为10、影响范围为2，“银卡”的移动力为15、影响范围为3，草地、泥地、雪地对移动力的消耗分别为2、3、4.</p>
<p>3、点击蓝色地块，将用黄色半透明遮罩标出棋子到达目标地块的路径，点击红色地块，则标出到达距这个红色地块最近的蓝色地块的路径：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cee275e9122b41f3975467aba755c4ad~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> 4、点击黄色地块，则棋子缓缓移动到目标黄色地块，到达目标后，在棋子周围显示棋子的影响范围：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df94b91e960d48c2955be8c543faff55~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　在更新版的程序里，取消了棋子下面的红色遮罩</p>
<p>5、点击棋子可以将镜头拉近到棋子附近；点击影响范围外的地块，可以取消棋子的选定；点击其他的棋子或者含有其他棋子的地块，可以改变选定的棋子。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b19035963bd14ffcb4b39f21ef956a12~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>二、代码实现：</p>
<p>　　这个棋盘场景是在上一个卡牌场景（<a href="https://www.cnblogs.com/ljzc002/p/9660676.html%EF%BC%89%E7%9A%84%E5%9F%BA%E7%A1%80%E4%B8%8A%E6%94%B9%E8%BF%9B%E8%80%8C%E6%9D%A5%E7%9A%84%EF%BC%8C%E8%BF%99%E9%87%8C%E5%8F%AA%E8%AE%A8%E8%AE%BA%E6%94%B9%E5%8F%98%E5%92%8C%E6%96%B0%E5%A2%9E%E7%9A%84%E4%BB%A3%E7%A0%81%E4%B8%AD%E6%AF%94%E8%BE%83%E9%87%8D%E8%A6%81%E7%9A%84%E9%83%A8%E5%88%86%EF%BC%8C%E5%A4%A7%E9%83%A8%E5%88%86%E6%96%B0%E5%A2%9E%E6%96%B9%E6%B3%95%E5%9C%A8Tiled.js%E4%B8%AD%E3%80%82%C2%A0%C2%A0" target="_blank" rel="nofollow noopener noreferrer">www.cnblogs.com/ljzc002/p/9…</a></p>
<p>1、在initArena中建立棋盘：</p>
<pre><code class="copyable">1         mesh_tiledGround=new BABYLON.Mesh("mesh_tiledGround", scene);//这是所有地块的父网格也是所有棋盘上的棋子的爷爷网格
2         mesh_tiledGround.position.y=-7;//设定棋盘高度
3         MakeTileds2(0,20,20);//产生正方形的棋盘网格，20*20大小。    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>MakeTileds2方法内容如下：</p>
<pre><code class="copyable">  1 arr_tilednodes=[];//一个二维数组，保存棋盘中的每个地块对象
  2 mesh_tiledCard=null;//所有棋子对象的父网格，是mesh_tiledGround的子元素
  3 function MakeTileds2(type,sizex,sizez)//换一种地块构造方式，想到tiledGround事实上并没有必要性，如果忽略掉性能上可能存在的优势
  4 &#123;
  5     //给几种遮罩层建立材质：蓝色、红色、黄色、绿色、全透明
  6     var mat_alpha_blue=new BABYLON.StandardMaterial("mat_alpha_blue", scene);
  7     mat_alpha_blue.diffuseTexture = new BABYLON.Texture("../ASSETS/IMAGE/LANDTYPE/alpha_blue.png",scene);
  8     mat_alpha_blue.diffuseTexture.hasAlpha=true;//声明漫反射纹理图片具有透明度
  9     mat_alpha_blue.useAlphaFromDiffuseTexture=true;//启用漫反射纹理的透明度
 10     //mat_alpha_blue.hasVertexAlpha=true;
 11     //mat_alpha_blue.diffuseColor = new BABYLON.Color3(0, 0,1);
 12     //mat_alpha_blue.alpha=0.2;//不透明度
 13     mat_alpha_blue.useLogarithmicDepth=true;//为了和卡牌之间正常显示，它也必须这样设置深度？
 14     MyGame.materials.mat_alpha_blue=mat_alpha_blue;
 15     var mat_alpha_red=new BABYLON.StandardMaterial("mat_alpha_red", scene);
 16     mat_alpha_red.diffuseTexture = new BABYLON.Texture("../ASSETS/IMAGE/LANDTYPE/alpha_red.png",scene);
 17     mat_alpha_red.diffuseTexture.hasAlpha=true;
 18     mat_alpha_red.useAlphaFromDiffuseTexture=true;
 19     //mat_alpha_red.diffuseColor = new BABYLON.Color3(1, 0,0);
 20     //mat_alpha_red.alpha=0.2;//不透明度
 21     mat_alpha_red.useLogarithmicDepth=true;
 22     MyGame.materials.mat_alpha_red=mat_alpha_red;
 23     var mat_alpha_green=new BABYLON.StandardMaterial("mat_alpha_green", scene);
 24     mat_alpha_green.diffuseTexture = new BABYLON.Texture("../ASSETS/IMAGE/LANDTYPE/alpha_green.png",scene);
 25     mat_alpha_green.diffuseTexture.hasAlpha=true;
 26     mat_alpha_green.useAlphaFromDiffuseTexture=true;
 27     //mat_alpha_green.diffuseColor = new BABYLON.Color3(0, 1,0);
 28     //mat_alpha_green.alpha=0.2;//不透明度
 29     mat_alpha_green.useLogarithmicDepth=true;
 30     MyGame.materials.mat_alpha_green=mat_alpha_green;
 31     var mat_alpha_yellow=new BABYLON.StandardMaterial("mat_alpha_yellow", scene);
 32     mat_alpha_yellow.diffuseTexture = new BABYLON.Texture("../ASSETS/IMAGE/LANDTYPE/alpha_yellow.png",scene);
 33     mat_alpha_yellow.diffuseTexture.hasAlpha=true;
 34     mat_alpha_yellow.useAlphaFromDiffuseTexture=true;
 35     //mat_alpha_yellow.diffuseColor = new BABYLON.Color3(1, 1,0);
 36     //mat_alpha_yellow.alpha=0.2;//不透明度
 37     mat_alpha_yellow.useLogarithmicDepth=true;
 38     MyGame.materials.mat_alpha_yellow=mat_alpha_yellow;
 39     var mat_alpha_null=new BABYLON.StandardMaterial("mat_alpha_null", scene);//或者直接将遮罩设为不可见？
 40     mat_alpha_null.diffuseColor = new BABYLON.Color3(1, 1,1);
 41     mat_alpha_null.alpha=0;//不透明度
 42     mat_alpha_null.useLogarithmicDepth=true;
 43     MyGame.materials.mat_alpha_null=mat_alpha_null;
 44 
 45     mesh_tiledCard=new BABYLON.Mesh("mesh_tiledCard",scene);//所有单位的父元素
 46     mesh_tiledCard.parent=mesh_tiledGround;
 47     if(type==0)// 两层循环
 48     &#123;
 49         var obj_p=&#123;xmin:-30,xmax:30,zmin:-30,zmax:30,precision :&#123;"w" : 2,"h" : 2&#125;,subdivisions:&#123;"w" : sizex,"h" : sizez&#125;
 50         &#125;;
 51         var heightp=(obj_p.zmax-obj_p.zmin)/sizez;//每一个小块的高度
 52         var widthp=(obj_p.xmax-obj_p.xmin)/sizex;
 53         obj_p.heightp=heightp;
 54         obj_p.widthp=widthp;
 55         mesh_tiledGround.obj_p=obj_p;//将地块的初始化参数记录下来
 56 
 57         //认为行数从上向下延伸，列数从左向右延伸
 58         for(var i=0;i<sizez;i++)//从0开始还是从1开始？?
 59         &#123;//对于每一列？->还是一行一行处理更好
 60             var z=obj_p.zmax-(heightp*i+0.5*heightp);
 61             var arr_rownodes=[];
 62             for(var j=0;j<sizex;j++)
 63             &#123;
 64                 var x=obj_p.xmin+(widthp*j+0.5*widthp);
 65                 //建立一个显示地面纹理的地块，需要把地块也做成一个类吗？
 66                 var mesh_tiled=new BABYLON.MeshBuilder.CreateGround("mesh_tiled_"+i+"_"+j
 67                     ,&#123;width:widthp,height:heightp,subdivisionsX : 2,subdivisionsY : 2,updatable:false&#125;,scene);
 68                 mesh_tiled.index_row=i;
 69                 mesh_tiled.index_col=j;
 70                 mesh_tiled.heightp=heightp;
 71                 mesh_tiled.widthp=widthp;
 72                 mesh_tiled.position.z=z;
 73                 mesh_tiled.position.x=x;
 74                 mesh_tiled.position.y=-1;//略低一点，使地块位于棋子的下面
 75                 mesh_tiled.parent=mesh_tiledGround;
 76                 mesh_tiled.renderingGroupId=2;
 77                 //随机给这个地块分配一种地形，参考DataWar的方式？？
 78                 var landtype=newland.RandomChooseFromObj(arr_landtypes);//从地形列表里等概率的选取一种地形
 79                 mesh_tiled.landtype=landtype.name;//地形名称
 80                 mesh_tiled.cost=arr_landtypes[landtype.name].cost;//这种地形的消耗
 81                 if(MyGame.materials["mat_"+landtype.name])//如果已经创建过这种类型的材质，则直接将材质交给网格
 82                 &#123;
 83                     mesh_tiled.material=MyGame.materials["mat_"+landtype.name];
 84                 &#125;
 85                 else
 86                 &#123;//否则建立这种地形材质并交个网格
 87                     var mat_tiled = new BABYLON.StandardMaterial("mat_"+landtype.name,scene);
 88                     mat_tiled.diffuseTexture = new BABYLON.Texture(landtype.Url,scene);
 89                     mat_tiled.useLogarithmicDepth=true;
 90                     MyGame.materials["mat_"+landtype.name]=mat_tiled;
 91                     mesh_tiled.material=mat_tiled;
 92                 &#125;
 93                 var mesh_mask=new BABYLON.MeshBuilder.CreatePlane("mesh_mask_"+i+"_"+j
 94                     ,&#123;width:widthp-0.1,height:heightp-0.1&#125;,scene);//为每一个地块建立一个遮罩网格
 95                 mesh_mask.material=MyGame.materials.mat_alpha_null;//在不显示范围时，所有的遮罩默认不可见
 96                 mesh_mask.parent=mesh_tiled;
 97                 mesh_tiled.mask=mesh_mask;
 98                 mesh_mask.rotation.x=Math.PI*0.5;
 99                 mesh_mask.position.y=0.1;
100                 mesh_mask.renderingGroupId=2;
101                 mesh_mask.isPickable=false;//遮罩只用来显示，是不接收鼠标点击事件的
102                 arr_rownodes.push(mesh_tiled);
103             &#125;
104             arr_tilednodes.push(arr_rownodes);
105         &#125;
106     &#125;
107 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这段代码首先设计了棋盘、地块、棋子网格之间的从属关系。然后在5到43行建立了表示地块不同状态的几种遮罩材质，最初使用</p>
<p>带有透明度的纯色材质（被注释掉的部分），后来发现纯色的半透明遮罩容易和地块颜色混淆，并且不同地块之间的边界不够分明，于是改为使用半透明图片作为遮罩的纹理。使用canvas生成半透明图片的代码如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/924eac0397924d7492900cb576c1a8b8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e2f265e4b54463e91711670f2af78cd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"> 1 <!DOCTYPE html>
 2 <html lang="en">
 3 <head>
 4     <meta charset="UTF-8">
 5     <title>用canvas生成含有半透明度的PNG图片</title>
 6 </head>
 7 <body>
 8 <div id="div_allbase">
 9     <canvas style="width: 512px;height: 512px" width="512" height="512" id="can_pic">
10 
11     </canvas>
12 </div>
13 </body>
14 <script>
15     var canvas=document.getElementById("can_pic");
16     window.onload=loadImage;
17     function loadImage()
18     &#123;
19         var context=canvas.getContext("2d");
20         context.fillStyle="rgb(0,255,0)";
21         context.fillRect(0,0,512,512);
22         drawRoundRect(context, 16, 16, 480, 480, 32);//建立一个路径，上下文、距canvas左上角距离、宽高、圆角半径
23         //context.strokeStyle = "#ff0000";
24         context.fillStyle="rgb(255,255,255)";
25         //context.stroke();//绘制路径
26         context.fill();//填充路径，关闭了路径也可以填充和绘制路径
27         //带有透明度的覆盖并不是替换颜色，而是混合颜色，比如0 0 255 255与0 255 0 64的混合结果是0 64 255 255，其实质应该是根据不透明度加权求和
28         //所以为了精确的设置颜色，还是通过ImageData逐像素设置比较好。
29 
30         var imagedata_temp=context.getImageData(0,0,512,512);//规定地貌块纹理图片的宽高是512
31         var data=imagedata_temp.data;
32         var len=data.length;
33         for(var i=0;i<len;i+=4)//对于每一个像素
34         &#123;
35             if(data[i]==255&&data[i+1]==255&&data[i+2]==255)//如果是纯白色
36             &#123;
37                 data[i]=0;
38                 data[i+1]=255;
39                 data[i+2]=0;
40                 data[i+3]=64;
41             &#125;
42             else
43             &#123;
44                 data[i+3]=192;
45             &#125;
46 
47         &#125;
48         context.putImageData(imagedata_temp,0,0);
49     &#125;
50 //网上找到的生成圆角矩形路径的方法
51     function drawRoundRect(cxt, x, y, width, height, radius)&#123;
52         cxt.beginPath();
53         cxt.arc(x + radius, y + radius, radius, Math.PI, Math.PI * 3 / 2);
54         cxt.lineTo(width - radius + x, y);
55         cxt.arc(width - radius + x, radius + y, radius, Math.PI * 3 / 2, Math.PI * 2);
56         cxt.lineTo(width + x, height + y - radius);
57         cxt.arc(width - radius + x, height - radius + y, radius, 0, Math.PI * 1 / 2);
58         cxt.lineTo(radius + x, height +y);
59         cxt.arc(radius + x, height - radius + y, radius, Math.PI * 1 / 2, Math.PI);
60         cxt.closePath();
61     &#125;
62 
63 </script>
64 </html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>View Code</p>
<p>　　其大概思路是首先用特定颜色在canvas中标志出一块区域，然后遍历canvas中的像素，将符合特定颜色的像素修改为需要的rgba颜色。</p>
<p>　　接下来根据设定的尺寸，为每个地块生成一个网格，再为每个地块网格生成一个遮罩网格，通过为遮罩网格设置不同的材质来表示地块网格的不同状态，而遮罩网格比地块网格略小一点，这可以让遮罩之间的界限更清晰。生成地块时用到的这种按行、按列遍历计算元素位置的算法，在图像处理和表格绘制程序中也很常用，要考虑将它封装为一个通用方法。</p>
<p>　　值得注意的是，Babylon.js内部也封装有一个建立“棋盘网格”的方法，但是我并没有发现这个方法的优势在哪里，反而因为所有地块无差别的合并在一个网格对象中导致对象选取困难，同时这种内置的棋盘网格只支持方形棋盘无法自定义棋盘形状。</p>
<p>　　RandomChooseFromObj方法的作用是，随机选择对象属性中的一个返回，其代码如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/924eac0397924d7492900cb576c1a8b8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e2f265e4b54463e91711670f2af78cd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"> 1 newland.RandomChooseFromObj=function(obj)//随机从一个对象的所有属性中按照概率选择一个属性
 2 &#123;
 3     var len=Object.getOwnPropertyNames(obj).length;//所有属性的个数
 4     var count_rate=0;
 5     var num=Math.random();
 6     var result=null;
 7     for(var key in obj)
 8     &#123;
 9         var ratep=1/len;
10         var pro=obj[key];
11         if(pro.rate)
12         &#123;
13             ratep=pro.rate;
14         &#125;
15         count_rate+=ratep;
16         if(count_rate>num)
17         &#123;
18             result=pro;
19             return result;//理论上讲总会从这里返回一个
20         &#125;
21     &#125;
22     return "fault";
23 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>View Code</p>
<p>　　</p>
<p>2、将鼠标点击事件重构为CameraClick方法，将代码从CameraMesh类里移出，放置在CameraClick.js文件中：</p>
<pre><code class="copyable"> 1 //专门处理相机点击事件
 2 function CameraClick(_this,evt)
 3 &#123;
 4     if(MyGame.init_state==1||MyGame.init_state==2)//点击canvas则锁定光标，在因为某种原因在first_lock状态脱离焦点后用来恢复焦点
 5     &#123;//不锁定指针时，这个监听什么也不做
 6         if(MyGame.flag_view!="first_pick")
 7         &#123;
 8             canvas.requestPointerLock = canvas.requestPointerLock || canvas.msRequestPointerLock || canvas.mozRequestPointerLock || canvas.webkitRequestPointerLock;
 9             if (canvas.requestPointerLock) &#123;//用于鼠标意外离开浏览器后重新锁定光标
10                 canvas.requestPointerLock();
11 
12                 MyGame.flag_view="first_lock";
13 
14                 _this.centercursor.isVisible=true;
15             &#125;
16             if(MyGame.init_state==1)
17             &#123;
18                 var width = engine.getRenderWidth();
19                 var height = engine.getRenderHeight();
20                 var pickInfo = scene.pick(width/2, height/2, null, false, MyGame.Cameras.camera0);
21                 if(pickInfo.hit&&pickInfo.pickedMesh.name.substr(0,5)=="card_")//根据网格的名字判断
22                 &#123;//点击棋盘上的一张卡，认为这时不可多选，并且同样可以点击其他人的卡片，但只能控制自己的卡片（？）
23                     cancelPropagation(evt);
24                     cancelEvent(evt);
25                     var mesh=pickInfo.pickedMesh;
26                     var card=mesh.card;
27                     PickCard2(card);//在棋盘上点击卡片
28                 &#125;
29                 else if(pickInfo.hit&&pickInfo.pickedMesh.name.substr(0,6)=="mesh_t")
30                 &#123;//如果点击在地块上，如果是第一次点击则显示路径，用粒子效果？如果已经计算了路径则表示路径确认，通过动画按路径移动
31                     PickTiled(pickInfo);
32                 &#125;
33             &#125;
34         &#125;
35         else//在非锁定光标（first_pick）时，click监听似乎不会被相机阻断，而mousedown会被相机阻断
36         &#123;
37             if(MyGame.flag_view=="first_ani")//由程序控制视角的动画时间
38             &#123;
39                 cancelPropagation(evt);
40                 cancelEvent(evt);
41                 return;
42             &#125;
43             //var width = engine.getRenderWidth();
44             //var height = engine.getRenderHeight();
45             var pickInfo = scene.pick(scene.pointerX, scene.pointerY, null, false, MyGame.Cameras.camera0);//点击信息，取屏幕中心信息而不是鼠标信息！！
46             if(MyGame.init_state==1&&MyGame.flag_view=="first_pick"
47                 &&pickInfo.hit&&pickInfo.pickedMesh.name.substr(0,5)=="card_"&&pickInfo.pickedMesh.card.belongto==MyGame.WhoAmI)//在一个卡片上按下鼠标，按下即被选中
48             &#123;//点击手牌中的一张卡片
49                 cancelPropagation(evt);
50                 cancelEvent(evt);
51                 //releaseKeyState();
52                 var mesh=pickInfo.pickedMesh;
53                 var card=mesh.card;
54                 PickCard(card);
55             &#125;
56 
57         &#125;
58     &#125;
59 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、点击棋子的处理：　　</p>
<pre><code class="copyable"> 1 function PickCard2(card)//点击一下选中，高亮边缘，在非选中状态使用2D视角跟随，还是3D视角跟随？，再点击一下则拉近放大，是否要调整视角跟随方式？
 2 //同时还要在卡片附近建立一层蓝色或红色的半透明遮罩网格，表示移动及影响范围
 3 &#123;//如果再次点击有已选中卡片，则把相机移到卡片面前
 4     if(card.isPicked)
 5     &#123;
 6         GetCardClose2(card);
 7         //DisposeRange();//隐藏范围显示，规定点击棋盘时计算到达路径，点击空处时清空范围，点击其他卡牌时切换范围，切换成手牌时清空范围
 8     &#125;
 9     else
10     &#123;
11         //getPicked(card);//考虑到选择新的棋子前要先清空已选中的棋子，这三句放在后面执行
12         //card.isPicked=true;//设为被选中卡片并为它计算范围
13         //card_Closed2=card;//card_Closed2是保存当前选定的棋子的全局变量
14         DisplayRange(card);
15     &#125;
16 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　当这个棋子已经被选中时，再次点击这个棋子将把相机移动到棋子面前，其代码如下：</p>
<pre><code class="copyable"> 1 function GetCardClose2(card)//让相机靠近card！！？？
 2 &#123;
 3     MyGame.flag_view="first_ani";
 4     MyGame.anicount=2;//如果开启了多个物体的动画，要确定这些物体的动画都结束再退出动画状态
 5     var pos_card=card.mesh._absolutePosition.clone();//获取相机对象的世界坐标系位置
 6     var pos_camera=MyGame.player.mesh.position.clone();//相机对象的局部坐标系位置，应该等于世界坐标系位置
 7     var pos=pos_card.clone().add(pos_camera.clone().subtract(pos_card).normalize().scale(3));
 8     var animation3=new BABYLON.Animation("animation3","position",30,BABYLON.Animation.ANIMATIONTYPE_VECTOR3,BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT);
 9     var keys1=[&#123;frame:0,value:MyGame.player.mesh.position.clone()&#125;,&#123;frame:30,value:pos&#125;];
10     animation3.setKeys(keys1);
11 
12 
13     var rot_camera=MyGame.player.mesh.rotation.clone();
14     var tran_temp=new BABYLON.Mesh("tran_temp",scene);//Babylon.js的“变换节点”类对象可能更适合
15     tran_temp.position=pos;//创建一个位于棋子面前的“暂时网格”，让这个网格朝向棋子，然后获取这个网格的姿态
16     tran_temp.lookAt(pos_card,Math.PI,0,0);//,Math.PI,Math.PI);YXZ?
17     var rot=tran_temp.rotation.clone();//看起来这个rot是反向的，如何把它正过来？
18     rot.x=-rot.x;
19     //MyGame.PI2=Math.PI*2;
20     //rot.x=(rot.x-Math.PI)%MyGame.PI2;
21     //rot.y=(rot.y-Math.PI)%MyGame.PI2;
22     //rot.z=0;//出现了奇怪的坐标反向
23     tran_temp.dispose();
24     var animation4=new BABYLON.Animation("animation4","rotation",30,BABYLON.Animation.ANIMATIONTYPE_VECTOR3,BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT);
25     var keys2=[&#123;frame:0,value:rot_camera&#125;,&#123;frame:30,value:rot&#125;];
26     animation4.setKeys(keys2);
27     MyGame.player.mesh.animations.push(animation3);//mesh和camera必须使用相同的动画？
28     //MyGame.Cameras.camera0.animations.push(animation3);
29     MyGame.Cameras.camera0.animations.push(animation4);
30     //MyGame.player.mesh.animations.push(animation4);
31     scene.beginAnimation(MyGame.player.mesh, 0, 30, false,1,function()&#123;
32         MyGame.anicount--;
33         if(MyGame.anicount==0)
34         &#123;
35             MyGame.flag_view="first_lock";
36         &#125;
37     &#125;);
38     scene.beginAnimation(MyGame.Cameras.camera0, 0, 30, false,1,function()&#123;
39         MyGame.anicount--;
40         if(MyGame.anicount==0)
41         &#123;
42             MyGame.flag_view="first_lock";
43         &#125;
44     &#125;);
45 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　代码的第七行计算了“棋子面前”的位置，其位置是“从棋子位置出发，向相机位置移动3单位距离”。接下来是计算相机移动到棋子面前时的朝向，Babylon.js中的lookAt方法可以使网格朝向某个指定的世界坐标系位置，但是其实际效果似乎和文档存在出入，经过反复试验找到了一种可行的用法，但并不确定原理。上述变换的示意图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0708f6038a6248cca81c225c27170eec~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> 　　然后是把相机移动后的位置 设为“相机网格类”的网格 的位置动画的关键帧，将相机移动后的姿态 设为相机网格类的相机 的姿态动画的关键帧，并执行动画。在渲染循环中，相机网格对象的相机会应用网格的位置，而网格则会应用相机的姿态。这样设置的原因可以参考上篇文章中对CameraMesh类的介绍。</p>
<p>4、计算并显示棋子的移动范围和影响范围：</p>
<p>a、准备工作：</p>
<pre><code class="copyable"> 1 arr_nodepath=&#123;&#125;;//使用它保存移动范围内每一个节点的消耗值与移动路径。这个变量是冗余的吗？-》不是
 2 arr_DisplayedMasks=[];//保存每个显示的遮罩对象
 3 arr_noderange=&#123;&#125;;//保存每个可能被影响的节点（红色材质），它不可以包含arr_nodepath中的节点
 4 function DisplayRange(card)//显示这个card的范围
 5 &#123;
 6     //首先要检查是否有已经显示的遮罩
 7     if(arr_DisplayedMasks.length>0)
 8     &#123;
 9         HideAllMask();//这里也会清空card_Closed2
10     &#125;
11     card_Closed2=card;//因为HideAllMask会清空已选中的棋子，所以切换棋子时的棋子选定代码应放在这里。
12     getPicked(card_Closed2);
13     card.isPicked=true;
14     if(card.workstate!="wait")
15     &#123;
16         return;//如果不在待命状态则不予显示范围遮罩
17     &#125;
18     var node_start=FindNode(card.mesh.position);//找到点击的棋子所在的格子
19     //var str=node_start.name;
20     arr_nodepath=&#123;&#125;;//将移动范围数据清空，然后将第一个地块（节点）放入
21     arr_noderange=&#123;&#125;;//将影响范围数据清空
22     arr_nodepath[node_start.name]=&#123;cost:0,path:[node_start.name],node:node_start&#125;;
23     //arr_nodepath=&#123;str:&#123;cost:0,path:[node_start.name]&#125;&#125;;
24     //node_start.open=true;
25     var list_node=[];//需要依次计算的节点列表
26     list_node.push(node_start);//一开始节点列表里只有第一个地块（起点）
27     var power=card.speed;//把卡牌的速度属性作为移动力
28     var costg=0;//消耗计量器，计算要分成两段，第一段是移动范围，第二段是影响范围（超过移动范围之后，所有地块消耗都视为1）
29     //var path=[node_start.name];//只在路径里保存名称，这样可以用concat??
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这一段代码初始化了范围计算所需的各项数据，其中FindNode方法的作用是根据棋子的位置寻找棋子所在的地块，其代码如下：</p>
<pre><code class="copyable">1 function FindNode(pos)//根据pos找到对应的地块
2 &#123;
3     var obj_p=mesh_tiledGround.obj_p;
4     var num_row=Math.floor((obj_p.zmax-pos.z)/obj_p.heightp);//暂时不考虑卡牌脱出棋盘之外的情况
5     var num_col=Math.floor((pos.x-obj_p.xmin)/obj_p.widthp);
6     var node=arr_tilednodes[num_row][num_col];
7     return node;
8 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>b、计算棋子的移动范围：</p>
<p>　　在编程过程中我发现list_node和arr_nodepath保存的数据存在重合，但是一方面要通过list_node顺序的遍历节点，另一方面又要在后续的代码中通过名字访问arr_nodepath中的数据，所以决定同时使用数组和对象这两种数据结构。</p>
<pre><code class="copyable"> 1 for(var i=0;i<list_node.length;i++)//这种变长的顺序遍历需要使用数组，而后面的按名称选择又要用到对象属性-》所以保持两套变量？？？？
 2     &#123;//对于节点列表中的每个节点，把它叫做“中央节点”把
 3         var arr_node_neighbor=FindNeighbor(list_node[i]);//找到它周围的所有节点
 4         var len=arr_node_neighbor.length;//
 5         for(var j=0;j<len;j++)//对于每一个邻居节点
 6         &#123;
 7             var nextnode=arr_node_neighbor[j];
 8             costg=arr_nodepath[list_node[i].name].cost;//到达中央节点的消耗
 9             //在计算移动时有两个思路，一是设定每一种地面的行动力消耗，二是设定每一种单位对每一种地形的行动能力，看来第一种更简单
10             //认为最初的起点消耗为0
11             costg+=nextnode.cost;//认为到达这个邻居节点的消耗是：到达中央节点的消耗+这个邻居节点的消耗
12             //path.push(nextnode);
13             var path2=arr_nodepath[list_node[i].name].path.concat();//到达中央节点的路径
14             path2.push(nextnode.name);//加入这个邻居节点
15             if(costg>power)//如果消耗超过了移动力，则认为这个邻居节点是通过这条路径所无法到达的
16             &#123;
17                 if(arr_nodepath[nextnode.name])//如果使用其他路径能够到达这个节点
18                 &#123;
19                     continue;//考虑下一个邻居
20                 &#125;
21                 else//如果超过移动范围，则将这个移动边界节点作为考虑影响范围时的一个起点
22                 &#123;
23                     arr_noderange[nextnode.name]=&#123;cost:1,path:[nextnode.name],path0:path2,node:nextnode&#125;;//那么这个点可能是影响范围内的起始节点
24                 &#125;
25             &#125;
26             else
27             &#123;//如果可以到达这个节点
28 
29 
30                 if(arr_nodepath[nextnode.name])//如果已经到达过这个节点，则要对消耗进行比较
31                 &#123;
32                     if(arr_nodepath[nextnode.name].cost>costg)//找到了到达这个点的更优方式
33                     &#123;//替换原先记录的到达这个节点的路径和消耗
34                         arr_nodepath[nextnode.name]=&#123;cost:costg,path:path2,node:nextnode&#125;;
35                     &#125;
36                     else&#123;//新的到达这个节点的方式并不更优
37                         continue;//考虑下一个邻居
38                     &#125;
39                 &#125;
40                 else//如果从未到达这个节点，则要计算到这个节点为止的消耗
41                 &#123;
42                     if(arr_noderange[nextnode.name])//如果这个节点在以前被设为移动边界节点，但又被证明可以达到
43                     &#123;
44                         delete arr_noderange[nextnode.name];
45                     &#125;
46                     arr_nodepath[nextnode.name]=&#123;cost:costg,path:path2,node:nextnode&#125;;
47                     list_node.push(nextnode);//第一次到达这个节点，则把这个节点加入节点列表，节点列表长度加一，接下来再使用这些新加入的节点作为中央节点计算范围
48                 &#125;
49             &#125;
50         &#125;
51     &#125;//节点列表遍历完成时，arr_nodepath中就保存了到达移动范围内的每个节点的路径和消耗
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　其中FindNeighbor方法用来寻找中央节点上下左右的四个“邻居节点”:</p>
<pre><code class="copyable"> 1 function FindNeighbor(node)//寻找一个地块周围的所有地块（最多四个）
 2 &#123;
 3     var arr_node_neighbor=[]
 4     var total_row=arr_tilednodes.length;//棋盘有多少行
 5     var total_col=arr_tilednodes[0].length;//棋盘有多少列
 6     var index_row=node.index_row;
 7     var index_col=node.index_col;
 8     //上面的
 9     var i=index_row-1;
10     if(i>=0)//如果不超出棋盘范围
11     &#123;
12         arr_node_neighbor.push(arr_tilednodes[i][index_col]);
13     &#125;
14     //右面的
15     i=index_col+1;
16     if(i<total_col)
17     &#123;
18         arr_node_neighbor.push(arr_tilednodes[index_row][i]);
19     &#125;
20     //下面的
21     i=index_row+1;
22     if(i<total_row)
23     &#123;
24         arr_node_neighbor.push(arr_tilednodes[i][index_col]);
25     &#125;
26     //左面的
27     i=index_col-1;
28     if(i>=0)
29     &#123;
30         arr_node_neighbor.push(arr_tilednodes[index_row][i]);
31     &#125;
32     return arr_node_neighbor;
33 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>c、计算棋子影响范围：</p>
<p>　　计算方式和前面计算移动范围的算法是相似的，只有一点小区别。</p>
<pre><code class="copyable"> 1 //寻找单位的影响范围
 2     var range=card.range;//将卡牌对象的范围属性作为棋子的影响范围
 3     var list_noderange=[];//计算范围的节点列表
 4     for(var key in arr_noderange)
 5     &#123;//将前面收集的边界节点放入节点列表
 6         list_noderange.push(arr_noderange[key].node)
 7     &#125;
 8     for(var i=0;i<list_noderange.length;i++)//遍历节点列表
 9     &#123;
10         var arr_node_neighbor=FindNeighbor(list_noderange[i]);
11         var len=arr_node_neighbor.length;
12         for(var j=0;j<len;j++)//对于每一个邻居节点
13         &#123;
14             costg=arr_noderange[list_noderange[i].name].cost;
15             costg+=1;//认为每个地块的影响消耗都为1
16             if(costg>range)
17             &#123;
18                 break;//因为影响范围的cost都是相同的，所以只要有一个邻居超过限度，则所有邻居都不可用
19             &#125;
20             //如果没有超限
21             var nextnode = arr_node_neighbor[j];
22             if(arr_nodepath[nextnode.name])//如果这个节点在可到达区域，则必然不在范围区域
23             &#123;
24                 continue;
25             &#125;
26             else
27             &#123;
28                 var path2=arr_noderange[list_noderange[i].name].path.concat();//从起始点去这个中央节点的路径
29                 path2.push(nextnode.name);
30                 if(arr_noderange[nextnode.name])//如果以前曾经到达这个节点
31                 &#123;
32                     if(arr_noderange[nextnode.name].cost>costg)
33                     &#123;
34                         arr_noderange[nextnode.name]=&#123;cost:costg,path:path2,node:nextnode,path0:arr_noderange[list_noderange[i].name].path0&#125;;
35                     &#125;
36                     else
37                     &#123;
38                         continue;
39                     &#125;
40                 &#125;
41                 else
42                 &#123;
43                     arr_noderange[nextnode.name]=&#123;cost:costg,path:path2,node:nextnode,path0:arr_noderange[list_noderange[i].name].path0&#125;;
44                     list_noderange.push(nextnode);
45                 &#125;
46             &#125;
47         &#125;
48     &#125;//遍历完成时arr_noderange里包含了影响范围内的每个节点的信息，其中path0是到达最近的（之一）边界节点的路径，path2是到达影响节点的路径。
49     DisplayAllMask()
50 
51 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　计算完成后使用DisplayAllMask方法，将移动范围和影响范围显示出来：</p>
<pre><code class="copyable"> 1 function DisplayAllMask()//绘制出移动范围和影响范围的遮罩
 2 &#123;
 3     for(var key in arr_nodepath)
 4     &#123;
 5         if(arr_nodepath[key].cost>0)
 6         &#123;
 7             arr_nodepath[key].node.mask.material=MyGame.materials.mat_alpha_blue;//蓝色表示移动范围
 8         &#125;
 9         arr_DisplayedMasks.push(arr_nodepath[key].node.mask);
10     &#125;
11     for(var key in arr_noderange)
12     &#123;
13         arr_noderange[key].node.mask.material=MyGame.materials.mat_alpha_red;//红色表示影响范围
14         arr_DisplayedMasks.push(arr_noderange[key].node.mask);
15     &#125;
16 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 5、点击地块的处理：</p>
<p>　　考虑到点击棋子可能比较困难，这里设定为点击棋子所在的地块也能选中棋子；另外，遮罩网格只是起显示作用，在选中棋子之后，也要通过监听地块的点击事件来决定棋子的移动目标。</p>
<pre><code class="copyable"> 1 function  PickTiled(pickInfo)//点击地块
 2 &#123;
 3     //不论是否有范围遮罩，点击地块就显示地块属性？-》下一步添加
 4     var mesh=pickInfo.pickedMesh;
 5     if(arr_DisplayedMasks.length>0&&card_Closed2)//如果存在地块遮罩，并且有选中的单位
 6     &#123;
 7         //如果点击的另一个地块里已经有一个单位，这里认为一个地块只能有一个单位，所以要切换被选中的单位
 8         var mesh_unit=TiledHasCard(mesh);//找到被点击的地块中的棋子
 9         if(mesh_unit)//如果找到了
10         &#123;
11             if(mesh_unit.name!=card_Closed2.mesh.name)
12             &#123;
13                 PickCard2(mesh_unit.card);//替换选中的棋子
14             &#125;
15             else//如果点击的是自己的地块！！拉近卡片
16             &#123;
17                 GetCardClose2(mesh_unit.card);
18             &#125;
19             return;
20         &#125;
21         //如果没有点击到别的单位的地块
22         //点击影响范围也自动寻路过去？
23         //if(arr_noderange[mesh.name])//如果在影响范围内
24         if(mesh.mask.material.name=="mat_alpha_red")//如果点击到红色地块
25         &#123;
26             //先清空可能存在的黄色路径
27             for(var key in arr_noderange)
28             &#123;
29                 var node=arr_noderange[key].node;
30                 if(node.mask.material.name=="mat_alpha_yellow")
31                 &#123;
32                     node.mask.material=MyGame.materials.mat_alpha_blue;
33                 &#125;
34             &#125;
35             if(card_Closed2.workstate=="wait")//如果棋子处在等待状态，点击红地块是移动到相应移动边界的意思
36             &#123;
37                 var path=arr_noderange[mesh.name].path0;//取到达这一点的路径，将对应地块置为黄色
38                 var len=path.length;
39                 for(var i=0;i<len;i++)
40                 &#123;
41                     if(arr_nodepath[path[i]]&&!TiledHasCard(arr_nodepath[path[i]].node))
42                     &#123;
43                         arr_nodepath[path[i]].node.mask.material=MyGame.materials.mat_alpha_yellow;//走过的路径地块标为黄色
44                     &#125;
45                 &#125;
46             &#125;
47             else if(card_Closed2.workstate=="moved")//如果已经移动了，那么这次点击就是发动效果
48             &#123;
49 
50             &#125;
51         &#125;
52         else if(mesh.mask.material.name=="mat_alpha_blue")//如果这个被点击的地块在选中单位的移动范围内
53         &#123;//点击了蓝色地块
54             //先清空可能存在的黄色路径
55             for(var key in arr_noderange)
56             &#123;
57                 var node=arr_noderange[key].node;
58                 if(node.mask.material.name=="mat_alpha_yellow")
59                 &#123;
60                     node.mask.material=MyGame.materials.mat_alpha_blue;
61                 &#125;
62             &#125;
63             var path=arr_nodepath[mesh.name].path;//取到达这一点的路径
64             var len=path.length;
65             for(var i=0;i<len;i++)
66             &#123;
67                 if(arr_nodepath[path[i]]&&!TiledHasCard(arr_nodepath[path[i]].node))//有单位存在的格子不置黄
68                 &#123;
69                     arr_nodepath[path[i]].node.mask.material=MyGame.materials.mat_alpha_yellow;//走过的路径地块标为黄色
70                 &#125;
71             &#125;
72         &#125;
73         else if(mesh.mask.material.name=="mat_alpha_yellow")//如果点击的是黄色地块，则移动到目标地块
74         &#123;
75             var path=arr_nodepath[mesh.name].path;//取到达这一点的路径，点到黄色地块的路径必然是可通行的？？
76             CardMove2Tiled(path);
77         &#125;
78         else//点击移动范围外的点
79         &#123;
80             HideAllMask();//取消棋子选定并隐藏所有遮罩
81         &#125;
82     &#125;
83     else&#123;
84         //如果在没有选中棋子时，点击了一个地块
85         var mesh_unit=TiledHasCard(mesh);
86         if(mesh_unit)//如果这个地块中存在棋子
87         &#123;
88             if(mesh_unit.card)
89             &#123;
90                 PickCard2(mesh_unit.card);//等同于点击棋子
91             &#125;
92             return;
93         &#125;
94     &#125;
95 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这段代码通过一系列条件判断，规定了每一种点击情况的处理方式，具体规则参考代码注释。</p>
<p>　　其中TiledHasCard方法用来寻找地块中可能存在的棋子：</p>
<pre><code class="copyable"> 1 function TiledHasCard(node)//寻找这个地块之内的单位，参数是地块对象
 2 &#123;
 3     var units=mesh_tiledCard._children;//这里存储的是卡牌对象的网格
 4     var len=units.length;
 5     var xmin=node.position.x-node.widthp/2;//这个地块的范围
 6     var xmax=node.position.x+node.widthp/2;
 7     var zmin=node.position.z-node.heightp/2;
 8     var zmax=node.position.z+node.heightp/2;
 9     for(var i=0;i<len;i++)
10     &#123;
11         var unit=units[i];
12         var pos=unit.position;
13         if(pos.x<xmax&&pos.x>xmin&&pos.z>zmin&&pos.z<zmax)//如果发现这个单位在这个地块以内
14         &#123;
15             return unit
16         &#125;
17     &#125;
18     return false;
19 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　HideAllMask方法隐藏所有遮罩，并取消当前棋子的选中：</p>
<pre><code class="copyable"> 1 function HideAllMask()//隐藏所有已经显示的mask，并且取消单位的选中
 2 &#123;
 3     var len=arr_DisplayedMasks.length;
 4     for(var i=0;i<len;i++)
 5     &#123;
 6         arr_DisplayedMasks[i].material=MyGame.materials.mat_alpha_null;
 7     &#125;
 8     arr_DisplayedMasks=[];
 9     arr_nodepath=&#123;&#125;;
10     arr_noderange=&#123;&#125;;
11     noPicked(card_Closed2);
12     card_Closed2=null;
13 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　CardMove2Tiled方法用来沿黄色路径移动棋子：</p>
<pre><code class="copyable"> 1 function CardMove2Tiled(path)
 2 &#123;
 3     MyGame.flag_view="first_ani";
 4     var len=path.length;
 5     //设计走一格用0.5秒分15帧
 6     var frame_total=len*15;
 7     var animation3=new BABYLON.Animation("animation3","position",30,BABYLON.Animation.ANIMATIONTYPE_VECTOR3,BABYLON.Animation.ANIMATIONLOOPMODE_CONSTANT);
 8     var keys1=[];
 9     for(var i=0;i<len;i++)//对于路径中的每个节点
10     &#123;
11         var pos=arr_nodepath[path[i]].node.position.clone();
12         pos.y=0;
13         keys1.push(&#123;frame:i*15,value:pos&#125;);添加对应的关键帧
14     &#125;
15     //var keys1=[&#123;frame:0,value:MyGame.player.mesh.position.clone()&#125;,&#123;frame:30,value:pos&#125;];
16     animation3.setKeys(keys1);
17     card_Closed2.mesh.animations.push(animation3);
18     MyGame.anicount=1;
19     var len=arr_DisplayedMasks.length;
20     for(var i=0;i<len;i++)//执行动画时把各种颜色的遮罩都取消
21     &#123;
22         arr_DisplayedMasks[i].material=MyGame.materials.mat_alpha_null;//这个数组里存的真的只是遮罩
23     &#125;
24     arr_DisplayedMasks=[];//清空它并不会影响移动和影响范围的保存！！！！
25     scene.beginAnimation(card_Closed2.mesh, 0, frame_total, false,1,function()&#123;
26         MyGame.anicount--;
27         if(MyGame.anicount==0)
28         &#123;
29             MyGame.flag_view="first_lock";
30             //HideAllMask();
31 
32             card_Closed2.workstate="moved";//移动完成之后将选中的棋子状态置为“已经移动”
33             DisplayRange2(card_Closed2,card_Closed2.range);//同一个单位使用不同技能可能有不同的影响范围
34         &#125;
35     &#125;);
36 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　执行动画的方式与前面基本相同，唯一的区别在于这里的关键帧是根据棋子移动路径生成的。动画完成之后执行DisplayRange2方法，显示棋子移动之后的影响范围，其代码如下：</p>
<pre><code class="copyable"> 1 var arr_noderange2=&#123;&#125;//移动之后计算范围用的数据结构
 2 function DisplayRange2(card,range)//只显示移动后的影响范围
 3 &#123;
 4     var node_start=FindNode(card.mesh.position);
 5     arr_noderange2=&#123;&#125;;
 6     arr_noderange2[node_start.name]=&#123;cost:0,path:[node_start.name],node:node_start&#125;;
 7     var costg=0;
 8     var range=card.range;
 9     var list_noderange=[node_start];
10     for(var i=0;i<list_noderange.length;i++)
11     &#123;
12         var arr_node_neighbor=FindNeighbor(list_noderange[i]);
13         var len=arr_node_neighbor.length;
14         for(var j=0;j<len;j++)
15         &#123;
16             costg=arr_noderange2[list_noderange[i].name].cost;
17             costg+=1;
18             if(costg>range)
19             &#123;
20                 break;//因为影响范围的cost都是相同的，所以只要有一个邻居超过限度，则所有邻居都不可用
21             &#125;
22             //如果没有超限
23             var nextnode = arr_node_neighbor[j];
24             var path2=arr_noderange2[list_noderange[i].name].path.concat();
25             path2.push(nextnode.name);
26             if(arr_noderange2[nextnode.name])//如果以前曾经到达这个节点
27             &#123;
28                 if(arr_noderange2[nextnode.name].cost>costg)//这里还是否有必要计算路径？？
29                 &#123;
30                     arr_noderange2[nextnode.name]=&#123;cost:costg,path:path2,node:nextnode&#125;;
31                 &#125;
32                 else
33                 &#123;
34                     continue;
35                 &#125;
36             &#125;
37             else
38             &#123;
39                 arr_noderange2[nextnode.name]=&#123;cost:costg,path:path2,node:nextnode&#125;;
40                 list_noderange.push(nextnode);
41             &#125;
42         &#125;
43     &#125;
44     for(var key in arr_noderange2)
45     &#123;
46         if(arr_noderange2[key].cost>0)
47         &#123;
48             arr_noderange2[key].node.mask.material=MyGame.materials.mat_alpha_red;
49         &#125;
50 
51         arr_DisplayedMasks.push(arr_noderange2[key].node.mask);
52     &#125;
53 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　是前面范围算法的简化版。</p>
<p>　　如此，完成了上述棋盘场景。</p>
<p>三、下一步</p>
<p>　　接下来计划尝试用eval函数编写即时计算的技能模块，并为场景添加简单的规则，然后参考Babylon.js文档尝试进行渲染优化提高帧数；再下一步计划引入以前编写的WebSocket组件，为场景添加多人交互控制。</p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p>　</p></div>  
</div>
            