
---
title: '记录一个基于vue2的小组件升级为基于vue3的组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6373'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 23:36:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=6373'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近用vue3+vue-router4+vuex4搭建了一个项目框架，用到了一个基于vue2的小组件，遂将它改成了基于vue3的，在修改的过程中出现了一个小问题，在查资料修改的过程中对vue3的一些概念的理解又深刻了一些，遂记录下来。</p>
<p>原组件是一个图片验证码，源代码非常简单，代码如下：<a href="https://github.com/luguanrui/vue-img-verify" target="_blank" rel="nofollow noopener noreferrer">地址</a></p>
<pre><code class="copyable"><template>
  <div class="img-verify">
    <canvas ref="verify" :width="width" :height="height" @click="handleDraw"></canvas>
  </div>
</template>

<script type="text/ecmascript-6">
export default &#123;
  data() &#123;
    return &#123;
      pool: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', // 字符串
      width: 120,
      height: 40,
      imgCode: ''
    &#125;
  &#125;,
  mounted() &#123;
    // 绘制图片验证码
    this.handleDraw();
  &#125;,
  methods: &#123;
    // 点击图片重新绘制
    handleDraw() &#123;
      this.$emit('getImgCode', this.draw())
    &#125;,
    // 1.随机数
    randomNum(min, max) &#123;
      return parseInt(Math.random() * (max - min) + min)
    &#125;,
    // 2.随机颜色
    randomColor(min, max) &#123;
      const r = this.randomNum(min, max)
      const g = this.randomNum(min, max)
      const b = this.randomNum(min, max)
      return `rgb($&#123;r&#125;,$&#123;g&#125;,$&#123;b&#125;)`
    &#125;,
    // 绘制图片
    draw() &#123;
      // 3.填充背景颜色，背景颜色要浅一点
      const ctx = this.$refs.verify.getContext('2d')
      // 填充颜色
      ctx.fillStyle = this.randomColor(180, 230)
      // 填充的位置
      ctx.fillRect(0, 0, this.width, this.height)
      // 定义paramText
      let imgCode = ''
      // 4.随机产生字符串，并且随机旋转
      for (let i = 0; i < 4; i++) &#123;
        // 随机的四个字
        const text = this.pool[this.randomNum(0, this.pool.length)]
        imgCode += text
        // 随机的字体大小
        const fontSize = this.randomNum(18, 40)
        // 字体随机的旋转角度
        const deg = this.randomNum(-30, 30)
        /*
         * 绘制文字并让四个文字在不同的位置显示的思路 :
         * 1、定义字体
         * 2、定义对齐方式
         * 3、填充不同的颜色
         * 4、保存当前的状态（以防止以上的状态受影响）
         * 5、平移translate()
         * 6、旋转 rotate()
         * 7、填充文字
         * 8、restore出栈
         * */
        ctx.font = fontSize + 'px Simhei'
        ctx.textBaseline = 'top'
        ctx.fillStyle = this.randomColor(80, 150)
        /*
         * save() 方法把当前状态的一份拷贝压入到一个保存图像状态的栈中。
         * 这就允许您临时地改变图像状态，
         * 然后，通过调用 restore() 来恢复以前的值。
         * save是入栈，restore是出栈。
         * 用来保存Canvas的状态。save之后，可以调用Canvas的平移、放缩、旋转、错切、裁剪等操作。 restore：用来恢复Canvas之前保存的状态。防止save后对Canvas执行的操作对后续的绘制有影响。
         *
         * */
        ctx.save()
        ctx.translate(30 * i + 15, 15)
        ctx.rotate((deg * Math.PI) / 180)
        // fillText() 方法在画布上绘制填色的文本。文本的默认颜色是黑色。
        // 请使用 font 属性来定义字体和字号，并使用 fillStyle 属性以另一种颜色/渐变来渲染文本。
        // context.fillText(text,x,y,maxWidth);
        ctx.fillText(text, -15 + 5, -15)
        ctx.restore()
      &#125;
      // 5.随机产生5条干扰线,干扰线的颜色要浅一点
      for (let i = 0; i < 5; i++) &#123;
        ctx.beginPath()
        ctx.moveTo(this.randomNum(0, this.width), this.randomNum(0, this.height))
        ctx.lineTo(this.randomNum(0, this.width), this.randomNum(0, this.height))
        ctx.strokeStyle = this.randomColor(180, 230)
        ctx.closePath()
        ctx.stroke()
      &#125;
      // 6.随机产生40个干扰的小点
      for (let i = 0; i < 40; i++) &#123;
        ctx.beginPath()
        ctx.arc(this.randomNum(0, this.width), this.randomNum(0, this.height), 1, 0, 2 * Math.PI)
        ctx.closePath()
        ctx.fillStyle = this.randomColor(150, 200)
        ctx.fill()
      &#125;
      return imgCode
    &#125;
  &#125;
&#125;
</script>
<style type="text/css">
.img-verify canvas &#123;
  cursor: pointer;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改的思路：</p>
