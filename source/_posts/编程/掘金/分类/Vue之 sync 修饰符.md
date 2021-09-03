
---
title: 'Vue之 .sync 修饰符'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5352'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 22:43:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=5352'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>.sync修饰符可以实现子组件与父组件的双向绑定，并且可以实现子组件同步修改父组件的值。</strong></p>
<p>利用EventBus，子组件触发事件，父组件响应事件并实现数据的更新，避免由子组件直接修改父组件传过来的内容。</p>
<p>举个例子：假如父亲有1000元，儿子想要用这些钱，就需要<strong>告诉</strong>他的父亲，然后父亲同意后，从父亲那边拿钱给儿子使用，如果没有事先通知就使用，就相当于偷钱，显然不对。</p>
<p>其实父子组件传值的过程等同于是父亲告诉儿子，我有这么些个钱可以用，不是让子组件直接操作这个值。你要用多少，告诉我，然后把用完后会剩余多少告诉我就可以了。</p>
<p>搞清楚了这个逻辑，那么来看一个例子：</p>
<blockquote>
<p><strong>child.vue(子组件)</strong></p>
</blockquote>
<pre><code class="copyable"><template>
  <div class="child">
    &#123;&#123;money&#125;&#125;
    <!-- 我要用100 -->
    <button @click="$emit('update:money', money-100)">
      <span>花钱</span>
    </button>
  </div>
</template>

<script>
export default &#123;
  props: ["money"]
&#125;;
</script>

<style>
.child &#123;
  border: 3px solid green;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>parent.vue(父组件)</strong></p>
</blockquote>
<pre><code class="copyable"><template>
  <div class="app">
    App.vue 我现在有 &#123;&#123;total&#125;&#125;
    <hr>
    <!-- 语法糖式写法 -->
    <!-- <Child :money.sync="total"/> -->
    <Child :money="total" v-on:update:money="total = $event"/>
  </div>
</template>

<script>
import Child from "./Child.vue";
export default &#123;
  data() &#123;
    return &#123; total: 10000 &#125;;
  &#125;,
  components: &#123; Child: Child &#125;
&#125;;
</script>

<style>
.app &#123;
  border: 3px solid red;
  padding: 10px;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个代码就是上述内容的解释，实现的原理是利用eventBus，在子组件使用<code>$emit('update:money', money-100)</code> 来通知父组件去响应，而父组件则通过<code>$event</code> 来接收经过子组件修改后的值。</p>
<pre><code class="copyable"><Child :money="total" v-on:update:money="total = $event"/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这么长的语句得以缩写为：</p>
<pre><code class="copyable"> <Child :money.sync="total"/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而子组件内也必须用<code>'update:money'</code>事件名去触发响应</p>
<pre><code class="copyable"><button @click="$emit('update:money', money-100)">
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            