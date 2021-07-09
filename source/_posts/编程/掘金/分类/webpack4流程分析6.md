
---
title: 'webpack4流程分析6'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96694014db194cfe99fa641b5c7c170c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 02:22:20 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96694014db194cfe99fa641b5c7c170c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.Compilation</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 经过之前的步骤我们得到了创建出来的modules 执行回调会到compilation.seal封装代码</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">seal</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.hooks.seal.call();
  <span class="hljs-comment">// 触发各种hook 为我们构建提供很多的钩子</span>
  <span class="hljs-built_in">this</span>.hooks.beforeChunks.call();
  <span class="hljs-comment">// _preparedEntrypoints 在addEntry的时候添加的 为每个入口生成一个chunk</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> preparedEntrypoint <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>._preparedEntrypoints) &#123;
    <span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> = preparedEntrypoint.module; <span class="hljs-comment">// 入口模块</span>
    <span class="hljs-keyword">const</span> name = preparedEntrypoint.name; <span class="hljs-comment">// main</span>
    <span class="hljs-comment">//  new Chunk(name)</span>
    <span class="hljs-keyword">const</span> chunk = <span class="hljs-built_in">this</span>.addChunk(name); <span class="hljs-comment">// 新建chunk将module添加到chunk中</span>
    <span class="hljs-comment">// extend ChunkGroup 主要用来优化 chunk graph</span>
    <span class="hljs-keyword">const</span> entrypoint = <span class="hljs-keyword">new</span> Entrypoint(name); <span class="hljs-comment">// 生成入口点</span>
    entrypoint.setRuntimeChunk(chunk); <span class="hljs-comment">// 运行时chunk</span>
    entrypoint.addOrigin(<span class="hljs-literal">null</span>, name, preparedEntrypoint.request); <span class="hljs-comment">// 增加来源</span>
    <span class="hljs-built_in">this</span>.namedChunkGroups.set(name, entrypoint); <span class="hljs-comment">// key为chunk的名称 值为chunkGroup</span>
    <span class="hljs-built_in">this</span>.entrypoints.set(name, entrypoint); <span class="hljs-comment">// key为chunk的名称 值为chunkGroup</span>
    <span class="hljs-built_in">this</span>.chunkGroups.push(entrypoint); <span class="hljs-comment">// 添加一个新的chunkGroup</span>

    <span class="hljs-comment">// 建立chunkGroup和chunk的关系 chunk.addGroup(chunkGroup);</span>
    <span class="hljs-comment">// this._groups.add(chunkGroup)</span>
    GraphHelpers.connectChunkGroupAndChunk(entrypoint, chunk);
    <span class="hljs-comment">// 建立chunk和module的关系 chunk.addModule(module);</span>
    <span class="hljs-comment">// this._modules.add(module);</span>
    GraphHelpers.connectChunkAndModule(chunk, <span class="hljs-built_in">module</span>);
    chunk.entryModule = <span class="hljs-built_in">module</span>; <span class="hljs-comment">// 代码块的入口模块</span>
    chunk.name = name; <span class="hljs-comment">// 代码块的名称</span>
    <span class="hljs-comment">// 依赖的深度??</span>
    <span class="hljs-comment">// this.assignDepth(module);</span>
  &#125;
  <span class="hljs-comment">// [&#123;Entrypoint: chunks: [ chunk: [&#123;_modules, _groups&#125;] ]&#125;]</span>
  <span class="hljs-comment">// 构建chunkGraph 用来生成优化chunk依赖图</span>
  buildChunkGraph(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>.chunkGroups.slice());
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. buildChunkGraph</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// seal的流程很多 先分析 buildChunkGraph 主要分为三步</span>
<span class="hljs-keyword">const</span> buildChunkGraph = <span class="hljs-function">(<span class="hljs-params">compilation, inputChunkGroups</span>) =></span> &#123;
  <span class="hljs-comment">// 1. 建立chunkGroup chunk module之间的关系 使用 blockInfoMap 保存信息</span>
  visitModules();
  <span class="hljs-comment">// 2. 建立不同chunkGroup之间的父子关系 优化chunkGroup</span>
  connectChunkGroups();
  <span class="hljs-comment">// 3. 清理无用的chunk 清理相关的联系</span>
  cleanupUnconnectedGroups();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">2.1 demo</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 为了方便看里面的逻辑 建立一个demo</span>
