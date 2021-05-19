
---
title: '快速！简单！便捷！得！使用UITableView和UICollectionView'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=6494'
author: 掘金
comments: false
date: Sun, 25 Apr 2021 00:27:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=6494'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>对于实现一个列表视图，使用苹果官方的方式真是恶心的不行，要实现多个代理，还要复写多个名字一样，参数名还很长的函数，真真的是写不下去的。。。</p>
<p>然后，依据android的adapter，弄了个swift版的Adapter类，方便的实现这一切，先看使用方法</p>
<h1 data-id="heading-0">简单使用</h1>
<p>实现一个简单的UICollectionView列表视图：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyModel</span></span>&#123;
    <span class="hljs-comment">//数据model</span>
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewCell</span>: <span class="hljs-title">UICollectionViewCell</span> </span>&#123;
    <span class="hljs-comment">//创建Cell布局</span>
&#125;
<span class="hljs-comment">//创建一个 adapter 类，传入泛型 model 和 cell</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyAdapter</span>: <span class="hljs-title">BaseQuickAdapter</span><<span class="hljs-title">MyModel</span>,<span class="hljs-title">MyViewCell</span>> </span>&#123;
    <span class="hljs-comment">//cell大小</span>
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">cellSize</span>(<span class="hljs-params">data</span>:<span class="hljs-type">MyModel</span>, <span class="hljs-params">indexPath</span>:<span class="hljs-type">IndexPath</span>)</span> -><span class="hljs-type">CGSize</span>&#123;
        <span class="hljs-type">CGSize</span>(width:<span class="hljs-type">ScreenWidth</span>, height:<span class="hljs-type">PT_100</span>)
    &#125;
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">bindView</span>(<span class="hljs-params">data</span>:<span class="hljs-type">MyModel</span>, <span class="hljs-params">indexPath</span>:<span class="hljs-type">IndexPath</span>, <span class="hljs-params">cell</span>:<span class="hljs-type">MyViewCell</span>)</span> &#123;
        <span class="hljs-comment">//将model的数据显示到cell上面</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后绑定：</p>
<pre><code class="hljs language-swift copyable" lang="swift">        <span class="hljs-keyword">let</span> mCollectionView <span class="hljs-operator">=</span> <span class="hljs-type">UICollectionView</span>(frame: .zero ,collectionViewLayout: <span class="hljs-type">UICollectionViewFlowLayout</span>())
        <span class="hljs-keyword">let</span> mAdapter <span class="hljs-operator">=</span> <span class="hljs-type">MyAdapter</span>()
        <span class="hljs-comment">//绑定collectionView 和 adapter</span>
        mCollectionView.setAdapter(mAdapter)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完事收工！！！</p>
<h1 data-id="heading-1">进阶使用</h1>
<pre><code class="hljs language-swift copyable" lang="swift">        mAdapter.setOnItemSelected &#123; (indexPath, model) <span class="hljs-keyword">in</span>
            <span class="hljs-comment">//处理点击事件</span>
        &#125;
        mAdapter.setOnItemLongPress &#123; (indexPath, model) <span class="hljs-keyword">in</span>
            <span class="hljs-comment">//处理长按事件</span>
            
            <span class="hljs-comment">//移除数据</span>
            mAdapter.removeItem(indexPath)
        &#125;
        <span class="hljs-comment">//设置数据</span>
        <span class="hljs-keyword">let</span> data <span class="hljs-operator">=</span> [<span class="hljs-type">MyModel</span>(),<span class="hljs-type">MyModel</span>(),<span class="hljs-type">MyModel</span>()]
        mAdapter.setNewData(data)
        <span class="hljs-comment">//添加数据</span>
        mAdapter.appendData(<span class="hljs-type">MyModel</span>())
        <span class="hljs-comment">//获取adapter的数据</span>
        <span class="hljs-keyword">let</span> dataArray <span class="hljs-operator">=</span> mAdapter.getData()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">使用多个cell布局</h2>
