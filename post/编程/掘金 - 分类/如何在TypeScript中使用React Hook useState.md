
---
title: '如何在TypeScript中使用React Hook useState'
categories: 
    - 编程
    - 掘金 - 分类
author: 掘金 - 分类
comments: false
date: Sun, 21 Mar 2021 21:01:01 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>前言：</strong></p>
<p>TypeScript给JavaScript和ReactJS生态系统带来了巨大的变化。它提高了开发效率，TypeScript的项目往往更加可靠，以及在开发过程中更容易排查bug。这篇文章总结了一些我在学习TypeScript中，如何使用useState，并声明state类型。</p>
<h1 data-id="heading-0">useState源码</h1>
<p>首先，让我们来看看React源码中的useState是如何声明的。</p>
<pre><code class="copyable">// ...
/**
 * Returns a stateful value, and a function to update it.
 *
 * @version 16.8.0
 * @see https://reactjs.org/docs/hooks-reference.html#usestate
 */
function useState<S>(initialState: S | (() => S)): [S, Dispatch<SetStateAction<S>>];
// convenience overload when first argument is ommitted
/**
 * Returns a stateful value, and a function to update it.
 *
 * @version 16.8.0
 * @see https://reactjs.org/docs/hooks-reference.html#usestate
 */
function useState<S = undefined>(): [S | undefined, Dispatch<SetStateAction<S | undefined>>];
// ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在React源码中，useState有两个函数。第二个函数重写（override）了第一个函数，使我们可以在调用useState时不直接声明state变量类型。</p>
<p>值得注意的是，第一个方法接一个名为S的TypeScript泛型，通过它，我们可以定义state的变量类型。</p>
<h1 data-id="heading-1">useState基础用法</h1>
<p>以下是在TypeScript中使用useState的基本例子。</p>
<pre><code class="copyable">import React, &#123;useState&#125; from 'react'

export default function App() &#123;
  const [name, setName] = useState<string>('未定义变量')
  const [age, setAge] = useState<number>(28)
  const [isProgrammer, setIsProgrammer] = useState<boolean>(true)

  return (
    <div>
      <ul>
        <li>Name: &#123;name&#125;</li>
        <li>Age: &#123;age&#125;</li>
        <li>Programmer: &#123;isProgrammer ? 'Yes' : 'No'&#125;</li>
      </ul>
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你在set函数中的参数不符合声明的变量类型，程序会报错。</p>
<pre><code class="copyable">import React, &#123;useEffect, useState&#125; from 'react'

export default function App() &#123;
  const [name, setName] = useState<string>('未定义变量')
  const [age, setAge] = useState<number>(28)
  const [isProgrammer, setIsProgrammer] = useState<boolean>(true)

  useEffect(() => &#123;
    // Error: Argument of type '28' is not assignable to parameter of type 'SetStateAction<string>'.ts(2345)
    setName(28)
    // Error: Argument of type 'true' is not assignable to parameter of type 'SetStateAction<number>'.ts(2345)
    setAge(true)
    // Error: Argument of type '"Gabriel Rufino"' is not assignable to parameter of type 'SetStateAction<boolean>'.
    setIsProgrammer('未定义变量')
  &#125;, [])

  return (
    <div>
      <ul>
        <li>Name: &#123;name&#125;</li>
        <li>Age: &#123;age&#125;</li>
        <li>Programmer: &#123;isProgrammer ? 'Yes' : 'No'&#125;</li>
      </ul>
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是对于JavaScript原始类型，我们其实不需要声明变量类型，因为TypeScript可以自己判断相应的变量类型。</p>
<pre><code class="copyable">import React, &#123;useEffect, useState&#125; from 'react'

export default function App() &#123;
  const [name, setName] = useState('未定义变量')
  const [age, setAge] = useState(28)
  const [isProgrammer, setIsProgrammer] = useState(true)

  return (
    <div>
      <ul>
        <li>Name: &#123;name&#125;</li>
        <li>Age: &#123;age&#125;</li>
        <li>Programmer: &#123;isProgrammer ? 'Yes' : 'No'&#125;</li>
      </ul>
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">useState进阶用法</h1>
<p>当我们需要使用useState处理复杂数据时（如数组或者对象），我们需要借用TypeScript中接口（interface）这个概念。</p>
<p>假设我们需要在useState中声明如下数据。</p>
<pre><code class="copyable">[
  &#123;
    "id": 1,
    "name": "蔡文姬",
    "type": "辅助"
  &#125;,
  &#123;
    "id": 1,
    "name": "后裔",
    "type": "射手"
  &#125;,
  &#123;
    "id": 1,
    "name": "鲁班7号",
    "type": "射手"
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们需要首先定义一个代表这组数据类型的接口（interface）。</p>
<pre><code class="copyable">interface IChampion &#123;
  id: number;
  name: string;
  type: string;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们在使用useState中，声明我们的state为Champion类型变量。</p>
<pre><code class="copyable">import React, &#123;useState&#125; from 'react'

interface IChampion &#123;
  id: number;
  name: string;
  type: string;
&#125;

export default function Champions() &#123;
  const [champions, setChampions] = useState<IChampion[]>([
    &#123;
      id: 1,
      name: '蔡文姬',
      type: '辅助'
    &#125;,
    &#123;
      id: 1,
      name: '后裔',
      type: '射手'
    &#125;,
    &#123;
      id: 1,
      name: '鲁班7号',
      type: '射手'
    &#125;
  ])

  return (
    <div>
      <ul>
        &#123;champions.map(champion=> (
          <li key=&#123;champion.id&#125;>&#123;champion.name&#125; - &#123;champion.type&#125;</li>
        ))&#125;
      </ul>
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但通常，我们会从API中异步获取数据，而非在useState中直接声明变量。</p>
<pre><code class="copyable">import React, &#123;useState, useEffect&#125; from 'react'
import axios from 'axios'

interface IChampion &#123;
  id: number;
  name: string;
  type: string;
&#125;

export default function Champions() &#123;
  const [champions, setChampions] = useState<IChampion[]>([])

  useEffect(() => &#123;
    axios.get<IUser[]>('https://api.yourservice.com/champions')
      .then((&#123; data &#125;) => &#123;
        setChampions(data)
      &#125;)
  &#125;, [])

  return (
    <div>
      <ul>
        &#123;champions.map((champion: IChampion) => (
          <li key=&#123;champion.id&#125;>&#123;champion.name&#125; - &#123;champion.type&#125;</li>
        ))&#125;
      </ul>
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是在React TypeScript，useState的一些用法。</p>
<hr>
<p><em><strong>--阅读更多文章，请关注我的公众号：未定义变量</strong></em></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            