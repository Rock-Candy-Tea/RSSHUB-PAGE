
---
title: 'React 学习之渲染过程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5550'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 01:03:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=5550'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">渲染原理</h2>
<p>术语描述：</p>
<p><strong>渲染：</strong> 生成用于显示的对象，以及将这些对象形成真实的 DOM 对象</p>
<ol>
<li>
<p><code>React 元素 (React Element)</code>：通过 <code>React.createElement</code> 创建 (语法糖：<code>JSX</code> 表达式创建)；如： <code><div>React Element</div></code>、<code><App /></code></p>
</li>
<li>
<p><code>React 节点 (React Component)</code>：专门用于渲染到 UI 界面的对象 (<code>Virtual DOM</code>)，React 会通过 <code>React 元素</code> 创建 React 节点，<code>ReactDOM</code> 一定是根据 React 节点来渲染页面的</p>
<p>节点类型：</p>
<ul>
<li><code>React DOM 节点 (Virtual DOM Node)</code>：创建该节点的 React 与元素类型是一个 <code>字符串</code> (<code>"div"</code>, <code>"h1'</code>等)</li>
<li><code>React 组件节点 (React ComponentNode)</code>：创建该节点的 React 与元素类型是一个 <code>函数</code> 或一个 <code>类</code> (<code>比如我们封装的函数组件或类组件等</code>)</li>
<li><code>React 文本节点 (React TextNode)</code>：由字符串、数字创建</li>
<li><code>React 空节点 (React EmptyNode)</code>：<code>null</code>, <code>undefined</code>, <code>false</code>, <code>true</code></li>
<li><code>React 数组节点 (React ArrayNode)</code>：由数组创建</li>
</ul>
</li>
</ol>
<h2 data-id="heading-1">首次渲染 (新节点挂载阶段)</h2>
<ol>
<li>
<p>通过参数的值创建节点 <code>ReactDOM.render(参数, MONT_NODE)</code></p>
</li>
<li>
<p>根据不同的节点，做不同的事情</p>
<ul>
<li>①<code>文本节点</code>：通过 <code>document.createTextNode()</code> 创建真实的文本节点</li>
<li>②<code>空节点</code>：不创建真实 DOM</li>
<li>③<code>数组节点</code>：遍历数组，对每一项递归进行创建节点 (回第 ① 步，直到遍历结束)</li>
<li>④<code>DOM 节点</code>：JSX 解析生成的对象 (React 元素)，通过 <code>document.createElement()</code> 创建真实 DOM 对象，然后遍历对应 React 元素的 children 属性(对象或数组)，递归操作 (回第1步，直到遍历结束)</li>
<li>⑤<code>组件节点</code>：<code>函数组件</code>：调用函数 (该函数必须返回可以生成节点的内容)，将该函数的返回结果递归生成节点 (同上)；<code>类组件</code>：创建该类的实例，立即调用对象的生命周期方法 <code>static getDerivedStateFromProps</code>，运行该对象的 <code>render</code> 方法，得到节点对象，递归操作；将该组件的 <code>componentDidMount</code> 加入到执行队列 (先进先执行)，当整个虚拟 DOM 树全部构建完毕，并且将真实的 DOM 对象加入到容器中后，遍历该队列执行</li>
</ul>
</li>
<li>
<p>生成虚拟 DOM 树后，将该树保存起来，以便后续使用 (diff)</p>
</li>
<li>
<p>将之前生成的真实 DOM 对象，加入到页面的容器中</p>
</li>
</ol>
<h2 data-id="heading-2">更新节点</h2>
<p>节点更新时机：</p>
<ol>
<li>
<p>重新调用 <code>ReactDOM.render()</code> 方法，完全重新生成节点树 (虚拟 DOM 树)，触发根节点的更新</p>
</li>
<li>
<p>在类组件中调用 <code>this.setState()</code> 更新状态，会导致该实例所在的节点更新</p>
</li>
<li>
<p>hook 涉及的更新后续再说~</p>
</li>
</ol>
<h3 data-id="heading-3">对比更新</h3>
<ol>
<li>
<p>如果调用 <code>ReactDOM.render()</code> 方法，<strong>对比更新根节点(<code>diff</code>)</strong></p>
</li>
<li>
<p>如果调用 <code>this.setState()</code> 方法</p>
<ul>
<li>运行生命周期函数 <code>static getDerivedStateFromProps</code></li>
<li>运行生命周期函数 <code>shouldComponentUpdate</code>，若 <code>返回 false，终止当前流程</code></li>
<li>运行 render，得到一个新的节点，进入该新节点的 <strong>对比更新</strong></li>
<li>将生命周期函数 <code>getSnapshotBeforeUpdate</code> 加入执行队列，等待执行</li>
<li>将生命周期函数 <code>componentDidUpdate</code> 加入执行队列 (与上面这步不是同一个队列)，等待执行</li>
</ul>
</li>
</ol>
<p>对比更新的后续步骤：</p>
<ul>
<li>更新虚拟 DOM 树</li>
<li>完成真实 DOM 的更新</li>
<li>依次调用执行队列中的 <code>compoentDidMount</code> (产生的新组件挂载)</li>
<li>依次调用执行队列中的 <code>getSnapshotBeforeUpdate</code></li>
<li>依次调用执行队列中的 <code>componentDidUpdate</code></li>
<li>依次调用执行队列中的 <code>componentWillUnmount</code> (被移除的子节点才会推入队列)</li>
</ul>
<p>对比更新：将新产生的节点，与之前虚拟 DOM 中的节点进行对比，发现差异，进行更新</p>
<h4 data-id="heading-4">对比假设</h4>
<p>React 为了提高对比效率，做出以下假设：</p>
<ol>
<li>
<p>React 节点的位置不会进行层级的移动 (对比时，直接找到旧树中对应位置的节点进行对比)</p>
</li>
<li>
<p>不同的节点类型会生成不同的结构</p>
<ul>
<li>相同的节点类型：节点本身类型相同 (如文本类型，DOM节点)；如果是组件节点，组件类型也得相同 (类 / 函数)；若是由 React 元素生成，type 值必须是一致的</li>
</ul>
</li>
<li>
<p>多个兄弟节点通过唯一标识 (key) 来确定对比的新节点</p>
<ul>
<li>key 值用于通过旧节点来寻找应该对比的新节点，如果某个旧节点有 key 值，则其更新时，会寻找相同层级中具有相同 key 值的节点 (若未找到，则进入未找到对比节点的流程)</li>
</ul>
</li>
</ol>
<h4 data-id="heading-5">找到对比节点</h4>
<p><strong>判断节点类型是否一致</strong></p>
<ol>
<li>
<p><strong>一致</strong>：根据不同的节点做不同的事：</p>
<ul>
<li>① <code>空节点</code>：不做任何事；</li>
<li>② <code>DOM 节点</code>：重用之前生成的真实 DOM 对象，将其属性的变化进行记录 (此时不会更新 DOM)，遍历该新的 React 元素的子元素，递归对比更新；</li>
<li>③ <code>文本节点</code>：直接重用之前的真实 DOM 对象，记录变化的 <code>nodeValue</code> 值；</li>
<li>④ <code>函数组件节点</code>：重新调用函数，得到一个节点对象，进入递归对比更新；</li>
<li>⑤ <code>类组件节点</code>：重用之前的实例，依次调用 <code>static getDerivedStateFromProps</code>, <code>shouldComponentUpdate</code> (若返回false，终止对比)，否则运行 <code>render</code>，进入递归对比更新，将该对象的 <code>getSnapshotBeforeUpdate</code>, <code>componentDidUpdate</code> 加入相应的队列，等待执行；</li>
<li>⑥ <code>数组节点</code>：遍历数组，进行递归对比更新</li>
</ul>
</li>
<li>
<p><strong>不一致</strong>：整体上，卸载旧的节点，重新创建新的节点 (<code>先创建新节点，后卸载旧节点</code>)。旧节点：</p>
<ul>
<li>① <code>空节点</code>, <code>文本节点</code>, <code>DOM 节点</code>, <code>数组节点</code>, <code>函数组件节点</code>：直接舍弃旧节点，创建新节点 (进入 <code>新节点挂载阶段</code>)；</li>
<li>② <code>类组件节点</code>：直接舍弃旧节点，调用该节点的 <code>componentWillUnmount</code> 函数，递归卸载子节点</li>
</ul>
</li>
</ol>
<h4 data-id="heading-6">未找到对比目标</h4>
<p>新的虚拟 DOM 树中有 <code>新的节点删除或添加</code>，即：创建新加入的节点，卸载多余的节点 (还是上面挂载跟卸载的流程)</p></div>  
</div>
            