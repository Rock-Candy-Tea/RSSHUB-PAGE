
---
title: '以前我没得选，现在我想学点Vue3...'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aab8b853fa3546feac5ee10d471550ea~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 19:38:11 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aab8b853fa3546feac5ee10d471550ea~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">完美的Vue实践项目是怎样的？</h2>
<ul>
<li>数据的展示 —— 最好是有多级复杂数据的展示</li>
<li>数据的创建 —— 可以发散出多个功能</li>
<li>组件的抽象 —— 循环渐进的组件开发</li>
<li>整体状态数据结构的设计和实现</li>
<li>权限管理和控制</li>
<li>真实的后端API</li>
</ul>
<h2 data-id="heading-1">本地环境</h2>
<ul>
<li>node -v v10.15.3 >9</li>
<li>npm -v 6.14.9 >6</li>
<li>vue -V @vue/cli 4.5.9 >4.5 不够的要升级</li>
</ul>
<h2 data-id="heading-2">开发步骤</h2>
<ol>
<li>安装node</li>
<li>vue-cli npm install -g @vue/cli</li>
<li>vue create 项目名</li>
</ol>
<h3 data-id="heading-3">相关配置</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aab8b853fa3546feac5ee10d471550ea~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>npm run serve启动</li>
<li>推荐插件：eslint、vetur</li>
<li>eslint不生效：可以在settings.json设置</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c641c8acdfd444b5a5ea1ecc4ce3e8e8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>假如启动报错：cannot find module 'fork-ts-checker-webpack-plugin-v5'或者其他，网上方案都是一堆卸载重装，压根没用，试试下面这种：</code></p>
<blockquote>
<p><del>解决方法：删除package-lock.json -> npm i --save -> npm run serve</del></p>
</blockquote>
<h2 data-id="heading-4">相关知识点</h2>
<p><code>import &#123; ref, computed, ... &#125; from 'vue'</code></p>
<p><code>setup（）&#123;&#125;</code> :</p>
<pre><code class="copyable">逻辑处理和生命周期一般都在这里写，很重要。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">Composition-Api</h3>
<pre><code class="copyable">一组低侵入式的、函数式的 API，使得我们能够更灵活地「组合」组件的逻辑。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adc787e043a2487baa8a5bf67b7a3ec6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>ref: 转换响应式API（原始类型）</code></p>
<pre><code class="copyable">const count = ref(0)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>computed: 计算属性API，相当于vue2中的computed计算属性</code></p>
<p><code>reactive: 转换响应式API（复杂类型或者原始类型），可代替ref，但是记得用toRefs代替</code></p>
<pre><code class="copyable">const data: DataProps = reactive(&#123;

    conunt: 0

&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>注意点:</code>
当用reactive使用, return出去，html写法比较麻烦，需要data.a 这种形式，想要直接a这种形式，需要...扩展运算符，但是会出现一个问题：将值从响应式对象中取出来，属性会失去响应式。因此需要用到<code>toRefs</code></p>
</blockquote>
<p><code>toRefs：搭配reactive，将reactive()创建出来的响应式对象转换成普通对象，只不过这个对象上的每一个属性节点，都是ref()类型的响应式数据</code></p>
<pre><code class="copyable">const refData = toRefs(data)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>interface: 类型推断接口 </code></p>
<pre><code class="copyable">interface DataProps &#123; count: Number &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>defineComponent：defineComponent函数，只是对setup函数进行封装，返回options的对象, defineComponent最重要的是：在TypeScript下，给予了组件 正确的参数类型推断.</code></p>
<pre><code class="copyable">export function defineComponent (options:unknown) &#123;    

return isFunction(options) ? &#123; setup : options &#125; : options    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>props:  传参集合, 与vue2差不多</code></p>
<p><code>emits：当前组件的通过emit的事件列表</code></p>
<blockquote>
<p>类型：Array|Object</p>
<p>作用：Vue3.0中使用emit发起事件时会要求当前组件记录emit事件（没有则控制台会抛出警告）。</p>
<p>用途：用于记录当前组件emit的事件，当为对象时，则可以验证传入的值是否有效。</p>
</blockquote>
<p><code>Teleport 瞬移（传送门）：</code></p>
<blockquote>
<p>类似React的Portals。React 的Portal提供了一种将子节点渲染到存在于父组件以外的DOM节点的优秀的方案，Vue 3中的Teleport跟这个其实是类似的。例如将嵌套在组件内部的弹窗传送到最外层</p>
</blockquote>
<p><code>Suspense:  解决异步请求的困境，返回一个promise</code></p>
<blockquote>
<p>Suspense是Vue 3新增的内置标签，每当我们希望组件等待数据获取时（通常在异步API调用中），我们都可以使用Vue3 Composition API制作异步组件。以前，在Vue 2中，我们必须使用条件（例如 v-if 或 v-else）来检查我们的数据是否已加载并显示后备内容。但是现在，Suspense随Vue3内置了，因此我们不必担心跟踪何时加载数据并呈现相应的内容。</p>
</blockquote>
<pre><code class="copyable"><Suspense>
     <template #default> <async-com /></template>
     <template #fallback>Loading ...</template>
</Suspense>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Vue3.x 生命周期变化</h2>
<h4 data-id="heading-7">被替换</h4>
<pre><code class="copyable">beforeCreate -> setup()

created -> setup()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">重命名</h4>
<pre><code class="copyable">beforeMount -> onBeforeMount

mounted -> onMounted

beforeUpdate -> onBeforeUpdate

updated -> onUpdated

beforeDestroy -> onBeforeUnmount

destroyed -> onUnmounted

errorCaptured -> onErrorCaptured
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">新增的</h4>
<p>新增的以下2个方便调试debug的回调钩子：</p>
<pre><code class="copyable">onRenderTracked

onRenderTriggered
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考：<a href="https://www.mybj123.com/8456.html" target="_blank" rel="nofollow noopener noreferrer">www.mybj123.com/8456.html</a></p>
<h2 data-id="heading-10">全局API修改</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d927eb4b5cd14e22b55d1273c9891e11~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">Vue2全局API遇到的问题：</h4>
<ul>
<li>
<p>在单元测试中，全局配置非常容易污染全局环境。</p>
</li>
<li>
<p>在不同的apps中，共享一份有不同配置的Vue对象，变得非常困难。</p>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddf894df1e3845dd9a2f17512e850965~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">主要修改点：</h2>
<h4 data-id="heading-13">全局配置：Vue.config-> app.config</h4>
<pre><code class="copyable">config.productionTip 被删除

config.ignoredElements改名为config.isCustomElement

config.keyCodes被删除
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">全局注册类API</h4>
<pre><code class="copyable">Vue.component->app.component

Vue.directive->app.directive
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">行为扩展类API</h4>
<pre><code class="copyable">Vue.mixin->app.,ixin

Vue.use->app.use
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">其他</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6dba70ef88740a684c76f53fd2ad422~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>如果对你有帮助，希望能够获得你的点赞认可～谢谢。 </code></p></div>  
</div>
            