
---
title: '_Element Plus 源码解析_ Affix 固钉'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3395'
author: 掘金
comments: false
date: Fri, 16 Jul 2021 21:02:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=3395'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">一、组件介绍</h2>
<p>Affix组件用于<code>将页面元素固定在特定可视区域</code>。</p>
<h3 data-id="heading-1">1.1 属性</h3>
<ul>
<li>position：指定固钉的位置，可设置为top或bottom，默认为top</li>
<li>offset: 设置偏移距离，默认为0</li>
<li>target：指定容器（CSS 选择器），让固钉始终保持在容器内，超过范围则隐藏，默认的容器是<code>document.documentElement</code>。</li>
<li>z-index: 固钉的层级，默认100</li>
</ul>
<h3 data-id="heading-2">1.2 事件</h3>
<ul>
<li>scroll： 容器滚动时触发事件，参数是：固钉的scrollTop值和状态（是否fixed）</li>
<li>change: 固钉状态改变时触发，参数是固钉当前是否处于fixed状态</li>
</ul>
<h2 data-id="heading-3">二、源码分析</h2>
<h2 data-id="heading-4">2.1 template</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"root"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-affix"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"rootStyle"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;'el-affix--fixed': state.fixed&#125;"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"affixStyle"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>template部分很简单，通过slot接收内容</p>
<h2 data-id="heading-5">2.2 script</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 部分核心代码，代码顺序有所调整</span>
<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, &#123; emit &#125;</span>)</span> &#123;
    <span class="hljs-comment">// target容器 ref</span>
    <span class="hljs-keyword">const</span> target = ref(<span class="hljs-literal">null</span>) 
    <span class="hljs-comment">// 固钉ref，与template中的ref属性配合，得到HTML元素</span>
    <span class="hljs-keyword">const</span> root = ref(<span class="hljs-literal">null</span>)
    <span class="hljs-comment">// 滚动容器ref</span>
    <span class="hljs-keyword">const</span> scrollContainer = ref(<span class="hljs-literal">null</span>)
    
    <span class="hljs-comment">// 固钉状态</span>
    <span class="hljs-keyword">const</span> state = reactive(&#123;
      <span class="hljs-attr">fixed</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">height</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// height of root</span>
      <span class="hljs-attr">width</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// width of root</span>
      <span class="hljs-attr">scrollTop</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// scrollTop of documentElement</span>
      <span class="hljs-attr">clientHeight</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// clientHeight of documentElement</span>
      <span class="hljs-attr">transform</span>: <span class="hljs-number">0</span>,
    &#125;)
    
    onMounted(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 根据传入的target确定 target容器</span>
      <span class="hljs-keyword">if</span> (props.target) &#123;
        target.value = <span class="hljs-built_in">document</span>.querySelector(props.target)
        <span class="hljs-keyword">if</span> (!target.value) &#123;
          <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`target is not existed: <span class="hljs-subst">$&#123;props.target&#125;</span>`</span>)
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        target.value = <span class="hljs-built_in">document</span>.documentElement
      &#125;
      
      <span class="hljs-comment">// 根据固钉元素，向上寻找滚动容器</span>
      scrollContainer.value = getScrollContainer(root.value)
      <span class="hljs-comment">// 监听滚动容器的scroll事件</span>
      on(scrollContainer.value, <span class="hljs-string">'scroll'</span>, onScroll)
      <span class="hljs-comment">// 监听固钉元素的resize事件</span>
      addResizeListener(root.value, updateState)
    &#125;)
    
    <span class="hljs-comment">// 滚动容器的scroll事件的响应函数</span>
    <span class="hljs-keyword">const</span> onScroll = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 更新固钉状态</span>
      updateState()
      
      emit(<span class="hljs-string">'scroll'</span>, &#123;
        <span class="hljs-attr">scrollTop</span>: state.scrollTop,
        <span class="hljs-attr">fixed</span>: state.fixed,
      &#125;)
    &#125;
    
    <span class="hljs-comment">// 更新固钉状态函数</span>
    <span class="hljs-keyword">const</span> updateState = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> rootRect = root.value.getBoundingClientRect()
      <span class="hljs-keyword">const</span> targetRect = target.value.getBoundingClientRect()
      state.height = rootRect.height
      state.width = rootRect.width
      state.scrollTop = scrollContainer.value === <span class="hljs-built_in">window</span> ? <span class="hljs-built_in">document</span>.documentElement.scrollTop : scrollContainer.value.scrollTop
      state.clientHeight = <span class="hljs-built_in">document</span>.documentElement.clientHeight

      <span class="hljs-keyword">if</span> (props.position === <span class="hljs-string">'top'</span>) &#123;
        <span class="hljs-keyword">if</span> (props.target) &#123;
          <span class="hljs-keyword">const</span> difference = targetRect.bottom - props.offset - state.height
          <span class="hljs-comment">// targetRect.bottom > 0 对应的是让固钉始终保持在容器内，超过范围则隐藏</span>
          state.fixed = props.offset > rootRect.top && targetRect.bottom > <span class="hljs-number">0</span>
          <span class="hljs-comment">// 用于处理场景：滚动过程中，target容器可视区域不足以显示整个固钉，则固钉应相应偏移，只展示部分</span>
          state.transform = difference < <span class="hljs-number">0</span> ? difference : <span class="hljs-number">0</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
          state.fixed = props.offset > rootRect.top
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">if</span> (props.target) &#123;
          <span class="hljs-keyword">const</span> difference = state.clientHeight - targetRect.top - props.offset - state.height
          state.fixed = state.clientHeight - props.offset < rootRect.bottom && state.clientHeight > targetRect.top
          state.transform = difference < <span class="hljs-number">0</span> ? -difference : <span class="hljs-number">0</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
          state.fixed = state.clientHeight - props.offset < rootRect.bottom
        &#125;
      &#125;
    &#125;
    <span class="hljs-comment">// 监测固钉fixed状态变化，并对外emit change事件</span>
    watch(<span class="hljs-function">() =></span> state.fixed, <span class="hljs-function">() =></span> &#123;
      emit(<span class="hljs-string">'change'</span>, state.fixed)
    &#125;)
    
    <span class="hljs-comment">// 计算属性，通过固钉的状态自动更新固钉的样式</span>
    <span class="hljs-keyword">const</span> affixStyle = computed(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (!state.fixed) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-keyword">const</span> offset = props.offset ? <span class="hljs-string">`<span class="hljs-subst">$&#123;props.offset&#125;</span>px`</span> : <span class="hljs-number">0</span>
      <span class="hljs-keyword">const</span> transform = state.transform ? <span class="hljs-string">`translateY(<span class="hljs-subst">$&#123;state.transform&#125;</span>px)`</span> : <span class="hljs-string">''</span>

      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">height</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;state.height&#125;</span>px`</span>,
        <span class="hljs-attr">width</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;state.width&#125;</span>px`</span>,
        <span class="hljs-attr">top</span>: props.position === <span class="hljs-string">'top'</span> ? offset : <span class="hljs-string">''</span>,
        <span class="hljs-attr">bottom</span>: props.position === <span class="hljs-string">'bottom'</span> ? offset : <span class="hljs-string">''</span>,
        <span class="hljs-attr">transform</span>: transform,
        <span class="hljs-attr">zIndex</span>: props.zIndex,
      &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.3 实现总结：</h3>
<ol>
<li>
<p>通过监听滚动容器的scroll事件(及固钉自身的resize事件)；</p>
</li>
<li>
<p>事件响应函数中动态获取固钉及target容器的DOM属性并以此计算固钉的状态；</p>
</li>
<li>
<p>利用计算属性自动更新固钉的样式；</p>
</li>
</ol></div>  
</div>
            