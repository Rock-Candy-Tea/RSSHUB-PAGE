
---
title: '【记】Vue - 拖拽元素组件实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1d9a6374e4c49209a6dd307d3513479~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 22:35:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1d9a6374e4c49209a6dd307d3513479~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">需求描述：</h1>
<ol>
<li>可实现PC/移动端元素拖拽移动</li>
<li>支持2种模式：
<ol>
<li>元素跟随光标点放置</li>
<li>元素在光标点平齐位置靠侧边吸附</li>
</ol>
</li>
</ol>
<p>市面上估计有很多这种组件和功能了，但我没找到合适的，用了VueUse的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvueuse.org%2Fcore%2FuseDraggable%2F%23demo" target="_blank" rel="nofollow noopener noreferrer" title="https://vueuse.org/core/useDraggable/#demo" ref="nofollow noopener noreferrer">useDraggable Function</a>感觉不太适合某些应用场景（比如需要拖拽的点击button），故自己手动实现了一下，此次实现也算是对事件处理以及元素定位的相关属性有了比较深入的了解了，仅以本文记录一下。也欢迎大佬们批评指正。</p>
<h1 data-id="heading-1">实现思路：</h1>
<h2 data-id="heading-2">整体思路</h2>
<ol>
<li>组件元素包括三部分：
<ol>
<li>移动容器</li>
<li>可拖拽元素</li>
<li>操作元素</li>
</ol>
</li>
</ol>
<p>移动容器包裹可拖拽元素和操作元素，且可拖拽元素和操作元素在页面中二者只显示其一。
当<code>props.snapEdge === false</code>时，可拖拽元素和操作元素为同一个，通过default slot传入；
当<code>props.snapEdge === true</code>时，可拖拽元素为snapEdge slot传入的元素，操作元素为default slot传入的元素。</p>
<ol start="2">
<li>拖拽可拖拽元素，可以放置整个移动容器的位置，支持2种方式：
<ol>
<li>在光标所在处放置容器</li>
<li>在光标所在平齐处放置元素靠侧边吸附</li>
</ol>
</li>
</ol>
<p>两种方式切换通过<code>props.snapEdge</code>设置。</p>
<h2 data-id="heading-3">细节思路</h2>
<ol>
<li><strong>DragEvent实现PC端拖拽功能</strong></li>
</ol>
<p>PC端拖拽可通过DragEvent事件监听（ondragstart、ondragend）【为什么不用MouseEvent（onmousedown、onmousemove、onmouseup、……），主要考虑是为了防止和内部元素的click事件冲突。vueuse中的useDraggable Function就存在这个问题，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvueuse%2Fvueuse%2Fblob%2F658374fd12fbce2ac6127a9fb9bca52fb2137505%2Fpackages%2Fcore%2FuseDraggable%2Findex.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vueuse/vueuse/blob/658374fd12fbce2ac6127a9fb9bca52fb2137505/packages/core/useDraggable/index.ts" ref="nofollow noopener noreferrer">useDraggable Function源码</a>中是通过PointerEvent事件监听，而PointerEvent是继承自MouseEvent，对其源码感兴趣的可转以上链接】
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1d9a6374e4c49209a6dd307d3513479~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" title="摘自useDraggable Function源码" loading="lazy" referrerpolicy="no-referrer">
在drag事件执行过程中会判断2个因素：</p>
<ol>
<li>可拖拽元素：可拖拽元素通过<code>draggable</code>属性设置；</li>
<li>可放置的目标元素：默认情况下，浏览器会阻止在大多数 HTML 元素上放置某些内容时发生任何事情。要想目标元素变为可放置元素，该元素需要通过ondragover事件来阻止默认事件的发生。</li>
</ol>
<p>即通过对拖拽元素本身和其父元素中添加ondragover事件</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> <span class="hljs-title function_">prevent</span> = (<span class="hljs-params">evt: DragEvent</span>) => &#123;
    evt.<span class="hljs-title function_">preventDefault</span>();
    evt.<span class="hljs-property">dataTransfer</span>.<span class="hljs-property">dropEffect</span> = <span class="hljs-string">'move'</span>
