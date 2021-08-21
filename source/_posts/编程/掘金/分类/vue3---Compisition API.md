
---
title: 'vue3---Compisition API'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f198834df34b4b65809954d0895cbdcc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 04:10:16 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f198834df34b4b65809954d0895cbdcc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第19天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f198834df34b4b65809954d0895cbdcc~tplv-k3u1fbpfcp-watermark.image" alt="composition API.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">setup函数配置项</h2>
<p>setup()是 Vue3.x 新增的一个选项，setup是所有<strong>Composition API（组合API）</strong> <em>“ 表演的舞台 ”</em> , 他是组件内使用 <code>Composition API</code>的入口,组件中所用到的：<strong>数据</strong>、<strong>方法</strong>等等，均要配置在setup中。</p>
<p><strong>setup函数的两种返回值：</strong></p>
<ol>
<li>若返回一个对象，则对象中的属性、方法, 在模板中均可以直接使用。（重点关注！）</li>
<li>若返回一个渲染函数：则可以自定义渲染内容。（了解）</li>
</ol>
<p><strong>注意点：</strong></p>
<ol>
<li>
<p>尽量不要与Vue2.x配置混用</p>
<ul>
<li>Vue2.x配置（data、methos、computed...）中<strong>可以访问到</strong>setup中的属性、方法。</li>
<li>但在setup中<strong>不能访问到</strong>Vue2.x配置（data、methos、computed...）。</li>
<li>如果有重名, setup优先。</li>
</ul>
</li>
<li>
<p>setup不能是一个async函数，因为返回值不再是return的对象, 而是promise, 模板看不到return对象中的属性。（后期也可以返回一个Promise实例，但需要Suspense和异步组件的配合）</p>
</li>
<li>
<p><strong>setup执行的时机</strong></p>
<ul>
<li>在<strong>beforeCreate之前</strong>执行一次，this是undefined。</li>
</ul>
</li>
<li>
<p>setup的参数</p>
<ul>
<li>
<p><strong>props</strong>：值为对象，包含：组件外部传递过来，且组件内部声明接收了的属性。</p>
</li>
<li>
<p><strong>context</strong>：上下文对象</p>
<ul>
<li>attrs: 值为对象，包含：组件外部传递过来，但没有在props配置中声明的属性, 相当于 <code>this.$attrs</code>。</li>
<li>slots: 收到的插槽内容, 相当于 <code>this.$slots</code>。</li>
<li>emit: 分发自定义事件的函数, 相当于 <code>this.$emit</code>。</li>
</ul>
</li>
</ul>
</li>
</ol>
<h2 data-id="heading-1">ref函数</h2>
<ul>
<li>
<p>作用: 定义一个响应式的数据</p>
</li>
<li>
<p>语法: <code>const xxx = ref(initValue)</code></p>
<ul>
<li>创建一个包含响应式数据的<strong>引用对象（reference对象，简称ref对象）</strong> 。</li>
<li>JS中操作数据： <code>xxx.value</code></li>
<li>模板中读取数据: 不需要.value，直接：<code><div>&#123;&#123;xxx&#125;&#125;</div></code></li>
</ul>
</li>
<li>
<p>备注：</p>
<ul>
<li>接收的数据可以是：基本类型、也可以是对象类型。</li>
<li>基本类型的数据：响应式依然是靠<code>Object.defineProperty()</code>的<code>get</code>与<code>set</code>完成的。</li>
<li>对象类型的数据：内部 <em>“ 求助 ”</em> 了Vue3.0中的一个新函数—— <code>reactive</code>函数。</li>
</ul>
</li>
</ul>
<h2 data-id="heading-2">reactive函数</h2>
<ul>
<li>作用: 定义一个<strong>对象类型</strong>的响应式数据（基本类型不要用它，要用<code>ref</code>函数）</li>
<li>语法：<code>const 代理对象= reactive(源对象)</code>接收一个对象（或数组），返回一个<strong>代理对象（Proxy的实例对象，简称proxy对象）</strong></li>
<li>reactive定义的响应式数据是“深层次的”。</li>
<li>内部基于 ES6 的 Proxy 实现，通过代理对象操作源对象内部数据进行操作。</li>
</ul>
<h2 data-id="heading-3">reactive对比ref</h2>
<ul>
<li>
<p>从定义数据角度对比：</p>
<ul>
<li>ref用来定义：<strong>基本类型数据</strong>。</li>
<li>reactive用来定义：<strong>对象（或数组）类型数据</strong>。</li>
<li>备注：ref也可以用来定义<strong>对象（或数组）类型数据</strong>, 它内部会自动通过<code>reactive</code>转为<strong>代理对象</strong>。</li>
</ul>
</li>
<li>
<p>从原理角度对比：</p>
<ul>
<li>ref通过<code>Object.defineProperty()</code>的<code>get</code>与<code>set</code>来实现响应式（数据劫持）。</li>
<li>reactive通过使用<strong>Proxy</strong>来实现响应式（数据劫持）, 并通过<strong>Reflect</strong>操作<strong>源对象</strong>内部的数据。</li>
</ul>
</li>
<li>
<p>从使用角度对比：</p>
<ul>
<li>ref定义的数据：操作数据<strong>需要</strong><code>.value</code>，读取数据时模板中直接读取<strong>不需要</strong><code>.value</code>。</li>
<li>reactive定义的数据：操作数据与读取数据：<strong>均不需要</strong><code>.value</code>。</li>
</ul>
</li>
</ul>
<h2 data-id="heading-4">watch函数</h2>
<ul>
<li>
<p>与Vue2.x中watch配置功能一致</p>
</li>
<li>
<p>两个小“坑”：</p>
<ul>
<li>监视reactive定义的响应式数据时：oldValue无法正确获取、强制开启了深度监视（deep配置失效）。</li>
<li>监视reactive定义的响应式数据中某个属性时：deep配置有效。</li>
</ul>
<pre><code class="copyable">//情况一：监视ref定义的响应式数据
watch(sum,(newValue,oldValue)=>&#123;
    console.log('sum变化了',newValue,oldValue)
&#125;,&#123;immediate:true&#125;)
​
//情况二：监视多个ref定义的响应式数据
watch([sum,msg],(newValue,oldValue)=>&#123;
    console.log('sum或msg变化了',newValue,oldValue)
&#125;) 
​
/* 情况三：监视reactive定义的响应式数据
            若watch监视的是reactive定义的响应式数据，则无法正确获得oldValue！！
            若watch监视的是reactive定义的响应式数据，则强制开启了深度监视 
*/
watch(person,(newValue,oldValue)=>&#123;
    console.log('person变化了',newValue,oldValue)
&#125;,&#123;immediate:true,deep:false&#125;) //此处的deep配置不再奏效
​
//情况四：监视reactive定义的响应式数据中的某个属性
watch(()=>person.job,(newValue,oldValue)=>&#123;
    console.log('person的job变化了',newValue,oldValue)
&#125;,&#123;immediate:true,deep:true&#125;) 
​
//情况五：监视reactive定义的响应式数据中的某些属性
watch([()=>person.job,()=>person.name],(newValue,oldValue)=>&#123;
    console.log('person的job变化了',newValue,oldValue)
&#125;,&#123;immediate:true,deep:true&#125;)
​
//特殊情况
watch(()=>person.job,(newValue,oldValue)=>&#123;
    console.log('person的job变化了',newValue,oldValue)
&#125;,&#123;deep:true&#125;) //此处由于监视的是reactive素定义的对象中的某个属性，所以deep配置有效
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-5">watchEffect函数</h2>
<ul>
<li>
<p>watch的套路是：既要指明监视的属性，也要指明监视的回调。</p>
</li>
<li>
<p>watchEffect的套路是：不用指明监视哪个属性，监视的回调中用到哪个属性，那就监视哪个属性。</p>
</li>
<li>
<p>watchEffect有点像computed：</p>
<ul>
<li>但computed注重的计算出来的值（回调函数的返回值），所以必须要写返回值。</li>
<li>而watchEffect更注重的是过程（回调函数的函数体），所以不用写返回值。</li>
</ul>
<pre><code class="copyable">//watchEffect所指定的回调中用到的数据只要发生变化，则直接重新执行回调。
watchEffect(()=>&#123;
    const x1 = sum.value
    const x2 = person.age
    console.log('watchEffect配置的回调执行了')
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-6">toRef 把XX变成ref</h2>
<pre><code class="copyable">return &#123;
    name:toRef(person, name),
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，name就会变成ref对象，并且访问name时访问的还是源对象person.name。</p>
<ul>
<li>作用：创建一个 ref 对象，其value值指向另一个对象中的某个属性。</li>
<li>语法：<code>const name = toRef(person,'name')</code></li>
<li>应用: 要将响应式对象中的某个属性单独提供给外部使用时。</li>
</ul>

<ul>
<li>扩展：<code>toRefs</code> 与<code>toRef</code>功能一致，但可以批量创建<code>多个</code>ref 对象，语法：<code>toRefs(person)</code></li>
</ul>
<h2 data-id="heading-7">生命周期</h2>
<ul>
<li>
<p>Vue3.0中可以继续使用Vue2.x中的生命周期钩子，但有有两个被更名：</p>
<ul>
<li><code>beforeDestroy</code>改名为 <code>beforeUnmount</code></li>
<li><code>destroyed</code>改名为 <code>unmounted</code></li>
</ul>
</li>
<li>
<p>Vue3.0也提供了 Composition API 形式的生命周期钩子，与Vue2.x中钩子对应关系如下：</p>
<ul>
<li><code>beforeCreate</code>===><code>setup()</code></li>
<li><code>created</code>=======><code>setup()</code></li>
<li><code>beforeMount</code> ===><code>onBeforeMount</code></li>
<li><code>mounted</code>=======><code>onMounted</code></li>
<li><code>beforeUpdate</code>===><code>onBeforeUpdate</code></li>
<li><code>updated</code> =======><code>onUpdated</code></li>
<li><code>beforeUnmount</code> ==><code>onBeforeUnmount</code></li>
<li><code>unmounted</code> =====><code>onUnmounted</code></li>
</ul>
</li>
</ul>
<h2 data-id="heading-8">自定义hook函数</h2>
<ul>
<li>什么是hook？—— 本质是一个函数，把setup函数中使用的Composition API进行了封装。</li>
<li>类似于vue2.x中的mixin。</li>
<li>自定义hook的优势: 复用代码, 让setup中的逻辑更清楚易懂。</li>
</ul>
<h2 data-id="heading-9">参考</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1Zy4y1K7SH%3Fp%3D156%26spm_id_from%3DpageDriver" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1Zy4y1K7SH?p=156&spm_id_from=pageDriver" ref="nofollow noopener noreferrer">www.bilibili.com/video/BV1Zy…</a></p></div>  
</div>
            