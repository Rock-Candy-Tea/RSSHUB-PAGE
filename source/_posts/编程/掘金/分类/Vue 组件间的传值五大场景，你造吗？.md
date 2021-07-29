
---
title: 'Vue 组件间的传值五大场景，你造吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14223295587544239368cfdbd3c60651~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 20:06:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14223295587544239368cfdbd3c60651~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>摘要：组件是 vue.js 最强大的功能之一，这五个组件间传值场景你了解吗？</p>
</blockquote>
<p>本文分享自华为云社区<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbbs.huaweicloud.com%2Fblogs%2F286734%3Futm_source%3Djuejin%26utm_medium%3Dbbs-ex%26utm_campaign%3Dother%26utm_content%3Dcontent" target="_blank" rel="nofollow noopener noreferrer" title="https://bbs.huaweicloud.com/blogs/286734?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" ref="nofollow noopener noreferrer">《你了解Vue组件间传值五大场景吗？》</a>，作者：北极光之夜。 。</p>
<h2 data-id="heading-0">父组件向子组件传值：</h2>
<p>比如有一个 Father.vue 的父组件要传值给 Children.vue 的子组件，完成共需四步：</p>
<p><strong>父组件 Father.vue 内容，注意里面的操作步骤：</strong></p>
<pre><code class="copyable"><template>
  <div>
     <h2>父组件区域</h2>
    <hr />
    <!-- 第二步：在引用的子组件标签里定义 :num="num" , num就是要传递的变量-->
    <Children :num="num"></Children>
  </div>
</template>


<script>
// 引入子组件
import Children from "./Children.vue";
export default &#123;
  data() &#123;
    return &#123;
      // 第一步：我们将要把变量 num 的值传给子组件Children
      num: 666,
    &#125;;
  &#125;,
  components: &#123;
    Children,
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>子组件 Children.vue 内容，注意里面的操作步骤：</strong></p>
<pre><code class="copyable"><template>
  <div>
    <h2>子组件区域</h2>
    <!-- 第四步：在子组件显示父组件传过来的值 -->
    <i>父组件传递过了的值:&#123;&#123; num &#125;&#125;</i>
  </div>
</template>
<script>
export default &#123;
  //第三步： 子组件可以通过定义的props就可以接收来自父组件的变量值 num
  props: ["num"],
  data() &#123;
    return &#123;&#125;;
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>运行效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14223295587544239368cfdbd3c60651~tplv-k3u1fbpfcp-zoom-1.image" alt="Vue组件间的传值五大场景，你造吗？" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">子组件向父组件传值：</h2>
<p>比如有一个 Children.vue 的子组件要传值给 Father.vue 的父组件，完成共需六步：</p>
<p><strong>子组件 Children.vue 内容，注意里面的操作步骤：</strong></p>
<pre><code class="copyable"><template>
  <div>
    <h2>子组件区域</h2>
    <!-- 第二步：得定义一个向父组件传值的方法，比如定义一个按钮，
    绑定一个点击事件，触发giveFather方法 -->
    <button @click="giveFather">giveFather</button>
  </div>
</template>
<script>
export default &#123;
  data() &#123;
    return &#123;
      // 第一步：我们将要把变量 word 的值传给父组件
      word: "北极光之夜。",
    &#125;;
  &#125;,
  methods: &#123;
    // 第三：定义子组件向父组件传值的事件方法
    giveFather() &#123;
      // 第四步：可以通过$emit传值给父组件,第一个参数为传值的方法，第二个参数为要传递的值
      this.$emit("giveFather", this.word);
    &#125;,
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>父组件 Father.vue 内容，注意里面的操作步骤：</strong></p>
<pre><code class="copyable"><template>
  <div>
    <h2>父组件区域</h2>
    <hr />
    <!-- 第五步：要在引用的子组件标签里定义一个自定义事件，
    该自定义事件要写为子组件$emit的第一个参数一样,
    然后双引号里的方法可以自定义，我这就为getSon -->
    <Children @giveFather="getSon"></Children>
  </div>
</template>


<script>
// 引入子组件
import Children from "./Children.vue";


export default &#123;
  data() &#123;
    return &#123;&#125;;
  &#125;,
  components: &#123;
    Children,
  &#125;,
  methods: &#123;
    //第六步：定义获取子组件值的方法，该方法的参数就为子组件传递过来的值
    getSon(temp) &#123;
      // 控制台输出看看能不能获取
      console.log(temp);
    &#125;,
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>运行效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e39377d794e44ee6a45398b17d61865f~tplv-k3u1fbpfcp-zoom-1.image" alt="Vue组件间的传值五大场景，你造吗？" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">兄弟组件间传值：</h2>
<p>比如有一个 Father.vue 的父组件，它有一个 Children.vue 的子组件和一个 Son.vue 的子组件，那么，Children.vue 和 Son.vue 就是兄弟关系，现在 Children.vue 要向兄弟 Son.vue 传值：</p>
<p><strong>首先在 vue 原型上定义一个新的实例，main.js 文件内容，注意里面的操作步骤：</strong></p>
<pre><code class="copyable">import Vue from 'vue'
import App from './App.vue'


Vue.config.productionTip = false


// 第一步，在vue原型上定义一个自己的方法，一般叫$bus，为vue实例
Vue.prototype.$bus = new Vue();


