
---
title: 'Vue3源码系列（一）：初探Vue3'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87a4702e63fa4932929c86ec5e42ea1d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 21:20:46 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87a4702e63fa4932929c86ec5e42ea1d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">Vue3新特性</h3>
<ol>
<li>
<p><strong>composition API。</strong></p>
<p>不同于Vue2的选项式API，组合式API将组件初始化时使用setup方法，包含所有数据、方法，并统一返回。</p>
<p>举个例子：</p>
<pre><code class="copyable">Vue3 composition API：

<script>
export default&#123;
setup（）&#123;
const count =ref (0);
        const add=()=>&#123;
        count.value++;
        &#125;
return &#123;
count,
add
&#125;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>基于Proxy的响应式。</strong></p>
<p>Vue2中响应式数据是通过ES5的数据劫持setter/getter 来实现的，使用的是object.defineproperty，但只能对现有的对象属性进行劫持，针对的是对象上的属性，尽管做一些重写也不能完全覆盖数据变更的地方（比如动态向对象上添加Key，或通过下标的方式修改数组。）</p>
<p>在Vue3中响应式数据使用的是Proxy，针对的是整个对象，直接代理对象，修改代理对象时拦截数据的变化。</p>
<pre><code class="copyable">const data=&#123;&#125;

const dataProxy=new Proxy(data,&#123;
set(target,key,val)&#123;
//代理对象
Reflact.set()
&#125;
get(target,key,val)&#123;
//
Reflact.get()
&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Proxy.revocable()方法可以用来创建一个可撤销的代理对象。</p>
<pre><code class="copyable">const target = &#123; name: 'vuejs'&#125;
const &#123;proxy, revoke&#125; = Proxy.revocable(target, handler)
proxy.name // 正常取值输出 vuejs
revoke() // 取值完成对proxy进行封闭，撤消代理
proxy.name // TypeError: Revoked
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但Proxy只有在ES6的环境使用，还无法编译降级。</p>
</li>
<li>
<p><strong>Tree-shaking的优化。</strong></p>
<p>在使用Vue3时可以选择按需选择引入相应的模块，而不是一次性引入所有代码，这样打包时Vue3可以将没有引用的源码移除，从而减少体积。</p>
</li>
<li>
<p><strong>渲染性能的优化。</strong></p>
<p>Vue3将静态节点、子树等渲染代码移到渲染函数之外，这样可以避免每次渲染时重新创建这些不会变化的对象。将元素的更新类型进行细分，例如动态绑定的部分如果只涉及到 class，则在对比时只需要对比 class 即可，不需要对比它的内容。此外，Vue3还有不少变化，比如模板中支持了多根节点的组件等，这边就不一一介绍。</p>
</li>
</ol>
<h3 data-id="heading-1">代码结构</h3>
<p>Vue3的代码主要分packages和scripts两个目录，script主要用于代码检查、打包等工程操作，真正的源码位于packages目录下，一共有13个包：</p>
<ul>
<li><code>compiler-core</code> 模板解析核心，与具体环境无关，主要生成 AST，并根据 AST 生成 <code>render()</code> 方法</li>
<li><code>compiler-dom</code> 浏览器环境中的模板解析逻辑，如处理 HTML 转义、处理 v-model 等指令</li>
<li><code>compiler-sfc</code> 负责解析 Vue 单文件组件，在前面 vue-loader 的解析中有讲解过</li>
<li><code>compiler-ssr</code> 服务端渲染环境中的模板解析逻辑</li>
<li><code>reactivity</code> 响应式数据相关逻辑</li>
<li><code>runtime-core</code> 与平台无关的运行时核心，包括 render</li>
<li><code>runtime-dom</code> 浏览器环境中的运行时核心</li>
<li><code>runtime-test</code> 用于自动化测试的相关配套</li>
<li><code>server-renderer</code> 用于 SSR 服务端渲染的逻辑</li>
<li><code>shared</code> 一些各个包之间共享的公共工具</li>
<li><code>size-check</code> 一个用于测试 tree shaking 后代码大小的示例库</li>
<li><code>template-explorer</code> 用于检查模板编译后的输出，主要用于开发调试</li>
<li><code>vue</code> Vue 3 的主要入口，包括运行时和编译器，包括几个不同的入口（开发版本、runtime 版本、full 版本）</li>
</ul>
<h3 data-id="heading-2">reactivity</h3>
<p>整体流程</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87a4702e63fa4932929c86ec5e42ea1d~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">ReactiveFlags</h4>
<pre><code class="copyable">export const enum ReactiveFlags &#123;
  skip = '__v_skip',
  isReactive = '__v_isReactive',
  isReadonly = '__v_isReadonly',
  raw = '__v_raw',
  reactive = '__v_reactive',
  readonly = '__v_readonly'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>代理对象会通过 <code>ReactiveFlags.raw</code> 引用原始对象</li>
<li>原始对象会通过 <code>ReactiveFlags.reactive</code> 或 <code>ReactiveFlags.readonly</code> 引用代理对象</li>
<li>代理对象根据它是 <code>reactive</code> 或 <code>readonly</code> 的， 将 <code>ReactiveFlags.isReactive</code> 或 <code>ReactiveFlags.isReadonly</code> 属性值设置为 <code>true</code></li>
</ul>
<h4 data-id="heading-4">Track与Trigger</h4>
<p><code>track()</code> 和 <code>trigger()</code> 是依赖收集的核心，<code>track()</code> 用来跟踪收集依赖(收集 <code>effect</code>)，<code>trigger()</code> 用来触发响应(执行 <code>effect</code>)，它们需要配合 <code>effect()</code> 函数使用</p>
<pre><code class="copyable">const obj = &#123; foo: 1 &#125;
effect(() => &#123;
  console.log(obj.foo)
  track(obj, TrackOpTypes.GET, 'foo')
&#125;)

obj.foo = 2
trigger(obj, TriggerOpTypes.SET, 'foo')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>track与trigger函数接受三个参数：</p>
<ul>
<li>target：要跟踪的目标对象，这里就是 <code>obj</code></li>
<li>跟踪操作的类型：<code>obj.foo</code> 是读取对象的值，因此是 <code>'get'</code></li>
<li>key：要跟踪目标对象的 <code>key</code>，我们读取的是 <code>foo</code>，因此 <code>key</code> 是 <code>foo</code></li>
</ul>
<p>本质上建立一种数据结构：</p>
<pre><code class="copyable">// 伪代码
map : &#123;
    [target]: &#123;
        [key]: [effect1, effect2....]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单的理解，<code>effect</code> 与对象和具体操作的 <code>key</code>，是以这种映射关系建立关联的：</p>
<pre><code class="copyable">[target]`---->`key1`---->`[effect1, effect2...]
[target]`---->`key2`---->`[effect1, effect3...]
[target2]`---->`key1`---->`[effect5, effect6...]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>既然 <code>effect</code> 与目标对象 <code>target</code> 已经建立了联系，那么当然就可以想办法通过 <code>target</code> ----> <code>key</code> 进而取到 <code>effect</code> ，然后执行它们，而这就是 <code>trigger()</code> 函数做的事情，所以在调用 <code>trigger</code> 函数时我们要指定目标对象和相应的<code>key</code>值。</p>
<h4 data-id="heading-5">toRef</h4>
<p>使用reactive 声明响应式对象有时出现对象的二次引用，造成响应丢失（对象解构返回渲染环境也会丢失响应）。</p>
<pre><code class="copyable">const obj = reactive(&#123; foo: 1 &#125;) // obj 是响应式数据
const obj2 = &#123; foo: obj.foo &#125;

effect(() => &#123;
  console.log(obj2.foo) // 这里读取 obj2.foo
&#125;)

obj.foo = 2  // 设置 obj.foo 显然无效
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决问题可以使用<code>toRef()</code> 函数把响应式对象的某个Key值转换成ref。它的实现就直接set、get返回，因为target本身就是响应式的，所以无需track和trigger。</p>
<pre><code class="copyable">function toRef(target, key) &#123;
    return &#123;
        isRef: true,
        get value() &#123;
            return target[key]
        &#125;,
        set value(newVal)&#123;
            target[key] = newVal
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是ref的值需要.value访问值才行。如果不想要.value来取值，我们可以直接再包一层reactive。</p>
<pre><code class="copyable">const obj = reactive(&#123; foo: 1 &#125;)
// const obj2 = &#123; foo: toRef(obj, 'foo') &#125;
const obj2 = reactive(&#123; ...toRefs(obj) &#125;)  // 让 obj2 也是 reactive

effect(() => &#123;
  console.log(obj2.foo)  // 即使 obj2.foo 是 ref，我们也不需要 .value 来取值
&#125;)

obj.foo = 2 // 有效
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它的实现，发现值如果是ref，则返回.value。但这对于ref组成的数组，仍然需要.value来访问。</p>
<pre><code class="copyable">if (isRef(res)) &#123;
      // ref unwrapping - does not apply for Array + integer key.
      const shouldUnwrap = !targetIsArray || !isIntegerKey(key)
      return shouldUnwrap ? res.value : res
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通常使用ref()函数时，我们是为了引用原始数据类型，但引用非基本类型也是可以，比如：</p>
<pre><code class="copyable">const refObj=ref(&#123;foo:1&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>refObj.value是一个对象，这对象是响应式的，修改refObj.value.foo会触发响应。而shallowRef是浅代理，只代理ref对象本身，也就是.value是被代理的，而.value所引用的对象并没有被代理，修改refObj.value.foo不会触发响应。那如果也要触发响应呢？Vue3提供triggerRef函数，可以让我们强制触发响应。</p>
<pre><code class="copyable">triggerRef(refObj) 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">Vue3 Diff</h3>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c162ab65538f4e9592e78a3bcaa7cbd4~tplv-k3u1fbpfcp-watermark.image" alt="image-20210618092346176" loading="lazy" referrerpolicy="no-referrer">
<p><strong>大体流程：</strong></p>
<ol>
<li>
<p>从头对比找到有相同的节点 patch ，发现不同，立即跳出。</p>
</li>
<li>
<p>如果第一步没有patch完，立即，从后往前开始patch ,如果发现不同立即跳出循环。</p>
</li>
<li>
<p>如果新的节点大于老的节点数 ，对于剩下的节点全部以新的vnode处理（ 这种情况说明已经patch完相同的vnode ）。</p>
</li>
<li>
<p>对于老的节点大于新的节点的情况 ， 对于超出的节点全部卸载 （ 这种情况说明已经patch完相同的vnode ）。</p>
</li>
<li>
<p>不确定的元素（ 这种情况说明没有patch完相同的vnode ） 与 3 ，4对立关系。如下情况：</p>
<pre><code class="copyable">     // [i ... e1 + 1]: a b [c d e] f g

     // [i ... e2 + 1]: a b [e d c h] f g

     // i = 2, e1 = 4, e2 = 5

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<ul>
<li>
<p>把没有比较过的新的vnode节点,通过map保存，记录已经patch的新节点的数量 patched，没有经过 path 新的节点的数量 toBePatched</p>
</li>
<li>
<p>建立一个数组newIndexToOldIndexMap，每个子元素都是[ 0, 0, 0, 0, 0, 0, ] 里面的数字记录老节点的索引 ，数组索引就是新节点的索引</p>
</li>
<li>
<p>遍历老节点：</p>
<ul>
<li>如果 toBePatched新的节点数量为0 ，那么统一卸载老的节点</li>
<li>如果,老节点的key存在 ，通过key找到对应的index</li>
<li>如果,老节点的key不存在：遍历剩下的所有新节点，如果找到与当前老节点对应的新节点那么 ，将新节点的索引，赋值给newIndex</li>
<li>没有找到与老节点对应的新节点，卸载当前老节点</li>
<li>如果找到与老节点对应的新节点，把老节点的索引，记录在存放新节点的数组中</li>
</ul>
</li>
<li>
<p>如果发生移动：</p>
</li>
</ul>
<ol>
<li>根据 newIndexToOldIndexMap 新老节点索引列表找到最长稳定序列</li>
<li>对于 newIndexToOldIndexMap[i] =0 证明不存在老节点 ，从新形成新的vnode</li>
<li>对移动的节点进行移动处理。</li>
</ol>
<h4 data-id="heading-7">Diff算法对比：</h4>
<ul>
<li>React：遍历新节点序列在旧节点序列出现的位置，如果位置递增，则新节点不需要移动，否则节点后移。</li>
<li>Vue 2：双端比较。分别用新、旧节点序列的start跟end相互比较，查找复用，直到指针重合，退出循环。若四次对比都没找到复用节点，只能拿新序列的节点去旧序列依次对比。</li>
<li>Vue 3：<strong>最长递增子序列</strong>。生成List代表新节点序列不需要移动的index数组，从后向前遍历，若List[j]==index 说明节点不需要移动，否则节点插入队尾。</li>
</ul></div>  
</div>
            