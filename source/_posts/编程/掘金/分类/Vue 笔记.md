
---
title: 'Vue 笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=871'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 00:33:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=871'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>============== vue ==================</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjiongks.name%2Fblog%2Fvue-code-review%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jiongks.name/blog/vue-code-review/" ref="nofollow noopener noreferrer">jiongks.name/blog/vue-co…</a></li>
<li>在进行DOM树的渲染时，render渲染函数的优先级最高，template次之且需编译成渲染函数，而挂载点el属性对应的元素若存在，则在前两者均不存在时，其outerHTML才会用于编译与渲染。</li>
</ul>
<h1 data-id="heading-0">vue 生命周期：</h1>
<pre><code class="copyable">1. new Vue() 
-   init Events & lifecycle
2. beforeCreate - 
init injections & reactivity
// resolve injections before data/props
// resolve provide after data/props
3. created - 依赖收集 data, method 已经有init
获取挂载的DOM 父节点
4. beforeMount -  virtual dom 已经创建
compile template or el ， 通过render 函数，vnode -> virdom tree
挂载dom
5. mounted - dom 已经挂载， 监听update

5.1beforeupdate 
 virtual dom re-render and patch
5.2 updated

6. beforeDestroy

7. destroyed

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">Vue.prototype._init(opt)&#123;
    ... 合并选项
    ... 设置初始值 ，事件 等数据
    initLifecycle(vm)
    callHook(vm, 'beforeCreate');
    ... 初始化选项等数据，依赖收集
    callHook(vm, 'created');
    ...获取挂载的DOM 父节点
    callHook(vm, 'beforeMount');
    ...解析模板成渲染函数，并执行渲染函数，生成DOM插入页面
    vm._isMounted = true;
    callHook(vm, 'mounted');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">vue options :</h1>
<ul>
<li>option/数据： data, props, computed, watch, methods, propsData - 只能用与 new Vue()实例中，区别于component</li>
<li>option/dom : el, template, render, renderError - developer 模式有效</li>
<li>option/lifehook: lifecycle</li>
<li>option/res: directives - 自定义指令， filters - | 连接多个filter,  components - 组件</li>
<li>option/组合：mixins, parent - , extends - 扩展一个组件， provide/inject
<pre><code class="hljs language-说明 copyable" lang="说明">  mixins - 数组
  extends: 单个
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h1 data-id="heading-2">Vue api</h1>
<h3 data-id="heading-3">全局:</h3>
<ul>
<li>Vue.component</li>
<li>Vue.use</li>
<li>Vue.extend</li>
<li>Vue.filter</li>
<li>Vue.complile</li>
<li>Vue.set</li>
<li>Vue.delete</li>
<li>Vue.mixin</li>
<li>Vue.directive</li>
<li>Vue.nextTick</li>
</ul>
<h1 data-id="heading-4">响应式原理：</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F53217382" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/53217382" ref="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/53217382</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2Fcdd7dde12786" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/cdd7dde12786" ref="nofollow noopener noreferrer">www.jianshu.com/p/cdd7dde12…</a></li>
</ul>
<ol>
<li>核心Observer,Dep, Watcher；</li>
<li>Observer 进行数据监听绑定， get 收集依赖， set 触发 watcher 回调</li>
<li></li>
</ol>
<h3 data-id="heading-5">问题</h3>
<ul>
<li>数据怎么实现监听？        - defineObjectProperty&#123; set, get&#125;, proxy</li>
<li>数据改变，要更新哪些视图   - 依赖收集, get  (页面、watch/computed)</li>
<li>什么时间更新              -  set 依赖更新</li>
</ul>
<h3 data-id="heading-6">源码实现</h3>
<ol>
<li>defineObjectProperty 重写 set/get,  set - 监听变化， get - 依赖收集</li>
<li>data 每个属性， 都有一个 依赖收集器 dep - &#123; id: , subs: [watcher]&#125;</li>
<li>watcher 监听，更新视图</li>
</ol>
<h3 data-id="heading-7">Observer, Dep, Watcher 关系：</h3>
<pre><code class="copyable">Observer 提供数据监听能力
Dep  保存data依赖,
Watcher 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Observer : collect dependencies and dispatch updates.</li>
<li>Dep:</li>
<li>Watcher:</li>
</ul>
<pre><code class="copyable">export class Observer &#123;
  dep: Dep;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">/**
 * A watcher parses an expression, collects dependencies,
 * and fires callback when the expression value changes.
 * This is used for both the $watch() api and directives.
 */
export default class Watcher &#123;
  addDep() &#123;
    // 我这个Watcher要被Observer塞到Dep里去了~~
  &#125;,
  update() &#123;
    // Dep通知我更新呢~~
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">/**
 * A dep is an observable that can have multiple
 * directives subscribing to it.
 */
export default class Dep &#123;
  static target: ?Watcher;
  id: number;
  subs: Array<Watcher>;

  constructor () &#123;
    this.id = uid++
    this.subs = []
  &#125;

  addSub (sub: Watcher) &#123;
    this.subs.push(sub)
  &#125;

  removeSub (sub: Watcher) &#123;
    remove(this.subs, sub)
  &#125;

  depend () &#123;
    if (Dep.target) &#123;
      Dep.target.addDep(this)
    &#125;
  &#125;

  notify () &#123;
    // stabilize the subscriber list first
    const subs = this.subs.slice()
    for (let i = 0, l = subs.length; i < l; i++) &#123;
      subs[i].update()
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">virtual dom diff实现：</h1>
<h1 data-id="heading-9">Vue computed 属性：</h1>
<h1 data-id="heading-10">vue watch 属性 ：</h1></div>  
</div>
            