
---
title: '弹幕效果实现(canvas)，含弹幕重叠处理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3345c68a6eae4fe98ff3117c5ddf1a7b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 02:45:00 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3345c68a6eae4fe98ff3117c5ddf1a7b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一.知识准备</h1>
<h2 data-id="heading-1">1.动画</h2>
<p>动画——我们的眼睛具有“视觉暂留”的特性，当我们看到一幅画或一个物体后，在0.34秒内不会消失，当我们在0.34秒内切换画时，就会有一种流畅地动画效果，整个画面看起来像是在动的，所以小时候的小人书，快速翻动时就感觉整个画面像是动了起来，其实它们就是由一张张静态的图画快速切换形成的动画效果</p>
<p>帧——就是影像动画中最小单位的单幅影像画面。 一帧就是一副静止的画面
动画是由多个静止的话面构成的</p>
<p>帧率——就是在1秒钟时间里传输的图片的张数，也可以理解为图形处理器每秒钟能够刷新几次，通常用FPS（Frames Per Second）表示，我们在玩游戏的时候说的掉帧，就是因为帧率过低所造成的画面出现停滞</p>
<p>弹幕效果——我们的弹幕效果就是每一帧通过不断擦除canvas重新绘制canvas来达到滑动的目的</p>
<h2 data-id="heading-2">2.requestAnimationFrame</h2>
<p>requestAnimationFrame() 告诉浏览器——你希望执行一个动画，并且要求浏览器在下次重绘之前调用指定的回调函数更新动画，也就是说根据显示器的刷新频率来决定一秒内重绘的次数，一般显示器都是为60Hz 或 75Hz，也就是说一秒内会执行60或75次函数，我们将传入一个函数，不断的对canvas进行清空与绘制</p>
<p><strong>仅从动画角度对比requestAnimationFrame与setTimeout<br>
优点</strong></p>
<p>1.requestAnimationFrame紧跟着浏览器刷新率，不会出现过渡绘制(绘制速度太快，超过浏览器刷新率，出现丢帧)，或绘制速度太慢造成的卡顿，而setTimeout和setInterva都不太准确，一旦设置的时间不能和浏览器刷新时间保持一致，就容易出现过渡绘制与卡顿</p>
<p>2.如果页面不是激活状态下的话，动画会自动暂停，有效节省了CPU开销(我们在绘制弹幕时切换到其他页面弹幕会暂停，直到你切换回页面才会继续绘制)，而setTimeout会一直在后台运行</p>
<p><strong>缺点:</strong></p>
<p>1.兼容性比不上setTimeout和setInterva</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3345c68a6eae4fe98ff3117c5ddf1a7b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">3.canvas篇</h2>
<h3 data-id="heading-4">初始化canvas</h3>
<pre><code class="copyable">    //获取canvas对象
    this.canvas = document.getElementById(canvas)
    //获得 2d 上下文对象
    this.context = this.canvas.getContext("2d")
    //获取canvas容器的宽高，Canvas类似于位图，一般根据手机的屏幕倍数展示,将容器宽高乘以2以适配两倍屏，可自定义
    this.canvasHeight = canvasHeight * 2
    this.canvasWidth = canvasWidth * 2
    //设置canvas的宽高
    this.canvas.width = this.canvasWidth
    this.canvas.height = this.canvasHeight
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">canvas绘制文字</h3>
<pre><code class="copyable">//设置文字颜色
this.context.fillStyle = '#008B8B'
//设置文字字体字号
this.context.font = `20px STheiti, SimHei`
//绘制文字位置
this.context.fillText(绘制的文本,填充文本的起点横坐标(X轴), 填充文本的起点纵坐标(Y轴),文本占据的最大宽度)
例:this.context.fillText(`拿来把你`, 500, 400)
我们会通过不断修改X轴坐标达到弹幕滑动效果，也可对弹幕速度进行控制
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">canvas清除内容</h3>
<pre><code class="copyable">//清空canvas画布内容
this.context.clearRect(矩形起点的 x 轴坐标,矩形起点的 y 轴坐标, 矩形的宽度, 矩形的高度)
this.context.clearRect(0, 0, this.canvasWidth , this.canvasHeight)
例:this.context.clearRect(0, 0, 500, 400)
每一帧都会擦除整个屏幕重新绘制所有弹幕
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">canvas测量文字宽度</h3>
<p>通过measureText()函数我们可以测量文字的宽度</p>
<pre><code class="copyable">   let width = this.context.measureText(value).width
<span class="copy-code-btn">复制代码</span></code></pre>
<p>作用:我们会通过文字宽度做两件事情，1.判断文字是否完整展示在画面上了 2.判断文字是否已经完整滑动出画面</p>
<h1 data-id="heading-8">二.弹幕实现</h1>
<p>本例子用的是vue哦,在barrage.vue中引入barrage.js，实例化Barrage类，该类可以直接放在项目中使用，需要传入参数
barrageEffect.Barrage(canvas的ID,canvas容器的宽,canvas容器的高,弹幕行数,字体大小)</p>
<p>barrage.vue</p>
<pre><code class="copyable"><template>
  <div class="barrage">
    <img src="https://images.pexels.com/photos/2286895/pexels-photo-2286895.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500" alt="">
    
    <canvas id="myCanvas">
      
    </canvas>
  </div>
