
---
title: '一个拓展性极强的el-dialog弹窗的插件解决方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/923dbd2b8d5046dea7808a9080e1aea5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 03 Jul 2021 20:04:37 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/923dbd2b8d5046dea7808a9080e1aea5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h4 data-id="heading-0">目的，其实为了用js的方式调用弹窗</h4>
<p>插件的目的就的为了已js的方式调用弹出组件。自定义内容。无需关注弹窗使用中的代码。无需写弹窗相关的<code>html</code>代码。
就这样，轻轻松松~~ 就完成了一个弹窗的调用、自定义插槽内容、可配置参数及事件回调。</p>
<pre><code class="hljs language-js copyable" lang="js">  methods:&#123;
        <span class="hljs-function"><span class="hljs-title">openDialog</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">this</span>.$Modal(&#123;
                <span class="hljs-comment">// 弹窗内嵌套组件</span>
                <span class="hljs-attr">component</span>: xxx,
                <span class="hljs-comment">// 嵌套组件传递属性</span>
                <span class="hljs-attr">componentProps</span>: &#123;

                &#125;,
                <span class="hljs-comment">// 弹窗属性设置</span>
                <span class="hljs-attr">props</span>: &#123;

                &#125;,
                <span class="hljs-comment">// 事件回调</span>
                <span class="hljs-attr">methods</span>: &#123;
                    
                &#125;
            &#125;);
        &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">写在前面</h4>
<p>在实际开发场景用应用<code>element-ui</code>居多。所以插件以<code>el-dialog</code>为例。理论上是可以拓展为任意ui组件库相关弹窗业务使用的，这里大家可以举一反三一下。</p>
<p>本文权当技术分享，成果分享，如有需要转发使用，请带上原链接。thank you ~
如果有更好的方式欢迎交流~
最后，就是写文档的初衷其实是很单纯的，就是为了你们的<code>点赞``点赞``点赞</code></p>
<p>动动你你们的小手 start ~</p>
<h4 data-id="heading-2">日常开发现状。</h4>
<ul>
<li>冗余代码</li>
</ul>
<p>多个弹窗需要定义需要定义多个属性。并且在业务使用过程中设置这些属性的<code>true</code>或者<code>false</code>。</p>
<ul>
<li>可复用性差</li>
</ul>
<p>页面多了很多非业务逻辑控制代码（可读性变差）。比如弹框一里面打开弹框二，控制代码却要写到弹框一的父页面。</p>
<ul>
<li>可维护性差</li>
</ul>
<p>无关代码在业务过程中穿插，解藕性差。维护也相对吃力。需要查找你控制弹窗显示与否的属性-》再看你渲染的弹窗内容...时间已经过去了几个世纪</p>
<p>组件化开发还是要尽可能的解藕。让使用方式随心所欲。业务代码更加独立。组件复用性所有提升才行。</p>
<h4 data-id="heading-3">日常coding中</h4>
<p>当业务中弹窗需要多个的时候基本如下，巴拉巴拉<code>coding...</code>,当然可能有其他的封装方式使用。但是单单的去写一些属性去控制这些弹窗的可见与否以及怎么把参数往子组件中传递.再者就是子组件业务处理完成要回调等等。这些看似繁琐而又看起来必要的东西。就这样写着写着会不会，有点不太漂亮（其实就是懒，不想写那么多代码。简单一点就好，极简一下更好）</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="hljs-comment">// .........举例子-巴拉巴拉一些弹窗代码.........</span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-dialog</span>
      <span class="hljs-attr">title</span>=<span class="hljs-string">"车辆基本信息"</span>
      <span class="hljs-attr">width</span>=<span class="hljs-string">"50%"</span>
      <span class="hljs-attr">append-to-body</span>
      <span class="hljs-attr">destroy-on-close</span>
      <span class="hljs-attr">:visible</span>=<span class="hljs-string">"carInfoVisible"</span>
      <span class="hljs-attr">:close-on-click-modal</span>=<span class="hljs-string">"false"</span>
      <span class="hljs-attr">:close-on-press-escape</span>=<span class="hljs-string">"false"</span>
      <span class="hljs-attr">:before-close</span>=<span class="hljs-string">"closeCarInfo"</span>
    ></span>
      <span class="hljs-tag"><<span class="hljs-name">info</span>
        <span class="hljs-attr">v-if</span>=<span class="hljs-string">"carInfoVisible"</span>
        <span class="hljs-attr">:info-id</span>=<span class="hljs-string">"infoId"</span>
        <span class="hljs-attr">:car-info-visible</span>=<span class="hljs-string">"carInfoVisible"</span>
        @<span class="hljs-attr">close</span>=<span class="hljs-string">"closeCarInfo"</span>
      /></span>
    <span class="hljs-tag"></<span class="hljs-name">el-dialog</span>></span></span>
    
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-dialog</span>
      <span class="hljs-attr">title</span>=<span class="hljs-string">"车辆作业信息"</span>
      <span class="hljs-attr">width</span>=<span class="hljs-string">"50%"</span>
      <span class="hljs-attr">append-to-body</span>
      <span class="hljs-attr">destroy-on-close</span>
      <span class="hljs-attr">:visible</span>=<span class="hljs-string">"carInfoWorkVisible"</span>
      <span class="hljs-attr">:close-on-click-modal</span>=<span class="hljs-string">"false"</span>
      <span class="hljs-attr">:close-on-press-escape</span>=<span class="hljs-string">"false"</span>
      <span class="hljs-attr">:before-close</span>=<span class="hljs-string">"closeCarWork"</span>
    ></span>
      <span class="hljs-tag"><<span class="hljs-name">work</span>
        <span class="hljs-attr">v-if</span>=<span class="hljs-string">"carInfoWorkVisible"</span>
        <span class="hljs-attr">:info-id</span>=<span class="hljs-string">"infoId"</span>
        <span class="hljs-attr">:car-info-visible</span>=<span class="hljs-string">"carInfoWorkVisible"</span>
        @<span class="hljs-attr">close</span>=<span class="hljs-string">"closeCarWork"</span>
      /></span>
    <span class="hljs-tag"></<span class="hljs-name">el-dialog</span>></span></span>
  <span class="hljs-comment">// ........如果还有其他业务需要弹 继续重复++.........</span>
