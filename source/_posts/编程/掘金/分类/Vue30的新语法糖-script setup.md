
---
title: 'Vue3.0的新语法糖-script setup'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: './assets/logo.png'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 04:32:33 GMT
thumbnail: './assets/logo.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">vue3.0的语法糖 script setup</h3>
<p>写在前面</p>
<p>进入vue3.0 我们的vue代码模板格式也发生变化 也许你看到的代码是这样的</p>
<pre><code class="copyable"><template>
  <div>
​
  </div>
</template>
​
<script lang="ts">
import &#123; defineComponent &#125; from 'vue'
​
export default defineComponent(&#123;
  setup () &#123;
    
​
    return &#123;&#125;
  &#125;
&#125;)
</script>
​
<style scoped>
​
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是每次 都要 import defineComponent 然后再去 export 让我们由衷感到苦恼 苦恼 vue3.0的写法貌似变复杂了很多</p>
<p>于是 它来了</p>
<pre><code class="copyable"><template>
  <div>
​
  </div>
</template>
​
<script setup lang="ts">
​
</script>
​
<style scoped>
​
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是感觉 巴适很多 当然以上只是一个对比 我们该如何使用呢 来来来 往下看</p>
<ol>
<li>
<p><strong>基本用法</strong></p>
<p>在Conponents目录下，新建一个msg.vue</p>
<pre><code class="copyable"><template>
  <div>
    &#123;&#123; msg &#125;&#125;
  </div>
</template>
​
<script setup>
  let msg = "hello!"
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二件事我们就是在父组件中引用它</p>
<pre><code class="copyable"><template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="Hello Vue 3.0 + Vite" />
  <msg></msg>
</template>
​
<script setup>
import HelloWorld from './components/HelloWorld.vue'
import msg from "./components/msg.vue"
​
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到 这个父组件中 直接import 就行啦 啥都不用干 就连vue2.0中的 也不需要了</p>
<pre><code class="copyable">components:&#123;
   msg
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再也不用担心 组件引用了 没有挂到components 中了</p>
</li>
<li>
<p><strong>props和emit</strong></p>
<p><strong>因为3.0中 我们的思想都是 先import 再使用 并非一次性把所有api 都全部加载了 所以 用props 和emit 也是一样的啦 用前先引用</strong></p>
<p>需要先去引入defineProps和defineEmit。这样引入是因为用了script setup标签，就相当于props和emit</p>
<pre><code class="copyable"><template>
  <div>
    &#123;&#123; msg &#125;&#125;
    <button @click="onClick">点击按钮</button>
  </div>
</template>
​
<script setup>
import &#123; defineProps, defineEmit &#125; from "vue";// props emit
let props = defineProps(&#123;
  msg: String,
&#125;);
console.log(props);
​
let emit = defineEmit(["click"]);
const onClick = () => &#123;
  emit("click");
console.log("click。。。");
​
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>app,vue中</p>
<pre><code class="copyable"><template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="Hello Vue 3.0 + Vite" />
  <msg msg="天气很好" @click="onClick"></msg>
</template>
​
<script setup>
import HelloWorld from './components/HelloWorld.vue'
import msg from "./components/msg.vue"
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>嗯.... 香y</p>
<p>原文借鉴于:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fsunqiaozhen%2Fp%2F14512943.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/sunqiaozhen/p/14512943.html" ref="nofollow noopener noreferrer">小兔儿_乖乖 的vue3.0的新语法糖-script setup</a></p>
<p>如有侵权 麻烦联系作者删除</p>
<p>\</p>
</li>
</ol></div>  
</div>
            