</template>
<script>
import barrageEffect from './barrage'
export default &#123;
  data () &#123;
    return &#123;
      imgUrl:'',
      canvasWidth:0,
      canvasHeight:0,
      context:null,
      mobile:0,
      barrage:null,
    &#125;
  &#125;,
  methods: &#123;
    init()&#123;
      const fontSize = 20
      const highwayAmount = 4
      this.barrage = new barrageEffect.Barrage('myCanvas',this.canvasWidth,this.canvasHeight,highwayAmount,fontSize)
        //可通过addTest方法不断添加弹幕
        this.barrage.addTest(['风景好美呀','绝了绝了','好想去','安排安排','醒醒醒醒，你没钱去'])
        setTimeout(()=>&#123;
          this.barrage.addTest(['年轻人','耗子尾子','耗耗反思','这是你该做的梦吗','醒醒醒醒，老实搬砖','再做梦别怪我捶你'])
        &#125;,500)
    &#125;,
    setCanvas()&#123;
      let canvasStyle = document.getElementById('myCanvas')
        this.canvasWidth = canvasStyle.offsetWidth
        this.canvasHeight =canvasStyle.offsetHeight
        this.init()
    &#125;
  &#125;,
  computed:&#123;
    
  &#125;,
  mounted()&#123;
    this.setCanvas()
  &#125;
&#125;;
</script>
<style lang="scss" scoped>
.barrage&#123;
  width: 100vw;
  height: 100vh;
  position: relative;
  #myCanvas&#123;
    position: absolute;
    z-index: 2;
    width: 565px;
    height: 377px;
    top: 0;
    left: 0;
  &#125;
  img&#123;
    width: 565px;
    height: 377px;
  &#125;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>barrage.js</p>
<pre><code class="copyable">class Barrage&#123;
    constructor(canvas,canvasWidth,canvasHeight,highwayAmount,fontSize)&#123;
        //获取canvas对象
        this.canvas = document.getElementById(canvas)
        //获得 2d 上下文对象
        this.context = this.canvas.getContext("2d")
        //获取canvas容器的宽高，Canvas类似于位图，一般根据手机的屏幕倍数展示,将容器宽高乘以2以适配两倍屏，可自定义
        this.canvasHeight = canvasHeight * 2
        this.canvasWidth = canvasWidth * 2
        //设置canvas的宽高
        this.canvas.width = this.canvasWidth
        this.canvas.height = this.canvasHeight
        //存储正在发送的弹幕
        this.barrageList = [];
        //存储待发送的弹幕
        this.textList = []
        //初始化字体大小
        this.fontSize = fontSize
        this.context.font = `$&#123;this.fontSize&#125;px STheiti, SimHei`
        this.highwayAmount = []
        //初始化弹幕的highwayAmount,将弹幕划分成类似一条条公路，防止弹幕在Y轴重叠，可根据实际情况调整数量
        this.initTop(highwayAmount)
        //是否绘画完成标志
        this.draw = false
    &#125;
    initTop(highwayAmount)&#123;
        //最多存在弹幕行数
        const maxHighwayAmount = parseInt(this.canvasHeight/(this.fontSize+20))
        //如果传入的行数大于最大行数，取最大行数
        maxHighwayAmount<highwayAmount ? highwayAmount = maxHighwayAmount : ''
        //highwayAmount弹幕行数
        for(let i =1;i<=highwayAmount;i++)&#123;
            this.highwayAmount.push(((this.fontSize+20)*i))
        &#125;
    &#125;
    drawBarrage()&#123;
        //清空canvas画布内容
        this.context.clearRect(0, 0, this.canvasWidth , this.canvasHeight)
        //提前清除无用的弹幕，保证绘制弹幕时所有弹幕都是存在于页面上的，如果边绘制弹幕边清除数据，因为数组下标的改变会引起弹幕闪烁
        for(let i=0;i<this.barrageList.length;i++)&#123;
            //当弹幕的left(距离canvas左边的位置)+width弹幕自身宽度<=0时，说明弹幕已出屏幕，从this.barrageList中剔除
            this.barrageList[i].left + this.barrageList[i].width <=0 ? this.barrageList.splice(i,1) : ''
        &#125;
        //绘制弹幕
        this.barrageList.forEach((val)=>&#123;
            //设置弹幕颜色
            this.context.fillStyle = val.color
            //绘制弹幕位置
            this.context.fillText(`$&#123;val.value&#125; `, val.left, val.top)
            //occupation为占用top标志，当弹幕的left(距离canvas左边的位置)+width弹幕自身宽度<屏幕宽度时，说明弹幕已完全展示于屏幕中，可以释放占用的top并插入新值，consumeText函数作用见下文
            val.occupation && val.left + val.width <= this.canvasWidth ? this.consumeText(val) : ''
            //控制弹幕速度
            val.left-=2
        &#125;)
        //this.barrageList为0，说明已无弹幕
        this.barrageList.length == 0 ? this.draw=false : requestAnimationFrame(this.drawBarrage.bind(this))
    &#125;
    consumeText(val)&#123;
        //将占用标志置为false，防止多次执行val.occupation && val.left + val.width <= this.canvasWidth ? this.consumeText(val) : ''
        val.occupation =false
        //释放top值，向this.highwayAmount返回占用的top值,延迟0.5s执行，防止弹幕粘黏
        setTimeout(()=>&#123;
            this.highwayAmount.push(val.top)
            //检查是否有待发送的弹幕，如果有，向this.barrageList插入新值
            if(this.textList.length!=0)&#123;
                this.barrageList.push(this.initTest(this.textList.splice(0,1)[0]))
            &#125;
        &#125;,500)
    &#125;
    addTest(textList)&#123;
        //判断是否处于绘制状态
        if(this.draw)&#123;
            //判断是否有空余的highwayAmount可以使用
            if(this.highwayAmount.length != 0)&#123;
                let barrageList = textList.splice(0,this.highwayAmount.length)
                for(const val of barrageList)&#123;
                    this.barrageList.push(this.initTest(val))
                &#125;
            &#125;
            this.textList.push(...textList)
        &#125;else&#123;
            this.textList.push(...textList)
            //将绘制状态置为true
            this.draw = true
            this.runBarrage()
        &#125;
    &#125;
    initTest(text)&#123;
        //初始化弹幕对象信息
        let value = text
        let color = ['#E0FFFF','#FFE1FF','#FFB5C5','#F0FFF0','#BFEFFF','#63B8FF','#FFFFFF']
        let barrageTest =&#123;
            value,//弹幕值
            top:this.highwayAmount.splice(0,1)[0],
            left:this.canvasWidth,//弹幕起点
            color:color[Math.floor(Math.random()*6)],//弹幕随机颜色
            offset:Math.ceil(Math.random()* 3),//弹幕速度
            width:Math.ceil(this.context.measureText(value).width),//获取该弹幕占用的宽度
            occupation:true,//占用top状态
        &#125;
        return barrageTest
    &#125;
    runBarrage()&#123;
        //根据弹幕top数初始化第一次展示的数据
        this.textList.splice(0,this.highwayAmount.length).forEach((val)=>&#123;
            this.barrageList.push(this.initTest(val))
        &#125;)
        //开始绘制
        this.drawBarrage()
    &#125;
&#125;

export default&#123;
    Barrage
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">三.类函数解析与弹幕重叠优化</h1>
<h2 data-id="heading-10">1.initTop(highwayAmount)函数(控制Y轴弹幕不重叠)</h2>
<p>接受一个参数(highwayAmount)，表示生成的弹幕行数，控制弹幕在Y轴上不重叠，将canvas的Y轴看成一条条公路，根据字体大小分配出每条公路的宽度坐标，最终根据highwayAmount参数，获取相应数量不重叠的公路Y轴坐标</p>
<p>计算最多存在的弹幕数
通过canvas的高度/文字大小可以得出最多的弹幕行数，为了让行数之间保持距离，多加了20px<code> parseInt(this.canvasHeight/(this.fontSize+20))</code></p>
<p>canvas绘制文字x,y坐标是按文字左下角计算，如果高度为0会出现如下情况</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50d17fd4c2df4b31954d7a9d96c467f8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以我们储存公路坐标时需要剔除掉0,所以i从1开始</p>
<pre><code class="copyable">    for(let i =1;i<=highwayAmount;i++)&#123;
        this.highwayAmount.push(((this.fontSize+20)*i))
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">2.initTest(text)函数</h2>
<p>生成一个个弹幕对象储存弹幕对象信息
top:this.highwayAmount.splice(0,1)[0],//返回一个top值，并将该top值从this.highwayAmount剔除，为什么要这么干呢，假设我们有1行弹幕，第一个弹幕没完全展示完成时该行不能输出弹幕，否则会导致弹幕在X轴上重叠，<br>
例：如下图
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32b6ef1f1a794178bc8bcdf3da45fd87~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
所以我们将值从this.highwayAmount剔除，防止被赋值给其他弹幕对象，如何判断弹幕已完全展示可插入其他弹幕呢，详见drawBarrage()函数<br>
occupation:true,//占用top状态，drawBarrage()需要用到</p>
<h2 data-id="heading-12">3.drawBarrage()函数</h2>
<p>根据this.highwayAmount数组获取弹幕展示行数，初始化第一批展示的数据，并调用this.drawBarrage()函数开始绘制</p>
<h2 data-id="heading-13">4.addTest(textList)函数</h2>
<p>它作为绘制弹幕的入口<br>
根据this.draw判断弹幕是否处于绘制状态，如果弹幕不处于绘制状态，将所有数据添加到this.textList中，并调用this.runBarrage()方法初始化弹幕数据进行绘制<br>
如果弹幕处于绘制状态检查是否有多余的top可以使用，如果有top可以使用，直接将数据添加至this.barrageList中进行绘制，其他数据添加至this.textList中等待绘制</p>
<h2 data-id="heading-14">5.drawBarrage()函数</h2>
<p>每一帧执行的函数，控制弹幕移动，添加，删除弹幕数据<br>
1.会通过this.context.clearRect(0, 0, this.canvasWidth , this.canvasHeight)清除画布重新绘制弹幕与弹幕位置<br>
2.根据弹幕距canvas的左边距离与自身宽度清除绘制完成的弹幕
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51a720bc225842a0805fcba6c3a1e893~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
3.根据每个弹幕对象绘制弹幕，并根据根据弹幕距canvas的左边距离与自身宽度判断是否已完整显示在了canvas中
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2edb71b464a4e3485d3d8087ae82323~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如果是，则调用consumeText(val)函数，将弹幕对象占用的top，释放到this.highwayAmount中，并查看this.textList是否有待发送弹幕，如果有，将其添加至this.barrageList中</p>
<h1 data-id="heading-15">三.结语</h1>
<p>首次发表文章，文中错误之处多多指正啊</p>
<h2 data-id="heading-16">效果展示</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dabd0c7eef884623bb37d5ee6dfc563c~tplv-k3u1fbpfcp-watermark.image" alt="tutieshi_320x180_9s.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            