<ol>
<li>将export default对象中的data、methods等用setup代替</li>
<li>将原data中的数据用reactive定义，用return导出</li>
<li>methods中的方法直接在setup中定义</li>
<li>去掉this，emit来源为setup的参数</li>
<li>this.$refs用ref定义并return，ref的值用ref().value代替（<strong>注意：查资料说是这么改的</strong>）</li>
</ol>
<p>修改后的代码如下：</p>
<pre><code class="copyable"><template>
  <div class="img-verify">
    <canvas ref="verify" :width="data.width" :height="data.height" @click="handleDraw"></canvas>
  </div>
</template>

<script>
import &#123; reactive ,ref,onMounted&#125; from 'vue';
export default &#123;
  setup(props,&#123;emit&#125;)&#123;
    const data=reactive(&#123;
      pool: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', // 字符串
      width: 120,
      height: 40,
      imgCode: ''
    &#125;)
    const verify=ref(null);
    handleDraw();
    function handleDraw()&#123;
      emit('getImgCode', draw())
    &#125;
    // 1.随机数
    function randomNum(min, max) &#123;
      return parseInt(Math.random() * (max - min) + min)
    &#125;
    // 2.随机颜色
    function randomColor(min, max) &#123;
      const r = randomNum(min, max)
      const g = randomNum(min, max)
      const b = randomNum(min, max)
      return `rgb($&#123;r&#125;,$&#123;g&#125;,$&#123;b&#125;)`
    &#125;
   
    function draw() &#123;
      // 3.填充背景颜色，背景颜色要浅一点
      const ctx = verify.value.getContext('2d')
      // 填充颜色
      ctx.fillStyle = randomColor(180, 230)
      // 填充的位置
      ctx.fillRect(0, 0, data.width, data.height)
      // 定义paramText
      let imgCode = ''
      // 4.随机产生字符串，并且随机旋转
      for (let i = 0; i < 4; i++) &#123;
        // 随机的四个字
        const text = data.pool[randomNum(0, data.pool.length)]
        imgCode += text
        // 随机的字体大小
        const fontSize = randomNum(18, 40)
        // 字体随机的旋转角度
        const deg = randomNum(-30, 30)
        /*
         * 绘制文字并让四个文字在不同的位置显示的思路 :
         * 1、定义字体
         * 2、定义对齐方式
         * 3、填充不同的颜色
         * 4、保存当前的状态（以防止以上的状态受影响）
         * 5、平移translate()
         * 6、旋转 rotate()
         * 7、填充文字
         * 8、restore出栈
         * */
        ctx.font = fontSize + 'px Simhei'
        ctx.textBaseline = 'top'
        ctx.fillStyle = randomColor(80, 150)
        /*
         * save() 方法把当前状态的一份拷贝压入到一个保存图像状态的栈中。
         * 这就允许您临时地改变图像状态，
         * 然后，通过调用 restore() 来恢复以前的值。
         * save是入栈，restore是出栈。
         * 用来保存Canvas的状态。save之后，可以调用Canvas的平移、放缩、旋转、错切、裁剪等操作。 restore：用来恢复Canvas之前保存的状态。防止save后对Canvas执行的操作对后续的绘制有影响。
         *
         * */
        ctx.save()
        ctx.translate(30 * i + 15, 15)
        ctx.rotate((deg * Math.PI) / 180)
        // fillText() 方法在画布上绘制填色的文本。文本的默认颜色是黑色。
        // 请使用 font 属性来定义字体和字号，并使用 fillStyle 属性以另一种颜色/渐变来渲染文本。
        // context.fillText(text,x,y,maxdata.width);
        ctx.fillText(text, -15 + 5, -15)
        ctx.restore()
      &#125;
      // 5.随机产生5条干扰线,干扰线的颜色要浅一点
      for (let i = 0; i < 5; i++) &#123;
        ctx.beginPath()
        ctx.moveTo(randomNum(0, data.width), randomNum(0, data.height))
        ctx.lineTo(randomNum(0, data.width), randomNum(0, data.height))
        ctx.strokeStyle = randomColor(180, 230)
        ctx.closePath()
        ctx.stroke()
      &#125;
      // 6.随机产生40个干扰的小点
      for (let i = 0; i < 40; i++) &#123;
        ctx.beginPath()
        ctx.arc(randomNum(0, data.width), randomNum(0, data.height), 1, 0, 2 * Math.PI)
        ctx.closePath()
        ctx.fillStyle = randomColor(150, 200)
        ctx.fill()
      &#125;
      return imgCode
    &#125;
    return &#123;data,verify&#125;
  &#125;
  

  
&#125;
</script>
<style type="text/css">
.img-verify canvas &#123;
  cursor: pointer;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，这样代码报错，说value前面的值为undefind，查了好多资料都说这么改没问题，但就是报错，无奈继续查，终于在查资料的过程中看到了一句话给了我启发</p>
<blockquote>
<p>setup执行时尚未创建组件实例</p>
</blockquote>
<p>既然setup执行时尚未创建组件实例，ref(0)又为undefind，那是否是因为是在组件加载完成之后才能执行ref(0).value的语句呢，于是将执行ref(0).value的语句的代码放在onmounted生命周期函数里，成功，
最终代码如下：</p>
<pre><code class="copyable"><template>
  <div class="img-verify">
    <canvas ref="verify" :width="data.width" :height="data.height" @click="handleDraw"></canvas>
  </div>
</template>

<script>
import &#123; reactive ,ref,onMounted&#125; from 'vue';
export default &#123;
  setup(props,&#123;emit&#125;)&#123;
    const data=reactive(&#123;
      pool: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', // 字符串
      width: 120,
      height: 40,
      imgCode: ''
    &#125;)
    const verify=ref(null);
    onMounted(() => &#123;
        // DOM元素将在初始渲染后分配给ref
        console.log(verify.value) // <div>这是根元素</div>
        handleDraw();
      &#125;)
    // handleDraw();
    function handleDraw()&#123;
      emit('getImgCode', draw())
    &#125;
    // 1.随机数
    function randomNum(min, max) &#123;
      return parseInt(Math.random() * (max - min) + min)
    &#125;
    // 2.随机颜色
    function randomColor(min, max) &#123;
      const r = randomNum(min, max)
      const g = randomNum(min, max)
      const b = randomNum(min, max)
      return `rgb($&#123;r&#125;,$&#123;g&#125;,$&#123;b&#125;)`
    &#125;
    
    function draw() &#123;
      // 3.填充背景颜色，背景颜色要浅一点
      const ctx = verify.value.getContext('2d')
      // 填充颜色
      ctx.fillStyle = randomColor(180, 230)
      // 填充的位置
      ctx.fillRect(0, 0, data.width, data.height)
      // 定义paramText
      let imgCode = ''
      // 4.随机产生字符串，并且随机旋转
      for (let i = 0; i < 4; i++) &#123;
        // 随机的四个字
        const text = data.pool[randomNum(0, data.pool.length)]
        imgCode += text
        // 随机的字体大小
        const fontSize = randomNum(18, 40)
        // 字体随机的旋转角度
        const deg = randomNum(-30, 30)
        /*
         * 绘制文字并让四个文字在不同的位置显示的思路 :
         * 1、定义字体
         * 2、定义对齐方式
         * 3、填充不同的颜色
         * 4、保存当前的状态（以防止以上的状态受影响）
         * 5、平移translate()
         * 6、旋转 rotate()
         * 7、填充文字
         * 8、restore出栈
         * */
        ctx.font = fontSize + 'px Simhei'
        ctx.textBaseline = 'top'
        ctx.fillStyle = randomColor(80, 150)
        /*
         * save() 方法把当前状态的一份拷贝压入到一个保存图像状态的栈中。
         * 这就允许您临时地改变图像状态，
         * 然后，通过调用 restore() 来恢复以前的值。
         * save是入栈，restore是出栈。
         * 用来保存Canvas的状态。save之后，可以调用Canvas的平移、放缩、旋转、错切、裁剪等操作。 restore：用来恢复Canvas之前保存的状态。防止save后对Canvas执行的操作对后续的绘制有影响。
         *
         * */
        ctx.save()
        ctx.translate(30 * i + 15, 15)
        ctx.rotate((deg * Math.PI) / 180)
        // fillText() 方法在画布上绘制填色的文本。文本的默认颜色是黑色。
        // 请使用 font 属性来定义字体和字号，并使用 fillStyle 属性以另一种颜色/渐变来渲染文本。
        // context.fillText(text,x,y,maxdata.width);
        ctx.fillText(text, -15 + 5, -15)
        ctx.restore()
      &#125;
      // 5.随机产生5条干扰线,干扰线的颜色要浅一点
      for (let i = 0; i < 5; i++) &#123;
        ctx.beginPath()
        ctx.moveTo(randomNum(0, data.width), randomNum(0, data.height))
        ctx.lineTo(randomNum(0, data.width), randomNum(0, data.height))
        ctx.strokeStyle = randomColor(180, 230)
        ctx.closePath()
        ctx.stroke()
      &#125;
      // 6.随机产生40个干扰的小点
      for (let i = 0; i < 40; i++) &#123;
        ctx.beginPath()
        ctx.arc(randomNum(0, data.width), randomNum(0, data.height), 1, 0, 2 * Math.PI)
        ctx.closePath()
        ctx.fillStyle = randomColor(150, 200)
        ctx.fill()
      &#125;
      return imgCode
    &#125;
    return &#123;data,verify&#125;
  &#125;
  

  
&#125;
</script>
<style type="text/css">
.img-verify canvas &#123;
  cursor: pointer;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：看来还是没有深刻的理解好概念，还需好好修炼</p></div>  
</div>
            