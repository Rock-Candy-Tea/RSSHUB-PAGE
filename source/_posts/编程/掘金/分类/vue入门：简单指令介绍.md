
---
title: 'vue入门：简单指令介绍'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1674'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 16:15:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=1674'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 11 天，活动详情查看： 8月更文挑战</p>
<h2 data-id="heading-0">1.为什么使用vue</h2>
<ul>
<li>业务越来越复杂，更多操作在前段进行。</li>
<li>渐进式</li>
<li>不需要操作dom</li>
<li>双向绑定</li>
<li>环境构建方便</li>
<li>组件开发</li>
<li>社区活跃</li>
</ul>
<h2 data-id="heading-1">2.vue入口</h2>
<p>main.js为主入口</p>
<pre><code class="copyable">import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue(&#123;
  el: '#app',
  router,
  components: &#123; App &#125;, //指定进入app.vue
  template: '<App/>'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3.基本指令</h2>
<h3 data-id="heading-3">1.&#123;&#123;&#125;&#125;与v-html</h3>
<p>用于打印与输出。</p>
<pre><code class="copyable"><template>
<div>
<!-- 表达式 -->
<p>&#123;&#123;1+1>1 ? '是':'否'&#125;&#125;</p>
&#123;&#123;msg&#125;&#125;
<div v-html = "msg"></div>
</div>
</template>

<script>
export default &#123;
name: 'HelloWorld',
el: '#app',

data () &#123;
  return &#123;
    msg:'<h1>我是消息</h1>'
&#125;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2.v-bind</h3>
<p>v-bind就是<strong>用于绑定数据和元素属性的</strong>。</p>
<pre><code class="copyable"><template>
<div v-bind:class = "active" v-bind:id=id>
&#123;&#123;msg&#125;&#125;  
</div>
</template>

<script>
export default &#123;
name: 'HelloWorld',
el: '#app',
data () &#123;
  return &#123;
    msg:'<h1>我是消息</h1>',
    active:"active",
    id:19
&#125;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">3.class与style</h3>
<p>class的绑定方式。</p>
<pre><code class="copyable"><template>
<div>
<p v-bind:class="&#123; active: isActive &#125;" v-bind:id=id>aaa</p>
<p v-bind:class="&#123; active: 10>1?true:false,test:true &#125;" >bbb</p>
<p v-bind:class='[msg]' >ccc</p>
<p v-bind:class="[&#123;active :0 > 1&#125;,'test']" >ddd</p>
<ul>
<li v-bind:class ="[&#123;active :index/2==0&#125;,'test']" v-for = "(item,index) in names">
&#123;&#123;item.name&#125;&#125;
</li>
</ul>
<p v-bind:style="&#123;color: activeColor, fontSize: fontSize + 'px' &#125;">eee</p>
</div>
</template>

<script>
export default &#123;
name: 'HelloWorld',
el: '#app',
data () &#123;
  return &#123;
    msg:'<h1>我是消息</h1>',
    isActive:false,
    names:[&#123;
      name:"aaa"
    &#125;,&#123;
      name:"bbb"
    &#125;,&#123;
      name:"ccc"
    &#125;],
    activeColor: 'red',
    fontSize: 30
&#125;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">4.观察指令method和computed</h3>
<p><strong>method和computed区别：</strong></p>
<p>我们可以将同一函数定义为一个方法而不是一个计算属性。两种方式的最终结果确实是完全相同的。然而，不同的是<strong>计算属性是基于它们的响应式依赖进行缓存的</strong>。只在相关响应式依赖发生改变时它们才会重新求值。这就意味着只要 <code>msg</code>还没有发生改变，多次访问 <code>showMessage</code>计算属性会立即返回之前的计算结果，而不必再次执行函数。</p>
<p>函数执行需要 数据属性里面的 message 值作为参数。</p>
<p>● 如果使用 methods 执行函数，vue 每次都要重新执行一次函数，不管msg的值是否有变化；</p>
<p>● 如果使用computed 执行函数，只有当msg这个最初的数据发生变化时，函数才会被执行。（依赖-监测数据变化） </p>
<pre><code class="copyable"><template>
<div id="example">
  &#123;&#123; msg.split('').reverse().join('') &#125;&#125;
  &#123;&#123; showMessage&#125;&#125;
</div>
</template>

<script>
export default &#123;
name: 'HelloWorld',
el: '#app',
data () &#123;
  return &#123;
    msg:'我是消息'
&#125;
&#125;,
computed: &#123;
  showMessage()&#123;
    return this.msg.split('').reverse().join('')
  &#125;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">5.条件渲染</h3>
<p>v-if,v-else顾名思义，判断是否可以显示。</p>
<pre><code class="copyable"><template>
<div >
<p v-if="sign">1111</p>
<p v-else>2222</p>
</div>
</template>

<script>
export default &#123;
name: 'HelloWorld',
el: '#app',
data () &#123;
  return &#123;
    sign:true,
    msg:'<h1>我是消息</h1>',
    active:"active",
    id:19
&#125;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>v-if：每次都会重新删除或创建元素，具有较高的切换性能消耗；</li>
<li>v-show：每次切换元素的 display：none 样式，具有较高的初始渲染消耗。</li>
<li>v-show只编译一次，后面其实就是控制css，而v-if不停的销毁和创建，故v-show性能更好一点。</li>
</ul>
<pre><code class="copyable"><template>
<div >
<p v-show="sign">1111</p>
</div>
</template>

<script>
export default &#123;
name: 'HelloWorld',
el: '#app',
data () &#123;
  return &#123;
    sign:true,
    msg:'<h1>我是消息</h1>',
    active:"active",
    id:19
&#125;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">6.列表输出</h3>
<p>v-for用于循环列表。</p>
<pre><code class="copyable"><template>
<div >
<ul>
<li v-bind:key ="index" v-for = "(item,key,index) in names">
&#123;&#123;item.age&#125;&#125;-&#123;&#123;item.name&#125;&#125;-&#123;&#123;index&#125;&#125;||&#123;&#123;item&#125;&#125;||&#123;&#123;key&#125;&#125;
</li>
</ul>
</div>
</template>

<script>
export default &#123;
name: 'HelloWorld',
el: '#app',
data () &#123;
  return &#123;
    sign:true,
    msg:'<h1>我是消息</h1>',
    names:[&#123;
      name:"aaa",
      age:19,
      sex:"1"
    &#125;,&#123;
      name:"bbb",
      age:20,
      sex:"1"
    &#125;,&#123;
      name:"ccc",
      age:21,
      sex:"1"
    &#125;]
&#125;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">7.数组更新</h3>
<p>注意：<code>filter()</code>、<code>concat()</code> 和 <code>slice()不发生更新</code>。</p>
<pre><code class="copyable"><template>
<div >
<ul>
<li v-bind:key ="index" v-for = "item in names">
&#123;&#123;item.name&#125;&#125;
</li>
</ul>
<button v-on:click = "clickbutton" name = "button" type = "button">按钮</button>
</div>
</template>

<script>
export default &#123;
name: 'HelloWorld',
el: '#app',
data () &#123;
  return &#123;
    sign:true,
    msg:'<h1>我是消息</h1>',
    names:[&#123;
      name:"aaa"
    &#125;,&#123;
      name:"bbb"
    &#125;,&#123;
      name:"ccc"
    &#125;]
&#125;
&#125;,
methods: &#123;
  clickbutton(event)&#123;
        this.names.push(&#123;name:"ddd"&#125;)
  &#125;
&#125;,
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">8.事件处理</h3>
<p>v-on：当执行xx动作时执行xx函数。</p>
<pre><code class="copyable"><template>
<div>
<button v-on:click = "count +=1" type = "button" name = "button">按钮</button>
<p>&#123;&#123;count&#125;&#125;</p>
<button v-on:click = "clickhandle" type = "button" name = "button">按钮2</button>
<p>&#123;&#123;demoshow&#125;&#125;</p>
<button v-on:click = "chance" type = "button" name = "button">按钮3</button>
<button v-on:click.once = "senddate('你好',$event)" type = "button" name = "button">按钮4</button>
</div>
</template>

<script>
export default &#123;
name: 'HelloWorld',
el: '#app',
data () &#123;
  return &#123;
    count:1,
    demoshow:"帅小伙"
&#125;
&#125;,
methods: &#123;
  clickhandle(event)&#123;
    console.log("触发")
  &#125;,
  chance(event)&#123;
    this.demoshow = "我不是帅小伙"
  &#125;,
  senddate(data,event)&#123;
    console.log(data,event)
  &#125;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">9.事件修饰</h3>
<pre><code class="copyable"><!-- 阻止单击事件继续传播 -->
<a v-on:click.stop="doThis"></a>

<!-- 提交事件不再重载页面 -->
<form v-on:submit.prevent="onSubmit"></form>

<!-- 修饰符可以串联 -->
<a v-on:click.stop.prevent="doThat"></a>

<!-- 只有修饰符 -->
<form v-on:submit.prevent></form>

<!-- 添加事件监听器时使用事件捕获模式 -->
<!-- 即内部元素触发的事件先在此处理，然后才交由内部元素进行处理 -->
<div v-on:click.capture="doThis">...</div>

<!-- 只当在 event.target 是当前元素自身时触发处理函数 -->
<!-- 即事件不是从内部元素触发的 -->
<div v-on:click.self="doThat">...</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">10.键盘事件</h3>
<pre><code class="copyable"><template>
<div>
<input  v-on:keyup.enter = "showlog" name = "button">输入框</button>
</div>
</template>
<script>
export default &#123;
name: 'HelloWorld',
el: '#app',
data () &#123;
  return &#123;
    count:1
&#125;
&#125;,
methods: &#123;
  showlog(event)&#123;
     console.log(event)
  &#125;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其余键盘操作介绍：</p>
<pre><code class="copyable">.enter
.tab
.delete (捕获“删除”和“退格”键)
.esc
.space
.up
.down
.left
.right
.ctrl
.alt
.shift
.meta 
等 请参考文档
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">11.表单输入</h3>
<p>双向数据绑定指令lazy，number，trim。</p>
<pre><code class="copyable"><template>
<div>
<input v-model.lazy="message" placeholder="edit me">
<p>Message is: &#123;&#123; message &#125;&#125;</p>
<button v-on:click = "getMsg" type = "button" name = "button">按钮</button>
</div>
</template>
<script>
export default &#123;
name: 'HelloWorld',
el: '#app',
data () &#123;
  return &#123;
    message:"这是一个消息"
&#125;
&#125;,
methods: &#123;
  getMsg(event)&#123;
     console.log(this.message)
  &#125;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">.lazy
在默认情况下，v-model 在每次 input 事件触发后将输入框的值与数据进行同步 (除了上述输入法组合文字时)。你可以添加 lazy 修饰符，从而转变为使用 change 事件进行同步：
<!-- 在“change”时而非“input”时更新 -->
<input v-model.lazy="msg" >

.number
如果想自动将用户的输入值转为数值类型，可以给 v-model 添加 number 修饰符：
<input v-model.number="age" type="number">
这通常很有用，因为即使在 type="number" 时，HTML 输入元素的值也总会返回字符串。如果这个值无法被 parseFloat() 解析，则会返回原始的值。


.trim
如果要自动过滤用户输入的首尾空白字符，可以给 v-model 添加 trim 修饰符：
<input v-model.trim="msg">
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            