
---
title: 'vue&react组件通信'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=169'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 17:30:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=169'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、父子组件通信</h3>
<h4 data-id="heading-1"><strong>VUE父子组件通信</strong></h4>
<h5 data-id="heading-2">1.props / emit</h5>
<p>父->子：通过props进行传递数据给子组件
子->父：通过emit向父组件传值</p>
<h5 data-id="heading-3">2.children/parent</h5>
<p>通过parent/children就可以访问组件的实例，拿到实例代表什么？代表可以访问此组件的所有方法和data</p>
<h4 data-id="heading-4"><strong>react父子组件通信</strong></h4>
<h5 data-id="heading-5">1.props / emit</h5>
<p>父->子：通过props进行传递数据给子组件
子->父：通过调用父组件传过来的函数并传入参数</p>
<h4 data-id="heading-6"><strong>总结父子组件通信</strong></h4>
<p>父传子 方式基本相同 形式不同，都是通过props
子传父 方式基本相同形式不同，都是通过绑定事件
Vue 多一些实例上面的方法 可以在父组件调用子组件实例，在子组件调用父组件实例
其实 React 的 子传父 在Vue里面也是可以用的</p>
<h3 data-id="heading-7">二、隔代组件通信</h3>
<h4 data-id="heading-8"><strong>vue隔代组件通信</strong></h4>
<h5 data-id="heading-9">1.普通传递</h5>
<h6 data-id="heading-10">爷传孙</h6>
<p>爷组件通过正常的props向下传递 子组件使用 $attrs接受(子组件没                                               接收的数据会继续向下传递)，最后在孙组件通过props接受</p>
<h6 data-id="heading-11">孙传爷</h6>
<p>孙组件通过 this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi><mi>m</mi><mi>i</mi><mi>t</mi><mo stretchy="false">(</mo><mo stretchy="false">)</mo><mtext>将事件向上传递在子组件使用</mtext></mrow><annotation encoding="application/x-tex">emit() 将事件向上传递 在子组件 使用</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">e</span><span class="mord mathnormal">m</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span><span class="mopen">(</span><span class="mclose">)</span><span class="mord cjk_fallback">将</span><span class="mord cjk_fallback">事</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">向</span><span class="mord cjk_fallback">上</span><span class="mord cjk_fallback">传</span><span class="mord cjk_fallback">递</span><span class="mord cjk_fallback">在</span><span class="mord cjk_fallback">子</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">使</span><span class="mord cjk_fallback">用</span></span></span></span></span>listeners 接受事件(子组                                 件没接收的数据会继续向上传递)，爷组件通过调用自定义事件 接受参数</p>
<h6 data-id="heading-12">孙传爷补充</h6>
<p>既然爷传孙已经实现了，那么这时候可以传递一个函数 通过调用这个函数传入参数传递数据</p>
<h5 data-id="heading-13">2.provide/inject</h5>
<p>通过父组件定义provide将组件实例向下传递，在后代的所有组件里面 都能通过inject 调用该实例的方法
属性</p>
<h4 data-id="heading-14"><strong>React隔代组件通信</strong></h4>
<p>Context  生产者-消费者模式</p>
<h5 data-id="heading-15">1.引用React 里面的一个方法createContext执行并将返回值 并且暴露出去</h5>
<pre><code class="copyable">import React from 'react';
export const MyContext=React.createContext()
父组件里面引用该方法返回值里面的一个属性
import &#123;MyContext&#125;  context'
const &#123;Provider&#125;=MyContext
<Provider  value=&#123;&#123;car1,car2,car3,changeCar1:this.changeCar1&#125;&#125;>
<Child car1=&#123;car1&#125; changeCar=&#123;this.changeCar&#125;></Child>
</Provider>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">2.在子组件里面使用</h5>
<pre><code class="copyable">import &#123;MyContext&#125; from '../../context'
在组件内部定义一个静态方法  注意 contextType 不能变
static contextType = MyContext
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候就能够通过在组件内部调用 this.context 使用 父组件传过来的方法
第二种调用方法 就不需要定义静态方法</p>
<pre><code class="copyable"><MyContext.Consumer>
    &#123;value => (value.smallCar)&#125; // value就是context中的value数据
