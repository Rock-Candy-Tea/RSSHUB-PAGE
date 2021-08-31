
---
title: '_Element Plus 源码解析_ Popper 弹框'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2461'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 23:00:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=2461'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">一、组件介绍</h2>
<p><code>element-plus</code>的官方文档中没有<code>ElPopper</code>组件，<code>ElPopper</code>在其他组件内部使用，如：<code>Select、Cascade、ColorPicker</code>等组件中都用到了<code>ElPopper</code>；</p>
<p>官方文档中提供的弹框组件是<code>ElPopover</code>，这两个组件之间的关系非常密切，这里先分析<code>ElPopper</code>组件。</p>
<h2 data-id="heading-1">二、源码分析</h2>
<h3 data-id="heading-2">2.1 popper.ts</h3>
<p><code>ElPopper</code>组件及其子组件都使用render函数编写。</p>
<p><code>popper.ts</code>对应弹出内容</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// packages\components\popper\src\renderers\popper.ts</span>
<span class="hljs-comment">// 参数：</span>
<span class="hljs-comment">// props: 传入的属性</span>
<span class="hljs-comment">// children: 子元素数组 </span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderPopper</span>(<span class="hljs-params">
  props: IRenderPopperProps,
  children: VNode[],
</span>) </span>&#123;
  <span class="hljs-comment">// 从props中解构出对应属性</span>
  <span class="hljs-keyword">const</span> &#123;
    effect,
    name,
    stopPopperMouseEvent,
    popperClass,
    popperStyle,
    popperRef,
    pure,
    popperId,
    visibility,
    onMouseenter,
    onMouseleave,
    onAfterEnter,
    onAfterLeave,
    onBeforeEnter,
    onBeforeLeave,
  &#125; = props

  <span class="hljs-comment">// 动态class，缩写挺逗的</span>
  <span class="hljs-keyword">const</span> kls = [
    popperClass,
    <span class="hljs-string">'el-popper'</span>,
    <span class="hljs-string">'is-'</span> + effect,
    pure ? <span class="hljs-string">'is-pure'</span> : <span class="hljs-string">''</span>,
  ]
  
  <span class="hljs-comment">// 鼠标按下/松开事件 stop = (e: Event) => e.stopPropagation()</span>
  <span class="hljs-keyword">const</span> mouseUpAndDown = stopPopperMouseEvent ? stop : NOOP
  <span class="hljs-comment">// render函数</span>
  <span class="hljs-keyword">return</span> h(
    <span class="hljs-comment">// 外层组件，使用vue官方过渡组件</span>
    Transition,
    <span class="hljs-comment">// 属性，主要是过渡事件</span>
    &#123;
      name,
      <span class="hljs-string">'onAfterEnter'</span>: onAfterEnter,
      <span class="hljs-string">'onAfterLeave'</span>: onAfterLeave,
      <span class="hljs-string">'onBeforeEnter'</span>: onBeforeEnter,
      <span class="hljs-string">'onBeforeLeave'</span>: onBeforeLeave,
    &#125;,
    <span class="hljs-comment">// slots</span>
    &#123;
      <span class="hljs-comment">// 默认插槽</span>
      <span class="hljs-comment">// withCtx withDirectives 是vue官方内部方法，</span>
      <span class="hljs-attr">default</span>: withCtx(<span class="hljs-function">() =></span> [withDirectives(
        <span class="hljs-comment">// 内部元素，部分传入的属性绑定在这一层元素上</span>
        h(
          <span class="hljs-string">'div'</span>,
          &#123;
            <span class="hljs-string">'aria-hidden'</span>: <span class="hljs-built_in">String</span>(!visibility),
            <span class="hljs-attr">class</span>: kls,
            <span class="hljs-attr">style</span>: popperStyle ?? &#123;&#125;,
            <span class="hljs-attr">id</span>: popperId,
            <span class="hljs-attr">ref</span>: popperRef ?? <span class="hljs-string">'popperRef'</span>,
            <span class="hljs-attr">role</span>: <span class="hljs-string">'tooltip'</span>,
            onMouseenter,
            onMouseleave,
            <span class="hljs-attr">onClick</span>: stop,
            <span class="hljs-attr">onMousedown</span>: mouseUpAndDown,
            <span class="hljs-attr">onMouseup</span>: mouseUpAndDown,
          &#125;,
          children,
        ),
        <span class="hljs-comment">// 指令，等同于 v-show="visibility"</span>
        [[vShow, visibility]],
      )]),
    &#125;,
  )
  <span class="hljs-comment">/**
   * 以上render函数，等同于：
   * <transition :name="name">
   *  <div v-show="visibility" :aria-hidden="!visibility" :class="kls" ref="popperRef" role="tooltip" <span class="hljs-doctag">@mouseenter</span>="" <span class="hljs-doctag">@mouseleave</span>="" <span class="hljs-doctag">@click</span>="">
   *    <slot />
   *  </div>
   * </transition>
   */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：</p>
