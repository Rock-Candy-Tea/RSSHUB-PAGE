
---
title: 'Vue 指令之 v-icon-tooltip 实现指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c894d26f3d5c4d3b94305617c1a50aa1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 01:09:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c894d26f3d5c4d3b94305617c1a50aa1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>又是充满希望的一天！</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>最近项目的各个模块及特殊操作需要增加名词解释，效果图如下，功能很简单，但现有的 <code>Tooltip</code> 组件却无法满足新需求，为此单独开发 <code>IconTooltip</code> 组件，并基于该组件进行 <code>v-icon-tooltip</code> 指令开发。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c894d26f3d5c4d3b94305617c1a50aa1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">Todo list</h2>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" checked disabled> 指定元素后面追加名词解释图标</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 交互方式为单击切换提示信息</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 通过指令简易配置即可实现需求</li>
</ul>
<h2 data-id="heading-2">IconTooltip</h2>
<p>UI 框架使用的是 <code>ViewDesign@4.5</code> 版本，<code>Tooltip</code> 组件本身只支持悬停方式显示，但是可以通过提供的 <code>disabled</code> 和 <code>always</code> 来控制提示信息的显示时机。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// components/IconTooltip/icon-tooltip.vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>
    <span class="hljs-attr">ref</span>=<span class="hljs-string">"mainRef"</span>
    <span class="hljs-attr">class</span>=<span class="hljs-string">"icon-tooltip-wrapper"</span>
    <span class="hljs-attr">:style</span>=<span class="hljs-string">"wrapperStyles"</span>
    <span class="hljs-attr">:class</span>=<span class="hljs-string">"classes"</span>
    @<span class="hljs-attr">click.stop</span>
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">Tooltip</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"tooltipProps"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Icon</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">"icon"</span>
        <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"iconProps"</span>
        <span class="hljs-attr">v-click-outside:</span>[<span class="hljs-attr">capture</span>]=<span class="hljs-string">"onClickOutside"</span>
        <span class="hljs-attr">v-click-outside:</span>[<span class="hljs-attr">capture</span>]<span class="hljs-attr">.mousedown</span>=<span class="hljs-string">"onClickOutside"</span>
        <span class="hljs-attr">v-click-outside:</span>[<span class="hljs-attr">capture</span>]<span class="hljs-attr">.touchstart</span>=<span class="hljs-string">"onClickOutside"</span>
        @<span class="hljs-attr">click.native</span>=<span class="hljs-string">"onIconClick"</span>
      /></span>
    <span class="hljs-tag"></<span class="hljs-name">Tooltip</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineProps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/util'</span>
<span class="hljs-keyword">import</span> &#123; pick &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'lodash'</span>
<span class="hljs-keyword">import</span> &#123; directive <span class="hljs-keyword">as</span> ClickOutside &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/directives/v-click-outside'</span>