</template>


<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">closeCarInfo</span>:<span class="hljs-literal">false</span>,
            <span class="hljs-attr">carInfoWorkVisible</span>:<span class="hljs-literal">false</span>,
            .......略.......
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>:&#123;
        .....略一些弹窗组件的事件回调...
        <span class="hljs-function"><span class="hljs-title">closeCarWork</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">懒癌发作开始思考</h4>
<p>这些千篇一律的东西能不能优化掉呢？如果是用js调用的弹窗的方式的话，应该可以省掉一些代码。然后如果弹窗里面的内容可以自己定义传递的那是不是可以好点了。</p>
<ul>
<li>不想仅仅控制弹窗显示与否以及传递参数。让data中的变量变得很庞大。</li>
<li>每个弹窗页面的内容组件是可以任意的，方便引入的使用。参数的传递和事件的回调都是简单而且都是可以自己定义的。</li>
</ul>
<p>感受启发，其他组件库js调用方式是这样的</p>
<pre><code class="hljs language-js copyable" lang="js">  methods:&#123;
        <span class="hljs-function"><span class="hljs-title">openDialog</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">this</span>.$Modal(&#123;
                <span class="hljs-attr">title</span>: <span class="hljs-string">'Js'</span>,
                <span class="hljs-attr">content</span>: <span class="hljs-string">'这是使用Js调用的弹出框'</span>
            &#125;);
        &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">而我期待的是这样的。</h4>
<ul>
<li>可以设置弹窗属性</li>
<li>要能方便自定义弹窗嵌套组件</li>
<li>要可以设置自定义弹窗嵌套组件的传递属性</li>
<li>要可以设置自定义弹窗嵌套组件的事件回调</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  methods:&#123;
        <span class="hljs-function"><span class="hljs-title">openDialog</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">this</span>.$Modal(&#123;
                <span class="hljs-comment">// 弹窗内嵌套组件</span>
                <span class="hljs-attr">component</span>: xxx,
                <span class="hljs-comment">// 嵌套组件传递属性</span>
                <span class="hljs-attr">componentProps</span>: &#123;

                &#125;,
                <span class="hljs-comment">// 弹窗属性设置</span>
                <span class="hljs-attr">props</span>: &#123;

                &#125;,
                <span class="hljs-comment">// 事件回调</span>
                <span class="hljs-attr">methods</span>: &#123;
                    
                &#125;
            &#125;);
        &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">实现思路</h4>
<p>每次使用调用的时候就实例化一个<code>el-dialog</code>组件同时设置 <code>el-dialog</code>的默认<code>slots</code>。考虑到同级使用和嵌套使用。所以在组件实例化的时候，都去 <code>createElement</code>一个<code>div</code>。作为组件挂载的元素。并且把这个元素至于<code>body</code>中。所以代码应该是这个样子的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">let</span> instance

