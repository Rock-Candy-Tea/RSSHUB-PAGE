
---
title: 'react中实现一个简单的拖拽排序react-dnd'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf2ab045886b4e98bb566993b72f06e7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 06:21:24 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf2ab045886b4e98bb566993b72f06e7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">React DnD 是什么？</h3>
<p>React DnD是React和Redux核心作者 Dan Abramov创造的一组React 高阶组件，可以在保持组件分离的前提下帮助构建复杂的拖放接口；</p>
<p>其中一些概念类似于Flux和Redux架构。</p>
<p>这并非巧合，因为 React DnD 在内部使用 Redux。</p>
<h3 data-id="heading-1">开始之前我们先来看一下效果；</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf2ab045886b4e98bb566993b72f06e7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>先上代码：</p>
<pre><code class="copyable">import React, &#123;    useState, useCallback, useRef, useEffect,  &#125; from 'react';  import &#123; DndProvider, useDrag, useDrop &#125; from 'react-dnd';  import &#123; HTML5Backend &#125; from 'react-dnd-html5-backend';  import update from 'immutability-helper';  import &#123; CloseOutlined, CloseCircleFilled &#125; from '@ant-design/icons';  import PropTypes from 'prop-types';  import './dragModule.scss';    const type = 'DragableBodyRow';    const DragableBodyRow = (&#123;    index, moveRow, className, style, label, value, onRemoveClick,  &#125;) => &#123;    const ref = useRef();    const [&#123; isOver, dropClassName &#125;, drop] = useDrop(      () => (&#123;        accept: type,        collect: (monitor) => &#123;          const &#123; index: dragIndex &#125; = monitor.getItem() || &#123;&#125;;          if (dragIndex === index) &#123;            return &#123;&#125;;          &#125;          return &#123;            isOver: monitor.isOver(),            dropClassName: dragIndex < index ? ' drop-over-downward' : ' drop-over-upward',          &#125;;        &#125;,        drop: (item) => &#123;          moveRow(item.index, index);        &#125;,      &#125;),      [index, moveRow],    );    const [, drag] = useDrag(      () => (&#123;        type,        item: &#123; index &#125;,        // canDrag: index > 1,        // 收集器函数        // collect: monitor => (&#123;        //   isDragging: monitor.isDragging(),        // &#125;),      &#125;),      [index],    );    drag(drop(ref));      return (      <div        ref=&#123;ref&#125;        className=&#123;`$&#123;className&#125;$&#123;isOver ? dropClassName : ''&#125;`&#125;        style=&#123;&#123; cursor: 'move', ...style &#125;&#125;      >        <span className="drag-list-item">          <span className="drag-list-item-content">&#123;label&#125;</span>          <CloseOutlined className="drag-list-item-remove" onClick=&#123;() => onRemoveClick(value)&#125; />        </span>      </div>    );  &#125;;  DragableBodyRow.propTypes = &#123;    index: PropTypes.number,    moveRow: PropTypes.func.isRequired,    className: PropTypes.string,    style: PropTypes.object,    label: PropTypes.string,    value: PropTypes.number,    onRemoveClick: PropTypes.func,  &#125;;    const DragModule = (&#123; value, onChange &#125;) => &#123;    const [dragData, setData] = useState([]);    useEffect(() => &#123;      let currentData = [];      if (dragData.length > value.length) &#123;        currentData = dragData.filter(a => value.find(b => a.value === b.value));      &#125; else &#123;        currentData = dragData.concat(value.filter(a => !(dragData.find(b => a.value === b.value))));      &#125;      setData(currentData);    // eslint-disable-next-line react-hooks/exhaustive-deps    &#125;, [value]);      const moveRow = useCallback(      (dragIndex, hoverIndex) => &#123;        const dragRow = dragData[dragIndex];        setData(          update(dragData, &#123;            $splice: [              [dragIndex, 1],              [hoverIndex, 0, dragRow],            ],          &#125;),        );      &#125;,      [dragData],    );      const onRemoveClick = (key) => &#123;      if (key) &#123;        const newData = value.filter(i => i.value !== key);        onChange(newData);      &#125; else &#123;        onChange([]);      &#125;    &#125;;      return (      <DndProvider backend=&#123;HTML5Backend&#125;>        <div className="tag-select-drag">          <div className="tag-select-drag-overflow">            &#123;              dragData.map((item, index) => (                <DragableBodyRow key=&#123;String(index)&#125; index=&#123;index&#125; moveRow=&#123;moveRow&#125; label=&#123;item.label&#125; value=&#123;item.value&#125; onRemoveClick=&#123;onRemoveClick&#125; className="drag-list-overflow" />              ))            &#125;          </div>          <CloseCircleFilled className="tag-select-drag-allclear" onClick=&#123;() => onRemoveClick()&#125; />        </div>      </DndProvider>    );  &#125;;    DragModule.propTypes = &#123;    value: PropTypes.oneOfType([PropTypes.object, PropTypes.array]),    onChange: PropTypes.func,  &#125;;  DragModule.defaultProps = &#123;    value: undefined,    onChange: () => &#123;&#125;,  &#125;;    export default DragModule;


