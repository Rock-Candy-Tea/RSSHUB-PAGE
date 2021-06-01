
---
title: 'Saga、Core-FE、React、JavaScript、TypeScript学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9955'
author: 掘金
comments: false
date: Mon, 31 May 2021 22:18:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=9955'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">TypeScript</h4>
<ul>
<li>
<p>基本数据类型</p>
<blockquote>
<p>备注：项目中最好定义类型   any形式一般不用</p>
</blockquote>
</li>
<li>
<p>private、public、project  set()/get()的使用</p>
<blockquote>
<p>get()/set()  用于获取私有值</p>
</blockquote>
</li>
<li>
<p>泛型</p>
<blockquote>
<p>作用：可以指定传入的类型  方便使用</p>
</blockquote>
</li>
<li>
<p>interface</p>
<pre><code class="copyable">interface SquareConfig &#123;
    color?: string;
    width?: number;
    [propName: string]: any;    //后期可自定义 属性名；  自定义的属性名类型必须为 string 或 number；val值得类型随意
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>接口</p>
<blockquote>
<p>在接口的某个属性上加个 "?" ，表明不需要强制匹配该属性</p>
</blockquote>
<pre><code class="copyable">interface Person&#123;
  name: string;
  age?: number;
  [propName:string]:string | number;   //任意属性
  readonly id: number  //只读属性
&#125;

