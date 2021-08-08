
---
title: 'Unity 创建一个网格地图'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a45c255baa44544a6b9e47094416ee2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 23:37:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a45c255baa44544a6b9e47094416ee2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>如果你玩过三国志这种类型的战旗游戏或者模拟城市、部落冲突、海岛奇兵这种模拟经营类的游戏，那么你对网格地图一定不会陌生。在这些游戏中，所有地图场景中的物体都是基于整齐的网格来记录位置等信息。如下图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a45c255baa44544a6b9e47094416ee2~tplv-k3u1fbpfcp-watermark.image" alt="我在网上找了一张图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果你还是感知不到什么是网格地图。俄罗斯方块或者贪吃蛇你一定不会陌生，物体的存在是依托于规整的网格地图而存在的。</p>
<p>还是一如既往，本篇文章为零基础小白文，如果你是小萌新，并且对网格地图感兴趣的话，可以学习本片文章，然后尝试创建自己的游戏吧！</p>
<p>本文章的最终显示效果为：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3780ef70382b4fdb90da4049416c087c~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-1">1，创建组建出网格的基本单元</h4>
<p>我们知道网格是由一个个格子组成的，所以第一步需要先创建出一个基本的模板：</p>
<p>创建一个脚本命名为<code>Grid</code>，并定义一些我们需要修改的属性，由于本案例我想要创建一个有障碍物的地图，用来作为A*寻路的地图。所以需要下面的信息：</p>
<ul>
<li>模板宽度</li>
<li>模板高度</li>
<li>模板颜色</li>
<li>模板是否为障碍（由颜色标识）</li>
<li>模板点击事件（模板颜色转换）</li>
</ul>
<p>编写模板脚本：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">using</span> System.Collections;
<span class="hljs-keyword">using</span> System.Collections.Generic;
<span class="hljs-keyword">using</span> UnityEngine;
<span class="hljs-keyword">using</span> System;

<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title">Grid</span> : <span class="hljs-title">MonoBehaviour</span>
&#123;

    <span class="hljs-keyword">public</span> <span class="hljs-built_in">float</span> gridWidght;
    <span class="hljs-keyword">public</span> <span class="hljs-built_in">float</span> girdHeight;
    <span class="hljs-keyword">public</span> <span class="hljs-built_in">bool</span> isHinder;
    <span class="hljs-keyword">public</span> Color color;
    <span class="hljs-keyword">public</span> Action OnClick;    
    <span class="hljs-comment">//当网格地图比较大时，每帧更新模板颜色比较消耗性能，可以修改为通过事件触发</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">Update</span>(<span class="hljs-params"></span>)</span>
    &#123;
        gameObject.GetComponent<MeshRenderer>().material.color=color;
    &#125;
    <span class="hljs-comment">//委托绑定模板点击事件</span>
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">OnMouseDown</span>(<span class="hljs-params"></span>)</span>
    &#123;
        OnClick?.Invoke();
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编写好脚本后，创建模板预制体，本案例就使用一个简单的方块来作为演示案例，为了保证可以区分每一个方格，大小缩放到<code>0.9</code>，这样两个方格之间就会有空隙来分割不同的网格块。</p>
<p>创建好方格后，将<code>Grid</code>脚本挂在到物体上，并设置相关的初始参数，具体如图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bc481ba351a42898264e38670618b25~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">2，编辑网格创建脚本</h4>
<p>接下来我们就需要封装一个网格创建的脚本，创建一个脚本命名为<code>GridMeshCreate</code>，然后编写该脚本，为了实现创建网格地图的功能，我们需要获取到一些基本信息：</p>
<ul>
<li>创建网格的宽度：<code>x</code>轴<code>Grid</code>预制体的个数</li>
<li>创建网格的高度：<code>y</code>轴<code>Grid</code>预制体的个数</li>
<li>创建网格中<code>Grid</code>的位置：通过一个初始点，然后通过<code>Grid</code>的长宽计算</li>
</ul>
<p>完成上面的信息的定义后，我们就可以编写脚本来实现网格创建的功能了，但是在此之前我们要思考一个问题，我们的创建的每一个<code>Grid</code>的会完全一摸一样吗。答案肯定是不会。比如说，在一些模拟经营的游戏中，一个物体可能会对周围的环境造成一些影响，为了标识其影响范围，就需要通过不同颜色的网格来表示，如图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce5d9395fc53401d8efd1eb77bb1d718~tplv-k3u1fbpfcp-watermark.image" alt="请添加图片描述" loading="lazy" referrerpolicy="no-referrer">在上面的图片中可以看出，我们需要对于不同区块的网格进行不同的信息展示，这就需要我们在网格创建时传入对应的处理逻辑。具体的代码结构为：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">using</span> System.Collections;
<span class="hljs-keyword">using</span> System.Collections.Generic;
<span class="hljs-keyword">using</span> UnityEngine;
<span class="hljs-keyword">using</span> System;