<p>同样非常的简单</p>
<pre><code class="hljs language-swift copyable" lang="swift">
<span class="hljs-comment">//数据model 实现 CellType 协议，根据cellType属性区分要使用的cell类型，cellType即注册cell时使用的标识</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyModel</span>:<span class="hljs-title">CellType</span></span>&#123;
    <span class="hljs-keyword">static</span> <span class="hljs-keyword">let</span> <span class="hljs-type">TYPE_1</span> <span class="hljs-operator">=</span> <span class="hljs-string">"1"</span>
    <span class="hljs-keyword">static</span> <span class="hljs-keyword">let</span> <span class="hljs-type">TYPE_2</span> <span class="hljs-operator">=</span> <span class="hljs-string">"2"</span>
    
    <span class="hljs-comment">//根据不同的布局设置不同的type</span>
    <span class="hljs-keyword">var</span> cellType: <span class="hljs-type">String</span> <span class="hljs-operator">=</span> <span class="hljs-type">TYPE_1</span>
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewCell</span>: <span class="hljs-title">UICollectionViewCell</span> </span>&#123;
    <span class="hljs-comment">//创建Cell布局</span>
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewCell2</span>: <span class="hljs-title">UICollectionViewCell</span> </span>&#123;
    <span class="hljs-comment">//创建Cell布局</span>
&#125;
<span class="hljs-comment">//创建一个 adapter 类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyAdapter</span>: <span class="hljs-title">BaseAdapter</span><<span class="hljs-title">MyModel</span>> </span>&#123;
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">init</span>()</span> &#123;
        <span class="hljs-keyword">super</span>.<span class="hljs-keyword">init</span>()
        <span class="hljs-comment">//注册cell</span>
        registerCell(<span class="hljs-type">MyViewCell</span>.<span class="hljs-keyword">self</span>, <span class="hljs-type">MyModel</span>.<span class="hljs-type">TYPE_1</span>)
        registerCell(<span class="hljs-type">MyViewCell2</span>.<span class="hljs-keyword">self</span>, <span class="hljs-type">MyModel</span>.<span class="hljs-type">TYPE_2</span>)
    &#125;
    <span class="hljs-comment">//cell大小</span>
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">cellSize</span>(<span class="hljs-params">data</span>: <span class="hljs-type">MyModel</span>, <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>)</span> -> <span class="hljs-type">CGSize</span> &#123;
        <span class="hljs-comment">//根据data.cellType 设置不同的size</span>
        <span class="hljs-keyword">if</span> data.cellType <span class="hljs-operator">==</span> <span class="hljs-type">MyModel</span>.<span class="hljs-type">TYPE_1</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-type">CGSize</span>(width: <span class="hljs-type">ScreenWidth</span>, height: <span class="hljs-type">PT_100</span>)
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> data.cellType <span class="hljs-operator">==</span> <span class="hljs-type">MyModel</span>.<span class="hljs-type">TYPE_2</span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-type">CGSize</span>(width: <span class="hljs-type">ScreenWidth</span>, height: <span class="hljs-type">PT_200</span>)
        &#125;
        <span class="hljs-keyword">return</span> .zero
    &#125;
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">bindView</span>(<span class="hljs-params">data</span>: <span class="hljs-type">MyModel</span>, <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>, <span class="hljs-params">collectionCell</span>: <span class="hljs-type">UICollectionViewCell</span>)</span> &#123;
        <span class="hljs-comment">//将model的数据显示到cell上面</span>
        
        <span class="hljs-comment">//根据data.cellType 转换成不同的 cell</span>
        <span class="hljs-keyword">if</span> data.cellType <span class="hljs-operator">==</span> <span class="hljs-type">MyModel</span>.<span class="hljs-type">TYPE_1</span> &#123;
            <span class="hljs-keyword">let</span> cell <span class="hljs-operator">=</span> collectionCell <span class="hljs-keyword">as!</span> <span class="hljs-type">MyViewCell</span>
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> data.cellType <span class="hljs-operator">==</span> <span class="hljs-type">MyModel</span>.<span class="hljs-type">TYPE_2</span>&#123;
            <span class="hljs-keyword">let</span> cell <span class="hljs-operator">=</span> collectionCell <span class="hljs-keyword">as!</span> <span class="hljs-type">MyViewCell2</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前就弄了这点功能，如果有使用到其他功能，后期再加。
