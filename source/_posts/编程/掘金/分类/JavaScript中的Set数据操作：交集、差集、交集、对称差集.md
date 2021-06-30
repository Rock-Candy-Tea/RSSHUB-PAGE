
---
title: 'JavaScript中的Set数据操作：交集、差集、交集、对称差集'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5866'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 05:36:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=5866'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>【这是我参与更文挑战的第 <strong>30</strong> 天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>”】</p>
<p>在许多情况下，需要比较多个列表，获取它们有或没有交集、差集等等，在 Javascript 有一个数据类型可以很好的实现这些需求，那就是 <code>Set</code> 。</p>
<p><code>Set</code>对象就像一个数组，但是仅包含唯一项。<code>Set</code>对象是值的集合，可以按照插入的顺序迭代它的元素。 <code>Set</code>中的元素只会出现一次，即 <code>Set</code> 中的元素是唯一的。是用来合并数组并去重的好方法，在文章《<a href="https://juejin.cn/post/6972337499850932238#heading-10" target="_blank">Vue开发中可以使用的ES6特征</a>》有简单提到。</p>
<p>文章涉及的代码地址：<a href="https://codepen.io/quintiontang/pen/rNmNbbY" target="_blank" rel="nofollow noopener noreferrer">codepen.io/quintiontan…</a></p>
<h3 data-id="heading-0">什么是 <code>Set</code></h3>
<p><code>Set</code> 对象是值的集合，可以按照插入的顺序迭代它的元素，元素只会出现一次，即 <code>Set</code>  是不按特定顺序存储的且值唯一的集合。与堆栈、队列和数组等其他集合类型不同，Set 可用于列表比较，并用于检测集合中是否存在某个项。</p>
<p><code>Set</code> 是一种抽象数据类型，它是由其行为定义的，类似堆栈和队列数据结构。由于<code>key-key</code>的特性，这一点与 <code>Map</code> 类似，详情可以参阅《<a href="https://juejin.cn/post/6955323411916652552" target="_blank">ECMAScript 6的Map映射</a>》。</p>
<h3 data-id="heading-1">Javascript <code>Set</code></h3>
<p>Javascript 中的 <code>Set</code> 是非常基础和简单的，它不像其他语言那样提供通用的集操作功能。它使用了一种独特的算法（不是基于严格的相等 <code>===</code> ）来检测元素是否相同。</p>
<p>这意味着在集合中存储 <code>undefined</code>、<code>null</code> 和 <code>NaN</code> 将只会存储一次，即使是 <code>NaN !== NaN</code> ，它通常应用于对象类型的存储。</p>
<pre><code class="copyable">const setTest = new Set([0, -0, Infinity,null, undefined, null, NaN, NaN, Infinity,null]);
console.log(setTest);  // Set &#123; 0, Infinity, null, undefined, NaN &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的执行结果可以得出以下结论：</p>
<ul>
<li>虽然 <code>NaN</code> 和 <code>NaN</code> 不相等，但是在 <code>Set</code> 集合里面只会存在一个</li>
<li><code>undefined</code> 和 <code>Infinity</code> 在 <code>Set</code> 集合里面只会存在一个</li>
</ul>
<p>基本 Set 的使用本文就不介绍了，可以参阅 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Set" target="_blank" rel="nofollow noopener noreferrer">mozilla</a> 网站。</p>
<h3 data-id="heading-2">什么时候使用 <code>Set</code></h3>
<p>当需要对特定列表执行比较和判断是否相等时，可以使用 <code>Set</code>，下面大家描述一下适用的场合，主要就是数据里的集合操作：</p>
<ul>
<li>获取两个集合的并集 <code>union</code></li>
<li>获取两个集合的差集 <code>difference</code></li>
<li>获取两个集合的交集 <code>intersection</code></li>
<li>获取两个集合的对称差集 <code>intersectionDifference</code></li>
<li>判断两个集合是否为子集 <code>isSubset</code></li>
<li>判断两个集合是否为超集 <code>isSuperset</code></li>
</ul>
<p>下面就以这三个场合来介绍 <code>Set</code> 的相关操作。</p>
<h3 data-id="heading-3"><code>Set</code> 操作</h3>
<p>在数学中，每当谈论集合时，都可以执行一些操作，实际上，<code>Set</code> 是数学有限集的计算机实现方式。</p>
<p>为了在代码中更好的展示 <code>Set</code> 操作，示例代码将 扩展 Javascript <code>Set</code> 以继承其属性和方法，并为其增加其它的方法。</p>
<blockquote>
<p>对于示例代码，只用了一个简单的方法来检查是否为不为空的有效的集合。</p>
</blockquote>
<pre><code class="copyable">class SetHelper extends Set &#123;
    /**
     * 验证集合是否为有效集合
     * @param &#123;*&#125; set
     * @returns
     */
    _isValid = (set) => &#123;
        return set && set instanceof Set && set.size > 0;
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">并集 <code>union</code></h4>
<p><code>union</code> 操作将合并多个 <code>Set</code> 对象并返回合并后的结果。实现上将当前集和给定集合并到一个数组中并创建它，从而返回一个新的集合。</p>
<pre><code class="copyable">union(set) &#123;
    if (!this._isValid(set)) return new SetHelper();
    return new SetHelper([...this, ...set]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">差集 <code>difference</code></h4>
<p><code>difference</code> 操作将返回一个新的集合，新集合只包含在一个集合中并且不在另一个集合中的元素，即数学的差集概念。</p>
<pre><code class="copyable">difference(set) &#123;
    if (!this._isValid(set)) return new SetHelper();
    const differenceSet = new SetHelper();
    this.forEach((item) => &#123;
        !set.has(item) && differenceSet.add(item);
    &#125;);
    return differenceSet;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">交集 <code>intersection</code></h4>
<p><code>intersection</code> 操作返回只包含两个集合共同拥有的元素的新集合。实现上将遍历较小的集合（避免不必要的检查）并检查每一项是否存在于较大的集合中并将其添加到交集中，遍历完成后将返回交集。</p>
<pre><code class="copyable">intersection(set) &#123;
    const intersectionSet = new SetHelper();
    if (!this._isValid(set)) return intersectionSet;
    const [smallerSet, biggerSet] =
        set.size <= this.size ? [set, this] : [this, set];
    smallerSet.forEach((item) => &#123;
        biggerSet.has(item) && intersectionSet.add(item);
    &#125;);
    return intersectionSet;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">对称差集 <code>intersectionDifference</code></h4>
<p><code>intersectionDifference</code> 操作将返回其中包含两个集合没有交集的所有元素的新集合。</p>
<pre><code class="copyable">intersectionDifference(set) &#123;
    if (!this._isValid(set)) return new SetHelper();
    return new SetHelper([
        ...this.difference(set),
        ...set.difference(this),
    ]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">子集 <code>subset</code></h4>
<p><code>isSubset</code> 操作将判断两个集合是否为子集关系（当一个集合的所有项都包含在另一个集合中时）。实现上首先检查两个集合的大小，如果一个集合更大，则它不能是另一个集合的子集，然后对于每个项目，它检查它是否存在于另一个中。</p>
<pre><code class="copyable">isSubset(set) &#123;
    if (!this._isValidSet(set)) return false;
    return (
        this.size <= set.size && [...this].every((item) => set.has(item))
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">超集 <code>superset</code></h4>
<p><code>isSuperset</code> 操作将判断两个集合是否为超集关系。超集是子集的反操作。当一个集合包含另一个较小或相等大小的集合的所有项目时，它就是一个超集。</p>
<pre><code class="copyable">isSuperset(set) &#123;
    if (!this._isValidSet(set)) return false;
    return (
        this.size >= set.size && [...set].every((item) => this.has(item))
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">静态 <code>Set</code></h3>
<p>静态<code>Set</code> 是一个始终包含它初始化元素的集合，不能添加、删除、清除元素。Javascript <code>Set</code> 不是静态的，它总能在创建后可以公开修改该集合的方法，如 <code>add</code>、<code>delete</code> ，为避免集合被修改，可以创建一个新的 <code>Set</code> ，将其修改方法重置 。</p>
<pre><code class="copyable">class StaticSet extends SetHelper &#123;
    constructor(items) &#123;
        super(items);

        this.add = undefined;
        this.delete = undefined;
        this.clear = undefined;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">使用</h3>
<p>现在就可以使用上面定义的方法操作两个 <code>Set</code>，如下：</p>
<pre><code class="copyable">const setA = new StaticSet(new Set([1, 2, 3, 4]));
const setB = new StaticSet(new Set([3, 4, 5, 6]));
console.log([...setA.union(setB)]); // [ 1, 2, 3, 4, 5, 6 ]
console.log([...setA.difference(setB)]); // [ 1, 2 ]
console.log([...setA.intersection(setB)]); // [ 3, 4 ]
console.log([...setB.intersectionDifference(setA)]); // [ 5, 6, 1, 2 ]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">总结</h3>
<p><code>Set</code> 不限于上面这些操作，之前有介绍过可以用来合并数组去重，由于 <code>Set</code> 和 <code>Array</code> 相互转换很简单，因此可以用到 <code>Array</code> 的场合可以优先考虑一下 <code>Set</code> ，因为在内存使用上， <code>Set</code> 比 <code>Array</code> 占用更少。</p></div>  
</div>
            