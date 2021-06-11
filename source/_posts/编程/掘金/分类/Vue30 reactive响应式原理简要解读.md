
---
title: 'Vue3.0 reactive响应式原理简要解读'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9342'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 18:01:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=9342'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.前言</h2>
<p>本人一直认为vue的数据响应式机制是它的灵魂，这也是本人更喜欢vue的原因之一。在2019.10.5日尤大发布了<code>Vue3.0</code>预览版源码，其中的响应式机制也被ES6中的新语法重写了，本人整理出了Vue3.0数据绑定的实现原理供大家参考。</p>
<h2 data-id="heading-1">2.Vue2.x的数据绑定机制</h2>
<p>读过<code>Vue2.x</code>源码的小伙伴肯定知道之前的数据绑定机制的原理，也就是利用<code>Object.defineProperty</code>来进行<code>拦截对象</code>，给对象的属性增加<code>set</code> 和 <code>get</code>方法，在<code>get</code>方法中收集依赖，在<code>set</code>方法中通知依赖更新视图，但是这种机制存在一定的缺陷：</p>
<ul>
<li>需要深度递归遍历对象，浪费内存</li>
<li><code>Object.defineProperty</code>无法监听数组的变化，所以需要手动封装数组方法劫持</li>
<li>对象中越过<code>get/set</code>方法，直接增加键值对无法对新增的键值对进行数据绑定</li>
</ul>
<p>以下简要说一下<code>vue2.x</code>的数据绑定机制：</p>
<blockquote>
<h3 data-id="heading-2">对象拦截</h3>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observer</span>(<span class="hljs-params">target</span>)</span>&#123;
    <span class="hljs-comment">// 如果不是对象数据类型直接返回即可</span>
    <span class="hljs-keyword">if</span>(!isObject(target))&#123;
        <span class="hljs-keyword">return</span> target
    &#125;
    <span class="hljs-comment">// 重新定义key</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> target)&#123;
        defineReactive(target,key,target[key])
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isObject</span>(<span class="hljs-params">target</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> target === <span class="hljs-string">"object"</span> && target !== <span class="hljs-literal">null</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive</span>(<span class="hljs-params">obj,key,value</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(isObject(value))&#123;
        observer(value); <span class="hljs-comment">//值为对象类型需要深层递归劫持</span>
    &#125;
    
    <span class="hljs-built_in">Object</span>.defineProperty(obj,key,&#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-comment">// 在get 方法中收集依赖</span>
            <span class="hljs-keyword">return</span> value
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newVal</span>)</span>&#123;
            <span class="hljs-keyword">if</span>(newVal !== value)&#123;
                <span class="hljs-comment">// 为对象类型需要继续劫持</span>
                <span class="hljs-keyword">if</span>(isObject(value))&#123;
                    observer(value);
                &#125;
                update(); <span class="hljs-comment">// 在set方法中触发更新</span>
            &#125;
        &#125;
    &#125;)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'update view'</span>)
&#125;

<span class="hljs-keyword">let</span> obj = &#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'youxuan'</span>&#125;
observer(obj);
obj.name = <span class="hljs-string">'webyouxuan'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h3 data-id="heading-3">数组方法劫持</h3>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> oldProtoMehtods = <span class="hljs-built_in">Array</span>.prototype;
<span class="hljs-keyword">const</span> proto = <span class="hljs-built_in">Object</span>.create(oldProtoMehtods);
[<span class="hljs-string">'push'</span>,<span class="hljs-string">'pop'</span>,<span class="hljs-string">'shift'</span>,<span class="hljs-string">'unshift'</span>,...].forEach(<span class="hljs-function"><span class="hljs-params">method</span>=></span>&#123;
    <span class="hljs-built_in">Object</span>.defineProperty(proto,method,&#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span>&#123;
            update();
            oldProtoMehtods[method].call(<span class="hljs-built_in">this</span>,...arguments)
        &#125;
    &#125;)
&#125;)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observer</span>(<span class="hljs-params">target</span>)</span>&#123;
    <span class="hljs-comment">// 如果不是对象数据类型直接返回即可</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> target !== <span class="hljs-string">'object'</span>)&#123;
        <span class="hljs-keyword">return</span> target
    &#125;
    
    <span class="hljs-comment">// 如果为数组为数组添加自定义数据劫持方法</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Array</span>.isArray(target))&#123;
        <span class="hljs-built_in">Object</span>.setPrototypeOf(target,proto);
        <span class="hljs-comment">// 给数组中的每一项进行observr</span>
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span> ; i < target.length;i++)&#123;
            observer(target[i])
        &#125;
        <span class="hljs-keyword">return</span>
    &#125;;
    <span class="hljs-comment">// 重新定义key</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> target)&#123;
        defineReactive(target,key,target[key])
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此处对<code>Vue2.x</code>的数据绑定原理就不过多阐述了，接下来我们把焦点放在<code>Vue3.0</code>上来。</p>
<h2 data-id="heading-4">3.Vue3.0源码目录剖析</h2>
<pre><code class="hljs language-base copyable" lang="base">├── packages
│   ├── compiler-core # 所有平台的编译器
│   ├── compiler-dom # 针对浏览器而写的编译器
│   ├── reactivity # 数据响应式系统
│   ├── runtime-core # 虚拟 DOM 渲染器 ，Vue 组件和 Vue 的各种API
│   ├── runtime-dom # 针对浏览器的 runtime。其功能包括处理原生 DOM API、DOM 事件和 DOM 属性等。
│   ├── runtime-test # 专门为测试写的runtime
│   ├── server-renderer # 用于SSR
│   ├── shared # 帮助方法
│   ├── template-explorer
│   └── vue # 构建vue runtime + compiler
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>compiler</strong>
<code>compiler-core</code>主要功能是暴露编译相关的<code>API</code>以及<code>baseCompile</code>方法
<code>compiler-dom</code>基于<code>compiler-core</code>封装针对浏览器的<code>compiler</code> (对浏览器标签进行处理)</p>
<p><strong>runtime</strong>
<code>runtime-core</code> 虚拟 DOM 渲染器、Vue 组件和 Vue 的各种API
<code>runtime-test</code>将<code>DOM</code>结构格式化成对象，方便测试
<code>runtime-dom</code> 基于<code>runtime-core</code>编写的浏览器的<code>runtime</code> (增加了节点的增删改查，样式处理等)，返回<code>render</code>、<code>createApp</code>方法</p>
<p><strong>reactivity</strong>
单独的数据响应式系统，核心方法<code>reactive</code>、<code>effect</code>、 <code>ref</code>、<code>computed</code></p>
<p><strong>vue</strong>
整合 <code>compiler</code> + <code>runtime</code></p>
<h2 data-id="heading-5">4.Vue3.0初体验</h2>
<p>由上面<code>Vue3.0</code>的目录结构来看整个项目还是非常清晰的，对于目前想要体验<code>vue3.0</code>的同学来说，官方脚手架也已经发布了支持vue-next版本的脚手架  <a href="https://github.com/vuejs/vue-cli-plugin-vue-next" target="_blank" rel="nofollow noopener noreferrer"><code>vue-cli-plugin-vue-next</code></a> ，具体体验方法如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># in an existing Vue CLI project</span>
vue add vue-next
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先使用<code>vue-cli</code>初始化一个项目，然后在项目根目录下命令行中输入 <code>vue add vue-next</code>即可。</p>
<blockquote>
<p>请注意：<code>vue-cli</code>版本必须更新到<code>v4.3.1</code>，并且<code>vue-router</code>以及<code>vuex</code>目前<code>vue3.0</code>并未支持。            — 20200511</p>
</blockquote>
<p>以下是简单的<code>vue3.0</code>代码演示：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <div>鼠标X坐标---&#123;&#123;x&#125;&#125;</div>
    <div>鼠标Y坐标---&#123;&#123;y&#125;&#125;</div>
  </div>
</template>

<script>
// 类似react hooks的方式，特有钩子直接从vue中导入
import &#123; ref, onMounted, onUnmounted &#125; from "vue";
    
// 特有逻辑函数剥离 vue3.0的好处    
function usePosition() &#123;
  // 实时获取鼠标位置
  const x = ref(0);
  const y = ref(0);
  function update(e) &#123;
    x.value = e.pageX;
    y.value = e.pageY;
  &#125;
  onMounted(() => &#123;
    window.addEventListener("mousemove", update);
  &#125;);
  onUnmounted(() => &#123;
    window.removeEventListener("mousemove", update);
  &#125;);

  return &#123;
    x,
    y
  &#125;;
&#125;
    
    
export default &#123;
  setup() &#123;
    const &#123; x, y &#125; = usePosition(); // 使用公共逻辑
    return &#123;
      x,
      y
    &#125;;
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">5.Vue3.0数据绑定解析</h2>
<p>在学习<code>Vue3.0</code>之前，必须要先熟练掌握ES6中的 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy" target="_blank" rel="nofollow noopener noreferrer">Proxy</a>、<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/reflect" target="_blank" rel="nofollow noopener noreferrer">Reflect</a> 及 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/map" target="_blank" rel="nofollow noopener noreferrer">Map</a>、<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/set" target="_blank" rel="nofollow noopener noreferrer">Set</a>两种数据结构，如果不熟悉的同学建议先熟练了解这些知识。</p>
<p>我们首先看<code>Vue3.0</code>中是如何实现数据绑定的</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> person = Vue.reactive(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'cangshudada'</span>&#125;); <span class="hljs-comment">//person对象已经成为响应式数据</span>
Vue.effect(<span class="hljs-function">()=></span>&#123; <span class="hljs-comment">// effect方法会立即触发一次</span>
    <span class="hljs-built_in">console</span>.log(person.name);
&#125;)

person.name = <span class="hljs-string">'仓鼠大大'</span>;; <span class="hljs-comment">// 当属性修改后会再次触发effect方法</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>源码是采用<code>ts</code>编写，由于可能有不熟悉ts的同学，这里我们采用js来从0编写实现原理，之后再看源码就会比较轻松啦！</p>
</blockquote>
<h3 data-id="heading-7">5.1 reactive实现</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 *
 * <span class="hljs-doctag">@description </span>生成响应式对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;any&#125;</span> <span class="hljs-variable">target</span></span>
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">target</span>) </span>&#123;
    <span class="hljs-comment">// 创建响应式对象</span>
    <span class="hljs-keyword">return</span> createReactiveObject(target);
&#125;

<span class="hljs-comment">/**
 *
 * <span class="hljs-doctag">@description </span>判断是不是object
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;any&#125;</span> <span class="hljs-variable">target</span></span>
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;boolean&#125;</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isObject</span>(<span class="hljs-params">target</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> target === <span class="hljs-string">"object"</span> && target !== <span class="hljs-literal">null</span>;
&#125;

<span class="hljs-comment">/**
 *
 * <span class="hljs-doctag">@description </span>创造响应式对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;any&#125;</span> <span class="hljs-variable">target</span></span>
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createReactiveObject</span>(<span class="hljs-params">target</span>)</span>&#123;
    <span class="hljs-comment">// 判断target是不是对象,不是对象直接返回</span>
    <span class="hljs-keyword">if</span>(!isObject(target))&#123;
        <span class="hljs-keyword">return</span> target;
    &#125;
    
    <span class="hljs-comment">// get set delete ...对象方法</span>
    <span class="hljs-keyword">const</span> handlers = &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target,key,receiver</span>)</span>&#123; <span class="hljs-comment">// 取值</span>
            <span class="hljs-keyword">let</span> res = <span class="hljs-built_in">Reflect</span>.get(target,key,receiver);
            <span class="hljs-keyword">return</span> res;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target,key,value,receiver</span>)</span>&#123; <span class="hljs-comment">// 更改/新增属性</span>
            <span class="hljs-keyword">let</span> result = <span class="hljs-built_in">Reflect</span>.set(target,key,value,receiver);
            <span class="hljs-keyword">return</span> result;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">deleteProperty</span>(<span class="hljs-params">target,key</span>)</span>&#123; <span class="hljs-comment">// 删除属性</span>
            <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Reflect</span>.deleteProperty(target,key);
            <span class="hljs-keyword">return</span> result;
        &#125;
    &#125;
    <span class="hljs-comment">// 开始代理</span>
    observed = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target,handlers);
    <span class="hljs-keyword">return</span> observed;
&#125;
<span class="hljs-keyword">let</span> p = reactive(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'cangshudada'</span>&#125;);
<span class="hljs-built_in">console</span>.log(p.name); <span class="hljs-comment">// 取值</span>
p.name = <span class="hljs-string">'仓鼠大大'</span>; <span class="hljs-comment">// 设置</span>
<span class="hljs-keyword">delete</span> p.name; <span class="hljs-comment">// 删除</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是可能存在这样的对象</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> person =&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'cangshudada'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">24</span>,
    <span class="hljs-attr">pets</span>: &#123;
        <span class="hljs-attr">dog</span>: &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'guagua'</span>,
            <span class="hljs-attr">age</span>: <span class="hljs-number">1</span>
        &#125;,
        <span class="hljs-attr">cat</span>: &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'gugu'</span>,
            <span class="hljs-attr">age</span>: <span class="hljs-number">2</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以我们得继续实现<strong>多层对象嵌套</strong>情况下的代理：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key, receiver</span>)</span> &#123;
    <span class="hljs-comment">// 取值</span>
    <span class="hljs-keyword">const</span> res = <span class="hljs-built_in">Reflect</span>.get(target, key, receiver);
    <span class="hljs-keyword">return</span> isObject(res) ? reactive(res) : res; <span class="hljs-comment">// 懒代理，只有当取值时再次做代理，vue2.0中一上来就会全部递归增加getter,setter</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们继续考虑<strong>数组</strong>的情况</p>
<p><code>Proxy</code>默认是可以支持数组，所以我们不需要像<code>Vue2.x</code>中一样对数组封装自己的方法并在其中来劫持监听数据改变，但是我们改变数组的时候仍然能够发现问题，那就是数组的改变会触发两次set，分别是<strong>数组的长度变化</strong>以及<strong>索引值的变化</strong>，接下来我们就需要屏蔽掉多次触发的问题。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, value, receiver</span>)</span> &#123;
    <span class="hljs-keyword">const</span> oldValue = target[key];
    <span class="hljs-keyword">const</span> hadKey = target.hasOwnProperty(key);
    <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Reflect</span>.set(target, key, value, receiver);
    <span class="hljs-comment">// 判断是否是新增还是修改的情况</span>
    <span class="hljs-keyword">if</span> (!hadKey) &#123; <span class="hljs-comment">//无key的情况则是新增</span>
        trigger(target, <span class="hljs-string">'add'</span>, key)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldValue !== value) &#123; <span class="hljs-comment">//防止数组重复操作修改索引或者length的时候多次触发set</span>
        trigger(target, <span class="hljs-string">'set'</span>, key)
    &#125;
    <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时数组的问题也解决了，最后就是对<strong>同一对象重复代理的兼容</strong>，这里我们利用<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/WeakMap" target="_blank" rel="nofollow noopener noreferrer">WeakMap </a>来解决，这样完整的<code>reactive</code> 实现如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> toProxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>(); <span class="hljs-comment">// 存放被代理过的对象</span>
<span class="hljs-keyword">const</span> toRaw = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>(); <span class="hljs-comment">// 存放已经代理过的对象</span>

<span class="hljs-comment">/**
 *
 * <span class="hljs-doctag">@description </span>生成响应式对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;any&#125;</span> <span class="hljs-variable">target</span></span>
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">target</span>) </span>&#123;
    <span class="hljs-comment">// 创建响应式对象</span>
    <span class="hljs-keyword">return</span> createReactiveObject(target);
&#125;


<span class="hljs-comment">/**
 *
 * <span class="hljs-doctag">@description </span>判断是不是object
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;any&#125;</span> <span class="hljs-variable">target</span></span>
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;boolean&#125;</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isObject</span>(<span class="hljs-params">target</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> target === <span class="hljs-string">"object"</span> && target !== <span class="hljs-literal">null</span>;
&#125;


<span class="hljs-comment">/**
 *
 * <span class="hljs-doctag">@description </span>判断对象中是否有该键
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;object&#125;</span> <span class="hljs-variable">target</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;object&#125;</span> <span class="hljs-variable">key</span></span>
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;boolean&#125;</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hasOwn</span>(<span class="hljs-params">target, key</span>) </span>&#123;
    <span class="hljs-keyword">return</span> target.hasOwnProperty(key);
&#125;

<span class="hljs-comment">/**
 *
 * <span class="hljs-doctag">@description </span>创造响应式对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;any&#125;</span> <span class="hljs-variable">target</span></span>
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createReactiveObject</span>(<span class="hljs-params">target</span>) </span>&#123;

    <span class="hljs-comment">// 是否是对象</span>
    <span class="hljs-keyword">if</span> (!isObject(target)) &#123;
        <span class="hljs-keyword">return</span> target;
    &#125;

    <span class="hljs-comment">// 判断取到被代理的对象</span>
    <span class="hljs-keyword">let</span> observed = toProxy.get(target);

    <span class="hljs-keyword">if</span> (observed) &#123; <span class="hljs-comment">// 判断是否被代理过</span>
        <span class="hljs-keyword">return</span> observed;
    &#125;
    <span class="hljs-keyword">if</span> (toRaw.has(target)) &#123; <span class="hljs-comment">// 判断重复代理的情况,如果重复代理</span>
        <span class="hljs-keyword">return</span> target;
    &#125;

    <span class="hljs-keyword">const</span> handlers = &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key, receiver</span>)</span> &#123;
            <span class="hljs-comment">// 取值</span>
            <span class="hljs-keyword">const</span> res = <span class="hljs-built_in">Reflect</span>.get(target, key, receiver);
            track(target, <span class="hljs-string">'get'</span>, key)；<span class="hljs-comment">//收集依赖</span>
            <span class="hljs-keyword">return</span> isObject(res) ? reactive(res) : res; <span class="hljs-comment">// 懒代理，只有当取值时再次做代理，vue2.0中一上来就会全部递归增加getter,setter</span>
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, value, receiver</span>)</span> &#123;
            <span class="hljs-keyword">const</span> oldValue = target[key];
            <span class="hljs-keyword">const</span> hadKey = hasOwn(target, key);
            <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Reflect</span>.set(target, key, value, receiver);
            <span class="hljs-comment">// 判断是否是新增还是修改的情况</span>
            <span class="hljs-keyword">if</span> (!hadKey) &#123; <span class="hljs-comment">//无key的情况则是新增</span>
                trigger(target, <span class="hljs-string">'add'</span>, key) <span class="hljs-comment">// 触发依赖更新 - 增加</span>
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldValue !== value) &#123; <span class="hljs-comment">//防止数组重复操作修改索引或者length的时候多次触发set</span>
                trigger(target, <span class="hljs-string">'set'</span>, key) <span class="hljs-comment">// 触发依赖更新 - 修改</span>
            &#125;
            <span class="hljs-keyword">return</span> result;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">deleteProperty</span>(<span class="hljs-params">target, key</span>)</span> &#123;
            trigger(target, <span class="hljs-string">'delete'</span>, key)；<span class="hljs-comment">// 触发依赖更新 - 删除 </span>
            <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Reflect</span>.deleteProperty(target, key);
            <span class="hljs-keyword">return</span> result;
        &#125;
    &#125;;

    <span class="hljs-comment">// 开始代理</span>
    observed = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handlers);
    toProxy.set(target, observed);
    toRaw.set(observed, target); <span class="hljs-comment">// 做映射表</span>
    <span class="hljs-keyword">return</span> observed;
&#125;

<span class="hljs-comment">// 对象的情况</span>
<span class="hljs-keyword">const</span> person = reactive(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'cangshudada'</span> &#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'person.name >>'</span>, person.name); <span class="hljs-comment">// 获取</span>
person.name = <span class="hljs-string">'仓鼠大大'</span>; <span class="hljs-comment">// 设置</span>
<span class="hljs-keyword">delete</span> person.name; <span class="hljs-comment">// 删除</span>
person.age = <span class="hljs-number">12</span>;<span class="hljs-comment">//能够代理到直接在对象增加的键</span>
person.age = <span class="hljs-number">24</span>

<span class="hljs-comment">// 能够直接代理数组以及重复代理的情况</span>
<span class="hljs-keyword">const</span> ary = reactive([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]);
ary.push(<span class="hljs-number">5</span>)
<span class="hljs-keyword">const</span> ary1 = reactive(ary); <span class="hljs-comment">//此时重复代理会直接返回之前代理过的对象</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>到这里<code>reactive</code>方法已经基本实现完毕，接下来就是与<code>Vue2.x</code>中的逻辑一样进行依赖收集和触发依赖更新了，其中<code>track</code>的作用是对依赖进行收集，收集的主要是<code>effect</code>，<code>trigger</code>方法则是通知<code>effect</code>更新</p>
</blockquote>
<h3 data-id="heading-8">5.2 effect实现</h3>
<p><code>effect</code>也就是副作用的意思，这个方法默认会在调用的时候率先执行一次，之后如果数据有变化后则会再次触发此回调函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> person = Vue.reactive(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'cangshudada'</span>&#125;); <span class="hljs-comment">//person对象已经成为响应式数据</span>
Vue.effect(<span class="hljs-function">()=></span>&#123; <span class="hljs-comment">// effect方法会立即触发一次</span>
    <span class="hljs-built_in">console</span>.log(person.name);
&#125;)

person.name = <span class="hljs-string">'仓鼠大大'</span>;; <span class="hljs-comment">// 当属性修改后会再次触发effect方法</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先来实现<code>effect</code>函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-comment">/**
 *
 * <span class="hljs-doctag">@description </span>effect函数
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;function&#125;</span> </span>fn 回调函数
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">effect</span>(<span class="hljs-params">fn</span>) </span>&#123;
    <span class="hljs-keyword">const</span> effect = createReactiveEffect(fn); <span class="hljs-comment">// 创建响应式的effect</span>
    effect(); <span class="hljs-comment">// 首先执行一次</span>
    <span class="hljs-keyword">return</span> effect;
&#125;

<span class="hljs-comment">// 存放响应式effect</span>
<span class="hljs-keyword">const</span> activeReactiveEffectStack = []; 

<span class="hljs-comment">/**
 *
 *
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;function&#125;</span> </span>fn 回调函数
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createReactiveEffect</span>(<span class="hljs-params">fn</span>) </span>&#123;
    <span class="hljs-keyword">const</span> effect = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// 响应式的effect</span>
        <span class="hljs-keyword">return</span> run(effect, fn);
    &#125;;
    <span class="hljs-keyword">return</span> effect;
&#125;


<span class="hljs-comment">/**
 *
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;function&#125;</span> </span>effect 响应式的effect
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;function&#125;</span> </span>fn 回调函数
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span>(<span class="hljs-params">effect, fn</span>) </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
        activeReactiveEffectStack.push(effect);
        <span class="hljs-keyword">return</span> fn(); <span class="hljs-comment">// 先让fn执行,执行时会触发get方法，可以将effect存入对应的key属性</span>
    &#125; <span class="hljs-keyword">finally</span> &#123;
        activeReactiveEffectStack.pop(effect);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当调用<code>fn()</code>时可能会触发<code>get</code>方法，此时会触发上面<strong>get</strong>中调用的<code>track</code>函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> targetMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">track</span>(<span class="hljs-params">target,type,key</span>)</span>&#123;
    <span class="hljs-comment">// 查看是否有effect</span>
    <span class="hljs-keyword">const</span> effect = activeReactiveEffectStack[activeReactiveEffectStack.length-<span class="hljs-number">1</span>];
    <span class="hljs-keyword">if</span>(effect)&#123;
        <span class="hljs-keyword">const</span> depsMap = targetMap.get(target);
        <span class="hljs-keyword">if</span>(!depsMap)&#123; <span class="hljs-comment">// 如果不存在依赖数组对象则添加Map对象</span>
            targetMap.set(target,depsMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>());
        &#125;
        <span class="hljs-keyword">const</span> deps = depsMap.get(target); 
        <span class="hljs-keyword">if</span>(!deps)&#123; <span class="hljs-comment">//如果deps不存在则增加Set数组</span>
            depsMap.set(key,(deps = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()));
        &#125;
        <span class="hljs-keyword">if</span>(!deps.has(effect))&#123; <span class="hljs-comment">//如果deps中没有这个effect就将effect添加到依赖数组中</span>
            deps.add(effect); 
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当更新属性时会触发<code>trigger</code>执行，并根据<code>key</code>值找到对应的存储集合中的<code>effect</code>依次执行</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trigger</span>(<span class="hljs-params">target,type,key</span>)</span>&#123;
    <span class="hljs-keyword">const</span> depsMap = targetMap.get(target);
    <span class="hljs-keyword">if</span>(!depsMap)&#123;
        <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-keyword">const</span> deps = depsMap.get(key);
    <span class="hljs-keyword">if</span>(deps)&#123;
        deps.forEach(<span class="hljs-function"><span class="hljs-params">effect</span>=></span>&#123;
            effect();
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候其实还存在<code>length</code>的问题，比如我们在<code>effect</code>中监听数组的<code>length</code>，这个时候因为我们上面在<strong>set</strong>函数中设置了<code>length</code>改变不触发<code>trigger</code>函数的机制，所以还需要在<code>trigger</code>中增加判断来兼容这种情况</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trigger</span>(<span class="hljs-params">target, type, key</span>) </span>&#123;
  <span class="hljs-keyword">const</span> depsMap = targetMap.get(target);
  <span class="hljs-keyword">if</span> (!depsMap) &#123;
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-keyword">const</span> deps = depsMap.get(key);
  <span class="hljs-keyword">if</span> (deps) &#123;
    deps.forEach(<span class="hljs-function"><span class="hljs-params">effect</span> =></span> &#123;
      deps();
    &#125;);
  &#125;
  <span class="hljs-comment">// 兼容处理当前更新类型是增加时，如果用到数组的length的effect应该也会被执行</span>
  <span class="hljs-keyword">if</span> (type === <span class="hljs-string">"add"</span>) &#123;
    <span class="hljs-keyword">const</span> lengthDeps = depsMap.get(<span class="hljs-string">"length"</span>);
    <span class="hljs-keyword">if</span> (lengthDeps) &#123;
      lengthDeps.forEach(<span class="hljs-function"><span class="hljs-params">effect</span> =></span> &#123;
        effect();
      &#125;);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">5.3 ref实现</h3>
<p>ref可以将原始数据类型同样转换成响应式数据，这个时候需要通过<code>.value</code>属性获取值</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/*
*
* @description 不同类型的数据响应式处理 如果是对象通过reactive函数进行数据绑定否则直接返回
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">convert</span>(<span class="hljs-params">target</span>) </span>&#123;
  <span class="hljs-keyword">return</span> isObject(target) ? reactive(target) : target;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ref</span>(<span class="hljs-params">raw</span>) </span>&#123;
  raw = convert(raw);
  <span class="hljs-keyword">const</span> v = &#123;
    <span class="hljs-attr">_isRef</span>:<span class="hljs-literal">true</span>, <span class="hljs-comment">// 标识是ref类型</span>
    <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
      track(v, <span class="hljs-string">"get"</span>, <span class="hljs-string">""</span>);
      <span class="hljs-keyword">return</span> raw;
    &#125;,
    <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">newVal</span>) &#123;
      raw = newVal;
      trigger(v,<span class="hljs-string">'set'</span>,<span class="hljs-string">''</span>);
    &#125;
  &#125;;
  <span class="hljs-keyword">return</span> v;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候问题又来了，假如出现如下情况，则每次调用都得多加一个<code>.value</code>就会非常麻烦，所以我们也得对这种情况做个兼容</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> name = ref(<span class="hljs-string">'cangshudada'</span>);
<span class="hljs-keyword">const</span> person = reactive(&#123;
    <span class="hljs-attr">c_Name</span>: name
&#125;);
<span class="hljs-built_in">console</span>.log(person.c_Name.value); <span class="hljs-comment">// 每次调用c.a都得加上.value 比较麻烦</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候需要在<code>get</code>函数中兼容</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key, receiver</span>)</span> &#123;
    <span class="hljs-comment">// 取值</span>
    <span class="hljs-keyword">const</span> res = <span class="hljs-built_in">Reflect</span>.get(target, key, receiver);
    <span class="hljs-comment">// 兼容ref的value情况 因为前面的判断所以ref不可能为对象 可以直接返回</span>
    <span class="hljs-keyword">if</span>(res._isRef)&#123;
        <span class="hljs-keyword">return</span> res.value
    &#125;
    track(target, <span class="hljs-string">'get'</span>, key)；<span class="hljs-comment">//收集依赖</span>
    <span class="hljs-keyword">return</span> isObject(res) ? reactive(res) : res; <span class="hljs-comment">// 懒代理</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">5.4 computed实现</h3>
<p>之前版本的<code>computed</code>函数会缓存监听变量的值，只有当监听的变量值发生变化函数才会触发，在实际项目中用处非常大，如今<code>vue3.0</code>响应式数据机制重写，也导致了<code>computed</code>的重写，我们来看看在<code>vue3.0</code> <code>computed</code>是如何实现的，首先我们来看看用法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> person = reactive(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'cangshudada'</span>&#125;);
<span class="hljs-keyword">const</span> _computed = computed(<span class="hljs-function">()=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'computed执行了'</span>)  
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;person.name&#125;</span> --- xixi`</span>;
&#125;)
<span class="hljs-comment">// 不取_computed.value值则回调函数不执行，除非监听对象改变则取n次只执行一次</span>
<span class="hljs-built_in">console</span>.log(_computed.value);<span class="hljs-comment">// computed执行了 cangshudada --- xixi</span>
<span class="hljs-built_in">console</span>.log(_computed.value);<span class="hljs-comment">// cangshudada --- xixi</span>
person.name = <span class="hljs-string">'仓鼠大大'</span>;
<span class="hljs-built_in">console</span>.log(_computed.value);<span class="hljs-comment">// computed执行了 仓鼠大大 --- xixi</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>computed实现</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computed</span>(<span class="hljs-params">fn</span>)</span>&#123;
  <span class="hljs-keyword">let</span> dirty = <span class="hljs-literal">true</span>; <span class="hljs-comment">// 第一次取值会触发</span>
  <span class="hljs-keyword">const</span> runner = effect(fn,&#123; <span class="hljs-comment">// 标识这个effect是懒执行</span>
    <span class="hljs-attr">lazy</span>:<span class="hljs-literal">true</span>, <span class="hljs-comment">// 懒执行</span>
    <span class="hljs-attr">scheduler</span>:<span class="hljs-function">()=></span>&#123; <span class="hljs-comment">// 当依赖的属性变化了，调用此方法，而不是重新执行effect 依赖不更新则不更新dirty，进而不会触发runner()，缓存机制</span>
      dirty = <span class="hljs-literal">true</span>;
    &#125;
  &#125;);
  <span class="hljs-keyword">let</span> value;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">_isRef</span>:<span class="hljs-literal">true</span>,
    <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>()&#123;
      <span class="hljs-keyword">if</span>(dirty)&#123;
        value = runner(); <span class="hljs-comment">// 执行runner会继续收集依赖</span>
        dirty = <span class="hljs-literal">false</span>;
      &#125; 
      <span class="hljs-keyword">return</span> value; <span class="hljs-comment">// value没变化不会执行computed回调</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改<code>effect</code>函数 此处建议结合<code>5.2 effect</code>实现查看</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">effect</span>(<span class="hljs-params">fn,options</span>) </span>&#123;
  <span class="hljs-keyword">let</span> effect = createReactiveEffect(fn,options);
  <span class="hljs-keyword">if</span>(!options.lazy)&#123; <span class="hljs-comment">// 如果是lazy 则不立即执行</span>
    effect();
  &#125;
  <span class="hljs-keyword">return</span> effect;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createReactiveEffect</span>(<span class="hljs-params">fn,options</span>) </span>&#123;
  <span class="hljs-keyword">const</span> effect = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> run(effect, fn);
  &#125;;
  effect.scheduler = options.scheduler;

  <span class="hljs-keyword">return</span> effect;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>trigger</code>时判断</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">deps.forEach(<span class="hljs-function"><span class="hljs-params">effect</span> =></span> &#123;
  <span class="hljs-keyword">if</span>(effect.scheduler)&#123; <span class="hljs-comment">// 如果有scheduler 说明不需要执行effect</span>
    effect.scheduler(); <span class="hljs-comment">// 将dirty设置为true,下次获取值时变可以重新执行runner方法</span>
  &#125;<span class="hljs-keyword">else</span>&#123;
    effect(); <span class="hljs-comment">// 否则正常执行effect即可</span>
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> person = reactive(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'cangshudada'</span>&#125;);
<span class="hljs-keyword">const</span> _computed = computed(<span class="hljs-function">()=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'computed执行了'</span>)  
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;person.name&#125;</span> --- xixi`</span>;
&#125;)
<span class="hljs-comment">// 不取_computed.value值则回调函数不执行，除非监听对象改变则取n次只执行一次</span>
<span class="hljs-built_in">console</span>.log(_computed.value);
person.name = <span class="hljs-string">'仓鼠大大'</span>; <span class="hljs-comment">// 更改值 不会触发重新计算,但是会将dirty变成true</span>
<span class="hljs-built_in">console</span>.log(_computed.value); <span class="hljs-comment">// 此时触发get函数进而调用runner()重新调用计算方法</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">6.总结</h2>
<p>至此我们就将<code>Vue3.0</code>源码中的 <code>reactivity</code> 部分解析完毕了！了解了vue的数据绑定机制对于之后不管是面试还是后期的应用都有着很大的帮助，当然本篇文章只是对这部分进行了简要地解析，清楚了数据绑定这部分的逻辑与思想后再来读源码这部分相信各位会有更多的收获。
本文实际发布时间较早，当时未能发布到社区，今天整理了一下重新发布出来，如各位有兴趣的话本人也会对其他模块进行解析并进行解读。当然若对本文有不同理解或意见的欢迎评论区交流，一起学习进步～</p></div>  
</div>
            