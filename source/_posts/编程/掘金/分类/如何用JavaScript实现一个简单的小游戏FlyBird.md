
---
title: '如何用JavaScript实现一个简单的小游戏FlyBird'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d1b6c4319144898a7c65d367e4b7b13~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 24 Apr 2021 22:19:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d1b6c4319144898a7c65d367e4b7b13~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>【前言】</strong></p>
<p>作为一个前端初学者，秉承着不想当老师的学生不是好学生的思想。利用空余时间将<strong>FlyBird</strong>这个曾经让人想砸手机的小游戏梳理了一下，整理成了一个小教程让大家来指点指点。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d1b6c4319144898a7c65d367e4b7b13~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>【首页图】</strong></p>
<ol>
<li>
<p>首先我们对首页图进行分析它的构成，我们可以从中发现以下元素①背景②start按钮③大标题④小鸟⑤草地（滚动的）等五大板块。在这我们通过图片来实现，虽说用代码也能够达到这种效果，但工程量太大，我们在这不推荐。</p>
</li>
<li>
<p>首先先建立基本的html页面（快捷键！＋tab可以快速建立基础页面）我们根据所看到的游戏封面先建立一个盒子#wrapBg用于存放背景图，设置好宽高。</p>
<pre><code class="copyable">     > #wrapBg
     > &#123;
     >     height: 480px;
     >     width:343px;
     >     margin:0 auto;
     >     position: relative;
     >     top:100px;
     >     background-image: url(../img/bg.jpg);
     > &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>其中margin 0：auto 将图片在x轴上水平居中，此时对position属性用relative，为下面的其它图片定位作父元素使用，后面会提到。</p>
<ol start="3">
<li>
<p>在背景图中加入大标题 并对其定位，同时在其中放入小鸟图片</p>
<pre><code class="copyable">     >  <!--标题-->
     >         <div id="headTitle">
     >             <img src="img/bird0.png" alt="" id="headBird">
     >         </div>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在css中设置标题的位置，在这用absolute定位，父容器为#wrapBg盒子，则相对于父容器来定位，以此来确定标题的位置</p>
<pre><code class="copyable">     > #headTitle
     > &#123;
     >     width: 236px;
     >     height:77px;
     >     background-image: url(../img/head.jpg);
     >     position:absolute;
     >     left:53px;
     >     top:100px;
     > &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>/<em>相对于父容器进行定位。谁有relative谁就是父容器，身上有absolute也行，没有父容器就以body作为榜样来进行定位</em>/</p>
