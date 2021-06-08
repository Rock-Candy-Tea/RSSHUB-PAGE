
---
title: '记录一些Vuex笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7011'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 05:33:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=7011'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Vuex笔记</h2>
<h3 data-id="heading-1">vuex是什么</h3>
<pre><code class="copyable">github站点: https://github.com/vuejs/vuex
在线文档: https://vuex.vuejs.org/zh-cn/
简单来说: 对应用中组件的状态进行集中式的管理(读/写)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">状态自管理应用</h3>
<pre><code class="copyable">state: 驱动应用的数据源
view: 以声明方式将state映射到视图
actions: 响应在view上的用户输入导致的状态变化(包含n个更新状态的方法)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">多组件共享状态的问题</h3>
<pre><code class="copyable">多个视图依赖于同一状态
来自不同视图的行为需要变更同一状态
以前的解决办法
* 将数据以及操作数据的行为都定义在父组件
* 将数据以及操作数据的行为传递给需要的各个子组件(有可能需要多级传递)
vuex就是用来解决这个问题的
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">vuex的核心概念</h3>
<h4 data-id="heading-5">1). state</h4>
<pre><code class="copyable">vuex管理的状态对象
它应该是唯一的
const state = &#123;
xxx: initValue
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">2). mutations</h4>
<pre><code class="copyable">包含多个直接更新state的方法(回调函数)的对象
谁来触发: action中的commit('mutation名称')
只能包含同步的代码, 不能写异步代码
const mutations = &#123;
yyy (state, data) &#123; 
// 更新state的某个属性
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">3). actions</h4>
<pre><code class="copyable">包含多个事件回调函数的对象
通过执行: commit()来触发mutation的调用, 间接更新state
谁来触发: 组件中: $store.dispatch('action名称')  // 'zzz'
可以包含异步代码(定时器, ajax)
const actions = &#123;
zzz (&#123;commit, state&#125;, data1) &#123;
commit('yyy', data2)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">4). getters</h4>
<pre><code class="copyable">包含多个计算属性(get)的对象
谁来读取: 组件中: $store.getters.xxx
const getters = &#123;
mmm (state) &#123;
return ...
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">5). modules</h4>
<pre><code class="copyable">包含多个module
一个module是一个store的配置对象
与一个组件(包含有共享数据)对应
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">6). 向外暴露store对象</h4>
<pre><code class="copyable">export default new Vuex.Store(&#123;
state,
mutations,
actions,
getters
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">7). 组件中:</h4>
<pre><code class="copyable">import &#123;mapGetters, mapActions&#125; from 'vuex'
export default &#123;
computed: mapGetters(['mmm'])
methods: mapActions(['zzz'])
&#125;

&#123;&#123;mmm&#125;&#125; @click="zzz(data)"
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">8). 映射store</h4>
<pre><code class="copyable">import store from './store'
new Vue(&#123;
store
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">9). store对象</h4>
<pre><code class="copyable">1.所有用vuex管理的组件中都多了一个属性$store, 它就是一个store对象
2.属性:
  state: 注册的state对象
  getters: 注册的getters对象
3.方法:
  dispatch(actionName, data): 分发action 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">将vuex引到项目中</h3>
<h4 data-id="heading-15">1). 下载: npm install vuex --save</h4>
<h4 data-id="heading-16">2). 使用vuex</h4>
<pre><code class="copyable">1.store.js
import Vuex from 'vuex'
export default new Vuex.Store(&#123;
state,
mutations,
actions,
getters,
modules
&#125;)
2.main.js
import store from './store.js'
new Vue(&#123;
store
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            