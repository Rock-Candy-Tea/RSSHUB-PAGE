
---
title: 'react + gojs'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: '...base64...'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 19:30:09 GMT
thumbnail: '...base64...'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgojs.net%2Flatest%2Fintro%2Freact.html" target="_blank" rel="nofollow noopener noreferrer" title="https://gojs.net/latest/intro/react.html" ref="nofollow noopener noreferrer">官方 GoJS with React</a> ，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fgojs-react" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/gojs-react" ref="nofollow noopener noreferrer">gojs-react</a></p>
<h6 data-id="heading-0">通过 <code>gojs-react</code> 简化，gojs在react项目中的使用，<code>gojs-react</code> 提供了 <code>ReactDiagram</code> ，<code>ReactPalette</code> ，<code>ReactOverview</code> 以供使用， <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FNorthwoodsSoftware%2Fgojs-react-basic" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/NorthwoodsSoftware/gojs-react-basic" ref="nofollow noopener noreferrer">gojs-react-basic</a> 提供了示例用法。</h6>
<ol start="0">
<li>
<h5 data-id="heading-1">安装 <code>npm install gojs gojs-react</code></h5>
</li>
<li>
<h5 data-id="heading-2">设置画布样式，需要指定宽度/高度。</h5>
<pre><code class="copyable">/* App.css */
.diagram-component &#123;
  width: 400px;
  height: 400px;
  border: solid 1px black;
  background-color: white;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h5 data-id="heading-3">基础应用</h5>
<pre><code class="copyable">// App.js
import React from 'react';
import * as go from 'gojs';
import &#123; ReactDiagram &#125; from 'gojs-react';
import './App.css';  // 引入对应样式
​
/**
 * 初始化图表方法，该方法用于制作图表初始化模型模版;模型的数据不由此设置，ReactDiagram组件通过其他props处理
 */