<ol start="5">
<li>
<p>由于小鸟在前面写入了headTitle盒子里，所以对其进行定位在这里我们也可以用position位置来确定小鸟的位置，但在此我们使用float浮动来将其放于盒子的最右边，浮动就是脱离文档流（文档流可以理解为类似js的从上到下运行，按顺序运行），通过设置float让它去最左边或者右边，类似从排队中提出某一人让他去任意地方，我是这样理解的。</p>
</li>
<li>
<p>按部就班将按钮位置给定位好</p>
<pre><code class="copyable">     > #startBtn&#123;
     >     width:85px;
     >     height: 29px;
     >     background-image: url(../img/start.jpg);
     >     position: absolute;
     >     left:129px;
     >     top:250px;
     > &#125;/*按钮自己天生有自带外边距，下面可以处理掉*/
     > 
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p><strong>【实现运动】</strong>
下一阶段就是让标题，鸟，翅膀还有草地进行运动</p>
<p><strong>标题运动</strong></p>
<p>首先我们思考，如何让标题进行上下运动
在这里我们首先想到通过变换标题位置的方式来对其进行运动，采取位置上下变换的方式来实现运动效果，在这我们使其上下移动3像素来进行来回运动。
首先我们要对标题盒子中的图片进行运动，在这里我们通过id这个属性来获取到当前的dom结构
我们定义jsHeadTitle来获取它的dom结构</p>
<blockquote>
<p>var jsHeadTitle = document.getElementById('headTitle');</p>
</blockquote>
<p>再定义上下移动的幅度，在此我们设置为3像素</p>
<blockquote>
<p>var Y = 3//上下摆动3像素  标题摆动的幅度</p>
</blockquote>
<p>我们建立一个函数来实现这个效果</p>
<pre><code class="copyable">`           function headWave() &#123;
            Y = Y * -1;
            jsHeadTitle.style.top = jsHeadTitle.offsetTop + Y + 'px'

         <!--------------------------分割线-------------------------!>
            //bird交替更换图片  思考怎么让鸟翅膀来回变换 应用数组下标
            jsHeadBird.src = imgArr[index++]
            if (index == 2) &#123;
                index = 0;  //一旦index变成了2 就马上赋值为0
            &#125;`
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>此函数前半段通过改变标题盒子离父类盒子的上部距离来改变其定位</strong>，我们在这里用offsetTop来获取
headTitle中top的数值，我们采取将Y值设置为相反数的方式，来实现标题的上下运动。</p>
<p><strong>鸟的翅膀运动</strong></p>
<p>此函数的下半部分则是让鸟的翅膀来回变动，我们这里采取将翅膀图片不断变换来实现效果。</p>
<ol>
<li>我们先定义一个数组用于存放鸟翅膀的图片</li>
</ol>
<p><code>var imgArr = ['img/bird0.png', 'img/bird1.png']</code></p>
<ol start="2">
<li>通过id来获取到当前的dom结构</li>
</ol>
<p><code> var jsHeadBird = document.getElementById('headBird');</code></p>
<ol start="3">
<li>
<p>用下列代码实现，当index即数组下标等于2时，对其赋值为0，之后不断重复，以此来达到两张图片不断来回切换的效果</p>
<pre><code class="copyable"> `
 jsHeadBird.src = imgArr[index++]
 if (index == 2) &#123;
   index = 0;  //一旦index变成了2 就马上赋值为0
                  &#125;
 var headWaveTimer= setInterval(headWave, 200)`
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>在这里使用一个定时器来实现函数的定时运行</p>
<p><strong>草地滚动</strong></p>
<p>我们思考如何让草地产生滚动效果？让草地无限长么？那显然咱们的电脑hold不住哈，大致思路是用两张同样的草地图片在y轴固定的位置来进行来回运动。</p>
<p>代码实现如下，先在html中</p>
<p><code> <div id="grassLand1"></div>  <div id="grassLand2"></div> </code></p>
<p>再回到css中对草地1和草地2对齐分别进行<strong>设置属性</strong></p>
<pre><code class="copyable">> #grassLand1,#grassLand2
> &#123;
>     width:343px;
>     height: 14px;
>     background-image: url(../img/banner.jpg);
>     position: absolute;
>     top:423px;
> &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>单独拿出来设置left属性 是因为两个草地要来回滚动 所以一个没有边距，一个刚好要在外面，所以left设置为草地的宽度</p>
<pre><code class="copyable">>   #grassLand1
> &#123;
>     left:0;
> &#125;
> #grassLand2
> &#123;
>     left:343px;
> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>草地1的left为0的原因是，#grassLand1刚好处在wrapBg当中，另一个设置距离刚好为343px，即wrapBg盒子的宽度，则它所处的位置刚好位于盒子的右部，为了使其溢出的图片不被显示，我们在这里用这行代码</p>
<p><code> overflow: hidden;/*用于隐藏超出容器的草地*/</code></p>
<p>来隐藏溢出的草地</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb9b91e8537e4590a6068fb768ece71c~tplv-k3u1fbpfcp-watermark.image" alt="QQ图片20210420225014.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（此时是溢出的草地）</p>
<p>同样的，我们通过id来获取当前的dom结构</p>
<blockquote>
<p> var jsGrassLand1 = document.getElementById('grassLand1')
 var jsGrassLand2 = document.getElementById('grassLand2')</p>