<span class="hljs-comment">/**
 * Tooltip 触发类型
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> TRIGGER_TYPE = <span class="hljs-built_in">Object</span>.freeze(&#123;
  <span class="hljs-attr">click</span>: <span class="hljs-string">'click'</span>,
  <span class="hljs-attr">hover</span>: <span class="hljs-string">'hover'</span>
&#125;)

<span class="hljs-keyword">const</span> ICON_PROP_KEYS = <span class="hljs-built_in">Object</span>.freeze([<span class="hljs-string">'icon'</span>, <span class="hljs-string">'custom'</span>, <span class="hljs-string">'color'</span>, <span class="hljs-string">'size'</span>])
<span class="hljs-keyword">const</span> TOOLTIP_PROP_KEYS = <span class="hljs-built_in">Object</span>.freeze([
  <span class="hljs-string">'content'</span>,
  <span class="hljs-string">'placement'</span>,
  <span class="hljs-string">'theme'</span>,
  <span class="hljs-string">'maxWidth'</span>,
  <span class="hljs-string">'transfer'</span>,
  <span class="hljs-string">'disabled'</span>,
  <span class="hljs-string">'always'</span>
])

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'IconTooltip'</span>,
  <span class="hljs-attr">directives</span>: &#123; ClickOutside &#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">icon</span>: defineProps(<span class="hljs-built_in">String</span>),
    <span class="hljs-attr">custom</span>: defineProps(<span class="hljs-built_in">String</span>),
    <span class="hljs-attr">color</span>: defineProps(<span class="hljs-built_in">String</span>),
    <span class="hljs-attr">size</span>: defineProps(<span class="hljs-built_in">Number</span>, <span class="hljs-number">16</span>),
    <span class="hljs-attr">content</span>: defineProps(<span class="hljs-built_in">String</span>, <span class="hljs-string">''</span>),
    <span class="hljs-attr">triggerType</span>: defineProps(<span class="hljs-built_in">String</span>, TRIGGER_TYPE.click),
    <span class="hljs-attr">placement</span>: defineProps(<span class="hljs-built_in">String</span>, <span class="hljs-string">'top'</span>),
    <span class="hljs-attr">theme</span>: defineProps(<span class="hljs-built_in">String</span>, <span class="hljs-string">'dark'</span>),
    <span class="hljs-attr">maxWidth</span>: defineProps([<span class="hljs-built_in">String</span>, <span class="hljs-built_in">Number</span>], <span class="hljs-number">200</span>),
    <span class="hljs-attr">transfer</span>: defineProps(<span class="hljs-built_in">Boolean</span>, <span class="hljs-literal">true</span>),
    <span class="hljs-attr">capture</span>: defineProps(<span class="hljs-built_in">Boolean</span>, <span class="hljs-literal">true</span>),
    <span class="hljs-attr">styles</span>: defineProps(<span class="hljs-built_in">Object</span>, <span class="hljs-literal">null</span>),
    <span class="hljs-attr">classes</span>: defineProps([<span class="hljs-built_in">String</span>, <span class="hljs-built_in">Object</span>, <span class="hljs-built_in">Array</span>], <span class="hljs-literal">null</span>)
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// 初始化时根据当前触发类型设置是否禁用</span>
      <span class="hljs-attr">disabled</span>: <span class="hljs-built_in">this</span>.triggerType === TRIGGER_TYPE.click,
      <span class="hljs-comment">// 单击后设为 true，可一直显示 Tooltip</span>
      <span class="hljs-attr">always</span>: <span class="hljs-literal">false</span>
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">tooltipProps</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> pick(<span class="hljs-built_in">this</span>, TOOLTIP_PROP_KEYS)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">iconProps</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> props = pick(<span class="hljs-built_in">this</span>, ICON_PROP_KEYS)
      props.type = props.type || props.icon
      <span class="hljs-keyword">return</span> props
    &#125;,
    <span class="hljs-function"><span class="hljs-title">wrapperStyles</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.assign(
        &#123;&#125;,
        <span class="hljs-comment">// calc(100% + 6px) 是为了让元素以自身右边作为 x 轴的偏移起始坐标，6px 为偏移量</span>
        &#123; <span class="hljs-attr">top</span>: <span class="hljs-string">'50%'</span>, <span class="hljs-attr">right</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">transform</span>: <span class="hljs-string">'translate(calc(100% + 6px), -50%)'</span> &#125;,
        <span class="hljs-built_in">this</span>.styles
      )
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">// 单击图标外部时关闭 tooltip</span>
    <span class="hljs-function"><span class="hljs-title">onClickOutside</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.triggerType === TRIGGER_TYPE.hover) <span class="hljs-keyword">return</span>
      <span class="hljs-built_in">this</span>.disabled = <span class="hljs-literal">true</span>
      <span class="hljs-built_in">this</span>.always = <span class="hljs-literal">false</span>
    &#125;,
    <span class="hljs-comment">// 单击图标时切换 tooltip</span>
    <span class="hljs-function"><span class="hljs-title">onIconClick</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.triggerType === TRIGGER_TYPE.hover) <span class="hljs-keyword">return</span>
      <span class="hljs-built_in">this</span>.disabled = !<span class="hljs-built_in">this</span>.disabled
      <span class="hljs-built_in">this</span>.always = !<span class="hljs-built_in">this</span>.always
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">'less'</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.icon-tooltip-wrapper</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;

  & <span class="hljs-selector-class">.icon</span> &#123;
    <span class="hljs-attribute">cursor</span>: pointer;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据需求实现了需要的 <code>IconTooltip</code> 组件，在封装组件时为了方便扩展，我们将 <code>Tooltip</code> 和 <code>Icon</code> 组件的一些属性暴露给外部调用，来方便其他特殊需求的使用。</p>
<h2 data-id="heading-3">v-icon-tooltip</h2>
<p>在我当前的需求中，组件的图标是固定的，只是显示方式和内容不同，并且 <code>IconTooltip</code> 组件需要总是为其父元素设置 <code>position</code> 属性用来定位，此时在各个模块中去使用仍然比较繁琐。</p>
<p>对于一向以 <code>懒人创造世界</code> 为理念的我，决定再开发一个基于该组件的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Fcustom-directive.html" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/custom-directive.html" ref="nofollow noopener noreferrer">指令</a>来满足特定的需求。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// directives/v-icon-tooltip.js</span>
<span class="hljs-keyword">import</span> &#123; getStyle, upObjVal &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/util'</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> IconTooltip, &#123; TRIGGER_TYPE &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/IconTooltip/icon-tooltip.vue'</span>
<span class="hljs-keyword">import</span> &#123; get, omit &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'lodash'</span>

<span class="hljs-keyword">const</span> PREFIX = <span class="hljs-string">'[v-icon-tooltip]'</span>

<span class="hljs-keyword">const</span> buildContent = <span class="hljs-function">(<span class="hljs-params">binding</span>) =></span>
  (<span class="hljs-keyword">typeof</span> binding.arg === <span class="hljs-string">'string'</span> ? binding.arg : <span class="hljs-string">''</span>) || get(binding.value, <span class="hljs-string">'content'</span>, <span class="hljs-string">''</span>)

<span class="hljs-keyword">const</span> buildProps = <span class="hljs-function">(<span class="hljs-params">...props</span>) =></span>
  upObjVal(
    &#123;
      <span class="hljs-attr">icon</span>: <span class="hljs-string">'md-help-circle'</span>,
      <span class="hljs-attr">custom</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// icon props custom</span>
      <span class="hljs-attr">size</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">color</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">triggerType</span>: TRIGGER_TYPE.click, <span class="hljs-comment">// optional type: click, hover</span>
      <span class="hljs-attr">content</span>: <span class="hljs-string">''</span>,
      <span class="hljs-attr">placement</span>: <span class="hljs-string">'top'</span>,
      <span class="hljs-attr">theme</span>: <span class="hljs-string">'dark'</span>,
      <span class="hljs-attr">maxWidth</span>: <span class="hljs-number">200</span>,
      <span class="hljs-attr">transfer</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">capture</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">styles</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">classes</span>: <span class="hljs-literal">null</span>
    &#125;,
    ...props
  )

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildTooltip</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-comment">// 通过 Vue.extend 获取组件的构造器</span>
  <span class="hljs-keyword">const</span> ctor = Vue.extend(IconTooltip)
  <span class="hljs-comment">// 返回组件的实例化对象</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ctor(&#123; <span class="hljs-attr">propsData</span>: props &#125;).$mount()
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bindTooltip</span>(<span class="hljs-params">el, binding</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-string">'arg'</span> <span class="hljs-keyword">in</span> binding && <span class="hljs-keyword">typeof</span> binding.arg !== <span class="hljs-string">'string'</span>) &#123;
    <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`<span class="hljs-subst">$&#123;PREFIX&#125;</span> Binding arg must be a string.`</span>)
  &#125;

  <span class="hljs-keyword">const</span> $tooltip = buildTooltip(buildProps(binding.value, &#123; <span class="hljs-attr">content</span>: buildContent(binding) &#125;))

  el.$hasTooltip = <span class="hljs-literal">true</span>
  el.$tooltip = $tooltip

  el.appendChild($tooltip.$el)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: PREFIX,
  <span class="hljs-function"><span class="hljs-title">bind</span>(<span class="hljs-params">el, binding</span>)</span> &#123;
    bindTooltip(el, binding)
  &#125;,
  <span class="hljs-function"><span class="hljs-title">inserted</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-comment">// 获取指令挂载元素的 position 属性，这里的 getStyle 方法会获取元素包含类样式在内的 position 属性</span>
    <span class="hljs-keyword">const</span> rawPosition = getStyle(el, <span class="hljs-string">'position'</span>) || <span class="hljs-string">''</span>

    <span class="hljs-comment">// 如果原始的 position 属性可以进行定位则跳过后续步骤</span>
    <span class="hljs-keyword">if</span> (![<span class="hljs-string">''</span>, <span class="hljs-string">'static'</span>].includes(rawPosition) || <span class="hljs-string">'$rawPosition'</span> <span class="hljs-keyword">in</span> el) <span class="hljs-keyword">return</span>

    <span class="hljs-comment">// 挂载原始定位属性并设置当前定位为相对定位</span>
    el.$rawPosition = rawPosition
    el.style.position = <span class="hljs-string">'relative'</span>
  &#125;,
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params">el, binding</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (el.$hasTooltip) &#123;
      <span class="hljs-comment">// 更新除 triggerType 的其他属性值</span>
      <span class="hljs-keyword">return</span> upObjVal(
        el.$tooltip._props,
        buildProps(omit(binding.value, <span class="hljs-string">'triggerType'</span>), &#123; <span class="hljs-attr">content</span>: buildContent(binding) &#125;)
      )
    &#125;
    bindTooltip(el, binding)
  &#125;,
  <span class="hljs-function"><span class="hljs-title">unbind</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-comment">// 指令销毁时销毁组件，若无这一步则在 tooltip 使用了 transfer 时，会产生垃圾元素</span>
    el.$tooltip.$destroy()
    el.$tooltip = <span class="hljs-literal">null</span>

    <span class="hljs-comment">// 还原元素的 position 值</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-string">'$rawPosition'</span> <span class="hljs-keyword">in</span> el) &#123;
      el.style.position = el.$rawPosition
    &#125;

    <span class="hljs-comment">// 逐一删除元素上的多余属性</span>
    ;[<span class="hljs-string">'$hasTooltip'</span>, <span class="hljs-string">'$tooltip'</span>, <span class="hljs-string">'$rawPosition'</span>].forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> <span class="hljs-keyword">delete</span> el[key])
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// util/index.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> upObjVal = <span class="hljs-function">(<span class="hljs-params">target, ...sources</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> onlySource = _.merge(&#123;&#125;, ...sources)
  <span class="hljs-keyword">return</span> _.merge(target, _.pick(onlySource, <span class="hljs-built_in">Object</span>.keys(target)))
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getStyle</span>(<span class="hljs-params">el, attr, pseudo = <span class="hljs-literal">null</span></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!(el <span class="hljs-keyword">instanceof</span> HTMLElement)) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'The parameter el must be a HTMLElement.'</span>)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> attr !== <span class="hljs-string">'string'</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
  &#125;
  <span class="hljs-comment">//IE6~8不兼容backgroundPosition写法，识别backgroundPositionX/Y</span>
  <span class="hljs-keyword">if</span> (attr === <span class="hljs-string">'backgroundPosition'</span> && !+<span class="hljs-string">'\v1'</span>) &#123;
    <span class="hljs-keyword">return</span> el.currentStyle.backgroundPositionX + <span class="hljs-string">' '</span> + el.currentStyle.backgroundPositionY
  &#125;
  <span class="hljs-keyword">const</span> currentStyle = <span class="hljs-string">'currentStyle'</span> <span class="hljs-keyword">in</span> el ? el.currentStyle : <span class="hljs-built_in">document</span>.defaultView.getComputedStyle(el, pseudo)
  <span class="hljs-keyword">return</span> currentStyle[attr]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">指令使用</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0f5433108d74ba9b8512e10f5016670~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe0c1f211f304846b439fb82c855f860~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">结尾</h2>
<p>我是不会告诉你开始只是想从网上 <code>copy</code> 份指令改改方便偷懒，没想到后面就开发了一个完整组件。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf6f6a25b45c40fa89113a8582104acc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>写文章小白，若是阅读让你枯燥乏味请你边听摇滚边阅读，若是还有其他问题还请各位在评论区留言。</p>
<p>若能顺手点个小欣欣，鄙人感激不尽！Thanks♪(･ω･)ﾉ</p></div>  
</div>
            