<ul>
<li><code>popper.ts</code>提供了<code>renderPopper</code>方法，该方法接收2个参数：传入的属性及子元素数组；</li>
<li><code>renderPopper</code>方法中，外层使用<code>Transition</code>组件展示过渡效果，内层使用div标签，将相应属性绑定在这一层div标签上，传入的children子元素作为这一层div的子元素。</li>
</ul>
<h3 data-id="heading-3">2.2 trigger.ts</h3>
<p><code>trigger.ts</code>对应触发部分</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// packages\components\popper\src\renderers\trigger.ts</span>

<span class="hljs-keyword">interface</span> IRenderTriggerProps <span class="hljs-keyword">extends</span> Record<string, unknown> &#123;
  <span class="hljs-attr">ref</span>: <span class="hljs-built_in">string</span> | Ref<ComponentPublicInstance | HTMLElement>
  onClick?: EventHandler
  onMouseover?: EventHandler
  onMouseleave?: EventHandler
  onFocus?: EventHandler
&#125;

<span class="hljs-comment">// 参数：</span>
<span class="hljs-comment">// 1、元素数组 2、传入的属性</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderTrigger</span>(<span class="hljs-params">trigger: VNode[], extraProps: IRenderTriggerProps</span>) </span>&#123;
  <span class="hljs-comment">// 获取第一个有效的VNode节点</span>
  <span class="hljs-keyword">const</span> firstElement = getFirstValidNode(trigger, <span class="hljs-number">1</span>)
  <span class="hljs-comment">// 没有有效VNode节点则报错提示</span>
  <span class="hljs-keyword">if</span> (!firstElement) throwError(<span class="hljs-string">'renderTrigger'</span>, <span class="hljs-string">'trigger expects single rooted node'</span>)
  <span class="hljs-comment">// 使用vue的cloneVNode api，将extraProps和firstElement的props融合</span>
  <span class="hljs-keyword">return</span> cloneVNode(firstElement, extraProps, <span class="hljs-literal">true</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：</p>
<ul>
<li><code>trigger.ts</code>的逻辑比较简单，找到第一个有效的VNode节点，并且将一些额外的属性融入到VNode节点中。</li>
</ul>
<h3 data-id="heading-4">2.3 arrow.ts</h3>
<p><code>arrow.ts</code>是弹框的箭头部分</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// packages\components\popper\src\renderers\arrow.ts</span>

<span class="hljs-comment">// 参数：1、是否展示箭头</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderArrow</span>(<span class="hljs-params">showArrow: <span class="hljs-built_in">boolean</span></span>) </span>&#123;
  <span class="hljs-comment">// 根据showArrow决定是否展示箭头</span>
  <span class="hljs-keyword">return</span> showArrow
    ? h(
      <span class="hljs-string">'div'</span>,
      &#123;
        <span class="hljs-attr">ref</span>: <span class="hljs-string">'arrowRef'</span>,
        <span class="hljs-attr">class</span>: <span class="hljs-string">'el-popper__arrow'</span>,
        <span class="hljs-string">'data-popper-arrow'</span>: <span class="hljs-string">''</span>,
      &#125;,
      <span class="hljs-literal">null</span>,
    )
    : h(Comment, <span class="hljs-literal">null</span>, <span class="hljs-string">''</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>arrow.ts</code>的逻辑更加简单，根据传入的<code>showArrow</code>参数决定是否展示箭头。</p>
<h3 data-id="heading-5">2.4 index.vue</h3>
<p>前面介绍了<code>ElPopper</code>的3个子组件部分，现在来看一下组件本身的<code>index.vue</code></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// packages\components\popper\src\index.vue</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: compName,
  <span class="hljs-attr">props</span>: defaultProps,
  <span class="hljs-attr">emits</span>: [UPDATE_VISIBLE_EVENT, <span class="hljs-string">'after-enter'</span>, <span class="hljs-string">'after-leave'</span>, <span class="hljs-string">'before-enter'</span>, <span class="hljs-string">'before-leave'</span>],
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, ctx</span>)</span> &#123;
    <span class="hljs-comment">// 如果用户没有写trigger插槽，则报错提示：必须提供trigger</span>
    <span class="hljs-keyword">if</span> (!ctx.slots.trigger) &#123;
      throwError(compName, <span class="hljs-string">'Trigger must be provided'</span>)
    &#125;
    <span class="hljs-comment">// 调用usePopper，返回值是popper的状态数据</span>
    <span class="hljs-keyword">const</span> popperStates = usePopper(props, ctx)
    <span class="hljs-comment">// 封装强制销毁方法</span>
    <span class="hljs-keyword">const</span> forceDestroy = <span class="hljs-function">() =></span> popperStates.doDestroy(<span class="hljs-literal">true</span>)
    <span class="hljs-comment">// 挂载时调用initializePopper</span>
    onMounted(popperStates.initializePopper)
    <span class="hljs-comment">// 卸载时销毁</span>
    onBeforeUnmount(forceDestroy)
    <span class="hljs-comment">// keep-alive激活时调用initializePopper</span>
    onActivated(popperStates.initializePopper)
    <span class="hljs-comment">// 失效时销毁</span>
    onDeactivated(forceDestroy)

    <span class="hljs-comment">// 返回状态数据</span>
    <span class="hljs-keyword">return</span> popperStates
  &#125;,

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 从this上解构属性，其中一部分属性是setup函数返回的，一部分是vue组件初始化时生成的</span>
    <span class="hljs-keyword">const</span> &#123;
      $slots,
      appendToBody,
      <span class="hljs-attr">class</span>: kls,
      style,
      effect,
      hide,
      onPopperMouseEnter,
      onPopperMouseLeave,
      onAfterEnter,
      onAfterLeave,
      onBeforeEnter,
      onBeforeLeave,
      popperClass,
      popperId,
      popperStyle,
      pure,
      showArrow,
      transition,
      visibility,
      stopPopperMouseEvent,
    &#125; = <span class="hljs-built_in">this</span>

    <span class="hljs-comment">// 是否手动触发模式</span>
    <span class="hljs-keyword">const</span> isManual = <span class="hljs-built_in">this</span>.isManualMode()
    <span class="hljs-comment">// 箭头</span>
    <span class="hljs-keyword">const</span> arrow = renderArrow(showArrow)
    <span class="hljs-comment">// 弹框</span>
    <span class="hljs-keyword">const</span> popper = renderPopper(
      <span class="hljs-comment">// 属性</span>
      &#123;
        effect,
        <span class="hljs-attr">name</span>: transition,
        popperClass,
        popperId,
        popperStyle,
        pure,
        stopPopperMouseEvent,
        <span class="hljs-attr">onMouseenter</span>: onPopperMouseEnter,
        <span class="hljs-attr">onMouseleave</span>: onPopperMouseLeave,
        onAfterEnter,
        onAfterLeave,
        onBeforeEnter,
        onBeforeLeave,
        visibility,
      &#125;,
      <span class="hljs-comment">// children</span>
      [
        <span class="hljs-comment">// 默认插槽内容</span>
        renderSlot($slots, <span class="hljs-string">'default'</span>, &#123;&#125;, <span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">return</span> [toDisplayString(<span class="hljs-built_in">this</span>.content)]
        &#125;),
        <span class="hljs-comment">// 箭头</span>
        arrow,
      ],
    )
    <span class="hljs-comment">// trigger slot</span>
    <span class="hljs-keyword">const</span> _t = $slots.trigger?.()
    <span class="hljs-comment">// trigger props</span>
    <span class="hljs-keyword">const</span> triggerProps = &#123;
      <span class="hljs-string">'aria-describedby'</span>: popperId,
      <span class="hljs-attr">class</span>: kls,
      style,
      <span class="hljs-attr">ref</span>: <span class="hljs-string">'triggerRef'</span>,
      ...this.events,
    &#125;
    <span class="hljs-comment">// 根据是否手动触发，决定是否给trigger添加clickOutside指令</span>
    <span class="hljs-keyword">const</span> trigger = isManual
      ? renderTrigger(_t, triggerProps)
      : withDirectives(renderTrigger(_t, triggerProps), [[ClickOutside, hide]])
    <span class="hljs-comment">// Fragment是vue内置的片段，其不会渲染出任何节点</span>
    <span class="hljs-keyword">return</span> h(Fragment, <span class="hljs-literal">null</span>, 
    <span class="hljs-comment">// children</span>
    [
      <span class="hljs-comment">// 触发元素</span>
      trigger,
      <span class="hljs-comment">// Teleport是vue内置的传送门组件，将子元素渲染到to指定的元素中</span>
      <span class="hljs-comment">// 这里的to赋值为body,即弹框部分挂载到body下</span>
      h(
        Teleport <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>, <span class="hljs-comment">// Vue did not support createVNode for Teleport</span>
        &#123;
          <span class="hljs-attr">to</span>: <span class="hljs-string">'body'</span>,
          <span class="hljs-comment">// 若appendToBody值为false，则禁用传送门</span>
          <span class="hljs-attr">disabled</span>: !appendToBody,
        &#125;,
        <span class="hljs-comment">// 弹框内容</span>
        [popper],
      ),
    ])
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：</p>
<ul>
<li>在<code>setup</code>方法中调用<code>usePopper</code>方法生成popper的状态数据；并注册生命周期钩子函数，在挂载/激活时调用<code>initializePopper</code>方法，在卸载/失效时调用<code>doDestroy(true)</code>；</li>
<li>在<code>render</code>函数中，首先通过解构赋值的方式从this上获取相应的属性值；调用<code>renderArrow/renderPopper/renderTrigger</code>生成相应子模块，调用时传入相应模块所需的属性值；</li>
<li>使用<code>Teleport</code>传送门组件，将popper部分挂载到body上</li>
</ul>
<h3 data-id="heading-6">2.5 use-popper/index.ts</h3>
<p>在上面的<code>index.vue</code>中，其setup函数内调用了<code>userPopper</code>方法，我们进一步分析一下这个方法：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// packages\components\popper\src\use-popper\index.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">
  props: IPopperOptions,
  &#123; emit &#125;: SetupContext<EmitType[]>,
</span>) </span>&#123;
  <span class="hljs-comment">// arrow trigger popper三个部分的ref</span>
  <span class="hljs-keyword">const</span> arrowRef = ref<RefElement>(<span class="hljs-literal">null</span>)
  <span class="hljs-keyword">const</span> triggerRef = ref(<span class="hljs-literal">null</span>) <span class="hljs-keyword">as</span> Ref<ElementType>
  <span class="hljs-keyword">const</span> popperRef = ref<RefElement>(<span class="hljs-literal">null</span>)

  <span class="hljs-comment">// 生成唯一的随机id</span>
  <span class="hljs-keyword">const</span> popperId = <span class="hljs-string">`el-popper-<span class="hljs-subst">$&#123;generateId()&#125;</span>`</span>
  <span class="hljs-keyword">let</span> popperInstance: Nullable<PopperInstance> = <span class="hljs-literal">null</span>
  <span class="hljs-comment">// 延迟出现的计时器，即触发显示后，延迟一段时间再显示</span>
  <span class="hljs-keyword">let</span> showTimer: Nullable<TimeoutHandle> = <span class="hljs-literal">null</span>
  <span class="hljs-comment">// 自动隐藏计时器，即显示弹框后，一段时间后自动隐藏</span>
  <span class="hljs-keyword">let</span> hideTimer: Nullable<TimeoutHandle> = <span class="hljs-literal">null</span>
  <span class="hljs-comment">// trigger的focus状态</span>
  <span class="hljs-keyword">let</span> triggerFocused = <span class="hljs-literal">false</span>

  <span class="hljs-comment">// 是否手动触发模式</span>
  <span class="hljs-keyword">const</span> isManualMode = <span class="hljs-function">() =></span> props.manualMode || props.trigger === <span class="hljs-string">'manual'</span>

  <span class="hljs-comment">// popper的动态样式，这里是通过PopupManager生成一个zIndex值</span>
  <span class="hljs-keyword">const</span> popperStyle = ref<CSSProperties>(&#123; <span class="hljs-attr">zIndex</span>: PopupManager.nextZIndex() &#125;)

  <span class="hljs-comment">// 调用usePopperOptions生成popperOptions</span>
  <span class="hljs-keyword">const</span> popperOptions = usePopperOptions(props, &#123;
    <span class="hljs-attr">arrow</span>: arrowRef,
  &#125;)

  <span class="hljs-comment">// 响应式数据，将props.visible的值转换成boolean类型，</span>
  <span class="hljs-keyword">const</span> state = reactive(&#123;
    <span class="hljs-attr">visible</span>: !!props.visible,
  &#125;)
  <span class="hljs-comment">// visible has been taken by props.visible, avoiding name collision</span>
  <span class="hljs-comment">// Either marking type here or setter parameter</span>
  <span class="hljs-comment">// 计算属性visibility，有get和set方法</span>
  <span class="hljs-keyword">const</span> visibility = computed<<span class="hljs-built_in">boolean</span>>(&#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (props.disabled) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> isBool(props.visible) ? props.visible : state.visible
      &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (isManualMode()) <span class="hljs-keyword">return</span>
      isBool(props.visible)
        ? emit(UPDATE_VISIBLE_EVENT, val)
        : (state.visible = val)
    &#125;,
  &#125;)
  <span class="hljs-comment">// 内部的show方法</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_show</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// autoClose用户控制弹框出现后，自动隐藏的延迟，若为0则不会自动隐藏</span>
    <span class="hljs-keyword">if</span> (props.autoClose > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// 定时器，时间到时调用_hide隐藏</span>
      hideTimer = <span class="hljs-built_in">window</span>.setTimeout(<span class="hljs-function">() =></span> &#123;
        _hide()
      &#125;, props.autoClose)
    &#125;
    visibility.value = <span class="hljs-literal">true</span>
  &#125;
  <span class="hljs-comment">// 内部的hide方法</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_hide</span>(<span class="hljs-params"></span>) </span>&#123;
    visibility.value = <span class="hljs-literal">false</span>
  &#125;

  <span class="hljs-comment">// 清除计时器，包括showTimer和hideTimer</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clearTimers</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">clearTimeout</span>(showTimer)
    <span class="hljs-built_in">clearTimeout</span>(hideTimer)
  &#125;
  
  <span class="hljs-comment">// 展示</span>
  <span class="hljs-keyword">const</span> show = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (isManualMode() || props.disabled) <span class="hljs-keyword">return</span>
    <span class="hljs-comment">// 清除计时器</span>
    clearTimers()
    <span class="hljs-keyword">if</span> (props.showAfter === <span class="hljs-number">0</span>) &#123;
      _show()
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 有延迟显示时，使用计时器</span>
      showTimer = <span class="hljs-built_in">window</span>.setTimeout(<span class="hljs-function">() =></span> &#123;
        _show()
      &#125;, props.showAfter)
    &#125;
  &#125;

  <span class="hljs-comment">// 隐藏</span>
  <span class="hljs-keyword">const</span> hide = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (isManualMode()) <span class="hljs-keyword">return</span>
    <span class="hljs-comment">// 清除计时器</span>
    clearTimers()
    <span class="hljs-keyword">if</span> (props.hideAfter > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// 若有延迟关闭，则使用计时器</span>
      hideTimer = <span class="hljs-built_in">window</span>.setTimeout(<span class="hljs-function">() =></span> &#123;
        close()
      &#125;, props.hideAfter)
    &#125; <span class="hljs-keyword">else</span> &#123;
      close()
    &#125;
  &#125;
  <span class="hljs-comment">// 关闭</span>
  <span class="hljs-keyword">const</span> close = <span class="hljs-function">() =></span> &#123;
    _hide()
    <span class="hljs-keyword">if</span> (props.disabled) &#123;
      <span class="hljs-comment">// 如果禁用，调用销毁</span>
      doDestroy(<span class="hljs-literal">true</span>)
    &#125;
  &#125;
  <span class="hljs-comment">// 鼠标进入popper事件处理函数</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onPopperMouseEnter</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// trigger非click模式下，鼠标进入popper，清除自动隐藏计时器</span>
    <span class="hljs-keyword">if</span> (props.enterable && props.trigger !== <span class="hljs-string">'click'</span>) &#123;
      <span class="hljs-built_in">clearTimeout</span>(hideTimer)
    &#125;
  &#125;
  <span class="hljs-comment">// 鼠标离开popper事件处理函数</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onPopperMouseLeave</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123; trigger &#125; = props
    
    <span class="hljs-keyword">const</span> shouldPrevent =
      (isString(trigger) && (trigger === <span class="hljs-string">'click'</span> || trigger === <span class="hljs-string">'focus'</span>)) ||
      (trigger.length === <span class="hljs-number">1</span> &&
        (trigger[<span class="hljs-number">0</span>] === <span class="hljs-string">'click'</span> || trigger[<span class="hljs-number">0</span>] === <span class="hljs-string">'focus'</span>))
    <span class="hljs-comment">// trigger是click或focus时，不触发关闭弹框    </span>
    <span class="hljs-keyword">if</span> (shouldPrevent) <span class="hljs-keyword">return</span>
    <span class="hljs-comment">// trigger是hover时关闭弹框，因为hide方法中对manual模式进行了判断，因此只有hover模式下会关闭</span>
    hide()
  &#125;

  <span class="hljs-comment">// 初始化 popper</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initializePopper</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// $()方法是element-plus自定义的一个方法，作用是直接拿到ref类型数据的value值</span>
    <span class="hljs-comment">//  function $<T>(ref: Ref<T>) &#123;</span>
    <span class="hljs-comment">//    return ref.value</span>
    <span class="hljs-comment">//  &#125;</span>
    <span class="hljs-keyword">if</span> (!$(visibility)) &#123;
      <span class="hljs-comment">// 隐藏状态下，直接return</span>
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-keyword">const</span> unwrappedTrigger = $(triggerRef)
    <span class="hljs-comment">// 判断trigger元素是HTML原生元素还是vue组件</span>
    <span class="hljs-comment">// 如果是组件，取其$el</span>
    <span class="hljs-keyword">const</span> _trigger = isHTMLElement(unwrappedTrigger)
      ? unwrappedTrigger
      : (unwrappedTrigger <span class="hljs-keyword">as</span> ComponentPublicInstance).$el
    <span class="hljs-comment">// 关键点：createPopper是popperjs库提供的方法</span>
    <span class="hljs-comment">// createPopper接收3个参数：1、reference，即触发弹框的对象；2、popper: 即弹框元素；3、popperOptions：即弹框配置</span>
    popperInstance = createPopper(_trigger, $(popperRef), $(popperOptions))
    <span class="hljs-comment">// 调用update</span>
    popperInstance.update()
  &#125;

  <span class="hljs-comment">// 销毁</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">doDestroy</span>(<span class="hljs-params">forceDestroy?: <span class="hljs-built_in">boolean</span></span>) </span>&#123;
    <span class="hljs-comment">/* istanbul ignore if */</span>
    <span class="hljs-keyword">if</span> (!popperInstance || ($(visibility) && !forceDestroy)) <span class="hljs-keyword">return</span>
    detachPopper()
  &#125;
  
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">detachPopper</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 调用popperjs的destroy方法</span>
    popperInstance?.destroy?.()
    popperInstance = <span class="hljs-literal">null</span>
  &#125;

  <span class="hljs-keyword">const</span> events = &#123;&#125; <span class="hljs-keyword">as</span> PopperEvents

  <span class="hljs-comment">// 显示切换副作用函数</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onVisibilityChange</span>(<span class="hljs-params">toState: <span class="hljs-built_in">boolean</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (toState) &#123;
      <span class="hljs-comment">// 变成可见状态时，更新zIndex</span>
      popperStyle.value.zIndex = PopupManager.nextZIndex()
      <span class="hljs-comment">// 重新调用initializePopper</span>
      initializePopper()
    &#125;
  &#125;
  <span class="hljs-comment">// 显示切换时，调用显示切换副作用函数</span>
  watch(visibility, onVisibilityChange)

  <span class="hljs-comment">// 非自动触发模式下</span>
  <span class="hljs-keyword">if</span> (!isManualMode()) &#123;
    <span class="hljs-comment">// 定义切换显示方法</span>
    <span class="hljs-keyword">const</span> toggleState = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> ($(visibility)) &#123;
        hide()
      &#125; <span class="hljs-keyword">else</span> &#123;
        show()
      &#125;
    &#125;

    <span class="hljs-comment">// 定义事件处理函数</span>
    <span class="hljs-keyword">const</span> popperEventsHandler = <span class="hljs-function">(<span class="hljs-params">e: Event</span>) =></span> &#123;
      <span class="hljs-comment">// 阻止冒泡</span>
      e.stopPropagation()
      <span class="hljs-keyword">switch</span> (e.type) &#123;
        <span class="hljs-comment">// 点击事件</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'click'</span>: &#123;
          <span class="hljs-keyword">if</span> (triggerFocused) &#123;
            <span class="hljs-comment">// 当前focus，则调整为非focus</span>
            triggerFocused = <span class="hljs-literal">false</span>
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 当前非focus，则切换显示状态</span>
            toggleState()
          &#125;
          <span class="hljs-keyword">break</span>
        &#125;
        <span class="hljs-comment">// 鼠标进入事件</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'mouseenter'</span>: &#123;
          <span class="hljs-comment">// 显示</span>
          show()
          <span class="hljs-keyword">break</span>
        &#125;
        <span class="hljs-comment">// 鼠标移出事件</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'mouseleave'</span>: &#123;
          <span class="hljs-comment">// 隐藏</span>
          hide()
          <span class="hljs-keyword">break</span>
        &#125;
        <span class="hljs-comment">// focus事件</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'focus'</span>: &#123;
          <span class="hljs-comment">// 置为focus状态，并显示</span>
          triggerFocused = <span class="hljs-literal">true</span>
          show()
          <span class="hljs-keyword">break</span>
        &#125;
        <span class="hljs-comment">// 失焦事件</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'blur'</span>: &#123;
          <span class="hljs-comment">// 置为非focus状态，并隐藏</span>
          triggerFocused = <span class="hljs-literal">false</span>
          hide()
          <span class="hljs-keyword">break</span>
        &#125;
      &#125;
    &#125;
    <span class="hljs-comment">// 根据trigger类型，绑定对应事件</span>
    <span class="hljs-keyword">const</span> triggerEventsMap: Partial<Record<TriggerType, (keyof PopperEvents)[]>> = &#123;
      <span class="hljs-comment">// click类型，绑定onClick事件</span>
      <span class="hljs-attr">click</span>: [<span class="hljs-string">'onClick'</span>],
      <span class="hljs-comment">// hover类型，绑定onMouseenter onMouseleave 事件</span>
      <span class="hljs-attr">hover</span>: [<span class="hljs-string">'onMouseenter'</span>, <span class="hljs-string">'onMouseleave'</span>],
      <span class="hljs-comment">// focus类型，绑定onFocus onBlur事件</span>
      <span class="hljs-attr">focus</span>: [<span class="hljs-string">'onFocus'</span>, <span class="hljs-string">'onBlur'</span>],
    &#125;
    
    <span class="hljs-keyword">const</span> mapEvents = <span class="hljs-function">(<span class="hljs-params">t: TriggerType</span>) =></span> &#123;
      triggerEventsMap[t].forEach(<span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
        <span class="hljs-comment">// 各个事件的响应函数都一样，popperEventsHandler函数内部针对event type进行处理</span>
        events[event] = popperEventsHandler
      &#125;)
    &#125;

    <span class="hljs-keyword">if</span> (isArray(props.trigger)) &#123;
      <span class="hljs-built_in">Object</span>.values(props.trigger).forEach(mapEvents)
    &#125; <span class="hljs-keyword">else</span> &#123;
      mapEvents(props.trigger <span class="hljs-keyword">as</span> TriggerType)
    &#125;
  &#125;

  <span class="hljs-comment">// popperOptions变化时，使用popperjs的setOptions方法重新设置，并update</span>
  watch(popperOptions, <span class="hljs-function"><span class="hljs-params">val</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (!popperInstance) <span class="hljs-keyword">return</span>
    popperInstance.setOptions(val)
    popperInstance.update()
  &#125;)

  <span class="hljs-keyword">return</span> &#123;
    doDestroy,
    show,
    hide,
    onPopperMouseEnter,
    onPopperMouseLeave,
    <span class="hljs-attr">onAfterEnter</span>: <span class="hljs-function">() =></span> &#123;
      emit(<span class="hljs-string">'after-enter'</span>)
    &#125;,
    <span class="hljs-attr">onAfterLeave</span>: <span class="hljs-function">() =></span> &#123;
      detachPopper()
      emit(<span class="hljs-string">'after-leave'</span>)
    &#125;,
    <span class="hljs-attr">onBeforeEnter</span>: <span class="hljs-function">() =></span> &#123;
      emit(<span class="hljs-string">'before-enter'</span>)
    &#125;,
    <span class="hljs-attr">onBeforeLeave</span>: <span class="hljs-function">() =></span> &#123;
      emit(<span class="hljs-string">'before-leave'</span>)
    &#125;,
    initializePopper,
    isManualMode,
    arrowRef,
    events,
    popperId,
    popperInstance,
    popperRef,
    popperStyle,
    triggerRef,
    visibility,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>usePopper</code>总结：</p>
<ul>
<li><code>usePopper</code>方法中，定义了属性和方法，维护弹框的显示状态；</li>
<li><code>usePopper</code>方法中，调用第三方库<code>popperjs</code>控制弹框的实际显示位置；</li>
<li><code>usePopper</code>方法中，为<code>trigger</code>绑定相应的事件处理函数，控制弹框的展示隐藏。</li>
</ul></div>  
</div>
            