&#125;;
dragContainerRef.<span class="hljs-property">value</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'dragover'</span>, prevent);
dragContainerRef.<span class="hljs-property">value</span>.<span class="hljs-property">parentNode</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'dragover'</span>, prevent);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>TouchEvent实现移动端拖拽功能</strong></li>
</ol>
<p>移动端拖拽可通过TouchEvent事件监听（ontouchstart、ontouchmove、ontouchend）</p>
<ol start="3">
<li><strong>元素随光标移动实现</strong></li>
</ol>
<p>在按下元素后记录鼠标相对元素的位置，在之后的光标移动过程中修改元素的位置使其始终保持和光标的相对位置。</p>
<h1 data-id="heading-4">代码实现：</h1>
<p>效果演示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69340a15fcb848a2a22d2622fbb5cad6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="1111.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
    <Drag-Elem class="drag-btn" :snapEdge="true">
      <button @click="onClick">💛操作元素</button>
      <template #snapEdge>
        <button @touch="onClick">💛</button>
      </template>
    </Drag-Elem>
</template>
<style>
  .drag-btn &#123;
    bottom: 100px;
    left: 10px;
  &#125;
</style>
<script setup>
import DragElem from '@/components/myUI/DragElem.vue';
const onClick = () => alert('💛点击')
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>------ 最后附上代码：</p>
<ol>
<li>template & style</li>
</ol>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <!-- 移动容器 -->
  <div ref="dragContainerRef" class="drag-container" :style="dragContainerStyle">
    <!-- 可拖拽元素，拖拽该元素会对整个移动容器进行移动 -->
    <div draggable="true" @dragstart="onDragstart" @dragend="onDragend" @touchstart="onTouchstart"
      @touchmove="onTouchmove" @touchend="onTouchend">
      <div :style="dragElemStyle">
        <div v-show="$slots.snapEdge&&isShowSnapEdgeElem" @mouseup="unShowSnapEdgeElem">
          <slot name="snapEdge"></slot>
        </div>
        <div v-show="!$slots.snapEdge">
          <slot></slot>
        </div>
      </div>
    </div>
    <!-- 操作元素，由可拖拽元素点击触发弹出 -->
    <div v-show="$slots.snapEdge && !($slots.snapEdge && isShowSnapEdgeElem)">
      <slot></slot>
    </div>
  </div>
</template>

<style>
  .drag-container &#123;
    position: fixed;
    z-index: 10;
  &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>typescript</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; onMounted, reactive, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;