</blockquote>
<p>然后建立landRun函数来实现效果</p>
<pre><code class="copyable">> 
> function landRun() &#123;
>             //思考如何来回动 用来判断 看草地离左边的距离
>             if (jsGrassLand1.offsetLeft <= -343) &#123;
>                 jsGrassLand1.style.left = '343px'
>             &#125;
>             if (jsGrassLand2.offsetLeft <= -343) &#123;
>                 jsGrassLand2.style.left = '343px'
>             &#125;
>             jsGrassLand1.style.left = jsGrassLand1.offsetLeft - 3 + 'px'
>             jsGrassLand2.style.left = jsGrassLand2.offsetLeft - 3 + 'px'
>         &#125;
>         setInterval(landRun, 30)同样用计时器来让函数运行，以实现效果
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中两个if语句是实现草地来回滚动的关键，我们通过获取其left值后，判断其大小是否＜=-343px，根据相对位置可知，这个位置是草地刚好位于wrapBg的左边，当判断它完全滚完后，对其的left进行重新赋值放于最右边</p>
<p>此时 游戏的基本页面已经制作完成，那我们要进行一个完整的游戏，点击开始按钮后，原来的开始页面肯定得被游戏页面所取代才行</p>
<p>首先同样的，我们先拿到它</p>
<blockquote>
<p>var jsStartBtn=document.getElementById('startBtn')</p>
</blockquote>
<p>接着创建一个函数</p>
<pre><code class="copyable">`        jsStartBtn.onclick=function()
        &#123;
            jsHeadTitle.style.display='none'//css属性都要加一个style，用了none则这个容器就会消失
            jsStartBtn.style.display='none'
            //除了让上下抖动消失外，再干一个操作
            clearInterval(headWaveTimer)
            //插入小鸟到页面上
            bird.showBird(jsWrapBg)
        &#125;
`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数的作用是：
在按动按钮得时候，画面中的按钮键和标题全部消失，与此同时，我们要让新的画面出现。
在这里我们建立一个bird对象来实现</p>
<pre><code class="copyable">> 
> var bird=&#123;
>     flyTime:null,//键值对，key：value  此处留作小鸟飞翔的定时器;
>     wingTimer:null,//小鸟摆动的定时器
> 
>     div:document.createElement('div'),//此时代表它就是一个div容器了
>     showBird:function(parentobj)
>     &#123;
>         this.div.style.width='40px'//给上面那个容器宽度设置为40px
>         this.div.style.height='28px'
>         this.div.style.background='#000'
>         parentobj.appendChild(this.div)//父容器添加一个孩子div
>     &#125;//后面调用它时，页面上就会出现一只小鸟
> &#125;
> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们需要一只鸟，在按动按钮的时候，凭空出现，会自由下落，而且翅膀还会进行扇动
在这里我们定义一个bird</p>
<pre><code class="copyable">> var bird = &#123;
>   flyTime: null, // 小鸟飞翔的定时器
>   wingTimer: null, // 小鸟翅膀摆动的定时器
>   div: document.createElement('div'),
>   showBird: function(parentObj) &#123;
>     this.div.style.width = '40px'
>     this.div.style.height = '28px'
>     this.div.style.backgroundImage = 'url(img/bird0.png)'
>     this.div.style.backgroundRepeat = 'no-repeat'
>     this.div.style.position = 'absolute'
>     this.div.style.left = '50px'
>     this.div.style.top = '200px'
>     this.div.style.zIndex = '1'
>     parentObj.appendChild(this.div)
>   &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置好鸟的宽高后，
默认情况下当图片没有盒子大时， 图片会在盒子的水平或者垂直方向平铺。在本游戏中我们要的只是一只鸟，所以我们在这对bird0.png设置定位与不平铺
>  this.div.style.backgroundRepeat = 'no-repeat'
>     this.div.style.position = 'absolute'
>     this.div.style.left = '50px'
>     this.div.style.top = '200px'</p>
<p>同时用z-index属性设置堆叠顺序，将bird的z-index设为正值，将其置于首位，在这大家可以了解下7阶层叠水平</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f559f2824da748e69eeabdcc3c722185~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体内容自行了解，在此不作赘述。
在设置好bird0后，我们思考，这个游戏需要什么，在画面中我们可以得知小鸟在不断前进的过程中在柱子之间上下飞行，但显然如果操控小鸟在上下飞行的同时还要前进的话，用代码来实现无疑是复杂的，所以我们将其分为两部分。一部分是操控鸟的上下运动，另一部分操纵柱子的运动即可实现相对运动的效果。
在此，我们先对鸟的初速度定为0</p>
<p><code>fallSpeed: 0, // 小鸟下落的速度</code></p>
<p>接着写控制小鸟下落的函数</p>
<pre><code class="copyable">> flyBird: function() &#123; // 控制小鸟下落的函数
>     bird.flyTime = setInterval(fly, 60)
>     function fly() &#123;
>       bird.div.style.top = bird.div.offsetTop + bird.fallSpeed++ + 'px'
>       if (bird.div.offsetTop >= 395) &#123; // 掉到地面，清除定时器
>         bird.fallSpeed = 0
>         clearInterval(bird.flyTime)
>         clearInterval(bird.wingTimer)
>       &#125;
>       // 不让小鸟飞出界
>       if (bird.div.offsetTop < 0) &#123;
>         bird.div.style.top = '0px'
>         bird.fallSpeed = 2
>       &#125;
>       if (bird.fallSpeed > 12) &#123;
>         bird.fallSpeed = 12
>       &#125;//设定最大速度
>     &#125;
>   &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们写好了小鸟下落的函数，里面针对小鸟触地和小鸟飞出上边界两种情况分别用代码进行了设置，其中当小鸟触及上边界时，自行设置了小鸟当时的速度。
再写出控制小鸟向上飞行的函数，我们用通过在按钮点击的同时对其bird.fallSpee设置为-8的方式来控制小鸟的向上飞行，具体代码如下：</p>
<pre><code class="copyable">         ` bird.showBird(jsWrapBg)
            bird.flyBird()
            bird.wingWave()
            jsWrapBg.onclick=function()&#123;
            bird.fallSpeed=-8
                &#125;`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们此时虽然已经可以控制小鸟的上升和下落，但是我们会发现，此时小鸟的翅膀和头部方向并不会扇动和改变，于是我们采用上文封面中小鸟翅膀扇动的方法：</p>
