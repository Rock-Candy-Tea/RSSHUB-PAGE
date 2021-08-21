
---
title: 'React学习知识点之组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=38'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 02:23:07 GMT
thumbnail: 'https://picsum.photos/400/300?random=38'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第16天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<h2 data-id="heading-0">组件</h2>
<h3 data-id="heading-1">是否受控</h3>
<ul>
<li>
<p>非受控组件</p>
<p>表单数据交由DOM节点管理，特点是表单数据在需要时要进行获取，不能实时获取，代码实现比较简单</p>
</li>
<li>
<p>受控组件</p>
<p>表单数据交由state对象管理，特点是可以实时得到表单时数据，代码相对复杂</p>
</li>
</ul>
<h3 data-id="heading-2">React Hook</h3>
<blockquote>
<p>作用：对函数组件进行增强，让函数组件可以存储状态，拥有处理副作用的能力</p>
</blockquote>
<h4 data-id="heading-3">路由Hooks react-router-dom</h4>
<ul>
<li>
<p>useHistory</p>
</li>
<li>
<p>useLocation</p>
</li>
<li>
<p>useRouteMatch</p>
</li>
<li>
<p>useParams</p>
</li>
</ul>
<h4 data-id="heading-4">钩子函数</h4>
<h5 data-id="heading-5">useState</h5>
<ul>
<li>
<p>通过闭包实现保存数据（一般函数执行完成后变量就会被释放掉）</p>
</li>
<li>
<p>状态每次更新时DOM都会重新渲染</p>
</li>
</ul>
<h5 data-id="heading-6">useEffect</h5>
<ul>
<li>
<p>替换componentDidmount、componentDidUpdate、componentWillUnmount生命周期</p>
</li>
<li>
<p>useEffect(()=>&#123;&#125;) 等于 componentDidmount、componentDidUpdate。会在组件挂载结束后执行、会在组件更新完成后执行</p>
</li>
<li>
<p>useEffect(()=>&#123;&#125;,[]) 等于 componentDidmount</p>
</li>
<li>
<p>useEffect(()=>()=>&#123;&#125;) 等于 componentWillUnmount。会在组件卸载前执行</p>
</li>
<li>
<p>只有指定数据发生变化后才会触发Effect：useEffect(()=>&#123;console.log(count)&#125;,[count])</p>
</li>
<li>
<p>useEffect中的参数函数不能是异步函数，因为useEffect函数要返回清理资源的函数，如果是异步函数就变成了返回Promise，可以在内部使用自执行函数</p>
</li>
</ul>
<p>标记: useEffect(()=>&#123;  (async ()=>&#123; await axios.get() &#125;  )()   &#125;)</p>
<h5 data-id="heading-7">useMemo</h5>
<blockquote>
<p>类似于Vue中的计算属性，可以检测某个值的变化，根据变化值计算新值</p>
</blockquote>
<p>会缓存计算结果，如果检测值没有发生变化，即使组件重新渲染，也不会重新计算，计算行为可以有助于避免在每个渲染上执行昂贵的计算</p>
<p>主要用于性能优化，如果本组件中的数据没有发生变化，则阻止组件更新，类似于类组件中的PureComponent和shouldComponentUpdate</p>
<h5 data-id="heading-8">useCallback</h5>
<p>主要用于性能优化，缓存函数，使组件重新渲染时得到相同的函数实例</p>
<h5 data-id="heading-9">useRef</h5>
<ul>
<li>
<p>用来获取DOM元素对象</p>
</li>
<li>
<p>用来保存数据，当组件重新渲染后数据不会丢失</p>
</li>
</ul>
<h5 data-id="heading-10">自定义Hook</h5>
<ul>
<li>
<p>可以实现组件与组件之间的逻辑共享</p>
</li>
<li>
<p>是一个函数，以use开头</p>
</li>
<li>
<p>是逻辑与内置Hook的组合</p>
</li>
</ul>
<h4 data-id="heading-11">生命周期</h4>
<h5 data-id="heading-12">挂载阶段</h5>
<ul>
<li>
<p>constructor（）</p>
</li>
<li>
<p>static getDerivedStateFromProps（）</p>
</li>
<li>
<p>render（）</p>
</li>
<li>
<p>componentDidMount（）</p>
</li>
</ul>
<h5 data-id="heading-13">更新阶段</h5>
<ul>
<li>
<p>static getDerivedStateFromProps（）</p>
</li>
<li>
<p>shouldComponentUpdate（）</p>
</li>
<li>
<p>render（）</p>
</li>
<li>
<p>getSnapshotBeforeUpdate（）：在最近一次渲染输出之前调用，使组件能在发生更改之前从DOM中捕获一些信息，如：滚动位置，此声生命周期的任何返回值将作为参数传递给componentDidUpdate（）</p>
</li>
<li>
<p>componentDidUpdate（）</p>
</li>
</ul>
<h5 data-id="heading-14">卸载阶段</h5>
<ul>
<li>componentWillUnmount（）</li>
</ul></div>  
</div>
            