<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title">GridMeshCreate</span> : <span class="hljs-title">MonoBehaviour</span>
&#123;
    [<span class="hljs-meta">Serializable</span>]
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title">MeshRange</span>
    &#123;
        <span class="hljs-keyword">public</span> <span class="hljs-built_in">int</span> widght;
        <span class="hljs-keyword">public</span> <span class="hljs-built_in">int</span> height;
    &#125;
    <span class="hljs-comment">//网格的宽高范围</span>
    <span class="hljs-keyword">public</span> MeshRange meshRange;
    <span class="hljs-comment">//生成网格起始点</span>
    <span class="hljs-keyword">public</span> Vector3 startPos;
    <span class="hljs-comment">//网格生成的父物体</span>
    <span class="hljs-keyword">public</span> Transform parentTran;
    <span class="hljs-comment">//模板预制体</span>
    <span class="hljs-keyword">public</span> GameObject gridPre;
    
    <span class="hljs-keyword">private</span> Grid[,] m_grids;
    <span class="hljs-keyword">public</span> Grid[,] MeshGridData
    &#123;
        <span class="hljs-keyword">get</span>
        &#123;
            <span class="hljs-keyword">return</span> m_grids;
        &#125;
    &#125;
    <span class="hljs-comment">//注册模板事件</span>
    <span class="hljs-keyword">public</span> Action<Grid> gridEvent;

    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> 基于挂载组件的初始数据创建网格</span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">CreateMesh</span>(<span class="hljs-params"></span>)</span>
    &#123;
        <span class="hljs-keyword">if</span> (meshRange.widght == <span class="hljs-number">0</span> || meshRange.height == <span class="hljs-number">0</span>)
        &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        ClearMesh();
        m_grids = <span class="hljs-keyword">new</span> Grid[meshRange.widght, meshRange.height];
        <span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> i = <span class="hljs-number">0</span>; i < meshRange.widght; i++)
        &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> j = <span class="hljs-number">0</span>; j < meshRange.height; j++)
            &#123;
                CreateGrid(i, j);

            &#125;
        &#125;
    &#125;

    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> 重载，基于传入宽高数据来创建网格</span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><param name="height"></span><span class="hljs-doctag"></param></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><param name="widght"></span><span class="hljs-doctag"></param></span></span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">CreateMesh</span>(<span class="hljs-params"><span class="hljs-built_in">int</span> height,<span class="hljs-built_in">int</span> widght</span>)</span>
    &#123;
        <span class="hljs-keyword">if</span> (widght == <span class="hljs-number">0</span> || height == <span class="hljs-number">0</span>)
        &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        ClearMesh();
        m_grids = <span class="hljs-keyword">new</span> Grid[widght, height];
        <span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> i = <span class="hljs-number">0</span>; i < widght; i++)
        &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> j = <span class="hljs-number">0</span>; j < height; j++)
            &#123;
                CreateGrid(i, j);
            &#125;
        &#125;
    &#125;

    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> 根据位置创建一个基本的Grid物体</span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><param name="row"></span>x轴坐标<span class="hljs-doctag"></param></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><param name="column"></span>y轴坐标<span class="hljs-doctag"></param></span></span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">CreateGrid</span>(<span class="hljs-params"><span class="hljs-built_in">int</span> row,<span class="hljs-built_in">int</span> column</span>)</span>
    &#123;
        GameObject go = GameObject.Instantiate(gridPre, parentTran);
        Grid grid = go.GetComponent<Grid>();

        <span class="hljs-built_in">float</span> posX = startPos.x + grid.gridWidght * row;
        <span class="hljs-built_in">float</span> posZ = startPos.z + grid.girdHeight * column;
        go.transform.position = <span class="hljs-keyword">new</span> Vector3(posX, startPos.y, posZ);
        m_grids[row, column] = grid;
        gridEvent?.Invoke(grid);
    &#125;

    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> 删除网格地图，并清除缓存数据</span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">ClearMesh</span>(<span class="hljs-params"></span>)</span>
    &#123;
        <span class="hljs-keyword">if</span> (m_grids == <span class="hljs-literal">null</span> || m_grids.Length == <span class="hljs-number">0</span>)
        &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-keyword">foreach</span> (Grid grid <span class="hljs-keyword">in</span> m_grids)
        &#123;
            <span class="hljs-keyword">if</span> (grid.gameObject != <span class="hljs-literal">null</span>)
            &#123;
                Destroy(grid.gameObject);
            &#125;
        &#125;
        Array.Clear(m_grids, <span class="hljs-number">0</span>, m_grids.Length);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于上面的脚本，有下面的两个关键点：</p>
