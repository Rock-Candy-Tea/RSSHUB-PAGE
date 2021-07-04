
---
title: '浅谈Vue3 effect'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5105'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 20:54:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=5105'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Vue3 中引入了 proxy进行数据劫持，而<code>effect</code> 是响应式系统的核心，而响应式系统又是 <code>vue3</code> 中的核心，所以从 <code>effect</code> 开始讲起。</p>
<p>首先看下面 <code>effect</code> 的传参，<code>fn</code> 是回调函数，<code>options</code> 是传入的参数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">effect</span><<span class="hljs-title">T</span> = <span class="hljs-title">any</span>>(<span class="hljs-params">
  fn: () => T,
  options: ReactiveEffectOptions = EMPTY_OBJ
</span>): <span class="hljs-title">ReactiveEffect</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-keyword">if</span> (isEffect(fn)) &#123;
    fn = fn.raw
  &#125;
  <span class="hljs-keyword">const</span> effect = createReactiveEffect(fn, options)
  <span class="hljs-keyword">if</span> (!options.lazy) &#123;
    effect()
  &#125;
  <span class="hljs-keyword">return</span> effect
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 <code>option</code> 的参数如下，都是属于可选的。</p>

































<table><thead><tr><th>参数</th><th>含义</th></tr></thead><tbody><tr><td>lazy</td><td>是否延迟触发 <code>effect</code></td></tr><tr><td>computed</td><td>是否为计算属性</td></tr><tr><td>scheduler</td><td>调度函数</td></tr><tr><td>onTrack</td><td>追踪时触发</td></tr><tr><td>onTrigger</td><td>触发回调时触发</td></tr><tr><td>onStop</td><td>停止监听时触发</td></tr></tbody></table>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> interface ReactiveEffectOptions &#123;
  lazy?: boolean
  computed?: boolean
  scheduler?: <span class="hljs-function">(<span class="hljs-params">job: ReactiveEffect</span>) =></span> <span class="hljs-keyword">void</span>
  onTrack?: <span class="hljs-function">(<span class="hljs-params">event: DebuggerEvent</span>) =></span> <span class="hljs-keyword">void</span>
  onTrigger?: <span class="hljs-function">(<span class="hljs-params">event: DebuggerEvent</span>) =></span> <span class="hljs-keyword">void</span>
  onStop?: <span class="hljs-function">() =></span> <span class="hljs-keyword">void</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分析完参数之后，继续我们一开始的分析。当我们调用 <code>effect</code> 时，首先判断传入的 <code>fn</code> 是否是 <code>effect</code>，如果是，取出原始值，然后调用 <code>createReactiveEffect</code> 创建 新的<code>effect</code>， 如果传入的 <code>option</code> 中的 <code>lazy</code> 不为为 true，则立即调用我们刚刚创建的 <code>effect</code>, 最后返回刚刚创建的 <code>effect</code>。</p>
<p>那么 <code>createReactiveEffect</code> 是怎样是创建 <code>effect</code>的呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createReactiveEffect</span><<span class="hljs-title">T</span> = <span class="hljs-title">any</span>>(<span class="hljs-params">
  fn: (...args: any[]) => T,
  options: ReactiveEffectOptions
</span>): <span class="hljs-title">ReactiveEffect</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-keyword">const</span> effect = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveEffect</span>(<span class="hljs-params">...args: unknown[]</span>): <span class="hljs-title">unknown</span> </span>&#123;
    <span class="hljs-keyword">if</span> (!effect.active) &#123;
      <span class="hljs-keyword">return</span> options.scheduler ? <span class="hljs-literal">undefined</span> : fn(...args)
    &#125;
    <span class="hljs-keyword">if</span> (!effectStack.includes(effect)) &#123;
      cleanup(effect)
      <span class="hljs-keyword">try</span> &#123;
        enableTracking()
        effectStack.push(effect)
        activeEffect = effect
        <span class="hljs-keyword">return</span> fn(...args)
      &#125; <span class="hljs-keyword">finally</span> &#123;
        effectStack.pop()
        resetTracking()
        activeEffect = effectStack[effectStack.length - <span class="hljs-number">1</span>]
      &#125;
    &#125;
  &#125; <span class="hljs-keyword">as</span> ReactiveEffect
  effect.id = uid++
  effect._isEffect = <span class="hljs-literal">true</span>
  effect.active = <span class="hljs-literal">true</span>
  effect.raw = fn
  effect.deps = []
  effect.options = options
  <span class="hljs-keyword">return</span> effect
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先忽略 <code>reactiveEffect</code>，继续看下面的挂载的属性。</p>

































