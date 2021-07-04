
---
title: 'CocosCreator实战项目1：忍者跳跳跳'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e44ce5eec5e740c9b43ac4318f86a07f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 22:04:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e44ce5eec5e740c9b43ac4318f86a07f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><hr color="#000000" size="1"">
<h2 data-id="heading-0">摘要</h2>
<p>CocosCreator模仿4399忍者跳跳跳小游戏 原版游戏链接：
<a href="http://h.4399.com/play/159472.htm" target="_blank" rel="nofollow noopener noreferrer">忍者跳跳跳</a></p>
<h2 data-id="heading-1">正文</h2>
<h4 data-id="heading-2">使用版本</h4>
<p>CocosCreator2.4.5版本</p>
<h4 data-id="heading-3">游戏截图</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e44ce5eec5e740c9b43ac4318f86a07f~tplv-k3u1fbpfcp-zoom-1.image" alt="忍者跳跳跳" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">游戏资源面板</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da0546b923ef4598839f50621ba3bb5f~tplv-k3u1fbpfcp-zoom-1.image" alt="游戏资源面板" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">脚本关系</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/698ef3d0fdcf4d969ae985d6e1aff99e~tplv-k3u1fbpfcp-zoom-1.image" alt="脚本关系" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">代码部分</h4>
<ol>
<li>util.ts：负责初始化数据和公共方法</li>
</ol>
<pre><code class="copyable">export class util&#123;

    public static readonly maxY = -500      //柱子最高点
    public static readonly minY = -750      //柱子最低点
    public static readonly maxX = 400       //柱子平面最宽点
    public static readonly minX = 250       //柱子平面最窄点
    public static readonly defaultPos = new cc.Vec2(-250,-500)      //柱子默认初始坐标
    public static readonly moveSpeed = 350  //柱子移动速度

    //麒麟子版适配分辨率
        public static resize() &#123;
        var cvs = cc.find('Canvas').getComponent(cc.Canvas);
        //保存原始设计分辨率，供屏幕大小变化时使用
        var dr = cvs.designResolution;
        var s = cc.view.getFrameSize();
        var rw = s.width;
        var rh = s.height;
        var finalW = rw;
        var finalH = rh;
 
        if((rw/rh) > (dr.width / dr.height))&#123;
            //!#zh: 是否优先将设计分辨率高度撑满视图高度。 */
            //cvs.fitHeight = true;
            
            //如果更长，则用定高
            finalH = dr.height;
            finalW = finalH * rw/rh;
        &#125;
        else&#123;
            /*!#zh: 是否优先将设计分辨率宽度撑满视图宽度。 */
            //cvs.fitWidth = true;
            //如果更短，则用定宽
            finalW = dr.width;
            finalH = rh/rw * finalW;
        &#125;
        cvs.designResolution = cc.size(finalW, finalH);
        cvs.node.width = finalW;
        cvs.node.height = finalH;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>gameManager.ts:挂载在游戏全局，实现游戏的初始化</li>
</ol>
<pre><code class="copyable">onLoad () &#123;
        util.resize();
        cc.director.getCollisionManager().enabled = true;
        this.startPanel.init(this);
        this.bgManager.init(this);
        this.uiManager.init(this);
        
    &#125;

    startGame()&#123;
        if(this.isStart)&#123;
            this.uiManager.initScene()
        &#125;
    &#125;

    failGame()&#123;
        this.failPanel.init()
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>uiManager.ts:负责游戏界面的初始化以及游戏逻辑,具体代码就不贴了，有兴趣就可以到gitee下载后看下代码</li>
</ol>
<pre><code class="copyable"> //初始化界面
    initScene()&#123;
        this.lastPillarPos = util.defaultPos
        this.isCreatePillarState = true
        let node = cc.instantiate(this.pillarPre)
        node.x = -450
        node.y = -500
        node.parent = this.uiWrapper
        this.initTween(this.ninja)
        this.initTween(node)
        node.getComponent('pillar').init(this)
        this.ninja.getComponent('ninja').init(this)
        this.initPillarPool()
        this.node.on('touchstart',this.touchStart,this)
        this.node.on('touchend',this.touchEnd,this)
        this.node.on('touchcanel',this.touchEnd,this)
    &#125;
      // 创建柱子
    private createPillar()&#123;
        if(this.lastPillarPos.x > cc.winSize.width/2)&#123;
            this.isCreatePillarState = false
            return
        &#125;
        let node:cc.Node = null;
        if(this.pillarPool.size()>0)&#123;
            node = this.pillarPool.get()
        &#125;else&#123;
            node = cc.instantiate(this.pillarPre)
        &#125;
        node.y = Math.random()*(util.maxY - util.minY) + util.minY
        node.x = this.lastPillarPos.x + Math.random()*(util.maxX - util.minX) + util.minX
        node.parent = this.uiWrapper
        node.getComponent('pillar').init(this)
        this.lastPillarPos = new cc.Vec2(node.x,node.y)
    &#125;
 。。。。。。。。。。。。。。。。。etc。。。。。。。。。。。。。。。。。。。。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.startPanel.ts: 游戏开始面板，点击开始按钮进入游戏</p>
<pre><code class="copyable">  init(game:gameManager)&#123;
        this.game = game
    &#125;
    onLoad () &#123;
        this.startBtn.on('touchstart',this.touchStart,this)
    &#125;

    private touchStart()&#123;
        cc.tween(this.startBtn).to(0.1,&#123;scale:0.9&#125;).to(0.1,&#123;scale:1&#125;).call(()=>&#123;
            this.node.active = false
            this.game.isStart = true
            this.game.startGame()
        &#125;).start()
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.failPanel.ts:游戏失败面板，设置显示后初始化数据和面板</p>
<pre><code class="copyable"> // 初始化失败界面
   init()&#123;
       this.node.active = true
       let curScoreText = cc.sys.localStorage.getItem('curScore')
       this.curScore.string = curScoreText
       this.bestScore.string = cc.sys.localStorage.getItem('bestScore')
       this.restartBtn.on('touchstart',this.restartTouch,this)
       this.strutBtn.on('touchstart',this.strutTouch,this)
        if(+curScoreText>5 && +curScoreText<10)&#123;
            cc.resources.load('6408',cc.SpriteFrame,(err,res)=>&#123;
            this.Level.getComponent(cc.Sprite).spriteFrame = res
        &#125;)
        &#125;
        else if(+curScoreText>=10)&#123;
             cc.resources.load('64014',cc.SpriteFrame,(err,res)=>&#123;
            this.Level.getComponent(cc.Sprite).spriteFrame = res
        &#125;)
        &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">结语</h2>
<p>游戏总体难度不大，代码行数只有两百行差不多，感兴趣的小伙伴可以到gitee上下载代码研究一下，函数之间都做了注释，容易看懂，顺便点个赞哈！！
<a href="https://gitee.com/mzt17/ninja-jump-jump" target="_blank" rel="nofollow noopener noreferrer">gitee链接</a></p></div>  
</div>
            