<pre><code class="copyable">` wingWave: function () &#123;//控制小鸟扇动翅膀
        var up = ['url(img/up_bird0.png)', 'url(img/up_bird1.png)']
        var down = ['url(img/down_bird0.png)', 'url(img/down_bird1.png)']
        bird.wingTimer = setInterval(wing, 120)
        var i = 0,j=0
        function wing() &#123;
           if(bird.fallSpeed>0)&#123;
            bird.div.style.backgroundImage = down[i++]
            if (i == 2) &#123; i = 0 &#125;
           &#125;
            if (bird.fallSpeed < 0) &#123;
             bird.div.style.backgroundImage = up[j++]
             if (j == 2) &#123; j = 0&#125; 
          &#125;

        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>html中的代码实现</p>
<pre><code class="copyable">     var jsStartBtn = document.getElementById('startBtn')
     jsStartBtn.onclick = function() &#123;
      jsHeadTitle.style.display = 'none'
      jsStartBtn.style.display = 'none'
      clearInterval(headWaveTimer)
      // 插入小鸟到页面中
      bird.showBird(jsWrapBg)
      bird.flyBird()
      bird.wingWave()
      jsWrapBg.onclick = function() &#123;
        bird.fallSpeed = -8//用于设置点击鼠标时，小鸟上升的效果
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>做完上述的几步之后，我们小鸟的翅膀和头部就可以随着上下的飞动而发生改变。接下来就是为游戏设置管道了，为了游戏的趣味性我们对管道的长度设置随机。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfd5aaf6a1ea4b4abdd2e47efa18d6ed~tplv-k3u1fbpfcp-watermark.image" alt="QQ图片20210425140455.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">    var baseObj=&#123;
        randomNum:function(min,max)&#123;
            return Math.random()*(max-min+1)+min //设置随机数
            return parseInt(Math.random()*(max-min+1)+min)//对它进行取整
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来让函数拿到随机数对上管道与下管道的长度和间隙进行设置</p>
<pre><code class="copyable">function Block()&#123;
    this.upDivWrap=null
    this.downDivWrap=null
    this.downHeight=baseObj.randomNum(0,150)//设置0到150之间的高度
    this.gapHeight=baseObj.randomNum(150,160)//设置管道间隙
    this.upHeight=312-this.downHeight-this.gapHeight//上方管道长度
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我们声明一个方法用于生成管道</p>
<pre><code class="copyable">this.createDiv=function(url,height,positionType)&#123;
        var newDiv=document.createElement('div')
        newDiv.style.width='62px'
        newDiv.style.height=height
        newDiv.style.position=positionType
        newDiv.style.left=left
        newDiv.style,top=top
        newDiv.style.backgroundImage=url
        return newDiv
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后写入值，生成管道</p>
<pre><code class="copyable">this.creatBlock=function()&#123;
        var upDiv1=this.createDiv('url(img/up_mod.png',this.upHeight+'px')
        var upDiv2=this.createDiv('url(img/up_pipe.png','60px')
        this.upDivWrap=this.createDiv(null,null,'absolute','450px')
        this.upDivWrap.appendChild(upDiv1)
        this.upDivWrap.appendChild(upDiv2)
        jsWrapBg.appendChild(this.upDivWrap)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着就是在html中调用他们。使其实例化，生成管道。</p>
<pre><code class="copyable"> var b = new Block() // 实例化
      b.createBlock()
    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着对管道的运动进行设置</p>
<pre><code class="copyable">this.moveBlock = function () &#123;
    this.upDivWrap.style.left = this.upDivWrap.offsetLeft - 3 + 'px'
    this.downDivWrap.style.left = this.downDivWrap.offsetLeft - 3 + 'px'
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着咱们在js中写入判断相撞的代码</p>
<pre><code class="copyable">// 判断两个矩形是否发生碰撞
  rectangleCrashExamine: function (obj1, obj2) &#123;
    var obj1Left = obj1.offsetLeft
    var obj1Width = obj1.offsetLeft + obj1.offsetWidth
    var obj1Top = obj1.offsetTop
    var obj1Height = obj1.offsetTop + obj1.offsetHeight

    var obj2Left = obj2.offsetLeft
    var obj2Width = obj2.offsetLeft + obj2.offsetWidth
    var obj2Top = obj2.offsetTop
    var obj2Height = obj2.offsetTop + obj2.offsetHeight

    if (!(obj1Left > obj2Width || obj1Width < obj2Left || obj1Top > obj2Height || obj1Height < obj2Top)) &#123;
      return true
    &#125;
    return false
  &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>写到这里大致就结束了，由于代码过长就不在这贴完整代码了，在这贴上链接，有需要的朋友可以自行下载学习
因为本人github这边暂时登不上上传不了，这里贴的是gitee的地址
<a href="https://gitee.com/little-fish-write-code/lesson_ss/tree/master/FlyBird" target="_blank" rel="nofollow noopener noreferrer">gitee.com/little-fish…</a></p></div>  
</div>
            