<table><thead><tr><th>effect 挂载属性</th><th>含义</th></tr></thead><tbody><tr><td>id</td><td>自增id， 唯一标识effect</td></tr><tr><td>_isEffect</td><td>用于标识方法是否是effect</td></tr><tr><td>active</td><td>effect 是否激活</td></tr><tr><td>raw</td><td>创建effect是传入的fn</td></tr><tr><td>deps</td><td>持有当前 effect 的dep 数组</td></tr><tr><td>options</td><td>创建effect是传入的options</td></tr></tbody></table>
<p>回到 <code>reactiveEffect</code>，如果 effect 不是激活状态，这种情况发生在我们调用了 effect 中的 stop 方法之后，那么先前没有传入调用 scheduler 函数的话，直接调用原始方法fn，否则直接返回。</p>
<p>那么处于激活状态的 effect 要怎么进行处理呢？首先判断是否当前 effect 是否在 effectStack 当中，如果在，则不进行调用，这个主要是为了避免死循环。拿下面测试用例来看</p>
<pre><code class="hljs language-js copyable" lang="js">it(<span class="hljs-string">'should avoid infinite loops with other effects'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> nums = reactive(&#123; <span class="hljs-attr">num1</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">num2</span>: <span class="hljs-number">1</span> &#125;)

    <span class="hljs-keyword">const</span> spy1 = jest.fn(<span class="hljs-function">() =></span> (nums.num1 = nums.num2))
    <span class="hljs-keyword">const</span> spy2 = jest.fn(<span class="hljs-function">() =></span> (nums.num2 = nums.num1))
    effect(spy1)
    effect(spy2)
    expect(nums.num1).toBe(<span class="hljs-number">1</span>)
    expect(nums.num2).toBe(<span class="hljs-number">1</span>)
    expect(spy1).toHaveBeenCalledTimes(<span class="hljs-number">1</span>)
    expect(spy2).toHaveBeenCalledTimes(<span class="hljs-number">1</span>)
    nums.num2 = <span class="hljs-number">4</span>
    expect(nums.num1).toBe(<span class="hljs-number">4</span>)
    expect(nums.num2).toBe(<span class="hljs-number">4</span>)
    expect(spy1).toHaveBeenCalledTimes(<span class="hljs-number">2</span>)
    expect(spy2).toHaveBeenCalledTimes(<span class="hljs-number">2</span>)
    nums.num1 = <span class="hljs-number">10</span>
    expect(nums.num1).toBe(<span class="hljs-number">10</span>)
    expect(nums.num2).toBe(<span class="hljs-number">10</span>)
    expect(spy1).toHaveBeenCalledTimes(<span class="hljs-number">3</span>)
    expect(spy2).toHaveBeenCalledTimes(<span class="hljs-number">3</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果不加 effectStack，会导致 num2 改变，触发了 spy1, spy1 里面 num1 改变又触发了 spy2, spy2 又会改变 num2，从而触发了死循环。</p>
<p>接着是清除依赖，每次 effect 运行都会重新收集依赖, deps 是持有 effect 的依赖数组，其中里面的每个 dep 是对应对象某个 key 的 全部依赖，我们在这里需要做的就是首先把 effect 从 dep 中删除，最后把 deps 数组清空。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cleanup</span>(<span class="hljs-params">effect: ReactiveEffect</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; deps &#125; = effect
  <span class="hljs-keyword">if</span> (deps.length) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < deps.length; i++) &#123;
      deps[i].delete(effect)
    &#125;
    deps.length = <span class="hljs-number">0</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>清除完依赖，就开始重新收集依赖。首先开启依赖收集，把当前 effect 放入 effectStack 中，然后讲 activeEffect 设置为当前的 effect，activeEffect 主要为了在收集依赖的时候使用（在下面会很快讲到），然后调用 fn 并且返回值，当这一切完成的时候，finally 阶段，会把当前 effect 弹出，恢复原来的收集依赖的状态，还有恢复原来的 activeEffect。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">try</span> &#123;
    enableTracking()
    effectStack.push(effect)
    activeEffect = effect
    <span class="hljs-keyword">return</span> fn(...args)
  &#125; <span class="hljs-keyword">finally</span> &#123;
    effectStack.pop()
    resetTracking()
    activeEffect = effectStack[effectStack.length - <span class="hljs-number">1</span>]
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那 effect 是怎么收集依赖的呢？vue3 利用 proxy 劫持对象，在上面运行 effect 中读取对象的时候，当前对象的 key 的依赖 set集合 会把 effect 收集进去。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">track</span>(<span class="hljs-params">target: object, type: TrackOpTypes, key: unknown</span>) </span>&#123;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vue3 在 reactive 中触发 track 函数，reactive 会在单独的章节讲。触发 track 的参数中，object 表示触发 track 的对象， type 代表触发 track 类型，而 key 则是 触发 track 的 object 的 key。在下面可以看到三种类型的读取对象会触发 track，分别是 get、 has、 iterate。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> enum TrackOpTypes &#123;
  GET = <span class="hljs-string">'get'</span>,
  HAS = <span class="hljs-string">'has'</span>,
  ITERATE = <span class="hljs-string">'iterate'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>回到 track 内部，如果 shouldTrack 为 false 或者 activeEffect 为空，则不进行依赖收集。接着 targetMap 里面有没有该对象，没有新建 map，然后再看这个 map 有没有这个对象的对应 key 的 依赖 set 集合，没有则新建一个。 如果对象对应的 key 的 依赖 set 集合也没有当前 activeEffect， 则把 activeEffect 加到 set 里面，同时把 当前 set 塞到 activeEffect 的 deps 数组。最后如果是开发环境而且传入了 onTrack 函数，则触发 onTrack。
所以 deps 就是 effect 中所依赖的 key 对应的 set 集合数组， 毕竟一般来说，effect 中不止依赖一个对象或者不止依赖一个对象的一个key，而且 一个对象可以能不止被一个 effect 使用，所以是 set 集合数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (!shouldTrack || activeEffect === <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-keyword">let</span> depsMap = targetMap.get(target)
  <span class="hljs-keyword">if</span> (!depsMap) &#123;
    targetMap.set(target, (depsMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()))
  &#125;
  <span class="hljs-keyword">let</span> dep = depsMap.get(key)
  <span class="hljs-keyword">if</span> (!dep) &#123;
    depsMap.set(key, (dep = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()))
  &#125;
  <span class="hljs-keyword">if</span> (!dep.has(activeEffect)) &#123;
    dep.add(activeEffect)
    activeEffect.deps.push(dep)
    <span class="hljs-keyword">if</span> (__DEV__ && activeEffect.options.onTrack) &#123;
      activeEffect.options.onTrack(&#123;
        <span class="hljs-attr">effect</span>: activeEffect,
        target,
        type,
        key
      &#125;)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>依赖都收集完毕了，接下来就是触发依赖。如果 targetMap 为空，说明这个对象没有被追踪，直接return。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trigger</span>(<span class="hljs-params">
  target: object,
  type: TriggerOpTypes,
  key?: unknown,
  newValue?: unknown,
  oldValue?: unknown,
  oldTarget?: <span class="hljs-built_in">Map</span><unknown, unknown> | <span class="hljs-built_in">Set</span><unknown>
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> depsMap = targetMap.get(target)
  <span class="hljs-keyword">if</span> (!depsMap) &#123;
    <span class="hljs-comment">// never been tracked</span>
    <span class="hljs-keyword">return</span>
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中触发的 type, 包括了 set、add、delete 和 clear。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> enum TriggerOpTypes &#123;
  SET = <span class="hljs-string">'set'</span>,
  ADD = <span class="hljs-string">'add'</span>,
  DELETE = <span class="hljs-string">'delete'</span>,
  CLEAR = <span class="hljs-string">'clear'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来对 key 收集的依赖进行分组，computedRunners 具有更高的优先级，会触发下游的 effects 重新收集依赖，</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> effects = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span><ReactiveEffect>()
<span class="hljs-keyword">const</span> computedRunners = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span><ReactiveEffect>()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>add 方法是将 effect 添加进不同分组的函数，其中 effect !== activeEffect 这个是为了避免死循环，在下面的注释也写的很清楚，避免出现 foo.value++ 这种情况。至于为什么是 set 呢，要避免 effect 多次运行。就好像循环中，set 触发了 trigger ，那么 ITERATE 和 当前 key 可能都属于同个 effect，这样就可以避免多次运行了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">effectsToAdd: <span class="hljs-built_in">Set</span><ReactiveEffect> | <span class="hljs-literal">undefined</span></span>) =></span> &#123;
<span class="hljs-keyword">if</span> (effectsToAdd) &#123;
  effectsToAdd.forEach(<span class="hljs-function"><span class="hljs-params">effect</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (effect !== activeEffect || !shouldTrack) &#123;
      <span class="hljs-keyword">if</span> (effect.options.computed) &#123;
        computedRunners.add(effect)
      &#125; <span class="hljs-keyword">else</span> &#123;
        effects.add(effect)
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// the effect mutated its own dependency during its execution.</span>
      <span class="hljs-comment">// this can be caused by operations like foo.value++</span>
      <span class="hljs-comment">// do not trigger or we end in an infinite loop</span>
    &#125;
  &#125;)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面根据触发 key 类型的不同进行 effect 的处理。如果是 clear 类型，则触发这个对象所有的 effect。如果 key 是 length , 而且 target 是数组，则会触发 key 为 length 的 effects ，以及 key 大于等于新 length的 effects， 因为这些此时数组长度变化了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (type === TriggerOpTypes.CLEAR) &#123;
    <span class="hljs-comment">// collection being cleared</span>
    <span class="hljs-comment">// trigger all effects for target</span>
    depsMap.forEach(add)
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'length'</span> && isArray(target)) &#123;
    depsMap.forEach(<span class="hljs-function">(<span class="hljs-params">dep, key</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'length'</span> || key >= (newValue <span class="hljs-keyword">as</span> number)) &#123;
        add(dep)
      &#125;
    &#125;)
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面则是对正常的新增、修改、删除进行 effect 的分组, isAddOrDelete 表示新增 或者不是数组的删除，这为了对迭代 key的 effect 进行触发，如果 isAddOrDelete 为 true 或者是 map 对象的设值，则触发 isArray(target) ? 'length' : ITERATE_KEY 的 effect ，如果 isAddOrDelete 为 true 且 对象为 map， 则触发 MAP_KEY_ITERATE_KEY 的 effect</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// schedule runs for SET | ADD | DELETE</span>
    <span class="hljs-keyword">if</span> (key !== <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>) &#123;
      add(depsMap.get(key))
    &#125;
    <span class="hljs-comment">// also run for iteration key on ADD | DELETE | Map.SET</span>
    <span class="hljs-keyword">const</span> isAddOrDelete =
      type === TriggerOpTypes.ADD ||
      (type === TriggerOpTypes.DELETE && !isArray(target))
    <span class="hljs-keyword">if</span> (
      isAddOrDelete ||
      (type === TriggerOpTypes.SET && target <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Map</span>)
    ) &#123;
      add(depsMap.get(isArray(target) ? <span class="hljs-string">'length'</span> : ITERATE_KEY))
    &#125;
    <span class="hljs-keyword">if</span> (isAddOrDelete && target <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Map</span>) &#123;
      add(depsMap.get(MAP_KEY_ITERATE_KEY))
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后是运行 effect， 像上面所说的，computed effects 会优先运行，因为 computed effects 在运行过程中，第一次会触发上游把cumputed effect收集进去，再把下游 effect 收集起来。</p>
<p>还有一点，就是 effect.options.scheduler，如果传入了调度函数，则通过 scheduler 函数去运行 effect， 但是 scheduler 里面可能不一定使用了 effect，例如 computed 里面，因为 computed 是延迟运行 effect， 这个会在讲 computed 的时候再讲。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> run = <span class="hljs-function">(<span class="hljs-params">effect: ReactiveEffect</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (__DEV__ && effect.options.onTrigger) &#123;
      effect.options.onTrigger(&#123;
        effect,
        target,
        key,
        type,
        newValue,
        oldValue,
        oldTarget
      &#125;)
    &#125;
    <span class="hljs-keyword">if</span> (effect.options.scheduler) &#123;
      effect.options.scheduler(effect)
    &#125; <span class="hljs-keyword">else</span> &#123;
      effect()
    &#125;
&#125;

<span class="hljs-comment">// Important: computed effects must be run first so that computed getters</span>
<span class="hljs-comment">// can be invalidated before any normal effects that depend on them are run.</span>
computedRunners.forEach(run)
effects.forEach(run)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以发现，不管是 track 还是 trigger， 都会导致 effect 重新运行去收集依赖。</p>
<p>最后再讲一个 stop 方法，当我们调用 stop 方法后，会清空其他对象对 effect 的依赖，同时调用 onStop 回调，最后将 effect 的激活状态设置为 false</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">stop</span>(<span class="hljs-params">effect: ReactiveEffect</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (effect.active) &#123;
    cleanup(effect)
    <span class="hljs-keyword">if</span> (effect.options.onStop) &#123;
      effect.options.onStop()
    &#125;
    effect.active = <span class="hljs-literal">false</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样当再一次调用 effect 的时候，不会进行依赖的重新收集，而且没有调度函数，就直接返回原始的 fn 的运行结果，否则直接返回 undefined。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (!effect.active) &#123;
  <span class="hljs-keyword">return</span> options.scheduler ? <span class="hljs-literal">undefined</span> : fn(...args)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            