let name: string | number = '';   //联合类型。数据类型可以为：字符串 或 数字
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-1">类组件  --复杂的逻辑用这个</h4>
<ul>
<li>redux</li>
<li>dispatch</li>
</ul>
<h4 data-id="heading-2">函数组件/钩子函数  --简单的逻辑</h4>
<ul>
<li>
<p>hook</p>
<blockquote>
<p>useEffect()   是hook的事件监听   useState()  更新state</p>
</blockquote>
</li>
<li>
<p>useSelector   用于拿取 store 的数据</p>
</li>
</ul>
<h4 data-id="heading-3">Redux</h4>
<ul>
<li>
<p>使用 connect() 将 业务层和逻辑层 连接</p>
</li>
<li>
<p>dispatch（）   与actions使用  在视图层中与业务层的方法形成连接</p>
</li>
</ul>
<h4 data-id="heading-4">yield</h4>
<ul>
<li>
<p>yield是ES6的新关键字，使生成器函数执行暂停，yield关键字后面的表达式的值返回给生成器的调用者。它可以被认为是一个基于生成器的版本的return关键字。</p>
</li>
<li>
<p>yield关键字实际返回一个IteratorResult（迭代器）对象，它有两个属性，value和done，分别代表返回值和是否完成。</p>
</li>
<li>
<p>yield无法单独工作，需要配合generator(生成器)的其他函数，如next，懒汉式操作，展现强大的主动控制特性。</p>
</li>
</ul>
<h4 data-id="heading-5">Redux 学习比较【阮一峰】</h4>
<blockquote>
<p>store、state、action</p>
</blockquote>
<ul>
<li>
<p>store：保存数据的地方。</p>
</li>
<li>
<p>state：对象包含所有数据。一个state对应一个View；只要state相同，view就相同</p>
</li>
<li>
<p>action：就是view发出的通知，表示state要发生变化了。【state变化会导致view发生变化。state的变化必须是view导致的】</p>
<blockquote>
<p>Action 是一个对象。其中的<code>type</code>属性是必须的，表示 Action 的名称。其他属性可以自由设置，社区有一个<a href="https://github.com/acdlite/flux-standard-action" target="_blank" rel="nofollow noopener noreferrer">规范</a>可以参考</p>
</blockquote>
</li>
<li>
<p>store.dispatch()  是view发出action的唯一方法</p>
<blockquote>
<p>接收action对象作为参数</p>
</blockquote>
</li>
<li>
<p>reducer：store收到action以后，必须给出一个新的state，这样View才会发生变化。这种state的计算过程叫reducer</p>
<blockquote>
<p>reducer：是一个函数；接收：Action和当前的State作为参数；</p>
<p>reducer：是一个纯函数</p>
</blockquote>
</li>
<li>
<p>Store提供的3个方法</p>
<pre><code class="copyable">1、store.getState()
2、store.dispatch()
3、store.subscribe()
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-6">累计</h4>
<ul>
<li>
<p>react 字符串比较使用 “===” 【3个等号】，而不是“==” 【两个等号】</p>
</li>
<li>
<p>项目中，复杂 、共用的写在业务层中，用Redux存储数据；简单、View视图等状态直接在View层中写，无需使用Redux进行存储</p>
</li>
</ul>
<h4 data-id="heading-7">代码注意事项</h4>
<ul>
<li>
<p>文件、方法命名语义化，零注释【即通过文件名、方法名可找到对应功能模块】</p>
</li>
<li>
<p>常亮定义：使用 大写形式，例如下：</p>
<blockquote>
<p>export const LOAD_RELATED_OPTION = "LOAD_RELATED_OPTION";</p>
</blockquote>
</li>
<li>
<p>变量命名使用小写字母开头</p>
</li>
<li>
<p>没有数据变化，只设计到UI层的，不需要使用 Redux 的形式</p>
</li>
<li>
<p>Table组件，需要把 <code>rowKey</code>  字段加上(antd的Table 中的rowKey要写，并且要是唯一值，否则会出现奇奇怪怪的问题)</p>
</li>
<li>
<p><code>** </code>表示乘方【几次方】；<code>*</code> 表示乘</p>
</li>
<li>
<p>Core-FE的setState 的赋值，需要与SagaGenerator一起使用</p>
</li>
<li>
<p>建议多函数【即每个函数建议不超过10行】</p>
</li>
<li>
<p>按issue提交代码并且完成对应功能</p>
</li>
<li>
<p>注意事项：</p>
<pre><code class="copyable">对于 FC Component, 最好遵照这样的顺序来排列内容：
1. useState, useSelector
2. useEffect
3. 方法或变量声明（包括 useCallback/useMemo)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>useEffect的用法备注</p>
<pre><code class="copyable">useEffect(()=>&#123;&#125;,[])     //是生命周期，只有首次加载时，会执行一次

useEffect(()=>&#123;&#125;,[aa])   //事件监听，相当于 监听 aa 值改变
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h5 data-id="heading-8">JS累计</h5>
<ul>
<li>
<p>map</p>
<pre><code class="copyable">map() 需要return 将值返回
例：
item.map((item, index) => &#123;
return ...;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>foreach</p>
<blockquote>
<p>forEach() 被调用时，不会改变原数组，也就是调用它的数组（尽管 callback 函数在被调用时可能会改变原数组）。</p>
</blockquote>
<blockquote>
<p>（译注：此处说法可能不够明确，具体可参考EMCA语言规范：</p>
</blockquote>
<blockquote>
<p>forEach does not directly mutate the object on which it is called but the object may be mutated by the calls to callbackfn.</p>
</blockquote>
<blockquote>
<p>即 forEach 不会直接改变调用它的对象，但是那个对象可能会被 callback 函数改变。）</p>
</blockquote>
<pre><code class="copyable">例：
orginData.foreach((item, index) => &#123;
item.name = "111";
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>concat()</p>
<pre><code class="copyable">concat() 需要用一个变量去接收
例：
let concatData: string[] = [];
orginData.foreach((item, index) => &#123;
concatData = concatData.concat(["11", "22", "33"]);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>技术点：immer</p>
<blockquote>
<p><a href="https://github.com/mweststrate/immer" target="_blank" rel="nofollow noopener noreferrer">Immer</a> 是 mobx 的作者写的一个 immutable 库，核心实现是利用 ES6 的 proxy，几乎以最小的成本实现了 js 的不可变数据结构，简单易用、体量小巧、设计巧妙，满足了我们对JS不可变数据结构的需求。</p>
</blockquote>
<pre><code class="copyable">例：
import &#123;producer&#125; from "immer";
let currentState = &#123;
  p: &#123;
    x: [2],
  &#125;,
&#125;
let preducerData = producer(currentState, item => &#123;
item.p.x = 3;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>备注：</p>
<p>​使用前先yarn  add  immer</p>
</blockquote>
</li>
<li>
<p>不刷新页面的情况下，修改URL的值：</p>
<pre><code class="copyable">window.location.search = "";
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>useBinaryAction</p>
<pre><code class="copyable">const getItemNumberDetail = useBinaryAction(actions.getItemNumberDetail);

备注：2个参数

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>useLoadingStatus</p>
<pre><code class="copyable">const loading = useLoadingStatus(LOAD_ITEM_LIST);

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>useSelector</p>
<pre><code class="copyable">import &#123;useSelector&#125; from "react-redux";

const &#123;bomItems&#125; = useSelector((state: RootState) => state.app.commonStock);

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>useUnaryAction</p>
<pre><code class="copyable">const search = useUnaryAction(actions.search);

备注：1个参数

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>useAction</p>
<pre><code class="copyable">const loadAttribute = useAction(actions.loadAttribute);

备注： 无参数

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            