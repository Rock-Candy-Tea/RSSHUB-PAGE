
---
title: 'Vue3 模板编译源码学习'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=368'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 02:32:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=368'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">前言</h1>
<p>在看这一块代码的时候我选择从测试用例入手：</p>
<pre><code class="copyable">describe('compiler: integration tests', () => &#123;
  const source = `
    <div id="foo" :class="bar.baz">
    &#123;&#123; world.burn() &#125;&#125;
    <div v-if="ok">yes</div>
    <template v-else>no</template>
    <div v-for="(value, index) in list"><span>&#123;&#123; value + index &#125;&#125;</span></div>
    </div>
  `.trim()
​
  test('function mode', () => &#123;
    const result = compile(source, &#123;
      sourceMap: true,
      filename: `foo.vue`
    &#125;)
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的调用 compile 函数就是编译的总入口。</p>
<p>在看模板编译这里需要了解的前置知识：</p>
<blockquote>
<p>Vue 的编译分为三个阶段，分别是 parse、transform 和 condegen。parse 阶段负责将模板字符串解析为抽象语法树 AST; transform 阶段是对 AST 进行转换，也就是在 AST 上增加一些标记，方便在 condegen 阶段更快生成可执行代码，也可以理解成对 AST 的优化; condegen 阶段就是根据 AST 生成对应的 render 函数字符串。</p>
</blockquote>
<p>接下来开始进入 compile 方法。</p>
<h1 data-id="heading-1">解析</h1>
<p>解析是整个模板编译的第一步，对应的伪代码如下：</p>
<pre><code class="copyable">const ast = baseParse(template, options)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来可以看一下 baseParse 中的代码</p>
<pre><code class="copyable">export function baseParse(
 content: string,
 options: ParserOptions = &#123;&#125;
): RootNode &#123;
  const context = createParserContext(content, options)
  const start = getCursor(context)
  return createRoot(
    parseChildren(context, TextModes.DATA, []),
    getSelection(context, start)
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里先创建了一个解析的上下文得到 context; 后续调用了 getCursor 方法，这个方法其实就是从 context 中取出了 column、line、offset 三个值返回一个对象赋值给了 start; 最后将 createRoot 的返回值 return 了出去，从这里可以知道解析的核心逻辑是在 createRoot 方法中。</p>
<p>因为调用 createRoot 的时候将 parseChildren 和 getSelection 两个方法的返回值传了进去，所以需要先看一下这两个方法。</p>
<h2 data-id="heading-2">createRoot 的参数一: parseChildren 方法的返回值</h2>
<p>通过这个方法名称也可以看出来这个方法是用来解析子节点的。</p>
<p>看完整个方法之后可以得出的<strong>结论</strong>是</p>
<ol start="0">
<li>解析标签是通过正则来匹配各个标签以及这个标签是开始标签还是结束标签。</li>
<li>在匹配的过程中会将当前匹配的开始标签放到缓存中，如果当前标签有自己子节点的话会先去解析子节点并将子节点的开始标签也 push 到缓存中，只有当子节点解析完成之后，才会将子节点的开始标签从缓存中取出来，这个时候父节点就知道子节点解析完成了，然后开始解析父节点的后半部分。</li>
<li>通过第 2 点也可以知道在解析的过程中是遵循了深度优先的原则。</li>
</ol>
<p>函数的返回值就是解析完成后的子节点组成的 AST。</p>
<h2 data-id="heading-3">createRoot 的参数而: getSelection 方法的返回值</h2>
<p>这个方法是用来获取当前节点的在源代码中的位置信息，最终的返回值就是这些位置信息。</p>
<pre><code class="copyable">return &#123;
  start,
  end,
  source: context.originalSource.slice(start.offset, end.offset)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>知道了 parseChildren 和 getSelection 两个方法的返回值后就可以去看 createRoot 方法了。</p>
<h2 data-id="heading-4">createRoot 方法</h2>
<pre><code class="copyable">export function createRoot(
  children: TemplateChildNode[],
  loc = locStub
): RootNode &#123;
  return &#123;
    type: NodeTypes.ROOT,
    children,
    helpers: [],
    components: [],
    directives: [],
    hoists: [],
    imports: [],
    cached: 0,
    temps: 0,
    codegenNode: undefined,
    loc
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法很简单，就是创建了一个根节点的 AST 并把 type 设置为了 ROOT，children 就是 parseChildren 方法的返回值，也就是所有子节点的 AST。</p>
<p>当执行完 createRoot 方法之后，模板对应的 AST 就全部生成了。</p>
<h1 data-id="heading-5">优化</h1>
<p>优化 AST 阶段对应的是 transform 方法。</p>
<p>还是先来看 transform 的调用</p>
<pre><code class="copyable">transform(
  ast,
  extend(&#123;&#125;, options, &#123;
    prefixIdentifiers,
    nodeTransforms: [
      ...nodeTransforms,
      ...(options.nodeTransforms || []) // user transforms
    ],
    directiveTransforms: extend(
      &#123;&#125;,
      directiveTransforms,
      options.directiveTransforms || &#123;&#125; // user transforms
    )
  &#125;)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要说明的参数有</p>
<ol start="0">
<li>
<p>prefixIdentifiers: 这个参数决定了代码生成方式。代码生成方式有两种:</p>
<ul>
<li>function 模式，特点是使用 <code>const &#123; helpers... &#125; = Vue</code> 的方式来引入帮助函数。向外导出使用 <code>return</code> 返回整个 <code>render()</code> 函数。</li>
<li>module 模式，特点是使用 es6 模块来导入导出函数，也就是使用 import 和 export。</li>
</ul>
</li>
<li>
<p>nodeTransforms 和 directiveTransforms 这两个参数分别是针对 node 和 directive 的单独优化。这两个参数都是从 getBaseTransformPreset 方法中得到的，在这个方法中可以看到这两个参数分别对应的是什么</p>
<ul>
<li>
<p>nodeTransforms 对应的是</p>
<pre><code class="copyable">transformOnce,
transformIf,
transformFor,
...[transformFilter],
...[
    trackVForSlotScopes,
    transformExpression
],
transformSlotOutlet,
transformElement,
trackSlotScopes,
transformText
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>directiveTransforms 对应的是</p>
<pre><code class="copyable">on: transformOn,
bind: transformBind,
model: transformModel
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>这就可以看出在各种节点和指令都会有专门的优化方法。</p>
</li>
</ol>
<p>看完这些参数就可以去看 transform 方法了。</p>
<pre><code class="copyable">export function transform(root: RootNode, options: TransformOptions) &#123;
    const context = createTransformContext(root, options)
​
    traverseNode(root, context)
​
    if (options.hoistStatic) &#123;
        hoistStatic(root, context)
    &#125;
​
    if (!options.ssr) &#123;
        createRootCodegen(root, context)
    &#125;
    // finalize meta information
    root.helpers = [...context.helpers.keys()]
    root.components = [...context.components]
    root.directives = [...context.directives]
    root.imports = context.imports
    root.hoists = context.hoists
    root.temps = context.temps
    root.cached = context.cached
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一步就是创建了一个上下文，里边初始化了一些属性及方法，具体的内容根据后边用到的再去看。</p>
<p>接下来就是调用了 traverseNode、hoistStatic、createRooCodegen 三个方法; 后边又将 context 中的属性赋值到了 root Vnode 上。</p>
<p>下面来分别看看那三个方法。</p>
<h2 data-id="heading-6">traverseNode</h2>
<pre><code class="copyable">export function traverseNode(
 node: RootNode | TemplateChildNode,
 context: TransformContext
) &#123;
   // ... 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个方法里可以分为三部分来看</p>
<h3 data-id="heading-7">第一部分</h3>
<p>伪代码如下：</p>
<pre><code class="copyable">// apply transform plugins
const &#123; nodeTransforms &#125; = context
const exitFns = []
for (let i = 0; i < nodeTransforms.length; i++) &#123;
    const onExit = nodeTransforms[i](node, context)
    if (onExit) &#123;
        if (isArray(onExit)) &#123;
            exitFns.push(...onExit)
        &#125; else &#123;
            exitFns.push(onExit)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码中从 context 中获取到了 nodeTransforms , 这个属性是一开始调用 transform 方法的时候传进来的，里边包含了对各种类型节点的 transform 方法。</p>
<p>所以这段代码的作用就是把当前 node 传入每个 nodeTransform 来处理当前 node，然后将每个 nodeTransform 的返回结果赋值给 onExit，再将 onExit push 到 exitFns 中。</p>
<blockquote>
<p>通过 onExit 可以判断每个 nodeTransform 的返回值还是一个函数。</p>
</blockquote>
<h4 data-id="heading-8">产生的问题</h4>
<ul>
<li>
<p>每个 nodeTransform 都干了什么？</p>
<p>这里用 transformElement 来举例，<strong>因为 transformElement 方法是一个所有 AST Element 都会被执行的一个方法</strong>。</p>
<p>在函数的最后可以看到会给传入的 node 中的 codegenNode 属性赋值</p>
<pre><code class="copyable">export const transformElement: NodeTransform = (node, context) => &#123;
  return function postTransformElement() &#123;
    // ...
    node.codegenNode = createVNodeCall(
      context,
      vnodeTag,
      vnodeProps,
      vnodeChildren,
      vnodePatchFlag,
      vnodeDynamicProps,
      vnodeDirectives,
      !!shouldUseBlock,
      false /* disableTracking */,
      node.loc
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>内容就是方法 createVNodeCall 的返回值，createVNodeCall 方法如下</p>
<pre><code class="copyable">export function createVNodeCall(
  context: TransformContext | null,
  tag: VNodeCall['tag'],
  props?: VNodeCall['props'],
  children?: VNodeCall['children'],
  patchFlag?: VNodeCall['patchFlag'],
  dynamicProps?: VNodeCall['dynamicProps'],
  directives?: VNodeCall['directives'],
  isBlock: VNodeCall['isBlock'] = false,
  disableTracking: VNodeCall['disableTracking'] = false,
  loc = locStub
): VNodeCall &#123;
  if (context) &#123;
    if (isBlock) &#123;
      context.helper(OPEN_BLOCK)
      context.helper(CREATE_BLOCK)
    &#125; else &#123;
      context.helper(CREATE_VNODE)
    &#125;
    if (directives) &#123;
      context.helper(WITH_DIRECTIVES)
    &#125;
  &#125;
​
  return &#123;
    type: NodeTypes.VNODE_CALL,
    tag,
    props,
    children,
    patchFlag,
    dynamicProps,
    directives,
    isBlock,
    disableTracking,
    loc
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到函数中调用了 context.helper 方法，其实这个方法就是把调用 helper 方法时传入的参数添加到 context.helpers 中</p>
<blockquote>
<p>context.helpers 由 symbol 类型组成的一个 set 数据结构，每一个 symbol 值就是当前节点创建、渲染等处理函数名称。</p>
</blockquote>
<p>除了调用 context.helper 方法就是 return 了一个 VNode。</p>
<p>看到这里就可以发现 transformElement 方法中对 node.codegenNode 属性的赋值知识赋了一个 VNode。但是 transform 方法不应该是针对各种节点类型来做优化的吗？这个优化在哪里呢？这里的优化其实是利用了 patchFlag 这个属性。那这个 patchFlag 是怎么促成优化的呢？</p>
<p>其实是<strong>在 diff 过程中会根据 patchFlag 进行优化</strong>。patchFlag 的所有值如下:</p>
<pre><code class="copyable">  // 标识具有动态 textContent（子级快速路径）的元素
  TEXT = 1, // 1
​
  // 标识具有动态类绑定的元素
  CLASS = 1 << 1, // 2
​
  // 标识具有动态 style 的节点
  STYLE = 1 << 2, // 4
​
  /**
   * Indicates an element that has non-class/style dynamic props.
   * Can also be on a component that has any dynamic props (includes
   * class/style). 
   * when this flag is present, the vnode also has a dynamicProps
   * array that contains the keys of the props that may change so the runtime
   * can diff them faster (without having to worry about removed props)
   */
  PROPS = 1 << 3, // 8
​
  /**
   * Indicates an element with props with dynamic keys. When keys change, a full
   * diff is always needed to remove the old key. This flag is mutually
   * exclusive with CLASS, STYLE and PROPS.
   */
  FULL_PROPS = 1 << 4, // 16
​
  // 标识具有事件监听的节点
  HYDRATE_EVENTS = 1 << 5, // 32
​
  // 标识一个不会改变子节点顺序的 fragment 
  STABLE_FRAGMENT = 1 << 6, // 64
​
  // 标识有 key 的 fragment 或者部分有 key 的子节点
  KEYED_FRAGMENT = 1 << 7, // 128
​
  // 标识一个子节点没有 key 的 framgent
  UNKEYED_FRAGMENT = 1 << 8, // 256
​
  // 标识只需要非 props 比较的节点
  NEED_PATCH = 1 << 9, // 512
​
  // 标识一个动态 slots 的组件
  DYNAMIC_SLOTS = 1 << 10, // 1024
​
  DEV_ROOT_FRAGMENT = 1 << 11,
​
  // 标识一个静态节点，静态节点从来不会更新，在优化的时候可以跳过
  HOISTED = -1,
​
  // 指示在 diff 过程应该要退出优化模式，不是 render 函数生成的一些元素，例如 renderSlot
  BAIL = -2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总体来看 patchFlag 分为两大类</p>
<ol>
<li>值大于 0 时则表示对应的元素在 diff 过程中是可以优化生成或更新的</li>
</ol>

<ol start="2">
<li>值小于 0 时则表示当前元素是可以跳过的</li>
</ol>
<p><strong>现在就可以回答 nodeTransform 方法都做了什么，在这个过程中是给所有节点加上了 patchFlag 属性，以便在 diff 过程中进行优化</strong>。</p>
</li>
</ul>
<h3 data-id="heading-9">第二部分</h3>
<pre><code class="copyable">switch (node.type) &#123;
  case NodeTypes.COMMENT:
    if (!context.ssr) &#123;
      // inject import for the Comment symbol, which is needed for creating
      // comment nodes with `createVNode`
      context.helper(CREATE_COMMENT)
    &#125;
    break
​
  case NodeTypes.INTERPOLATION:
    // no need to traverse, but we need to inject toString helper
    if (!context.ssr) &#123;
      context.helper(TO_DISPLAY_STRING)
    &#125;
    break
​
    // for container types, further traverse downwards
  case NodeTypes.IF:
    for (let i = 0; i < node.branches.length; i++) &#123;
      traverseNode(node.branches[i], context)
    &#125;
    break
  case NodeTypes.IF_BRANCH:
  case NodeTypes.FOR:
  case NodeTypes.ELEMENT:
  case NodeTypes.ROOT:
    traverseChildren(node, context)
    break
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里调用了三个方法</p>
<ol>
<li>
<p>context.helper 在第一部分中提到过，这里来看一下他的具体实现</p>
<pre><code class="copyable">helper(name) &#123;
  const count = context.helpers.get(name) || 0
  context.helpers.set(name, count + 1)
  return name
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里就是将其传入的 name set 到了 helpers 中，key 是 name，value 是 name 在 helpers 中出现的次数。</p>
</li>
<li>
<p>如果 node.type 为 NodeTypes.IF 类型则遍历了一个 if 的其他分支然后递归调用了 traverseNode</p>
</li>
<li>
<p>如果 node.type 为 NodeTypes.IF_BRANCH、NodeTypes.FOR、NodeTypes.ELEMENT、NodeTypes.ROOT 类型则调用 traverseChildren 方法</p>
<pre><code class="copyable">export function traverseChildren(
  parent: ParentNode,
  context: TransformContext
) &#123;
  let i = 0
  const nodeRemoved = () => &#123;
    i--
  &#125;
  for (; i < parent.children.length; i++) &#123;
    const child = parent.children[i]
    if (isString(child)) continue
    context.parent = parent
    context.childIndex = i
    context.onNodeRemoved = nodeRemoved
    traverseNode(child, context)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过代码可以看到，在 traverseChildren 方法中也没有过多的操作，只是遍历了当前节点的子节点，然后每一个子节点都去调用 traverseNode 方法。</p>
</li>
</ol>
<p><strong>在这一部分主要就是给 node 对应的 context 中的 helpers 属性添加了每个节点对应的处理方法</strong>。这里 helpers 中的值什么时候会用到呢？是在生成可执行代码阶段根据这些方法名会将其对应的方法引入。</p>
<h3 data-id="heading-10">第三部分</h3>
<pre><code class="copyable">// exit transforms
context.currentNode = node
let i = exitFns.length
while (i--) &#123;
  exitFns[i]()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里就是将第一部分的调用结果分别再调用一遍。看了第一部分之后可以知道 exitFns 里存放的都是方法。</p>
<h3 data-id="heading-11">总结</h3>
<p>通过 traverseNode 方法可以得到是他会对每个 node 上的 codegenNode 属性进行赋值，在 codegenNode 中会有一个 patchFlag 值。这里会在 diff 的时候用到。</p>
<p>在 node 对应的 context 中还会有一个 helpers 属性，这里存放了每个节点应该什么样的处理的方法名。这里的会在代码生成阶段用到，会将这里的所有方法引入。</p>
<h2 data-id="heading-12">hoistStatic</h2>
<p>这里就是 vue3 相对于 vue2 的另外一个优化点: 静态提升。</p>
<h3 data-id="heading-13">什么是静态提升</h3>
<p>静态提升就是将静态节点提升到 render 函数外边生成，后续 render 函数有变化的时候就可以直接引用这个已经生成的函数，并不需要再次创建。</p>
<p>这个可以通过生成的渲染函数来看就会很明显</p>
<ul>
<li>Template:</li>
</ul>
<pre><code class="copyable"><div>
  <div>123</div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Render:</li>
</ul>
<pre><code class="copyable">import &#123; createElementVNode as _createElementVNode, openBlock as _openBlock, createElementBlock as _createElementBlock &#125; from "vue"
​
const _hoisted_1 = /*#__PURE__*/_createElementVNode("div", null, "123", -1 /* HOISTED */)
const _hoisted_2 = [
  _hoisted_1
]
​
export function render(_ctx, _cache, $props, $setup, $data, $options) &#123;
  return (_openBlock(), _createElementBlock("div", null, _hoisted_2))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这个 render 函数就可以看到，上边的 div 以及其中的值都是静态的，一成不变的值，开启静态提升之后就会将创建静态节点的方法提升到 render 函数外边。</p>
<h3 data-id="heading-14">hoistStatic 方法</h3>
<pre><code class="copyable">export function hoistStatic(root: RootNode, context: TransformContext) &#123;
  walk(
    root,
    context,
    // Root node is unfortunately non-hoistable due to potential parent
    // fallthrough attributes.
    isSingleElementRoot(root, root.children[0])
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个方法中是直接调用了 walk 方法，在调用 walk 方法之前调用了 isSingleElementRoot 方法，这个方法就是判断了是不是根节点，因为根节点是不可被提升的。</p>
<p>在 walk 方法主要是对当前节点的子节点的操作</p>
<ol>
<li>
<p>更改子节点 child 的 codegenNode 中的 patchFlag 值</p>
<pre><code class="copyable">(child.codegenNode as VNodeCall).patchFlag = PatchFlags.HOISTED + (__DEV__ ? ` /* HOISTED */` : ``)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>将 child 的 codegenNode push 到 context.hoists 中，这一步是调用了 context 中的 hoist 方法</p>
<pre><code class="copyable">context.hoist(child.codegenNode!)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>hoist 方法如下</p>
<pre><code class="copyable">hoist(exp) &#123;
  context.hoists.push(exp)
  const identifier = createSimpleExpression(
    `_hoisted_$&#123;context.hoists.length&#125;`,
    false,
    exp.loc,
    ConstantTypes.CAN_HOIST
  )
  identifier.hoisted = exp
  return identifier
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法的一开始就是进行 push 操作，后续又调用 createSimpleExpression 方法创建了一个标识符 identifier。createSimpleExpression 方法内部就是将传入的值加上一个 type 组成了一个对象 return 了出来</p>
<pre><code class="copyable">export function createSimpleExpression(
  content: SimpleExpressionNode['content'],
  isStatic: SimpleExpressionNode['isStatic'],
  loc: SourceLocation = locStub,
  constType: ConstantTypes = ConstantTypes.NOT_CONSTANT
): SimpleExpressionNode &#123;
  return &#123;
    type: NodeTypes.SIMPLE_EXPRESSION,
    loc,
    content,
    isStatic,
    constType: isStatic ? ConstantTypes.CAN_STRINGIFY : constType
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>hoist 方法将这个 identifier return 了出去，也就产生了 walk 方法的第三个操作。</p>
</li>
<li>
<p>将 hoist 方法的返回值赋值给了 child.codegenNode</p>
<pre><code class="copyable">child.codegenNode = context.hoist(child.codegenNode!)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>

<ol start="4">
<li>如果当前子节点是一个动态的，但是他的 props 有可能是可以被提升的，这个时候也会调用 hoist 方法将 child 的 props 添加到 context.hoists 中，然后将 hoist 方法的返回值赋值给 codegenNode.props。</li>
</ol>

<ol start="5">
<li>后边就是如果 child 的 type 是 element、for、if、类型的话就遍历他们的子节点或分支然后递归调用 walk 方法。</li>
</ol>
<h3 data-id="heading-15">总结</h3>
<ul>
<li>在这个方法中处理了所有静态节点，将所有的静态节点的 codegenNode 都 push 到根节点的上下文中的 hoists 数组中。</li>
</ul>

<ul>
<li>对当前静态节点的 codegenNode 进行赋值。</li>
</ul>
<h3 data-id="heading-16">问题</h3>
<ul>
<li>
<p>为什么将所有的静态节点的 codegenNode 都 push 到根节点的上下文中的 hoists 数组中？</p>
<p>这应该也就属于静态提升的其中一步，这样的话可以最快的找到所有的静态节点并将其对应的 render 函数创建出来，也就不需要再去遍历每一个节点去寻找静态节点。</p>
</li>
</ul>
<h2 data-id="heading-17">createRootCodegen</h2>
<p>前边那些都是对子节点的处理，现在要创建出根节点的 codegen。</p>
<p>伪代码如下</p>
<pre><code class="copyable">function createRootCodegen(root: RootNode, context: TransformContext) &#123;
  const &#123; helper, removeHelper &#125; = context
  const &#123; children &#125; = root
  if (children.length === 1) &#123;
    const child = children[0]
    // if the single child is an element, turn it into a block.
    if (isSingleElementRoot(root, child) && child.codegenNode) &#123;
      const codegenNode = child.codegenNode
      root.codegenNode = codegenNode
    &#125; else &#123;
      // - single <slot/>, IfNode, ForNode: already blocks.
      // - single text node: always patched.
      // root codegen falls through via genNode()
      root.codegenNode = child
    &#125;
  &#125; else if (children.length > 1) &#123;
    // root has multiple nodes - return a fragment block.
    let patchFlag = PatchFlags.STABLE_FRAGMENT
    let patchFlagText = PatchFlagNames[PatchFlags.STABLE_FRAGMENT]
​
    root.codegenNode = createVNodeCall(
      context,
      helper(FRAGMENT),
      undefined,
      root.children,
      patchFlag + (__DEV__ ? ` /* $&#123;patchFlagText&#125; */` : ``),
      undefined,
      undefined,
      true
    )
  &#125; else &#123;
    // no children = noop. codegen will return null.
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中处理了只有一个自己子节点和更多子节点。</p>
<p>如果只有一个子节点则判断子节点中是否有 codegenNode 属性，如果有则 root.codegenNode 就是子节点的 codegenNode，反之 root.codegenNode 就是子节点本身。</p>
<p>如果有更多子节点则调用前边提到的 createVNodeCall 方法来生成 root.codegenNode。</p>
<h1 data-id="heading-18">生成可执行代码</h1>
<p>这一部分是通过 generate 方法来生成的。主要也可以分为 5 个部分</p>
<ol>
<li>
<p>创建上下文</p>
<pre><code class="copyable">const context = createCodegenContext(ast, options)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>根据 prefixIdentifiers 字段决定代码生成采用 module 还是 function 的形式，这两种方式在上边已经说过。</p>
</li>
<li>
<p>根据不同的引入方式引入 helpers 中的方法</p>
<pre><code class="copyable">if (!__BROWSER__ && mode === 'module') &#123;
  genModulePreamble(ast, preambleContext, genScopeId, isSetupInlined)
&#125; else &#123;
  genFunctionPreamble(ast, preambleContext)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>genModulePreamble 和 genFunctionPreamble 方法都是用来引入 helpers 中的方法的，只不过是引入方式的不同。</p>
</li>
<li>
<p>向 context.code 中添加、追加可执行的代码字符串</p>
<p>这里就是频繁的调用 push、indent、newline、deindent 等方法来对代码字符串中的格式进行优化</p>
</li>
<li>
<p>将最终的结果 return，在最终的数据里 code 就是可执行代码字符串，ast 就是抽象语法树。</p>
<pre><code class="copyable">&#123;
  ast,
  code: context.code,
  preamble: isSetupInlined ? preambleContext.code : ``,
  // SourceMapGenerator does have toJSON() method but it's not in the types
  map: context.map ? (context.map as any).toJSON() : undefined
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>到这一步，所有的模板解析过程就结束了。</p>
<h1 data-id="heading-19">参考链接</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000023594560" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000023594560" ref="nofollow noopener noreferrer">Vue3 模板编译原理</a></li>
<li><a href="https://juejin.cn/post/6874419253865365511" target="_blank" title="https://juejin.cn/post/6874419253865365511">从编译过程，理解 Vue3 静态节点提升 | 源码解读</a></li>
</ul></div>  
</div>
            