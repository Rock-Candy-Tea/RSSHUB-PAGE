
---
title: 'JS-VUE-九宫格抽奖'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a3c77dcd6cf4d0cbea92393d5efc41f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 12 May 2021 01:55:44 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a3c77dcd6cf4d0cbea92393d5efc41f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>继之前两篇“老虎机抽奖”、“大转盘抽奖”，所以把九宫格也一并补全了，整体的实现方案不是很复杂，就是dom以及中奖的配置需要特别注意一下，好了话不多少，直接开始~</p>
<h3 data-id="heading-1">其他方案</h3>
<p><a href="https://juejin.cn/post/6903693990781321230" target="_blank">JS-VUE-老虎机抽奖>>></a></p>
<p><a href="https://juejin.cn/post/6961317142465609742" target="_blank">JS-VUE-大转盘抽奖>>></a></p>
<h3 data-id="heading-2">UI</h3>
<ul>
<li>老规矩，先看下静态UI，以便于有个图像概念</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a3c77dcd6cf4d0cbea92393d5efc41f~tplv-k3u1fbpfcp-watermark.image" alt="1620808806(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">方案分析</h3>
<ul>
<li>
<h4 data-id="heading-4">思路清单</h4>
<ul>
<li>
<p>结构布局，九个位置（<code>左青龙，右白虎，老牛在中间</code>），具体的可以看下面参考图</p>
<ul>
<li>这里有个好玩的地方了，1-9个位置（可不是简单的1-9哦，是跑外圈哦）,如果是静态布局，其实就是九个盒子，没啥复杂的；但如果是动态渲染同一个数据列表，有同学说了，也很简单做个判断呗；但是如果服务端返回的json是无序的，那么我们要怎么处理前端的方案以及怎么和服务端制定比较友好的数据结构呢，先买个小关子，一起往下看，看看我会不会和可爱的你想的一样呢~</li>
</ul>
</li>
<li>
<p>核心逻辑，跑毒（不对跑圈）</p>
<ul>
<li>
<ol>
<li>设定数量圈数 （我就是个冷冰冰的数字）</li>
</ol>
</li>
<li>
<ol start="2">
<li>设置速度（思路就是，每一次递归我都会越来越快哦，好吧，其实就是<code>速度++</code>，等到达上述1的指定圈数后，我在+10圈让<code>速度--</code>，是不是很简单~）</li>
</ol>
</li>
</ul>
</li>
<li>
<p>选中效果（不用怜悯我，根据每次递归的下标，给我设置一个冷冰冰的class并把上一个兄弟的class清空就行了）</p>
</li>
</ul>
</li>
<li>
<h4 data-id="heading-5">初始参考各值参考图</h4>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7350b89cfbe448e82c3b112a302bc7a~tplv-k3u1fbpfcp-watermark.image" alt="abb6e1af3314d0718664561ce8fff92.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">实现逻辑</h3>
<h4 data-id="heading-7">参数配置</h4>
<pre><code class="copyable">data () &#123;
    return &#123;
      resultList: [], // 奖品列表
      isTurn: true, // 是否可以抽奖
      index: 1, //当前转动到哪个位置，起点位置
      orderList: [1, 2, 3, 8, -9, 4, 7, 6, 5], // 正常循环排列下的顺序 0 为中间的抽奖按钮/分区标识
      lotterywin: -9, // 中奖位置
      lottery: &#123;
        count: 8, //总共有多少个位置
        timer: 0, //setTimeout的ID，用clearTimeout清除
        speed: 35, //初始转动速度
        times: 0, //转动次数
        cynum: 50, // 圈数
        win: 0 //中奖位置 0 默认不中奖
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h4 data-id="heading-8">第一步，我来填坑了，先把结构搞出来</h4>
结构分析 根据上述参考图，得到 <code>-9</code> 为中间按钮需要特殊处理（必须是-9吗，不，宝贝，随你开心~）</li>
</ul>
<pre><code class="copyable">  <ul>
      <li
        :ref="`item$&#123;val.order&#125;`"
        :data-index="val.order"
        :class="val.order >= 1 ? 'rw' : ''"
        v-for="val in resultList"
        :key="val.prize_id"
      >
        <div v-if="val.order !== -9">
          <div class="header"><img :src="val.prize_img" alt="" /></div>
          <div class="name">&#123;&#123; val.name &#125;&#125;</div>
        </div>
        <div v-else class="start" @click.stop.prevent="startGo"></div>
      </li>
    </ul>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h4 data-id="heading-9">第二步，渲染顺序（产品大佬：这不是我要的顺序啊）</h4>
<ul>
<li>
<p>设计数据结构</p>
<p>结构中定义好 order 顺序，无论远端如何调整，只要遵循规则，前端拿到直接根据order排序即可（所以服务端返回的数据可以是无序的）</p>
<pre><code class="copyable"> 
[
      &#123;
        name: '10点券',
        prize_img: coupon,
        prize_id: 'c10',
        order: 1 // 没错我就是顺序
      &#125;,
      &#123;
        name: '20点券',
        prize_img: coupon,
        prize_id: 'c20',
        order: 2
      &#125;,
       ......
      &#123;
        name: '80点券',
        prize_img: coupon,
        prize_id: 'c80',
        order: 8
      &#125;
  ]
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>排序</p>
<p>既然结构规则定义好了，那么我默认就有个一组排序值，-9为中心位置（<code>// 根据 orderList 的顺序重新排列服务端奖品列表</code>）</p>
<pre><code class="copyable"> orderList: [1, 2, 3, 8, -9, 4, 7, 6, 5]
 // 开始排序
 // 处理 最终的列表渲染顺序 已正常的排序思维顺序
    const keyObj = &#123;&#125;
    const arr = []
    const downArr = Object.assign([], val)
    if (downArr.length) &#123;
      downArr.push(&#123; order: -9 &#125;)
      downArr.forEach(element => &#123;
        keyObj[element.order] = element
      &#125;)
      // 依据数组的顺序填充
      this.orderList.forEach(ele => &#123;
        arr.push(keyObj[ele])
      &#125;)
    &#125;
    this.resultList = arr
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<h4 data-id="heading-10">第三步，开始让我跑起来吧</h4>
<code>上活，setTimeout，执行时间 加的越多越慢反之越快</code></li>
</ul>
<pre><code class="copyable">  _rolling () &#123;
      this.lottery.times++
      this._roll_actived() // 设置状态
      // +10 将速度降下来的圈数周期
      if (
        this.lottery.times > this.lottery.cynum + 10 &&
        this.lotterywin === this.index
      ) &#123;
        clearTimeout(this.lottery.timer)
        setTimeout(() => &#123;
          this.resetData()
          this.$emit('change', 'fin', &#123;&#125;)
        &#125;, 1000) // 此时间给予用户感受中奖反馈时间
      &#125; else &#123;
        if (this.lottery.times > this.lottery.cynum) this.lottery.speed += 20 // 惯性 越来越慢
        this.index++
        this.lottery.timer = setTimeout(this._rolling, this.lottery.speed)
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h4 data-id="heading-11">第四步，设置状态</h4>
干掉上一个样式，新增当前index，调整classList
<pre><code class="copyable">_roll_actived () &#123;
    // running 选中的状态
    let pre = this.index - 1
    if (this.index > this.lottery.count) this.index = 1
    const preDom = this.$refs['item' + pre]
    const downDom = this.$refs['item' + this.index]
    if (pre > 0 && preDom) &#123;
      preDom[0].classList.remove('active')
    &#125;
    if (downDom) &#123;
      downDom[0].classList.add('active')
    &#125;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h4 data-id="heading-12">第五步，其他拓展</h4>
<ul>
<li>获取真实奖品</li>
</ul>
<pre><code class="copyable">// await api 获取中奖信息 （因为数据结构的定义，这里拿到中奖位置将变得非常 esay）
    let win = 6 // 模拟中奖位置
 // 拿到中奖位置就可以跑毒了~
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>抽奖的生命周期</li>
</ul>
<pre><code class="copyable">this.$emit('change', 'start', &#123;&#125;) // 抽奖开始
this.$emit('change', 'fin', &#123;&#125;) // 抽奖完成
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-13">组件使用</h3>
<ul>
<li>使用</li>
</ul>
<pre><code class="copyable">import sudoluWrap from '../../components/sudoku/sudoku.vue'
<sudoluWrap @change="lotteryChange" :awardList="awardList"></sudoluWrap>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">抽奖效果</h3>
<p><code>我这个录屏git软件有点问题，抓不到特别快的帧，大家想看效果可以跑一跑源代码，文末有，或者参考的快结束的那一段跑毒效果</code></p>
<p>另外哪位小可爱有比较好的软件可以推荐一下，评论区等你哈~</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eab0439473f94d979e673779c328bf55~tplv-k3u1fbpfcp-watermark.image" alt="GIF 2021-5-12 17-42-43.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">结语</h3>
<p>打完收工，以上提供核心思路和一些简单的配置，更加粒度的操作，交给勤快可爱的大家哈~</p>
<p>另附本文-<a href="https://github.com/uniquedestiny/vue-cli3-more" target="_blank" rel="nofollow noopener noreferrer">源码地址</a>，欢迎探讨哈~</p></div>  
</div>
            