
---
title: '仿百度验证码(vue+node)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5bef0482a374c0d8970184c649f103d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 08:11:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5bef0482a374c0d8970184c649f103d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1 为什么我们要使用验证码?</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5bef0482a374c0d8970184c649f103d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如果你是一个只想看干货的程序员，又不想听我说废话，这里请直接滑动到最后，获取代码。</p>
<blockquote>
<p>描述一个业务场景:</p>
<p>假设你想要浪费xxx公司的短信验证码，你会怎么做?</p>
<p>假设你就是这家公司的程序员，你该怎么保护公司呢?</p>
</blockquote>
<h3 data-id="heading-1">1.2 设想性攻防战</h3>
<h4 data-id="heading-2">第一回合</h4>
<p>攻击方: (模拟接口调用) <br>
使用postman工具，将发送短信的接口疯狂的调用。 <br></p>
<p>防守方: (运营商保护) <br>
作为后端团队，马上开启会议模式，思考如何防止呢?好，接口供应商的接口保护开启。设置一天内容同一个手机号，
只能请求10次，每个小时只能请求1次。 <br></p>
<hr>
<h4 data-id="heading-3">第二回合</h4>
<p>攻击方: (手机号足够多呢) <br>
发现接口调用失败，开启了异常状态，同一手机号被限制了。好，使用手机词典模式，只要我手机号足够多，肯定就可以不停的调用你，写了一个脚本模拟调用。 <br></p>
<p>防守方: (IP地址保护) <br>
通过接口日志发现，居然有一个人，每秒都在调用接口，然后发送之后，并没有任何用户行为操作?通过ip监控发现，居然是来自一个IP的攻击，马上开启保护模式，限制同一IP。 <br></p>
<hr>
<h4 data-id="heading-4">第三回合</h4>
<p>攻击方: <br>
突然发现电脑接口调用失败了，但是手机热点的调用却成功了。那就开启虚拟IP，接着开始调用。 <br></p>
<p>防守方: <br>
叫上前端，我们讨论一下，开启验证码。 <br></p>
<hr>
<h2 data-id="heading-5">2 验证码方案</h2>
<p>作为防守方，我们要明白一个任务，我要收集用户的同时，可能更加希望对方是一个人，而不是机器。那么如何确定对方是一个人呢?</p>
<h2 data-id="heading-6">3 文字验证码</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fd2979160b942d9aff1a82f4e5defda~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>随机的数字或者字母图片，这是最原始也是最简单的验证码</li>
<li>GIF格式的随机数字或者字母图片</li>
<li>随机数字+随机大写英文字母+随机干扰像素+随机位置BMP格式图片</li>
<li>随机英文字母+随机颜色+随机位置+随机长度的JPG格式图片，对字母进行大小写，位置，颜色，长度等进行随机显示</li>
</ol>
<p>(以上为间断性的方案...)</p>
<p>最后的结果大家，已经知道，不论是前端还是后端，都有相应的库。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6439901e4ab74f35bbb0298db27cc964~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们设计出了这样的方案。那么这样的方案好不好呢？
通过了多年，人们对于模糊的文字识别技术升级后，这样的验证码技术，安全系数就耍耍的减低。</p>
<h2 data-id="heading-7">4 问题验证码</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2622428807d14e0d90f51d2b740c7d14~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
将文字的验证码升级后，略带互动的形式，地理问题（如图），数学问题，常识问。然后你会发现，总有那么几个问题，真的是人也不一定答出来。</p>
<h2 data-id="heading-8">5 图片验证码</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15c2f4f8547543d8965f0afae0ae1dea~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
放上一些图片，让你找出下列的书、花、红绿灯。这是一个经典的验证码，最出名的就是现在12306采用的防刷票措施了，对于用户的来说，总有几个脸盲患者，和看走眼的时候。在保护了接口的同时，也烦躁了用户。</p>
<h2 data-id="heading-9">6 滑动验证码</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8d986b74e1440cf9afcac1cb03a6a0c~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>将图片拖到底部</li>
<li>将图片和缺口复合</li>
<li>图片上开启2个缺口</li>
</ol>
<p>对于用户的要求降低之后，用户的体验就大大升级。俗话说，用的人多了，就不是什么难点了。即使二代升级了2个缺口，利用puppeteer破解极验的滑动验证工具，也随之诞生。</p>
<h2 data-id="heading-10">7 百度验证码 (附代码)</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/856f6ad6000e4311925e0ce1d238a9f7~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这套方案，我有在py的破解方案中找到，你可以理解为，生成无数个模型找到相似的算法，进行破解图片。那么我们这时候，假设一个图片会有360个角度，我们要去掉本来不需要旋转的度数，比如340个角度，去掉旋转不多的角度，180个角度，对于破解来说，就是260张图片。那么假设我的图片库内，有1000张图片，你需要破解，则需要180000张图片来存储，而我可以选择，定期更新这些图片。</p>
<h3 data-id="heading-11">7.1 node 代码</h3>
<ol>
<li>图片肯定必须是后端生成的。=> 生成一张图片</li>
<li>不希望图片存储到服务器上(毕竟是临时图片) => base64就是比较好的方案=> sharp库</li>
<li>实际上最有意义的是90-270随机数(或许可以更多，没有具体测试)=> 取随机数</li>
<li>这里我们服务选择了koa</li>
</ol>
<blockquote>
<p>这里的随机数是存储，如果你想使用在项目中，需要存储到缓存，这里推荐redis。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> sharp = <span class="hljs-built_in">require</span>(<span class="hljs-string">'sharp'</span>)
<span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa'</span>);
<span class="hljs-keyword">const</span> router = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa-router'</span>)()

