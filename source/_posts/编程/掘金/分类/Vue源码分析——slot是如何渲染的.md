
---
title: 'Vue源码分析——slot是如何渲染的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a4567246b6d42288de78d1c357b3eea~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 04:04:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a4567246b6d42288de78d1c357b3eea~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>今天主要分析 Vue.js 中常用的 Slots 功能是如何设计和实现的。</p>
<p>本文将分为<strong>普通插槽</strong>、<strong>作用域插槽</strong>以及 Vue.js 2.6.x 版本的 <strong>v-slot 语法</strong>三部分进行讨论。</p>
<p>本文属于进阶内容，如果有还不懂 Slots 用法的同学，建议先移步 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/index.html" ref="nofollow noopener noreferrer">Vue.js 官网</a>进行学习。</p>
<h2 data-id="heading-0">1 普通插槽</h2>
<p>首先举一个 Slots 使用的简单例子。</p>
<pre><code class="copyable"><!-- SlotDemo.vue --><template>  <div class="slot-demo">    <slot>this is slot default content text.</slot>  </div></template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接在页面上渲染这个组件，效果如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a4567246b6d42288de78d1c357b3eea~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着，我们对 Slots 里的内容进行覆盖：</p>
<p><code><slot-demo>this is slot custom content.</slot-demo></code></p>
<p>重新渲染后，效果如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a89c841d77de477a8ee6abfd9f38ff36~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Slots 的用法大家肯定都很清楚了，那么这背后 Vue.js 执行了怎样的逻辑呢？接下来我们一起看看 Vue.js 底层对 Slots 的具体实现。</p>
<h3 data-id="heading-1">1.1 vm.$slots</h3>
<p>首先看看 Vue.js 的 Component 接口上对 <code>$slots</code> 属性的定义：</p>
<p><code>$slots: &#123; [key: string]: Array<VNode> &#125;;</code></p>
<p>多的咱不说，咱直接在控制台打印一下上面例子中的 <code>$slots</code>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eeb6a194b58841a983ebe8d540a83230~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0291cad54bd41598471ff7e823230ba~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来讲解 Slots 内容如何进行渲染以及转换成上图对象的过程。</p>
<h3 data-id="heading-2">1.2 renderSlot</h3>
<p>看完了具体实例中 Slots 渲染后的 <code>vm.$slots</code> 对象，我们来解析一下 <code>renderSlot</code> 这块的逻辑，首先我们先看看 <code>renderSlot</code> 函数的参数都有哪些。</p>
<pre><code class="copyable">export function renderSlot (  name: string, // 插槽名 slotName  fallback: ?Array<VNode>, // 插槽默认内容生成的 vnode 数组  props: ?Object, // props 对象  bindObject: ?Object // v-bind 绑定对象): ?Array<VNode> &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们先不看 scoped-slot 的逻辑，只看普通 Slots 的逻辑：</p>
<pre><code class="copyable">const slotNodes = this.$slots[name]nodes = slotNodes || fallbackreturn nodes
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里拿到<code>this.$slots[name]</code>的值后做了一个空值判断，若存在则直接返回其对应的 vnode 数组，否则返回 fallback 。</p>
<h3 data-id="heading-3">1.3 resolveSlots</h3>
<p>看到这，很多人可能不知道 <code>this.$slots</code> 在哪定义的，解释这个之前，我们要先了解另外一个方法 <code>resolveSlots</code></p>
<pre><code class="copyable">export function resolveSlots (  children: ?Array<VNode>, // 父节点的 children  context: ?Component // 父节点的上下文，即父组件的 vm 实例): &#123; [key: string]: Array<VNode> &#125; &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看完 <code>resolveSlots</code> 的定义后我们接着往后看其中的具体逻辑。</p>
<p>这里先定义了一个 <code>slots</code> 的空对象，如果 参数<code>children</code> 不存在，直接返回：</p>
<pre><code class="copyable">const slots = &#123;&#125;if (!children) &#123;  return slots&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果存在，则对 <code>children</code> 进行遍历操作：</p>
<pre><code class="copyable">for (let i = 0, l = children.length; i < l; i++) &#123;  const child = children[i]  const data = child.data    // 如果 data.slot 存在，将插槽名称当做 key，child 当做值直接添加到 slots 中去  if ((child.context === context || child.fnContext === context) &&    data && data.slot != null  ) &#123;    const name = data.slot    const slot = (slots[name] || (slots[name] = []))    // child 的 tag 为 template 标签的情况    if (child.tag === 'template') &#123;      slot.push.apply(slot, child.children || [])    &#125; else &#123;      slot.push(child)    &#125;      // 如果 data.slot 不存在，则直接将 child 丢到 slots.default 中去  &#125; else &#123;    (slots.default || (slots.default = [])).push(child)  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>slots</code> 获取到值后，会过滤掉只包含空白字符的属性，然后返回：</p>
<pre><code class="copyable">// ignore slots that contains only whitespacefor (const name in slots) &#123;  if (slots[name].every(isWhitespace)) &#123;    delete slots[name]  &#125;&#125;return slots

// isWhitespace 相关逻辑function isWhitespace (node: VNode): boolean &#123;  return (node.isComment && !node.asyncFactory) || node.text === ' '&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">1.4 initRender</h3>
<p>上文解释了 <code>slots</code> 变量的初始化和赋值过程。接下来介绍的 <code>initRender</code> 方法对 <code>vm.$slots</code> 进行了初始化的过程。</p>
<pre><code class="copyable">//  src/core/instance/render.js const options = vm.$optionsconst parentVnode = vm.$vnode = options._parentVnode // the placeholder node in parent treeconst renderContext = parentVnode && parentVnode.contextvm.$slots = resolveSlots(options._renderChildren, renderContext)genSlot()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看完上面的代码，肯定有人会问：你这不就只是拿到了一个对象么，怎么把其中的内容给解析出来呢？</p>
<h3 data-id="heading-5">1.5 genSlot</h3>
<p>别急，我们接着就来把 Slots 解析的相关逻辑过一过，话不多说，咱直接上代码：</p>
<pre><code class="copyable">function genSlot (el: ASTElement, state: CodegenState): string &#123;  const slotName = el.slotName || '"default"' // 取 slotName，若无，则直接命名为 'default'  const children = genChildren(el, state) // 对 children 进行 generate 操作  let res = `_t($&#123;slotName&#125;$&#123;children ? `,$&#123;children&#125;` : ''&#125;`  const attrs = el.attrs && `&#123;$&#123;el.attrs.map(a => `$&#123;camelize(a.name)&#125;:$&#123;a.value&#125;`).join(',')&#125;&#125;` // 将 attrs 转换成对象形式  const bind = el.attrsMap['v-bind'] // 获取 slot 上的 v-bind 属性    // 若 attrs 或者 bind 属性存在但是 children 却木得，直接赋值第二参数为 null  if ((attrs || bind) && !children) &#123;    res += `,null`  &#125;    // 若 attrs 存在，则将 attrs 作为 `_t()` 的第三个参数(普通插槽的逻辑处理)  if (attrs) &#123;    res += `,$&#123;attrs&#125;`  &#125;    // 若 bind 存在，这时如果 attrs 存在，则 bind 作为第三个参数，否则 bind 作为第四个参数(scoped-slot 的逻辑处理)  if (bind) &#123;    res += `$&#123;attrs ? '' : ',null'&#125;,$&#123;bind&#125;`  &#125;  return res + ')'&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的 <code>slotName</code> 在 <code>processSlot</code> 函数中进行了赋值，并且 父组件编译阶段用到的 <code>slotTarget</code> 也在这里进行了处理：</p>
<pre><code class="copyable">// src/compiler/parser/index.jsfunction processSlot (el) &#123;  if (el.tag === 'slot') &#123;    // 直接获取 attr 里面 name 的值    el.slotName = getBindingAttr(el, 'name')    // ...  &#125;  // ...  const slotTarget = getBindingAttr(el, 'slot')  if (slotTarget) &#123;    // 如果 slotTarget 存在则直接取命名插槽的 slot 值，否则直接为 'default'    el.slotTarget = slotTarget === '""' ? '"default"' : slotTarget    if (el.tag !== 'template' && !el.slotScope) &#123;      addAttr(el, 'slot', slotTarget)    &#125;  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随即在 <code>genData</code> 函数中使用 <code>slotTarget</code> 进行 <code>data</code> 的数据拼接：</p>
<pre><code class="copyable">if (el.slotTarget && !el.slotScope) &#123;  data += `slot:$&#123;el.slotTarget&#125;,`&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时父组件将生成以下代码</p>
<pre><code class="copyable">with(this) &#123;  return _c('div', [    _c('slot-demo'),    &#123;      attrs: &#123; slot: 'default' &#125;,      slot: 'default'    &#125;,    [ _v('this is slot custom content.') ]  ])&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后当 <code>el.tag</code> 为 <code>slot</code> 的情况，直接执行 <code>genSlot</code> 函数：</p>
<pre><code class="copyable">else if (el.tag === 'slot') &#123;  return genSlot(el, state)&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照我们举出的例子，子组件最终会生成以下代码：</p>
<pre><code class="copyable">with(this) &#123;  // _c => createElement ; _t => renderSlot ; _v => createTextVNode  return _c(    'div',    &#123;      staticClass: 'slot-demo'    &#125;,    [ _t('default', [ _v('this is slot default content text.') ]) ]  )&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">2 作用域插槽</h2>
<p>上面我们已经了解到 Vue.js 对于普通的 slot 标签是如何进行处理和转换的。接下来我们来分析下作用域插槽的实现逻辑。</p>
<h3 data-id="heading-7">2.1 vm.$scopedSlots</h3>
<p>老规矩，先看看 Vue.js 的 Component 接口上对 <code>$scopedSlots</code> 属性的定义：</p>
<pre><code class="copyable">$scopedSlots: &#123; [key: string]: () => VNodeChildren &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中的 <code>VNodeChildren</code> 定义如下：</p>
<pre><code class="copyable">declare type VNodeChildren = Array<?VNode | string | VNodeChildren> | string;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先来个相关的例子：</p>
<pre><code class="copyable"><template>  <div class="slot-demo">    <slot text="this is a slot demo , " :msg="msg"></slot>  </div></template><script>export default &#123;  name: 'SlotDemo',  data () &#123;    return &#123;      msg: 'this is scoped slot content.'    &#125;  &#125;&#125;</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后进行使用：</p>
<pre><code class="copyable"><template>  <div class="parent-slot">    <slot-demo>      <template slot-scope="scope">        <p>&#123;&#123; scope.text &#125;&#125;</p>        <p>&#123;&#123; scope.msg &#125;&#125;</p>      </template>    </slot-demo>  </div></template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e038512b38594cddb6e7a55894d61b90~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69ee2fa0ce2745a3a1363d35374d716c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从例子中我们能看出用法，子组件的 slot 标签上绑定 <code>text</code> 以及 <code>:msg</code> 属性。然后父组件在使用插槽用 <code>slot-scope</code> 属性去读取插槽属性对应的值。</p>
<h3 data-id="heading-8">2.2 processSlot</h3>
<p>提及一下 <code>processSlot</code> 函数对于 <code>slot-scope</code> 的处理逻辑：</p>
<pre><code class="copyable">let slotScopeif (el.tag === 'template') &#123;    slotScope = getAndRemoveAttr(el, 'scope')  // 兼容 2.5 以前版本 slot scope 的用法(这块有个警告，我直接忽略掉了)    el.slotScope = slotScope || getAndRemoveAttr(el, 'slot-scope')&#125; else if ((slotScope = getAndRemoveAttr(el, 'slot-scope'))) &#123;    el.slotScope = slotScope &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码我们能看出，Vue.js 直接读取 <code>slot-scope</code> 属性并赋值给 AST 抽象语法树的 <code>slotScope</code> 属性。而拥有 <code>slotScope</code> 属性的节点，会直接以 <strong>插槽名称 name 为 key、本身为 value</strong> 的对象形式挂载在父节点的 <code>scopedSlots</code> 属性上。</p>
<pre><code class="copyable">else if (element.slotScope) &#123;     currentParent.plain = false    const name = element.slotTarget || '"default"'    (currentParent.scopedSlots || (currentParent.scopedSlots = &#123;&#125;))[name] = element&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 <code>renderMixin</code> 函数中对 <code>vm.$scopedSlots</code> 进行了如下赋值：</p>
<pre><code class="copyable">// src/core/instance/render.jsif (_parentVnode) &#123;  vm.$scopedSlots = _parentVnode.data.scopedSlots || emptyObject&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后 <code>genData</code> 函数里会进行以下逻辑处理：</p>
<pre><code class="copyable">if (el.scopedSlots) &#123;  data += `$&#123;genScopedSlots(el, el.scopedSlots, state)&#125;,`&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2.3 genScopedSlots & genScopedSlot</h3>
<p>紧接着我们来看看 <code>genScopedSlots</code> 函数中的逻辑：</p>
<pre><code class="copyable">function genScopedSlots (  slots: &#123; [key: string]: ASTElement &#125;,  state: CodegenState): string &#123;  // 对 el.scopedSlots 对象进行遍历，执行 genScopedSlot，且将结果用逗号进行拼接  // _u => resolveScopedSlots (具体逻辑下面一个小节进行分析)  return `scopedSlots:_u([$&#123;    Object.keys(slots).map(key => &#123;      return genScopedSlot(key, slots[key], state)    &#125;).join(',')  &#125;])`&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们再来看看 <code>genScopedSlot</code> 函数是如何生成 render function 字符串的：</p>
<pre><code class="copyable">function genScopedSlot (  key: string,  el: ASTElement,  state: CodegenState): string &#123;  if (el.for && !el.forProcessed) &#123;    return genForScopedSlot(key, el, state)  &#125;  // 函数参数为标签上 slot-scope 属性对应的值 (getAndRemoveAttr(el, 'slot-scope'))  const fn = `function($&#123;String(el.slotScope)&#125;)&#123;` +    `return $&#123;el.tag === 'template'      ? el.if        ? `$&#123;el.if&#125;?$&#123;genChildren(el, state) || 'undefined'&#125;:undefined`        : genChildren(el, state) || 'undefined'      : genElement(el, state)    &#125;&#125;`  // key 为插槽名称，fn 为生成的函数代码  return `&#123;key:$&#123;key&#125;,fn:$&#123;fn&#125;&#125;`&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们把上面例子的 <code>$scopedSlots</code> 在控制台打印一下，结果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc67ae4b14aa4ad0b9f0c27c80f996f8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面例子中父组件最终会生成如下代码：</p>
<pre><code class="copyable">with(this)&#123;  // _c => createElement ; _u => resolveScopedSlots  // _v => createTextVNode ; _s => toString  return _c('div',    &#123; staticClass: 'parent-slot' &#125;,    [_c('slot-demo',      &#123; scopedSlots: _u([        &#123;          key: 'default',          fn: function(scope) &#123;            return [              _c('p', [ _v(_s(scope.text)) ]),              _c('p', [ _v(_s(scope.msg)) ])            ]          &#125;        &#125;])      &#125;    )]  )&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2.4 renderSlot(slot-scope) & renderSlot</h3>
<p>上面我们提及对于插槽渲染逻辑的时候忽略了 <code>slot-scope</code> 的相关逻辑，这里我们来看看这部分内容：</p>
<pre><code class="copyable">export function renderSlot (  name: string,  fallback: ?Array<VNode>,  props: ?Object,  bindObject: ?Object): ?Array<VNode> &#123;  const scopedSlotFn = this.$scopedSlots[name]  let nodes  if (scopedSlotFn) &#123; // scoped slot    props = props || &#123;&#125;    // ...    nodes = scopedSlotFn(props) || fallback  &#125; // ... return nodes&#125;resolveScopedSlots()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里 <code>renderHelps</code> 函数里面的 <code>_u</code> ，即 <code>resolveScopedSlots</code>，其逻辑如下：</p>
<pre><code class="copyable">export function resolveScopedSlots (  fns: ScopedSlotsData, // Array<&#123; key: string, fn: Function &#125; | ScopedSlotsData>  res?: Object): &#123; [key: string]: Function &#125; &#123;  res = res || &#123;&#125;  // 遍历 fns 数组，生成一个 `key 为插槽名称，value 为函数` 的对象  for (let i = 0; i < fns.length; i++) &#123;    if (Array.isArray(fns[i])) &#123;      resolveScopedSlots(fns[i], res)    &#125; else &#123;      res[fns[i].key] = fns[i].fn    &#125;  &#125;  return res&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>genSlot</code> 函数上面我已经讲解过，要看请往上翻阅。结合我们的例子，子组件则会生成以下代码：</p>
<pre><code class="copyable">with(this) &#123;  return _c(    'div',    &#123;      staticClass: 'slot-demo'    &#125;,    [      _t('default', null, &#123; text: 'this is a slot demo , ', msg: msg &#125;)    ]  )&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到目前为止，对于普通插槽和作用域插槽已经谈的差不多了。接下来，我们将一起看看 Vue.js 2.6.x 版本的 v-slot 语法。</p>
<h2 data-id="heading-11">3 v-slot</h2>
<h3 data-id="heading-12">3.1 基本用法</h3>
<p>Vue.js 2.6.x 已经出来有一段时间了，其中对于插槽这块则是放弃了 slot-scope 作用域插槽推荐写法，直接改成了 v-slot 指令形式的推荐写法。(当然这只是个语法糖而已)</p>
<p>在看具体实现逻辑前，我们先通过一个例子来先了解下其基本用法。</p>
<pre><code class="copyable"><template>  <div class="slot-demo">    <slot name="demo">this is demo slot.</slot>    <slot text="this is a slot demo , " :msg="msg"></slot>  </div></template><script>export default &#123;  name: 'SlotDemo',  data () &#123;    return &#123;      msg: 'this is scoped slot content.'    &#125;  &#125;&#125;</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后</p>
<pre><code class="copyable"><template>  <slot-demo>    <template v-slot:demo>this is custom slot.</template>    <template v-slot="scope">      <p>&#123;&#123; scope.text &#125;&#125;&#123;&#123; scope.msg &#125;&#125;</p>    </template>  </slot-demo></template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看着好 easy 。</p>
<h3 data-id="heading-13">3.2 相同与区别</h3>
<p>接下来，咱来会会这个新特性。</p>
<h4 data-id="heading-14">3.2.1 <span class="math math-inline"><span class="katex-error" title="ParseError: KaTeX parse error: Expected 'EOF', got '&' at position 7: slots &̲ " style="color:#cc0000">slots & </span></span>scopedSlots</h4>
<p><code>$slots</code> 这块逻辑没变，还是沿用的以前的代码：</p>
<pre><code class="copyable">// $slotsconst options = vm.$optionsconst parentVnode = vm.$vnode = options._parentVnodeconst renderContext = parentVnode && parentVnode.contextvm.$slots = resolveSlots(options._renderChildren, renderContext)$scopedSlots 这块则进行了改造，执行了 normalizeScopedSlots() 并接收其返回值为 $scopedSlots 的值if (_parentVnode) &#123;  vm.$scopedSlots = normalizeScopedSlots(    _parentVnode.data.scopedSlots,    vm.$slots,    vm.$scopedSlots  )&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，我们来会一会 <code>normalizeScopedSlots</code> ，首先我们先看看它的定义：</p>
<pre><code class="copyable">export function normalizeScopedSlots (  slots: &#123; [key: string]: Function &#125; | void,  // 某节点 data 属性上 scopedSlots  normalSlots: &#123; [key: string]: Array<VNode> &#125;, // 当前节点下的普通插槽  prevSlots?: &#123; [key: string]: Function &#125; | void // 当前节点下的特殊插槽): any &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，如果 <code>slots</code> 不存在，则直接返回一个空对象 <code>&#123;&#125;</code> 。</p>
<pre><code class="copyable">if (!slots) &#123;  res = &#123;&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若 <code>prevSlots</code> 存在，且满足系列条件的情况，则直接返回 <code>prevSlots</code> 。</p>
<pre><code class="copyable">const hasNormalSlots = Object.keys(normalSlots).length > 0 // 是否拥有普通插槽const isStable = slots ? !!slots.$stable : !hasNormalSlots // slots 上的 $stable 值const key = slots && slots.$key // slots 上的 $key 值else if (  isStable &&  prevSlots &&  prevSlots !== emptyObject &&  key === prevSlots.$key && // slots $key 值与 prevSlots $key 相等  !hasNormalSlots && // slots 中没有普通插槽  !prevSlots.$hasNormal // prevSlots 中没有普通插槽) &#123;  return prevSlots&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注：这里的 <code>key</code> , <code>hasNormal</code> , <code>$stable</code> 是直接使用 Vue.js 内部对 <code>Object.defineProperty</code> 封装好的 <code>def</code> 方法进行赋值的。</p>
<pre><code class="copyable">def(res, '$stable', isStable)def(res, '$key', key)def(res, '$hasNormal', hasNormalSlots)否则，则对 slots 对象进行遍历，操作 normalSlots ，赋值给 key 为 key，value 为 normalizeScopedSlot 返回的函数 的对象 reslet reselse &#123;  res = &#123;&#125;  for (const key in slots) &#123;    if (slots[key] && key[0] !== '$') &#123;      res[key] = normalizeScopedSlot(normalSlots, key, slots[key])    &#125;  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随后再次对 <code>normalSlots</code> 进行遍历，若 <code>normalSlots</code> 中的 <code>key</code> 在 <code>res</code> 找不到对应的 <code>key</code>，则直接进行 <code>proxyNormalSlot</code> 代理操作，将 <code>normalSlots</code> 中的 <code>slot</code> 挂载到 <code>res</code> 对象上。</p>
<pre><code class="copyable">for (const key in normalSlots) &#123;  if (!(key in res)) &#123;    res[key] = proxyNormalSlot(normalSlots, key)  &#125;&#125;function proxyNormalSlot(slots, key) &#123;  return () => slots[key]&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，我们看看 <code>normalizeScopedSlot</code> 函数都做了些什么事情。该方法接收三个参数，第一个参数为 <code>normalSlots</code> ，第二个参数为 <code>key</code> ，第三个参数为 <code>fn</code> 。</p>
<pre><code class="copyable">function normalizeScopedSlot(normalSlots, key, fn) &#123;  const normalized = function () &#123;    // 若参数为多个，则直接使用 arguments 作为 fn 的参数，否则直接传空对象作为 fn 的参数    let res = arguments.length ? fn.apply(null, arguments) : fn(&#123;&#125;)    // fn 执行返回的 res 不是数组，则是单 vnode 的情况，赋值为 [res] 即可    // 否则执行 normalizeChildren 操作，这块主要对针对 slot 中存在 v-for 操作    res = res && typeof res === 'object' && !Array.isArray(res)      ? [res] // single vnode      : normalizeChildren(res)    return res && (      res.length === 0 ||      (res.length === 1 && res[0].isComment) // slot 上 v-if 相关处理    ) ? undefined      : res  &#125;  // v-slot 语法糖处理  if (fn.proxy) &#123;    Object.defineProperty(normalSlots, key, &#123;      get: normalized,      enumerable: true,      configurable: true    &#125;)  &#125;  return normalized&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">3.2.2 renderSlot</h4>
<p>这块逻辑处理其实和之前是一样的，只是删除了一些警告的代码而已。这点这里就不展开叙述了。</p>
<h4 data-id="heading-16">3.2.3 processSlot</h4>
<p>首先，这里解析 slot 的方法名从 processSlot 变成了 processSlotContent，但其实前面的逻辑和以前是一样的。只是新增了一些对于 v-slot 的逻辑处理，下面我们就来捋捋这块。过具体逻辑前，我们先看一些相关的正则和方法。</p>
<ol>
<li>
<p>相关正则 & functions</p>
<p>dynamicArgRE 动态参数匹配const dynamicArgRE = /^[.*]<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="normal">/</mi><mi mathvariant="normal">/</mi><mi mathvariant="normal">/</mi><mtext>匹配</mtext><msup><mtext>到</mtext><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup><mo stretchy="false">[</mo><msup><mo stretchy="false">]</mo><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup><mtext>则为</mtext><mi>t</mi><mi>r</mi><mi>u</mi><mi>e</mi><mtext>，</mtext><msup><mtext>如</mtext><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup><mo stretchy="false">[</mo><mi>i</mi><mi>t</mi><mi>e</mi><mi>m</mi><msup><mo stretchy="false">]</mo><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup><mi>s</mi><mi>l</mi><mi>o</mi><mi>t</mi><mi>R</mi><mi>E</mi><mtext>匹配</mtext><mi>v</mi><mo>−</mo><mi>s</mi><mi>l</mi><mi>o</mi><mi>t</mi><mtext>语法相关正则</mtext><mi>c</mi><mi>o</mi><mi>n</mi><mi>s</mi><mi>t</mi><mi>s</mi><mi>l</mi><mi>o</mi><mi>t</mi><mi>R</mi><mi>E</mi><mo>=</mo><msup><mi mathvariant="normal">/</mi><mi>v</mi></msup><mo>−</mo><mi>s</mi><mi>l</mi><mi>o</mi><mi>t</mi><mo stretchy="false">(</mo><mo>:</mo><mi mathvariant="normal">∣</mi></mrow><annotation encoding="application/x-tex">/ // 匹配到 '[]' 则为 true，如 '[ item ]'slotRE 匹配 v-slot 语法相关正则const slotRE = /^v-slot(:|</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1.001892em;vertical-align:-0.25em;"></span><span class="mord">/</span><span class="mord">/</span><span class="mord">/</span><span class="mord cjk_fallback">匹</span><span class="mord cjk_fallback">配</span><span class="mord"><span class="mord cjk_fallback">到</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class="mopen">[</span><span class="mclose"><span class="mclose">]</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class="mord cjk_fallback">则</span><span class="mord cjk_fallback">为</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">u</span><span class="mord mathnormal">e</span><span class="mord cjk_fallback">，</span><span class="mord"><span class="mord cjk_fallback">如</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class="mopen">[</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal">m</span><span class="mclose"><span class="mclose">]</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class="mord mathnormal">s</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">o</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.00773em;">R</span><span class="mord mathnormal" style="margin-right:0.05764em;">E</span><span class="mord cjk_fallback">匹</span><span class="mord cjk_fallback">配</span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">s</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">o</span><span class="mord mathnormal">t</span><span class="mord cjk_fallback">语</span><span class="mord cjk_fallback">法</span><span class="mord cjk_fallback">相</span><span class="mord cjk_fallback">关</span><span class="mord cjk_fallback">正</span><span class="mord cjk_fallback">则</span><span class="mord mathnormal">c</span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mord mathnormal">s</span><span class="mord mathnormal">t</span><span class="mord mathnormal">s</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">o</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.00773em;">R</span><span class="mord mathnormal" style="margin-right:0.05764em;">E</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord"><span class="mord">/</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.03588em;">v</span></span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">s</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">o</span><span class="mord mathnormal">t</span><span class="mopen">(</span><span class="mrel">:</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord">∣</span></span></span></span></span>)|^#/ // 匹配到 'v-slot' 或 'v-slot:' 则为 truegetAndRemoveAttrByRegex 通过正则匹配绑定的 attr 值export function getAndRemoveAttrByRegex (  el: ASTElement,  name: RegExp // ) &#123;  const list = el.attrsList // attrsList 类型为 Array  // 对 attrsList 进行遍历，若有满足 RegExp 的则直接返回当前对应的 attr  // 若参数 name 传进来的是 slotRE = /^v-slot(:|<span class="math math-inline"><span class="katex-error" title="ParseError: KaTeX parse error: Expected group after '^' at position 3: )|^̲#/ // 那么匹配到 'v-…" style="color:#cc0000">)|^#/ // 那么匹配到 'v-slot' 或者 'v-slot:xxx' 则会返回其对应的 attr for (let i = 0, l = list.length; i < l; i++) &#123; const attr = list[i] if (name.test(attr.name)) &#123; list.splice(i, 1) return attr &#125; &#125;&#125;ASTAttr 接口定义declare type ASTAttr = &#123; name: string; value: any; dynamic?: boolean; start?: number; end?: number&#125;;createASTElement 创建 ASTElementexport function createASTElement ( tag: string, // 标签名 attrs: Array<ASTAttr>, // attrs 数组 parent: ASTElement | void // 父节点): ASTElement &#123; return &#123; type: 1, tag, attrsList: attrs, attrsMap: makeAttrsMap(attrs), rawAttrsMap: &#123;&#125;, parent, children: [] &#125;&#125;getSlotName 获取 slotNamefunction getSlotName (binding) &#123; // 'v-slot:item' 匹配获取到 'item' let name = binding.name.replace(slotRE, '') if (!name) &#123; if (binding.name[0] !== '#') &#123; name = 'default' &#125; else if (process.env.NODE_ENV !== 'production') &#123; warn( `v-slot shorthand syntax requires a slot name.`, binding ) &#125; &#125; // 返回一个 key 包含 name，dynamic 的对象 // 'v-slot:[item]' 匹配然后 replace 后获取到 name = '[item]' // 进而进行动态参数进行匹配 dynamicArgRE.test(name) 结果为 true return dynamicArgRE.test(name) ? &#123; name: name.slice(1, -1), dynamic: true &#125; // 截取变量，如 '[item]' 截取后变成 'item' : &#123; name: `"</span></span>&#123;name&#125;"`, dynamic: false &#125;&#125;</p>
</li>
<li>
<p><code>processSlotContent</code></p>
</li>
</ol>
<p>这里我们先看看 Slots 对于 template 是如何处理的。</p>
<pre><code class="copyable">if (el.tag === 'template') &#123;  // 匹配绑定在 template 上的 v-slot 指令，这里会匹配到对应 v-slot 的 attr(类型为 ASTAttr)  const slotBinding = getAndRemoveAttrByRegex(el, slotRE)  // 若 slotBinding 存在，则继续进行 slotName 的正则匹配  // 随即将匹配出来的 name 赋值给 slotTarget，dynamic 赋值给 slotTargetDynamic  // slotScope 赋值为 slotBinding.value 或者 '_empty_'  if (slotBinding) &#123;    const &#123; name, dynamic &#125; = getSlotName(slotBinding)    el.slotTarget = name    el.slotTargetDynamic = dynamic    el.slotScope = slotBinding.value || emptySlotScopeToken  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果不是 template，而是绑定在 component 上的话，对于 v-slot 指令和 slotName 的匹配操作是一样的，不同点在于这里需要将组件的 children 添加到其默认插槽中去。</p>
<pre><code class="copyable">else &#123;  // v-slot on component 表示默认插槽  const slotBinding = getAndRemoveAttrByRegex(el, slotRE)  // 将组件的 children 添加到其默认插槽中去  if (slotBinding) &#123;    // 获取当前组件的 scopedSlots    const slots = el.scopedSlots || (el.scopedSlots = &#123;&#125;)    // 匹配拿到 slotBinding 中 name，dynamic 的值    const &#123; name, dynamic &#125; = getSlotName(slotBinding)    // 获取 slots 中 key 对应匹配出来 name 的 slot    // 然后再其下面创建一个标签名为 template 的 ASTElement，attrs 为空数组，parent 为当前节点    const slotContainer = slots[name] = createASTElement('template', [], el)    // 这里 name、dynamic 统一赋值给 slotContainer 的 slotTarget、slotTargetDynamic，而不是 el    slotContainer.slotTarget = name    slotContainer.slotTargetDynamic = dynamic    // 将当前节点的 children 添加到 slotContainer 的 children 属性中    slotContainer.children = el.children.filter((c: any) => &#123;      if (!c.slotScope) &#123;        c.parent = slotContainer        return true      &#125;    &#125;)    slotContainer.slotScope = slotBinding.value || emptySlotScopeToken    // 清空当前节点的 children    el.children = []    el.plain = false  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样处理后我们就可以直接在父组件上面直接使用 v-slot 指令去获取 slot 绑定的值。</p>
<p>举个官方例子：</p>
<pre><code class="copyable">Default slot with text<!-- old --><foo>  <template slot-scope="&#123; msg &#125;">    &#123;&#123; msg &#125;&#125;  </template></foo><!-- new --><foo v-slot="&#123; msg &#125;">  &#123;&#123; msg &#125;&#125;</foo>Default slot with element<!-- old --><foo>  <div slot-scope="&#123; msg &#125;">    &#123;&#123; msg &#125;&#125;  </div></foo><!-- new --><foo v-slot="&#123; msg &#125;">  <div>    &#123;&#123; msg &#125;&#125;  </div></foo>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">3.2.4 genSlot</h4>
<p>在这块逻辑也没发生本质性的改变，唯一一个改变就是为了支持 v-slot 动态参数做了些改变，具体如下：</p>
<pre><code class="copyable">// oldconst attrs = el.attrs && `&#123;$&#123;el.attrs.map(a => `$&#123;camelize(a.name)&#125;:$&#123;a.value&#125;`).join(',')&#125;&#125;`// new// attrs、dynamicAttrs 进行 concat 操作，并执行 genProps 将其转换成对应的 generate 字符串const attrs = el.attrs || el.dynamicAttrs    ? genProps(        (el.attrs || []).concat(el.dynamicAttrs || []).map(attr => (&#123;          // slot props are camelized          name: camelize(attr.name),          value: attr.value,          dynamic: attr.dynamic        &#125;))     )    : null
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89e0de761fb74782bfaea7a7268719cc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            