<span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> common <span class="hljs-keyword">from</span> <span class="hljs-string">"./common.js"</span>;
<span class="hljs-keyword">import</span>(<span class="hljs-string">"./async.js"</span>).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> <span class="hljs-built_in">console</span>.log(result));
<span class="hljs-comment">// async.js</span>
<span class="hljs-keyword">import</span> title <span class="hljs-keyword">from</span> <span class="hljs-string">"./title.js"</span>;
<span class="hljs-keyword">import</span>(<span class="hljs-string">"./common.js"</span>).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> <span class="hljs-built_in">console</span>.log(result));
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> lazy = <span class="hljs-string">"lazy"</span>;
<span class="hljs-comment">// common.js</span>
<span class="hljs-keyword">import</span> title <span class="hljs-keyword">from</span> <span class="hljs-string">"./title.js"</span>;
<span class="hljs-comment">// title.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> title = <span class="hljs-string">"title"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96694014db194cfe99fa641b5c7c170c~tplv-k3u1fbpfcp-watermark.image" alt="demo.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2.2 visitModules</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. 建立关联</span>
<span class="hljs-keyword">const</span> visitModules = <span class="hljs-function">(<span class="hljs-params">
  compilation,
  inputChunkGroups,
  chunkGroupInfoMap,
  blockConnections,
  blocksWithNestedBlocks,
  allCreatedChunkGroups
</span>) =></span> &#123;
  <span class="hljs-comment">// 1.使用blockInfo用来存储模块关系 同步存入modules 异步blocks module graph</span>

  <span class="hljs-comment">// 经过处理 blockInfoMap 中共有6条记录 特别注意ImportDependenciesBlock_async的两个</span>
  <span class="hljs-comment">// const obj = &#123;</span>
  <span class="hljs-comment">//   NormalModule_index: &#123; modules: [common], blocks: [async] &#125;,</span>
  <span class="hljs-comment">//   ImportDependenciesBlock_async: &#123; modules: [async], blocks: [] &#125;,</span>
  <span class="hljs-comment">//   NormalModule_common: &#123; modules: [title], blocks: [] &#125;,</span>
  <span class="hljs-comment">//   NormalModule_async: &#123; blocks: [common], modules: [title] &#125;,</span>
  <span class="hljs-comment">//   ImportDependenciesBlock_common: &#123; modules: [common] &#125;,</span>
  <span class="hljs-comment">//   NormalModule_title: &#123; modules: [] &#125;,</span>
  <span class="hljs-comment">// &#125;;</span>

  <span class="hljs-keyword">const</span> blockInfoMap = extraceBlockInfoMap(compilation);

  <span class="hljs-comment">// 2.处理模块之见的关系 chunk graph</span>
  <span class="hljs-keyword">let</span> nextFreeModuleIndex = <span class="hljs-number">0</span>; <span class="hljs-comment">// 下一个模块的空闲索引 每个模块是有两个index的默认是0</span>
  <span class="hljs-keyword">let</span> nextFreeModuleIndex2 = <span class="hljs-number">0</span>; <span class="hljs-comment">// 通过下表去添加值</span>
  <span class="hljs-keyword">const</span> ADD_AND_ENTER_MODULE = <span class="hljs-number">0</span>; <span class="hljs-comment">// 增加进入模块</span>
  <span class="hljs-keyword">const</span> ENTER_MODULE = <span class="hljs-number">1</span>; <span class="hljs-comment">// 进入模块</span>
  <span class="hljs-keyword">const</span> PROCESS_BLOCK = <span class="hljs-number">2</span>; <span class="hljs-comment">// 处理代码块</span>
  <span class="hljs-keyword">const</span> LEAVE_MODULE = <span class="hljs-number">3</span>; <span class="hljs-comment">// 离开模块</span>

  <span class="hljs-keyword">const</span> reduceChunkGroupToQueueItem = <span class="hljs-function">(<span class="hljs-params">queue, chunkGroup</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunk <span class="hljs-keyword">of</span> chunkGroup.chunks) &#123;
      queue.push(&#123;
        <span class="hljs-attr">action</span>: ENTER_MODULE,
        <span class="hljs-attr">block</span>: <span class="hljs-built_in">module</span>,
        <span class="hljs-attr">module</span>: chunk.entryModule,
        chunk,
        chunkGroup,
      &#125;);
    &#125;
    <span class="hljs-comment">// 设置 chunkGroupInfoMap 映射 chunkGroup 和相关的信息对象</span>
    chunkGroupInfoMap.set(chunkGroup, &#123; chunkGroup, <span class="hljs-attr">children</span>: <span class="hljs-literal">undefined</span> &#125;);
    <span class="hljs-keyword">return</span> queue;
  &#125;;
  <span class="hljs-comment">// 将 entryPoint(chunkGroup) 变成一个queue &#123;block, chunk, chunkGroup, module&#125;</span>
  <span class="hljs-keyword">let</span> queue = inputChunkGroups
    .reduce(reduceChunkGroupToQueueItem, [])
    .reverse();
  <span class="hljs-keyword">const</span> iteratorBlock = <span class="hljs-function">(<span class="hljs-params">b</span>) =></span> &#123;
    <span class="hljs-comment">// 1. 为block创建一个chunk import动态引入的会单独生成一个chunk(这个时候chunk中还没有依赖的module)</span>
    <span class="hljs-comment">// const chunkGroup = new ChunkGroup(groupOptions);</span>
    <span class="hljs-comment">// if (module) chunkGroup.addOrigin(module, loc, request); this.origins.push(&#123;&#125;)</span>
    <span class="hljs-comment">// const chunk = this.addChunk(name);</span>
    <span class="hljs-comment">// this.chunkGroups.push(chunkGroup);</span>
    c = compilation.addChunkInGroup(b.chunkName, <span class="hljs-built_in">module</span>);
    blockChunkGroups.set(b, c); <span class="hljs-comment">// c是一个chunkGroup</span>
    allCreatedChunkGroups.add(c); <span class="hljs-comment">// 已经创建的chunksGroup</span>
    blockConnections.set(b, []); <span class="hljs-comment">// chunk Group的依赖</span>
    <span class="hljs-comment">// 2. 建立 module 所属的 chunkGroup 和 block 和 block 属于的chunkGroup的依赖关系</span>
    <span class="hljs-comment">// 主要用于优化 chunk graph</span>
    blockConnections.get(b).push(&#123;
      <span class="hljs-attr">originChunkGroupInfo</span>: chunkGroupInfo, <span class="hljs-comment">// chunkGroupInfoMap对应的信息</span>
      <span class="hljs-attr">chunkGroup</span>: c,
    &#125;);
    <span class="hljs-comment">// 3. 创建/跟新 chunk Group 的信息</span>
    queueConnect.set(chunkGroup, connectList);
    connectList.add(c);
    <span class="hljs-comment">// 4. 代码块 用作外层的遍历</span>
    queueDelayed.push(&#123;
      <span class="hljs-attr">action</span>: PROCESS_BLOCK,
      <span class="hljs-attr">block</span>: b,
      <span class="hljs-attr">module</span>: <span class="hljs-built_in">module</span>,
      <span class="hljs-attr">chunk</span>: c.chunks[<span class="hljs-number">0</span>],
      <span class="hljs-attr">chunkGroup</span>: c,
    &#125;);
  &#125;;

  <span class="hljs-comment">/**
   * 第一次外层while是入口 entry: &#123;block, chunk, module, chunkGroup&#125;
   * 第一次内层循环
   *  进入ENTER_MODULE 处理 完成后(没有break)进入 PROCESS_BLOCK
   *  PROCESS_BLOCK中会处理 modules 和 blocks
   *  index中的
   *      modules 是 common queue.push()
   *      blocks 是 async iteratorBlock是 新建chunk queueDelayed.push() 外层循环
   *
   * 第二次内层循环
   *  处理 ./common.js 调用 module.addChunk(chunk);
   *  在处理 common 的 modules(./title.js) 和 blocks(无)
   *
   * 第三次内层循环
   *  处理 title.js 没有 modules 和 blocks
   *
   *  处理queueConnect 在处理blocks的时候会处理
   *
   * 在处理 queueDelayed 开始外层的循环
   * // 这里使用了reverse的
   * queue = queueDelayed.reverse()
   *
   * 开始第二次外层循环 
   * 开始一次内循环
   *  queueDelayed的参数 &#123;
   *    block: b, // index中blocks的block async.js
  module: module, // index的module index.js
   *  &#125;
      从bockInfoMap中找到 async 对应的 blockInfo
      block为  './async.js'  modules为空
   *
   * 。。。 通过while有一直处理下去 建立 graph图
   * 
   * 我们得到三个 chunkGroup entry async common
   */</span>
  <span class="hljs-comment">// 外层循环 会对queueDelayed的数据集进行处理 第一次的queue是entry开始</span>
  <span class="hljs-keyword">while</span> (queue.length) &#123;
    <span class="hljs-comment">// 每一轮的内层都对应同一个chunkGroup 对chunkGroup中所有的module进行处理</span>
    <span class="hljs-keyword">while</span> (queue.length) &#123;
      <span class="hljs-keyword">const</span> queueItem = queue.pop();
      <span class="hljs-built_in">module</span> = queueItem.module;
      block = queueItem.block;
      chunk = queueItem.chunk;
      chunkGroup = queueItem.chunkGroup;
      chunkGroupInfo = chunkGroupInfoMap.get(chunkGroup);
      <span class="hljs-comment">// 判断不同的同作</span>
      <span class="hljs-keyword">switch</span> (queueItem.action) &#123;
        <span class="hljs-keyword">case</span> ADD_AND_ENTER_MODULE: &#123;
          <span class="hljs-keyword">if</span> (chunk.addModule(<span class="hljs-built_in">module</span>)) &#123;
            <span class="hljs-built_in">module</span>.addChunk(chunk);
          &#125;
          <span class="hljs-keyword">break</span>;
        &#125;
        <span class="hljs-comment">// 入口出的就是进入模块</span>
        <span class="hljs-keyword">case</span> ENTER_MODULE: &#123;
          chunkGroup.setModuleIndex(
            <span class="hljs-built_in">module</span>,
            chunkGroupCounters.get(chunkGroup).index++
          );
          <span class="hljs-comment">// 添加一个离开的动作</span>
          queue.push(&#123; <span class="hljs-attr">action</span>: LEAVE_MODULE &#125;);
        &#125;
        <span class="hljs-comment">// 上面没有break 执行完ENTER_MODULE就会执行PROCESS_BLOCK处理代码快</span>
        <span class="hljs-keyword">case</span> PROCESS_BLOCK: &#123;
          <span class="hljs-comment">// 获取这个module的同步依赖modules和异步依赖blocks</span>
          <span class="hljs-comment">// 入口出的block就是chunk.entryModule</span>
          <span class="hljs-keyword">const</span> blockInfo = blockInfoMap.get(block);
          <span class="hljs-comment">// 同步的依赖</span>
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> refModule <span class="hljs-keyword">of</span> blockInfo.modules) &#123;
            <span class="hljs-keyword">if</span> (chunk.containsModule(refModule)) &#123;
              <span class="hljs-keyword">continue</span>; <span class="hljs-comment">// 有就跳过 否则添加 继续内层的遍历</span>
            &#125; <span class="hljs-keyword">else</span> &#123;
              <span class="hljs-comment">// 将依赖的module添加到这个chunkGroup中了</span>
              queueBuffer.push(&#123;
                <span class="hljs-attr">action</span>: ADD_AND_ENTER_MODULE,
                <span class="hljs-attr">block</span>: refModule,
                <span class="hljs-attr">module</span>: refModule,
                chunk,
                chunkGroup,
              &#125;);
            &#125;
          &#125;
          <span class="hljs-comment">// 处理blocks</span>
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> block <span class="hljs-keyword">of</span> blockInfo.blocks) iteratorBlock(block);
          <span class="hljs-keyword">break</span>;
        &#125;
        <span class="hljs-keyword">case</span> LEAVE_MODULE: &#123;
          <span class="hljs-comment">// 将这个module添加都了chunkGroup中</span>
          chunkGroup.setModuleIndex(<span class="hljs-built_in">module</span>);
          <span class="hljs-keyword">break</span>;
        &#125;
      &#125;
    &#125;
    <span class="hljs-comment">// block的处理会set值</span>
    <span class="hljs-keyword">while</span> (queueConnect.size > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> [chunkGroup, targets] <span class="hljs-keyword">of</span> queueConnect) &#123;
        <span class="hljs-keyword">const</span> info = chunkGroupInfoMap.get(chunkGroup);
        <span class="hljs-comment">// 1. 添加i个新的模块数据集 添加chunkGroup中chunk的模块</span>
        <span class="hljs-keyword">const</span> resultingAvailableModules = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(minAvailableModules);
        resultingAvailableModules.add(m);
        info.children = targets;
        <span class="hljs-comment">// 2. 更新chunkGroup的信息</span>
        chunkGroupInfoMap.set(target, chunkGroupInfo);
        <span class="hljs-keyword">if</span> (outdatedChunkGroupInfo.size > <span class="hljs-number">0</span>) &#123;
          <span class="hljs-comment">// 合并模块</span>
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> info <span class="hljs-keyword">of</span> outdatedChunkGroupInfo) &#123;
          &#125;
        &#125;
      &#125;
    &#125;

    <span class="hljs-comment">// 内层遍历完成表示一个chunkGroup完了</span>
    <span class="hljs-comment">// 处理queueDelayed 就是 用来处理block 异步的是在说有的同步处理了再处理的</span>
    <span class="hljs-keyword">if</span> (queue.length === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">const</span> tempQueue = queue;
      queue = queueDelayed.reverse();
      queueDelayed = tempQueue;
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2.3 extraceBlockInfoMap</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 经过之前的流程 我们可以得到4个模块</span>

<span class="hljs-comment">// 1. 处理index.js对应的模块 因为是pop会先处理block push的</span>
<span class="hljs-comment">// &#123;NormalModule => Object&#125;   // 1.index.js</span>
<span class="hljs-comment">// &#123;ImportDependenciesBlock => Object&#125;  // 2.async</span>
<span class="hljs-comment">// 2.处理common模块</span>
<span class="hljs-comment">// &#123;NormalModule => Object&#125; // 3.common</span>

<span class="hljs-comment">// 3.处理async模块</span>
<span class="hljs-comment">// &#123;NormalModule => Object&#125; // 4.async模块 里面 import 了 common</span>
<span class="hljs-comment">// &#123;ImportDependenciesBlock => Object&#125; // 5.async 模块中的 common</span>
<span class="hljs-comment">// 4.处理title的module</span>
<span class="hljs-comment">// &#123;NormalModule => Object&#125; // 6.title模块</span>
<span class="hljs-keyword">const</span> extraceBlockInfoMap = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> blockInfoMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
  <span class="hljs-keyword">const</span> iteratorDependency = <span class="hljs-function">(<span class="hljs-params">d</span>) =></span> &#123;
    <span class="hljs-comment">// module</span>
    blockInfoModules.add(refModule);
  &#125;;
  <span class="hljs-keyword">const</span> iteratorBlockPrepare = <span class="hljs-function">(<span class="hljs-params">b</span>) =></span> &#123;
    blockInfoBlocks.push(b);
    <span class="hljs-comment">// index和async中有block的依赖会再次遍历</span>
    blockQueue.push(b); <span class="hljs-comment">// 将block加入到blockQueue中 下一次遍历</span>
  &#125;;

  <span class="hljs-comment">// 遍历执行所有的模块 开始我们是有四个模块的</span>
  <span class="hljs-comment">// &#123;"～/src/index.js" => NormalModule&#125; 里面有 import('./async')</span>
  <span class="hljs-comment">// &#123;"～/src/common.js" => NormalModule&#125;</span>
  <span class="hljs-comment">// &#123;"～/src/async.js" => NormalModule&#125; 里面有 import('./common')</span>
  <span class="hljs-comment">// &#123;"～/src/title.js" => NormalModule&#125;</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">of</span> compilation.modules) &#123;
    blockQueue = [<span class="hljs-built_in">module</span>]; <span class="hljs-comment">// blockQueue</span>
    currentModule = <span class="hljs-built_in">module</span>; <span class="hljs-comment">// 当前模块</span>
    <span class="hljs-comment">// block的需要加入到队列中再次处理</span>
    <span class="hljs-keyword">while</span> (blockQueue.length > <span class="hljs-number">0</span>) &#123;
      block = blockQueue.pop(); <span class="hljs-comment">// 这里用的是pop 所有会先处理block加进来的</span>
      <span class="hljs-comment">// 分别处理 variables dependencies blocks</span>
      <span class="hljs-keyword">if</span> (block.variables) &#123;
        <span class="hljs-comment">// 变量</span>
        iteratorDependency();
      &#125;
      <span class="hljs-keyword">if</span> (block.dependencies) &#123;
        <span class="hljs-comment">// 依赖</span>
        iteratorDependency();
      &#125;
      <span class="hljs-keyword">if</span> (block.blocks) &#123;
        <span class="hljs-comment">// import的动态模块依赖</span>
        iteratorBlockPrepare();
      &#125;
      <span class="hljs-keyword">const</span> blockInfo = &#123;
        <span class="hljs-attr">modules</span>: blockInfoModules,
        <span class="hljs-attr">blocks</span>: blockInfoBlocks,
      &#125;;
      <span class="hljs-comment">// compilation.modules module</span>
      blockInfoMap.set(block, blockInfo);
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> blockInfoMap;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2.4 connectChunkGroups</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 经过上面的处理 我们得到三个chunkGroup 连接chunkGroup 建立父子关系</span>
<span class="hljs-keyword">const</span> connectChunkGroups = <span class="hljs-function">(<span class="hljs-params">
  blocksWithNestedBlocks,
  blockConnections,
  chunkGroupInfoMap
</span>) =></span> &#123;
  <span class="hljs-comment">// 检查代码块中是否已经有了所有的模块</span>
  <span class="hljs-keyword">const</span> areModulesAvailable = <span class="hljs-function">() =></span> &#123;&#125;;
  <span class="hljs-comment">// 遍历所有的connections chunk group的依赖</span>
  <span class="hljs-comment">// 在处理blocks的时候 async和common的时候 会被加到里面 blockConnections.set()</span>
  <span class="hljs-comment">// [ImportDependenciesBlock => Array(1), ImportDependenciesBlock => Array(1)]</span>
  <span class="hljs-keyword">const</span> map = &#123;
    <span class="hljs-string">"./sync.js"</span>: &#123;
      <span class="hljs-comment">// const chunkGroup = new ChunkGroup(groupOptions);</span>
      <span class="hljs-attr">chunkGroup</span>: compilation.addChunkInGroup(b.chunkName, <span class="hljs-built_in">module</span>),
    &#125;,
  &#125;;
  <span class="hljs-comment">// block是blocks中的block</span>
  <span class="hljs-comment">// blockConnections.set('./async', [&#123;originChunkGroupInfo, chunkGroup&#125;])</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> [block, connections] <span class="hljs-keyword">of</span> blockConnections) &#123;
    <span class="hljs-comment">// 1. 检查连接是否有必要</span>
    <span class="hljs-comment">// 2. Foreach edge</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < connections.length; i++) &#123;
      <span class="hljs-comment">// chunkGroup是new 出来的c  originChunkGroupInfo是map对象中值</span>
      <span class="hljs-keyword">const</span> &#123; chunkGroup, originChunkGroupInfo &#125; = connections[i];
      <span class="hljs-comment">// 之前是通过 chunkGroup.setModuleIndex(module); 往里面添加了module</span>
      <span class="hljs-comment">// 3. Connect block with chunk 把block添加到chunkGroup中</span>
      GraphHelpers.connectDependenciesBlockAndChunkGroup(block, chunkGroup);
      <span class="hljs-comment">//  4. Connect chunk with parent建立父子关系  blockInfoMap中的属性</span>
      GraphHelpers.connectChunkGroupParentAndChild(
        originChunkGroupInfo.chunkGroup,
        chunkGroup
      );
    &#125;
  &#125;
&#125;;

<span class="hljs-keyword">const</span> connectChunkGroupParentAndChild = <span class="hljs-function">(<span class="hljs-params">parent, child</span>) =></span> &#123;
  <span class="hljs-comment">// chunkGroup</span>
  <span class="hljs-keyword">if</span> (parent.addChild(child)) &#123;
    <span class="hljs-comment">// this._parents.add(parentChunk);</span>
    child.addParent(parent);
  &#125;
&#125;;

<span class="hljs-comment">// async.js: &#123;chunkGroup: chunkGroup&#125;</span>
<span class="hljs-keyword">const</span> connectDependenciesBlockAndChunkGroup = <span class="hljs-function">(<span class="hljs-params">depBlock, chunkGroup</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (chunkGroup.addBlock(depBlock)) &#123;
    depBlock.chunkGroup = chunkGroup;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.5 cleanupUnconnectedGroups</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> cleanupUnconnectedGroups = <span class="hljs-function">(<span class="hljs-params">compilation, allCreatedChunkGroups</span>) =></span> &#123;
  <span class="hljs-comment">// async和common建立的chunkGroup</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunkGroup <span class="hljs-keyword">of</span> allCreatedChunkGroups) &#123;
    <span class="hljs-keyword">if</span> (chunkGroup.getNumberOfParents() === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// 如果有父亲 就将chunkGroup中所有的chunk删除</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunk <span class="hljs-keyword">of</span> chunkGroup.chunks) &#123;
        <span class="hljs-keyword">const</span> idx = compilation.chunks.indexOf(chunk);
        <span class="hljs-keyword">if</span> (idx >= <span class="hljs-number">0</span>) compilation.chunks.splice(idx, <span class="hljs-number">1</span>);
        chunk.remove(<span class="hljs-string">"unconnected"</span>);
      &#125;
      chunkGroup.remove(<span class="hljs-string">"unconnected"</span>);
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">3. optimizeChunk</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 生成chunk之后我们对进行一些优化的处理</span>
<span class="hljs-built_in">this</span>.hooks.optimize.call();
<span class="hljs-comment">// module</span>
<span class="hljs-built_in">this</span>.hooks.optimizeModulesBasic.call(<span class="hljs-built_in">this</span>.modules)
<span class="hljs-built_in">this</span>.hooks.optimizeModules.call(<span class="hljs-built_in">this</span>.modules)
<span class="hljs-built_in">this</span>.hooks.optimizeModulesAdvanced.call(<span class="hljs-built_in">this</span>.modules)
<span class="hljs-comment">// chunks</span>
<span class="hljs-built_in">this</span>.hooks.optimizeChunksBasic.call(<span class="hljs-built_in">this</span>.chunks, <span class="hljs-built_in">this</span>.chunkGroups)
<span class="hljs-built_in">this</span>.hooks.optimizeChunks.call(<span class="hljs-built_in">this</span>.chunks, <span class="hljs-built_in">this</span>.chunkGroups)
<span class="hljs-built_in">this</span>.hooks.optimizeChunksAdvanced.call(<span class="hljs-built_in">this</span>.chunks, <span class="hljs-built_in">this</span>.chunkGroups)
<span class="hljs-built_in">this</span>.hooks.optimizeTree.callAsync(<span class="hljs-built_in">this</span>.chunks, <span class="hljs-built_in">this</span>.modules, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-built_in">this</span>.applyModuleIds(); <span class="hljs-comment">// 设置模块id</span>
  <span class="hljs-built_in">this</span>.applyChunkIds(); <span class="hljs-comment">// 设置 chunk.id</span>
  <span class="hljs-built_in">this</span>.createHash(); <span class="hljs-comment">// hash</span>
  <span class="hljs-comment">// 生成资源</span>
  <span class="hljs-built_in">this</span>.createModuleAssets();
  <span class="hljs-comment">// 生成chunk资源</span>
  <span class="hljs-built_in">this</span>.hooks.beforeChunkAssets.call();
<span class="hljs-built_in">this</span>.createChunkAssets();
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">4. SplitChunksPlugin</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 这个特性非常重要 单独说明下 当我们触发optimizeChunksAdvanced的时候</span>
<span class="hljs-comment">// 面试被问过 splitChunks的原理是什么 不知道</span>
<span class="hljs-comment">// 也是在webpackOptionsApply中处理的</span>
<span class="hljs-keyword">if</span> (options.optimization.splitChunks) &#123;
  <span class="hljs-comment">// 配置的splitChunks</span>
  <span class="hljs-keyword">const</span> SplitChunksPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./optimize/SplitChunksPlugin"</span>);
  <span class="hljs-keyword">new</span> SplitChunksPlugin(options.optimization.splitChunks).apply(compiler);
&#125;
<span class="hljs-comment">// 配置的runtimeChunk</span>
<span class="hljs-keyword">if</span> (options.optimization.runtimeChunk) &#123;
  <span class="hljs-keyword">const</span> RuntimeChunkPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./optimize/RuntimeChunkPlugin"</span>);
  <span class="hljs-keyword">new</span> RuntimeChunkPlugin(options.optimization.runtimeChunk).apply(compiler);
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SplitChunksPlugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-comment">// 格式化</span>
    <span class="hljs-built_in">this</span>.options = SplitChunksPlugin.normalizeOptions(options);
  &#125;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    compiler.hooks.thisCompilation.tap(<span class="hljs-string">"SplitChunksPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">compilation</span>) =></span> &#123;
      <span class="hljs-comment">// 监听这个钩子 在生成了chunkGroup之后 优化的时候触发的代码分割</span>
      compilation.hooks.optimizeChunksAdvanced.tap(
        <span class="hljs-string">"SplitChunksPlugin"</span>,
        <span class="hljs-function">(<span class="hljs-params">chunks</span>) =></span> &#123;&#125;
      )
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">4.1 config</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 以element-admin的配置为例子 加一些配置的说明</span>
config.optimization.splitChunks(&#123;
   <span class="hljs-comment">// initial async all function(return chunks) 要提取的模块</span>
  <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>,
  <span class="hljs-comment">// minSize: 10000, // 最小的体积 10k的才会分出来</span>
  <span class="hljs-comment">// maxSize: 0, // 代表能分则分 分不了就算了 保证尽量的小</span>
  <span class="hljs-comment">// minChunks: 1, //  最小的被引用次数</span>
  <span class="hljs-comment">// maxAsyncRequests: 5, // 按需加载的代码块最多允许的并行请求数 在webpack5里默认值变为6</span>
  <span class="hljs-comment">// maxInitialRequests: 3, // 入口代码块最多允许的并行请求数，在webpack5里默认值变为4</span>
  <span class="hljs-comment">// automaticNameDelimiter: "~", // 代码块命名分割符</span>
  <span class="hljs-comment">// name: true, // 每个缓存组打包得到的代码块的名称</span>
  <span class="hljs-attr">cacheGroups</span>: &#123;
    <span class="hljs-attr">libs</span>: &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'chunk-libs'</span>, <span class="hljs-comment">// 打包的名字</span>
      <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\\/]node_modules[\\/]/</span>, <span class="hljs-comment">// 正则</span>
      priority: <span class="hljs-number">10</span>, <span class="hljs-comment">// 优先级</span>
      <span class="hljs-attr">chunks</span>: <span class="hljs-string">'initial'</span>
    &#125;,
    <span class="hljs-attr">elementUI</span>: &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'chunk-elementUI'</span>,
      <span class="hljs-attr">priority</span>: <span class="hljs-number">20</span>, 
      <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\\/]node_modules[\\/]_?element-ui(.*)/</span> 
    &#125;,
    <span class="hljs-comment">// 之前一直打包不出来是因为没有设置 minSize</span>
    <span class="hljs-attr">commons</span>: &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'chunk-commons'</span>,
      <span class="hljs-attr">test</span>: resolve(<span class="hljs-string">'src/components'</span>), 
      <span class="hljs-attr">minSize</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 最小提取字节数</span>
      <span class="hljs-attr">minChunks</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 最小的被引用次数</span>
      <span class="hljs-attr">priority</span>: <span class="hljs-number">5</span>,
      <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 重用模块</span>
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">4.2 demo</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 为了演示效果 我们安装element-ui和jquery</span>

<span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> $ <span class="hljs-keyword">from</span> <span class="hljs-string">"jquery"</span>;
<span class="hljs-keyword">import</span> ElementUI <span class="hljs-keyword">from</span> <span class="hljs-string">"element-ui"</span>;
<span class="hljs-keyword">import</span>(<span class="hljs-string">"./async.js"</span>).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> <span class="hljs-built_in">console</span>.log(result));
<span class="hljs-keyword">import</span>(<span class="hljs-string">"./async1.js"</span>).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> <span class="hljs-built_in">console</span>.log(result));
<span class="hljs-keyword">import</span>(<span class="hljs-string">"./async2.js"</span>).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> <span class="hljs-built_in">console</span>.log(result));
<span class="hljs-comment">// async async1 async2 设置了minChunks表示至少被几个chunk引用</span>
<span class="hljs-keyword">import</span> title <span class="hljs-keyword">from</span> <span class="hljs-string">"./title.js"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>得到打包结果</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbbd2a394fdf432bb0f2b51ae0df4e94~tplv-k3u1fbpfcp-watermark.image" alt="WX20210621-103945@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">4.3</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// splitChunk就是将每个模块按照规则分配到不同的缓存组中</span>
<span class="hljs-comment">// 每个缓存组对应最终分割出来的新代码块</span>
<span class="hljs-comment">// chunksInfoMap </span>
<span class="hljs-comment">// addModuleToChunksInfoMap</span>
<span class="hljs-comment">// newChunk = compilation.addChunk(chunkName);</span>
<span class="hljs-function"><span class="hljs-keyword">function</span>  <span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>) </span>&#123;
  compiler.hooks.thisCompilation.tap(<span class="hljs-string">"SplitChunksPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">compilation</span>) =></span> &#123;
    <span class="hljs-comment">// 监听这个钩子 在生成了chunkGroup之后 优化的时候触发的代码分割</span>
    compilation.hooks.optimizeChunksAdvanced.tap(
      <span class="hljs-string">"SplitChunksPlugin"</span>,
      <span class="hljs-function">(<span class="hljs-params">chunks</span>) =></span> &#123;
        <span class="hljs-comment">// 生成一个index 给每个选中的chunk一个index  create strings from chunks</span>
        indexMap.set(chunk, index++);
        <span class="hljs-comment">// key和chunkSet的关系</span>
        <span class="hljs-keyword">const</span> chunkSetsInGraph = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
        <span class="hljs-comment">// 遍历modules为每个module的chunk生成一个key</span>
        <span class="hljs-comment">// 经过上面的处理 我们得到四个chunk n个modules(element-ui和jquery中有很多个module)</span>
        <span class="hljs-comment">// &#123;1: &#123;&#125;, 2: &#123;&#125;, 3: &#123;&#125;, 4: &#123;&#125;, '2, 3, 4': &#123;set(3)&#125;&#125; title.js是在三个chunks中的</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">of</span> compilation.modules) &#123;
          <span class="hljs-comment">// chunksIterable return this._chunks</span>
          <span class="hljs-keyword">const</span> chunksKey = getKey(<span class="hljs-built_in">module</span>.chunksIterable);
          <span class="hljs-keyword">if</span> (!chunkSetsInGraph.has(chunksKey)) &#123;
            chunkSetsInGraph.set(chunksKey, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(<span class="hljs-built_in">module</span>.chunksIterable));
          &#125;
        &#125;

        <span class="hljs-comment">// 按照count对这些chunk进行分组</span>
        <span class="hljs-keyword">const</span> chunkSetsByCount = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
        <span class="hljs-comment">// &#123;1: [4], 3: [3]&#125; 数量为1的是四个chunk 3个的是 set(3)</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunksSet <span class="hljs-keyword">of</span> chunkSetsInGraph.values()) &#123;
          <span class="hljs-comment">// 每个module对应一个chunksSet 一个chunkSet中有多个module就是有多个count</span>
          <span class="hljs-keyword">const</span> count = chunksSet.size;
          <span class="hljs-keyword">let</span> array = chunkSetsByCount.get(count);
          <span class="hljs-keyword">if</span> (array === <span class="hljs-literal">undefined</span>) &#123;
            array = [];
            chunkSetsByCount.set(count, array);
          &#125;
          array.push(chunksSet);
        &#125;

        <span class="hljs-comment">// 创建一个可能组合的列表  Map<string, Set<Chunk>[]></span>
        <span class="hljs-keyword">const</span> combinationsCache = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
        <span class="hljs-comment">// 根据key得到module中对应的chunks集合 set</span>
        <span class="hljs-keyword">const</span> chunksSet = chunkSetsInGraph.get(key);
        <span class="hljs-keyword">const</span> getCombinations = <span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
          <span class="hljs-keyword">const</span> chunksSet = chunkSetsInGraph.get(key);
          <span class="hljs-keyword">var</span> array = [chunksSet];
          <span class="hljs-keyword">if</span> (chunksSet.size > <span class="hljs-number">1</span>) &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> [count, setArray] <span class="hljs-keyword">of</span> chunkSetsByCount) &#123;
              <span class="hljs-comment">// "equal" is not needed because they would have been merge in the first step</span>
              <span class="hljs-keyword">if</span> (count < chunksSet.size) &#123;
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> set <span class="hljs-keyword">of</span> setArray) &#123;
                  <span class="hljs-keyword">if</span> (isSubset(chunksSet, set)) &#123;
                    array.push(set);
                  &#125;
                &#125;
              &#125;
            &#125;
          &#125;
          <span class="hljs-keyword">return</span> array;
        &#125;;
        <span class="hljs-comment">// 处理缓存</span>
        <span class="hljs-comment">// const selectedChunksCacheByChunksSet = new WeakMap();</span>
        <span class="hljs-comment">// // 通过将过滤器功能应用于列表来获取列表和键 出于性能原因，它被缓存</span>
        <span class="hljs-comment">// const getSelectedChunks = (chunks, chunkFilter) => &#123;&#125;;</span>
        <span class="hljs-comment">// Map a list of chunks to a list of modules 代码分割的信息</span>
        <span class="hljs-keyword">const</span> chunksInfoMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
        <span class="hljs-keyword">const</span> addModuleToChunksInfoMap = <span class="hljs-function">(<span class="hljs-params">
          cacheGroup, <span class="hljs-comment">// the current cache group 当前的cache组</span>
          cacheGroupIndex, <span class="hljs-comment">// the index of the cache group of ordering</span>
          selectedChunks, <span class="hljs-comment">// chunks selected for this module</span>
          selectedChunksKey, <span class="hljs-comment">// a key of selectedChunks</span>
          <span class="hljs-built_in">module</span> <span class="hljs-comment">// the current module</span>
        </span>) =></span> &#123;
          <span class="hljs-comment">// minChunks属性</span>
          <span class="hljs-keyword">if</span> (selectedChunks.length < cacheGroup.minChunks) <span class="hljs-keyword">return</span>;
          <span class="hljs-comment">// name</span>
          <span class="hljs-keyword">const</span> name = cacheGroup.getName();
          <span class="hljs-comment">// key</span>
          <span class="hljs-keyword">const</span> key =
            cacheGroup.key +
            (name ? <span class="hljs-string">` name:<span class="hljs-subst">$&#123;name&#125;</span>`</span> : <span class="hljs-string">` chunks:<span class="hljs-subst">$&#123;selectedChunksKey&#125;</span>`</span>);
          <span class="hljs-keyword">let</span> info = chunksInfoMap.get(key);
          <span class="hljs-comment">// 添加新的缓存组信息</span>
          chunksInfoMap.set(
            key,
            (info = &#123;
              <span class="hljs-attr">modules</span>: <span class="hljs-keyword">new</span> SortableSet(<span class="hljs-literal">undefined</span>, sortByIdentifier),
              cacheGroup,
              cacheGroupIndex,
              name,
              <span class="hljs-attr">size</span>: <span class="hljs-number">0</span>,
              <span class="hljs-attr">chunks</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(),
              <span class="hljs-attr">reuseableChunks</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(),
              <span class="hljs-attr">chunksKeys</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(),
            &#125;)
          );
          info.modules.add(<span class="hljs-built_in">module</span>);
          info.size += <span class="hljs-built_in">module</span>.size(); <span class="hljs-comment">// 判断我们设置的miniSize</span>
          info.chunksKeys.add(selectedChunksKey);
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunk <span class="hljs-keyword">of</span> selectedChunks) &#123;
            info.chunks.add(chunk); <span class="hljs-comment">// 最后打包的是chunk</span>
          &#125;
        &#125;;
        <span class="hljs-comment">// 遍历模块 分组</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">of</span> compilation.modules) &#123;
          <span class="hljs-comment">// 一个module可能符合多个条件 我们会根据 优先级来判断</span>
          <span class="hljs-keyword">let</span> cacheGroups = <span class="hljs-built_in">this</span>.options.getCacheGroups(<span class="hljs-built_in">module</span>, context);
          <span class="hljs-keyword">const</span> chunksKey = getKey(<span class="hljs-built_in">module</span>.chunksIterable);
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> cacheGroupSource <span class="hljs-keyword">of</span> cacheGroups) &#123;
            <span class="hljs-keyword">const</span> minSize = cacheGroupSource.minSize;
            <span class="hljs-keyword">const</span> cacheGroup = &#123;
              <span class="hljs-comment">// 一系列的属性 配置</span>
              <span class="hljs-attr">key</span>: cacheGroupSource.key,
              <span class="hljs-comment">// 默认优先级是0</span>
              <span class="hljs-attr">priority</span>: cacheGroupSource.priority || <span class="hljs-number">0</span>,
              minSize,
              <span class="hljs-attr">minChunks</span>: cacheGroupSource.minChunks,
            &#125;;
          &#125;
          <span class="hljs-comment">// 根据webpack的配置 选出符合添加的chunk</span>
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunkCombination <span class="hljs-keyword">of</span> combs) &#123;
            addModuleToChunksInfoMap();
          &#125;
        &#125;
        <span class="hljs-comment">// 处理size < minSize</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> pair <span class="hljs-keyword">of</span> chunksInfoMap) &#123;
          chunksInfoMap.delete(pair[<span class="hljs-number">0</span>]);
        &#125;
        <span class="hljs-comment">// maxSize</span>
        <span class="hljs-keyword">const</span> maxSizeQueueMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
        <span class="hljs-keyword">while</span> (chunksInfoMap.size > <span class="hljs-number">0</span>) &#123;
          <span class="hljs-keyword">let</span> bestEntryKey; <span class="hljs-comment">// 最匹配的cacheGroup分组信息</span>
          <span class="hljs-keyword">let</span> bestEntry;
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> pair <span class="hljs-keyword">of</span> chunksInfoMap) &#123;
            bestEntry = pair[<span class="hljs-number">1</span>];
            bestEntryKey = pair[<span class="hljs-number">0</span>];
          &#125;
          <span class="hljs-keyword">const</span> item = bestEntry;
          chunksInfoMap.delete(bestEntryKey);
          <span class="hljs-keyword">let</span> chunkName = item.name;
          <span class="hljs-comment">// 新的chunk</span>
          <span class="hljs-keyword">let</span> newChunk;
          <span class="hljs-comment">// 重用模块 如果没有name 看是否能复用</span>
          <span class="hljs-keyword">if</span> (item.cacheGroup.reuseExistingChunk) &#123;
          &#125;
          <span class="hljs-comment">// 创建新的代码块</span>
          newChunk = compilation.addChunk(chunkName);
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunk <span class="hljs-keyword">of</span> usedChunks) &#123;
            <span class="hljs-comment">// Add graph connections for splitted chunk 建立关系</span>
            chunk.split(newChunk);
          &#125;
          <span class="hljs-keyword">if</span> (chunkName) &#123;
            <span class="hljs-keyword">const</span> entrypoint = compilation.entrypoints.get(chunkName);
          &#125;
          <span class="hljs-comment">// 删除提取出来的模块</span>
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> [key, info] <span class="hljs-keyword">of</span> chunksInfoMap) &#123;
          &#125;
          <span class="hljs-comment">// Make sure that maxSize is fulfilled</span>
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunk <span class="hljs-keyword">of</span> compilation.chunks.slice()) &#123;
          &#125;
        &#125;
      &#125;
    );
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">5. hash</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 各种hash值 content hash chunk hash full hash module hash</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createHash</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> hashFunction = outputOptions.hashFunction;
  <span class="hljs-keyword">const</span> hash = createHash(hashFunction);
  <span class="hljs-comment">// new MainTemplate(this.outputOptions);</span>
  <span class="hljs-built_in">this</span>.mainTemplate.updateHash(hash);
  <span class="hljs-built_in">this</span>.chunkTemplate.updateHash(hash);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">of</span> <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">this</span>.moduleTemplates).sort()) &#123;
    <span class="hljs-built_in">this</span>.moduleTemplates[key].updateHash(hash);
  &#125;
  <span class="hljs-comment">// module hash</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.modules.length; i++) &#123;
    <span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> = modules[i];
    <span class="hljs-keyword">const</span> moduleHash = createHash(hashFunction);
    <span class="hljs-built_in">module</span>.updateHash(moduleHash);
  &#125;
  <span class="hljs-keyword">const</span> chunks = <span class="hljs-built_in">this</span>.chunks.slice();
  chunks.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> &#123;&#125;);
  <span class="hljs-comment">// chunk hash</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < chunks.length; i++) &#123;
    <span class="hljs-keyword">const</span> chunk = chunks[i];
    <span class="hljs-keyword">const</span> chunkHash = createHash(hashFunction);
    <span class="hljs-comment">// hasRuntime</span>
    <span class="hljs-built_in">this</span>.hooks.contentHash.call(chunk);
  &#125;
  <span class="hljs-built_in">this</span>.fullHash = <span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;string&#125;</span> </span>*/</span> (hash.digest(hashDigest));
  <span class="hljs-built_in">this</span>.hash = <span class="hljs-built_in">this</span>.fullHash.substr(<span class="hljs-number">0</span>, hashDigestLength);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            