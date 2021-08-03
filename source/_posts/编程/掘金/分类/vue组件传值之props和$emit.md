
---
title: 'vue组件传值之props和$emit'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/651be4f7e88942549c22361dad056f60~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 05:06:09 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/651be4f7e88942549c22361dad056f60~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">vue组件传值之<code>Props</code>和<code>$emit</code></h1>
<h2 data-id="heading-1">前言</h2>
<p>上次我们谈了<code>$refs</code>和<code>$parent</code>传值，发完之后我发现还有种传值方式<code>$attrs</code>和<code>$listeners</code>，小Q可能一时间想不起来那么多，希望大家见谅，有错误的地方也欢迎大家指正😁</p>
<p>今天我们就来说说目前比较常用<code>props</code>和<code>$emit</code>😎</p>
<h2 data-id="heading-2">正文</h2>
<p>首先<code>props</code>是什么？怎么用？我们来看官方文档</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/651be4f7e88942549c22361dad056f60~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有小伙伴说这个解释看不懂啊，简单来说就是组件间传值，我们再来看官方文档传值的方法</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2811b14bc23e41b2ba34598c927b7490~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>很显然，可以传数组和对象嘛，但是这里小Q要说一下，数组方式目前已经不推荐了，尽量少用</p>
<p>那这玩意到底怎么用呢，废话不多说上码</p>
<pre><code class="copyable"><template>
  <div class="father">
    <h2>父组件</h2>
    <!-- 01.基本使用 -->
    <son info="你好吗?" skill="不,我不好" food="吃西兰花可以平复心情哦"></son>
  </div>
</template>

<script>
// 导入子组件
import son from './components/01.son.vue'
export default &#123;
// 注册子组件
  components: &#123;
    son
  &#125;
&#125;
</script>

<style>
body &#123;
  margin: 0;
&#125;
.father &#123;
  height: 100vh;
  background-color: skyblue;
  /* 去除 因为h2 造成的塌陷 */
  overflow: hidden;
&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><template>
  <div class="son">
    <h3>子组件</h3>
    <p>&#123;&#123; info &#125;&#125;</p>
  </div>
</template>

<script>
export default &#123;
  name: 'son',
  // 定义props 数组 基本用法
  props: ['info', 'skill', 'food']
&#125;
</script>

<style>
.son &#123;
  border: 3px solid hotpink;
  width: 300px;
  height: 300px;
  background-color: orange;
&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种是简单的父组件传值给子组件父组件中的值要与<code>props</code>中的值要相对应，不然无法取到，那么对象用法怎么用呢？</p>
<p>对象的用法相比于数组的用法多了类型校验</p>
<pre><code class="copyable"><template>
  <div class="son">
    <h3>子组件</h3>
    <p>&#123;&#123; info &#125;&#125;</p>
  </div>
</template>

<script>
export default &#123;
  name: 'son',
  props: &#123;
    info: &#123;
      // 类型
      type: String,
      // 默认值
      default: '喜洋洋,美羊羊'
    &#125;,
    food: &#123;
      type: String,
      // 必填项
      required: true,
      validator (value) &#123;
        // console.log('value:', value)
        // 返回 true 成功 false 失败
        // return false
        // 必须传
        const res = ['鲱鱼罐头', '黑蒜', '榴莲', '逆风十里臭豆腐'].includes(
          value
        )
        // 存在 true 反之就是false
        return res
      &#125;
    &#125;
  &#125;
&#125;
</script>

<style>
.son &#123;
  border: 3px solid hotpink;
  width: 300px;
  height: 300px;
  background-color: orange;
&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>type</code>是定义类型，<code>常见的</code>有(<code>Number</code>,<code>String</code>,<code>Boolean</code>,<code>Array</code>,<code>Object</code>)</p>
<p><code>required</code>是否必填 <code>validator</code>是自定义验证函数</p>
<h3 data-id="heading-3">小Q提醒大家子组件中获取过来的值不建议去修改（虽然可以修改）因为子组件中的值是父组件流过来的，如果子组件修改了值，父组件中出现了数据变化，子组件中的值也会随之改变（单项数流）</h3>
<h2 data-id="heading-4"><code>$emit</code>使用：</h2>
<p>子组件：</p>
<ol>
<li>
<p>子组件这次叫做<code>emit-use</code></p>
</li>
<li>
<p>通过<code>$emit('事件名')</code>，触发事件</p>
</li>
<li>
<p>事件名可以随便写，有意义即可</p>
</li>
</ol>
<pre><code class="copyable"><template>
  <div class="emit-container">
      <input @click="add" type="button" value="点击累加">
  </div>
