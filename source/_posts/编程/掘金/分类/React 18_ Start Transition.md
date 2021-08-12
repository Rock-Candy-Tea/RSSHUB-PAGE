
---
title: 'React 18_ Start Transition'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://tech-proxy.bytedance.net/tos/images/1627395451171_9c797380996f87eeee5e51c3fad96ac0.gif'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 17:58:48 GMT
thumbnail: 'https://tech-proxy.bytedance.net/tos/images/1627395451171_9c797380996f87eeee5e51c3fad96ac0.gif'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Do you know!?!</p>
<h2 data-id="heading-0">Javascript is a single-threaded language</h2>
<p>Yeah, you read it correctly, <strong>Javascript is a single-threaded language</strong>. Surprised!!! 🥳 🎉</p>
<p>Javascript has one call stack and one memory heap. All events will be put into this stack, execute one by one by ordering.</p>
<p>In other words, Javascript's stack executes <strong>Synchronous</strong>!
<img src="https://tech-proxy.bytedance.net/tos/images/1627395451171_9c797380996f87eeee5e51c3fad96ac0.gif" alt="animation (2).gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Thank Javascript engine (V8, Spidermonkey, JavaScriptCore, etc...) even though Javascript is a single-threaded language but makes Javascript super fast, sometimes make some people misunderstanding.</p>
<p>Wait!?! 🤔... but Javascript can do <strong>Asynchronous</strong> as well</p>
<p>Yeah, you are right. Technically it is still same stack but with different order, example:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Javascript'</span>)
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Synchronous'</span>)
&#125;, <span class="hljs-number">1000</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'is'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>So the result is ...</p>
<pre><code class="hljs language-js copyable" lang="js">Javascript
is
<span class="hljs-literal">undefined</span>
Synchronous
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Wait ... what?!? 😳😵‍💫 Where did <code>undefined</code> come in from? And why <code>Syncronous</code> is in the last.</p>
<p>So <code>setTimeout</code> tells Javascript is that "Hey, I have event but I also want execute this event after 1s". So Javascript will execute <code>setTimeout</code> in the last.</p>
<p>After executing <code>console.log('Javascript')</code> and <code>console.log('is)'</code></p>
<ul>
<li><strong>Javascript</strong>: <code>setTimeout</code> "Are you ready?"</li>
<li><strong>setTimeout</strong>: Not yet, need to wait for 1 second</li>
<li><strong>Javascript</strong>: Okay. When you are ready, do let me know, trigger the callback.</li>
<li><strong>Javascript</strong>: <em>undefined</em> as default.</li>
</ul>
<p>1 second later</p>
<ul>
<li><strong>setTimeout</strong>: Okay, I am ready. Please execute</li>
<li><strong>Javascript</strong>: Synchronous
<img src="https://tech-proxy.bytedance.net/tos/images/1627435438802_67424061cbf789f7e42719d0fc3db46e.gif" alt="animation (5).gif" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
<p>Well, ... you might think "hmm, it is a bit strange, but I got it" but why it relates to <strong>startTransition</strong>? 🤔</p>
<p>The answer is Yes, it is related.</p>
<h2 data-id="heading-1">startTransition: <em>Urgent</em> event and Not <em>Urgent</em> event</h2>
<p>As the user types input search, the user expects 2 things to happen</p>
<ul>
<li>Words are typed should show immediately - urgent event</li>
<li>The search result can show after typing - not urgent event</li>
</ul>
<p>In other words, urgent events are those events we want to execute immediately, and not urgent events are those events that can execute after urgent events finish.</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Urgent event</span>
setInputValue(value)
....
....
<span class="hljs-comment">// Not urgent event</span>
setSearchData(data)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>So why it matters because Javascript is a single-threaded language, when one event executes the rest will be "frozen", in the status "waiting".</p>
<p>Before React 18, all events in React are urgent, which means it will execute one by one as Javascript does. However, it is not the "best" user experience in some scenarios.</p>
<p>Back to our example</p>
<pre><code class="hljs language-js copyable" lang="js">setInputValue(value)
...
setSearchData(data)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>user</strong>: type 'A' into Input field</li>
<li><strong>setInputValue</strong>: set value 'A' into Input and render ✅</li>
<li><strong>setSearchData</strong>: set search data by value 'A' and render but it takes a bit time 💻</li>
<li><strong>user</strong>: type 'B' into Input field</li>
<li><strong>setInputValue</strong>: set value 'AB' into Input and render but 🛑</li>
<li><strong>Javascript</strong>: Please wait for <strong>setSearchData</strong> finish first ✋</li>
<li><strong>user</strong>: Feel a bit laggy, value 'B' doesn't show immediately 🤔</li>
<li><strong>Javascript</strong>: Okay <strong>setSeachDate</strong> finishes, <strong>setInputValue</strong> you can go ahead. ✅</li>
<li><strong>setInputValue</strong>: set value 'AB' into Input and render</li>
<li><strong>setSearchData</strong>: set search data by value 'AB' and render but it takes a bit time</li>
</ul>
<p><img src="https://tech-proxy.bytedance.net/tos/images/1627438029076_bd1d010a774aee1fc0097dc4ee9992db.gif" alt="ezgif.com-gif-maker (5).gif" loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fobjective-wildflower-rbykk%3Ffile%3D%2Fsrc%2FApp.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/objective-wildflower-rbykk?file=/src/App.js" ref="nofollow noopener noreferrer">Playground</a></p>
<p>So to enhance the user experience in those scenarios, React provides <strong>startTransition</strong> feature to let us as developers decide which event is urgent, which event is not urgent. In our case, <code>setInputValue</code> is urgent and <code>setSearchDate</code> is not urgent.</p>
<pre><code class="hljs language-js copyable" lang="js">setInputValue(value)
...
startTransition(<span class="hljs-function">() =></span> &#123;
  setSearchData(data)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://tech-proxy.bytedance.net/tos/images/1627438385339_e08519e8af2491335bc130dc6d9db390.gif" alt="ezgif.com-gif-maker (6).gif" loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fmodest-sky-537xq%3Ffile%3D%2Fsrc%2FApp.js%3A282-305" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/modest-sky-537xq?file=/src/App.js:282-305" ref="nofollow noopener noreferrer">Playground</a></p>
<p>Well, you might see a bit hard to see different but there are 😅. However, the main idea is to explain the story behind it.</p>
<p>Here are more examples for your references:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F65" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/65" ref="nofollow noopener noreferrer">github.com/reactwg/rea…</a></p>
<h2 data-id="heading-2">startTransition is different setTimeout</h2>
<p>As we discussed above, <code>setTimeout</code> is <strong>Asynchronous</strong> but <code>startTransition</code> is <strong>synchronous</strong>.
<img src="https://tech-proxy.bytedance.net/tos/images/1627439591667_95b130df7d26e64a4ef8925cedd0555e.gif" alt="animation (6).gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>We can see that <code>startTransition</code> doesn't change the order of events, it is still there but it will "wait" urgent events to finish then it will execute, it is likemagic🤯. The React Core team makes it happen. 🎉</p>
<p><strong>Asynchronous</strong> is hard, you have been told that we need to <code>clearTimeout</code> whenever we use <code>setTimeout</code>, it might make Javascript confused and we need to set the time when it executes and as humans, we won't ever know what is the exact time to execute because different scenarios we might different time and we only set at one.</p>
<p>You watch <strong>Loki</strong>, if we don't manage <strong>Asynchronous</strong> well, it might cause "<strong>multiverse</strong>" 😱
<img src="https://tech-proxy.bytedance.net/tos/images/1627440047398_b199b378072a14c4defb2a7ca65d184e.gif" alt="tenor.gif" loading="lazy" referrerpolicy="no-referrer">
<img src="https://tech-proxy.bytedance.net/tos/images/1627440122758_f5b0738cd2c9ef393eb50a48220c0925.gif" alt="55964ad6b687ea1a80217f6c0518985c.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">Small changes sometimes will make big different</h2>
<p>When you read until here, I hope you get the concept of <code>startTransition</code>, the story behind it.</p>
<p>Generally speaking, you might not need to use <code>startTransition</code> in your projects especially if you don't work on enterprise projects. However, when Front End World is getting complex and our application becomes super application, <code>startTransition</code> will play a big role there. As mentioned some of my articles that React Core Team starts invest in animation with <code>startTransition</code>, <code>SRR</code>, <code>Suspense</code>, ... are complementary, it will be good for you to know each part how does it work 🙂</p>
<p><strong>Disclaimer</strong> Because <code>startTransition</code> is very new, I could be wrong about some parts of it, free feel to leave the comment to correct me.</p>
<p><strong>References:</strong></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F41" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/41" ref="nofollow noopener noreferrer">github.com/reactwg/rea…</a></li>
</ul>
<p>Hope you enjoy the article, good luck!!!</p></div>  
</div>
            