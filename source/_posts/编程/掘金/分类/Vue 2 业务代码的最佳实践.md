
---
title: 'Vue 2 业务代码的最佳实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7115'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 11:48:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=7115'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0">记录一下Vue 2 业务代码的最佳实践</h5>
<h5 data-id="heading-1">1. 禁用Watcher</h5>
<p>为什么禁用Watcher？
在我看来，Watcher在Vue中完全是多余的存在。它的缺点很多，优点几乎没有。
先说优点，优点就是写代码快。不需要逻辑，什么都是Watch就行了。比如，我在我们合同工的代码中看到很多Watcher，这对于快速开发确实是优点。因为不需要过多考虑逻辑，只要值变了，就执行函数就行了。
至于缺点有很多：</p>
<ul>
<li><code>错误的暗示</code>一个Watcher自带暗示：被Watch的变量可以被任何东西改变，换句话说你不知道这个值将会被什么改变。这在维护的时候非常麻烦，你要经常通读代码来判断如何修改相关的业务。
<strong>如何解决？</strong> 去掉Watcher，用<code>v-if</code>控制组件载入并在子组件的Created()钩子内处理相关业务。另外要善用Computed，善用emit派发event来改变值。这样数据流比较清晰。总之尽量做到每个值的改变都有迹可循。</li>
<li><code>混乱嵌套的Watcher</code>只要多用Watcher就能创造更多Bug，听起来像一个优点，对程序员来说可以多创建点Bug ticket。这种代码是这么写的，先Watch A,再Watch B并且在修改B的时候顺便修改一下A的属性，然后在修改A的时候顺便在修改一下B的属性，最好再修改一个八杆子打不着的变量C，然后再Watch下C再改一下其它值。还不够完美，在滥用Wather这方面有人肯定能比我写的专业。</li>
<li><code>难于测试</code>对，就是在写测试的时候会遇到很多困难，有时候Watcher在测试内是不能被激活的。这里不再赘述。当然如果你不写测试程序就没有这个问题。</li>
</ul>
<h5 data-id="heading-2">2. 禁用Vuex</h5>
<p>Vuex， 又是一个生造出来的东西。什么<code>大项目用，中小项目不用之类的说法都是错误</code>的。不懂的人最喜欢这个忽悠，你细问他有说不出个所以然来。我的结论是<code>什么代码都不要用</code>。
这个东西是过度设计以及设计错误。为什么这么说，一旦你使用Vuex了，就代表你的组件<strong>设计</strong>一定出了问题。当然这么一顿批评它的缺点到底在哪里呢？</p>
<ul>
<li><code>逻辑混乱</code> 有人肯定说这东西用好了就怎么怎么样，用不好才会怎么怎么样。错，我告诉你这东西没法用好，不要用。随着代码量的增加Vuex会使你的代码逻辑变得非常混乱。这个Vuex就是一个全局变量，而且满天飞。维护的时候要花很多时间，尤其是多个程序员维护一份代码，自己搞自己的，过了一段时间代码就会变得没法看。而且没人敢乱改，一改可能就全塌了。</li>
<li><code>难于测试</code> 写测试的时候要引入更多多余的mock。而且有些在Vuex里面触发的事件根本无法测试导致你无法写出正确的测试。如果你在测试内派发事件，那么这个测试就是无效测试。因为你的代码逻辑改了测试还是能够通过。</li>
</ul>
<h5 data-id="heading-3">3. 禁用Mixin</h5>
<p>Mixin又有什么问题？
Mixin最大的问题就是带来代码的逻辑混乱。使用了Mixin的代码维护更加困难，还<code>不如export函数易于阅读</code>。
如果是mix组件的hook那将是个灾难。
我觉得Mixin只有一个时候可以用用就是多组件共用同一个Prop的时候。其它时候真的可以不用了。</p>
<h5 data-id="heading-4">4. 尽量不要在HTML内用Form tag</h5>
<p>会引起错误的提交并且导致Vue地址栏胡乱添加问号。</p>
<h5 data-id="heading-5">5. 多用Computed计算属性</h5>
<p>这里的多用意思是，你觉得不能用的时候也要想办法用。
Computed属性有很多优点。它就像一个只读变量（如果我们不用setter的话）。计算属性的存在给Vue程序员减少了很多心智负担。你会发现有时候可以把变量放入Data()，似乎用计算属性也行。那么首选计算属性。</p>
<p>老生常谈的跟别人一样的部分我就尽量不提了，没意思。先写这么多，回头再添加。</p></div>  
</div>
            