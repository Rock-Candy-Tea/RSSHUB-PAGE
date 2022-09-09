
---
title: 'Flutter学习 - Bloc - 05 倒计时'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d314995cf3864b9588c7784d018131f3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Thu, 18 Aug 2022 02:02:41 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d314995cf3864b9588c7784d018131f3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>携手创作，共同成长！这是我参与「掘金日新计划 · 8 月更文挑战」的第19天，<a href="https://juejin.cn/post/7123120819437322247" title="https://juejin.cn/post/7123120819437322247" target="_blank">点击查看活动详情</a></p>
<blockquote>
<p>本文主要使用bloc 模式创建一个倒计时，包括暂停重置等状态</p>
</blockquote>
<h2 data-id="heading-0">1. 分析</h2>
<p>首先就是如下图所示，是一个倒计时，提供了开始，暂停，继续，重置几种状态，同时还有一个完成状态当，倒计时结束后达到重置效果。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d314995cf3864b9588c7784d018131f3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="iShot_2022-08-18_15.26.02.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时有一个计时器，我们可以订阅它，之后发送我们的秒数。这个时候可以使用<code>stream</code>流就行执行。对于UI方面，我们会根据状态展示不同按钮。</p>
<h2 data-id="heading-1">2. periodic</h2>
<p>我们使用<code>Stream</code>初始化一个流，每秒执行1次，执行次数通过方法传进来，之后转化下剩余秒数。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TimeTicker</span></span>&#123;
  <span class="hljs-keyword">const</span> TimeTicker();

  Stream<<span class="hljs-built_in">int</span>> tick(&#123;<span class="hljs-keyword">required</span> <span class="hljs-built_in">int</span> ticks&#125;)&#123;
    <span class="hljs-keyword">return</span> Stream.periodic(<span class="hljs-keyword">const</span> <span class="hljs-built_in">Duration</span>(seconds: <span class="hljs-number">1</span>),(count) => ticks - count <span class="hljs-number">-1</span>).take(ticks);
  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里对于必填的参数我们使用<code>required</code>修饰，这样明确语意</p>
<h2 data-id="heading-2">3. State</h2>
<p>我们之前分析了计时器的几种状态，因此我们可以设置几种状态</p>
<ul>
<li><code>CalculateInitial</code>：准备从指定的时间开始倒计时，用户可以进行倒计时。</li>
<li><code>TimerRunInProgress</code>：正在倒计时中，暂停和重置计时器并且可以看到剩余的时间。</li>
<li><code>TimerRunPause</code>：暂停，恢复倒计时和重置计时器。</li>
<li><code>TimerRunComplete</code>：结束，重置计时器。</li>
</ul>
<pre><code class="hljs language-scala copyable" lang="scala">part of 'calculate_bloc.dart';

<span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CalculateState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Equatable</span> </span>&#123;
  <span class="hljs-keyword">final</span> int duration;
  const <span class="hljs-type">CalculateState</span>(<span class="hljs-keyword">this</span>.duration);
  <span class="hljs-meta">@override</span>
  <span class="hljs-type">List</span><<span class="hljs-type">Object</span>> get props => [duration];
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CalculateInitial</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">CalculateState</span> </span>&#123;
  const <span class="hljs-type">CalculateInitial</span>(<span class="hljs-keyword">super</span>.duration);
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TimerRunPause</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">CalculateState</span> </span>&#123;
  const <span class="hljs-type">TimerRunPause</span>(<span class="hljs-keyword">super</span>.duration);

&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TimerRunInProgress</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">CalculateState</span> </span>&#123;

  const <span class="hljs-type">TimerRunInProgress</span>(<span class="hljs-keyword">super</span>.duration);

&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TimerRunComplete</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">CalculateState</span> </span>&#123;
  const <span class="hljs-type">TimerRunComplete</span>() : <span class="hljs-keyword">super</span>(<span class="hljs-number">0</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意所有的<code>states</code>都继承自抽象基类<code>CalculateState</code>，它有一个duration属性。这是因为不管<code>TimerBloc</code>在哪里，我们都想知道还剩余多少时间。另外<code>CalculateState</code>还继承了<code>Equatable</code>用于确保如果有相同状态不会再次触发重建。</p>
<h2 data-id="heading-3">4. Event</h2>
<p>对于我们Event事件驱动，我们对应state也有相对应的event</p>
<ul>
<li><code>TimerStarted</code>：通知Bloc开始计时。</li>
<li><code>TimerPaused</code>：通知Bloc暂停。</li>
<li><code>TimerResumed</code>：通知Bloc恢复计时。</li>
<li><code>TimerReset</code>：通知Bloc重置计时器到原来的状态。</li>
<li><code>TimerTicked</code>：通知Bloc一个tick已经发生，需要更新它对应的状态。</li>
</ul>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-keyword">part</span> of <span class="hljs-string">'calculate_bloc.dart'</span>;

<span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CalculateEvent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Equatable</span> </span>&#123;
  <span class="hljs-keyword">const</span> CalculateEvent();
  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">List</span><<span class="hljs-built_in">Object</span>> <span class="hljs-keyword">get</span> props => [];
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TimerStarted</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">CalculateEvent</span> </span>&#123;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">int</span> duration;

  <span class="hljs-keyword">const</span> TimerStarted(&#123;<span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.duration &#125;);

&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TimerTicked</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">CalculateEvent</span> </span>&#123;
  <span class="hljs-keyword">const</span> TimerTicked(&#123;<span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.duration&#125;);
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">int</span> duration;

  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">List</span><<span class="hljs-built_in">Object</span>> <span class="hljs-keyword">get</span> props => [duration];
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TimerPaused</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">CalculateEvent</span> </span>&#123;
  <span class="hljs-keyword">const</span> TimerPaused();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TimerResumed</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">CalculateEvent</span> </span>&#123;
  <span class="hljs-keyword">const</span> TimerResumed();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TimerReset</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">CalculateEvent</span> </span>&#123;
  <span class="hljs-keyword">const</span> TimerReset();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">5. Bloc</h2>
<p>我们这里实现逻辑,针对event，处理逻辑发送对应的state</p>
<h3 data-id="heading-5">5.1 初始化</h3>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">part</span> <span class="hljs-string">'calculate_event.dart'</span>;
<span class="hljs-keyword">part</span> <span class="hljs-string">'calculate_state.dart'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CalculateBloc</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Bloc</span><<span class="hljs-title">CalculateEvent</span>, <span class="hljs-title">CalculateState</span>> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> <span class="hljs-built_in">int</span> _duration = <span class="hljs-number">60</span>;
  <span class="hljs-keyword">final</span> TimeTicker _ticker;

  StreamSubscription<<span class="hljs-built_in">int</span>>? _tickerStreamSubscription;
  CalculateBloc(&#123;<span class="hljs-keyword">required</span> TimeTicker ticker&#125;) :_ticker = ticker , <span class="hljs-keyword">super</span>(<span class="hljs-keyword">const</span> CalculateInitial(_duration)) &#123;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们定义倒计时和计时器，同时定义一个订阅者用于订阅Stream，从而控制我们的Stream是否暂停，继续以及销毁。</p>
<p>我们关闭的时候需要，关闭订阅</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-comment"><span class="hljs-doctag">///</span> 关闭的时候 关闭订阅</span>
@override
<span class="hljs-function">Future<<span class="hljs-keyword">void</span>> <span class="hljs-title">close</span>() <span class="hljs-keyword">async</span></span> &#123;
  _tickerStreamSubscription?.cancel();
  <span class="hljs-keyword">return</span> super.close();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">5.2 TimerStarted</h3>
<p>如果<code>CalculateBloc</code>收到<code>TimerStarted</code>事件，它会发送一个带有开始时间的<code>TimerRunInProgress</code>状态。此外，如果已经打开了<code>_tickerSubscription</code>我们需要取消它释放内存。我们也需要在<code>TimerBloc</code>中重载<code>close</code>方法，当<code>TimerBloc</code>被关闭的时候能取消<code>_tickerSubscription </code>。最后我们监听<code>_ticker.tick</code>流并且在每个触发时间我们添加一个包含剩余时间的<code>TimerTicked</code>事件。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart">
<span class="hljs-comment">/// <span class="markdown">开始：1。发送一个带有开始时间的状态</span></span>
<span class="hljs-keyword">void</span> _onStarted(TimerStarted event, Emitter<CalculateState> emit) &#123;

  emit(TimerRunInProgress(event.duration));
  _tickerStreamSubscription?.cancel();
  _tickerStreamSubscription = _ticker
  .tick(ticks: event.duration)
  .listen((event) => add(TimerTicked(duration: event)));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">5.3 TimerTicked</h3>
<p>每次接收到<code>TimerTicked</code>事件，如果剩余时间大于0，我们需要发送一个带有新的剩余时间的<code>TimerRunInProgress</code>事件来更新状态。否则，如果剩余时间等于0，那么倒计时已经结束，我们需要发送<code>TimerRunComplete</code>状态。</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-comment"><span class="hljs-doctag">///</span> 计时中，判断是否剩余时间</span>
<span class="hljs-keyword">void</span> _onTicked(TimerTicked <span class="hljs-keyword">event</span>, Emitter<CalculateState> emit)&#123;

  emit(<span class="hljs-keyword">event</span>.duration><span class="hljs-number">0</span> ? TimerRunInProgress(<span class="hljs-keyword">event</span>.duration): <span class="hljs-function"><span class="hljs-keyword">const</span> <span class="hljs-title">TimerRunComplete</span>())</span>;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">5.4 TimerPaused</h3>
<p>在<code>_onPaused</code>中如果我们<code>TimerBloc</code>中的状态是<code>TimerRunInProgress</code>，我们可以暂停<code>_tickerSubscription</code>并且发送一个带有当前时间的<code>TimerRunPause</code>状态。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-comment">/// <span class="markdown"> 暂停，判断当时是否state为TimerRunInprogress类型，之后暂停订阅，发送暂停state</span></span>
<span class="hljs-keyword">void</span> _onPaused(TimerPaused event, Emitter<CalculateState> emit) &#123;
  <span class="hljs-keyword">if</span>( state <span class="hljs-keyword">is</span> TimerRunInProgress) &#123;
    _tickerStreamSubscription?.pause();
    emit(TimerRunPause(state.duration));
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">5.5 TimerResumed</h3>
<p><code>TimerResumed</code>事件处理和<code>TimerPaused</code>事件的处理非常相似。如果<code>CalculateBloc</code>的<code>state</code>是<code>TimerRunPause</code>并且它接收到一个<code>TimerResumed</code>事件，它恢复<code>_tickerSubscription</code>并且发送一个带有当前时间的<code>TimerRunInProgress</code>状态。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-comment">/// <span class="markdown">恢复，我们判断当前state为暂停状态后，进行恢复jiant</span></span>
<span class="hljs-keyword">void</span> _onResumed(TimerResumed event, Emitter<CalculateState> emit)&#123;
  <span class="hljs-keyword">if</span>( state <span class="hljs-keyword">is</span> TimerRunPause) &#123;
    _tickerStreamSubscription?.resume();
    emit(TimerRunInProgress(state.duration));
  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">5.6 TimerReset</h3>
<p>如果<code>CalculateBloc</code>接收到一个<code>TimerReset</code>事件，它需要取消当前的<code>_tickerSubscription</code>这样它就不会被计时器通知，并且发送一个带有初始时间的<code>CalculateInitial</code>状态。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-comment">/// <span class="markdown">重置,初始化</span></span>
<span class="hljs-keyword">void</span> _onReset(TimerReset event ,Emitter<CalculateState> emit) &#123;

  _tickerStreamSubscription?.cancel();
  emit(<span class="hljs-keyword">const</span> CalculateInitial(_duration));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">6. UI</h2>
<p>我们通过BlocProvider关联我们的页面和bloc</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TimerPage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> TimerPage(&#123;Key? key&#125;) : <span class="hljs-keyword">super</span>(key: key);


  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
   <span class="hljs-keyword">return</span> BlocProvider(
       create: (_) => CalculateBloc(ticker: <span class="hljs-keyword">const</span> TimeTicker()),
       child: <span class="hljs-keyword">const</span> TimerView(),

   );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">6.1 TimerPage</h3>
<p>根据布局我们使用Stack，方便我们添加背景什么的。</p>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TimerView</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> <span class="hljs-variable constant_">TimerView</span>(&#123;Key? key&#125;) : <span class="hljs-title function_ invoke__">super</span>(<span class="hljs-attr">key</span>: key);
  @override
  Widget <span class="hljs-title function_ invoke__">build</span>(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-title function_ invoke__">Scaffold</span>(
      <span class="hljs-attr">appBar</span>: <span class="hljs-title function_ invoke__">AppBar</span>(<span class="hljs-attr">title</span>: <span class="hljs-keyword">const</span> <span class="hljs-title function_ invoke__">Text</span>(<span class="hljs-string">'倒计时'</span>)),
      <span class="hljs-attr">body</span>: <span class="hljs-title function_ invoke__">Stack</span>(
        <span class="hljs-attr">children</span>: [
          <span class="hljs-title function_ invoke__">Column</span>(
            <span class="hljs-attr">mainAxisAlignment</span>: MainAxisAlignment.center,
            <span class="hljs-attr">crossAxisAlignment</span>: CrossAxisAlignment.center,
            <span class="hljs-attr">children</span>: <span class="hljs-keyword">const</span> <Widget>[
              <span class="hljs-title function_ invoke__">Padding</span>(
                <span class="hljs-attr">padding</span>: EdgeInsets.<span class="hljs-title function_ invoke__">symmetric</span>(<span class="hljs-attr">vertical</span>: <span class="hljs-number">100.0</span>),
                <span class="hljs-attr">child</span>: <span class="hljs-title function_ invoke__">Center</span>(<span class="hljs-attr">child</span>: <span class="hljs-title function_ invoke__">TimerText</span>()),
              ),
              <span class="hljs-title function_ invoke__">Actions</span>(),
            ],
          ),
        ],
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">6.2 TimerText</h3>
<p>通过context获取Bloc，之后展示在Text中</p>
<pre><code class="hljs language-Dart copyable" lang="Dart">
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TimerText</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> TimerText(&#123;Key? key&#125;) : <span class="hljs-keyword">super</span>(key: key);
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">final</span> duration = context.select((CalculateBloc bloc) => bloc.state.duration);
    <span class="hljs-keyword">final</span> minutesStr =
    ((duration / <span class="hljs-number">60</span>) % <span class="hljs-number">60</span>).floor().toString().padLeft(<span class="hljs-number">2</span>, <span class="hljs-string">'0'</span>);
    <span class="hljs-keyword">final</span> secondsStr = (duration % <span class="hljs-number">60</span>).floor().toString().padLeft(<span class="hljs-number">2</span>, <span class="hljs-string">'0'</span>);
    <span class="hljs-keyword">return</span> Text(
      <span class="hljs-string">'<span class="hljs-subst">$minutesStr</span>:<span class="hljs-subst">$secondsStr</span>'</span>,
      style: Theme.of(context).textTheme.headline1,
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">6.3 Actions</h3>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">class</span> <span class="hljs-title">Actions</span> <span class="hljs-title">extends</span> <span class="hljs-title">StatelessWidget</span> &#123;
  <span class="hljs-function"><span class="hljs-keyword">const</span> <span class="hljs-title">Actions</span>(<span class="hljs-params">&#123;Key? key&#125;</span>) : <span class="hljs-title">super</span>(<span class="hljs-params">key: key</span>)</span>;
  @override
  <span class="hljs-function">Widget <span class="hljs-title">build</span>(<span class="hljs-params">BuildContext context</span>)</span> &#123;
    <span class="hljs-keyword">return</span> BlocBuilder<CalculateBloc, CalculateState>(
      buildWhen: (prev, state) => prev.runtimeType != state.runtimeType,
      builder: (context, state) &#123;
        <span class="hljs-keyword">return</span> Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            <span class="hljs-keyword">if</span> (state <span class="hljs-keyword">is</span> CalculateInitial) ...[
              FloatingActionButton(
                heroTag: <span class="hljs-literal">null</span>,
                child: <span class="hljs-function"><span class="hljs-keyword">const</span> <span class="hljs-title">Icon</span>(<span class="hljs-params">Icons.play_arrow</span>),
                onPressed: ()</span> => context
                    .read<CalculateBloc>()
                    .<span class="hljs-keyword">add</span>(TimerStarted(duration: state.duration)),
              ),
            ],
            <span class="hljs-keyword">if</span> (state <span class="hljs-keyword">is</span> TimerRunInProgress) ...[
              FloatingActionButton(
                heroTag: <span class="hljs-literal">null</span>,
                child: <span class="hljs-function"><span class="hljs-keyword">const</span> <span class="hljs-title">Icon</span>(<span class="hljs-params">Icons.pause</span>),
                onPressed: ()</span> => context.read<CalculateBloc>().<span class="hljs-keyword">add</span>(<span class="hljs-function"><span class="hljs-keyword">const</span> <span class="hljs-title">TimerPaused</span>()),
              ),
              <span class="hljs-title">FloatingActionButton</span>(<span class="hljs-params">
                heroTag: <span class="hljs-literal">null</span>,
                child: <span class="hljs-keyword">const</span> Icon(Icons.replay</span>),
                onPressed: ()</span> => context.read<CalculateBloc>().<span class="hljs-keyword">add</span>(<span class="hljs-function"><span class="hljs-keyword">const</span> <span class="hljs-title">TimerReset</span>()),
              ),
            ],
            <span class="hljs-title">if</span> (<span class="hljs-params">state <span class="hljs-keyword">is</span> TimerRunPause</span>) ...[
              <span class="hljs-title">FloatingActionButton</span>(<span class="hljs-params">
                heroTag: <span class="hljs-literal">null</span>,
                child: <span class="hljs-keyword">const</span> Icon(Icons.play_arrow</span>),
                onPressed: ()</span> => context.read<CalculateBloc>().<span class="hljs-keyword">add</span>(<span class="hljs-function"><span class="hljs-keyword">const</span> <span class="hljs-title">TimerResumed</span>()),
              ),
              <span class="hljs-title">FloatingActionButton</span>(<span class="hljs-params">
                heroTag: <span class="hljs-literal">null</span>,
                child: <span class="hljs-keyword">const</span> Icon(Icons.replay</span>),
                onPressed: ()</span> => context.read<CalculateBloc>().<span class="hljs-keyword">add</span>(<span class="hljs-function"><span class="hljs-keyword">const</span> <span class="hljs-title">TimerReset</span>()),
              ),
            ],
            <span class="hljs-title">if</span> (<span class="hljs-params">state <span class="hljs-keyword">is</span> TimerRunComplete</span>) ...[
              <span class="hljs-title">FloatingActionButton</span>(<span class="hljs-params">
                heroTag: <span class="hljs-literal">null</span>,
                child: <span class="hljs-keyword">const</span> Icon(Icons.replay</span>),
                onPressed: ()</span> => context.read<CalculateBloc>().<span class="hljs-keyword">add</span>(<span class="hljs-function"><span class="hljs-keyword">const</span> <span class="hljs-title">TimerReset</span>()),
              ),
            ]
          ],
        )</span>;
      &#125;,
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Actions</code>小部件只是另一个<code>StatelessWidget</code>，每当我们获取到一个新的TimerState时，它使用<code>BlocBuilder</code>来重建UI。<code>Actions</code>使用<code>context.read<TimerBloc>()</code>访问<code>TimerBloc</code>实例并且基于当前<code>TimerBloc</code>状态返回不同的<code>FloatingActionButtons</code>。每个<code>FloatingActionButtons</code>的<code>onPressed</code>回调中都添加一个事件通知<code>CalculateBloc</code>。</p>
<p>如果你想细微的控制，当<code>builder</code>方法被调用的时候你可以提供一个可选的<code>buildWhen</code>到<code>BlocBuilder</code>。<code>buildWhen</code>携带前一个bloc状态和当前的bloc状态，并且返回一个<code>boolean</code>值。如果<code>buildWhen</code>返回<code>true</code>，将调用带有<code>state</code>的<code>builder</code>并且重建组件。如果<code>buildWhen</code>返回<code>false</code>，带有<code>state</code>的<code>builder</code>将不会被调用并且不会被重建。</p>
<p>这种情况下，我们不想每次都重新构建<code>Actions</code>组件，这样效率很低。我们只想在<code>TimeState</code>的<code>runtimeType</code>改变的时候(TimerInitial => TimerRunInProgress, TimerRunInProgress => TimerRunPause, 等…)重建 <code>Actions</code>。</p>
<h2 data-id="heading-15">7. 小结</h2>
<p>对于一些多状态的场景，我们可以<code>继承抽象类</code>，每种状态代表一种情况，都持有抽象类参数<code>duration</code>。与之对应的是<code>event</code>，通过<code>event</code>发送不同state刷新界面。同时我们通过<code>stream</code>可以监听，根据传递状态做出对应操作，最后做到了 <code>event-state</code> 一一对应。</p></div>  
</div>
            