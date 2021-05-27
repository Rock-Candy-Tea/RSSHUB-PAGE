
---
title: 'vue加入购物车动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6696'
author: 掘金
comments: false
date: Wed, 26 May 2021 23:24:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=6696'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">使用方法</h3>
<pre><code class="copyable"><addShop ref="addShop" />

import addShop from '@/views/components/addShop'

 
// dom：需要移动的dom   
// state ：true添加 false移除 

 this.$refs.addschool.init(dom, state)
 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">addShop组件</h3>
<pre><code class="copyable"> <template>
  <div class="add-school-box">
    <transition @before-enter="beforeEnter"
      @enter="enter"
      @after-enter="afterEnter">
      <div id="cloneBox"
        v-show="isShow"></div>
    </transition>
    <div class="add-school-shop"
      :style="&#123;left: isCollapse ? '250px' : '100px'&#125;">
      <i class="el-icon-shopping-cart-full"></i>
    </div>
  </div>
</template>

<script>
import addShop from '@/utils/addShop'
export default &#123;
  data () &#123;
    return &#123;
      addShop: '',
      isShow: false
    &#125;
  &#125;,
  computed: &#123;
    isCollapse () &#123;
      return this.$store.state.app.sidebar.opened
    &#125;
  &#125;,
  mounted () &#123;
  &#125;,
  methods: &#123;
    //dom 加入的dom state  true添加 false删除
    init (dom, state) &#123;
      this.addCard = new addShop(&#123;
        dom,// 需要克隆的dom
        state, // 删除还是新增，
        cloneBoxId: 'cloneBox', // 克隆dom 的容器
        shopClass: 'add-school-shop', // 购物车dom
        shopAnmationClass: 'dom-all-in'
      &#125;)
      this.addCard.init()
      this.isShow = true
    &#125;,
    // el表示要执行动画的dom元素
    beforeEnter (el) &#123;
      this.addCard.beforeEnter(el)
    &#125;,
    // 设置完成动画之后的结束状态
    enter (el, done) &#123;
      this.addCard.enter(el, done)
    &#125;,
    // 动画完成之后调用afterEnter函数
    afterEnter (el) &#123;
      this.addCard.afterEnter(el).then(() => &#123;
        this.isShow = false
      &#125;)
    &#125;
  &#125;,

&#125;
</script>

<style lang="scss">
.add-school-shop &#123;
  position: fixed;
  bottom: 100px;
  left: 200px;
  width: 100px;
  height: 100px;
  transition: all 0.4s;
  i &#123;
    font-size: 100px;
  &#125;
&#125;
.dom-all-in &#123;
  animation: mymove 1s infinite;
  animation-iteration-count: 1;
&#125;
@keyframes mymove &#123;
  0% &#123;
    transform: scale(1); /*开始为原始大小*/
  &#125;
  50% &#123;
    transform: scale(1.2);
  &#125;
  100% &#123;
    transform: scale(1);
  &#125;
&#125;
</style>


<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">使用到的addShop方法</h3>
<pre><code class="copyable">export default class addShop &#123;
  constructor(&#123; dom, shopClass, state, cloneBoxId, shopAnmationClass &#125;) &#123;
    // 点击的dom
    this.dom = dom;
    // 购物车dom
    this.shopDom = "";
    this.shopClass = shopClass;
    this.shopAnmationClass = shopAnmationClass;
    // 判断是添加还是删除
    this.state = state;
    // 复制的dom
    this.cloneDiv = "";
    // 装复制dom的容器
    this.cloneDomBox = "";
    this.cloneBoxId = cloneBoxId;
    this.x = 0;
    this.y = 0;
    // 点击dom的信息
    this.width = 0;
    this.height = 0;
    // 购物车的位置信息
    this.shopX = 0;
    this.shopY = 0;
  &#125;
  init() &#123;
    this.shopDom = document.getElementsByClassName(this.shopClass)[0]; // 购物车dom
    this.cloneDomBox = document.getElementById(this.cloneBoxId); // 克隆dom 的容器
    // 初始化被点击dom的信息
    const oRectDom = this.dom.getBoundingClientRect();
    const &#123; width, height, x, y &#125; = oRectDom;
    this.width = width;
    this.height = height;
    this.x = x;
    this.y = y;
    // 克隆点击的dom
    this.cloneDiv = this.dom.cloneNode(true);
    // 将克隆的元素添加到盒子里
    this.cloneDomBox.appendChild(this.cloneDiv);
    // 初始化购物车的位置
    const oRectShop = this.shopDom.getBoundingClientRect();
    this.shopX = oRectShop.x;
    this.shopY = oRectShop.y;
  &#125;
  beforeEnter(el) &#123;
    let top = this.state ? this.y : this.shopY;
    let left = this.state ? this.x : this.shopX;
    // 动画入场前,设置元素开始动画的起始位置
    el.style.width = this.width + "px";
    el.style.height = this.height + "px";
    el.style.position = "fixed";
    el.style.left = left + "px";
    el.style.top = top + "px";
    // 动画过程禁止滚动
    document.getElementsByTagName("html")[0].style.overflowY = "hidden";
    if (!this.state) &#123;
      el.style.transform = `scale(0.1)`;
      el.style.transformOrigin = "0 0";
      this.shopDom.classList.add(this.shopAnmationClass);
    &#125;
  &#125;
  // 设置完成动画之后的结束状态
  enter(el, done) &#123;
    el.offsetWidth; // 强制刷新动画
    // 结束位置
    let enterX = this.x - this.shopX;
    let enterY = this.shopY - this.y;
    let x = this.state ? "-" + enterX : enterX;
    let y = this.state ? enterY : "-" + enterY;
    let scaleNum = this.state ? "0.1" : "1";
    el.style.transform = `translate($&#123;x&#125;px,$&#123;y&#125;px) scale($&#123;scaleNum&#125;)`;
    el.style.transformOrigin = "0 0";
    el.style.transition = "all 1s ease";
    // document.getElementsByTagName("html")[0].style.overflowY = "auto";
    // 执行done函数,完成下面钩子函数
    setTimeout(() => &#123;
      done();
    &#125;, 800);
  &#125;
  // 动画完成之后调用afterEnter函数
  afterEnter(el) &#123;
    this.shopDom.classList[this.state ? "add" : "remove"](
      this.shopAnmationClass
    );
    return new Promise(resolve => &#123;
      setTimeout(() => &#123;
        this.cloneDomBox.style = &#123;
          position: "fixed",
          "z-index": 1000,
          background: "white"
        &#125;;
        this.cloneDiv && this.cloneDiv.remove();
        this.shopDom.classList.remove(this.shopAnmationClass);
        // 动画结束允许滚动
        document.getElementsByTagName("html")[0].style.overflowY = "auto";
        resolve();
      &#125;, 500);
    &#125;);
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            