
---
title: 'React 中的useReducer是个什么东西'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3644'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 04:53:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=3644'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">写在前面</h3>
<p>如果你想深入学习React，借助它解决自己遇到的各种业务场景，那么你就需要了解useReducer。</p>
<p>结合我自己的学习心得和使用经验，写下这篇博客跟大家分享useReducer最简单的知识点。</p>
<h3 data-id="heading-1">什么是useReducer</h3>
<p>useReducer是React推出的一个扩展Hook，如下代码所示，它接受 (state, action) ⇒ newSatte的一个reduce，并返回当前的state以及与其配套的dispatch方法，让开发人员能够更好的管理代码中的数据，如果你熟悉Redux，那么你对useReducer的工作原理就非常清楚了。</p>
<pre><code class="copyable">const [state, dispatch] = useReducer(reducer, initialState)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里简单介绍以上面的几个变量：</p>
<ol>
<li>initialState：需要我们自己定义，是我们要管理的一个初始变量。可以是一个数字，字符串，数组，对象等。</li>
<li>reducer：是我们自己定义的一个纯函数，它的作用就是通过定义好的逻辑来改变initialState初始变量，为我们的项目服务。</li>
<li>state：reduce里面的逻辑处理数据之后，会返回一个最新的值，就是这个state</li>
<li>dispatch：触发器，reducer中会定义很多条件，具体要使用哪一个条件来改变initialState变量呢，就是要通过触发器来控制。</li>
</ol>
<p>总结起来一句话：我们使用dispatch来触发reducer纯函数，用reducer纯函数中的逻辑修改initialState，得到一个新的变量，把这个变量赋值给state，最终返回。</p>
<p>从这一点看，useReducer和useState非常相似，如下代码所示，我们是这样使用useState的：</p>
<pre><code class="copyable">const [userName, setUserName] = useState("Allen")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>useState接受一个初始值"Allen"，返回一个最新值userName和修改这个最新值的方法setUserName。从这里可以看出，useState是对useReducer的封装，useReducer是一种更原生的Hook，你能在使用useState的地方都替换成使用useReducer。后面我们会给出useReducer的几种使用场景。</p>
<h3 data-id="heading-2">为什么要使用useReducer</h3>
<p>如果你是一个刚刚接触React Hooks的程序员，你可能更加倾向于使用useState而不是useReducer，因为useState太好用了，组件中需要管理几个变量，就是用几个useState定义多少变量和方法就可以了，这没有什么问题。但是很多有丰富经验的程序员更加推荐你使用useReducer，理由如下：</p>
<h4 data-id="heading-3">1. 在需要管理大量数据的场景中，使用useReducer更加合适</h4>
<p>在一些业务场景下使用useReducer更加合适，比如：一个组件中要收集用户很多方面的信息，例如身高体重性别等基本信息，学历专业特长等学校信息，公司职位工龄等单位信息等等。</p>
<p>如果你要为这些信息都一一创建变量来保存，那就太繁琐了。即使你使用一个或几个对象来存储，也还是不够清晰，这个时候使用useReducer就显得很方便，这一点我们在后面的实例中会给出，</p>
<h4 data-id="heading-4">2. 使用useReducer更加利于其他程序员理解</h4>
<p>大多数程序员对Redux比较熟悉，习惯于使用dispatch触发action，然后获取最新的state。这种情况下，</p>
<p>他来阅读useReducer会跟加得心应手。但是如果让他们去学习和掌握useState，显然主要花费一些时间。</p>
<h3 data-id="heading-5">如何使用useReduce管理组件中的状态</h3>
<p>下面给出一个简单的例子，来跟大家介绍如何使用Reducer管理组件中的状态。</p>
<p>这是一个计数器，可以自增，自减和重置，如果你有兴趣，可以直接到codesandbox中查看这个例子：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Freact-usereducer-demo-ztekg" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/react-usereducer-demo-ztekg" ref="nofollow noopener noreferrer"></a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Freact-usereducer-demo-ztekg" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/react-usereducer-demo-ztekg" ref="nofollow noopener noreferrer">codesandbox.io/s/react-use…</a></p>
<h4 data-id="heading-6">1. 首先我们需要定义一个初始的变量</h4>
<p>一般情况下这个变量是一个对象，这里的变量只有一个属性amount，表示当前的数量：</p>
<pre><code class="copyable">const initState = &#123;
    amount: 0
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2. 然后我们需要定义reducer</h4>
<p>reducer就是一个纯函数。这个纯函数接受两个参数，最终返回一个最新的状态值。</p>
<p>这两个参数分别是initstate和action。initstate是要管理的状态值的初始状态，action是一种命令，他告诉reducer要如何管理state状态值。</p>
<p>返回的变量，我们称作是最新的状态值。这里定义的reducer代码如下：</p>
<pre><code class="copyable">const reducer = (state, action) => &#123;
  switch (action.type) &#123;
    case "add":
      return &#123;
        amount: state.amount + 1
      &#125;;
    case "minus":
      return &#123;
        amount: state.amount - 1
      &#125;;
    case "reset":
      return &#123;
        amount: 0
      &#125;;
    default:
      return &#123;
        amount: 0
      &#125;;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">4. 使用useReducer来定义state和触发reducer的方法</h4>
<p>代码如下：</p>
<pre><code class="copyable">const [state, dispatch] = useReducer(reducer, initState);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">5. 使用dispatch触发action，修改状态</h4>
<p>在实际使用的时候，我们需要用dispatch触发一个action，reducer根据action的种类进行操作，代码如下：</p>
<pre><code class="copyable"><button onClick=&#123;() => &#123; dispatch(&#123; type: "add" &#125;); &#125;&#125; >Add</button>

<button onClick=&#123;() => &#123; dispatch(&#123; type: "minus" &#125;);&#125;&#125;>minus</button>

<button onClick=&#123;() => &#123; dispatch(&#123; type: "reset" &#125;);&#125;&#125;>reset</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">结合具体的使用示例，介绍如何使用useReducer，</h3>
<p>之前看到一篇文章，对useReducer的使用场景做了很详细的描述，这里直接给出列出，有兴趣的小伙伴可以自行阅读：</p>
<p>在 React Hooks 中使用 useReducer 的几种用例：<a href="https://juejin.cn/post/6844903817981460493" target="_blank" title="https://juejin.cn/post/6844903817981460493"></a><a href="https://juejin.cn/post/6844903817981460493" target="_blank" title="https://juejin.cn/post/6844903817981460493">juejin.cn/post/684490…</a></p>
<h3 data-id="heading-11">写在最后</h3>
<p>以上就是自己的总结，有错误之处，还希望大家予以纠正。</p></div>  
</div>
            