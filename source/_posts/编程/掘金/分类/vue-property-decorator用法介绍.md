
---
title: 'vue-property-decorator用法介绍'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2854'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 05:01:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=2854'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>在Vue2.0中使用TypeScript语法时，需要引用 vue-property-decorator。</p>
<p>vue-property-decorator 完全依赖于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-class-component" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-class-component" ref="nofollow noopener noreferrer">vue-class-component</a>，因此在使用vue-property-decorator之前可以先了解下vue-class-component。</p>
<p>vue-property-decorator 把Vue2.0声明式的写法通过 es6 装饰器的方式，改造成构造函数式的写法，主要目的是让 vue 的开发模式更工程化。</p>
<h2 data-id="heading-1">Install</h2>
<pre><code class="hljs language-json copyable" lang="json">npm i -S vue-class-component
npm i -S vue-property-decorator 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">用法</h2>
<p>这里有几个装饰器和一个函数(Mixin):</p>
<ul>
<li><code>@Prop</code></li>
<li><code>@PropSync</code></li>
<li><code>@Model</code></li>
<li><code>@ModelSync</code></li>
<li><code>@Watch</code></li>
<li><code>@Provide</code></li>
<li><code>@Inject</code></li>
<li><code>@ProvideReactive</code></li>
<li><code>@InjectReactive</code></li>
<li><code>@Emit</code></li>
<li><code>@Ref</code></li>
<li><code>@VModel</code></li>
<li><code>@Component</code> (由 vue-class-component 提供)</li>
<li><code>Mixins</code> (<code>mixins</code> 函数 由 vue-class-component 提供)</li>
</ul>
<h2 data-id="heading-3">示例</h2>
<p><code>@Component</code>
即使没有组件也不能省略@Component，否则会报错。</p>
<pre><code class="copyable"><script lang="ts">
import &#123; Vue, Component &#125; from 'vue-property-decorator'

@Component
export default class extends Vue &#123; 
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件引用</p>
<pre><code class="copyable">import &#123; Component, Vue &#125; from "vue-property-decorator";
import DemoComponent"./DemoComponent.vue";
@Component(&#123;
  components: &#123;
    DemoComponent
  &#125;
&#125;)
export default class YourComponent extends Vue &#123; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>@Prop</code> 父子组件之间值的传递</p>
<pre><code class="copyable"><script lang="ts">
import &#123; Vue, Component, Prop &#125; from 'vue-property-decorator'
 
@Component
export default class YourComponent extends Vue &#123;
  @Prop(Number) readonly propA: number | undefined 
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于</p>
<pre><code class="copyable">export default &#123;
  props: &#123;
    propA: &#123;
      type: Number,
    &#125; 
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你不想设置每个prop的type类型，你可以使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frbuckton%2Freflect-metadata" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rbuckton/reflect-metadata" ref="nofollow noopener noreferrer">reflect-metadata</a>.</p>
<pre><code class="copyable">npm install reflect-metadata -D
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><script lang="ts">
import &#123; Vue, Component, Prop &#125; from 'vue-property-decorator'
import 'reflect-metadata'

@Component
export default class extends Vue &#123;
  @Prop() age!: number
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>@PropSync</code>
相当于在父组件中添加.sync装饰器, 使子组件也可以更新prop的值。具体查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Fcomponents-custom-events.html%23sync-%25E4%25BF%25AE%25E9%25A5%25B0%25E7%25AC%25A6" title="https://cn.vuejs.org/v2/guide/components-custom-events.html#sync-%E4%BF%AE%E9%A5%B0%E7%AC%A6" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer"><code>.sync</code> 修饰符</a></p>
<pre><code class="copyable"><script lang="ts">
import &#123; Vue, Component, PropSync &#125; from 'vue-property-decorator'
@Component
export default class extends Vue &#123;
  @PropSync('name', &#123; type: String &#125;) syncedName!: string; // 用来实现组件的双向绑定
 
  changeName(): void &#123;
    this.syncedName = '子组件修改过后的syncedName!'; // 更改syncedName会更改父组件的name 
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>@Watch</code> 监听属性</p>
<pre><code class="copyable">import &#123; Vue, Component, Watch &#125; from 'vue-property-decorator'
 
@Component
export default class YourComponent extends Vue &#123;
  @Watch('child')
  onChildChanged(val: string, oldVal: string) &#123;&#125;
 
  @Watch('person', &#123; immediate: true, deep: true &#125;)
  onPersonChanged1(val: Person, oldVal: Person) &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="copyable">export default &#123;
  watch: &#123;
    child: [
      &#123;
        handler: 'onChildChanged',
        immediate: false,
        deep: false,
      &#125;,
    ],
    person: [
      &#123;
        handler: 'onPersonChanged1',
        immediate: true,
        deep: true,
      &#125; 
    ],
  &#125;,
  methods: &#123;
    onChildChanged(val, oldVal) &#123;&#125;,
    onPersonChanged1(val, oldVal) &#123;&#125; 
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>@Emit</code></p>
<pre><code class="copyable">import &#123; Vue, Component, Emit &#125; from 'vue-property-decorator'
 
@Component
export default class YourComponent extends Vue &#123;
  @Emit()
  addToCount(n: number) &#123; 
  &#125;
 
  @Emit('reset')
  resetCount() &#123;
    this.count = 0
  &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="copyable">export default &#123;
  methods: &#123;
    addToCount(n) &#123; 
      this.$emit('add-to-count', n)
    &#125;,
    resetCount() &#123; 
      this.$emit('reset')
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>mixins</code> 混入公共方法</p>
<pre><code class="copyable">import &#123; Component, Vue &#125; from "vue-property-decorator";
import mixinsMethod from '@/plugins/mixins.js';

@Component(&#123;
  components: &#123;&#125;,
  mixins:[mixinsMethod]
&#125;)
export default class YourComponent extends Vue &#123; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>计算属性</code>
使用时只需 get 开头 + 方法 + 返回值</p>
<pre><code class="copyable">import &#123; Component, Vue &#125; from "vue-property-decorator";
@Component 
export default class YourComponent extends Vue &#123;
  type:  number = 0
  // 计算属性
  get getName() &#123;
    let type: any = &#123;
      1: 'Taobao',
      2: 'Pdd',
     &#125;;
     return type[this.type];
  &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvue-property-decorator" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/vue-property-decorator" ref="nofollow noopener noreferrer">vue-property-decorator - npm</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-class-component" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-class-component" ref="nofollow noopener noreferrer">vue-class-component</a></p></div>  
</div>
            