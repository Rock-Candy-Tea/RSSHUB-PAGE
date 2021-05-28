
---
title: 'vue自定义组件实现 v-model双向绑定数据'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9850'
author: 掘金
comments: false
date: Thu, 27 May 2021 23:08:34 GMT
thumbnail: 'https://picsum.photos/400/300?random=9850'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>项目中会遇到自定义公共组件供项目调用，正常情况可以使用 props定义参数接收父组件传的参数，然后通过子组件的$emits()方法回传数据给父组件。
类似如下：
父组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><common-checkbox :checked=<span class="hljs-string">"goodsSelected"</span> <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"left"</span> :height=<span class="hljs-string">"'16px'"</span> :width=<span class="hljs-string">"'16px'"</span>  @checkChange=<span class="hljs-string">"checkChange"</span>></common-checkbox>

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">     <span class="hljs-comment">/**
     * 接收子组件回传进行处理
     */</span>
    <span class="hljs-function"><span class="hljs-title">checkChange</span>(<span class="hljs-params">value</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.goodsSelected=value<span class="hljs-comment">//子组件数据赋值给父组件</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">/**
     * 切换选中回传
     */</span>
    <span class="hljs-function"><span class="hljs-title">toggleCheck</span>(<span class="hljs-params">value</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'changeCheck'</span>, value)<span class="hljs-comment">//回传方法，把子组件变化后的数据回传给父组件处理</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这种写法需要调用公共组件的页面额外写处理的方法，而且显得太low，我们可不可以像是框架自带的公共组件一样去声明直接v-model双向绑定呢？接下来提供项目中实际遇到这种情况的处理方法
第一种方式：
正常情况下当你在父组件里给子组件绑定 v-model属性时，子组件中会默认的将 v-model绑定的数据，付给子组件 名为 value的props属性，value依然需要提前在子组件props中声明，否则接收不到。
当 value修改后，并不会立即双向回传给父组件。如果想回传实现同步更新父组件的v-model需要如下操作</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'input'</span>, value) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当未声明双向绑定回传的事件时，默认通过input事件回传，为什么说 “当未声明双向绑定回传的事件”,这个便是第二种方式，下面会讲到。
简单来说，第一种方式的实现，首先是v-model绑定父组件数据 ，然后子组件value 的props属性自动接收，最后当数据更改后调用this.$emit('input', value) 回传父组件，这样父组件不需要额外实现子组件的回传就可以实现双向绑定
第二种方式：
前面提到 “当未声明双向绑定回传的事件” 默认使用 input回传，既然这样说了那就存在，如果我不用input呢？这就需要了解vue的一个特殊的属性：model，
这个属性可以用来声明 子组件用哪个字段去接收双向绑定的数据，以及用哪个方法回调更新父组件v-model的数据，写法如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'CommonCkeckBox'</span>,
  <span class="hljs-attr">model</span>: &#123;
    <span class="hljs-attr">prop</span>: <span class="hljs-string">'checked'</span>,
    <span class="hljs-attr">event</span>: <span class="hljs-string">'changeCheck'</span>
  &#125;,
    <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">checked</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-literal">false</span>,
    &#125;, <span class="hljs-comment">// 选中状态</span>
  &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种写法就意味着，父组件 双向绑定的数据会绑定到子组件名为checked的props属性，并且，当子组件调用this.$emit('changeCheck', value)时，会同步的更新父组件的数据，实现双向绑定。
接下来附一段自定义checkbox的代码以作参考：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"check-box-container"</span>  @<span class="hljs-attr">click</span>=<span class="hljs-string">"toggleCheck()"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;width:width,height:height&#125;"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"checkbox-icon"</span>></span>
              <span class="hljs-comment"><!-- 三种状态 选中  未选  禁用 --></span>
              <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">alt</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"`$&#123;$cdnImageUrl&#125;/cart/icon-selected.png`"</span> <span class="hljs-attr">:width</span>=<span class="hljs-string">"width"</span> <span class="hljs-attr">:height</span>=<span class="hljs-string">"height"</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"select"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"checked&&!disabled"</span>/></span>
              <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">alt</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"`$&#123;$cdnImageUrl&#125;/cart/icon-unselected.png`"</span> <span class="hljs-attr">:width</span>=<span class="hljs-string">"width"</span> <span class="hljs-attr">:height</span>=<span class="hljs-string">"height"</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"unselected"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"!checked&&!disabled"</span> /></span>
              <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">alt</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"`$&#123;$cdnImageUrl&#125;/cart/icon-unselected.png`"</span> <span class="hljs-attr">:width</span>=<span class="hljs-string">"width"</span> <span class="hljs-attr">:height</span>=<span class="hljs-string">"height"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"disabled"</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"unselected"</span>  <span class="hljs-attr">v-if</span>=<span class="hljs-string">"disabled"</span>/></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-comment">/**
 * 全局统一弹窗
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'CommonCkeckBox'</span>,
  <span class="hljs-attr">model</span>: &#123;
    <span class="hljs-attr">prop</span>: <span class="hljs-string">'checked'</span>,
    <span class="hljs-attr">event</span>: <span class="hljs-string">'changeCheck'</span>
  &#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">checked</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-literal">false</span>,
    &#125;, <span class="hljs-comment">// 选中状态</span>
    <span class="hljs-attr">disabled</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-literal">false</span>,
    &#125;, <span class="hljs-comment">// 是否禁用</span>
    <span class="hljs-attr">width</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">'16px'</span>,
    &#125;, <span class="hljs-comment">// 按钮默认宽度</span>
    <span class="hljs-attr">height</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">'16px'</span>,
    &#125;, <span class="hljs-comment">// 按钮默认高度</span>
  &#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">/**
     * 切换选中回传
     */</span>
    <span class="hljs-function"><span class="hljs-title">toggleCheck</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'changeCheck'</span>, !<span class="hljs-built_in">this</span>.checked)
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'toggleCheck'</span>)
    &#125;
  &#125;,
  <span class="hljs-attr">watch</span>: &#123;
    <span class="hljs-attr">checked</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">handler</span>(<span class="hljs-params">newValue, oldValue</span>)</span> &#123;
      <span class="hljs-comment">// 开放状态变更事件</span>
        <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'onChange'</span>)
      &#125;,
      <span class="hljs-attr">deep</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span>  <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.check-box-container</span>&#123;
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-selector-class">.checkbox-icon</span>&#123;
        <span class="hljs-selector-tag">img</span>&#123;
          <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">0</span>);
          will-change: auto;
        &#125;
        <span class="hljs-selector-class">.disabled</span>&#123;
          <span class="hljs-attribute">background-color</span>:<span class="hljs-number">#f5f5f5</span>;
          <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
        &#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">      <common-checkbox v-model=<span class="hljs-string">"item.goodsSelected"</span> <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"left"</span> :width=<span class="hljs-string">"'16px'"</span>  :height=<span class="hljs-string">"'16px'"</span>></common-checkbox>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体用哪种方式根据项目场景选择，若第一种不满足需求，可以尝试第二中实现。</p></div>  
</div>
            