new Vue(&#123;
  render: h => h(App),
&#125;).$mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Children.vue 内容，注意里面的操作步骤：</strong></p>
<pre><code class="copyable"><template>
  <div>
    <h2>Children子组件区域</h2>
    <!-- 第三步：定义一个向兄弟组件传值的方法，比如定义一个按钮，
    绑定一个点击事件，触发giveSon方法 -->
    <button @click="giveSon">giveSon</button>
  </div>
</template>
<script>
export default &#123;
  data() &#123;
    return &#123;
      // 第二步：我们将要把变量 word 的值传给兄弟组件
      word: "北极光之夜。",
    &#125;;
  &#125;,
  methods: &#123;
    // 第四：定义子组件向兄弟组件传值的事件方法
    giveSon() &#123;
      // 第五步：可以通过自定义的$bus的$emit传值给兄弟组件,
      //第一个参数为传值的方法，第二个参数为要传递的值
      this.$bus.$emit("giveSon", this.word);
    &#125;,
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Son.vue 内容，注意里面的操作步骤：</strong></p>
<pre><code class="copyable"><template>
  <div>
    <h2>Son子组件区域</h2>
  </div>
</template>
<script>
export default &#123;
  data() &#123;
    return &#123;&#125;;
  &#125;,
  created() &#123;
    //第六步：通过$on方法进行获取兄弟传递过来的值。
    //第一个参数为兄弟组件传值的方法，第二个参数是自定义的方法
    this.$bus.$on("giveSon", this.getSon);
  &#125;,
  methods: &#123;
    //第七步，自定义的方法,参数就是兄弟传过来的值
    getSon(temp) &#123;
      //输出看看
      console.log(temp);
    &#125;,
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>运行效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b787be772ef341379c89fb44304024b4~tplv-k3u1fbpfcp-zoom-1.image" alt="Vue组件间的传值五大场景，你造吗？" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总结就是，在 vue 原型上定义一个新的实例，然后采用 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi><mi>m</mi><mi>i</mi><mi>t</mi><mtext>和</mtext></mrow><annotation encoding="application/x-tex">emit 和</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal">e</span><span class="mord mathnormal">m</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span><span class="mord cjk_fallback">和</span></span></span></span></span> on 这两个方法进行获取传递过来的值。</p>
<h2 data-id="heading-3">使用 Vuex 状态机传值：</h2>
<p>Vuex 是实现组件全局状态(数据)管理的一种机制，可以很方便的实现组件之间数据的共享。关于 Vuex 的详细使用，可以看这篇文章，指路：<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fauroras.blog.csdn.net%2Farticle%2Fdetails%2F117536679" target="_blank" rel="nofollow noopener noreferrer" title="https://auroras.blog.csdn.net/article/details/117536679" ref="nofollow noopener noreferrer">auroras.blog.csdn.net/article/det…</a></p>
<h2 data-id="heading-4">给后代组件传值，provide 和 inject：</h2>
<p>比如有一个 Father.vue 的父组件，它有一个 Children.vue 的子组件，那么这个 Children.vue 的子组件是他的后代。而若 Children.vue 也有一个子组件 grandSon.vue，那么 grandSon.vue 就相当于 Father.vue 的孙子组件，同样，grandSon.vue 也会是 Father.vue 的后代。以此类推，它的孙子，孙子的孙子等等都是它后代。现在我们实现 Father.vue 给它的后代 grandSon.vue 孙子组件传值：</p>
<p><strong>父组件 Father.vue 内容，注意里面的操作步骤：</strong></p>
<pre><code class="copyable"><template>
  <div>
    <h2>父组件区域</h2>
    <hr />
    <Children></Children>
  </div>
</template>


<script>
// 引入子组件
import Children from "./Children.vue";
export default &#123;
  data() &#123;
    return &#123;
      // 第一步：定义一个变量，我们将要把变量 num 的值传给后代组件grandSon.vue
      num: "北极光之夜",
    &#125;;
  &#125;,
  // 第二步，定义一个provide函数
  provide() &#123;
    //第三步，如下定义，给后代接收
    //giveAfter名称为自己定义，任意起，this固定写法
    return &#123;
      giveAfter: this,
    &#125;;
  &#125;,
  components: &#123;
    Children,
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>子组件 Children.vue 内容，没什么，引入子组件就行：</strong></p>
<pre><code class="copyable"><template>
  <div>
    <h2>
      Children子组件区域
      <hr />
      <Grand-son></Grand-son>
    </h2>
  </div>
</template>
<script>
// 引入子组件
import GrandSon from "./GrandSon.vue";
export default &#123;
  data() &#123;
    return &#123;&#125;;
  &#125;,


  components: &#123;
    GrandSon,
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>孙子组件 GrandSon.vue 内容，注意里面的操作步骤：</strong></p>
<pre><code class="copyable"> <template>
  <div>
    GrandSon孙子组件区域
    <!-- 第六步：展示数据 -->
    <i> &#123;&#123; num &#125;&#125;</i>
  </div>
</template>
<script>
export default &#123;
  //第四步：定义inject,里面写祖先组件自定义的名称
  inject: ["giveAfter"],
  data() &#123;
    return &#123;
      // 第五步：取得祖先组件传的值，this.giveAfter.要传递值的变量名
      //赋值给num
      num: this.giveAfter.num,
    &#125;;
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>看运行效果，成功获取：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f675ee4810841d19efcfae0c4d783ed~tplv-k3u1fbpfcp-zoom-1.image" alt="Vue组件间的传值五大场景，你造吗？" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbbs.huaweicloud.com%2Fblogs%3Futm_source%3Djuejin%26utm_medium%3Dbbs-ex%26utm_campaign%3Dother%26utm_content%3Dcontent" target="_blank" rel="nofollow noopener noreferrer" title="https://bbs.huaweicloud.com/blogs?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" ref="nofollow noopener noreferrer">点击关注，第一时间了解华为云新鲜技术~</a></p></div>  
</div>
            