/MyContext.Consumer>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">三、状态集中式管理</h3>
<h4 data-id="heading-18"><strong>VueX</strong></h4>
<p>Vuex是vue配套的公共数据管理工具，我们可以将共享的数据保存到Vuex中</p>
<h5 data-id="heading-19">1.方便整个程序中任意组件都可以获取并且修改vuex中保存的数据</h5>
<p>如果您不打算开发大型单页应用，使用 Vuex 可能是繁琐冗余的。确实是如此——如果您的应用够简单，您最好不要使用 Vuex。一个简单的 store 模式 (opens new window)就足够您所需了。但是，如果您需要构建一个中大型单页应用，您很可能会考虑如何更好地在组件外部管理状态，Vuex 将会成为自然而然的选择</p>
<h5 data-id="heading-20">2.VueX包含以下几个部分</h5>
<ul>
<li>
<pre><code class="copyable">state，驱动应用的数据源；
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="copyable">mutations  更改 Vuex 的 store 中的状态的唯一方法
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="copyable">actions  响应在 view 上的用户输入导致的状态变化。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="copyable">getters  从store 中的 state 中派生出一些状态
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="copyable">modules  将 store 分割成模块
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h5 data-id="heading-21">3.如何配置定义vuex</h5>
<pre><code class="copyable">import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
export default new Vuex.Store(&#123;
  state: &#123;状态数据&#125;,
  mutations: &#123;改变数据的方法&#125;,
  actions: &#123;复杂的修改方法&#125;,
  getters:&#123;数据重新加工输出&#125;，
  modules: &#123;多个store统一加载&#125;，
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-22">4.如何使用vuex里面的状态</h5>
<p>组件里面可以通过 this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>s</mi><mi>t</mi><mi>o</mi><mi>r</mi><mi>e</mi><mi mathvariant="normal">.</mi><mi>s</mi><mi>t</mi><mi>a</mi><mi>t</mi><mi>e</mi><mtext>与</mtext><mi>t</mi><mi>h</mi><mi>i</mi><mi>s</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">store.state 与this.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">s</span><span class="mord mathnormal">t</span><span class="mord mathnormal">o</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord">.</span><span class="mord mathnormal">s</span><span class="mord mathnormal">t</span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord cjk_fallback">与</span><span class="mord mathnormal">t</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord">.</span></span></span></span></span>store.getters 调用state 与getters,也可以通过 Vuex  里面提供的方法 mapState mapMutations</p>
<pre><code class="copyable">mapState([key])  mapMutations([eventName])
mutations 的方法可以通过 this.$store.commit(eventName,parms)
actions 的方法可以通过  this.$store.dispatch(eventName,parms)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23"><strong>redux</strong></h4>
<p>redux是一个专用与状态管理的js库，可以用于vue，react，angular
redux不是专门用于react 的库，而是一个通用的库，他与react没任何关系，知识react 用它用的比较多，Redux 是一个专门用来做状态管理的js库 类似与 Vuex<br>
基本上就是配合 React 使用
将 需要被多方使用到的状态 交到Redux里面 需要的时候 直接取出来 共享使用</p>
<h5 data-id="heading-24">1.redux 的使用</h5>
<p>创建 stroe.js 文件 只需要一个</p>
<pre><code class="copyable"> import &#123;createStore&#125; from 'redux'  
//引入createStore 用于创建 store
     import countReduce from './count_reduce' 
//创建需要传入 参数 countReduce
    export default createStore(countReduce) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>//创建并且传入参数  并且暴露出去
创建reduce.js文件---count_reduce.js</p>
<pre><code class="copyable">export default function (state='自行车',action)&#123;
const &#123;type,data&#125;=action
switch(type)&#123;case 'change':
return data
default:
return state&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前面已经定义好了redux 那么如何使用呢？</p>
<p>可以通过  store.getState()  获取状态</p>
<p>改变值 store.dispatch(&#123;type:'add',data:value&#125;)  第一个传过去的状态  第二个 去进行计算的值</p>
<p>渲染页面   因为虽然通过上面方法改变了redux的值 但是页面并没有重新渲染</p>
<pre><code class="copyable">componentDidMount()&#123;  //页面挂载  就开始监听 store
    store.subscribe(()=>&#123;
        console.log('store任意状态改变的时候调用该方法')
        this.setState(&#123;&#125;)  //调用setState 使页面重新渲染  有效率问题
&#125;) &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">四、Vue事件总线（EventBus）</h3>
<h4 data-id="heading-26">** vue -eventBus**</h4>
<p>EventBus 又称为事件总线。在Vue中可以使用 EventBus 来作为沟通桥梁的概念，就像是所有组件共用相同的事件中心，可以向该中心注册发送事件或接收事件，所以组件都可以上下平行地通知其他组件，但也就是太方便所以若使用不慎，就会造成难以维护的“灾难”，因此才需要更完善的Vuex作为状态管理中心，将通知的概念上升到共享状态层次
如何使用</p>
<h5 data-id="heading-27">1.在入口文件 main.js里面 定义一个 bus</h5>
<pre><code class="copyable">Vue.prototype.$bus=new Vue()
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-28">2.数据传递</h5>
<pre><code class="copyable">this.$bus.$emit(eventName,params)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-29">3.数据接受</h5>
<p>在mounted 里面 绑定事件</p>
<pre><code class="copyable">this.$bus.$on(eventName,(val)=>&#123;this.msg=val&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-30">4.其他方法</h5>
<p>你也可以使用 this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>b</mi><mi>u</mi><mi>s</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">bus.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">b</span><span class="mord mathnormal">u</span><span class="mord mathnormal">s</span><span class="mord">.</span></span></span></span></span>off('aMsg') 来移除应用内所有对此某个事件的监听。或者直接调用
this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>b</mi><mi>u</mi><mi>s</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">bus.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">b</span><span class="mord mathnormal">u</span><span class="mord mathnormal">s</span><span class="mord">.</span></span></span></span></span>off() 来移除所有事件频道，不需要添加任何参数 。</p>
<h3 data-id="heading-31">五、消息订阅与发布</h3>
<p>消息订阅与发布其实有很多组件库    pub-sub  event 等等
它其实是一个js库 所以在vue react angular里面都可以使用，
但是基本不会在vue里面使用</p>
<h3 data-id="heading-32">最后总结</h3>
<p>都是我自己总结出来的 React 用的不多 了解的不深  有什么遗漏或者错误 希望各位指正···</p></div>  
</div>
            