<span class="hljs-keyword">const</span> Modal = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">&#123; component, methods, props, componentProps &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> dom = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
  <span class="hljs-built_in">document</span>.body.appendChild(dom)
  instance = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: dom,
  &#125;)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Modal
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么怎么去渲染弹窗和定义弹窗嵌套组件的呢？</p>
<h4 data-id="heading-7">方案1 template 模板渲染的方式(gg)</h4>
<p>这是一开始想到的方式。巴拉巴拉<code>coding...</code>如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; Dialog &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span>

<span class="hljs-keyword">let</span> instance

<span class="hljs-keyword">const</span> template =
    <span class="hljs-string">'<Dialog :title="title" v-model="showModal"  @close="close">'</span> +
        <span class="hljs-string">'<Plugin v-on:close="close" :componentProps="componentProps"> </Plugin>'</span> +
    <span class="hljs-string">'</Dialog>'</span>

<span class="hljs-keyword">const</span> Modal = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">&#123; component, methods, props, componentProps &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> dom = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
  <span class="hljs-built_in">document</span>.body.appendChild(dom)
  instance = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>: dom,
      template,
      <span class="hljs-attr">components</span>: &#123;
       <span class="hljs-attr">Dialog</span>: Dialog,
       <span class="hljs-attr">Plugin</span>: component
      &#125;,
      <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">return</span> &#123;
              <span class="hljs-attr">title</span>:<span class="hljs-string">'弹窗描述Title'</span>,
              <span class="hljs-attr">showModal</span>:<span class="hljs-literal">true</span>
              ...如果还有更多的参数就不够灵活了...
          &#125;
      &#125;,
      <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">close</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">this</span>.showModal = <span class="hljs-literal">false</span>
        &#125;
      &#125;,
  &#125;)
  <span class="hljs-keyword">return</span> instance
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Modal
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一顿调试之后发现这个方案并不是很好。编译报警告,即时处理了警告。如果有多参数的传递，后续也是一个灾难。所以这个方案到这里我就end了。如果有可以完成验证通过的同学可以留言告知一下。</p>
<pre><code class="hljs language-js copyable" lang="js">[Vue warn]: You are using the runtime-only build <span class="hljs-keyword">of</span> Vue where the template compiler is not available. Either pre-compile the templates into render functions, or use the compiler-included build.
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">方案2 render 函数渲染的方式</h4>
<p><code>render</code>由于本身用的比较少。用的比较简单，只是作为单一的标签渲染。加上书写的方式有点小难受，一直也被当忽略一般。组件方式渲染的方式想都没有想过。指导看到下面的代码. <code>createElement</code>第一个参数支持<code>组件选项对象</code>！！！！。那就是说可以渲染组件咯。<code>biubiu coding...</code> 等等，按照这种方式那么怎么决定弹窗的内容组件？我们都知道<code>el-dialog</code>的内容是通过<code>slot</code>插槽插进去的。那么<code>render</code>可以去设置插槽吗？答案是可以的。通过设置<code>scopedSlots</code>。</p>
<p><a href="https://cn.vuejs.org/v2/guide/render-function.html" target="_blank" rel="nofollow noopener noreferrer">点击了解更多关于render函数</a>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// @returns &#123;VNode&#125;</span>
createElement(
  <span class="hljs-comment">// &#123;String | Object | Function&#125;</span>
  <span class="hljs-comment">// 一个 HTML 标签名、组件选项对象，或者</span>
  <span class="hljs-comment">// resolve 了上述任何一种的一个 async 函数。必填项。</span>
  <span class="hljs-string">'div'</span>,

  <span class="hljs-comment">// &#123;Object&#125;</span>
  <span class="hljs-comment">// 一个与模板中 attribute 对应的数据对象。可选。</span>
  &#123;
    <span class="hljs-comment">// (详情见下一节)</span>
  &#125;,

  <span class="hljs-comment">// &#123;String | Array&#125;</span>
  <span class="hljs-comment">// 子级虚拟节点 (VNodes)，由 `createElement()` 构建而成，</span>
  <span class="hljs-comment">// 也可以使用字符串来生成“文本虚拟节点”。可选。</span>
  [
    <span class="hljs-string">'先写一些文字'</span>,
    createElement(<span class="hljs-string">'h1'</span>, <span class="hljs-string">'一则头条'</span>),
    createElement(MyComponent, &#123;
      <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">someProp</span>: <span class="hljs-string">'foobar'</span>
      &#125;
    &#125;)
  ]
)

<span class="hljs-comment">// 深入数据对象</span>
&#123;
 <span class="hljs-comment">// 作用域插槽的格式为</span>
  <span class="hljs-comment">// &#123; name: props => VNode | Array<VNode> &#125;</span>
  <span class="hljs-attr">scopedSlots</span>: &#123;
    <span class="hljs-attr">default</span>: <span class="hljs-function"><span class="hljs-params">props</span> =></span> createElement(<span class="hljs-string">'span'</span>, props.text)
  &#125;,
  <span class="hljs-comment">// 如果组件是其它组件的子组件，需为插槽指定名称</span>
  <span class="hljs-attr">slot</span>: <span class="hljs-string">'name-of-slot'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查阅<code>render</code>相关文档之后。最后的本质就是通过<code>render</code>--》变成<code>template</code>书写的那样。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; Dialog &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span>
<span class="hljs-keyword">let</span> instance

<span class="hljs-keyword">const</span> Modal = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">&#123; component, methods, props, componentProps &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> dom = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
  <span class="hljs-built_in">document</span>.body.appendChild(dom)
  instance = <span class="hljs-keyword">new</span> vue(&#123;
    <span class="hljs-attr">el</span>: dom,
    data () &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">showModal</span>: <span class="hljs-literal">true</span>
      &#125;
    &#125;,
    <span class="hljs-attr">components</span>: &#123;
      <span class="hljs-attr">Dialog</span>: Dialog,
      <span class="hljs-attr">Plugin</span>: component
    &#125;,
    render (createElement) &#123;
      <span class="hljs-keyword">return</span> createElement(
        <span class="hljs-string">'Dialog'</span>, &#123;
          <span class="hljs-attr">scopedSlots</span>: &#123;
            <span class="hljs-attr">default</span>: <span class="hljs-function">()=></span> createElement(<span class="hljs-string">'Plugin'</span>)
          &#125;
        &#125;)
    &#125;,
  &#125;)
  <span class="hljs-keyword">return</span> instance
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Modal

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">最后调整一下传递的<code>props</code>和回调的绑定的<code>methods</code>.弹窗内部的组件。并不需要一直纯在。期待在弹窗<code>visible:true</code>渲染既可。<code>render</code>的时候可以根据数据响应式渲染。设置<code>scopedSlots</code>在显示的时候渲染。</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; Dialog &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span>

<span class="hljs-keyword">let</span> instance

<span class="hljs-keyword">const</span> Modal = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">&#123; component, methods, props, componentProps &#125;</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (Vue.prototype.$isServer) <span class="hljs-keyword">return</span>
  <span class="hljs-keyword">const</span> dom = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
  <span class="hljs-built_in">document</span>.body.appendChild(dom)
  instance = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: dom,
    data () &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">showModal</span>: <span class="hljs-literal">true</span>
      &#125;
    &#125;,
    <span class="hljs-attr">components</span>: &#123;
      <span class="hljs-attr">Dialog</span>: Dialog,
      <span class="hljs-attr">Plugin</span>: component
    &#125;,
    render (createElement) &#123;
      <span class="hljs-keyword">const</span> plugin = <span class="hljs-built_in">this</span>.showModal ? <span class="hljs-function">() =></span> createElement(<span class="hljs-string">'Plugin'</span>, &#123;
        <span class="hljs-attr">props</span>: &#123;
          ...componentProps
        &#125;,
        <span class="hljs-attr">on</span>: &#123;
          <span class="hljs-attr">close</span>: <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> <span class="hljs-built_in">this</span>.close(e),
          ...methods
        &#125;
      &#125;) : <span class="hljs-literal">null</span>
      <span class="hljs-keyword">return</span> createElement(
        <span class="hljs-string">'Dialog'</span>, &#123;
          <span class="hljs-attr">props</span>: &#123;
            <span class="hljs-attr">visible</span>: <span class="hljs-built_in">this</span>.showModal,
            ...props
          &#125;,
          <span class="hljs-attr">on</span>: &#123;
            <span class="hljs-attr">close</span>: <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> <span class="hljs-built_in">this</span>.close(e)
          &#125;,
          <span class="hljs-attr">scopedSlots</span>: &#123;
            <span class="hljs-attr">default</span>: plugin
          &#125;
        &#125;)
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      close () &#123;
        <span class="hljs-built_in">this</span>.showModal = <span class="hljs-literal">false</span>
        <span class="hljs-built_in">document</span>.body.removeChild(<span class="hljs-built_in">this</span>.$el)
        <span class="hljs-built_in">this</span>.$destroy()
      &#125;
    &#125;
  &#125;)
  <span class="hljs-keyword">return</span> instance
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Modal
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">插件使用</h4>
<p><code>main.js</code>中导入并装载到<code>prototype</code>原型中既可。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// main.js</span>
  <span class="hljs-keyword">import</span> modal <span class="hljs-keyword">from</span> <span class="hljs-string">'@/plugins/modal'</span>
  Vue.prototype.$modal = modal
  
  <span class="hljs-comment">// 使用以js的方式使用弹窗、配置的方式完成参数传递、事件回调</span>
   <span class="hljs-built_in">this</span>.$modal(&#123;
    <span class="hljs-comment">// 弹窗内嵌套组件传递属性</span>
    <span class="hljs-attr">componentProps</span>: &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-string">'7676043D-F0DA-80DA-1CBD-BDD7068B3A77'</span>
    &#125;,
    <span class="hljs-comment">// 弹窗内嵌套组件</span>
    <span class="hljs-comment">// component: Table, //同步</span>
    <span class="hljs-attr">component</span>: <span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> <span class="hljs-built_in">require</span>([<span class="hljs-string">'./cube-table-list.vue'</span>], resolve), <span class="hljs-comment">// 异步</span>
    <span class="hljs-comment">// 弹窗属性设置</span>
    <span class="hljs-attr">props</span>: &#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'基本信息弹窗'</span>
      <span class="hljs-comment">// width: '520px',</span>
      <span class="hljs-comment">// fullscreen: false</span>
    &#125;,
    <span class="hljs-comment">// 事件回调</span>
    <span class="hljs-attr">methods</span>: &#123;
      refresh (e) &#123;
        <span class="hljs-built_in">console</span>.log(e, <span class="hljs-string">'--x-x-x-'</span>)
      &#125;
    &#125;
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">弹窗以js的方式调用。</h4>
<p>以js的方式调用组件。以配置的方式决定弹窗内容。就可以省略掉这些一些<code>玉女无瓜</code>和业务无关属性、方法。弹窗是否关闭等不再是我们代码关心的。需要就调用渲染，关闭则销毁。支持无限极嵌套、多个同级使用。让开发更专注于业务的开发。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 玉女无瓜的代码</span>
<template>
    <span class="hljs-comment">// .........举例子-巴拉巴拉一些弹窗代码.........</span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-dialog</span>
      <span class="hljs-attr">title</span>=<span class="hljs-string">"车辆基本信息"</span>
      <span class="hljs-attr">width</span>=<span class="hljs-string">"50%"</span>
      <span class="hljs-attr">append-to-body</span>
      <span class="hljs-attr">destroy-on-close</span>
      <span class="hljs-attr">:visible</span>=<span class="hljs-string">"carInfoVisible"</span>
      <span class="hljs-attr">:close-on-click-modal</span>=<span class="hljs-string">"false"</span>
      <span class="hljs-attr">:close-on-press-escape</span>=<span class="hljs-string">"false"</span>
      <span class="hljs-attr">:before-close</span>=<span class="hljs-string">"closeCarInfo"</span>
    ></span>
      <span class="hljs-tag"><<span class="hljs-name">info</span>
        <span class="hljs-attr">v-if</span>=<span class="hljs-string">"carInfoVisible"</span>
        <span class="hljs-attr">:info-id</span>=<span class="hljs-string">"infoId"</span>
        <span class="hljs-attr">:car-info-visible</span>=<span class="hljs-string">"carInfoVisible"</span>
        @<span class="hljs-attr">close</span>=<span class="hljs-string">"closeCarInfo"</span>
      /></span>
    <span class="hljs-tag"></<span class="hljs-name">el-dialog</span>></span></span>
  <span class="hljs-comment">// ........n++弹窗.........</span>
</template>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用对应映射关系。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/923dbd2b8d5046dea7808a9080e1aea5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">在最后</h4>
<p>本代码插件是本人原创设计，因为在此之前也尝试寻找类似的解决方案。都没有找到合适的。然后就有了你们所看到的这个文章。当然如有雷同，权当没看见~。</p>
<p>本文权当技术分享，成果分享，如有需要转发使用，请带上原链接。thank you ~
如果有更好的方式欢迎交流~
最后，就是写文档的初衷其实是很单纯的，就是为了你们的<code>点赞``点赞``点赞</code></p>
<p>动动你你们的小手 start ~</p></div>  
</div>
            