<span class="hljs-keyword">const</span> img_name = <span class="hljs-string">'./images/1.jpg'</span> <span class="hljs-comment">// 放一张图片、未来这里可以放随机一个图片</span>
<span class="hljs-keyword">const</span> max = <span class="hljs-number">90</span>; <span class="hljs-comment">// 最大值</span>
<span class="hljs-keyword">const</span> min = <span class="hljs-number">270</span>; <span class="hljs-comment">// 最小值</span>
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();
<span class="hljs-keyword">let</span> random = <span class="hljs-number">0</span> <span class="hljs-comment">// 仅仅做demo、未来存储redis这里则不需要</span>

app.use(router.routes())
router.get(<span class="hljs-string">'/'</span>, <span class="hljs-keyword">async</span> (ctx) => &#123;
    ctx.body = <span class="hljs-string">"hello!"</span>
&#125;)

<span class="hljs-comment">// 发起图片请求</span>
router.get(<span class="hljs-string">'/getImg'</span>, <span class="hljs-keyword">async</span> (ctx) => &#123;
    <span class="hljs-comment">// 生产一个随机数</span>
  random = <span class="hljs-built_in">Math</span>.ceil(<span class="hljs-built_in">Math</span>.random() * (max - min) + min);
  <span class="hljs-comment">// 生成一张图片、这里可以详细的看sharp的文档，比如模糊这个功能就可以开启。</span>
    <span class="hljs-keyword">await</span> sharp(img_name)
        .resize(<span class="hljs-number">400</span>, <span class="hljs-number">400</span>)
        .rotate(random)
        .toBuffer()
        .then(<span class="hljs-function"><span class="hljs-params">bitmap</span> =></span> &#123;
      <span class="hljs-comment">// </span>
            <span class="hljs-keyword">const</span> base64str = Buffer.from(bitmap, <span class="hljs-string">'binary'</span>).toString(<span class="hljs-string">'base64'</span>); <span class="hljs-comment">// base64编码</span>
            ctx.body = &#123;
                <span class="hljs-attr">base64str</span>: <span class="hljs-string">`data:image/png;base64,<span class="hljs-subst">$&#123;base64str&#125;</span>`</span>
                <span class="hljs-comment">// id: 此处可以给予一个uuid方便查询</span>
            &#125;
        &#125;)
&#125;)

<span class="hljs-comment">// 图片的验证</span>
router.get(<span class="hljs-string">'/validation'</span>, <span class="hljs-keyword">async</span> (ctx) => &#123;
    <span class="hljs-keyword">const</span> rotate = ctx.request.query.rotate;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Math</span>.abs(<span class="hljs-number">360</span> - rotate - random));
  <span class="hljs-comment">// 此处10可以修改的更大，或者更小，来调整难度</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Math</span>.abs(<span class="hljs-number">360</span> - rotate - random) <= <span class="hljs-number">10</span>) &#123;
        ctx.body = &#123;
            <span class="hljs-attr">flag</span>: <span class="hljs-literal">true</span>
        &#125;
        <span class="hljs-keyword">return</span>;
    &#125;
    ctx.body = &#123;
        <span class="hljs-attr">flag</span>: <span class="hljs-literal">false</span>
    &#125;
&#125;)


app.listen(<span class="hljs-number">3000</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'server is running at http://localhost:3000'</span>)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">7.2 vue代码</h3>
<blockquote>
<p>基于vue-drag-verify开发 DragVerify.vue</p>
</blockquote>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="drag-verify-container">
    <div :style="dragVerifyImgStyle">
      <img
        ref="checkImg"
        :src="imgsrc"
        class="check-img"
        :class="&#123; goOrigin: isOk &#125;"
        @load="checkimgLoaded"
        :style="imgStyle"
        alt=""
      />
      <div class="tips success" v-if="showTips && isPassing">&#123;&#123; successTip &#125;&#125;</div>
      <div class="tips danger" v-if="showTips && !isPassing && showErrorTip">&#123;&#123; failTip &#125;&#125;</div>
    </div>
    <div
      ref="dragVerify"
      class="drag_verify"
      :style="dragVerifyStyle"
      @mousemove="dragMoving"
      @mouseup="dragFinish"
      @mouseleave="dragFinish"
      @touchmove="dragMoving"
      @touchend="dragFinish"
    >
      <div
        class="dv_progress_bar"
        :class="&#123; goFirst2: isOk &#125;"
        ref="progressBar"
        :style="progressBarStyle"
      >
        &#123;&#123; successMessage &#125;&#125;
      </div>
      <div class="dv_text" :style="textStyle" ref="message">
        &#123;&#123; message &#125;&#125;
      </div>

      <div
        class="dv_handler dv_handler_bg"
        :class="&#123; goFirst: isOk &#125;"
        @mousedown="dragStart"
        @touchstart="dragStart"
        ref="handler"
        :style="handlerStyle"
      >
        <i :class="handlerIcon"></i>
      </div>
    </div>
  </div>
</template>
<script>
export default &#123;
  name: 'DragVerifyImg',
  props: &#123;
    isPassing: &#123;
      type: Boolean,
      default: false
    &#125;,
    width: &#123;
      type: Number,
      default: 250
    &#125;,
    height: &#123;
      type: Number,
      default: 40
    &#125;,
    text: &#123;
      type: String,
      default: 'swiping to the right side'
    &#125;,
    successText: &#123;
      type: String,
      default: 'success'
    &#125;,
    background: &#123;
      type: String,
      default: '#eee'
    &#125;,
    progressBarBg: &#123;
      type: String,
      default: '#76c61d'
    &#125;,
    completedBg: &#123;
      type: String,
      default: '#76c61d'
    &#125;,
    circle: &#123;
      type: Boolean,
      default: false
    &#125;,
    radius: &#123;
      type: String,
      default: '4px'
    &#125;,
    handlerIcon: &#123;
      type: String
    &#125;,
    successIcon: &#123;
      type: String
    &#125;,
    handlerBg: &#123;
      type: String,
      default: '#fff'
    &#125;,
    textSize: &#123;
      type: String,
      default: '14px'
    &#125;,
    textColor: &#123;
      type: String,
      default: '#333'
    &#125;,
    imgsrc: &#123;
      type: String
    &#125;,
    showTips: &#123;
      type: Boolean,
      default: true
    &#125;,
    successTip: &#123;
      type: String,
      default: '验证通过'
    &#125;,
    failTip: &#123;
      type: String,
      default: '验证失败'
    &#125;,
    minDegree: &#123;
      type: Number,
      default: 90
    &#125;,
    maxDegree: &#123;
      type: Number,
      default: 270
    &#125;
  &#125;,
  mounted: function () &#123;
    const dragEl = this.$refs.dragVerify;
    dragEl.style.setProperty('--textColor', this.textColor);
    dragEl.style.setProperty('--width', Math.floor(this.width / 2) + 'px');
    dragEl.style.setProperty('--pwidth', -Math.floor(this.width / 2) + 'px');
  &#125;,
  computed: &#123;
    handlerStyle: function () &#123;
      return &#123;
        width: this.height + 'px',
        height: this.height + 'px',
        background: this.handlerBg
      &#125;;
    &#125;,
    message: function () &#123;
      return this.isPassing ? '' : this.text;
    &#125;,
    successMessage: function () &#123;
      return this.isPassing ? this.successText : '';
    &#125;,
    dragVerifyStyle: function () &#123;
      return &#123;
        width: this.width + 'px',
        height: this.height + 'px',
        lineHeight: this.height + 'px',
        background: this.background,
        borderRadius: this.circle ? this.height / 2 + 'px' : this.radius
      &#125;;
    &#125;,
    dragVerifyImgStyle: function () &#123;
      return &#123;
        'width': this.width + 'px',
        'height': this.width + 'px',
        'position': 'relative',
        'overflow': 'hidden',
        'border-radius': '50%'
      &#125;;
    &#125;,
    progressBarStyle: function () &#123;
      return &#123;
        background: this.progressBarBg,
        height: this.height + 'px',
        borderRadius: this.circle
          ? this.height / 2 + 'px 0 0 ' + this.height / 2 + 'px'
          : this.radius
      &#125;;
    &#125;,
    textStyle: function () &#123;
      return &#123;
        height: this.height + 'px',
        width: this.width + 'px',
        fontSize: this.textSize
      &#125;;
    &#125;,
    factor: function () &#123;
      //避免指定旋转角度时一直拖动到最右侧才验证通过
      if (this.minDegree == this.maxDegree) &#123;
        return Math.floor(1 + Math.random() * 6) / 10 + 1;
      &#125;
      return 1;
    &#125;
  &#125;,
  data() &#123;
    return &#123;
      isMoving: false,
      x: 0,
      isOk: false,
      showBar: false,
      showErrorTip: false,
      ranRotate: 0,
      cRotate: 0,
      imgStyle: &#123;&#125;
    &#125;;
  &#125;,
  methods: &#123;
    checkimgLoaded: function () &#123;
      this.ranRotate = 120;
    &#125;,
    dragStart: function (e) &#123;
      if (!this.isPassing) &#123;
        this.isMoving = true;
        this.x = e.pageX || e.touches[0].pageX;
      &#125;
      this.showBar = true;
      this.showErrorTip = false;
      this.$emit('handlerMove');
    &#125;,
    dragMoving: function (e) &#123;
      if (this.isMoving && !this.isPassing) &#123;
        var _x = (e.pageX || e.touches[0].pageX) - this.x;
        var handler = this.$refs.handler;
        handler.style.left = _x + 'px';
        this.$refs.progressBar.style.width = _x + this.height / 2 + 'px';
        var cRotate = Math.ceil((_x / (this.width - this.height)) * this.maxDegree * this.factor);
        this.cRotate = cRotate;
        var rotate = cRotate;
        this.imgStyle = &#123;
          transform: `rotateZ($&#123;rotate&#125;deg)`
        &#125;;
      &#125;
    &#125;,
    dragFinish: function () &#123;
      if (this.isMoving && !this.isPassing) &#123;
        this.$emit('postRotate', this.cRotate);
        this.isMoving = false;
      &#125;
    &#125;,
    setFinish(val) &#123;
      if (val) &#123;
        this.passVerify();
        return;
      &#125;
      this.isOk = true;
      this.imgStyle = &#123;
        transform: `rotateZ($&#123;this.ranRotate&#125;deg)`
      &#125;;
      const that = this;
      setTimeout(function () &#123;
        const handler = that.$refs.handler;
        const progressBar = that.$refs.progressBar;
        handler.style.left = '0';
        progressBar.style.width = '0';
        that.isOk = false;
      &#125;, 500);
      this.showErrorTip = true;
      this.$emit('update:isPassing', false);
      this.$emit('passfail');
    &#125;,
    passVerify: function () &#123;
      this.$emit('update:isPassing', true);
      this.isMoving = false;
      var handler = this.$refs.handler;
      handler.children[0].className = this.successIcon;
      this.$refs.progressBar.style.background = this.completedBg;
      this.$refs.message.style['-webkit-text-fill-color'] = 'unset';
      this.$refs.message.style.animation = 'slidetounlock2 3s infinite';
      this.$refs.progressBar.style.color = '#fff';
      this.$refs.progressBar.style.fontSize = this.textSize;
      this.$emit('passcallback');
    &#125;,
    reset: function () &#123;
      this.reImg();
      this.checkimgLoaded();
    &#125;,
    reImg: function () &#123;
      this.$emit('update:isPassing', false);
      const oriData = this.$options.data();
      for (const key in oriData) &#123;
        if (Object.prototype.hasOwnProperty.call(oriData, key)) &#123;
          this[key] = oriData[key];
        &#125;
      &#125;
      var handler = this.$refs.handler;
      var message = this.$refs.message;
      handler.style.left = '0';
      this.$refs.progressBar.style.width = '0';
      handler.children[0].className = this.handlerIcon;
      message.style['-webkit-text-fill-color'] = 'transparent';
      message.style.animation = 'slidetounlock 3s infinite';
      message.style.color = this.background;
    &#125;,
    refreshimg: function () &#123;
      this.$emit('refresh');
    &#125;
  &#125;,
  watch: &#123;
    imgsrc: &#123;
      immediate: false,
      handler: function () &#123;
        this.reImg();
      &#125;
    &#125;
  &#125;
&#125;;
</script>
<style scoped>
.drag_verify &#123;
  position: relative;
  background-color: #e8e8e8;
  text-align: center;
  overflow: hidden;
&#125;
.drag_verify .dv_handler &#123;
  position: absolute;
  top: 0px;
  left: 0px;
  cursor: move;
&#125;
.drag_verify .dv_handler i &#123;
  color: #666;
  padding-left: 0;
  font-size: 16px;
&#125;
.drag_verify .dv_handler .el-icon-circle-check &#123;
  color: #6c6;
  margin-top: 9px;
&#125;
.drag_verify .dv_progress_bar &#123;
  position: absolute;
  height: 34px;
  width: 0px;
&#125;
.drag_verify .dv_text &#123;
  position: absolute;
  top: 0px;
  color: transparent;
  -moz-user-select: none;
  -webkit-user-select: none;
  user-select: none;
  -o-user-select: none;
  -ms-user-select: none;
  background: -webkit-gradient(
    linear,
    left top,
    right top,
    color-stop(0, var(--textColor)),
    color-stop(0.4, var(--textColor)),
    color-stop(0.5, #fff),
    color-stop(0.6, var(--textColor)),
    color-stop(1, var(--textColor))
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  -webkit-text-size-adjust: none;
  animation: slidetounlock 3s infinite;
&#125;
.drag_verify .dv_text * &#123;
  -webkit-text-fill-color: var(--textColor);
&#125;
.goFirst &#123;
  left: 0px !important;
  transition: left 0.5s;
&#125;
.goOrigin &#123;
  transition: transform 0.5s;
&#125;
.goKeep &#123;
  transition: left 0.2s;
&#125;
.goFirst2 &#123;
  width: 0px !important;
  transition: width 0.5s;
&#125;
.drag-verify-container &#123;
  position: relative;
  line-height: 0;
  border-radius: 50%;
&#125;
.move-bar &#123;
  position: absolute;
  z-index: 100;
&#125;
.clip-bar &#123;
  position: absolute;
  background: rgba(255, 255, 255, 0.8);
&#125;
.refresh &#123;
  position: absolute;
  right: 5px;
  top: 5px;
  cursor: pointer;
  font-size: 20px;
  z-index: 200;
&#125;
.tips &#123;
  position: absolute;
  bottom: 25px;
  height: 20px;
  line-height: 20px;
  text-align: center;
  width: 100%;
  font-size: 12px;
  z-index: 200;
&#125;
.tips.success &#123;
  background: rgba(255, 255, 255, 0.6);
  color: green;
&#125;
.tips.danger &#123;
  background: rgba(0, 0, 0, 0.6);
  color: yellow;
&#125;
.check-img &#123;
  width: 140%;
  margin-left: -20%;
  margin-top: -20%;
  border-radius: 50%;
  /* width: 100%;
*/
&#125;
</style>
<style>
@-webkit-keyframes slidetounlock &#123;
  0% &#123;
    background-position: var(--pwidth) 0;
  &#125;
  100% &#123;
    background-position: var(--width) 0;
  &#125;
&#125;
@-webkit-keyframes slidetounlock2 &#123;
  0% &#123;
    background-position: var(--pwidth) 0;
  &#125;
  100% &#123;
    background-position: var(--pwidth) 0;
  &#125;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>app.vue</p>
</blockquote>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <drag-verify-img
      ref="verify"
      :imgsrc="imgsrc"
      :isPassing.sync="isPassing"
      text="请按住滑块拖动"
      successText="验证通过"
      handlerIcon="el-icon-d-arrow-right"
      successIcon="el-icon-circle-check"
      @postRotate="postRotate"
      @passcallback="passcallback"
      @passfail="passfail"
    >
    </drag-verify-img>
  </div>
</template>

<script>
import DragVerifyImg from './components/DragVerify.vue';
import axios from 'axios';

export default &#123;
  name: 'App',
  components: &#123;
    DragVerifyImg
  &#125;,
  data: function () &#123;
    return &#123;
      imgsrc: '',
      isPassing: false
    &#125;;
  &#125;,
  created() &#123;
    this.getImg();
  &#125;,
  methods: &#123;
    async getImg() &#123;
      try &#123;
        const res = await axios.get('/api/getImg');
        this.imgsrc = res.data.base64str;
      &#125; catch (error) &#123;
        console.log(error);
      &#125;
    &#125;,
    async postRotate(val) &#123;
      const res = await axios.get(`/api/validation?rotate=$&#123;val&#125;`);
      this.$refs.verify.setFinish(res.data.flag);
    &#125;,
    passcallback() &#123;
      console.log('成功');
    &#125;,
    passfail() &#123;
      this.$refs.verify.reset(); // 默认重置
      console.log('失败');
    &#125;
  &#125;
&#125;;
</script>

<style lang="scss">
#app &#123;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">8 github地址</h2>
<blockquote>
<p><a href="https://github.com/MYQ1996/drag-verify-demo.git" target="_blank" rel="nofollow noopener noreferrer">github.com/MYQ1996/dra…</a></p>
</blockquote></div>  
</div>
            