</template>

<script>
  export default &#123;
    name: 'emit-use',
    methods:&#123;
        add()&#123;
            // 触发add事件
            this.$emit('add')
        &#125;
    &#125;
  &#125;
</script>

<style></style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件:</p>
<ol>
<li>
<p>注册并实现add事件</p>
</li>
<li>
<p>可以实现一个计数功能</p>
</li>
</ol>
<pre><code class="copyable"><template>
  <div>
    <!-- emit基本使用 -->
    <h2>你点了:&#123;&#123; num &#125;&#125; 次</h2>
    <emit-use @add="fatherAdd"></emit-use>
  </div>
</template>

<script>
  export default &#123;
    data() &#123;
      return &#123;
        num:0
      &#125;
    &#125;,
    methods:&#123;
      fatherAdd()&#123;
        console.log('fatherAdd')
        this.num++
      &#125;
    &#125;
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">有的时候，我们不仅仅要触发事件，还需要传递自定义的参数，只需要在<code>emit</code>方法的后面依次写上需要的参数即可</h3>
<p>语法：<code>emit('事件名',参数1,参数2....)</code></p>
<p>子组件:</p>
<ol>
<li>
<p>子组件这次叫做<code>emit-param</code></p>
</li>
<li>
<p>子组件中通过双击事件来触发<code>emit</code></p>
</li>
<li>
<p>同时传递数据</p>
</li>
</ol>
<pre><code class="copyable"><template>
  <div class="emit-container">
      <input @dblclick="add" type="button" value="双击加2">
  </div>
</template>

<script>
  export default &#123;
    name: 'emit-param',
    methods:&#123;
        add()&#123;
          // 触发add事件，同时传递参数
            this.$emit('add',2)
        &#125;
    &#125;
  &#125;
</script>

<style></style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件</p>
<ol>
<li>
<p>注册事件，并定义参数</p>
</li>
<li>
<p>获取并使用参数</p>
</li>
<li>
<p>这里为了对比，上一步不传递数据的组件也一起保留作为对比</p>
</li>
<li>
<p>点击第一个组件，一次加1</p>
</li>
<li>
<p>双击第二个组件，一次加2</p>
</li>
</ol>
<pre><code class="copyable"><template>
  <div>
    <!-- emit传递参数 -->
    <h2>你点了:&#123;&#123; num &#125;&#125; 次</h2>
    <!-- 不传递参数 -->
    <emit-use @add="fatherAdd"></emit-use>
    <!-- 传递参数 -->
    <emit-param @add="fatherAdd"></emit-param>
  </div>
</template>

<script>
  export default &#123;
    data() &#123;
      return &#123;
        num: 0
      &#125;
    &#125;,
    methods: &#123;
      fatherAdd(num) &#123;
        console.log('fatherAdd')
        console.log(`num:$&#123;num&#125;`)
        // 如果有参数，获取并累加
        if(num)&#123;
          this.num+=num
        &#125;else&#123;
          // 如果没有参数，累加1
          this.num++
        &#125;
      &#125;
    &#125;
  &#125;
</script>

<style></style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意:</p>
<ol>
<li>
<p>如果要传递多个参数，用逗号分隔，继续向后写</p>
</li>
<li>
<p>父组件注册事件时，也定义对应个参数即可</p>
</li>
<li>
<p>如果不想挨个传递，可以把多个数据放到一个对象中，也是可以的</p>
</li>
</ol>
<h2 data-id="heading-6">END</h2>
<p>这就是<code>props</code>和<code>$emit</code>的使用了，多在测试代码中摸索，找到属于自己的理解方式，这样对这种传值的方法理解能更深一些。如果有什么问题可以直接私我，欢迎大家和我一块学习进步。</p>
<h4 data-id="heading-7">我是还在学习的前端小Q😘</h4></div>  
</div>
            