function initDiagram() &#123;
  const $ = go.GraphObject.make;
  const diagram =
    $(go.Diagram,
      &#123;
        'undoManager.isEnabled': true,  // 撤销管理器，应始终启用 UndoManager 以允许发生事务，但可以将 UndoManager.maxHistoryLength 设置为 0 以防止撤消和重做
        // 'undoManager.maxHistoryLength': 0,  // 取消注释禁用撤消/重做功能
        'clickCreatingTool.archetypeNodeData': &#123; text: 'new node', color: 'lightblue' &#125;,
        model: $(go.GraphLinksModel,
          &#123;
            linkKeyProperty: 'key'  // 使用 GraphLinksModel 时应始终设置此项
          &#125;)
      &#125;);
​
  diagram.nodeTemplate =
    $(go.Node, 'Auto',
      new go.Binding('location', 'loc', go.Point.parse).makeTwoWay(go.Point.stringify),
      $(go.Shape, 'RoundedRectangle',
        &#123; name: 'SHAPE', fill: 'white', strokeWidth: 0 &#125;,
        // 图形填充颜色和数据对象的color绑定
        new go.Binding('fill', 'color')),
      $(go.TextBlock,
        &#123; margin: 8, editable: true &#125;, 
        new go.Binding('text').makeTwoWay()
      )
    );
​
  return diagram;
&#125;
​
function handleModelChange(changes) &#123;
  alert('GoJS model changed!');
&#125;
​
// linkDataArray 链接关系数组，只有在使用 GraphLinksModel 时才需要，而Models或 TreeModels 则不需要
function App() &#123;
  return (
    <div>
      ...
      <ReactDiagram
        initDiagram=&#123;initDiagram&#125;
        divClassName='diagram-component'
        nodeDataArray=&#123;[
          &#123; key: 0, text: 'Alpha', color: 'lightblue', loc: '0 0' &#125;,
          &#123; key: 1, text: 'Beta', color: 'orange', loc: '150 0' &#125;,
          &#123; key: 2, text: 'Gamma', color: 'lightgreen', loc: '0 150' &#125;,
          &#123; key: 3, text: 'Delta', color: 'pink', loc: '150 150' &#125;
        ]&#125;
        linkDataArray=&#123;[
          &#123; key: -1, from: 0, to: 1 &#125;,
          &#123; key: -2, from: 0, to: 2 &#125;,
          &#123; key: -3, from: 1, to: 1 &#125;,
          &#123; key: -4, from: 2, to: 3 &#125;,
          &#123; key: -5, from: 3, to: 0 &#125;
        ]&#125;
        onModelChange=&#123;handleModelChange&#125;
      />
      ...
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>画鱼骨图参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2FWondser%2Farticle%2Fdetails%2F117447737" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/Wondser/article/details/117447737" ref="nofollow noopener noreferrer">vue+gojs 绘制鱼骨图</a> 实现，需要引入对应<code>FishboneLayout.js</code></p>
</blockquote>
</li>
<li>
<h5 data-id="heading-4">获取图片</h5>
<blockquote>
<ul>
<li><code>makeImage</code> 返回<code><img src='...base64...' ></code></li>
</ul>

<ul>
<li>
<p><code>makeImageData</code> 返回 base64 字符串（如果显示为黑色，不显示线条，尝试将 <code>background: 'white'</code>）</p>
<p>此方法使用 HTMLCanvasElement 的 toDataURL 方法创建数据 URL，或 Canvas Context 的 getImageData 方法。 与 toDataURL 不同的是，如果在画布上绘制了跨域图像，此方法不会抛出错误，而是会返回忽略这些图像的位图的数据 URL</p>
</li>
</ul>
</blockquote>
<h6 data-id="heading-5">按照如上官方提供的基础案例和获取图片方法，会下意识的认为要写在 <code>initDiagram</code> 对应的方法里，但实际上写在这获取数据为null，应该是因为在这一步并没有生成Dom元素。</h6>
<h6 data-id="heading-6">用 <code>useRef</code> 设置变量，在 <code>initDiagram</code> 对应的方法里将 <code>diagram</code> 赋值 给对应变量，然后在 <code>onModelChange</code> 对应方法中用获取图片的方法获取到对应值。</h6>
<pre><code class="copyable">//如上个案例的重复部分就不赘述，用省略替代，结合前面理解
import React, &#123; useRef &#125; from 'react';
// ...省略其他import引入...
const Diagram = (&#123;&#125;) => &#123;
    const diagramRef = useRef(null);
    const initDiagram = () => &#123;
        const $ = go.GraphObject.make;
        const diagram = $(go.Diagram, &#123;
            isReadOnly: true
        &#125;);
        ...
    diagramRef.current = diagram;
    return diagram;
  &#125;;
  const handleModelChange = (changes) => &#123;
      diagramRef.current.makeImageData(&#123; 
          background: 'white', 
          type:'image/jpeg' 
      &#125;);
  &#125;;
    // ...省略其他设置方法...
    return (
        <ReactDiagram
          initDiagram=&#123;initDiagram&#125;
          onModelChange=&#123;handleModelChange&#125;
          // ...省略其他设置...
        />
  );
&#125;
export default Diagram;
```react + gojs

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgojs.net%2Flatest%2Fintro%2Freact.html" target="_blank" rel="nofollow noopener noreferrer" title="https://gojs.net/latest/intro/react.html" ref="nofollow noopener noreferrer">官方 GoJS with React</a> ，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fgojs-react" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/gojs-react" ref="nofollow noopener noreferrer">gojs-react</a></p>
<h6 data-id="heading-7">通过 <code>gojs-react</code> 简化，gojs在react项目中的使用，<code>gojs-react</code> 提供了 <code>ReactDiagram</code> ，<code>ReactPalette</code> ，<code>ReactOverview</code> 以供使用， <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FNorthwoodsSoftware%2Fgojs-react-basic" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/NorthwoodsSoftware/gojs-react-basic" ref="nofollow noopener noreferrer">gojs-react-basic</a> 提供了示例用法。</h6>
<ol start="0">
<li>
<h5 data-id="heading-8">安装 <code>npm install gojs gojs-react</code></h5>
</li>
<li>
<h5 data-id="heading-9">设置画布样式，需要指定宽度/高度。</h5>
<pre><code class="copyable">/* App.css */
.diagram-component &#123;
  width: 400px;
  height: 400px;
  border: solid 1px black;
  background-color: white;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h5 data-id="heading-10">基础应用</h5>
<pre><code class="copyable">// App.js
import React from 'react';
import * as go from 'gojs';
import &#123; ReactDiagram &#125; from 'gojs-react';
import './App.css';  // 引入对应样式
​
/**
 * 初始化图表方法，该方法用于制作图表初始化模型模版;模型的数据不由此设置，ReactDiagram组件通过其他props处理
 */
function initDiagram() &#123;
  const $ = go.GraphObject.make;
  const diagram =
    $(go.Diagram,
      &#123;
        'undoManager.isEnabled': true,  // 撤销管理器，应始终启用 UndoManager 以允许发生事务，但可以将 UndoManager.maxHistoryLength 设置为 0 以防止撤消和重做
        // 'undoManager.maxHistoryLength': 0,  // 取消注释禁用撤消/重做功能
        'clickCreatingTool.archetypeNodeData': &#123; text: 'new node', color: 'lightblue' &#125;,
        model: $(go.GraphLinksModel,
          &#123;
            linkKeyProperty: 'key'  // 使用 GraphLinksModel 时应始终设置此项
          &#125;)
      &#125;);
​
  diagram.nodeTemplate =
    $(go.Node, 'Auto',
      new go.Binding('location', 'loc', go.Point.parse).makeTwoWay(go.Point.stringify),
      $(go.Shape, 'RoundedRectangle',
        &#123; name: 'SHAPE', fill: 'white', strokeWidth: 0 &#125;,
        // 图形填充颜色和数据对象的color绑定
        new go.Binding('fill', 'color')),
      $(go.TextBlock,
        &#123; margin: 8, editable: true &#125;, 
        new go.Binding('text').makeTwoWay()
      )
    );
​
  return diagram;
&#125;
​
function handleModelChange(changes) &#123;
  alert('GoJS model changed!');
&#125;
​
// linkDataArray 链接关系数组，只有在使用 GraphLinksModel 时才需要，而Models或 TreeModels 则不需要
function App() &#123;
  return (
    <div>
      ...
      <ReactDiagram
        initDiagram=&#123;initDiagram&#125;
        divClassName='diagram-component'
        nodeDataArray=&#123;[
          &#123; key: 0, text: 'Alpha', color: 'lightblue', loc: '0 0' &#125;,
          &#123; key: 1, text: 'Beta', color: 'orange', loc: '150 0' &#125;,
          &#123; key: 2, text: 'Gamma', color: 'lightgreen', loc: '0 150' &#125;,
          &#123; key: 3, text: 'Delta', color: 'pink', loc: '150 150' &#125;
        ]&#125;
        linkDataArray=&#123;[
          &#123; key: -1, from: 0, to: 1 &#125;,
          &#123; key: -2, from: 0, to: 2 &#125;,
          &#123; key: -3, from: 1, to: 1 &#125;,
          &#123; key: -4, from: 2, to: 3 &#125;,
          &#123; key: -5, from: 3, to: 0 &#125;
        ]&#125;
        onModelChange=&#123;handleModelChange&#125;
      />
      ...
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>画鱼骨图参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2FWondser%2Farticle%2Fdetails%2F117447737" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/Wondser/article/details/117447737" ref="nofollow noopener noreferrer">vue+gojs 绘制鱼骨图</a> 实现，需要引入对应<code>FishboneLayout.js</code></p>
</blockquote>
</li>
<li>
<h5 data-id="heading-11">获取图片</h5>
<blockquote>
<ul>
<li><code>makeImage</code> 返回<code><img src='...base64...' ></code></li>
</ul>

<ul>
<li>
<p><code>makeImageData</code> 返回 base64 字符串（如果显示为黑色，不显示线条，尝试将 <code>background: 'white'</code>）</p>
<p>此方法使用 HTMLCanvasElement 的 toDataURL 方法创建数据 URL，或 Canvas Context 的 getImageData 方法。 与 toDataURL 不同的是，如果在画布上绘制了跨域图像，此方法不会抛出错误，而是会返回忽略这些图像的位图的数据 URL</p>
</li>
</ul>
</blockquote>
<h6 data-id="heading-12">按照如上官方提供的基础案例和获取图片方法，会下意识的认为要写在 <code>initDiagram</code> 对应的方法里，但实际上写在这获取数据为null，应该是因为在这一步并没有生成Dom元素。</h6>
<h6 data-id="heading-13">用 <code>useRef</code> 设置变量，在 <code>initDiagram</code> 对应的方法里将 <code>diagram</code> 赋值 给对应变量，然后在 <code>onModelChange</code> 对应方法中用获取图片的方法获取到对应值。</h6>
<pre><code class="copyable">//如上个案例的重复部分就不赘述，用省略替代，结合前面理解
import React, &#123; useRef &#125; from 'react';
// ...省略其他import引入...
const Diagram = (&#123;&#125;) => &#123;
    const diagramRef = useRef(null);
    const initDiagram = () => &#123;
        const $ = go.GraphObject.make;
        const diagram = $(go.Diagram, &#123;
            isReadOnly: true
        &#125;);
        ...
    diagramRef.current = diagram;
    return diagram;
  &#125;;
  const handleModelChange = (changes) => &#123;
      diagramRef.current.makeImageData(&#123; 
          background: 'white', 
          type:'image/jpeg' 
      &#125;);
  &#125;;
    // ...省略其他设置方法...
    return (
        <ReactDiagram
          initDiagram=&#123;initDiagram&#125;
          onModelChange=&#123;handleModelChange&#125;
          // ...省略其他设置...
        />
  );
&#125;
export default Diagram;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol></div>  
</div>
            