<span class="hljs-comment">// component props</span>
<span class="hljs-comment">// :snapEdge="true" 开启元素侧边栏吸附 </span>
<span class="hljs-keyword">const</span> props = <span class="hljs-title function_">defineProps</span>(&#123;
  <span class="hljs-attr">snapEdge</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-title class_">Boolean</span>,
    <span class="hljs-attr">required</span>: <span class="hljs-literal">false</span>,
  &#125;,
&#125;)
<span class="hljs-comment">// 移动容器位置</span>
<span class="hljs-keyword">const</span> dragContainerStyle = <span class="hljs-title function_">reactive</span>(&#123;
  <span class="hljs-attr">top</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">left</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">bottom</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">right</span>: <span class="hljs-string">''</span>,
&#125;);
<span class="hljs-comment">// 设置可拖拽元素拖拽时大小（仅对移动端生效）</span>
<span class="hljs-keyword">const</span> <span class="hljs-variable constant_">SCALE</span> = <span class="hljs-string">'1.5'</span>
<span class="hljs-keyword">const</span> dragElemStyle = <span class="hljs-title function_">reactive</span>(&#123;
  <span class="hljs-attr">transform</span>: <span class="hljs-string">'scale(1)'</span>,
&#125;)
<span class="hljs-comment">// 是否显示侧边栏吸附元素，仅在使用了$slots.snapEdge插槽时生效</span>
<span class="hljs-keyword">const</span> isShowSnapEdgeElem = <span class="hljs-title function_">ref</span>(<span class="hljs-literal">false</span>)

<span class="hljs-keyword">const</span> dragContainerRef = ref<<span class="hljs-title class_">HTMLElement</span>>(<span class="hljs-literal">null</span>)
<span class="hljs-keyword">const</span> <span class="hljs-title function_">initLocation</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">const</span> &#123; offsetLeft, offsetTop &#125; = dragContainerRef.<span class="hljs-property">value</span>
  dragContainerStyle.<span class="hljs-property">top</span> = offsetTop + <span class="hljs-string">'px'</span>
  dragContainerStyle.<span class="hljs-property">left</span> = offsetLeft + <span class="hljs-string">'px'</span>
  dragContainerStyle.<span class="hljs-property">bottom</span> = <span class="hljs-string">'auto'</span>
  dragContainerStyle.<span class="hljs-property">right</span> = <span class="hljs-string">'auto'</span>
  <span class="hljs-title function_">setElemSnapEdgeLocation</span>()
&#125;
<span class="hljs-title function_">onMounted</span>(initLocation)


<span class="hljs-keyword">let</span> <span class="hljs-attr">pointerRelativeX</span>: <span class="hljs-built_in">number</span>, <span class="hljs-attr">pointerRelativeY</span>: <span class="hljs-built_in">number</span>;
<span class="hljs-comment">// 记录指针相对元素位置</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">recordPointerLocation</span> = (<span class="hljs-params">clientX: <span class="hljs-built_in">number</span>, clientY: <span class="hljs-built_in">number</span></span>) => &#123;
  pointerRelativeX = clientX - dragContainerRef.<span class="hljs-property">value</span>.<span class="hljs-property">offsetLeft</span>;
  pointerRelativeY = clientY - dragContainerRef.<span class="hljs-property">value</span>.<span class="hljs-property">offsetTop</span>;
&#125;;
<span class="hljs-comment">// 模式一：设置目标元素位置，以指针为基点</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">setElemLocation</span> = (<span class="hljs-params">clientX: <span class="hljs-built_in">number</span>, clientY: <span class="hljs-built_in">number</span></span>) => &#123;
  <span class="hljs-keyword">const</span> left = clientX - pointerRelativeX;
  <span class="hljs-keyword">const</span> top = clientY - pointerRelativeY;
  dragContainerStyle.<span class="hljs-property">right</span> = <span class="hljs-string">'auto'</span>;
  dragContainerStyle.<span class="hljs-property">bottom</span> = <span class="hljs-string">'auto'</span>;
  dragContainerStyle.<span class="hljs-property">top</span> = top + <span class="hljs-string">'px'</span>;
  dragContainerStyle.<span class="hljs-property">left</span> = left + <span class="hljs-string">'px'</span>;
&#125;;
<span class="hljs-comment">// 模式二：设置目标元素吸附位置</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">setElemSnapEdgeLocation</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">if</span> (!props.<span class="hljs-property">snapEdge</span>) <span class="hljs-keyword">return</span>;
  <span class="hljs-keyword">const</span> &#123; offsetLeft, offsetWidth &#125; = dragContainerRef.<span class="hljs-property">value</span>
  <span class="hljs-keyword">const</span> &#123; innerWidth &#125; = <span class="hljs-variable language_">window</span>
  <span class="hljs-keyword">if</span> (offsetLeft + offsetWidth / <span class="hljs-number">2</span> < innerWidth / <span class="hljs-number">2</span>) &#123;
    dragContainerStyle.<span class="hljs-property">left</span> = <span class="hljs-string">'0px'</span>
    dragContainerStyle.<span class="hljs-property">right</span> = <span class="hljs-string">'auto'</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    dragContainerStyle.<span class="hljs-property">right</span> = <span class="hljs-string">'0px'</span>
    dragContainerStyle.<span class="hljs-property">left</span> = <span class="hljs-string">'auto'</span>
  &#125;
  isShowSnapEdgeElem.<span class="hljs-property">value</span> = <span class="hljs-literal">true</span>
&#125;;

<span class="hljs-comment">// 隐藏吸附边缘的元素，显示操作元素</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">unShowSnapEdgeElem</span> = (<span class="hljs-params"></span>) => &#123;
  isShowSnapEdgeElem.<span class="hljs-property">value</span> = <span class="hljs-literal">false</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123; <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'click'</span>, showSnapEdgeElem) &#125;)
&#125;
<span class="hljs-keyword">const</span> <span class="hljs-title function_">showSnapEdgeElem</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">removeEventListener</span>(<span class="hljs-string">'click'</span>, showSnapEdgeElem)
  isShowSnapEdgeElem.<span class="hljs-property">value</span> = <span class="hljs-literal">true</span>
&#125;

<span class="hljs-comment">// pc端鼠标拖拽事件</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">onDragstart</span> = (<span class="hljs-params">evt: DragEvent</span>) => &#123;
  evt.<span class="hljs-title function_">preventDefault</span>();
  evt.<span class="hljs-title function_">stopPropagation</span>();
  <span class="hljs-keyword">const</span> &#123; clientX, clientY &#125; = evt;
  dragContainerRef.<span class="hljs-property">value</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'dragover'</span>, prevent);
  dragContainerRef.<span class="hljs-property">value</span>.<span class="hljs-property">parentNode</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'dragover'</span>, prevent);
  <span class="hljs-title function_">recordPointerLocation</span>(clientX, clientY);
