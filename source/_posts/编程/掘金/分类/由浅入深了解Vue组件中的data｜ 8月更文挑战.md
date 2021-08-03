
---
title: '由浅入深了解Vue组件中的data｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9747'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 07:01:53 GMT
thumbnail: 'https://picsum.photos/400/300?random=9747'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>我们先参考vue官网给出的解释：</p>
<p><strong>一个组件的 <code>data</code> 选项必须是一个函数</strong>，<strong>使得每个实例可以维护一份被返回对象的独立的拷贝</strong></p>
</blockquote>
<p>首先，我们先看一个简单的原型链有关知识。</p>
<pre><code class="copyable">`function VueComponent()&#123;&#125; 

VueComponent.prototype.$options = &#123; 
        data:&#123;
                name:'zf',
        &#125;
&#125;

let vc1 = new VueComponent()

vc1.$options.data = 'lx'

let vc2 = new VueComponent() 

console.log(vc2.$options.data)` 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到，实例对象VC1修改了name的值为“lx”,新的实例对象VC2访问到的值也是修改后的“lx”。</p>
<p>这是因为VC1和VC2两个实例对象在操作$options时是在操作VueComponent构造函数原型对象上的属性，<strong>实例对象的隐式原型属性等于其构造函数的显示原型属性，所以它们指向的是同一块内存空间。</strong>
这导致了两个对象数据不独立，会相互污染。</p>
<p>根据以上结果，再回到我们Vue组件中的data属性。</p>
<p><em>同一个组件被复用多次，会创建多个实例。这些实例用的是同一个构造函数，如果 data 是一个对象的话，那么所有组件都共享了同一个对象。为了保证组件的数据独立性要求每个组件必须通过 data 函数返回一个对象作为组件的状态。</em></p>
<p><code>core/global-api/extend.js line:33</code></p>
<pre><code class="copyable">Sub.options = mergeOptions(Super.options, extendOptions)

function mergeOptions() &#123;
        function mergeField(key) &#123;
                const strat = strats[key] || defaultStrat options[key] = strat(parent[key], child[key], vm, key)
        &#125;
&#125;
strats.data = function(parentVal: any, childVal: any, vm ? : Component

): ? Function &#123;
        if (!vm) &#123; // 合并是会判断子类的data必须是一个函数 
                if (childVal && typeof childVal !== 'function') &#123;
                        process.env.NODE_ENV !== 'production' && warn('The "data" option should be a function ' +
                                'that returns a per-instance value in component ' + 'definitions.', vm) return parentVal
                &#125;
                return mergeDataOrFn(parentVal, childVal)
        &#125;
        return mergeDataOrFn(parentVal, childVal, vm)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-0">总结：</h5>
<p>一个组件被使用多次，用的都是同一个构造函数。为了保证组件的不同的实例data不冲突，组件中的数据相互
独立，要求data必须是一个函数，这样组件间不会相互影响。</p></div>  
</div>
            