const length = 10;const value = [];for (let i = 0; i < length; i++) &#123;  value.push(&#123;    value: i,    label: `这是第$&#123;i&#125;列`  &#125;)&#125;
<DragModule value=&#123;value&#125;/>
  
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">安装</h2>
<pre><code class="copyable">npm install react-dnd react-dnd-html5-backend
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">React DnD 的基本概念</h3>
<h3 data-id="heading-4">items & types</h3>
<p>与 Flux（或 Redux）一样，React DnD 使用数据而不是视图作为事实的来源。当您在屏幕上拖动某物时，我们并不是说正在拖动组件或 DOM 节点。</p>
<p>所以这里用一个“数据对象对象items”描述拖动的元素，例如&#123;id: 1&#125;</p>
<p>types类型是唯一标识应用程序中整个项目类别的字符串（或符号），类型很有用，因为随着您的应用程序的增长您可能希望使更多内容可拖动，但您不一定希望所有现有的放置目标突然开始对新项目做出反应。这些类型允许您指定兼容的拖放源和放置目标。您可能会在您的应用程序中枚举类型常量，类似于您可能如何枚举 Redux 操作类型。</p>
<h3 data-id="heading-5">Backend</h3>
<p>React DnD 使用HTML5 拖放 API。</p>
<p>这是一个合理的默认设置，因为它会截取拖动的 DOM 节点并将其用作开箱即用的“拖动预览”。当光标移动时，您不必进行任何绘图，这很方便。此 API 也是处理文件放置事件的唯一方法。</p>
<p>它所做的就是将 DOM 事件转换为 React DnD 可以处理的内部 Redux 操作</p>
<h3 data-id="heading-6">Monitors</h3>
<p>React DnD 通过 Monitor 来存储拖放状态并且提供查询；</p>
<h3 data-id="heading-7">Connectors</h3>
<p>Backend 关注 DOM 事件，组件关注拖放状态，connector 可以连接组件和 Backend ，可以让 Backend 获取到 DOM。</p>
<h3 data-id="heading-8">Hooks API</h3>
<p><strong>useDrag</strong></p>
<p>该useDrag钩子提供了一种将您的组件作为拖动源连接到 DnD 系统的方法。</p>
<pre><code class="copyable">import &#123; useDrag &#125; from 'react-dnd'

function DraggableComponent(props) &#123;
  const [collected, drag, dragPreview] = useDrag(() => (&#123;
    type, // 必须，唯一标识
    item: &#123; id &#125;, // 必须：描述被拖动数据的普通 JavaScript 对象
    collect: () => &#123;&#125;,// 可选， 返回的对象供组件使用 -> collectedProps
    canDrag: () => &#123;&#125;, // 元素是否可拖拽
    ...
  &#125;))
  return collected.isDragging ? (
    <div ref=&#123;dragPreview&#125; />
  ) : (
    <div ref=&#123;drag&#125; &#123;...collected&#125;>
      ...
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>collected: 包含从 collect 函数收集的属性的对象。如果没有collect定义函数，则返回一个空对象。</p>
<p>drag: 拖动源的连接器功能。这必须附加到 DOM 的可拖动部分。</p>
<p>dragPreview: 拖动预览的连接器功能。这可能会附加到 DOM 的预览部分。</p>
<p><strong>useDrop</strong></p>
<p>该useDrop钩子提供了一种将组件连接到 DnD 系统作为放置目标的方法。</p>
<pre><code class="copyable">import &#123; useDrop &#125; from 'react-dnd'

function myDropTarget(props) &#123;
  const [collectedProps, drop] = useDrop(() => (&#123;
    accept, // 必须，与useDrag中的type对应；
    collect: () => &#123;&#125;,// 可选， 返回的对象供组件使用 -> collectedProps
    drop: () => &#123;&#125;, // 可选的。在目标上放置兼容项目时调用。
    hover: () => &#123;&#125;, // 可选的。当项目悬停在组件上时调用。
    canDrop: () => &#123;&#125;, // 可选， 元素是否可放置
  &#125;))

  return <div ref=&#123;drop&#125;>Drop Target</div>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>collected: 包含从 collect 函数收集的属性的对象。如果没有collect定义函数，则返回一个空对象。</p>
<p>drop:放置目标的连接器功能。这必须附加到 DOM 的放置目标部分。</p>
<h1 data-id="heading-9">更好的更新复杂数据</h1>
<p>immutability-helper </p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fdocs%2Fupdate.html" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/docs/update.html" ref="nofollow noopener noreferrer">reactjs.org/docs/update…</a></p>
<p>参考：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTML%255C_Drag%255C_and%255C_Drop%255C_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTML%5C_Drag%5C_and%5C_Drop%5C_API" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freact-dnd%2Freact-dnd" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/react-dnd/react-dnd" ref="nofollow noopener noreferrer">github.com/react-dnd/r…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Freact-dnd.github.io%2Freact-dnd%2Fdocs%2Foverview" target="_blank" rel="nofollow noopener noreferrer" title="https://react-dnd.github.io/react-dnd/docs/overview" ref="nofollow noopener noreferrer">react-dnd.github.io/react-dnd/d…</a></p></div>  
</div>
            