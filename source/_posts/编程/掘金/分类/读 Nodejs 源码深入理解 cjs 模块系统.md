
---
title: '读 Node.js 源码深入理解 cjs 模块系统'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4673'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 00:19:34 GMT
thumbnail: 'https://picsum.photos/400/300?random=4673'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>作者：牟牟（周飞宇）</p>
</blockquote>
<h1 data-id="heading-0">前前言</h1>
<p>🔥 震惊！寒冬下！这个淘系前端团队居然还有海量校招HC！我们团队今年的校招开始啦，欢迎大家投递，详见<a href="https://juejin.cn/post/7138722162802130980" target="_blank" title="https://juejin.cn/post/7138722162802130980">链接</a></p>
<h1 data-id="heading-1">前言</h1>
<p>相信大家都知道如何在 Node.js 中加载一个模块：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);
<span class="hljs-keyword">const</span> anotherModule = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./another-module'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没错，<code>require</code> 就是加载 cjs 模块的 API，但 V8 本身是没有 cjs 模块系统的，所以 node 是怎么通过 <code>require</code>找到模块并且加载的呢？我们今天将对 Node.js 源码进行探索，深入理解 cjs 模块的加载过程。
我们阅读的 node 代码版本为 v17.x：</p>
<ul>
<li>git head ：881174e016d6c27b20c70111e6eae2296b6c6293</li>
<li>代码链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Ftree%2F881174e016d6c27b20c70111e6eae2296b6c6293" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nodejs/node/tree/881174e016d6c27b20c70111e6eae2296b6c6293" ref="nofollow noopener noreferrer">github.com/nodejs/node…</a></li>
</ul>
<h1 data-id="heading-2">源码阅读</h1>
<h2 data-id="heading-3">内置模块</h2>
<p>为了知道 <code>require</code> 的工作逻辑，我们需要先了解内置模块是如何被加载到 node 中的(诸如 'fs'，'path'，'child_process'，其中也包括一些无法被用户引用的内部模块)，准备好代码之后，我们首先要从 node 启动开始阅读。
node 的 main 函数在 <code>[src/node_main.cc](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/src/node_main.cc#L105)</code> 内，通过调用方法 <code>[node::Start](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/src/node.cc#L1134)</code> 来启动一个 node 实例：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-type">int</span> <span class="hljs-title">Start</span><span class="hljs-params">(<span class="hljs-type">int</span> argc, <span class="hljs-type">char</span>** argv)</span> </span>&#123;
  InitializationResult result = <span class="hljs-built_in">InitializeOncePerProcess</span>(argc, argv);
  <span class="hljs-keyword">if</span> (result.early_return) &#123;
    <span class="hljs-keyword">return</span> result.exit_code;
  &#125;

  &#123;
    Isolate::CreateParams params;
    <span class="hljs-type">const</span> std::vector<<span class="hljs-type">size_t</span>>* indices = <span class="hljs-literal">nullptr</span>;
    <span class="hljs-type">const</span> EnvSerializeInfo* env_info = <span class="hljs-literal">nullptr</span>;
    <span class="hljs-type">bool</span> use_node_snapshot =
        per_process::cli_options->per_isolate->node_snapshot;
    <span class="hljs-keyword">if</span> (use_node_snapshot) &#123;
      v8::StartupData* blob = NodeMainInstance::<span class="hljs-built_in">GetEmbeddedSnapshotBlob</span>();
      <span class="hljs-keyword">if</span> (blob != <span class="hljs-literal">nullptr</span>) &#123;
        params.snapshot_blob = blob;
        indices = NodeMainInstance::<span class="hljs-built_in">GetIsolateDataIndices</span>();
        env_info = NodeMainInstance::<span class="hljs-built_in">GetEnvSerializeInfo</span>();
      &#125;
    &#125;
    <span class="hljs-built_in">uv_loop_configure</span>(<span class="hljs-built_in">uv_default_loop</span>(), UV_METRICS_IDLE_TIME);

    <span class="hljs-function">NodeMainInstance <span class="hljs-title">main_instance</span><span class="hljs-params">(&params,
                                   uv_default_loop(),
                                   per_process::v8_platform.Platform(),
                                   result.args,
                                   result.exec_args,
                                   indices)</span></span>;
    result.exit_code = main_instance.<span class="hljs-built_in">Run</span>(env_info);
  &#125;

  <span class="hljs-built_in">TearDownOncePerProcess</span>();
  <span class="hljs-keyword">return</span> result.exit_code;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里创建了事件循环，且创建了一个 <code>NodeMainInstance</code> 的实例 <code>main_instance</code> 并调用了它的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fblob%2F881174e016d6c27b20c70111e6eae2296b6c6293%2Fsrc%2Fnode_main_instance.cc%23L127" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/src/node_main_instance.cc#L127" ref="nofollow noopener noreferrer">Run</a> 方法：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-type">int</span> <span class="hljs-title">NodeMainInstance::Run</span><span class="hljs-params">(<span class="hljs-type">const</span> EnvSerializeInfo* env_info)</span> </span>&#123;
  <span class="hljs-function">Locker <span class="hljs-title">locker</span><span class="hljs-params">(isolate_)</span></span>;
  <span class="hljs-function">Isolate::Scope <span class="hljs-title">isolate_scope</span><span class="hljs-params">(isolate_)</span></span>;
  <span class="hljs-function">HandleScope <span class="hljs-title">handle_scope</span><span class="hljs-params">(isolate_)</span></span>;

  <span class="hljs-type">int</span> exit_code = <span class="hljs-number">0</span>;
  DeleteFnPtr<Environment, FreeEnvironment> env =
      <span class="hljs-built_in">CreateMainEnvironment</span>(&exit_code, env_info);
  <span class="hljs-built_in">CHECK_NOT_NULL</span>(env);

  <span class="hljs-function">Context::Scope <span class="hljs-title">context_scope</span><span class="hljs-params">(env->context())</span></span>;
  <span class="hljs-built_in">Run</span>(&exit_code, env.<span class="hljs-built_in">get</span>());
  <span class="hljs-keyword">return</span> exit_code;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Run</code> 方法中调用 <code>[CreateMainEnvironment](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/src/node_main_instance.cc#L170)</code> 来创建并初始化环境：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function">Environment* <span class="hljs-title">CreateEnvironment</span><span class="hljs-params">(
    IsolateData* isolate_data,
    Local<Context> context,
    <span class="hljs-type">const</span> std::vector<std::string>& args,
    <span class="hljs-type">const</span> std::vector<std::string>& exec_args,
    EnvironmentFlags::Flags flags,
    ThreadId thread_id,
    std::unique_ptr<InspectorParentHandle> inspector_parent_handle)</span> </span>&#123;
  Isolate* isolate = context-><span class="hljs-built_in">GetIsolate</span>();
  <span class="hljs-function">HandleScope <span class="hljs-title">handle_scope</span><span class="hljs-params">(isolate)</span></span>;
  <span class="hljs-function">Context::Scope <span class="hljs-title">context_scope</span><span class="hljs-params">(context)</span></span>;
  <span class="hljs-comment">// TODO(addaleax): This is a much better place for parsing per-Environment</span>
  <span class="hljs-comment">// options than the global parse call.</span>
  Environment* env = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Environment</span>(
      isolate_data, context, args, exec_args, <span class="hljs-literal">nullptr</span>, flags, thread_id);
<span class="hljs-meta">#<span class="hljs-keyword">if</span> HAVE_INSPECTOR</span>
  <span class="hljs-keyword">if</span> (inspector_parent_handle) &#123;
    env-><span class="hljs-built_in">InitializeInspector</span>(
        std::<span class="hljs-built_in">move</span>(<span class="hljs-built_in">static_cast</span><InspectorParentHandleImpl*>(
            inspector_parent_handle.<span class="hljs-built_in">get</span>())->impl));
  &#125; <span class="hljs-keyword">else</span> &#123;
    env-><span class="hljs-built_in">InitializeInspector</span>(&#123;&#125;);
  &#125;
<span class="hljs-meta">#<span class="hljs-keyword">endif</span></span>

  <span class="hljs-keyword">if</span> (env-><span class="hljs-built_in">RunBootstrapping</span>().<span class="hljs-built_in">IsEmpty</span>()) &#123;
    <span class="hljs-built_in">FreeEnvironment</span>(env);
    <span class="hljs-keyword">return</span> <span class="hljs-literal">nullptr</span>;
  &#125;

  <span class="hljs-keyword">return</span> env;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建 <code>Environment</code> 对象 <code>env</code> 并调用其 <code>[RunBootstrapping](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/src/node.cc#L398)</code> 方法：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function">MaybeLocal<Value> <span class="hljs-title">Environment::RunBootstrapping</span><span class="hljs-params">()</span> </span>&#123;
  <span class="hljs-function">EscapableHandleScope <span class="hljs-title">scope</span><span class="hljs-params">(isolate_)</span></span>;

  <span class="hljs-built_in">CHECK</span>(!<span class="hljs-built_in">has_run_bootstrapping_code</span>());

  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">BootstrapInternalLoaders</span>().<span class="hljs-built_in">IsEmpty</span>()) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">MaybeLocal</span><Value>();
  &#125;

  Local<Value> result;
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">BootstrapNode</span>().<span class="hljs-built_in">ToLocal</span>(&result)) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">MaybeLocal</span><Value>();
  &#125;

  <span class="hljs-comment">// Make sure that no request or handle is created during bootstrap -</span>
  <span class="hljs-comment">// if necessary those should be done in pre-execution.</span>
  <span class="hljs-comment">// Usually, doing so would trigger the checks present in the ReqWrap and</span>
  <span class="hljs-comment">// HandleWrap classes, so this is only a consistency check.</span>
  <span class="hljs-built_in">CHECK</span>(<span class="hljs-built_in">req_wrap_queue</span>()-><span class="hljs-built_in">IsEmpty</span>());
  <span class="hljs-built_in">CHECK</span>(<span class="hljs-built_in">handle_wrap_queue</span>()-><span class="hljs-built_in">IsEmpty</span>());

  <span class="hljs-built_in">DoneBootstrapping</span>();

  <span class="hljs-keyword">return</span> scope.<span class="hljs-built_in">Escape</span>(result);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 <code>[BootstrapInternalLoaders](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/src/node.cc#L298)</code> 实现了 node 模块加载过程中非常重要的一步：
通过包装并执行 <code>[internal/bootstrap/loaders.js](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/lib/internal/bootstrap/loaders.js#L326)</code> 获取内置模块的 <code>[nativeModulerequire](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/lib/internal/bootstrap/loaders.js#L332)</code> 函数用于加载内置的 js 模块，获取 <code>[internalBinding](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/lib/internal/bootstrap/loaders.js#L164)</code> 用于加载内置的 C++ 模块，<code>[NativeModule](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/lib/internal/bootstrap/loaders.js#L191)</code> 则是专门用于内置模块的小型模块系统。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">function</span> <span class="hljs-title function_">nativeModuleRequire</span>(<span class="hljs-params">id</span>) &#123;
  <span class="hljs-keyword">if</span> (id === loaderId) &#123;
    <span class="hljs-keyword">return</span> loaderExports;
  &#125;

  <span class="hljs-keyword">const</span> mod = <span class="hljs-title class_">NativeModule</span>.<span class="hljs-property">map</span>.<span class="hljs-title function_">get</span>(id);
  <span class="hljs-comment">// Can't load the internal errors module from here, have to use a raw error.</span>
  <span class="hljs-comment">// eslint-disable-next-line no-restricted-syntax</span>
  <span class="hljs-keyword">if</span> (!mod) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">TypeError</span>(<span class="hljs-string">`Missing internal module '<span class="hljs-subst">$&#123;id&#125;</span>'`</span>);
  <span class="hljs-keyword">return</span> mod.<span class="hljs-title function_">compileForInternalLoader</span>();
&#125;

<span class="hljs-keyword">const</span> loaderExports = &#123;
  internalBinding,
  <span class="hljs-title class_">NativeModule</span>,
  <span class="hljs-attr">require</span>: nativeModuleRequire
&#125;;

<span class="hljs-keyword">return</span> loaderExports;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，这个 <code>require</code> 函数只会被用于内置模块的加载，用户模块的加载并不会用到它。（这也是为什么我们通过打印 <code>require('module')._cache</code> 可以看到所有用户模块，却看不到 <code>fs</code> 等内置模块的原因，因为两者的加载和缓存维护方式并不一样）。</p>
<h2 data-id="heading-4">用户模块</h2>
<p>接下来让我们把目光移回到 <code>[NodeMainInstance::Run](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/src/node_main_instance.cc#L127)</code> 函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">int <span class="hljs-title class_">NodeMainInstance</span>::<span class="hljs-title class_">Run</span>(<span class="hljs-keyword">const</span> <span class="hljs-title class_">EnvSerializeInfo</span>* env_info) &#123;
  <span class="hljs-title class_">Locker</span> <span class="hljs-title function_">locker</span>(isolate_);
  <span class="hljs-title class_">Isolate</span>::<span class="hljs-title class_">Scope</span> <span class="hljs-title function_">isolate_scope</span>(isolate_);
  <span class="hljs-title class_">HandleScope</span> <span class="hljs-title function_">handle_scope</span>(isolate_);

  int exit_code = <span class="hljs-number">0</span>;
  <span class="hljs-title class_">DeleteFnPtr</span><<span class="hljs-title class_">Environment</span>, <span class="hljs-title class_">FreeEnvironment</span>> env =
      <span class="hljs-title class_">CreateMainEnvironment</span>(&exit_code, env_info);
  <span class="hljs-title function_">CHECK_NOT_NULL</span>(env);

  <span class="hljs-title class_">Context</span>::<span class="hljs-title class_">Scope</span> <span class="hljs-title function_">context_scope</span>(env-><span class="hljs-title function_">context</span>());
  <span class="hljs-title class_">Run</span>(&exit_code, env.<span class="hljs-title function_">get</span>());
  <span class="hljs-keyword">return</span> exit_code;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们已经通过 <code>CreateMainEnvironment</code> 函数创建好了一个 <code>env</code> 对象，这个 <code>Environment</code> 实例已经有了一个模块系统 <code>NativeModule</code> 用于维护内置模块。
然后代码会运行到 <code>Run</code> 函数的另一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fblob%2F881174e016d6c27b20c70111e6eae2296b6c6293%2Fsrc%2Fnode_main_instance.cc%23L142" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/src/node_main_instance.cc#L142" ref="nofollow noopener noreferrer">重载版本</a>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">void</span> <span class="hljs-title class_">NodeMainInstance</span>::<span class="hljs-title class_">Run</span>(int* exit_code, <span class="hljs-title class_">Environment</span>* env) &#123;
  <span class="hljs-keyword">if</span> (*exit_code == <span class="hljs-number">0</span>) &#123;
    <span class="hljs-title class_">LoadEnvironment</span>(env, <span class="hljs-title class_">StartExecutionCallback</span>&#123;&#125;);

    *exit_code = <span class="hljs-title class_">SpinEventLoop</span>(env).<span class="hljs-title class_">FromMaybe</span>(<span class="hljs-number">1</span>);
  &#125;

  <span class="hljs-title class_">ResetStdio</span>();

  <span class="hljs-comment">// TODO(addaleax): Neither NODE_SHARED_MODE nor HAVE_INSPECTOR really</span>
  <span class="hljs-comment">// make sense here.</span>
#<span class="hljs-keyword">if</span> <span class="hljs-variable constant_">HAVE_INSPECTOR</span> && <span class="hljs-title function_">defined</span>(__POSIX__) && !<span class="hljs-title function_">defined</span>(<span class="hljs-variable constant_">NODE_SHARED_MODE</span>)
  struct sigaction act;
  <span class="hljs-title function_">memset</span>(&act, <span class="hljs-number">0</span>, <span class="hljs-title function_">sizeof</span>(act));
  <span class="hljs-keyword">for</span> (unsigned nr = <span class="hljs-number">1</span>; nr < kMaxSignal; nr += <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">if</span> (nr == <span class="hljs-variable constant_">SIGKILL</span> || nr == <span class="hljs-variable constant_">SIGSTOP</span> || nr == <span class="hljs-variable constant_">SIGPROF</span>)
      <span class="hljs-keyword">continue</span>;
    act.<span class="hljs-property">sa_handler</span> = (nr == <span class="hljs-variable constant_">SIGPIPE</span>) ? <span class="hljs-variable constant_">SIG_IGN</span> : <span class="hljs-variable constant_">SIG_DFL</span>;
    <span class="hljs-title function_">CHECK_EQ</span>(<span class="hljs-number">0</span>, <span class="hljs-title function_">sigaction</span>(nr, &act, nullptr));
  &#125;
#endif

#<span class="hljs-keyword">if</span> <span class="hljs-title function_">defined</span>(<span class="hljs-variable constant_">LEAK_SANITIZER</span>)
  <span class="hljs-title function_">__lsan_do_leak_check</span>();
#endif
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里调用 <code>[LoadEnvironment](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/src/api/environment.cc#L403)</code>：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function">MaybeLocal<Value> <span class="hljs-title">LoadEnvironment</span><span class="hljs-params">(
    Environment* env,
    StartExecutionCallback cb)</span> </span>&#123;
  env-><span class="hljs-built_in">InitializeLibuv</span>();
  env-><span class="hljs-built_in">InitializeDiagnostics</span>();

  <span class="hljs-keyword">return</span> <span class="hljs-built_in">StartExecution</span>(env, cb);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后执行 <code>[StartExecution](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/src/node.cc#L455)</code>：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function">MaybeLocal<Value> <span class="hljs-title">StartExecution</span><span class="hljs-params">(Environment* env, StartExecutionCallback cb)</span> </span>&#123;
  <span class="hljs-comment">// 已省略其他运行方式，我们只看 `node index.js` 这种情况，不影响我们理解模块系统</span>
  <span class="hljs-keyword">if</span> (!first_argv.<span class="hljs-built_in">empty</span>() && first_argv != <span class="hljs-string">"-"</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">StartExecution</span>(env, <span class="hljs-string">"internal/main/run_main_module"</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>StartExecution(env, "internal/main/run_main_module")</code>这个调用中，我们会包装一个 function，并传入刚刚从 loaders 中导出的 <code>require</code> 函数，并运行 <code>[lib/internal/main/run_main_module.js](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/lib/internal/main/run_main_module.js)</code> 内的代码：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-string">'use strict'</span>;

<span class="hljs-type">const</span> &#123;
  prepareMainThreadExecution
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'internal/bootstrap/pre_execution'</span>);

<span class="hljs-built_in">prepareMainThreadExecution</span>(<span class="hljs-literal">true</span>);

<span class="hljs-built_in">markBootstrapComplete</span>();

<span class="hljs-comment">// Note: this loads the module through the ESM loader if the module is</span>
<span class="hljs-comment">// determined to be an ES module. This hangs from the CJS module loader</span>
<span class="hljs-comment">// because we currently allow monkey-patching of the module loaders</span>
<span class="hljs-comment">// in the preloaded scripts through require('module').</span>
<span class="hljs-comment">// runMain here might be monkey-patched by users in --require.</span>
<span class="hljs-comment">// <span class="hljs-doctag">XXX:</span> the monkey-patchability here should probably be deprecated.</span>
<span class="hljs-built_in">require</span>(<span class="hljs-string">'internal/modules/cjs/loader'</span>).Module.<span class="hljs-built_in">runMain</span>(process.argv[<span class="hljs-number">1</span>]);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>所谓的包装 function 并传入 <code>require</code>，伪代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">require</span>, <span class="hljs-comment">/* 其他入参 */</span></span>) &#123;
  <span class="hljs-comment">// 这里是 internal/main/run_main_module.js 的文件内容</span>
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以这里是通过<strong>内置模块</strong>的 <code>require</code> 函数加载了 <code>[lib/internal/modules/cjs/loader.js](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/lib/internal/modules/cjs/loader.js#L172)</code> 导出的 Module 对象上的 <code>runMain</code> 方法，不过我们在 <code>loader.js</code> 中并没有发现 <code>runMain</code> 函数，其实这个函数是在 <code>[lib/internal/bootstrap/pre_execution.js](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/lib/internal/bootstrap/pre_execution.js#L428)</code> 中被定义到 <code>Module</code> 对象上的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">function</span> <span class="hljs-title function_">initializeCJSLoader</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> <span class="hljs-title class_">CJSLoader</span> = <span class="hljs-built_in">require</span>(<span class="hljs-string">'internal/modules/cjs/loader'</span>);
  <span class="hljs-keyword">if</span> (!noGlobalSearchPaths) &#123;
    <span class="hljs-title class_">CJSLoader</span>.<span class="hljs-property">Module</span>.<span class="hljs-title function_">_initPaths</span>();
  &#125;
  <span class="hljs-comment">// TODO(joyeecheung): deprecate this in favor of a proper hook?</span>
  <span class="hljs-title class_">CJSLoader</span>.<span class="hljs-property">Module</span>.<span class="hljs-property">runMain</span> =
    <span class="hljs-built_in">require</span>(<span class="hljs-string">'internal/modules/run_main'</span>).<span class="hljs-property">executeUserEntryPoint</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>[lib/internal/modules/run_main.js](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/lib/internal/modules/run_main.js#L74)</code> 中找到 <code>executeUserEntryPoint</code> 方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">function</span> <span class="hljs-title function_">executeUserEntryPoint</span>(<span class="hljs-params">main = process.argv[<span class="hljs-number">1</span>]</span>) &#123;
  <span class="hljs-keyword">const</span> resolvedMain = <span class="hljs-title function_">resolveMainPath</span>(main);
  <span class="hljs-keyword">const</span> useESMLoader = <span class="hljs-title function_">shouldUseESMLoader</span>(resolvedMain);
  <span class="hljs-keyword">if</span> (useESMLoader) &#123;
    <span class="hljs-title function_">runMainESM</span>(resolvedMain || main);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// Module._load is the monkey-patchable CJS module loader.</span>
    <span class="hljs-title class_">Module</span>.<span class="hljs-title function_">_load</span>(main, <span class="hljs-literal">null</span>, <span class="hljs-literal">true</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数 <code>main</code> 即为我们传入的入口文件 <code>index.js</code>。可以看到，<code>index.js</code> 作为一个 cjs 模块应该被 <code>Module._load</code> 加载，那么 <code>_load</code>干了些什么呢？这个函数是 cjs 模块加载过程中最重要的一个函数，值得仔细阅读：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// `_load` 函数检查请求文件的缓存</span>
<span class="hljs-comment">// 1. 如果模块已经存在，返回已缓存的 exports 对象</span>
<span class="hljs-comment">// 2. 如果模块是内置模块，通过调用 `NativeModule.prototype.compileForPublicLoader()`</span>
<span class="hljs-comment">//    获取内置模块的 exports 对象，compileForPublicLoader 函数是有白名单的，只能获取公开</span>
<span class="hljs-comment">//    内置模块的 exports。</span>
<span class="hljs-comment">// 3. 以上两者皆为否，创建新的 Module 对象并保存到缓存中，然后通过它加载文件并返回其 exports。</span>

<span class="hljs-comment">// request：请求的模块，比如 `fs`，`./another-module`，'@pipcook/core' 等</span>
<span class="hljs-comment">// parent：父模块，如在 `a.js` 中 `require('b.js')`，那么这里的 request 为 'b.js',</span>
           parent 为 <span class="hljs-string">`a.js`</span> 对应的 <span class="hljs-title class_">Module</span> 对象
<span class="hljs-comment">// isMain: 除入口文件为 `true` 外，其他模块都为 `false`</span>
<span class="hljs-title class_">Module</span>.<span class="hljs-property">_load</span> = <span class="hljs-keyword">function</span>(<span class="hljs-params">request, parent, isMain</span>) &#123;
  <span class="hljs-keyword">let</span> relResolveCacheIdentifier;
  <span class="hljs-keyword">if</span> (parent) &#123;
    <span class="hljs-title function_">debug</span>(<span class="hljs-string">'Module._load REQUEST %s parent: %s'</span>, request, parent.<span class="hljs-property">id</span>);
    <span class="hljs-comment">// relativeResolveCache 是模块路径缓存，</span>
    <span class="hljs-comment">// 用于加速父模块所在目录下的所有模块请求当前模块时</span>
    <span class="hljs-comment">// 可以直接查询到实际路径，而不需要通过 _resolveFilename 查找文件</span>
    relResolveCacheIdentifier = <span class="hljs-string">`<span class="hljs-subst">$&#123;parent.path&#125;</span>\x00<span class="hljs-subst">$&#123;request&#125;</span>`</span>;
    <span class="hljs-keyword">const</span> filename = relativeResolveCache[relResolveCacheIdentifier];
    <span class="hljs-keyword">if</span> (filename !== <span class="hljs-literal">undefined</span>) &#123;
      <span class="hljs-keyword">const</span> cachedModule = <span class="hljs-title class_">Module</span>.<span class="hljs-property">_cache</span>[filename];
      <span class="hljs-keyword">if</span> (cachedModule !== <span class="hljs-literal">undefined</span>) &#123;
        <span class="hljs-title function_">updateChildren</span>(parent, cachedModule, <span class="hljs-literal">true</span>);
        <span class="hljs-keyword">if</span> (!cachedModule.<span class="hljs-property">loaded</span>)
          <span class="hljs-keyword">return</span> <span class="hljs-title function_">getExportsForCircularRequire</span>(cachedModule);
        <span class="hljs-keyword">return</span> cachedModule.<span class="hljs-property">exports</span>;
      &#125;
      <span class="hljs-keyword">delete</span> relativeResolveCache[relResolveCacheIdentifier];
    &#125;
  &#125;
<span class="hljs-comment">// 尝试查找模块文件路径，找不到模块抛出异常</span>
  <span class="hljs-keyword">const</span> filename = <span class="hljs-title class_">Module</span>.<span class="hljs-title function_">_resolveFilename</span>(request, parent, isMain);
  <span class="hljs-comment">// 如果是内置模块，从 `NativeModule` 加载</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-title class_">StringPrototypeStartsWith</span>(filename, <span class="hljs-string">'node:'</span>)) &#123;
    <span class="hljs-comment">// Slice 'node:' prefix</span>
    <span class="hljs-keyword">const</span> id = <span class="hljs-title class_">StringPrototypeSlice</span>(filename, <span class="hljs-number">5</span>);

    <span class="hljs-keyword">const</span> <span class="hljs-variable language_">module</span> = <span class="hljs-title function_">loadNativeModule</span>(id, request);
    <span class="hljs-keyword">if</span> (!<span class="hljs-variable language_">module</span>?.<span class="hljs-property">canBeRequiredByUsers</span>) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title function_">ERR_UNKNOWN_BUILTIN_MODULE</span>(filename);
    &#125;

    <span class="hljs-keyword">return</span> <span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span>;
  &#125;
<span class="hljs-comment">// 如果缓存中已存在，将当前模块 push 到父模块的 children 字段</span>
  <span class="hljs-keyword">const</span> cachedModule = <span class="hljs-title class_">Module</span>.<span class="hljs-property">_cache</span>[filename];
  <span class="hljs-keyword">if</span> (cachedModule !== <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-title function_">updateChildren</span>(parent, cachedModule, <span class="hljs-literal">true</span>);
    <span class="hljs-comment">// 处理循环引用</span>
    <span class="hljs-keyword">if</span> (!cachedModule.<span class="hljs-property">loaded</span>) &#123;
      <span class="hljs-keyword">const</span> parseCachedModule = cjsParseCache.<span class="hljs-title function_">get</span>(cachedModule);
      <span class="hljs-keyword">if</span> (!parseCachedModule || parseCachedModule.<span class="hljs-property">loaded</span>)
        <span class="hljs-keyword">return</span> <span class="hljs-title function_">getExportsForCircularRequire</span>(cachedModule);
      parseCachedModule.<span class="hljs-property">loaded</span> = <span class="hljs-literal">true</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> cachedModule.<span class="hljs-property">exports</span>;
    &#125;
  &#125;
<span class="hljs-comment">// 尝试从内置模块加载</span>
  <span class="hljs-keyword">const</span> mod = <span class="hljs-title function_">loadNativeModule</span>(filename, request);
  <span class="hljs-keyword">if</span> (mod?.<span class="hljs-property">canBeRequiredByUsers</span>) <span class="hljs-keyword">return</span> mod.<span class="hljs-property">exports</span>;

  <span class="hljs-comment">// Don't call updateChildren(), Module constructor already does.</span>
  <span class="hljs-keyword">const</span> <span class="hljs-variable language_">module</span> = cachedModule || <span class="hljs-keyword">new</span> <span class="hljs-title class_">Module</span>(filename, parent);

  <span class="hljs-keyword">if</span> (isMain) &#123;
    process.<span class="hljs-property">mainModule</span> = <span class="hljs-variable language_">module</span>;
    <span class="hljs-variable language_">module</span>.<span class="hljs-property">id</span> = <span class="hljs-string">'.'</span>;
  &#125;
<span class="hljs-comment">// 将 module 对象加入缓存</span>
  <span class="hljs-title class_">Module</span>.<span class="hljs-property">_cache</span>[filename] = <span class="hljs-variable language_">module</span>;
  <span class="hljs-keyword">if</span> (parent !== <span class="hljs-literal">undefined</span>) &#123;
    relativeResolveCache[relResolveCacheIdentifier] = filename;
  &#125;

  <span class="hljs-comment">// 尝试加载模块，如果加载失败则删除缓存中的 module 对象，</span>
  <span class="hljs-comment">// 同时删除父模块的 children 内的 module 对象。</span>
  <span class="hljs-keyword">let</span> threw = <span class="hljs-literal">true</span>;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-variable language_">module</span>.<span class="hljs-title function_">load</span>(filename);
    threw = <span class="hljs-literal">false</span>;
  &#125; <span class="hljs-keyword">finally</span> &#123;
    <span class="hljs-keyword">if</span> (threw) &#123;
      <span class="hljs-keyword">delete</span> <span class="hljs-title class_">Module</span>.<span class="hljs-property">_cache</span>[filename];
      <span class="hljs-keyword">if</span> (parent !== <span class="hljs-literal">undefined</span>) &#123;
        <span class="hljs-keyword">delete</span> relativeResolveCache[relResolveCacheIdentifier];
        <span class="hljs-keyword">const</span> children = parent?.<span class="hljs-property">children</span>;
        <span class="hljs-keyword">if</span> (<span class="hljs-title class_">ArrayIsArray</span>(children)) &#123;
          <span class="hljs-keyword">const</span> index = <span class="hljs-title class_">ArrayPrototypeIndexOf</span>(children, <span class="hljs-variable language_">module</span>);
          <span class="hljs-keyword">if</span> (index !== -<span class="hljs-number">1</span>) &#123;
            <span class="hljs-title class_">ArrayPrototypeSplice</span>(children, index, <span class="hljs-number">1</span>);
          &#125;
        &#125;
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> &&
               !<span class="hljs-title function_">isProxy</span>(<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span>) &&
               <span class="hljs-title class_">ObjectGetPrototypeOf</span>(<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span>) ===
                 <span class="hljs-title class_">CircularRequirePrototypeWarningProxy</span>) &#123;
      <span class="hljs-title class_">ObjectSetPrototypeOf</span>(<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span>, <span class="hljs-title class_">ObjectPrototype</span>);
    &#125;
  &#125;
<span class="hljs-comment">// 返回 exports 对象</span>
  <span class="hljs-keyword">return</span> <span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>module</code> 对象上的 <code>[load](https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/lib/internal/modules/cjs/loader.js#L963)</code> 函数用于执行一个模块的加载：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title class_">Module</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">load</span> = <span class="hljs-keyword">function</span>(<span class="hljs-params">filename</span>) &#123;
  <span class="hljs-title function_">debug</span>(<span class="hljs-string">'load %j for module %j'</span>, filename, <span class="hljs-variable language_">this</span>.<span class="hljs-property">id</span>);

  <span class="hljs-title function_">assert</span>(!<span class="hljs-variable language_">this</span>.<span class="hljs-property">loaded</span>);
  <span class="hljs-variable language_">this</span>.<span class="hljs-property">filename</span> = filename;
  <span class="hljs-variable language_">this</span>.<span class="hljs-property">paths</span> = <span class="hljs-title class_">Module</span>.<span class="hljs-title function_">_nodeModulePaths</span>(path.<span class="hljs-title function_">dirname</span>(filename));

  <span class="hljs-keyword">const</span> extension = <span class="hljs-title function_">findLongestRegisteredExtension</span>(filename);
  <span class="hljs-comment">// allow .mjs to be overridden</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-title class_">StringPrototypeEndsWith</span>(filename, <span class="hljs-string">'.mjs'</span>) && !<span class="hljs-title class_">Module</span>.<span class="hljs-property">_extensions</span>[<span class="hljs-string">'.mjs'</span>])
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title function_">ERR_REQUIRE_ESM</span>(filename, <span class="hljs-literal">true</span>);

  <span class="hljs-title class_">Module</span>.<span class="hljs-property">_extensions</span>[extension](<span class="hljs-variable language_">this</span>, filename);
  <span class="hljs-variable language_">this</span>.<span class="hljs-property">loaded</span> = <span class="hljs-literal">true</span>;

  <span class="hljs-keyword">const</span> esmLoader = asyncESM.<span class="hljs-property">esmLoader</span>;
  <span class="hljs-comment">// Create module entry at load time to snapshot exports correctly</span>
  <span class="hljs-keyword">const</span> <span class="hljs-built_in">exports</span> = <span class="hljs-variable language_">this</span>.<span class="hljs-property">exports</span>;
  <span class="hljs-comment">// Preemptively cache</span>
  <span class="hljs-keyword">if</span> ((<span class="hljs-variable language_">module</span>?.<span class="hljs-property">module</span> === <span class="hljs-literal">undefined</span> ||
       <span class="hljs-variable language_">module</span>.<span class="hljs-property">module</span>.<span class="hljs-title function_">getStatus</span>() < kEvaluated) &&
      !esmLoader.<span class="hljs-property">cjsCache</span>.<span class="hljs-title function_">has</span>(<span class="hljs-variable language_">this</span>))
    esmLoader.<span class="hljs-property">cjsCache</span>.<span class="hljs-title function_">set</span>(<span class="hljs-variable language_">this</span>, <span class="hljs-built_in">exports</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际的加载动作是在 <code>Module._extensions[extension](this, filename);</code> 中进行的，根据扩展名的不同，会有不同的加载策略：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fblob%2F881174e016d6c27b20c70111e6eae2296b6c6293%2Flib%2Finternal%2Fmodules%2Fcjs%2Floader.js%23L1104" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/lib/internal/modules/cjs/loader.js#L1104" ref="nofollow noopener noreferrer">.js</a>：调用 <code>fs.readFileSync</code> 读取文件内容，将文件内容包在 wrapper 中，需要注意的是，这里的 <code>require</code> 是 <code>Module.prototype.require</code> 而非内置模块的 <code>require</code> 方法。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> wrapper = [
  <span class="hljs-string">'(function (exports, require, module, __filename, __dirname) &#123; '</span>,
  <span class="hljs-string">'\n&#125;);'</span>,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fblob%2F881174e016d6c27b20c70111e6eae2296b6c6293%2Flib%2Finternal%2Fmodules%2Fcjs%2Floader.js%23L1152" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/lib/internal/modules/cjs/loader.js#L1152" ref="nofollow noopener noreferrer">.json</a>：调用 <code>fs.readFileSync</code> 读取文件内容，并转换为对象。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fblob%2F881174e016d6c27b20c70111e6eae2296b6c6293%2Flib%2Finternal%2Fmodules%2Fcjs%2Floader.js%23L1170" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nodejs/node/blob/881174e016d6c27b20c70111e6eae2296b6c6293/lib/internal/modules/cjs/loader.js#L1170" ref="nofollow noopener noreferrer">.node</a>：调用 <code>dlopen</code> 打开 node 扩展。</li>
</ul>
<p>而 <code>Module.prototype.require</code> 函数也是调用了静态方法 <code>Module._load</code>实现模块加载的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title class_">Module</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">require</span> = <span class="hljs-keyword">function</span>(<span class="hljs-params">id</span>) &#123;
  <span class="hljs-title function_">validateString</span>(id, <span class="hljs-string">'id'</span>);
  <span class="hljs-keyword">if</span> (id === <span class="hljs-string">''</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title function_">ERR_INVALID_ARG_VALUE</span>(<span class="hljs-string">'id'</span>, id,
                                    <span class="hljs-string">'must be a non-empty string'</span>);
  &#125;
  requireDepth++;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-title class_">Module</span>.<span class="hljs-title function_">_load</span>(id, <span class="hljs-variable language_">this</span>, <span class="hljs-comment">/* isMain */</span> <span class="hljs-literal">false</span>);
  &#125; <span class="hljs-keyword">finally</span> &#123;
    requireDepth--;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">总结</h1>
<p>看到这里，cjs 模块的加载过程已经基本清晰了：</p>
<ol>
<li>初始化 node，加载 NativeModule，用于加载所有的内置的 js 和 c++ 模块</li>
<li>运行内置模块 <code>run_main</code></li>
<li>在 <code>run_main</code> 中引入用户模块系统 <code>module</code></li>
<li>通过 <code>module</code> 的 <code>_load</code> 方法加载入口文件，在加载时通过传入 <code>module.require</code> 和 <code>module.exports</code> 等让入口文件可以正常 <code>require</code> 其他依赖模块并递归让整个依赖树被完整加载。</li>
</ol>
<p>在清楚了 cjs 模块加载的完整流程之后，我们还可以顺着这条链路阅读其他代码，比如 <code>global</code> 变量的初始化，esModule 的管理方式等，更深入地理解 node 内的各种实现。</p></div>  
</div>
            