初学者，代码比较简陋随意O(∩_∩)O，欢迎指正！</p>
<h1 data-id="heading-3">BaseAdapter源码：</h1>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">//</span>
<span class="hljs-comment">//  BaseAdapter.swift</span>
<span class="hljs-comment">//  bookista</span>
<span class="hljs-comment">//</span>
<span class="hljs-comment">//  Created by DU on 2021/4/25.</span>
<span class="hljs-comment">//</span>

<span class="hljs-keyword">import</span> Foundation

<span class="hljs-keyword">let</span> <span class="hljs-type">DefaultCellId</span> <span class="hljs-operator">=</span> <span class="hljs-string">"BaseCell"</span> <span class="hljs-comment">//默认的cellId</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BaseAdapter</span><<span class="hljs-title">T</span>> :<span class="hljs-title">NSObject</span>,<span class="hljs-title">UICollectionViewDataSource</span>,<span class="hljs-title">UICollectionViewDelegate</span>,<span class="hljs-title">UICollectionViewDelegateFlowLayout</span>, <span class="hljs-title">UITableViewDelegate</span>,<span class="hljs-title">UITableViewDataSource</span></span>&#123;
    
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> mData <span class="hljs-operator">=</span> [<span class="hljs-type">T</span>]()<span class="hljs-comment">//数据列表</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> mCell <span class="hljs-operator">=</span> [<span class="hljs-type">String</span>:<span class="hljs-type">AnyClass</span>?]() <span class="hljs-comment">//需要注册的cell</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> onItemSelected:((<span class="hljs-type">IndexPath</span>,<span class="hljs-type">T</span>)-><span class="hljs-type">Void</span>)<span class="hljs-operator">?</span> <span class="hljs-comment">//点击事件</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> onItemLongPress:((<span class="hljs-type">IndexPath</span>,<span class="hljs-type">T</span>)-> <span class="hljs-type">Void</span>)<span class="hljs-operator">?</span> <span class="hljs-comment">//长按事件</span>
    
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> mCollectionView:<span class="hljs-type">UICollectionView</span>?
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> mTableView:<span class="hljs-type">UITableView</span>?
    
    <span class="hljs-comment">/**
     绑定 UICollectionView
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">bindTo</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">collectionView</span>: <span class="hljs-type">UICollectionView</span>)</span>&#123;
        <span class="hljs-keyword">if</span> mTableView <span class="hljs-operator">!=</span> <span class="hljs-literal">nil</span> <span class="hljs-operator">||</span> mCollectionView <span class="hljs-operator">!=</span> <span class="hljs-literal">nil</span> &#123;
            <span class="hljs-built_in">fatalError</span>(<span class="hljs-string">"已经绑定过 UITableView 或 UICollectionView"</span>)
        &#125;
        mCollectionView <span class="hljs-operator">=</span> collectionView
        mCollectionView<span class="hljs-operator">?</span>.delegate <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>
        mCollectionView<span class="hljs-operator">?</span>.dataSource <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>
        mCell.forEach &#123; (cell) <span class="hljs-keyword">in</span>
            mCollectionView<span class="hljs-operator">?</span>.register(cell.value, forCellWithReuseIdentifier: cell.key)
        &#125;
    &#125;
    <span class="hljs-comment">/**
     绑定 UITableView
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">bindTo</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">tableView</span>: <span class="hljs-type">UITableView</span>)</span>&#123;
        <span class="hljs-keyword">if</span> mTableView <span class="hljs-operator">!=</span> <span class="hljs-literal">nil</span> <span class="hljs-operator">||</span> mCollectionView <span class="hljs-operator">!=</span> <span class="hljs-literal">nil</span>&#123;
            <span class="hljs-built_in">fatalError</span>(<span class="hljs-string">"已经绑定过 UITableView 或 UICollectionView"</span>)
        &#125;
        mTableView <span class="hljs-operator">=</span> tableView
        mTableView<span class="hljs-operator">?</span>.delegate <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>
        mTableView<span class="hljs-operator">?</span>.dataSource <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>
        mCell.forEach &#123; (cell) <span class="hljs-keyword">in</span>
            mTableView<span class="hljs-operator">?</span>.register(cell.value, forCellReuseIdentifier: cell.key)
        &#125;
    &#125;
    
    <span class="hljs-comment">/**
     获取数据
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">getData</span>()</span> -> [<span class="hljs-type">T</span>]&#123;
        <span class="hljs-keyword">return</span> mData
    &#125;
    <span class="hljs-comment">/**
     设置新的数据
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">setNewData</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">data</span>:[<span class="hljs-type">T</span>])</span>&#123;
        mData.removeAll()
        mData.append(contentsOf: data)
        mCollectionView<span class="hljs-operator">?</span>.reloadData()
        mTableView<span class="hljs-operator">?</span>.reloadData()
    &#125;
    <span class="hljs-comment">/**
     添加数据
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">appendData</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">data</span>:<span class="hljs-type">T</span>)</span>&#123;
        mData.append(data)
        mCollectionView<span class="hljs-operator">?</span>.reloadData()
        mTableView<span class="hljs-operator">?</span>.reloadData()
    &#125;
    
    <span class="hljs-comment">/**
     注册cell - 用于不用样式的cell注册
     reuseIdentifier = model.cellType
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">registerCell</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">cell</span>:<span class="hljs-type">AnyClass</span>?,<span class="hljs-keyword">_</span> <span class="hljs-params">reuseIdentifier</span>: <span class="hljs-type">String</span>)</span>&#123;
        mCell.updateValue(cell, forKey: reuseIdentifier)
    &#125;
    <span class="hljs-comment">/**
     注册cell - 只有一种样式
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">registerCell</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">cell</span>:<span class="hljs-type">AnyClass</span>?)</span>&#123;
        <span class="hljs-keyword">self</span>.registerCell(cell, <span class="hljs-type">DefaultCellId</span>)
    &#125;
    
    <span class="hljs-comment">/**
     item 点击
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">setOnItemSelected</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">onItemSelected</span>:((<span class="hljs-type">IndexPath</span>,<span class="hljs-type">T</span>)-><span class="hljs-type">Void</span>)<span class="hljs-operator">?</span>)</span>&#123;
        <span class="hljs-keyword">self</span>.onItemSelected <span class="hljs-operator">=</span> onItemSelected
    &#125;
    
    <span class="hljs-comment">/**
     设置长按点击事件
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">setOnItemLongPress</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">todo</span>: ((<span class="hljs-type">IndexPath</span>,<span class="hljs-type">T</span>)-> <span class="hljs-type">Void</span>)<span class="hljs-operator">?</span>)</span>&#123;
        <span class="hljs-keyword">self</span>.onItemLongPress <span class="hljs-operator">=</span> todo
        <span class="hljs-keyword">let</span> recognizer <span class="hljs-operator">=</span> <span class="hljs-type">UILongPressGestureRecognizer</span>(target: <span class="hljs-keyword">self</span>, action: #selector(longPressGesture(<span class="hljs-keyword">_</span>:)))
        <span class="hljs-keyword">self</span>.mCollectionView<span class="hljs-operator">?</span>.addGestureRecognizer(recognizer)
        <span class="hljs-keyword">self</span>.mTableView<span class="hljs-operator">?</span>.addGestureRecognizer(recognizer)
    &#125;
    
    <span class="hljs-comment">//长按动作</span>
    <span class="hljs-keyword">@objc</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">longPressGesture</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">tap</span>: <span class="hljs-type">UILongPressGestureRecognizer</span>)</span> &#123;
        <span class="hljs-keyword">if</span> tap.state <span class="hljs-operator">==</span> .began &#123;
            <span class="hljs-keyword">if</span> mTableView <span class="hljs-operator">!=</span> <span class="hljs-literal">nil</span> &#123;
                <span class="hljs-keyword">guard</span> <span class="hljs-keyword">let</span> path <span class="hljs-operator">=</span> mTableView<span class="hljs-operator">!</span>.indexPathForRow(at: tap.location(in: mTableView<span class="hljs-operator">!</span>)) <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-keyword">return</span>
                &#125;
                <span class="hljs-keyword">self</span>.onItemLongPress<span class="hljs-operator">?</span>(path,mData[path.row])
            &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> mCollectionView <span class="hljs-operator">!=</span> <span class="hljs-literal">nil</span> &#123;
                <span class="hljs-keyword">guard</span> <span class="hljs-keyword">let</span> path <span class="hljs-operator">=</span> mCollectionView<span class="hljs-operator">!</span>.indexPathForItem(at: tap.location(in: mCollectionView<span class="hljs-operator">!</span>)) <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-keyword">return</span>
                &#125;
                <span class="hljs-keyword">self</span>.onItemLongPress<span class="hljs-operator">?</span>(path,mData[path.item])
            &#125;
        &#125;
    &#125;
    <span class="hljs-comment">/**
     移除cell
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">removeItem</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">indexPath</span>:<span class="hljs-type">IndexPath</span>)</span>&#123;
        <span class="hljs-keyword">if</span> mCollectionView <span class="hljs-operator">!=</span> <span class="hljs-literal">nil</span> &#123;
            mData.remove(at: indexPath.item)
            mCollectionView<span class="hljs-operator">?</span>.deleteItemsAtIndexPaths([indexPath], animationStyle: .automatic)
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> mTableView <span class="hljs-operator">!=</span> <span class="hljs-literal">nil</span> &#123;
            mData.remove(at: indexPath.row)
            mTableView<span class="hljs-operator">?</span>.deleteItemsAtIndexPaths([indexPath], animationStyle: .automatic)
        &#125;
    &#125;
    
    
    <span class="hljs-comment">//MARK:  UITableView =========================================================</span>
    
    <span class="hljs-comment">/**
     设置view显示内容 - UITableViewCell
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">bindView</span>(<span class="hljs-params">data</span>:<span class="hljs-type">T</span>, <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>, <span class="hljs-params">tableCell</span>:<span class="hljs-type">UITableViewCell</span>)</span>&#123;
        
    &#125;
    <span class="hljs-comment">/**
     table cell height
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">cellHeight</span>(<span class="hljs-params">data</span>:<span class="hljs-type">T</span>, <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>)</span> -> <span class="hljs-type">CGFloat</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">100</span>
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">tableView</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">tableView</span>: <span class="hljs-type">UITableView</span>, <span class="hljs-params">numberOfRowsInSection</span> <span class="hljs-params">section</span>: <span class="hljs-type">Int</span>)</span> -> <span class="hljs-type">Int</span> &#123;
        mData.count
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">tableView</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">tableView</span>: <span class="hljs-type">UITableView</span>, <span class="hljs-params">cellForRowAt</span> <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>)</span> -> <span class="hljs-type">UITableViewCell</span> &#123;
        <span class="hljs-keyword">var</span> cellId <span class="hljs-operator">=</span> <span class="hljs-type">DefaultCellId</span>
        <span class="hljs-keyword">if</span> <span class="hljs-type">T</span>.<span class="hljs-keyword">self</span> <span class="hljs-keyword">is</span> <span class="hljs-type">CellType</span> &#123;
            cellId <span class="hljs-operator">=</span> (mData[indexPath.row] <span class="hljs-keyword">as!</span> <span class="hljs-type">CellType</span>).cellType
        &#125;
<span class="hljs-comment">//        let cellId = mData[indexPath.row].cellType</span>
        <span class="hljs-keyword">let</span> cell <span class="hljs-operator">=</span> tableView.dequeueReusableCell(withIdentifier: cellId, for: indexPath)
        <span class="hljs-keyword">self</span>.bindView(data: mData[indexPath.row], indexPath: indexPath, tableCell: cell)
        <span class="hljs-keyword">return</span> cell
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">tableView</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">tableView</span>: <span class="hljs-type">UITableView</span>, <span class="hljs-params">didSelectRowAt</span> <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>)</span> &#123;
        <span class="hljs-keyword">self</span>.onItemSelected<span class="hljs-operator">?</span>(indexPath,mData[indexPath.row])
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">tableView</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">tableView</span>: <span class="hljs-type">UITableView</span>, <span class="hljs-params">heightForRowAt</span> <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>)</span> -> <span class="hljs-type">CGFloat</span> &#123;
        <span class="hljs-keyword">return</span> cellHeight(data: mData[indexPath.row], indexPath: indexPath)
    &#125;
    
    
    
    <span class="hljs-comment">//MARK:  UICollectionView =========================================================</span>
    
    <span class="hljs-comment">/**
     设置view显示内容 - UICollectionViewCell
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">bindView</span>(<span class="hljs-params">data</span>:<span class="hljs-type">T</span>, <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>, <span class="hljs-params">collectionCell</span>:<span class="hljs-type">UICollectionViewCell</span>)</span>&#123;
        
    &#125;
    <span class="hljs-comment">/**
     cell size
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">cellSize</span>(<span class="hljs-params">data</span>:<span class="hljs-type">T</span>, <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>)</span> -> <span class="hljs-type">CGSize</span>&#123;
        <span class="hljs-keyword">return</span> .zero
    &#125;
    <span class="hljs-comment">/**
     行间距
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">lineSpace</span>()</span> -> <span class="hljs-type">CGFloat</span>&#123;
        <span class="hljs-number">0</span>
    &#125;
    <span class="hljs-comment">/**
     左右间距
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">interitemSpace</span>()</span> -> <span class="hljs-type">CGFloat</span>&#123;
        <span class="hljs-number">0</span>
    &#125;
    <span class="hljs-comment">/**
     section 边距
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">sectionInset</span>()</span> -> <span class="hljs-type">UIEdgeInsets</span> &#123;
        .zero
    &#125;
    
    
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">collectionView</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">collectionView</span>: <span class="hljs-type">UICollectionView</span>, <span class="hljs-params">numberOfItemsInSection</span> <span class="hljs-params">section</span>: <span class="hljs-type">Int</span>)</span> -> <span class="hljs-type">Int</span> &#123;
        mData.count
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">collectionView</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">collectionView</span>: <span class="hljs-type">UICollectionView</span>, <span class="hljs-params">cellForItemAt</span> <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>)</span> -> <span class="hljs-type">UICollectionViewCell</span> &#123;
        <span class="hljs-keyword">var</span> cellId <span class="hljs-operator">=</span> <span class="hljs-type">DefaultCellId</span>
        <span class="hljs-keyword">if</span> <span class="hljs-type">T</span>.<span class="hljs-keyword">self</span> <span class="hljs-keyword">is</span> <span class="hljs-type">CellType</span> &#123;
            cellId <span class="hljs-operator">=</span> (mData[indexPath.item] <span class="hljs-keyword">as!</span> <span class="hljs-type">CellType</span>).cellType
        &#125;
<span class="hljs-comment">//        let cellId = mData[indexPath.item].cellType</span>
        <span class="hljs-keyword">let</span> cell <span class="hljs-operator">=</span> collectionView.dequeueReusableCell(withReuseIdentifier: cellId, for: indexPath)
        <span class="hljs-keyword">self</span>.bindView(data: mData[indexPath.item], indexPath: indexPath, collectionCell: cell)
        <span class="hljs-keyword">return</span> cell
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">collectionView</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">collectionView</span>: <span class="hljs-type">UICollectionView</span>, <span class="hljs-params">didSelectItemAt</span> <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>)</span> &#123;
        <span class="hljs-keyword">self</span>.onItemSelected<span class="hljs-operator">?</span>(indexPath,mData[indexPath.item])
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">collectionView</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">collectionView</span>: <span class="hljs-type">UICollectionView</span>, <span class="hljs-params">layout</span> <span class="hljs-params">collectionViewLayout</span>: <span class="hljs-type">UICollectionViewLayout</span>, <span class="hljs-params">sizeForItemAt</span> <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>)</span> -> <span class="hljs-type">CGSize</span> &#123;
        <span class="hljs-keyword">return</span> cellSize(data:mData[indexPath.item],indexPath: indexPath)
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">collectionView</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">collectionView</span>: <span class="hljs-type">UICollectionView</span>, <span class="hljs-params">layout</span> <span class="hljs-params">collectionViewLayout</span>: <span class="hljs-type">UICollectionViewLayout</span>, <span class="hljs-params">minimumLineSpacingForSectionAt</span> <span class="hljs-params">section</span>: <span class="hljs-type">Int</span>)</span> -> <span class="hljs-type">CGFloat</span> &#123;
        <span class="hljs-keyword">return</span> lineSpace()
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">collectionView</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">collectionView</span>: <span class="hljs-type">UICollectionView</span>, <span class="hljs-params">layout</span> <span class="hljs-params">collectionViewLayout</span>: <span class="hljs-type">UICollectionViewLayout</span>, <span class="hljs-params">minimumInteritemSpacingForSectionAt</span> <span class="hljs-params">section</span>: <span class="hljs-type">Int</span>)</span> -> <span class="hljs-type">CGFloat</span> &#123;
        <span class="hljs-keyword">return</span> interitemSpace()
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">collectionView</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">collectionView</span>: <span class="hljs-type">UICollectionView</span>, <span class="hljs-params">layout</span> <span class="hljs-params">collectionViewLayout</span>: <span class="hljs-type">UICollectionViewLayout</span>, <span class="hljs-params">insetForSectionAt</span> <span class="hljs-params">section</span>: <span class="hljs-type">Int</span>)</span> -> <span class="hljs-type">UIEdgeInsets</span> &#123;
        <span class="hljs-keyword">return</span> sectionInset()
    &#125;
    
&#125;
<span class="hljs-comment">//MARK:  BaseQuickAdapter =================================</span>

<span class="hljs-comment">/**
 快速创建一个单样式的adapter
 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BaseQuickAdapter</span><<span class="hljs-title">Model</span>,<span class="hljs-title">ViewCell</span>:<span class="hljs-title">UIView</span>>: <span class="hljs-title">BaseAdapter</span><<span class="hljs-title">Model</span>> </span>&#123;
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">init</span>()</span> &#123;
        <span class="hljs-keyword">super</span>.<span class="hljs-keyword">init</span>()
        registerCell(<span class="hljs-type">ViewCell</span>.<span class="hljs-keyword">self</span>)
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">bindView</span>(<span class="hljs-params">data</span>: <span class="hljs-type">Model</span>, <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>, <span class="hljs-params">cell</span>: <span class="hljs-type">ViewCell</span>)</span>&#123;
        
    &#125;
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">bindView</span>(<span class="hljs-params">data</span>: <span class="hljs-type">Model</span>, <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>, <span class="hljs-params">tableCell</span>: <span class="hljs-type">UITableViewCell</span>)</span> &#123;
        <span class="hljs-keyword">self</span>.bindView(data: data, indexPath: indexPath, cell: tableCell <span class="hljs-keyword">as!</span> <span class="hljs-type">ViewCell</span>)
    &#125;
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">bindView</span>(<span class="hljs-params">data</span>: <span class="hljs-type">Model</span>, <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>, <span class="hljs-params">collectionCell</span>: <span class="hljs-type">UICollectionViewCell</span>)</span> &#123;
        <span class="hljs-keyword">self</span>.bindView(data: data, indexPath: indexPath, cell: collectionCell <span class="hljs-keyword">as!</span> <span class="hljs-type">ViewCell</span>)
    &#125;
&#125;

<span class="hljs-comment">//MARK:  ===============================================</span>
<span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">UICollectionView</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">setAdapter</span><<span class="hljs-type">T</span>>(<span class="hljs-keyword">_</span> <span class="hljs-params">adapter</span>:<span class="hljs-type">BaseAdapter</span><<span class="hljs-type">T</span>>)</span>&#123;
        adapter.bindTo(<span class="hljs-keyword">self</span>)
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">UITableView</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">setAdapter</span><<span class="hljs-type">T</span>>(<span class="hljs-keyword">_</span> <span class="hljs-params">adapter</span>:<span class="hljs-type">BaseAdapter</span><<span class="hljs-type">T</span>>)</span>&#123;
        adapter.bindTo(<span class="hljs-keyword">self</span>)
    &#125;
&#125;
<span class="hljs-comment">/**
 实现不同布局的cell，使model类实现此协议
 */</span>
<span class="hljs-class"><span class="hljs-keyword">protocol</span> <span class="hljs-title">CellType</span></span>&#123;
    <span class="hljs-comment">/**
     注册cell时的 ReuseIdentifier
     */</span>
    <span class="hljs-keyword">var</span> cellType:<span class="hljs-type">String</span>&#123;<span class="hljs-keyword">get</span> <span class="hljs-keyword">set</span>&#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            