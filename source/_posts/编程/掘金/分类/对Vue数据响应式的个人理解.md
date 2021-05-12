
---
title: '对Vue数据响应式的个人理解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac36f743a3b34c41b569f770fbcd0d44~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 12 May 2021 02:11:41 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac36f743a3b34c41b569f770fbcd0d44~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://cn.vuejs.org/v2/guide/reactivity.html" target="_blank" rel="nofollow noopener noreferrer">文章出处部分来源</a></p>
<h3 data-id="heading-0">一.一张图追踪数据响应式变化</h3>
<p>数据响应式是Vue 最独特的特性之一，是其非侵入性的响应式系统。数据模型仅仅是普通的 JavaScript 对象。而当你修改它们时，视图会进行更新。</p>
<p>当你把一个普通的 JavaScript 对象传入 Vue 实例作为 data 选项，Vue 将遍历此对象所有的 property，并使用 Object.defineProperty 把这些 property 全部转为 getter/setter。Object.defineProperty 是 ES5 中一个无法 shim 的特性，这也就是 Vue 不支持 IE8 以及更低版本浏览器的原因。</p>
<p>这些 getter/setter 对用户来说是不可见的，但是在内部它们让 Vue 能够追踪依赖，在 property 被访问和修改时通知变更。这里需要注意的是不同浏览器在控制台打印数据对象时对 getter/setter 的格式化并不同，所以建议安装 vue-devtools 来获取对检查数据更加友好的用户界面。</p>
<p>每个组件实例都对应一个 watcher 实例，它会在组件渲染的过程中把“接触”过的数据 property 记录为依赖。之后当依赖项的 setter 触发时，会通知 watcher，从而使它关联的组件重新渲染。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac36f743a3b34c41b569f770fbcd0d44~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于 JavaScript 的限制，Vue 不能检测数组和对象的变化。尽管如此我们还是有一些办法来回避这些限制并保证它们的响应性</p>
<h3 data-id="heading-1">二.vue数据响应式的含义是什么？</h3>
<p>vue能实现对实例中声明过的数据进行监听。当数据发生变化时，试图会根据变化内容进行重新渲染页面，从而简化程序员的工作。</p>
<h3 data-id="heading-2">三.如何做到数据响应式？</h3>
<pre><code class="copyable">通过 object.defineProperty()，配合 getter 和 setter 实现监听，同时引入代理，负责对象的属性读写,代码如下：
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 需求五：就算用户擅自修改 myData，也要拦截他

let myData5 = &#123;n:0&#125;
let data5 = proxy2(&#123; data:myData5 &#125;) // 括号里是匿名对象，无法访问

function proxy2(&#123;data&#125;&#123;
  let value = data.n
  Object.defineProperty(data, 'n', &#123;
    get()&#123;
      return value
    &#125;,
    set(newValue)&#123;
      if(newValue<0)return
      value = newValue
    &#125;
  &#125;)
  // 就加了上面几句，这几句话会监听 data

// data5 就是 obj
console.log(`需求五：$&#123;data5.n&#125;`)
myData5.n = -1
console.log(`需求五：$&#123;data5.n&#125;，设置为 -1 失败了`)
myData5.n = 1
console.log(`需求五：$&#123;data5.n&#125;，设置为 1 成功了`)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>vm = new Vue(&#123;data:myData&#125;),会让vm成为myData的代理，对myData的所有睡醒进行建空，防止myData发生变化。只有代理vm知道了变化，才能根据变化重新渲染视图。</p>
<h3 data-id="heading-3">四.如何给数据新增key</h3>
<h5 data-id="heading-4">1.普通的对象</h5>
<p>使用Vue.set 或者this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>s</mi><mi>e</mi><mi>t</mi><mo stretchy="false">(</mo><mtext>加</mtext></mrow><annotation encoding="application/x-tex">set(加</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">s</span><span class="mord mathnormal">e</span><span class="mord mathnormal">t</span><span class="mopen">(</span><span class="mord cjk_fallback">加</span></span></span></span></span>是为了防止命名冲突)</p>
<pre><code class="copyable">methods: &#123;
    setB() &#123;
      Vue.set(this.obj, 'b', 1)
// 等价于 this.$set(this.obj, 'b', 1)
    &#125;
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：
新增key，自动创建代理和监听，触发UI更新</p>
<h5 data-id="heading-5">2.数组对象</h5>
<p>代码：</p>
<pre><code class="copyable">class VueArray extends Array&#123;
push(...args)&#123;
const oldLength = this.length
super.push(...args)
console.log('你push了')
for(let i = oldLength; i<this.length; i++)&#123;
Vue.set(this, i ,this[i])
&#125;
&#125;
&#125;

//这不是Vue的真实实现，只是展示下思路

<span class="copy-code-btn">复制代码</span></code></pre>
<p>原理就是新增一层原型，供vue使用。</p>
<p>具体就这么多，后面了解深入之后再进行更新。</p></div>  
</div>
            