
---
title: 'Vue基础整理与理解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4c56c34f7044fbb08b2adc1fb77631~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 25 May 2021 02:12:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4c56c34f7044fbb08b2adc1fb77631~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<h2 data-id="heading-0">基础：</h2>
</blockquote>
<h3 data-id="heading-1">v-if和v-show 区别：</h3>
<p>v-show：通过display来控制显示和隐藏；</p>
<p>v-if是组件真正的渲染和销毁，而不是现实和吟唱；</p>
<p>频繁切换场景使用v-show;</p>
<h3 data-id="heading-2">keep-alive:</h3>
<p>缓存组件，需要频繁切换但不需要频繁渲染常用；例如tab切换；</p>
<p>也可以作为vue性能优化手段之一；</p>
<h3 data-id="heading-3">mixin:</h3>
<p>优点：适用于 多个组件有相同的逻辑，可以使用mixin,比较方便；</p>
<p>缺点：多mixin可能造成命名冲突；变量来源不明确，不利于阅读；</p>
<p>mixin和组件可能出现多对多关系，复杂度比较高；</p>
<h3 data-id="heading-4">computed 和watch区别</h3>
<p>computed优点：缓存，data不变不会重新计算；</p>
<p>提升性能；</p>
<h3 data-id="heading-5">$nextTick：</h3>
<p>$nextTick在Dom更新完成之后，触发回调；</p>
<p><strong>实现原理：</strong></p>
<p>nextTick 方法主要是使用了宏任务和微任务,定义了一个异步方法.多次调用 nextTick 会将方法存入 队列中，通过这个异步方法清空当前队列。 所以这个 nextTick 方法就是异步方法；</p>
<p>在下次 DOM 更新循环结束之后执行延迟回调。nextTick主要使用了宏任务和微任务。根据执行环境分别尝试采用</p>
<ul>
<li>Promise</li>
<li>MutationObserver</li>
<li>setImmediate</li>
<li>如果以上都不行则采用setTimeout</li>
</ul>
<p>备注： <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/MutationObserver/MutationObserver" target="_blank" rel="nofollow noopener noreferrer">MutationObserver()</a></p>
<p>创建并返回一个新的 MutationObserver 它会在指定的DOM发生变化时被调用。</p>
<p>setImmediate()方法用于中断长时间运行的操作，并在浏览器完成其他操作（如事件和显示更新）后立即运行回调函数。</p>
<p>定义了一个异步方法，多次调用nextTick会将方法存入队列中，通过这个异步方法清空当前队列。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4c56c34f7044fbb08b2adc1fb77631~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">v-for中用key:</h3>
<p>1）必须是key,不能是index;</p>
<p>2）diff算法中通过tag和key来判断，是不是sameNode;</p>
<p>key 是为 Vue 中 vnode 的唯一标记，通过这个 key，我们的 diff 操作可以更准确、更快速</p>
<ul>
<li>更准确：因为带 key 就不是就地复用了，在 sameNode 函数a.key === b.key对比中可以避免就地复用的情况。所以会更加准确。</li>
<li>更快速：利用 key 的唯一性生成 map 对象来获取对应节点，比遍历方式更快</li>
</ul>
<p>3）减少渲染次数，提升性能；</p>
<h3 data-id="heading-7">vue中常用的组件通讯；</h3>
<p><strong>常用的：</strong></p>
<p>父子组件： props和 this.$emit;</p>
<p>自定义事件： event.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>o</mi><mi>n</mi><mo separator="true">,</mo><mi>e</mi><mi>v</mi><mi>e</mi><mi>n</mi><mi>t</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">on,event.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.80952em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord">.</span></span></span></span></span>off 和 event.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>n</mi><mi>o</mi><mtext>（需要在</mtext><mi>d</mi><mi>e</mi><mi>s</mi><mi>t</mi><mi>o</mi><mi>r</mi><mi>y</mi><mtext>生命周期中，销毁自定义事件</mtext><mi>e</mi><mi>v</mi><mi>e</mi><mi>n</mi><mi>e</mi><mi>t</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">no （需要在destory 生命周期中，销毁自定义事件evenet.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">n</span><span class="mord mathnormal">o</span><span class="mord cjk_fallback">（</span><span class="mord cjk_fallback">需</span><span class="mord cjk_fallback">要</span><span class="mord cjk_fallback">在</span><span class="mord mathnormal">d</span><span class="mord mathnormal">e</span><span class="mord mathnormal">s</span><span class="mord mathnormal">t</span><span class="mord mathnormal">o</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="mord cjk_fallback">生</span><span class="mord cjk_fallback">命</span><span class="mord cjk_fallback">周</span><span class="mord cjk_fallback">期</span><span class="mord cjk_fallback">中</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">销</span><span class="mord cjk_fallback">毁</span><span class="mord cjk_fallback">自</span><span class="mord cjk_fallback">定</span><span class="mord cjk_fallback">义</span><span class="mord cjk_fallback">事</span><span class="mord cjk_fallback">件</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">e</span><span class="mord mathnormal">t</span><span class="mord">.</span></span></span></span></span>off）</p>
<p>vuex</p>
<p><strong>总共大致有这几种：</strong></p>
<p>父子组件通信</p>
<ul>
<li>事件机制(**父->子props,子->父 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>o</mi><mi>n</mi><mtext>、</mtext></mrow><annotation encoding="application/x-tex">on、</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mord cjk_fallback">、</span></span></span></span></span>emit)</li>
<li>获取父子组件实例 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>p</mi><mi>a</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mtext>、</mtext></mrow><annotation encoding="application/x-tex">parent、</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">p</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord cjk_fallback">、</span></span></span></span></span>children</li>
<li>Ref 获取实例的方式调用组件的属性或者方法</li>
<li>Provide、inject (不推荐使用，组件库时很常用)</li>
</ul>
<p>兄弟组件通信</p>
<ul>
<li>eventBus 这种方法通过一个空的 Vue实例作为中央事件总线（事件中心），用它来触发事件和监听事件，从而实现任何组件间的通信，包括父子、隔代、兄弟组件；</li>
</ul>
<p>Vue.prototype.$bus = new Vue</p>
<ul>
<li>Vuex</li>
</ul>
<p>跨级组件通信</p>
<ul>
<li>
<p>Vuex</p>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi><mi>t</mi><mi>t</mi><mi>r</mi><mi>s</mi><mtext>、</mtext></mrow><annotation encoding="application/x-tex">attrs、</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">、</span></span></span></span></span>listeners</p>
</li>
</ul>
<h3 data-id="heading-8">beforeDetory 使用场景：</h3>
<p>解除自定义事件evenet.$off</p>
<p>清楚定时器</p>
<p>解除自定义DOM 事件，例如window scroll等等；</p>
<blockquote>
<h2 data-id="heading-9">自己理解（小白，若有不当敬请指出）：</h2>
</blockquote>
<h2 data-id="heading-10">vue如何监听数据变化？响应式原理</h2>
<p>核心就是Object.defineProperty来实现响应式(当然vue3.0使用的是Proxy)</p>
<p>大致分为  监听对象情况， 需要深度监听复杂对象(observer(value))情况，监听数组这几种情况；</p>
<p>监听对象核心：</p>
<pre><code class="copyable">function defineReactive(target,key,value) &#123;  
// 核心 api 
//深度监听
observer(value)
 Object.defineProperty(target,key, &#123;  
     get() &#123;  
       return value    
     &#125;,  
    set(newValue) &#123;  
      if(newValue !== value) &#123;    
       //深度监听新值
      observer(newValue)
        // 设置新值     
         value = newValue     
        // 触发更新视图     
       updateView()    
      &#125;  
    &#125; 
 &#125;)&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要深度监听复杂对象(observer(value))情况</p>
<pre><code class="copyable">//如果是复杂对象，需要调用obser方法// 监听对象
function oberver(target) &#123; 
   if (typeof target !== 'object' || target === null) &#123;   
 // 不是对象 或数组   
 return target  &#125;  
// 污染全局的Array 原型  
if(Array.isArray(target)) &#123;  
   target._proto_ =  arrProto  &#125; 
  // 重新定义各个属性  
for (let key in target) &#123;  
  defineReactive(target,key,target[key])  
&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>监听数组变化：（无法原生监听到数组，需要此处特殊处理；）</p>
<pre><code class="copyable">// 重新定义数组原型
const oldArrayProperty = Array.prototype
// 创建新对象，原型指向 oldArrayProperty ，再扩展新的方法不会影响原型
const arrProto = Object.create(oldArrayProperty);
['push', 'pop', 'shift', 'unshift', 'splice'].forEach(methodName => &#123;
    arrProto[methodName] = function () &#123;
        updateView() // 触发视图更新
        oldArrayProperty[methodName].call(this, ...arguments)
        // Array.prototype.push.call(this, ...arguments)
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">object.defineProperty 缺点：</h3>
<p>1）深度监听，需要递归到底（源数据对象有多深，就要一次性递循环归到最深处），一次性计算量比较大</p>
<p>2）无法监听新增属性/删除属性（可以通过Vue.set Vue.delete增删）</p>
<p>3）无法原生监听到数组，需要特殊处理；</p>
<h2 data-id="heading-12">diff 算法过程：</h2>
<p>这个我是看博客看了几篇，还是没明白；后来花了快一天时间才明白；建议自己手本子上画diff比对过程；</p>
<p>diff即对比，是一个广泛的概念；Vue将Diff进行了优化，<strong>从O(n^3) -> O(n)</strong>，只有当新旧children都为多个子节点时才需要用核心的Diff算法进行同层级比较。</p>
<p>树diff时间复杂度O(n3) --->优化时间复杂度到0（n）</p>
<p><strong>O(n3) ：</strong> 第一： 遍历tree1,第二遍历tree2；第三，排序</p>
<p><strong>优化到O(n)：</strong></p>
<p>只比较同一层级，不跨级比较</p>
<p>tag不相同，则直接删除重建，不再深度比较</p>
<p>tag和key，两者都相同，则认为是相同节点，不再深度比较；</p>
<p>比较过程</p>
<ul>
<li>
<p>同级比较，再比较子节点</p>
</li>
<li>
<p>先判断一方有子节点一方没有子节点的情况(如果新的children没有子节点，将旧的子节点移除)</p>
</li>
<li>
<p>比较都有子节点的情况(核心diff)</p>
</li>
<li>
<p>递归比较子节点；</p>
</li>
<li>
<p>。。。。</p>
</li>
</ul>
<h2 data-id="heading-13">diff算法时间复杂度</h2>
<h2 data-id="heading-14">Object.defineproperty原理</h2>
<h2 data-id="heading-15">虚拟dom</h2>
<h3 data-id="heading-16">vue 生命周期</h3>
<blockquote>
<h2 data-id="heading-17">V3.0新特性</h2>
</blockquote>
<blockquote>
<h3 data-id="heading-18">vue 和  react  对比；</h3>
</blockquote></div>  
</div>
            