<ul>
<li>创建网格</li>
<li>对外暴露处理<code>Grid</code>逻辑的方法</li>
</ul>
<p>关于网格的创建，在脚本中，我们写了一个重载的方法<code>public void CreateMesh(int height,int widght)</code>，传入了网格宽和高，来方便通过后期通过脚本灵活的修改网格的宽和高（注意这里的宽和高指的是<code>x</code>轴与<code>y</code>轴格子的个数）</p>
<p>而对于<code>Grid</code>逻辑对外暴露的实现，是利用在创建预制体时，为其添加一个委托事件。这样就可以在我们其他脚本创建时写入逻辑方法，而不需要对于这个封装好的网格地图创建类进行修改，而关于委托的一些知识，可以查看我之前的文章：</p>
<blockquote>
<p>关于委托的文章：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fxinzhilinger%2Farticle%2Fdetails%2F116834955%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/xinzhilinger/article/details/116834955?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">C# 委托基础与入门</a></li>
</ul>
</blockquote>
<h4 data-id="heading-3">3，地图生成案例</h4>
<p>在我们封装好网格创建的脚本后，就可以通过该脚本来做一个简单的网格地图来演示其用法</p>
<p>创建脚本命名为<code>MainRun</code> ，并进行编辑：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">using</span> System.Collections;
<span class="hljs-keyword">using</span> System.Collections.Generic;
<span class="hljs-keyword">using</span> UnityEngine;

<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title">MainRun</span> : <span class="hljs-title">MonoBehaviour</span>
&#123;
    <span class="hljs-comment">//获取网格创建脚本</span>
    <span class="hljs-keyword">public</span> GridMeshCreate gridMeshCreate;
    <span class="hljs-comment">//控制网格元素grid是障碍的概率</span>
    [<span class="hljs-meta">Range(0,1)</span>]
    <span class="hljs-keyword">public</span> <span class="hljs-built_in">float</span> probability;

    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">Update</span>(<span class="hljs-params"></span>)</span>
    &#123;
        <span class="hljs-keyword">if</span> (Input.GetKeyDown(KeyCode.Space))
        &#123;
            Run();
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">Run</span>(<span class="hljs-params"></span>)</span>
    &#123;
        
        gridMeshCreate.gridEvent = GridEvent;
        gridMeshCreate.CreateMesh();
    &#125;

    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> 创建grid时执行的方法，通过委托传入</span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><param name="grid"></span><span class="hljs-doctag"></param></span></span>
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">GridEvent</span>(<span class="hljs-params">Grid grid</span>)</span>
    &#123;
        <span class="hljs-comment">//概率随机决定该元素是否为障碍</span>
        <span class="hljs-built_in">float</span> f = Random.Range(<span class="hljs-number">0</span>, <span class="hljs-number">1.0f</span>);
        Debug.Log(f.ToString());
        grid.color = f <= probability ? Color.red : Color.white;
        grid.isHinder = f <= probability;
        <span class="hljs-comment">//模板元素点击事件</span>
        grid.OnClick = () => &#123;
            <span class="hljs-keyword">if</span> (!grid.isHinder)
                grid.color = Color.blue;
        &#125;;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，在<code>Run</code>方法中是对于我们网格创建框架的一个调用，而在<code>GridEvent(Grid grid)</code>中我们就可以写入我们的逻辑，并通过修改<code>Grid</code>脚本中的代码来辅助完成我们需要的效果，比如本案例中在<code>Grid</code>写入了一个点击事件，就可以在创建时通过委托定义该事件。</p>
<blockquote>
<p><strong>注意:</strong></p>
<ul>
<li>在脚本里面用到了<code>Random.Range(0, 1.0f)</code>来生成一个概率,注意不要写成<code>Random.Range(0, 1)</code>,因为这样输出的结果只能为整数，即只能输出零</li>
</ul>
</blockquote>
<p>在编写完成脚本后，就可以将<code>GridMeshCreate</code>脚本挂载到场景中的物体上，并根据注释进行相关的赋值。如图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25166c273f33468f8c2b43eb220e7450~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>完成脚本挂载后点击运行，进入游戏后，点击空格键就会创建一张地图，在地图中会有随机的障碍物，以红色来标识障碍物，不可被点击，而白色区域点击后颜色变为蓝色，具体效果如图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75664c8fea154939b531a6aa01421b79~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">总结</h3>
<p>这里只是介绍了一个简单的案例，如果你觉得有用的话，可以尝试基于<code>GridMeshCreate</code>脚本创建自己的网格地图生成方法，来做出自己想要的效果！</p></div>  
</div>
            