&#125;;
<span class="hljs-keyword">const</span> <span class="hljs-title function_">onDragend</span> = (<span class="hljs-params">evt: DragEvent</span>) => &#123;
  evt.<span class="hljs-title function_">preventDefault</span>();
  evt.<span class="hljs-title function_">stopPropagation</span>();
  <span class="hljs-keyword">const</span> &#123; clientX, clientY, target &#125; = evt;
  dragContainerRef.<span class="hljs-property">value</span>.<span class="hljs-title function_">removeEventListener</span>(<span class="hljs-string">'dragover'</span>, prevent);
  dragContainerRef.<span class="hljs-property">value</span>.<span class="hljs-property">parentNode</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'dragover'</span>, prevent);
  <span class="hljs-title function_">setElemLocation</span>(clientX, clientY);
  <span class="hljs-title function_">setElemSnapEdgeLocation</span>()
&#125;;
<span class="hljs-keyword">const</span> <span class="hljs-title function_">prevent</span> = (<span class="hljs-params">evt: DragEvent</span>) => &#123;
  evt.<span class="hljs-title function_">preventDefault</span>();
  evt.<span class="hljs-property">dataTransfer</span>.<span class="hljs-property">dropEffect</span> = <span class="hljs-string">'move'</span>
&#125;;

<span class="hljs-comment">// 移动端</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">onTouchstart</span> = (<span class="hljs-params">evt: TouchEvent</span>) => &#123;
  evt.<span class="hljs-title function_">stopPropagation</span>();
  <span class="hljs-keyword">const</span> &#123; clientX, clientY &#125; = evt.<span class="hljs-property">touches</span>[<span class="hljs-number">0</span>];
  <span class="hljs-title function_">recordPointerLocation</span>(clientX, clientY);
  dragElemStyle.<span class="hljs-property">transform</span> = <span class="hljs-string">`scale(<span class="hljs-subst">$&#123;SCALE&#125;</span>)`</span>
&#125;;
<span class="hljs-keyword">const</span> <span class="hljs-title function_">onTouchmove</span> = (<span class="hljs-params">evt: TouchEvent</span>) => &#123;
  evt.<span class="hljs-title function_">preventDefault</span>();
  evt.<span class="hljs-title function_">stopPropagation</span>();
  <span class="hljs-keyword">const</span> &#123; clientX, clientY &#125; = evt.<span class="hljs-property">touches</span>[<span class="hljs-number">0</span>];
  <span class="hljs-title function_">setElemLocation</span>(clientX, clientY);
&#125;;
<span class="hljs-keyword">const</span> <span class="hljs-title function_">onTouchend</span> = (<span class="hljs-params">evt: TouchEvent</span>) => &#123;
  evt.<span class="hljs-title function_">stopPropagation</span>();
  <span class="hljs-title function_">setElemSnapEdgeLocation</span>()
  dragElemStyle.<span class="hljs-property">transform</span> = <span class="hljs-string">`scale(1)`</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            